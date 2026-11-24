# Research digest · 2026-11-24
<!-- {% raw %} -->

New papers posted from about 2026-11-23 to 2026-11-24 (UTC).

> Papers are picked by how closely their wording matches each topic's description (the "relevance" score), not by quality. Summaries are written by AI from the abstract only; open the paper before relying on them.

## Highlights

- **[The Order of the Inertia Bound for Random Graphs](https://arxiv.org/abs/2611.27000)** (Combinatorics): The paper proves a Hermitian version of the Kwan–Wigderson conjecture for random graphs G(n,1/2), showing that the minimum number of nonnegative eigenvalues of zero-diagonal Hermitian matrices supported on G is order n/log n, and it gives related bounds using Alon's constructions with independence number 2 and Shannon capacity 3.</one_liner>
<parameter name="plain">The paper studies how few "nonnegative" eigenvalues a matrix can have when its nonzero entries are only allowed where a given network has edges. For a typical random network with n points, where each pair is linked with probability one half, the authors show this minimum is at least a constant times n divided by log n, with very high probability. They also build specific graphs where the same quantity is larger than a small power of n.
- **[Detection of genuine multipartite entanglement by means of entanglement monotones](https://arxiv.org/abs/2611.27660)** (Quantum information and computing): The paper studies how to measure whether several quantum particles are entangled in a truly joint way, not just in pairs or as a product of smaller linked groups. The authors first show that one natural way of scoring this cannot satisfy two desirable rules at once. They then relax one rule and build a simple method for producing scores that do work, and report that a subset of these scores detects every form of genuine three-particle entanglement in three-qubit systems.
- **[Cyclic perturbations encode memories in trained neural networks without loss of performance](https://arxiv.org/abs/2611.27647)** (Statistical physics): Some physical materials, such as certain disordered solids and suspensions, remember how they were repeatedly nudged back and forth. This paper asks whether a trained artificial neural network can do the same. The authors repeatedly shake all of the network's weights (its adjustable numbers), let it settle back through training, and find that the size of the shake can be read back out later.

## Probability

### [A Stochastic Tamed-Regularized Random Batch Method for Uncertain Particle Systems with Singularities](https://arxiv.org/abs/2611.26946)
*Wenyi Wang, Lei Li, Yiwen Lin* · `math.NA` · arXiv:2611.26946v1 · relevance 0.16

- **In one sentence**: The paper proposes a stochastic tamed-regularized random batch (str-RB) scheme that combines an exponential regularization of singular diffusion coefficients, stochastic Galerkin projection for random coefficients, and random batch sampling to simulate uncertain interacting particle systems with singularities.
- **In plain words**: Many models describe large groups of interacting particles whose rules are only partly known, and some of the forces or noise strengths blow up when particles get close. Standard numerical solvers can produce runaway, meaningless values in these cases. The authors modify the calculation by smoothing the singular noise term with an exponential regularization and by computing only random subsets of particle interactions at each step to save work.
- **Why it matters**: The text reports that the method shows weak convergence, lower errors than several major existing methods on singular test cases, and stability over a wider range of singular settings, which matters for simulating uncertain many-body dynamics. The text does not give details of the test systems, so the size of the improvement and its relevance to particular applications are unclear from this summary alone.
- **Background needed**: - Particle system: many interacting objects (particles) whose motion depends on pairwise forces, here with random noise.
- Drift and diffusion: the deterministic push and the random-noise strength in a stochastic differential equation.
- Singularity: a point where a coefficient becomes infinite, e.g. when two particles nearly coincide.
- Numerical blow-up: a simulation producing unbounded, unphysical values.
- Taming / regularization: modifying a singular term so it stays finite while keeping the main behaviour.
- Stochastic Galerkin (sG) method: representing randomness in model coefficients as a series of known basis functions.
- Random batch method: updating only a small random subset of pairwise interactions per step to cut computing cost.
- Weak convergence: the accuracy of statistics (averages) of the solution, not of individual random paths. · level: research-level

<details><summary>Original abstract</summary>

The coefficients of particle systems often exhibit uncertainties due to incomplete knowledge. For particle systems with uncertainties and singularities in the drift and diffusion terms, existing methods may encounter numerical blow-up. In this paper, we propose a novel stochastic tamed-regularized Random Batch (str-RB) method for such uncertain particle systems with singularities. Specifically, since singularities in the diffusion term are more challenging than those in the drift term, building on a tamed scheme, we design an exponential regularization strategy that more effectively mitigates singularities in the diffusion term. This strategy ensures that the stochastic Galerkin (sG) projection coefficients remain finite even when the corresponding integrals for the original singular diffusion coefficient diverge. The sG method is applied to handle the random coefficients, and a random batch approach is then employed to reduce the computational complexity of large-scale simulations. Several theoretical properties of the proposed algorithm are established. Numerical tests demonstrate that the str-RB algorithm exhibits weak convergence, achieves lower errors than major existing methods across singular tests, and remains stable in a wider range of singular regimes. This work provides a robust and accurate approach for uncertain particle systems with singularities, laying a foundation for high-performance solvers in uncertain many-body dynamics.

</details>

### [How communities help epidemics persist](https://arxiv.org/abs/2611.27843)
*J\'ulia Komj\'athy, Marco Seiler, Daniel Valesin* · `math.PR` · arXiv:2611.27843v1 · relevance 0.15

- **In one sentence**: The paper studies the contact process (SIS epidemic model) on random intersection graphs and their local weak limit, a tree of overlapping complete-graph communities, and gives survival-versus-extinction criteria based on the tails of the membership and community-size distributions.
- **In plain words**: This paper asks how infections spread through a population whose contacts happen inside overlapping groups such as households and workplaces. The authors model each person as belonging to a random number of groups, each group having a random size, and everyone in a group being in contact with everyone else. They show that whether an infection dies out or lingers depends on how heavy the tails of those group-count and group-size distributions are: when the tails are heavy, the infection persists for a very long time with high probability, while under certain lighter-tail conditions and a small transmission rate it dies out in the limiting tree-like model.
- **Why it matters**: Empirical studies cited in the paper indicate that community structure strongly affects how long infections last, so a mathematical account of this effect is relevant to disease modelling. The paper's comparison with "community-free" random graphs with similar degree patterns is meant to isolate the role of communities; the text does not claim direct applications beyond this.
- **Background needed**: - Contact process (SIS model): individuals are either infected or healthy; infected ones recover at rate 1 and infect each neighbour at rate lambda, and can be reinfected.
- Survival vs. extinction: whether the infection persists forever or dies out; "exponentially long" survival means the time to die out grows exponentially with population size.
- Random graph: a network generated by a random rule; a random intersection graph links people who share a group.
- Complete graph: a group where every member is connected to every other member.
- Local weak limit: the tree-like picture of what a typical neighbourhood in a very large random network looks like.
- Moment generating function / exponential moments (E[e^{cM}]): a measure of how heavy the upper tail of a random quantity is. · level: research-level

<details><summary>Original abstract</summary>

Empirical studies show that communities such as households and workplaces strongly influence how an infection spreads and how long it persists in a population. To understand this effect, we study the contact process (SIS epidemic model) on random intersection graphs and their local weak limit. In the contact process, infected vertices recover with rate $1$ and transmit the infection to each of their neighbours with rate $\lambda$. The random intersection graph is defined on a finite population; each individual belongs to a random number of communities (captured by a membership distribution), and each community has a random size (captured by a community size distribution). Communities are all taken to be complete graphs. The local weak limit of the random intersection graph, called the branching community tree, has complete graphs arranged in a tree structure. Letting $M$ have the membership distribution and $K$ have the community size distribution, we prove that if either $\mathbb E[e^{cM}]=\infty$ for all $c > 0$ or $\mathbb E[e^{cK\log K}] = \infty$ for all $c > 0$, then for all $\lambda > 0$, the infection on the finite graph survives for exponentially long with high probability, and on the local limit graph, it survives forever with positive probability. On the other hand, if for some $c > 0$ both $\mathbb E[e^{cM}]<\infty$ and $\mathbb E[e^{K\log(cK)}]<\infty$ hold, then the process with small $\lambda$ dies out in the local limit graph. We compare these findings with known results on the behaviour of the contact process on a "community-free" random graph with similar degree distributions, to highlight the impact of communities.

</details>

## Differential geometry

### [Riemannian Curvature Functionals for de Rham Spectral Triples](https://arxiv.org/abs/2611.27776)
*Yong Wang* · `math.DG` · arXiv:2611.27776v1 · relevance 0.10

- **In one sentence**: The paper builds curvature functionals (Riemann and Einstein tensors) from mixed Clifford residues of the Hodge-de Rham operator in even dimensions, and examines their boundary behaviour, extensions to two one-form actions, and failure cases on noncommutative tori, finite-direction examples and a conformal example.
- **In plain words**: The paper asks whether the curvature of a space (how much it bends, the quantity Einstein used for gravity) can be recovered from a purely algebraic setup built on the operator that describes differential forms on the space. The authors compute several such "curvature functionals" and check them on special cases, including spaces with boundaries. They also report where the recipe breaks: some versions fail to respect the usual symmetry rules for curvature, and a naive extension does not recover the classical curvature.
- **Why it matters**: It connects noncommutative geometry, where spaces are described by algebras of operators, with classical Riemannian curvature, which is a useful test of whether that framework captures geometry correctly. The text states its limitations explicitly, so the value lies partly in the clearly mapped failure cases; the wider significance beyond this setting is not established by the text.
- **Background needed**: - Riemannian manifold: a smooth curved space in which distances and angles are defined locally.
- Curvature (Riemann and Einstein tensors): standard measures of how a space bends; the Einstein tensor is a contraction of the Riemann tensor.
- Differential forms and the Hodge-de Rham operator: generalised "areas and volumes" on a space and the operator that acts on them.
- Clifford algebra: an algebra that encodes directions and their products, used here to build symbols of operators.
- Spectral triple: a noncommutative-geometry package (algebra, Hilbert space, operator) that encodes a space algebraically.
- Residue functional: a linear functional extracting a coefficient from the asymptotic expansion of an operator's zeta or heat-type data.
- Noncommutative torus: a standard example of a noncommutative space; finite-direction examples are simpler toy models.
- Manifold with boundary and warped collar: a space with an edge, and a specific product-like neighbourhood of that edge. · level: research-level

<details><summary>Original abstract</summary>

We compute mixed Clifford residue functionals for the Hodge-de Rham operator in even dimensions. A symbol-composition calculation recovers the Riemann and Einstein tensors and yields two ordered curvature functionals with the same classical limit. For specified truncation products on warped collars, we evaluate all five boundary cases and prove that the curvature-recovering antisymmetrizations have no boundary correction. We extend the constructions to spectral data equipped with two one-form actions. Explicit noncommutative torus and finite-direction examples distinguish the functionals and exhibit failures of module balancing and Riemann symmetries. A conformal example shows that a naive exterior lift need not recover classical curvature. The additional structures and limitations of each extension are stated explicitly.

</details>

### [Yau's pinching problem and vanishing of Betti numbers](https://arxiv.org/abs/2611.27950)
*Xiaolong Li, Elham Matinpour, Peter Petersen* · `math.DG` · arXiv:2611.27950v1 · relevance 0.10

- **In one sentence**: Under a pinching condition relating sectional curvature to scalar curvature (sec > Scal/(n(n+2))), closed Riemannian n-manifolds with n ≥ 4 are shown to have vanishing real cohomology in degrees 1 through n-1, with rigidity results for the weak inequality and intermediate Ricci variants.</one_liner>
<parameter name="plain">This paper studies closed curved shapes of dimension four or higher and asks when their curvature, measured in two ways, forces them to have no "holes" of the usual topological kinds. The authors show that a specific curvature inequality (a version of Yau's pinching condition) forces the relevant topological counts, called Betti numbers, to vanish in most degrees. The complex projective space is used to show the constant in the inequality cannot be improved and the strict inequality is needed in even dimensions.
- **Why it matters**: It settles a sharp, decades-old style question about how curvature controls topology, and the rigidity result (only a quotient of complex projective space escapes the conclusion) gives a clear classification-type statement. Its wider connections are to the sphere theorem and to Hodge theory, but the text itself does not say how far these tools reach beyond the stated cases.
- **Background needed**: - Riemannian manifold: a smooth space with a way of measuring lengths and angles, so it has a notion of curvature.
- Sectional curvature: curvature measured on each two-dimensional plane through a point; scalar curvature is a single averaged number at each point.
- Pinching condition: an inequality bounding one curvature quantity by a fraction of another, which constrains the shape of the space.
- Betti numbers: counts of independent "holes" of each dimension in a space, computed with real coefficients here.
- Rational homology sphere: a space whose topology looks like a sphere when counted with rational numbers.
- Hodge theory and Weitzenböck formula: tools linking harmonic forms (smooth generalized "fields" on the space) to curvature.
- Complex projective space with Fubini-Study metric: a standard highly symmetric example of a curved space. · level: research-level

<details><summary>Original abstract</summary>

We prove that a closed connected Riemannian $n$-manifold, $n\geq4$, satisfying $\sec>\frac{\operatorname{Scal}}{n(n+2)}$ at every point has vanishing real cohomology in degrees $1,..., n-1$. It is consequently a rational homology sphere if $n$ is odd or the manifold is orientable. Complex projective space shows that the coefficient is optimal and that the strict inequality is necessary in every even dimension. The required estimate for the Weitzenb\"ock curvature term is established by integrating restricted Ricci operators over orthonormal frames and combining complementary degrees using Hodge duality. This also allows us to replace sectional curvature pinching by intermediate Ricci curvature bounds. For a nonflat metric, the weak Yau inequality, $\sec\geq\frac{\operatorname{Scal}}{n(n+2)}$, gives the same cohomology vanishing unless the manifold is isometric, up to scaling, to a quotient of complex projective space with its Fubini-Study metric. This also holds using the second intermediate Ricci curvature in place of sectional curvature. More generally, a nonzero Betti number in the range controlled by an intermediate Ricci bound forces local symmetry. We also derive sharp Hodge eigenvalue estimates and a scalar spectral vanishing criterion.

</details>

## Partial differential equations

### [Growth of subsolutions to fully nonlinear equations in halfspaces II](https://arxiv.org/abs/2611.27902)
*Fatma Gamze D\"uzg\"un, Niklas L. P. Lundstr\"om, Marcus Olofsson* · `math.AP` · arXiv:2611.27902v1 · relevance 0.14

- **In one sentence**: The paper proves sharp lower growth bounds for subsolutions of fully nonlinear elliptic equations posed in half-spaces, where the source term may depend on the solution itself, covering both growth at infinity and blow-up at a finite distance from the boundary, by extending an earlier ODE-based method.
- **In plain words**: This paper studies how certain functions that satisfy a type of mathematical inequality must grow when they live on one side of a flat boundary, such as a half-space. The authors show that these functions cannot stay small: they must grow at least at a certain rate far away, and they can blow up when approaching a finite distance from the boundary. The work extends a method that uses ordinary differential equations, a technique from an earlier paper by the same line of research.
- **Why it matters**: Estimates like these are the kind of tool used to rule out or classify solutions to nonlinear equations, which matter across geometry and physics models. The text is short and does not state specific applications, so any wider connection is uncertain from this description alone.
- **Background needed**: - Elliptic partial differential equations: equations describing steady states, such as heat or potential distributions, where a function's value depends on its surroundings.
- Subsolution: a function that satisfies an inequality version of the equation, roughly "at most as curved as needed" in a certain sense.
- Fully nonlinear: the equation depends non-linearly on the second derivatives (how the function bends), not just linearly.
- Half-space: the region on one side of a flat plane, used as a simple model domain with a boundary.
- Growth estimate: a guaranteed lower bound on how fast a function must increase, often used to show solutions cannot be too small.
- Blow-up: the function becomes unboundedly large at a finite location.
- ODE method: reducing the problem to an ordinary differential equation in one variable to derive the bounds. · level: research-level

<details><summary>Original abstract</summary>

We establish sharp lower growth estimates for subsolutions of fully nonlinear elliptic equations in half-spaces, allowing source terms that depend explicitly on the solution. The estimates capture both growth at infinity and blow-up at a finite distance from the boundary. Our approach extends the ODE-based method introduced in [J. Differential Equations 320 (2022), 143--173].

</details>

### [Almost-sure quenched KAM tori for nonlinear wave equations with a spatial white-noise potential](https://arxiv.org/abs/2611.26634)
*Yingdu Dong, Wenwen Jian, Xiaoping Yuan* · `math.AP` · arXiv:2611.26634v1 · relevance 0.12

- **In one sentence**: Constructs, for almost every path of a white-noise spatial potential, a Cantor family of small-amplitude invariant tori for a nonlinear wave equation with a random Schrödinger operator, via a partial Birkhoff normal form up to degree ten.
- **In plain words**: The paper studies a vibrating string whose stiffness varies randomly from point to point, modeled as white noise, and which also has a cubic-type nonlinearity. It shows that, for almost every realization of that randomness, the string's frequencies avoid a certain set of integer coincidences. Under that condition, it builds many quasi-periodic vibration patterns (invariant tori) that persist as small-amplitude motions.
- **Why it matters**: Persistent quasi-periodic motions in random media are hard to establish because the randomness can destroy the resonance structure that classical methods rely on. The result is a rigorous statement that such motions survive for almost every noise path, which may be of interest to researchers in KAM theory and random operators; the text does not discuss applications beyond this.
- **Background needed**: - A wave equation u_tt + A u + f(u) = 0 describes vibrations; here A is a random operator (a second-derivative operator plus a noisy potential).
- White noise is a random signal with no smooth structure; Brownian motion B is its integral, and its derivative is taken in a distributional (generalized) sense.
- Eigenvalues/frequencies: the natural vibration rates of the operator; integer relations among them are "resonances" that can spoil persistence of motion.
- Birkhoff normal form: a change of variables that simplifies a nonlinear Hamiltonian system so its long-term behavior is easier to read off.
- KAM theory: a framework showing that most quasi-periodic motions survive small perturbations; invariant tori are the resulting closed quasi-periodic orbits.
- Cantor family: a parameter set with many gaps but whose measure approaches full as the amplitude parameter goes to zero.
- Normally elliptic vs. hyperbolic directions describe whether nearby motions stay bounded or drift apart. · level: research-level

<details><summary>Original abstract</summary>

Let \[ A_\omega=-\partial_x^2+\rho\,\partial_xB(x,\omega), \qquad \rho\ne0, \] be the Dirichlet Schr\"odinger operator on $(0,\pi)$ with a spatial Gaussian white-noise potential, realized pathwise via quasi-derivatives. Here $B$ is Brownian motion in the spatial variable $x$, and $\partial_xB$ denotes its distributional derivative. We consider the nonlinear wave equation \[ u_{tt}+A_\omega u+f(u)=0, \] where $f$ is odd and real analytic near zero, with $f(u)=\kappa u^3+O(u^5)$ and $\kappa\ne0$. We show that, on a single event of probability one, no nontrivial finitely supported integer combination of the positive wave frequencies is an integer, and the quartic twist matrix is nonsingular for every finite tangential set of positive modes. After fixing a path in this event, we construct a partial Birkhoff normal form of the Hamiltonian up to degree ten. For every finite nonempty tangential set $J$ of cardinality $b$ associated with positive eigenvalues, we obtain a Cantor family of real-analytic, small-amplitude invariant $b$-tori in $H^1_0(0,\pi;\mathbb{R})\times L^2(0,\pi;\mathbb{R})$. The family is parametrized by a Cantor subset of $[\nu,2\nu]^b$ whose relative measure tends to one as $\nu\to0$. The tori are normally elliptic when $A_\omega$ is positive. Otherwise, they have $h$ stable and $h$ unstable normal directions, where $h$ is the number of negative eigenvalues of $A_\omega$.

</details>

## Harmonic analysis

### [Stable phase retrieval from operator measurements](https://arxiv.org/abs/2611.27085)
*Deanna Needell, Yaniv Plan, Tomasz Szczepanski et al.* · `math.FA` · arXiv:2611.27085v1 · relevance 0.10

- **In one sentence**: The paper studies stable phase retrieval from operator-valued quadratic measurements in Hilbert spaces, showing that stability fails for most exponents p in infinite dimensions, that p=4 admits stable examples built from rank-one or rank-two operators, and that stability can be tested on orthogonal pairs.
- **In plain words**: The problem is recovering a signal from measurements that lose its overall phase, such as measuring only the squared amplitudes of its components, while still requiring that small errors in the data cause only small errors in the reconstruction. The paper shows that in infinitely many dimensions this kind of stable recovery is impossible for most measurement settings, with one exponent (p = 4) as the exception. It then constructs specific measurement systems that work in that exceptional case and proves that, in finite dimensions, unique recovery automatically implies stable recovery.
- **Why it matters**: It extends a known negative result about frames to a broader class of measurements and identifies exactly where stability can still be achieved. The text mentions second-moment measurements in cryo-electron microscopy as motivation, but the text does not say how far the results carry over to that application.
- **Background needed**: - Phase retrieval: recovering a signal (up to a global phase factor) from measurements that discard phase information.
- Hilbert space: a generalized space of vectors, possibly infinite-dimensional, with lengths and angles.
- Frame and Bessel system: a family of vectors (or operators) whose measurements are controlled in size; a p-Bessel system bounds the measurements in a chosen norm.
- Stability: small changes in the measured data cause only small changes in the recovered signal.
- Rank-one and rank-two operators: simple linear maps with image of dimension one or two; self-adjoint means the operator equals its own conjugate transpose.
- Cryo-EM: an imaging technique that reconstructs 3D molecular structures from noisy 2D projections. · level: research-level

<details><summary>Original abstract</summary>

A known result of Cahill, Casazza and Daubechies [Trans. Amer. Math. Soc. Ser. B3(2016), 63-76] states that no frame in an infinite-dimensional Hilbert space does stable phase retrieval. We show that stable recovery becomes possible for more general operator measurements, but only at a single exponent. Given a system of bounded operators $\{A_j\}_{j\in J}$ on a real or complex Hilbert space $H$, we study recovery of $f\in H$ up to a global phase from the quadratic measurements $\langle A_j f,f\rangle$ and from their phase preserving square roots. We consider $p$-Bessel systems ($2\leq p<\infty$) for which we measure the quadratic data in $\ell_{p/2}$ and the square root data in $\ell_p$. In infinite dimensions, we show that whenever $p\neq 4$, no $p$-Bessel system of operators does stable phase retrieval. In the case of $p=4$, we show that stability still fails on any system of semidefinite operators. Nevertheless, we construct a system of rank-one operators, not all self-adjoint, for which stable recovery is possible. We also show that stability can be achieved on a system of self-adjoint operators of rank-two. For both types of measurements, we show that the stability can be tested on orthogonal pairs. This reduction preserves the optimal constant for quadratic measurements and, when the operators are semidefinite, for their phase preserving square roots. We deduce that in finite dimensions, uniqueness of recovery implies its stability. Finally, we show that whenever only the moduli of the measurements are retained, both the orthogonal reduction and the implication from uniqueness to stability can fail, already in dimension two. We also give second moment measurements in cryo-electron microscopy (cryo-EM) as a motivation for the quadratic model.

</details>

### [A rigorous Abel-summed Hardy-type identity for $p$-circle domains via regularized Poisson summation](https://arxiv.org/abs/2611.26769)
*Masaya Kitajima* · `math.CA` · arXiv:2611.26769v1 · relevance 0.08

- **In one sentence**: The paper rigorously justifies, via an anisotropic Abel-type regularization of Poisson summation, a generalized Hardy-type identity for astroid-type p-circle domains, with boundary corrections (weight 1/2 at smooth points, vanishing cusp contributions for 0<p<1) and recovery of the classical p=2 Hardy–Voronoï Bessel series.
- **In plain words**: The paper studies a identity relating the counting of whole-number lattice points inside a certain shape (a "p-circle" with star-like corners) to a series of special functions. An earlier formal derivation left open whether the series is justified, so the authors smooth the counting with a damping kernel and take a limit. They find that smooth edge points contribute half weight, while the sharp corners contribute nothing when 0 < p < 1.
- **Why it matters**: It puts a previously heuristic lattice-point identity on rigorous footing and reduces to the known classical Hardy–Voronoï series when p=2, so it links to a well-studied area of number theory. The text does not say the unregularized series converges, which the authors flag as a separate open problem, so the practical reach is currently limited.
- **Background needed**: - Lattice points: integer coordinate points counted inside a region.
- Poisson summation: a standard tool relating sums over lattice points to sums over the Fourier transform of the region's indicator function.
- Abel summation: a way of assigning a finite value to a divergent or oscillating series by damping it with a parameter and taking a limit.
- p-circle: the set |x|^p + |y|^p ≤ 1; p=2 is an ordinary circle, and other p give squarish or star-like shapes (astroids for small p).
- Bessel functions: classical special functions that arise in wave and circle problems; the p-Bessel versions generalize them.
- Hardy–Voronoï identity: a classical formula for lattice points in a circle, expressed as a Bessel series.
- Cusp: a sharp corner of a boundary. · level: research-level

<details><summary>Original abstract</summary>

In our previous work, a generalized Hardy-type identity (GHI) for astroid-type $p$-circle domains was formally derived in terms of generalized $p$-Bessel functions. However, the direct application of the Poisson summation formula to the indicator functions of these domains leaves the convergence and rigorous justification of the resulting oscillatory series unresolved. In the present paper, we address this difficulty by introducing an anisotropic regularization based on convolution kernels with Fourier multipliers $e^{-t(|\xi_{1}|^p+|\xi_{2}|^{p})}$. We establish the corresponding regularized Poisson summation identity and rigorously justify the limiting process through uniform estimates for lattice-point sums. A key feature of our analysis is the determination of boundary contributions: smooth boundary points carry weight $1/2$, whereas the contributions from axial cusps vanish for $0<p<1$. These results lead to an Abel-summed GHI, expressed in terms of the distorted-angle-dependent $p$-Bessel functions introduced in our previous work, with explicit boundary corrections. In particular, for $p=2$, the identity recovers the Abel-summed form of the classical Hardy--Vorono\"i Bessel series. Our result provides a rigorous regularized counterpart of the previously proposed identity, while the convergence of the corresponding unregularized series remains a separate problem.

</details>

## Complex analysis

### [Weighted fixed-bidegree subelliptic estimates for the \(\overline{\partial}_f\)-Neumann problem on Lipschitz pseudoconvex domain](https://arxiv.org/abs/2611.27502)
*Ping'an Zhang* · `math.CV` · arXiv:2611.27502v1 · relevance 0.07

- **In one sentence**: The paper proves two types of a priori weighted subelliptic estimates, uniform in bidegree, for the twisted ∂̄_f-Neumann problem on bounded pseudoconvex domains with Lipschitz boundary satisfying an algebraic plurisubharmonic-type condition, with the twisting function holomorphic and having isolated critical points in the interior.
- **In plain words**: This paper is about a equation-solving problem in several complex variables, the kind that asks how smooth a solution must be when the domain has a rough, non-smooth edge. The authors prove estimates showing that solutions gain a limited amount of smoothness (a gain between 0 and 1/2) near the boundary, and that this holds consistently across the different types of forms involved. The result depends on a technical condition on how the boundary curves, and on a twisting function with controlled behavior.
- **Why it matters**: Estimates of this kind are the main tools for studying regularity of solutions to the ∂̄-Neumann problem, which connects complex geometry, partial differential equations and the theory of function spaces. The text does not say what specific applications follow, so beyond this field its wider significance is unclear from the text alone.
- **Background needed**: - Complex analysis in several variables: functions of several complex numbers, and domains in complex space.
- Pseudoconvexity: a geometric property of a domain's boundary, related to whether functions can be extended across it.
- Plurisubharmonic function: a generalized convex-type function in complex space; its Hessian (matrix of second derivatives) measures its curvature.
- ∂̄-Neumann problem: a boundary value problem for solving the complex analogue of the Cauchy-Riemann equations on a domain.
- Subelliptic estimate: an inequality showing solutions are smoother than the equation alone guarantees, with a loss or gain measured by an exponent.
- Lipschitz boundary: a boundary that is continuous and has bounded slope, but need not be smooth.
- Twisted (weighted) problem: the problem modified by a weight e^{-f}, here with f holomorphic.
- Bidegree: the type of differential form, indexed by how many holomorphic and antiholomorphic differentials it contains. · level: research-level

<details><summary>Original abstract</summary>

We establish two types of \emph{a priori} subelliptic estimates for the twisted \(\overline{\partial}_f\)-Neumann problem on a bounded pseudoconvex domain with Lipschitz boundary. The estimates feature a subelliptic gain in \((0, 1/2)\) and are uniform with respect to the bidegree. The boundary is assumed to satisfy a plurisubharmonic-type condition, characterized by the local existence, near each boundary point, of a bounded plurisubharmonic function whose Hessian blows up algebraically near the boundary, with potentially different exponents at different points. The twisting function is holomorphic in a neighborhood of the domain, has bounded gradient, and its critical set inside the domain consists of isolated interior points with finite vanishing orders.

</details>

### [The Thurston algorithm for general entire maps on the complex plane: Existence and uniqueness](https://arxiv.org/abs/2611.27925)
*Sebastian van Strien* · `math.DS` · arXiv:2611.27925v1 · relevance 0.05

- **In one sentence**: The paper gives an existence and uniqueness criterion (no Levy cycle relative to A and infinity) for realizing marked entire Thurston maps of stable parabolic type by postsingularly finite entire functions, and proves a Wolff–Denjoy type contraction estimate on Teichmüller space that supplies the foliation used in the existence proof.
- **In plain words**: The paper studies when an abstract map of the plane, one that records how a surface is wrapped onto itself, can be realized by an actual complex function of the form studied in complex dynamics. It states that this is possible exactly when there is no obstruction called a Levy cycle, and that in that case the function is unique up to affine change of coordinates. The authors also prove a result about repeatedly applied contractions on the space of surface shapes, using a fixed measure built from limits of rescaled pushforwards along a geometric ray.
- **Why it matters**: Thurston's characterization of rational maps via a no-obstruction condition is a central idea in complex dynamics, and extending it to transcendental entire functions is a natural and technically hard step. The text does not say how widely the result will be used, so its broader significance is uncertain from the abstract alone.
- **Background needed**: - Entire function: a complex function defined and holomorphic on the whole complex plane (e.g. exp(z)); "transcendental" means it is not a polynomial.
- Thurston map: a topological map of a sphere or plane that is locally like a complex map, with a finite set of special points (postsingular set) whose orbits are tracked.
- Thurston equivalence: two maps are equivalent if a pair of homeomorphisms relates them compatibly; realizability asks whether such a map comes from an actual holomorphic function.
- Levy cycle: a combinatorial obstruction (a cycle of nested curves with certain degree behavior) that prevents realization.
- Teichmüller space: the space of shapes (complex structures) of a surface, with a natural distance; Thurston pullback acts on it.
- Measured foliation and extremal length: tools measuring how "long" curve families are on a surface; used to quantify contraction.
- Wolff–Denjoy theorem: a classical result that orbits of a non-expanding map on a disk/hyperbolic space converge to a boundary point; the paper proves an analogue on Teichmüller space.
- Relation to other settings: real entire maps and exponential maps, which the authors compare with. · level: research-level

<details><summary>Original abstract</summary>

We prove that a marked topological entire Thurston map $(f,A)$ of stable parabolic type is Thurston equivalent relative to $A$ to a postsingularly finite entire function if and only if it has no Levy cycle relative to $A\cup\{\infty\}$. Here $A$ is a finite forward-invariant set containing the postsingular set. In the realizable case, the entire function is unique up to complex affine conjugacy, and every orbit of the Thurston pullback converges to its fixed point. We establish a Wolff--Denjoy type estimate for nonexpanding self-maps $T$ of the Teichm\"uller space of any connected orientable surface of finite type without boundary. If $T$ has an unbounded orbit, there are a nonzero measured foliation $G$ and a constant $C$ such that $\operatorname{Ext}_{T^k x}(G)\le C\operatorname{Ext}_x(G)$ for every $x$ and $k\ge0$. For a fixed-point-free transcendental Thurston pullback, this supplies the foliation used in the existence proof. A central tool is a fixed finite measure obtained as the total-variation limit of renormalized pushforward measures transported back along a Teichm\"uller ray. It allows us to select a cylinder at a late time and compare the mass of the same marked region at different times. If $G$ has a cylinder, a four-point extremal-length estimate and the Thurston matrix force a Levy cycle. Otherwise, in the absence of a Levy cycle, cluster rescaling shows that cylinders of large modulus carry almost all the fixed measure at all late times. Following a cylinder of definite mass until its modulus decreases gives a contradiction. We compare this geometric argument with the proofs for real entire maps and exponential maps.

</details>

## Operator algebras and spectral theory

### [Nonlinear skew Lie-type centralizers on $\ast$-algebras](https://arxiv.org/abs/2611.26647)
*Mohammad Afajal Ansari, Mohammad Ashraf, Md Shamim Akhter* · `math.RA` · arXiv:2611.26647v1 · relevance 0.15

- **In one sentence**: The paper shows that nonlinear maps on a unital *-algebra that commute with a skew Lie-type bracket p_n are of the form X -> ZX with Z a self-adjoint central element, and uses this to describe nonlinear generalized skew Lie n-derivations as ZX plus an additive *-derivation.
- **In plain words**: This is a pure mathematics paper about algebras of operators, which are collections of matrix-like objects that can be multiplied and "starred" (a kind of conjugate-transpose). The authors study maps that respect a special twisted commutator-style bracket built from several inputs. They prove that any such map must simply multiply its input by a fixed central, self-adjoint element, and they use this to classify a wider family of related maps.
- **Why it matters**: The result gives a rigid classification of nonlinear maps that preserve an algebraic structure, which is a standard type of question in operator algebra theory. The text does not discuss applications beyond the algebra classes it names, so its wider significance is uncertain.
- **Background needed**: - Unital *-algebra: a ring of operators containing an identity element, closed under an involution X -> X* (a conjugate-transpose-like operation).
- Center Z(A): the elements that commute with everything in the algebra.
- Commutator-type bracket: a product built from two inputs that measures how far they fail to commute; here a skew variant using X*.
- Iterated brackets p_n: the bracket applied repeatedly to n inputs.
- Derivation: a map obeying a product rule; an additive *-derivation also respects addition and the involution.
- Nonlinear preserver problem: classifying nonlinear maps that keep a given algebraic expression unchanged.
- Prime algebras, standard operator algebras and von Neumann algebras: standard classes of operator algebras with well-studied structure. · level: research-level

<details><summary>Original abstract</summary>

Let \(\mathcal{A}\) be a unital \(\ast\)-algebra over the complex field \(\mathbb{C}\), with center \(\mathcal{Z}(\mathcal{A})\). For any \(X_1,X_2,\ldots,X_n\in\mathcal{A}\), define recursively $ p_1(X_1)=X_1,$ $p_2(X_1, X_2)=[X_1,X_2]_{\ast}=X_1X_2-X_2X_1^{\ast}$ and $p_n(X_1,X_2,\ldots,X_n)=[p_{n-1}(X_1,X_2,\ldots,X_{n-1}),X_n]_{\ast}$ for all integers \(n\geq 2\). In this paper, we prove that if a map \(\Phi:\mathcal{A}\to\mathcal{A}\) satisfies $\Phi(p_n(X_1,X_2,\ldots,X_n))=p_n(\Phi(X_1),X_2,\ldots,X_n)$ for all \(X_1,X_2,\ldots,X_n\in\mathcal{A}\), then \(\Phi\) necessarily has the form $\Phi(X)=ZX,$ where \(Z=Z^{\ast}\in\mathcal{Z}(\mathcal{A})\). As an application, we establish that, under suitable assumptions, every nonlinear generalized skew Lie \(n\)-derivation \(G:\mathcal{A}\to\mathcal{A}\) admits a standard form $G(X)=ZX+D(X),$ where \(Z\in\mathcal{Z}(\mathcal{A})\) and \(D:\mathcal{A}\to\mathcal{A}\) is an additive \(\ast\)-derivation. Finally, we apply this result to several important classes of unital \(\ast\)-algebras, including unital prime \(\ast\)-algebras, standard operator algebras, and von Neumann algebras.

</details>

### [One exponential or two? Invertibility tests for Jordan epimorphisms](https://arxiv.org/abs/2611.27850)
*Catalin Badea* · `math.FA` · arXiv:2611.27850v1 · relevance 0.11

- **In one sentence**: The paper asks how many exponential-type test elements are needed to certify that a unital surjection between complex Banach algebras (with semisimple target) is a Jordan epimorphism, and gives conditions using products of two exponentials, single exponentials, kernel ideal properties, and special source or target classes.
- **In plain words**: The paper studies a question about structure-preserving maps between algebras of mathematical objects (operators). A map is called a Jordan epimorphism if it respects a symmetrised version of multiplication. The authors ask how many special test elements, the "exponentials," must be checked to tell whether a given map has this property, and find that checking products of two exponentials suffices in general.
- **Why it matters**: The work sharpens when a simple invertibility check can certify a structural property of a map, which matters for the theory of operator algebras. The text does not indicate applications beyond this area, so broader significance is unclear from the given material.
- **Background needed**: - Banach algebra: a space of bounded linear operators or functions that can be multiplied and has a norm, so limits make sense.
- Unital linear surjection: a linear map that preserves the identity element and hits every element of the target.
- Semisimple algebra: one with no nonzero nilpotent-type "hidden" pieces; its structure is determined by its nontrivial representations.
- Jordan epimorphism: a surjective map that preserves the Jordan product (ab+ba)/2, a symmetrised product, rather than full multiplication.
- Exponential of an element a: the series e^a, which is always invertible; testing whether T maps such elements to invertible ones is the test used.
- Two-sided ideal: a subset closed under multiplication from both sides by any element of the algebra; the kernel condition in the result.
- C*-algebra and group algebra l^1(G): standard examples of algebras with an adjoint or a group structure.
- Tracial state: a normalised positive functional that behaves like a trace (value unchanged under commutators).
- Spectral isometry and resolvent estimates: tools relating how spectra (sets of eigenvalue-like numbers) and inverses behave under the map. · level: research-level

<details><summary>Original abstract</summary>

How many exponential factors must one test to recognise a Jordan epimorphism? Let \(T\colon A\to B\) be a unital linear surjection between complex Banach algebras, with \(B\) semisimple. Using a spectral-isometry theorem of Aznay and Chabbabi, we show that it suffices for \(T\) to send every product of two exponentials to an invertible element to force $T$ to be Jordan. If only single exponentials are tested, \(T\) is a Jordan epimorphism if and only if its kernel is a two-sided ideal, or equivalently a left ideal. A resolvent estimate on a logarithmic spiral shows that a single exponential suffices when the source is a \(C^*\)-algebra or the group algebra \(\ell^1(G)\) of a discrete group. A separate argument, which does not use the spectral-isometry theorem, shows that a single exponential also suffices when the target is a \(C^*\)-algebra with a faithful family of tracial states.

</details>

## Algebra

### [Claw-free difference graphs of finite groups](https://arxiv.org/abs/2611.27414)
*Pallabi Manna* · `math.GR` · arXiv:2611.27414v1 · relevance 0.16

- **In one sentence**: The paper classifies finite groups whose difference graph (a graph built from cyclic subgroup relations among elements in the enhanced power graph) is claw-free, giving group-theoretic conditions, consequences for symmetric, alternating and simple groups, and a complete list for soluble groups.
- **In plain words**: The paper studies a graph built from a finite group: elements are linked when they generate a cyclic subgroup and neither is a power of the other. It asks when this graph contains no "claw" (one vertex joined to three others that are mutually unlinked). The authors show this happens exactly when the element orders and the centralizers of elements of order 2 and 3 satisfy specific restrictions, and they work out which groups qualify.
- **Why it matters**: The result gives a complete, checkable criterion linking a graph-theoretic property to the internal structure of groups, and it covers symmetric, alternating, simple and soluble groups. The text does not say what wider applications it has, so its significance beyond this graph-theoretic setting is unclear from the excerpt.
- **Background needed**: - A finite group: a finite set of symmetries closed under composition, such as permutations of n objects.
- Element order: the smallest positive power of an element that gives the identity.
- Cyclic group: a group generated by one element, like repeated rotation.
- Graph, vertex, edge: dots and lines; a claw is one dot joined to three dots that are not joined to each other.
- Enhanced power graph: the graph where elements are linked if they lie in a common cyclic subgroup; the difference graph is a refinement of it.
- Centralizer: the elements that commute with a given element.
- Sylow p-subgroup, normal subgroup, soluble group, simple group, EPPO group: standard group-theory terms; soluble groups are built from abelian pieces, and simple groups have no nontrivial normal subgroups.
- Frobenius group: a group with a complement acting fixed-point-freely on a normal subgroup. · level: research-level

<details><summary>Original abstract</summary>

Let $\D(G)$ be the difference graph of a finite group $G$: the graph on the non-isolated vertices of $\PE(G)-\Pg(G)$, where $x\sim_{\D} y$ if and only if $\gen{x,y}$ is cyclic and neither of $x,y$ lies in the cyclic group generated by the other. A claw is the graph $K_{1,3}$ and a graph is claw-free if it has no induced claw. We prove that for every finite group $G$, $\D(G)$ is claw-free if and only if it is a disjoint union of copies of the path $P_3$, if and only if the element orders of $G$ are prime powers or $6$, every element of order $3$ has at most one involution in its centralizer, and every involution has at most one subgroup of order $3$ in its centralizer (equivalently: $C_G(a)$ has a normal Sylow $2$-subgroup of order at most $2$ for every $a$ of order $3$, and $C_G(u)$ a normal Sylow $3$-subgroup of order at most $3$ for every involution $u$). Consequences: a nilpotent group that is not a $p$-group has claw-free $\D$ if and only if $G\cong C_6$; $\D(\Sym_n)$ is claw-free if and only if $n\le 5$; $\D(\Alt_n)$ is claw-free if and only if $n\le 6$; a non-abelian simple group has claw-free $\D$ if and only if it is EPPO or $\PSL_2(11)$ or $\PSL_2(13)$, proved family by family (this uses the classification of finite simple groups). For soluble groups we obtain a complete classification: the non-EPPO soluble groups with claw-free $\D$ are $C_6$, $D_{12}$, $C_3\rtimes C_4$ and the Frobenius groups $N\rtimes K$ with $N$ an abelian $r$-group, $r\ge 5$, and $K\cong C_6$ or $C_3\rtimes C_4$. For every group with claw-free non-empty $\D$ we show $|O_2(G)|\le 2$ and $|O_3(G)|\le 3$, and we give non-soluble examples ($\Sym_5$, $\PGL_2(7)$, $\PSL_2(11)$, $\PSL_2(13)$). We also prove that the full enhanced power graph is claw-free only for cyclic groups and clarify the relations between claw-freeness of $\D(G)$, $\Pg(G)$ and $\PE(G)$.

</details>

### [Local cohomology module with infinitely many associated primes over ramified regular local rings of the least possible dimensions](https://arxiv.org/abs/2611.26655)
*Rajsekhar Bhattacharyya* · `math.AC` · arXiv:2611.26655v1 · relevance 0.15

- **In one sentence**: The paper constructs local cohomology modules with infinitely many associated primes over ramified regular local rings in two specific ring dimensions, which are the smallest possible, building on an earlier 12-dimensional example and a cited theorem (Theorem 2.6 in SS).
- **In plain words**: This paper is about a question in commutative algebra, a branch of mathematics that studies rings of polynomial-like objects. The author asks when certain algebraic objects called local cohomology modules can have infinitely many "associated primes," which are special sub-objects that record their structure. The paper builds such examples in two different dimensions of a particular kind of ring, and it says these dimensions are the least possible.
- **Why it matters**: Finding the smallest dimension where a behaviour occurs tells us where the boundary of the phenomenon lies. The text does not say how far the results reach beyond these examples, and it does not discuss applications outside algebra.
- **Background needed**: - Ring: a set of numbers or objects with addition and multiplication, such as polynomials.
- Regular local ring: a well-behaved ring with a single special point, where the "dimension" counts independent directions.
- Ramified: a technical condition on how the ring sits relative to a prime number; here it means the ring is not in the simplest form.
- Local cohomology module: an algebraic object built from a ring and an ideal (a special subset), used to measure its hidden structure.
- Associated prime: a special sub-object that a module "points to"; having infinitely many is unusual, since most modules of this kind have finitely many.
- Dimension: the number of independent directions in the ring.
- The text relies on an earlier result (SS, Theorem 2.6) and on an earlier paper (Ma) that gave a 12-dimensional example; the source of the cited theorem is not given here. · level: research-level

<details><summary>Original abstract</summary>

In \cite{Ma} we have observed the example of local cohomology module with infinitely many associated primes over a 12 dimensional ramified regular local ring. In this paper we construct examples of local cohomology modules with infinitely many associated primes over ramified regular local rings of two different ring dimensions. The result of this paper is very much dependent on the result (\cite{SS}, Theorem 2.6).

</details>

## Representation theory

### [Categorification of the reduced stated ${\rm SL}_n$-skein algebras of polygons](https://arxiv.org/abs/2611.26922)
*Min Huang, Zhihao Wang* · `math.QA` · arXiv:2611.26922v1 · relevance 0.09

- **In one sentence**: The paper gives a monoidal categorification of the reduced stated SL_n-skein algebra of an m-punctured polygon, using the Kashiwara–Kim–Oh–Park category of quantum affine sl_n-modules attached to the Garside element of the braid group, and shows that a key subalgebra is a quantum cluster algebra that quantizes a braid variety.
- **In plain words**: This is a research paper in representation theory about a family of algebras built from polygons with marked boundary points, which encode ways of drawing networks of curves on the polygon. The authors show these algebras can be realized as the representation rings of a family of symmetry-based objects (modules over a quantum affine algebra), so their structure can be read off from that setting. A central piece, a smaller subalgebra, is shown to have the same structure as a known kind of "cluster algebra" that comes from a specific building block of the braid group.
- **Why it matters**: It connects three areas that are usually studied separately: skein algebras from knot theory, cluster algebras, and monoidal categories of quantum group representations. The text claims the result gives a positive basis for the whole algebra, but the text does not show how widely this framework applies beyond polygons, so its wider significance is uncertain.
- **Background needed**: - Skein algebra: an algebra whose elements are diagrams of curves or webs on a surface, with relations from knot theory.
- SL_n / quantum group: a family of symmetry groups and their deformed versions, whose representations are studied here.
- Cluster algebra: an algebra generated by variables grouped into overlapping "clusters" that mutate in a prescribed way.
- Monoidal categorification: a way of matching a cluster algebra with a category of representations, where simple objects correspond to cluster variables.
- Braid group and Garside element: the group of braids (ways of tangling strands) and a distinguished element of it.
- Braid variety: a geometric space defined by braid data.
- Quantization: a deformation of a commutative algebra into a noncommutative one with a parameter q.
- Skew Laurent extension: an algebra obtained by adjoining invertible variables with a twisted commutation rule. · level: research-level

<details><summary>Original abstract</summary>

Let $\overline{\mathscr{S}}(\mathbb P_m)$ be the reduced stated ${\rm SL}_n$-skein algebra of a polygon with $m$ boundary punctures ($m\geq 3$). Building on the quantum cluster algebra structure of $\overline{\mathscr{S}}(\mathbb P_m)$ established by Cao and the authors, and on the monoidal category $\mathcal{C}(\Delta^{m-2})$ of finite-dimensional modules over the quantum affine algebra $U_q'(\widehat{\mathfrak{sl}}_n)$ introduced by Kashiwara, Kim, Oh and Park, where $\Delta$ is the Garside element of ${\rm Br}_n$, we give a monoidal categorification of $\overline{\mathscr{S}}(\mathbb P_m)$. As a consequence, $\overline{\mathscr{S}}(\mathbb P_m)$ has a basis with positive structure constants. A key role is played by the subalgebra $\mathcal A_{n,m}$ spanned by the stated $n$-webs whose $m-1$ edge weights are zero. We show that $\mathcal A_{n,m}$ is a quantum cluster algebra whose seed coincides with the Kashiwara--Kim--Oh--Park seed of $\Delta^{m-2}$. Hence it is the quantum Grothendieck ring of a monoidal localization, at the frozen modules, of a subcategory of $\mathcal{C}(\Delta^{m-2})$ with the same simple objects, and a quantization of the braid variety $X(\Delta^{m-1})$. The whole algebra $\overline{\mathscr{S}}(\mathbb P_m)$ is a skew Laurent extension of $\mathcal A_{n,m}$ in $(m-1)(n-1)$ frozen variables.

</details>

### [Cohomology of twisted tensor products over commutative rings](https://arxiv.org/abs/2611.26746)
*Xingting Wang, Sarah Witherspoon* · `math.RT` · arXiv:2611.26746v1 · relevance 0.08

- **In one sentence**: The paper gives explicit descriptions of the cohomology of bicharacter-twisted tensor products of rings over a commutative ground ring, under hereditary and root-of-unity assumptions, and computes cohomology rings of Taft orders over cyclotomic integers as examples.
- **In plain words**: The paper studies a way of combining two algebraic structures, called rings, into one larger structure using a "twist" that changes how their elements interact. It asks how a standard invariant, cohomology, of the combined structure relates to those of the two original pieces. The authors give explicit descriptions for a specific kind of twist, and work out examples involving Taft orders over cyclotomic integers.
- **Why it matters**: The text does not say how the results are used elsewhere, so their wider importance is unclear from the summary alone. It may matter to researchers in representation theory and homological algebra who study rings built from twisted products and their invariants.
- **Background needed**: - Ring: a set with addition and multiplication, such as the integers.
- Commutative ground ring: the base ring over which everything is built, where multiplication order does not matter.
- Tensor product of rings: a standard way to build a bigger ring from two smaller ones.
- Twisted tensor product: a version where the two pieces interact through a rule (the twist) rather than independently.
- Bicharacter: a two-input rule that is multiplicative in each input, used here to define the twist.
- Cohomology (of a ring): an algebraic invariant that measures structure and extensions; its ring structure is the object studied.
- Hereditary ring: a ring where certain algebraic objects (submodules) behave simply; a technical assumption.
- Roots of unity and grading groups: numbers that repeat under powers, and labels that split a structure into pieces indexed by a finite group.
- Taft orders over cyclotomic integers: specific families of rings built from roots-of-unity-type integers, used as test cases. · level: research-level

<details><summary>Original abstract</summary>

Over a commutative ground ring, cohomology of a twisted tensor product of two rings mixes their cohomology via the twisting. We focus on bicharacter twistings and give explicit descriptions when the ground ring is itself a module. We state our main results for ground rings that are hereditary and contain roots of unity corresponding to finite grading groups. As a class of examples, we compute cohomology rings of Taft orders over cyclotomic integers.

</details>

## Number theory

### [Period maps and the $C_{\rm st}$ conjecture](https://arxiv.org/abs/2611.27054)
*Pierre Colmez, Wies{\l}awa Nizio{\l}, Xinyu Shao* · `math.AG` · arXiv:2611.27054v1 · relevance 0.16

- **In one sentence**: The paper constructs elliptic-curve families over p-adic discs that violate the C_st conjecture in degree 1, and shows that for smooth proper families over small discs the conjecture holds exactly when the period map is constant.
- **In plain words**: This is about a conjecture on p-adic numbers, a number system used in number theory in which distance is measured differently from ordinary arithmetic. The authors build a family of elliptic curves (smooth curves defined by cubic-type equations) over a small p-adic disc and show that the total space of this family breaks the conjecture. They also find that, for curves, the conjecture holds in small discs exactly when a certain "period map" is constant.
- **Why it matters**: The C_st conjecture is a statement relating two kinds of p-adic cohomology invariants, and the result shows it does not carry over from proper families to proper families over Stein bases (a class of nice non-compact spaces). The text does not say how this connects to wider applications, so its broader significance is unclear from the abstract alone.
- **Background needed**: - p-adic numbers: an alternative completion of the rationals, where numbers close together are those whose difference is divisible by a high power of a prime p.
- p-adic disc: the p-adic analogue of a small open disc in the complex plane, used as a base space for families.
- Elliptic curve: a smooth genus-one curve with a group structure, a standard object in number theory.
- Proper family: a family of spaces with no points "escaping to infinity"; Stein varieties are a class of well-behaved non-compact spaces.
- Cohomology and local systems: tools that attach algebraic invariants to a space and its continuous deformations; a local system is "geometrically constant" when these invariants do not vary across the base.
- Period map: a map recording how the Hodge-type data of a family varies; constant means it does not change across the base.
- Gauss–Manin Higgs fields: the derivative-like objects describing how the family's cohomology varies; vanishing means no variation.
- C_st conjecture: a conjecture about the relation between de Rham and semistable p-adic cohomology, which is the subject of the result. · level: research-level

<details><summary>Original abstract</summary>

We construct a family of elliptic curves over an open disc whose total space violates the $C_{\mathrm{st}}$ conjecture in degree $1$. Hence the conjecture, known for proper and for Stein varieties, as well as for products of such, does not extend to proper families over Stein bases. This is an instance of a general criterion: the $C_{\mathrm{st}}$ conjecture holds for the total space of a smooth proper family over a sufficiently small open disc if and only if its period map is constant, i.e., all Gauss--Manin Higgs fields vanish or, equivalently, the $p$-adic local systems $R^if_*\mathbf{Q}_p$ are geometrically constant. This criterion is special to curves: over a $2$-dimensional polydisc, we give a family of $p$-adic analogues of non-K\"ahler elliptic surfaces whose period maps and local systems are constant, but whose total space violates the conjecture.

</details>

### [On generation of the coefficient field of a primitive HMF by a single Fourier coefficient: An application of Nekov\'a\v{r}'s Theorem](https://arxiv.org/abs/2611.26934)
*Narasimha Kumar, Dwipanjana Shit* · `math.NT` · arXiv:2611.26934v1 · relevance 0.10

- **In one sentence**: The paper proves an analogue of Ribet's large image theorem for residual Galois representations of non-CM primitive Hilbert modular forms, using Nekovář's large image theorem on the associated automorphic representation, and deduces that the coefficient field of a form without nontrivial inner twists is generated by a single prime Fourier coefficient for a set of primes of Dirichlet density one.
- **In plain words**: The paper studies special symmetric functions (Hilbert modular forms) defined over a number field and the numbers that encode them, called Fourier coefficients. It shows that, for a form with no hidden symmetries of the kind called inner twists, one coefficient at a suitable prime position is enough to generate all the numbers needed to describe the form. The statement holds for a set of primes that is large in a precise density sense, and the authors derive it from a more general result about a smaller field attached to the form.
- **Why it matters**: The result sharpens a known style of conclusion in the theory of modular forms, where one asks how little data determines the whole arithmetic of a form. It is a technical contribution, and the text does not indicate wider applications beyond this area.
- **Background needed**: - Modular forms: highly symmetric functions on complex space; Hilbert modular forms generalise them to several real number fields at once.
- Fourier coefficients: the numbers appearing in the series expansion of a form; they carry its arithmetic information.
- Coefficient field: the number field generated by all Fourier coefficients of a form.
- Inner twists: symmetries that relate a form to twisted copies of itself; "non-CM" means the form lacks complex multiplication, a special extra symmetry.
- Galois representations: ways the absolute Galois group (symmetries of number fields) acts on vector spaces, attached to forms; "residual" means the mod-prime reduction.
- Large image theorems (Ribet, Nekovář): results saying such representations have image as large as possible under generic conditions.
- Dirichlet density: a way of measuring the size of a set of primes. · level: research-level

<details><summary>Original abstract</summary>

Let $f$ be a non-CM primitive Hilbert modular form (HMF) over a totally real number field, of parallel even weight $k\geq 2$, with coefficient field $E_f$, and let $F_f \subseteq E_f$ denote the field fixed by the inner twists of $f$. In this article, we establish an analogue of Ribet's large image theorem for the residual Galois representations associated with $f$, by applying Nekov\'a\v{r}'s large image theorem (cf.~\cite[Theorem B.5.2]{Nek12}) to the automorphic representation $\pi(f)$ associated with $f$. As a result, we prove that if $f$ has no nontrivial inner twists, then $E_f$ is generated by a single prime Fourier coefficient, for a set of prime ideals of Dirichlet density one. We derive this result as a consequence of a more general theorem established for $F_f$.

</details>

## Algebraic geometry

### [Tensor products of additive groups as reciprocity sheaves](https://arxiv.org/abs/2611.26947)
*Toshiro Hiranouchi, Rin Sugiyama* · `math.AG` · arXiv:2611.26947v1 · relevance 0.12

- **In one sentence**: The paper computes the Nisnevich reciprocity sheaves attached to tensor products of cube-invariant objects built from the additive and multiplicative groups (with at least one additive factor), showing over perfect fields of characteristic not two that they split into sums of absolute Kähler differential sheaves with binomial multiplicities, and applies this to the Hochschild homology of the additive object.</one_liner>
<parameter name="plain">This is a technical paper in algebraic geometry, a field that studies solutions of polynomial equations using geometric tools. The authors study a family of mathematical objects built by combining two basic building blocks, the additive group and the multiplicative group, and they work out exactly what these objects look like. They find that, over suitable number systems, each one breaks apart into simpler pieces of a known type, and they use this to describe a related construction called Hochschild homology.
- **Why it matters**: The text gives only the abstract, so the wider significance is unclear from it alone. It is likely of interest to specialists working on reciprocity sheaves and motivic or cohomological methods, where explicit decompositions of this kind can be useful for computations.
- **Background needed**: - Algebraic geometry: the study of geometric shapes defined by polynomial equations.
- Sheaf: a bookkeeping device that assigns data to open pieces of a space consistently.
- Reciprocity sheaf: a sheaf with extra structure (from Kahn, Saito and Yamazaki) that tracks how data behaves under maps of curves; used in motivic homotopy theory.
- Additive and multiplicative groups: the line with addition, and the nonzero numbers with multiplication, viewed as geometric objects.
- Tensor product: a way of combining two algebraic objects into one.
- Kähler differentials: an algebraic notion of "infinitesimal change" of functions.
- Hochschild homology: an invariant measuring the structure of an algebra, here applied to geometric objects.
- Perfect field of characteristic not two: a base number system with well-behaved arithmetic, excluding the case where 1+1=0. · level: research-level

<details><summary>Original abstract</summary>

We compute the Nisnevich reciprocity sheaves associated with tensor products of the cube-invariant objects for the additive and multiplicative groups, with at least one additive factor. Over a perfect field of characteristic different from two, these sheaves decompose into direct sums of absolute K$\"a$hler differential sheaves with binomial multiplicities. As an application, we compute the associated reciprocity sheaves of the Hochschild homology of the additive object.

</details>

### [Constructing toric diagonal modules with short linear resolutions](https://arxiv.org/abs/2611.27025)
*Jay Yang* · `math.AC` · arXiv:2611.27025v1 · relevance 0.11

- **In one sentence**: For a complete simplicial toric variety, the paper constructs Cohen–Macaulay modules with linear resolutions whose associated sheaf is the diagonal, and relates the Favero–Huang and Hanlon–Hicks–Lazarev constructions as dual approaches starting from a compatible Z^n-stratification.
- **In plain words**: This paper works in algebraic geometry, the study of shapes defined by polynomial equations. It looks at a special family of geometric spaces called toric varieties and builds, for each one, a collection of algebraic objects (modules) that have especially simple step-by-step "resolutions," which are ways of approximating a given object by a chain of simpler ones. These objects are tied to the diagonal, the natural copy of a space sitting inside the product of the space with itself. The authors also say that two existing methods for building such resolutions turn out to be dual to each other.</plain>
<parameter name="why">The text gives the construction and the duality claim, but not the detailed results or their applications, so its wider significance is hard to judge from this excerpt. It may matter for researchers who use resolutions of the diagonal as a tool in homological algebra and geometry.
- **Background needed**: - Toric variety: a geometric space built from combinatorial data (cones and fans), often studied through polytopes.
- Simplicial: the underlying cones have a simple, triangle-like shape, which makes computations tractable.
- Sheaf: a tool for keeping track of local data (like functions) across a space.
- Diagonal: the subspace of pairs (x, x) inside the product space; its associated sheaf encodes how the space relates to itself.
- Cohen–Macaulay module: an algebraic object with good depth properties, meaning it behaves well under taking slices.
- Linear resolution: a chain of free modules whose maps are given by linear equations, the simplest kind of resolution.
- Z^n-stratification: splitting a space into pieces indexed by integer lattice points, used to organize the construction. · level: research-level

<details><summary>Original abstract</summary>

For a complete simplicial toric variety $X$, we construct a collection of Cohen--Macaulay modules with linear resolutions where the associated sheaf is the diagonal. Through this work, we see that the resolutions constructed by Favero--Huang from homotopy path algebras and those constructed by Hanlon--Hicks--Lazarev can be viewed as two dual methods to construct resolutions of the diagonal starting from a compatible $\mathbb{Z}^n$-stratification.

</details>

## Topology

### [On the chromatic splitting conjecture in coheight $1$](https://arxiv.org/abs/2611.27879)
*Tobias Barthel, Lucas Mann, Rin Ray et al.* · `math.AT` · arXiv:2611.27879v1 · relevance 0.11

- **In one sentence**: The paper proves cases of Hopkins' chromatic splitting conjecture in coheight 1, showing a map between K(h-1)-local E-infinity rings has a retract (and is an isomorphism when h=2 and p is odd), using a new two-tower isomorphism and solid Lubin–Tate spectra.
- **In plain words**: This is research in stable homotopy theory, the study of the "shapes" that spaces and their symmetries leave behind when viewed through a generalized kind of counting. The authors look at a conjectured pattern (Hopkins' chromatic splitting conjecture) that relates layers of this structure, and they confirm it in a specific case, at a prime p and height h where h-1 is the relevant "layer". They prove the relevant map has a retract (a left inverse, in a loose sense) when p-1 does not divide h-1, and for h=2 with p odd they show the map is an isomorphism.
- **Why it matters**: The text claims a partial confirmation of a published prediction, which is of interest to specialists in chromatic homotopy theory. The abstract also introduces a new "two-tower isomorphism" and solid Lubin–Tate spectra, which may be useful tools beyond this paper, though the text does not say how far they reach.
- **Background needed**: - Stable homotopy theory: a framework for studying topological spaces through homotopy invariants, organized by spectra.
- Chromatic homotopy theory: studies these invariants by "height" h, layered by how they behave under certain prime-based localizations (K(h)-local objects).
- Morava stabilizer group G_h: a profinite symmetry group attached to height h that acts on the Lubin–Tate spectrum E_h.
- p-divisible groups: algebro-geometric objects (roughly, towers of p-power torsion) that classify the height-h data.
- p-adic geometry: geometry over p-adic numbers and perfectoid spaces, where the paper's towers and Banach–Colmez spaces live.
- Retract: a map with a left inverse, so the source contains the target as a summand.
- Faltings' isomorphism: a known correspondence between the Lubin–Tate and Drinfeld towers, used here as an analogy. · level: research-level

<details><summary>Original abstract</summary>

This article confirms predictions made by Hopkins' chromatic splitting conjecture in stable homotopy theory. A consequence of our main theorem is that a certain map of $K(h-1)$-local $\mathbb{E}_\infty$-rings $\mathbb{S}_{K(h-1)}^{B\mathbb{Z}}\to L_{K(h-1)}\mathbb{S}_{K(h)}$ admits a retract, so long as $p-1$ does not divide $h-1$. If $h=2$ and $p$ is odd, we show this map is an isomorphism. We use methods from the theory of $p$-divisible groups and $p$-adic geometry. Along the way we prove an entirely new kind of "two-tower isomorphism," in analogy with Faltings' isomorphism between the Lubin--Tate and Drinfeld towers, which parametrizes $p$-divisible groups over characteristic $p$ perfectoid spaces with fixed generic fiber in terms of negative Banach--Colmez spaces. Using the two-tower isomorphism, we gain control over the continuous cohomology of the Morava stabilizer group $\mathbb{G}_h$ with coefficients in $\pi_*L_{K(h-1)}E_h$. To study the continuous action of $\mathbb{G}_h$ on $L_{K(h-1)} E_h$, it was necessary to develop the theory of solid Lubin--Tate spectra. Adapting Lurie's constructions, we attach a solid Lubin--Tate spectrum to $p$-divisible groups over a broad class of solid rings in characteristic $p$.

</details>

### [The Strong AJ Conjecture for Hyperbolic Prime Knots is False](https://arxiv.org/abs/2611.26905)
*RJ Acu\~na* · `math.GT` · arXiv:2611.26905v1 · relevance 0.07

- **In one sentence**: The paper shows that the strong AJ conjecture, which links the minimal annihilator of the colored Jones polynomial to the Cooper–Culler–Gillet–Long–Shalen A-polynomial, fails for hyperbolic prime knots, using the knot 8_11, and verifies Lê's P-hat = A-hat conjecture and the weak AJ conjecture for that knot.
- **In plain words**: This paper is about knots, the tangled loops studied in topology, and two mathematical "fingerprints" that can be computed for each knot. The authors check whether these fingerprints match, as a conjecture predicts, and find that for the knot 8_11 they do not: an extra factor appears that the conjecture did not allow. The work was partly done with AI assistance and partly checked in the Lean proof assistant.
- **Why it matters**: It matters because it shows a widely studied conjecture linking quantum-style knot invariants to classical geometry fails even for a prime hyperbolic knot, which narrows what the conjecture can be. The text does not say how far the counterexample reaches beyond 8_11, and it mentions a separate later report of counterexamples among non-hyperbolic knots, so the broader picture is still being worked out.
- **Background needed**: - A knot is a closed loop tangled in 3D space; knot invariants are numbers or polynomials that tell knots apart.
- The colored Jones polynomial is a family of knot invariants J(n) indexed by an integer n; its minimal annihilator is the simplest polynomial relation it satisfies.
- The A-polynomial (Cooper, Culler, Gillet, Long, Shalen) is a two-variable polynomial that encodes the geometry of the knot's complement via representations of its fundamental group.
- The AJ conjecture says these two objects should match after a specialization of variables; "hyperbolic" means the knot complement has a constant-curvature geometry.
- Zhang previously found counterexamples among composite knots; Lê proposed the P-hat = A-hat conjecture and a weak AJ version.
- The paper says it was AI assisted and partly formalized in Lean, a computer proof checker. · level: research-level

<details><summary>Original abstract</summary>

Let $K$ be a knot in $S^3$. The strong AJ conjecture relates two of its invariants. The first is the minimal-order annihilator $\widehat A$ of the $n$th colored Jones polynomial $J(n)$. The second is the two-variable $A$-polynomial of Cooper, Culler, Gillet, Long, and Shalen. The conjecture says that after specialization $\varepsilon^*(\widehat A)\asymp A$. Zhang gave the first family of composite-knot counterexamples. For $8_{11}$ the specialization of $\widehat A$ carries an extra trefoil factor $L+M^6$. We prove this by verifying L\^e's $\widehat P=\widehat A$ conjecture. Zhang's corrected formulation of the AJ conjecture agrees with L\^e's weak AJ conjecture, which we prove for $8_{11}$. Li, Li, and Sun have since reported counterexamples of the weak AJ conjecture among non-hyperbolic prime knots. This work was AI assisted, and parts of it have been formalized in Lean.

</details>

## Dynamical systems

### [Nonlinear stability of periodic waves in the Benjamin-Ono equation](https://arxiv.org/abs/2611.27036)
*Jinbing Chen, Colin Grant, Dmitry E. Pelinovsky* · `math.AP` · arXiv:2611.27036v1 · relevance 0.10

- **In one sentence**: The paper proves nonlinear orbital stability of periodic traveling waves of the Benjamin-Ono equation by building a Lyapunov functional from conserved quantities (momentum, energy, and a higher-order energy from integrability) and checking its second variation is positive.
- **In plain words**: The Benjamin-Ono equation is a mathematical model for waves in deep stratified fluids, such as internal waves in the ocean. This paper studies repeating wave shapes that keep travelling without changing form. The authors show that if you nudge such a wave a little, it stays close to its original shape over time.
- **Why it matters**: Showing that a wave pattern is stable under small disturbances is a basic question for whether such patterns can persist in real physical systems. The text does not say how far the result reaches beyond this equation, so its wider significance is uncertain.
- **Background needed**: - Benjamin-Ono equation: a nonlinear partial differential equation describing one-directional waves in certain fluids.
- Periodic wave: a wave shape that repeats in space, like a regular ripple, that travels at constant speed.
- Orbital stability: a solution that stays close to the family of its shifted versions after small disturbances.
- Conserved quantities: totals (such as momentum and energy) that do not change as the wave evolves; they are used to control the dynamics.
- Lyapunov functional: a measure built from these quantities that cannot grow, used to prove stability.
- Second variation: the curvature of that measure around the wave; positivity of it is the key check.
- Integrability: a special structure that gives extra conserved quantities.
- Sobolev space H^1: a function class measuring size and smoothness of disturbances. · level: research-level

<details><summary>Original abstract</summary>

We construct the Lyapunov functional for the periodic waves of the Benjamin-Ono equation based on the conservation of momentum, energy, and a higher-order energy, which exists due to integrability. Positivity of the second variation of the Lyapunov functional for perturbations in Sobolev space $H^1(\mathbb{R})$ is established by utilizing the basis properties of eigenfunctions of the linearized Benjamin-Ono equation in $L^2(\mathbb{R})$. Coercivity of the Lyapunov functional for co-periodic and multiple-periodic perturbations yields the nonlinear orbital stability of the periodic waves in the periodic domain.

</details>

### [Real-analytic actions of higher-rank lattices preserving an ergodic volume](https://arxiv.org/abs/2611.27557)
*Federico Rodriguez Hertz, Zhiren Wang* · `math.DS` · arXiv:2611.27557v1 · relevance 0.06

- **In one sentence**: The paper classifies real-analytic actions of higher-rank lattices that preserve an ergodic smooth volume on a compact manifold, showing that on an open dense full-measure set they are analytically conjugate to affine actions on copies of a single double quotient, which is offered as the open homogeneous case of Zimmer's program.
- **In plain words**: The paper studies how a certain kind of discrete symmetry group (a lattice in a higher-rank Lie group) can act smoothly on a compact space, such as a manifold, while keeping a volume measure fixed. It reports that, for real-analytic actions preserving an ergodic volume, almost all of the space can be described by a simple standard model built from affine (linear-plus-shift) motions. The author states that this gives a classification of the open homogeneous case.
- **Why it matters**: The question sits in Zimmer's program, which asks how far rigid algebraic models control all actions of large symmetry groups on manifolds, so a full classification in the open homogeneous case would be a substantial structural statement. The text does not show how wide its consequences are beyond this setting, so its reach should be judged by specialists.
- **Background needed**: - Lattice: a discrete subgroup of a Lie group, such as integer matrices inside a group of transformations.
- Higher-rank: the Lie group has several independent directions of symmetry, which makes rigidity results much stronger.
- Action: a way the group moves points of a space, here a compact manifold (a smooth curved space).
- Real-analytic: smooth in a strong sense where functions are given by convergent power series.
- Ergodic volume: a measure preserved by the action such that no invariant piece splits it non-trivially; the orbits spread through the space.
- Conjugacy: an change of coordinates that turns one action into another, so they are essentially the same.
- Affine action and double quotient: the standard model, built from linear-plus-shift motions on a quotient of a Lie group.
- Zimmer's program: a research program on rigidity of group actions on manifolds.
- Lyapunov manifolds and joinings: tools for tracking how nearby orbits separate and for comparing two actions. · level: research-level

<details><summary>Original abstract</summary>

We classify real-analytic actions of higher-rank lattices that preserve an ergodic smooth volume on a compact manifold. On an invariant open dense set of full volume, the action is analytically conjugate to the restriction of an affine action on finitely many copies of one double quotient. The conjugacy carries Haar probability to the given volume. Analytic germ superrigidity supplies local coordinates with measurable dependence on the center. The conditional measures on coarse Lyapunov manifolds determine the law of a displaced center. A two-point joining pairs charts whose evaluations agree there and gives the change of coordinates. The resulting analytic frame bundle carries a coframe whose vector fields integrate to the homogeneous model. This gives the open homogeneous classification in Zimmer's program.

</details>

## Combinatorics

### [The Order of the Inertia Bound for Random Graphs](https://arxiv.org/abs/2611.27000)
*Zhengbo Chen, Xiao-Dong Zhang* · `math.CO` · arXiv:2611.27000v1 · relevance 0.13

- **In one sentence**: The paper proves a Hermitian version of the Kwan–Wigderson conjecture for random graphs G(n,1/2), showing that the minimum number of nonnegative eigenvalues of zero-diagonal Hermitian matrices supported on G is order n/log n, and it gives related bounds using Alon's constructions with independence number 2 and Shannon capacity 3.</one_liner>
<parameter name="plain">The paper studies how few "nonnegative" eigenvalues a matrix can have when its nonzero entries are only allowed where a given network has edges. For a typical random network with n points, where each pair is linked with probability one half, the authors show this minimum is at least a constant times n divided by log n, with very high probability. They also build specific graphs where the same quantity is larger than a small power of n.
- **Why it matters**: This quantity links linear algebra of matrices to graph structure, and bounds on it can bear on problems such as Shannon capacity of graphs, a measure of how much information a noisy channel can carry. The text does not show further consequences beyond the stated results, so the wider significance is uncertain.
- **Background needed**: - Graph G on n vertices: points joined by edges; G(n,1/2) is a random graph where each edge appears independently with probability 1/2.
- Eigenvalues: special numbers attached to a square matrix; the paper counts how many are zero or positive (nonnegative).
- Hermitian matrix: a complex-valued matrix equal to its own conjugate transpose; zero-diagonal and "supported on G" means nonzero entries only on edges of G.
- Independence number alpha(G): the size of the largest set of vertices with no edges between them.
- Shannon capacity: a graph measure from information theory giving the best rate at which symbols can be sent error-free over a noisy channel.
- Kwan–Wigderson conjecture: a real-valued version of this eigenvalue question that the paper extends to the Hermitian case.
- Big-O/Theta notation: Theta(f) means growth at the same rate as f up to constant factors; "with high probability" means the failure chance shrinks rapidly with n. · level: research-level

<details><summary>Original abstract</summary>

For an $n$-vertex graph $G$, let $n_{\geq0}(G)$ be the minimum number of nonnegative eigenvalues among zero-diagonal Hermitian matrices supported on $G$, allowing zero edge weights. For $n\geq2$ and $G\sim G(n,1/2)$, we prove $n_{\geq0}(G)\geq c_2n/\log(2n)$ with probability at least $1-\exp(-c_1n\log(2n))$, where $c_1,c_2>0$ are absolute constants. This proves a Hermitian extension of the Kwan--Wigderson conjecture. With high probability, $n_{\geq0}(G)=\Theta(n/\log n)$ and $n_{\geq0} G)/\alpha(G)=\Theta(n/(\log n)^2)$, where $\alpha(G)$ is the independence number. Using Alon's constructions, we obtain, for every sufficiently large $n$, a $n$-vertex graph $G$ with $\alpha(G)=2$ and $n_{\geq0}(G)=\Omega(n^{1/3})$. For infinitely many $n$, we also obtain $n$-vertex graphs $H$ with Shannon capacity $3$ and $n_{\geq0}(H)=\Omega(n^{1/4})$.

</details>

### [Additive cubes are avoidable by a non-uniform morphism of length $6$ over $\{0,a,b\}$ (with $b \ge 4$ and $\gcd(a,b) = 1$)](https://arxiv.org/abs/2611.27519)
*Damien Jamet* · `math.CO` · arXiv:2611.27519v1 · relevance 0.10

- **In one sentence**: The paper shows that additive cubes can be avoided over every ternary alphabet {0, a, b} with gcd(a,b)=1 and b ≥ 4, using a single pair of parameterized non-uniform morphisms of image length at most 6 applied to the Cassaigne et al. additive-cube-free word, with abelian-cube reduction and finite-graph certification for the remaining cases.
- **In plain words**: The question is whether an infinite string built from three symbols can avoid a certain repeating pattern, where a block appears three times in a row with the same "sum" of letter values. The authors give one construction that works for all three-symbol alphabets {0, a, b} with b at least 4 (and a, b having no common factor), extending an earlier result that needed b at least 6. Parts of the proof for large b rely on a reduction to a related pattern called abelian cubes, and the small remaining cases are checked by computer.
- **Why it matters**: This settles a conjecture posed by Rao (2015) for a range of alphabets, narrowing the gap to the smallest cases. It sits in the area of combinatorics on words, which studies which patterns can or cannot be avoided in long strings; the wider relevance is mainly to that field and to computer-checked proofs.
- **Background needed**: - Word combinatorics: a word is a finite or infinite string over an alphabet; a pattern is "avoidable" if some infinite word contains no instance of it.
- Additive cube: a block repeated three times in a row where the corresponding letter values sum to the same amount in each copy (letters are read as integers).
- Abelian cube: a block repeated three times where the blocks have the same letter counts, though not necessarily the same order.
- Morphism: a rule that replaces each letter by a fixed block of letters; "non-uniform" means the blocks can have different lengths. Image length is the length of those blocks.
- Dual pair: two related morphisms used together.
- Finite-graph method: a computer-checkable technique for proving that a family of words avoids a pattern. · level: research-level

<details><summary>Original abstract</summary>

We prove that additive cubes are avoidable over every ternary alphabet $\{0, a, b\}$ with $1 \le a < b$, $\gcd(a, b) = 1$, and $b \ge 4$, thereby solving and extending Rao's~(2015) conjecture from $b \ge 6$ down to $b \ge 4$. Our construction applies a single dual pair of parameterized non-uniform morphisms of image length at most~$6$ to the additive-cube-free word $\mathbf{w}$ of Cassaigne et al.~(2014). For $b \ge 10$, we prove that every additive square in the image is an abelian square, reducing additive cubes to abelian cubes; the absence of abelian cubes and the $24$ finite cases with $4 \le b \le 9$ are then certified via the finite-graph method of Jamet and Rosenfeld~(2026).

</details>

## Numerical analysis

### [A Coats-Based Formulation for Multiphase Reactive Transport Accounting for Aqueous Phase Disappearance](https://arxiv.org/abs/2611.27930)
*Thomas Jacumin, Roland Masson, Laurent Jeannin et al.* · `math.NA` · arXiv:2611.27930v1 · relevance 0.10

- **In one sentence**: The paper extends Coats' fully implicit formulation for multiphase reactive transport so that the aqueous (liquid water) phase can disappear and reappear during simulations, with a multiphase flash step handling phase appearance and a new set of basis-species concentration unknowns keeping the Jacobian nonsingular.
- **In plain words**: Storing hydrogen underground in a porous rock layer can change the gas through chemical reactions with water and minerals. Computer models of this often assume that liquid water is always present, but during gas injection and withdrawal near wells the water can evaporate and minerals can precipitate, so that assumption breaks down. The authors present a way to model these reactions and phase changes all at once, and test it on carbon dioxide storage benchmarks and a cyclic hydrogen storage case in an aquifer.
- **Why it matters**: Reliable simulation of underground hydrogen storage matters for assessing whether such storage is feasible as part of the energy transition. The text suggests the method avoids splitting errors from solving flow and chemistry separately, but its practical accuracy and cost are not detailed in the given text.
- **Background needed**: - Porous media: rock or sediment with connected pore spaces that hold fluids and gas.
- Multiphase flow: several fluids (gas, liquid water) moving together in those pores.
- Reactive transport: fluids carrying dissolved chemicals that react with each other and with minerals as they move.
- Globally implicit approach: solving flow and chemistry together in one system, rather than in alternating steps.
- Splitting error: inaccuracy introduced when flow and chemistry are solved in separate sequential steps.
- Flash calculation: a routine that determines how a mixture divides into phases (gas, liquid) at given conditions.
- Jacobian matrix: the table of derivatives used by numerical solvers; if singular, the solver cannot proceed.
- Basis species: a chosen set of independent chemical components used to describe all the others. · level: research-level

<details><summary>Original abstract</summary>

As part of the energy transition, underground hydrogen (H2) storage in porous media has emerged as an alternative solution for large-scale energy storage to salt caverns. Assessing the feasibility of such systems and ensuring their operation requires accurate modeling of the geochemical processes that may alter the composition of the stored gas. This results in a highly nonlinear coupled system of partial differential equations, ordinary differential equations, and algebraic constraints, calling for robust and specialized numerical strategies. In this work, we adopt a Globally Implicit Approach (GIA), as sequential solution algorithms are known to introduce splitting errors due to the decoupling of flow and geochemical processes. In addition, most splitting-based methods implicitly assume the persistent presence of the liquid phase, an assumption that may be violated during gas injection or withdrawal owing to aqueous phase vaporization and mineral precipitation in the vicinity of wells. We extend Coats' formulation to multiphase reactive transport with a rigorous and fully implicit management of aqueous phase disappearance and reappearance. The proposed approach introduces new molar concentration unknowns for basis species that track the re-appearance of the aqueous phase and guarantee the nonsingularity of the Jacobian matrix. Additionally, the appearance of the liquid phase is managed using a multiphase flash calculation algorithm. The proposed algorithm is validated against the CO2 storage benchmark problems. Finally, the approach is applied to an underground H2 storage in an aquifer under cyclic injection and withdrawal conditions.

</details>

### [Tackling Many-Body Coulomb Singularity by Randomization](https://arxiv.org/abs/2611.27851)
*Di Fang, Wook Yoon* · `quant-ph` · arXiv:2611.27851v1 · relevance 0.10

- **In one sentence**: The paper shows that Trotter and standard qDRIFT product formulas converge slowly for many-body Coulomb dynamics because of the singularity at close particle approach, and introduces a supersmoothing randomized qDRIFT variant whose error decreases linearly in the time step uniformly over all initial states.
- **In plain words**: The paper studies how to simulate quantum systems of interacting charged particles, such as electrons around atomic nuclei, on a quantum computer. The standard step-by-step methods become inaccurate because the electric force becomes infinitely strong when particles get very close. The authors show that randomizing the steps does not fix this by itself, and they propose a modified randomized method whose error shrinks in proportion to the step size.
- **Why it matters**: Simulating molecules is a leading expected use of quantum computers, so the cost of accurate simulation matters. The text claims the end-to-end gate count beats qubitization and high-order Trotter methods on the discretized Hamiltonian, but the comparison details are not in the given text, so the size of that gain is unclear.
- **Background needed**: - Product formulas (Trotter formulas): approximate the evolution of a quantum system by applying simpler pieces of the dynamics one after another in small time steps.
- Coulomb singularity: the electric interaction between charges grows without bound as they approach, which makes error analysis harder.
- Randomized product formulas (qDRIFT): pick pieces of the dynamics at random with suitable probabilities instead of in a fixed order.
- Error scaling: how the approximation error shrinks as the number of time steps grows; "linear" means halving the step roughly halves the error.
- Qubitization: another quantum simulation technique used here as a benchmark.
- Gate count: the number of elementary quantum operations needed, a proxy for cost. · level: research-level

<details><summary>Original abstract</summary>

Many-body Coulomb dynamics is central to quantum chemistry and molecular simulation, yet the Coulomb singularity undermines both the standard error analysis and performance of product formulas. Even for the simple hydrogen ground state, the celebrated Trotter formulas converge more slowly than their nominal order, and going to higher order does not help. Randomization by itself does not resolve this. We show that conventional qDRIFT suffers the same loss of accuracy, and that for general initial states, the errors of both Trotter formulas and qDRIFT can decrease more slowly than any power of the number of time steps (logarithmically). To overcome these limitations, we introduce supersmoothing qDRIFT, a randomized product formula that turns a physical property of free particle propagation into an algorithmic resource. Our algorithm achieves an error bound that decreases linearly with the time step, uniformly over \textit{all} initial states and without any smoothness or energy assumptions. Combined with spatial discretization analysis, the resulting end-to-end gate count improves on those of qubitization and high-order Trotter formulas applied directly to the discretized Hamiltonian, despite first-order convergence in time. This work demonstrates new ways of utilizing continuum dynamics to achieve algorithmic advantage.

</details>

## Logic and foundations

### [Rates of metastability for a generalization of the Halpern iteration](https://arxiv.org/abs/2611.27798)
*Nicoleta Dumitru, Laurentiu Leustean* · `math.OC` · arXiv:2611.27798v1 · relevance 0.05

- **In one sentence**: The paper uses proof-mining techniques to derive uniform rates of metastability for a generalized Halpern iteration (studied by Kanzow and Shehu), recovering rates for the Halpern, modified Halpern and Tikhonov-Mann iterations as special cases.
- **In plain words**: This paper is about iterative methods: step-by-step procedures that repeatedly refine a guess until it settles near a solution. The authors study a general family of such procedures, and ask how many steps are needed before the iterates stop changing much, a quantity called a "rate of metastability." They obtain such bounds for several known special cases and note that ordinary convergence results follow from these bounds.
- **Why it matters**: Knowing how quickly an iterative method settles gives a guarantee about how much computation is needed, not just that it eventually works. The text does not say what applications this has beyond the mathematical setting, so its wider significance is uncertain.
- **Background needed**: - Iteration: repeatedly applying the same update rule, each step using the previous result.
- Convergence: the sequence of iterates approaches a limit or solution.
- Metastability: a finite-horizon, logic-style form of convergence. For every tolerance and every starting point of a window, there is a point after which the iterates vary less than the tolerance over that window. The "rate" is an explicit bound on how far one must look.
- Uniform rate: a bound that depends only on the problem's general parameters, not on the particular starting point.
- Proof mining: a research program (led by Kohlenbach and others) that extracts explicit, quantitative information from existing non-constructive convergence proofs.
- Halpern iteration: a classical scheme for finding fixed points of nonexpansive (distance-non-increasing) maps, with several variants named in the text.
- Tikhonov-Mann iteration: another named variant of these fixed-point schemes. · level: research-level

<details><summary>Original abstract</summary>

We apply proof mining methods developed by Kohlenbach and the second author to compute uniform rates of metastability for a generalization of the Halpern iteration studied by Kanzow and Shehu. As special cases, we obtain rates of metastability for the Halpern and modified Halpern iterations, as well as for the Tikhonov-Mann iteration. Furthermore, convergence results are obtained as immediate consequences of our quantitative results.

</details>

## Mathematical physics

### [Consecutive Supersymmetric Quantum Mechanical Algorithms for Resolving the Spectra of Legendre-type Differential Operators](https://arxiv.org/abs/2611.27295)
*Tianchun Zhou* · `quant-ph` · arXiv:2611.27295v1 · relevance 0.06

- **In one sentence**: The paper proposes iterative algorithms built from consecutive supersymmetric quantum mechanics (SUSYQM) to compute the eigenspectra of the Legendre operator and related operators in various coordinate systems, using supersymmetry and shape invariance as guiding principles.
- **In plain words**: The paper concerns a standard class of equations from mathematical physics (Legendre-type differential operators) whose solutions describe quantities such as allowed energy levels. The authors build step-by-step computational procedures that find these allowed values by repeatedly applying a hidden pairing symmetry, without relying on the traditional power-series method. The abstract claims the procedures are simple, efficient and independent of the older methods, but the excerpt itself gives no worked examples or numerical comparisons.
- **Why it matters**: The work offers an alternative route to well-known spectra, and the authors suggest some of these algorithms could replace the popular power-series approach. Whether that holds in practice cannot be judged from the abstract alone, since the text provides no results or benchmarks.
- **Background needed**: - Differential operator: an equation-level rule (here, a Legendre-type equation) whose solutions are special functions used across physics.
- Eigenspectrum: the set of allowed values (such as energy levels) for which the equation has well-behaved solutions.
- Supersymmetric quantum mechanics: a method that pairs a problem with a related "partner" problem so that their energy levels are linked, allowing solutions to be built step by step.
- Shape invariance: a property where partner problems share the same mathematical form with shifted parameters, which makes the chain of steps solvable.
- Power series approach: the traditional method of solving such equations by writing the solution as an infinite sum of powers. · level: research-level

<details><summary>Original abstract</summary>

Quite comprehensive iterative algorithms based on consecutive supersymmetric quantum mechanics (SUSYQM) have been constructed heuristically, for resolving the eigenspectra of the Legendre operator and its associates parametrized in various coordinates, \emph{without receiving any input from traditional analytical methods}. On building these algorithms, the two symmetries \text{--} supersymmetry and shape invariance symmetry \text{--} hidden in these operators are brought to the fore as the only two governing principles, with the aids of the newly devised algebraic techniques such as the \emph{active supersymmetrization transformations}, \emph{momentum operator maps} as well as plain and \emph{higher-order spin matrix maps}. In view of their algebraic simplicity and elegance, high efficiency, as well as independence of traditional methods, some of these algorithms become the promising candidates to supplant the popular power series approach to the eigenspectra of Legendre-type operators.

</details>

### [Submanifolds, restriction of differential operators and Schouten-Nijenhuis bracket](https://arxiv.org/abs/2611.27912)
*J. Queva, J. Renaud* · `math.DG` · arXiv:2611.27912v1 · relevance 0.05

- **In one sentence**: The paper gives new, compact formulas for restricting the Hodge star, the codifferential and the Hodge Laplacian (operators on differential forms) to a submanifold, using the Schouten-Nijenhuis bracket and the generalized interior product.
- **In plain words**: The paper is about a technical question in geometry: if you have a rule for measuring or transforming shapes and fields in a space, how do you apply that rule when you only look at a smaller surface or curve sitting inside it? The authors write down new, shorter formulas for doing this for three standard operators. They say the formulas are concise and make explicit calculations easier in practice.
- **Why it matters**: Restricting these operators to a submanifold comes up when studying fields and waves on surfaces embedded in a larger space, so cleaner formulas can save effort in such calculations. The provided text is only the abstract, so I cannot say how widely the formulas apply or how they compare with existing approaches.
- **Background needed**: - Submanifold: a smaller curved surface or curve sitting inside a larger space, such as a sphere inside three-dimensional space.
- Differential forms: a general language for describing quantities like flux, area and volume, which can be integrated over shapes.
- Hodge operator (Hodge star): a rule that converts a form into its "complementary" form, linked to the geometry of the space.
- Codifferential and Hodge Laplacian: operators built from the Hodge star and differentiation; the Laplacian generalizes the familiar second-derivative operator that appears in heat and wave equations.
- Restriction: evaluating an operator only on the submanifold, using only information available there.
- Schouten-Nijenhuis bracket: an algebraic operation on multivector fields used as a bookkeeping tool here.
- Generalized interior product: a way of contracting a form with a vector-like object, used to simplify the formulas. · level: research-level

<details><summary>Original abstract</summary>

In this article, we present new formulas for restricting the Hodge operator, the codifferential and the Hodge Laplacian to a submanifold. These formulas are concise, thanks to the use of tools for differential forms (Schouten-Nijenhuis bracket and generalized interior product). They also facilitate explicit calculations for practical applications.

</details>

## Optimization and control

### [Error-Corrected Physics-Informed Neural Operator for Optimal Control of Unmanned Aerial Vehicles under Uncertainty](https://arxiv.org/abs/2611.27272)
*Oliver Lundqvist, Fabricio Oliveira* · `math.OC` · arXiv:2611.27272v1 · relevance 0.17

- **In one sentence**: A physics-informed DeepONet surrogate, trained only on the dynamics residual and corrected by one Newton step computed with a parallel scan, is used to solve open-loop optimal control of a fixed-wing UAV under parametric uncertainty across many scenarios at once.
- **In plain words**: The paper looks at how to plan flight paths for a drone when some of its physical settings are not known exactly. Instead of solving each possible case separately, it trains a neural network that predicts the drone's trajectories for all sampled cases in one go. A single mathematical correction step then tightens these predictions so the optimizer is not misled by small mistakes in the network.
- **Why it matters**: Planning under uncertainty usually means solving many similar problems, which is slow, so a faster way to do this could matter for robust vehicle control. The paper reports matching the accuracy of two standard solvers while running about 8 to 15 times faster on the benchmark it tested; the text does not show how well this carries over to other vehicles or real flights.
- **Background needed**: - Optimal control: choosing inputs (e.g., control surfaces, throttle) over time to reach a goal at the lowest cost, subject to the laws of motion.
- Parametric uncertainty: some model values (such as wind or mass) are unknown and are treated as a range of possible scenarios.
- Neural operator (DeepONet): a neural network that learns a mapping from input functions or settings to whole solution curves, so it can be reused for new targets and time horizons.
- Physics-informed training: the network is trained to satisfy the governing equations (the dynamics residual) rather than fitted to data from solved examples.
- Newton step: one iteration of a classic root-finding method that nudges an approximate solution toward one that satisfies the equations.
- Parallel scan: an algorithm that computes sequential time-step updates simultaneously on a GPU.
- Adam and Ipopt: a gradient-based optimizer commonly used to train neural networks, and a standard nonlinear optimization solver, used here as baselines. · level: research-level

<details><summary>Original abstract</summary>

We solve open-loop optimal control problems under parametric uncertainty using a physics-informed DeepONet that returns trajectories for all sampled scenarios in one evaluation. Trained only on the residual at generic controls, the operator is reused across targets and horizons. Because a gradient-based optimizer exploits surrogate errors, we correct the prediction by one Newton step on the dynamics, computed for all scenarios and times by one parallel scan. The corrected state has a second-order error bounded by the residual alone, and the corrected cost is honest for every control up to the sampling error. On a fixed-wing UAV benchmark, the corrected operator matches the accuracy of a batched Adam solver and an Ipopt solver at equal sample size and is 8 times faster than the Adam solver on the same GPU at a few hundred scenarios and 15 times faster than Ipopt on a CPU.

</details>

### [Boundary gradient asymptotics for superquadratic viscous Hamilton--Jacobi equations via optimal control](https://arxiv.org/abs/2611.27484)
*S. E. Nikitin* · `math.AP` · arXiv:2611.27484v1 · relevance 0.15

- **In one sentence**: The paper derives sharp boundary gradient asymptotics for maximal solutions of a superquadratic viscous Hamilton–Jacobi equation on arbitrary bounded C² domains, resolving a Lasry–Lions conjecture for bounded state-dependent terms and extending to singular terms, using stochastic optimal control and boundary blow-up analysis.</one_liner>
<parameter name="plain">The paper studies a equation that describes how a quantity u varies in space and how steeply it rises near the edge of a region, when the rise is driven by a power of the slope greater than 2. The authors find the precise way the slope grows as one approaches the boundary, for any smooth bounded region, and they also handle cases where the driving term becomes singular near the edge. They get these results by recasting the equation as a control problem where a random process is steered at lowest cost, and by studying how the solution blows up near the boundary.
- **Why it matters**: The text says the result settles a conjecture of Lasry and Lions and removes the geometric restrictions that earlier boundary asymptotics needed, which matters for the theory of such equations. Its link to applications beyond this theory is not stated in the text, so I cannot say more.
- **Background needed**: - Hamilton–Jacobi equation: a nonlinear partial differential equation describing optimal cost or value functions in control problems.
- Viscous term (−Δu): a diffusion or noise term that smooths the solution; here the equation is elliptic.
- Superquadratic gradient term |∇u|^p with p > 2: the nonlinearity grows faster than the square of the slope, which drives steep boundary behavior.
- Maximal solution: the largest solution of the equation, which is the one that corresponds to the optimal control value.
- Boundary gradient asymptotics: precise description of how the slope of the solution behaves as one approaches the boundary.
- Stochastic optimal control: choosing controls for a randomly moving system to minimize an expected cost; dynamic programming is the standard tool for it.
- Blow-up analysis: rescaling near a point where the solution becomes very large to extract a limiting profile.
- Ergodic problem: a long-run average-cost version of the control problem. · level: research-level

<details><summary>Original abstract</summary>

We study the boundary behavior of the maximal solution of \[ -\Delta u + |\nabla u|^{p} + \lambda u = f \] on arbitrary bounded $C^{2}$ domains, where $p > 2$ and $\lambda > 0$. For bounded state-dependent terms $f$, we resolve a conjecture of Lasry and Lions by establishing sharp boundary gradient asymptotics without geometric restrictions on the domain. Previously, such asymptotics were established only for certain classes of domains with additional restrictions on $p$ and $f$. We also extend the analysis to state-dependent terms that may be singular near the boundary and obtain sharp boundary profiles and gradient asymptotics. Our approach relies on stochastic optimal control and boundary blow-up analysis. Dynamic programming estimates and comparisons of near-optimal trajectories establish tangential invariance of boundary blow-up limits, leading to the identification of one-dimensional profiles and the asymptotic formulas. For the associated state-constrained control problem, we establish sharp asymptotics for the minimizing feedback and deduce its admissibility and optimality, with corresponding results for the ergodic problem.

</details>

## Statistics theory

### [Estimating contextual networks via Fisher-scoring surrogate likelihood](https://arxiv.org/abs/2611.26886)
*Myung Jin Lee, Fangzheng Xie* · `stat.ME` · arXiv:2611.26886v1 · relevance 0.06

- **In one sentence**: A tuning-free likelihood method, using a smooth surrogate likelihood and Fisher scoring, estimates latent positions in contextual generalized random dot product graphs with high-dimensional low-rank vertex covariates, with consistency and asymptotic normality established for the estimator.
- **In plain words**: The paper looks at networks, where data points are linked in pairs (such as people who know each other), and each point also carries a list of measured attributes. The authors propose a way to place each point at a hidden location that accounts for both the links and the attributes, without needing extra settings that depend on how sparse the network is. They report that the estimator is consistent and asymptotically normal, and they apply it to real data as a demonstration.
- **Why it matters**: Many real networks come with attributes for each node, and combining the two sources of information is a common need. The paper argues that existing spectral methods can be suboptimal and require tuning parameters that depend on unobservable quantities, so a tuning-free likelihood approach is of interest to people working on network and covariate data; the text does not show how it compares to these methods beyond these claims.
- **Background needed**: - A network (graph) is a set of nodes joined by edges; here, a model places each node at a hidden "latent position" and the chance of an edge depends on those positions.
- Vertex covariates are measured attributes attached to each node.
- Random dot product graphs are a model where edge probability is given by the inner product of latent position vectors.
- Spectral methods estimate positions using eigenvectors of a matrix, usually needing a tuning parameter.
- Likelihood-based estimation picks the parameter values that make the observed data most probable; Fisher scoring is an iterative numerical way to find that maximum.
- Consistency means estimates converge to the true values as data grow; asymptotic normality means their errors are approximately bell-curve distributed in large samples.
- Tuning parameters are settings the user must choose by hand. · level: research-level

<details><summary>Original abstract</summary>

When networks are accompanied by vertex-level covariates, effectively integrating and aligning the information underlying both data sources becomes a natural yet critical task. Current spectral approaches, despite their popularity, may yield suboptimal results and necessitate the specification of additional tuning parameters that are contingent upon unobservable signal-to-noise ratios. We propose a tuning-free, likelihood-based learning framework for estimating latent positions in contextual generalized random dot product graphs in the presence of high-dimensional vertex covariates with a low-rank structure. Our method constructs a smooth surrogate likelihood and implements a Fisher-scoring algorithm to iteratively estimate latent positions without introducing additional tuning parameters that depend on the network sparsity. We establish the consistency and asymptotic normality of the Fisher-scoring estimator. Application to real-world data further demonstrates the method's practical utility, offering a principled and scalable alternative to spectral approaches for analyzing contextual networks in high-dimensional settings.

</details>

### [On the Role of Fisher Information, Variance and Asymptotics in Statistical Inference](https://arxiv.org/abs/2611.27683)
*Paul W. Vos* · `math.ST` · arXiv:2611.27683v1 · relevance 0.06

- **In one sentence**: A reading of Bahadur's asymptotics chapter (MLE normality, Fisher's bound, Hodges's counterexample, local asymptotic normality) that replaces point estimators with a continuum of significance tests assessed by Fisher information, which yields an exact bound that differs geometrically from the Cramér–Rao bound.
- **In plain words**: This paper is about the mathematical limits on how precisely a quantity can be estimated from data, which statisticians have long described using approximations for large samples. The author revisits the standard large-sample results and re-describes them in terms of a family of significance tests rather than a single estimate, measuring the information they carry. The text reports that, under this view, the statements hold exactly at every sample size, and it gives an example where a t-test family keeps about half an observation's worth of the information in the sample mean.
- **Why it matters**: It offers a reframing of classical results like Fisher's bound and Hodges's counterexample, which are central to how statisticians think about efficiency. The connection to other fields is not described in the text, so its wider relevance is unclear.
- **Background needed**: - Maximum likelihood estimator: the value of a parameter that makes observed data most probable.
- Fisher information: a measure of how much data reveal about an unknown parameter, based on how sensitive the likelihood is to it.
- Variance and mean square error: measures of how spread out or inaccurate an estimate is.
- Cramér–Rao bound: a lower limit on the variance of an unbiased estimator, given by inverse Fisher information.
- Superefficiency and Hodges's estimator: a known counterexample where an estimator beats the usual limit at one parameter value.
- Asymptotic normality: the approximation that estimates behave like a bell curve as sample size grows.
- Significance test: a procedure for judging whether data are consistent with a hypothesis.
- Companion paper: the author's earlier work applying the same reframing to the preceding chapters. · level: research-level

<details><summary>Original abstract</summary>

Bahadur's \emph{Lectures on the Theory of Estimation} close with a chapter on asymptotics: asymptotic normality of the maximum likelihood estimator, Fisher's bound on its asymptotic variance with Hodges's counterexample, and local asymptotic normality. A companion paper read the earlier lectures with one modification, replacing the point estimator by a generalized estimator---Fisher's continuum of significance tests---assessed by information rather than variance. This paper reads Chapter 8 the same way. At each of its three parts the classical statement is an approximation about a point estimator, while the corresponding statement about the score is exact at every sample size. Superefficiency does not arise, because information is bounded by the Fisher information at every $n$; Hodges's estimator, computed exactly, is fully efficient at the origin and loses information only where its mean square error is worst. The information of a generalized estimator is argued to be Fisher information: the mean rate at which a continuum of tests responds to the parameter, standardized by its variance. The resulting Fisher upper bound differs geometrically, not merely algebraically, from the Cram\'er--Rao lower bound. The extension is not empty: the $t$-test continuum loses about half an observation's worth of the information in $\bar X$ at every $n$.

</details>

## Statistical methods and applications

### [graphMTP: An R Shiny Interface for Graphical Multiple Testing and Interim Monitoring](https://arxiv.org/abs/2611.27052)
*Valerie Le, MengYang Yi, Philip He* · `stat.CO` · arXiv:2611.27052v1 · relevance 0.09

- **In one sentence**: This paper presents graphMTP, an R Shiny application for building graphical multiple testing procedures with per-hypothesis group-sequential interim monitoring, alpha recycling, and JSON export of designs and histories.
- **In plain words**: Clinical trials often test several questions at once, and each test must be guarded so that the chance of any false "success" stays small. This paper describes a software tool, graphMTP, that lets analysts draw the rules for these tests as a graph, set up planned interim looks at the data, and see how unused significance budget gets passed on to other tests. The text describes the tool's features and worked examples; it does not report clinical findings.
- **Why it matters**: Trials that test several endpoints or patient groups need careful bookkeeping, and an interactive tool that records the exact boundaries used at each look could make such designs easier to check and reproduce. The text does not give any evidence of adoption or of how it compares with existing tools, so its practical reach is unclear.
- **Background needed**: - Multiple testing: testing several hypotheses inflates the chance of a false positive, so the overall error rate (family-wise error rate) must be controlled.
- Graphical procedure: hypotheses are nodes in a graph; each carries a share of the significance level (alpha), and when one is rejected its share is passed ("recycled") to neighbours.
- Group-sequential design: data are examined at planned interim looks, with stopping boundaries that keep the error rate under control across looks.
- Spending profile: a rule that sets how much error budget is used at each interim look.
- Local significance level: the threshold applied to one hypothesis at a given look.
- Fixed-sequence gatekeeping: hypotheses are tested in a set order, each only after the previous one succeeds. · level: research-level

<details><summary>Original abstract</summary>

Graphical multiple testing procedures provide a framework for controlling the family-wise error rate across endpoints, treatment comparisons, and patient populations in confirmatory clinical trials. Interim monitoring requires analysts to track changing local significance levels together with hypothesis-specific testing schedules. We present graphMTP, an R application built with shiny, for constructing hypothesis graphs, specifying per-hypothesis group-sequential plans, and inspecting alpha recycling. The application uses TrialSimulator for graph updates, gsDesign for spending profiles, and rpact for boundary calculations. It records the local levels, boundaries, and decisions used for each submitted test and exports designs and histories as JSON files. Worked examples cover fixed-design reallocation, fixed-sequence gatekeeping, delayed activation, and retesting a previously monitored recipient of alpha. Replication code checks graph updates, normal crossing probabilities, and saved-session replay. Sequential tests use a prespecified information schedule and reconstruct the complete local boundary family at the current allocation, including after recycling. Historical event records retain the boundaries actually used. An installable package and standalone sources accompany the article.

</details>

### [Scalable Matrix-Free Algorithms for Variance Estimation of Survey-Weighted Survival Curves](https://arxiv.org/abs/2611.27867)
*Jingchen Liang* · `stat.ME` · arXiv:2611.27867v1 · relevance 0.08

- **In one sentence**: The paper presents two matrix-free algorithms that compute the conventional Taylor-linearization variance of survey-weighted Kaplan-Meier-type survival curves without forming the full event-time covariance matrix, validated on NHATS data and simulations.
- **In plain words**: When researchers estimate how long people survive in a large survey, the uncertainty around the survival curve can take a lot of computer time and memory to calculate, especially when many distinct event times occur. This paper describes two alternative calculation methods that avoid building a huge intermediate table, and that give the same results as the existing R implementation. On a 7-year study of 7,608 older adults with 2,879 deaths, run times dropped from about 26 minutes to a few seconds.
- **Why it matters**: The work targets a practical bottleneck: standard software can run out of memory on demanding survey analyses, while the proposed methods finished those cases. Its relevance beyond this one dataset and software setup is not established by the text.
- **Background needed**: - Survival curve: the estimated share of people still alive over time.
- Survey weights: numbers that make a sample represent a larger population; they change how uncertainty is computed.
- Variance estimate: a measure of how much the estimate would vary across repeated samples; here it is a standard error-type quantity.
- Taylor linearization: a standard approximation that turns a complicated estimate into a sum of per-person contributions to estimate its variance.
- Primary sampling unit (PSU): a cluster (such as a neighborhood) from which survey respondents were drawn; variance is often aggregated at this level.
- Matrix-free computation: calculating a result by accumulating sums directly, rather than storing a large grid of pairwise values in memory.
- NHATS: the National Health and Aging Trends Study, a US survey of older adults. · level: research-level

<details><summary>Original abstract</summary>

Variance estimation for survey-weighted survival curves using existing statistical software can require substantial time and memory, particularly when the number of distinct event times is large. We developed two matrix-free algorithms that compute the conventional Taylor linearization variance estimator without constructing the full event-time covariance matrix: one accumulates individual-level linearization contributions, while the other directly updates aggregated contributions at the primary sampling unit (PSU) level. We evaluated numerical accuracy, runtime, and peak memory usage through an application to the National Health and Aging Trends Study (NHATS) and simulation experiments. Both approaches yielded survival and variance estimates identical to the R implementation. In the 7-year follow-up analysis of 7,608 NHATS participants with 2,879 deaths, computation time decreased from approximately 26 minutes to less than 3 seconds with the individual-level approach and less than 1 second with the PSU-level approach. Simulations with sample sizes of 1,000 to 10,000 showed similar results, with more pronounced computational advantages as sample size and the number of distinct event times increased. In more demanding settings, the existing implementation failed due to memory exhaustion, whereas both proposed approaches completed successfully. Matrix-free computation can improve the efficiency and scalability of design-based variance estimation while preserving numerical accuracy.

</details>

## AI industry news

### [Anthropic launches Claude Ship, letting AI agents review, fix, and approve code changes](https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/)
*Sarah Perez* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.09

- **In one sentence**: Anthropic has announced developer tools ("Claude Ship") that let AI agents review, fix, and approve code changes, aimed at easing the review bottleneck created by growing volumes of AI-generated code.
- **In plain words**: Software teams increasingly use AI to write code, and the human step of checking and approving those changes is becoming a slowdown. Anthropic's new tools let AI agents take over some of the routine checking and sign-off work. The article is a short announcement; it does not report measured results.
- **Why it matters**: If AI agents can safely handle routine approvals, software teams could ship changes faster, which matters for how much human oversight stays in the loop. The text is too brief to say how well the tools work or what safeguards exist, so the practical impact is unclear.
- **Background needed**: - "Agent": an AI system that carries out multi-step tasks on its own, not just answering a single question.
- "Code review": a process where another engineer reads proposed software changes before they are accepted.
- "Bottleneck": a stage in a process that slows everything downstream, here the human review step.
- "Pull request" or "merge": the standard way a proposed code change is submitted to and accepted into a project.
- The article gives no details on accuracy, testing, or how approvals are audited. · level: introductory

<details><summary>Original abstract</summary>

As AI-generated code piles up, Anthropic's new developer tools aim to eliminate another bottleneck by letting agents handle routine approvals.

</details>

### [Supertake raises $20M to let AI agents turn your market predictions into stock portfolios](https://techcrunch.com/2026/11/23/supertake-raises-20m-to-let-ai-agents-turn-your-market-predictions-into-stock-portfolios/)
*Sarah Perez* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.06

- **In one sentence**: A news item reports that startup Supertake raised $20M and offers AI agents that convert a user's market views into stock portfolios, though the text is only a short teaser with few details.
- **In plain words**: Supertake is a startup that says you can act on your own ideas about where the stock market is going without choosing individual stocks yourself. Its AI agents, which are software programs that act on a user's behalf, turn those predictions into a portfolio, meaning a bundle of investments. The article is very short, so it does not explain how this works in practice or how well it performs.
- **Why it matters**: It is a small example of AI being pitched as a way for ordinary people to invest on their own views, which may matter to debates about automated investing and financial advice. The text gives too little detail to judge whether the approach is sound or significant.
- **Background needed**: - A "startup" is a young company, often funded by investors; "raising $20M" means it received $20 million in new investment.
- A "stock portfolio" is a collection of shares in different companies held as one investment.
- "AI agents" are AI programs that carry out multi-step tasks for a user, rather than only answering questions.
- Turning a prediction into a portfolio means a system must choose which stocks to buy and in what amounts to reflect the user's view.
- The article offers no information on fees, regulation, risk, or track record, so these remain unknown. · level: introductory

<details><summary>Original abstract</summary>

Think you know where the market is headed? A startup called Supertake lets you put money behind your ideas without having to pick the stocks yourself.

</details>

### [Sierra doubles valuation to $30B within six months as demand for AI in CX takes off](https://techcrunch.com/2026/11/23/sierra-doubles-valuation-to-30b-within-six-months-as-demand-for-ai-in-cx-takes-off/)
*Ivan Mehta* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.06

- **In one sentence**: Sierra, a customer-experience AI startup co-founded by former Salesforce co-CEO Bret Taylor, reportedly raised $1.75 billion in a Series F round, roughly doubling its valuation to $30 billion within six months.
- **In plain words**: Sierra is a company that builds AI tools for businesses to handle customer service and similar interactions. It announced on Monday that it has raised $1.75 billion from investors, a funding round that pushes its estimated company value to about $30 billion. The article presents this as a sign of strong demand for AI in customer experience.
- **Why it matters**: The article is a funding announcement, not a research result, so it mainly signals investor confidence in AI for customer service. Whether the demand it describes lasts is not shown in the text; the article gives no revenue or customer figures.
- **Background needed**: - Series F: a late-stage round of private fundraising, typically after several earlier rounds (A, B, and so on).
- Valuation: the estimated total worth of a company, often set by the price investors pay for shares. A doubling in six months is a fast rise.
- Customer experience (CX): how a company's customers interact with it, including support chat, phone, and service.
- Bret Taylor: former co-CEO of Salesforce, a large business software firm; he co-founded Sierra.
- The article gives no details on Sierra's products, customers, revenue, or investors. · level: introductory

<details><summary>Original abstract</summary>

Enterprise customer experience company Sierra, co-founded by former Salesforce co-CEO Bret Taylor, said on Monday that it has raised $1.75 billion in a Series F round.

</details>

### [Nvidia employees greet Jensen Huang like a hero as he returns to company’s HQ](https://techcrunch.com/2026/11/23/nvidia-employees-greet-jensen-huang-like-a-hero-as-he-returns-to-companys-hq/)
*Amanda Silberling* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.06

- **In one sentence**: A short news piece reporting that Nvidia employees welcomed CEO Jensen Huang warmly on his return to the company's headquarters, with Huang saying he intends to be a better CEO "the second time around."
- **In plain words**: This is a brief report about Nvidia, the chipmaker that makes the processors used to train and run many AI systems. Its co-founder and chief executive, Jensen Huang, came back to the company's headquarters and was greeted warmly by staff, and he told them he plans to be a better CEO this time. The text is only a single quoted line and a headline, so it does not say why he left or came back, or what changes he plans.
- **Why it matters**: Nvidia is one of the central companies in the AI hardware business, so changes in its leadership are followed closely by investors and the industry. The article alone does not explain the circumstances of his absence or return, so its wider significance is unclear.
- **Background needed**: - Nvidia designs graphics and AI chips (GPUs) that are widely used to build and run AI models.
- Jensen Huang is Nvidia's co-founder and long-serving chief executive.
- "CEO" means chief executive officer, the top manager of a company.
- The phrase "the second time around" suggests he had stepped away from the role or been absent before, but the text does not give details.
- The source text is very thin: a headline and one quote, with no context, dates, or company statements. · level: introductory

<details><summary>Original abstract</summary>

"I'm going to be a better CEO the second time around," Huang told employees.

</details>

### [Why data centers are at the center of the Big Tech backlash](https://techcrunch.com/2026/11/22/why-data-centers-are-at-the-center-of-the-big-tech-backlash/)
*Anthony Ha* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.06

- **In one sentence**: A news piece summarizing journalist Paris Marx's new book "Hyperscale," which frames data centers as a focal point of growing public criticism of Big Tech.
- **In plain words**: This article is about the growing public pushback against Big Tech companies over the huge computer facilities, called data centers, that run online services and AI. It introduces journalist Paris Marx's new book, "Hyperscale," which looks at why these facilities have become a point of conflict. The text provided is only a short teaser, so it does not report specific findings or details of the book's arguments.
- **Why it matters**: Data centers are where much of the computing for AI and cloud services happens, so local and political objections to them may affect how the industry expands. The text is too brief to say how strong the backlash is or what the book concludes.
- **Background needed**: - Data center: a large building full of servers that store data and run online services and AI models.
- Hyperscale: a term for the very largest data centers, typically run by a few major cloud companies.
- Big Tech backlash: public criticism of large technology companies, covering issues such as power use, local impacts, and market power.
- Paris Marx: a journalist and host who writes about technology and its political and economic effects. · level: introductory

<details><summary>Original abstract</summary>

Journalist Paris Marx unpacks his new book "Hyperscale."

</details>

## Model architectures and training

### [Model Carving: Training Transformers That Optimize Their Own Topology](https://arxiv.org/abs/2611.27962)
*Kaden Zheng, Pratyusha Sharma* · `cs.LG` · arXiv:2611.27962v1 · relevance 0.29

- **In one sentence**: Model Carving trains a Transformer's weights and its layer structure together in one run by attaching learnable scalar gates to each sublayer, so the training loss can switch off components and leave a smaller, non-uniform network.
- **In plain words**: Standard language models are built with the same fixed set of building blocks repeated at every layer, and the design is usually chosen by convention rather than tested. This paper proposes letting training itself decide which parts of the network to keep, so the final model ends up smaller and irregular. The authors report that, at equal training compute, these "carved" models reach lower validation loss than dense models, and run faster with fewer operations per token.
- **Why it matters**: If the approach holds up, it suggests that small, efficient models for devices could come from training rather than from shrinking a large model after the fact. The text claims gains over pruning and distillation, but these are the authors' own experiments, and the summary does not show how robust the results are across other settings.
- **Background needed**: - Transformer: the neural network design behind most modern language models, made of stacked layers, each with attention and feed-forward (MLP) sublayers.
- Sublayer: one component inside a layer; here, each can be switched on or off.
- Learnable scalar gate: a single adjustable number that scales a component's contribution; training can push it toward zero, effectively removing that component.
- Validation loss: a measure of prediction error on held-out text; lower is better.
- FLOPs: floating-point operations, a rough measure of computation cost.
- Pruning and distillation: standard ways to make a smaller model, by cutting parts of a trained large model or by training a small model to imitate it.
- Looped Transformer: a variant that reuses the same layers repeatedly. · level: research-level
- Matched keywords: transformer, attention, distillation, architecture

<details><summary>Original abstract</summary>

Machine learning has largely kept separate the choice of architecture and the process of training. A classic Transformer, for instance, trains a fixed set of attention and MLP sublayers at every layer, in the same order, and optimizes the weights within. This uniformity is a convention rather than a principled design choice, and it is likely suboptimal: the best architecture for a given task may be smaller, more efficient, and far from uniform. We believe that, ideally, training itself should shape the model's topology. To this end, we introduce Model Carving, which learns both a Transformer's weights and its architecture in a single run. By applying learnable, scalar gates to each sublayer, we allow the training loss to remove the model's own components during training -- freeing a smaller heterogeneous network inside. We evaluate Model Carving by pre-training standard Transformers from 140M to 2.7B parameters and looped Transformers from 140M to 1.3B. At equal training compute, carved models reach a lower validation loss than dense models trained with up to 1.7 times more compute. Furthermore, carved models also outperform size-matched models produced by pruning or distillation, suggesting that the best way to obtain small models for edge devices is to carve them during training, not to compress a large one afterwards. This advantage both grows with scale and carries over to downstream tasks such as few-shot evaluation and generation. Because the removed sublayers no longer run, carved models also cost up to 34% fewer FLOPs per token and decode up to 1.6 times faster without cost in quality. Our results show that architecture, like weights, should be learned and not fixed in advance, and that inside every large transformer is a smaller, faster, stronger one waiting to be carved out.

</details>

### [BusemannFormer: Horospherical Self-Attention for Hyperbolic Graph Transformers](https://arxiv.org/abs/2611.27167)
*Youheng Yao, Ziyao Zeng, Wenbo Liao et al.* · `cs.LG` · arXiv:2611.27167v1 · relevance 0.25

- **In one sentence**: Proposes Horospherical Self-Attention, a hyperbolic attention mechanism that scores keys by Busemann depth along ideal-boundary directions, integrated into a fully hyperbolic graph Transformer (BusemannFormer) with log-depth and finite-boundary-dictionary variants.
- **In plain words**: Graph data often has a tree-like hierarchy, such as categories nested inside categories or citation networks. This paper designs a new attention mechanism, a way for a neural network to decide which parts of the data to focus on, that works in a curved "hyperbolic" space which suits tree-like structures. Its key idea is to measure how deep each item sits along a chosen direction toward the edge of that space. The authors report that their model, BusemannFormer-LD, beats the baselines they tested on several node-classification benchmarks.
- **Why it matters**: Hierarchical data is common, and existing hyperbolic Transformers mostly adapt standard attention without using the geometry of the space's boundary, so this is a different design angle. The text does not show how large or consistent the gains are, so its practical value is not yet established.
- **Background needed**: - Graph neural network: a model that learns from nodes and their connections, here used to classify nodes.
- Attention / Transformer: a mechanism where each item weighs how relevant every other item is.
- Hyperbolic space: a curved geometry in which tree-like hierarchies can be embedded with little distortion.
- Ideal boundary: the "edge at infinity" of hyperbolic space; directions point toward it.
- Busemann function / horosphere: a way of measuring depth toward a boundary point; level sets of it are horospheres (curved surfaces).
- Flat limit: the case where the curvature shrinks to zero, recovering ordinary dot-product attention.
- Node classification: predicting a label for each node in a graph. · level: research-level
- Matched keywords: transformer, attention

<details><summary>Original abstract</summary>

Hyperbolic neural networks excel on hierarchical graph data, yet existing hyperbolic Transformers largely adapt conventional attention without explicitly exploiting the ideal boundary, a geometric structure closely tied to tree hierarchy. We propose Horospherical Self-Attention (HSA): each query selects an ideal-boundary direction and scores keys by their Busemann depth along that direction, yielding a token-to-token hyperbolic attention kernel. We establish a flat-limit connection to dot-product attention, characterize score level sets as horospheres, and bound key-side gradients. HSA is integrated into BusemannFormer, a fully hyperbolic graph Transformer, with a log-depth variant that uses query depth to modulate attention concentration. We further introduce a finite-boundary-dictionary extension supporting linear-complexity global attention. Experiments on hierarchical and citation graphs show that BusemannFormer-LD outperforms the evaluated baselines on several node-classification benchmarks and achieves competitive performance across diverse graph structures.

</details>

## Machine learning theory

### [The Optimal Sample Complexity of Agnostic PAC Learning for Partial Concept Classes](https://arxiv.org/abs/2611.27946)
*Liang-Yu Zou* · `cs.LG` · arXiv:2611.27946v1 · relevance 0.25

- **In one sentence**: The paper gives a deterministic agnostic PAC learner for partial concept classes (hypotheses that may abstain with a star) of finite VC dimension d, using O((d+log(1/δ))/ε²) samples and outputting a total classifier, and says this matches the lower bound of Alon et al. (FOCS 2021).
- **In plain words**: This is about teaching a computer to make yes/no predictions from examples when the data may be noisy and the set of allowed rules is allowed to "abstain" on some inputs. The authors describe a learning procedure that reaches a near-best rule using a number of examples that scales as the complexity of the rule family divided by the square of the allowed error, and they state that no procedure can do substantially better. The text reports this as a matching upper and lower bound on how many examples are needed.
- **Why it matters**: Settling the exact number of examples needed for a basic learning task is a foundational question in learning theory, and the stated match with a known lower bound is what makes the result notable. The text does not show the technical construction, so its broader relevance to practical learning is unclear from this excerpt alone.
- **Background needed**: - PAC learning: a formal model where a learner sees random labelled examples and must output a rule that is approximately correct with high probability.
- Agnostic learning: no assumption that a perfect rule exists; the goal is to do nearly as well as the best rule in a given family, even when labels are noisy.
- Partial concept class: a family of rules that may output +1, -1, or a star meaning "no prediction" on some inputs.
- VC dimension: a single number measuring how complex a family of rules is; larger means more examples are needed.
- Sample complexity: how many training examples are required to reach a target accuracy.
- Lower bound: a proof that no learner can succeed with fewer examples than a stated amount.
- Total concept: a rule that gives a yes/no answer on every input, with no abstention. · level: research-level
- Matched keywords: sample complexity

<details><summary>Original abstract</summary>

Let $\mathcal H\subseteq\{-1,+1,\star\}^{\mathcal X}$ be a partial concept class of finite VC dimension $d$. We construct a deterministic agnostic PAC learner that, for every $\varepsilon,\delta\in(0,1)$, uses $O((d+\log(1/\delta))/\varepsilon^2)$ i.i.d. examples from an arbitrary distribution $\mathcal D$ over $\mathcal X\times\{-1,+1\}$ and returns a total concept $\hat h:\mathcal X\to\{-1,+1\}$ satisfying $\text{er}_{\mathcal D}(\hat h)\leq \min_{h\in\mathcal H}\text{er}_{\mathcal D}(h)+\varepsilon$ with probability at least $1-\delta$, where $\text{er}_{\mathcal D}(h)=\mathbb P_{(x,y)\sim\mathcal D}[h(x)\neq y]$. This establishes the optimal sample complexity, matching the lower bound of Alon et al. (FOCS 2021).

</details>

### [Geometrically Constrained Learning II: Agnostic Proper Learning of Lipschitz Functions](https://arxiv.org/abs/2611.27700)
*Jane Lange, Cassandra Marcussen, Arsen Vasilyan* · `cs.LG` · arXiv:2611.27700v1 · relevance 0.19

- **In one sentence**: The paper gives a proper (outputs a Lipschitz function) agnostic learner for Lipschitz functions under Gaussian input, using L1 polynomial regression with a convex gradient constraint followed by a local correction based on the lower Lipschitz envelope.
- **In plain words**: The paper studies how to learn a rule that maps numbers to numbers from examples, where the rule must change no faster than a set speed limit (a "Lipschitz" function). The inputs are assumed to be random draws from a Gaussian (bell-curve) distribution in d dimensions. The authors describe an algorithm that returns a function obeying the speed limit and whose error is small, and they state its running time and sample needs as (d+1) raised to a power that depends on the speed limit and target error.
- **Why it matters**: The text claims a learner that always returns a function with the required smoothness, which is harder than merely predicting well, and also covers the case where labels are noisy or arbitrary, with the error compared to the best possible Lipschitz approximator. Its relevance beyond theory is not discussed in the text, so broader significance is unclear.
- **Background needed**: - Lipschitz function: a function whose outputs cannot change faster than a fixed multiple of input changes (a bounded "steepness").
- Proper learner: one that outputs a function from the target class itself, here a Lipschitz function.
- Agnostic learning: performance is measured against the best function in the class, even when the data do not come from that class.
- Gaussian distribution: the standard bell-curve distribution over inputs.
- L1 regression: fitting a model by minimizing average absolute error.
- Polynomial regression: fitting a polynomial to data.
- Sample complexity and running time: how many examples and how much computation are needed.
- Sublevel set: the set of inputs where a function's value is at or below some threshold. · level: research-level
- Matched keywords: sample complexity

<details><summary>Original abstract</summary>

We give a proper learner for Lipschitz functions over the Gaussian distribution on $\mathbb{R}^d$. Given random Gaussian examples labeled by a $\lambda$-Lipschitz function, $\lambda \ge 1$, the learner returns a function $h:\mathbb{R}^d\to\mathbb{R}$ that is globally $\lambda$-Lipschitz and has loss (absolute or squared) at most $\varepsilon$. The sample complexity, running time, and representation size are \[ (d+1)^{\mathsf{poly}(\lambda/\varepsilon)}. \] The learning algorithm can be made \emph{agnostic}, given a known bound on the variance of the label marginal distribution. Some known control of label scale is information-theoretically necessary. For arbitrary labels with variance at most $V^2 \ge 1$, the complexity is \[ (d+1)^{\mathsf{poly}(V\lambda/\varepsilon)}, \] and the error is $\mathsf{opt} + \varepsilon$, where $\mathsf{opt}$ is the minimal error among Lipschitz approximators. Our approach combines $L_1$ polynomial regression under a convex gradient constraint with local correction of the Lipschitz property. The learner finds a polynomial that, after smoothing and clipping its range, is very close to a canonical Lipschitz correction of itself, the lower Lipschitz envelope. Our local corrector modifies the lower envelope by replacing distances to sublevel sets with a Gaussian sampling proxy, allowing the construction to be locally and stably estimated from samples.

</details>

## Large language models

### [Silent Arbitration: How Large Language Models Resolve Co-Authoritative Conflicting Instructions](https://arxiv.org/abs/2611.27444)
*Sihyeon Lee, Jiwoo Kum, Jihun Song et al.* · `cs.CL` · arXiv:2611.27444v1 · relevance 0.13

- **In one sentence**: This paper measures how five LLMs handle a single prompt that assigns two opposing personas with equal authority, across eight conflict types, looking at whether they disclose the conflict, how they resolve it, and which side their answers lean toward.
- **In plain words**: Chatbots are often given instructions about who to be, such as a role, values, or a tone. This paper asks what happens when one prompt gives two incompatible roles at equal weight with no rule for choosing between them. The authors tested five language models and found that the models often notice the clash when asked directly (72% of the time) but rarely mention it in their actual answers (22%), so they quietly pick a side instead.
- **Why it matters**: It matters for anyone who relies on AI systems following instructions, since a model that hides a conflict and silently favors one side may be hard to audit. The text does not go beyond its own measurements, so its broader implications for deployment are not established here.
- **Background needed**: - Large language model (LLM): an AI system trained on large amounts of text that generates responses to written prompts.
- Persona: a role or identity a prompt asks the model to adopt, such as a character or a type of speaker.
- Co-authoritative conflict: two instructions that clash but are given equal weight, with no tie-breaking rule.
- Silent arbitration: the model settling the conflict without telling the user that a conflict existed.
- Dominance vs. compromise: the response either follows one persona mostly, or tries to blend both; the paper notes compromise answers can still lean one way.
- Directional stance: which of the two personas a response tilts toward. · level: intermediate

<details><summary>Original abstract</summary>

Large language models increasingly receive high-level instructions about roles, values, interests, and communication style. Such instructions can conflict even when a prompt assigns them equal authority and provides no priority rule. We study co-authoritative persona conflict, in which a single prompt jointly assigns two opposing personas. Across eight conflict types grounded in published source material and five LLMs, we measure conflict acknowledgment, resolution strategy, and directional stance. Models acknowledge incompatibility in 72% of direct checks but explicitly surface it in only 22% of task responses, revealing silent arbitration. Dominance accounts for 45% of dual-persona responses, and 35% of compromise-labeled responses retain directional lean. Prompt framing further changes the visible form of arbitration substantially more than ordinary paraphrase variation. These findings show that evaluating instruction following should assess whether models disclose conflicts, how they resolve them, and which persona their responses favor.

</details>

### [Do Language Models Know Which Words Steer Their Reasoning?](https://arxiv.org/abs/2611.27317)
*Yanbei Jiang, Chao Lei, Jey Han Lau et al.* · `cs.CL` · arXiv:2611.27317v1 · relevance 0.12

- **In one sentence**: The paper shows that language models' chain-of-thought reasoning is steered by semantically irrelevant prompt words that the models themselves deny are relevant, and proposes an inference-time intervention (Online KV Suppression) that zeroes out the cache entries of one such word to improve accuracy.
- **In plain words**: When AI language models work through a problem step by step, it is unclear which words in the prompt actually shape their reasoning. The authors find that models are pulled by words that have no real bearing on the question, and when asked, the same models say those words don't matter. They then test a simple fix: they remove the influence of one such word while the model is generating its answer, which raised accuracy on several reasoning tests.
- **Why it matters**: It points to a gap between what a model's internal behavior is doing and what it reports about itself, which matters for trusting explanations of AI reasoning. Whether the reported gains hold beyond the tested models and benchmarks is not something the summary establishes.
- **Background needed**: - Chain-of-thought (CoT): prompting a model to write out intermediate reasoning steps before its final answer.
- Next-token distribution: the model's probability scores over possible next words; the paper measures how these shift.
- Leave-one-out analysis: testing the effect of a piece of input by deleting it and seeing how the output changes.
- Jensen-Shannon divergence (JSD): a standard measure of how different two probability distributions are.
- KV cache: the stored internal memory of earlier words that a model consults when generating new ones; zeroing entries effectively hides those words from the model.
- Percentage points: the difference between two accuracy rates, not a relative change. · level: research-level

<details><summary>Original abstract</summary>

While chain-of-thought (CoT) prompting elicits intermediate reasoning steps from language models, it is unclear which words in the context actually steer the CoT. We identify Phantom Context Influence (PCI): language models are disproportionately steered by semantically irrelevant context words, even as the same models deny those words' relevance when asked. To localize PCI, we introduce Leave-One-Out Word JSD analysis, which removes one context word at a time from the otherwise intact context to isolate its marginal effect on the next-token distribution; words whose removal flips the prediction (pivot words) are passed to the same LLM to self-judge whether it recognizes this predictive dependence. Across four models and three benchmarks, language models largely do not know which words steer their reasoning, a mismatch we call the Generation-Judgment Contradiction. Inspired by this phenomenon, we propose Online KV Suppression: it scores every prompt word's influence over the whole chain of thought in a single pass, then zeroes the KV-cache entries of the highest-influence word the model itself judges inert and redecodes. This single-word intervention improves CoT accuracy across four models and five reasoning benchmarks, by up to 8.9 percentage points on math reasoning benchmark.

</details>

## Computer vision

### [Leakage-Free Is Not Confounder-Free: What a Patient-Level Split Cannot Certify About a Medical Imaging Benchmark](https://arxiv.org/abs/2611.27585)
*Ignazio Gallo, Mattia Gatti, Leonardo Sgroi et al.* · `cs.CV` · arXiv:2611.27585v1 · relevance 0.15

- **In one sentence**: A five-question audit shows that on the DMR-IR breast thermography benchmark, the acquisition date alone predicts malignancy better than any imaging model, so a patient-level split cannot rule out this confounder.
- **In plain words**: Medical AI studies often split data so that no patient appears in both training and test sets, and this paper argues that this does not guard against every shortcut. Using a public set of breast heat-camera images from 236 patients, the authors found that the year a scan was taken predicted cancer better than any of nine image-based approaches, because benign and malignant cases were recorded in different years. They also report that a second, separately collected cohort, where patient age plays this role, gave the same result.
- **Why it matters**: It suggests that high scores on a widely used medical imaging benchmark may reflect how and when scans were collected rather than disease itself. The lesson about confounders applies beyond thermography to any medical dataset where recording conditions track the diagnosis.
- **Background needed**: - Confounder: a hidden factor linked to both the outcome and the data, so a model can learn it instead of the real signal.
- Patient-level split: dividing data so each patient is entirely in training or entirely in testing, to prevent memorizing individuals.
- AUROC: a 0 to 1 score for how well a test ranks positive cases above negative ones; 0.5 is chance, 1.0 is perfect.
- Breast thermography: using infrared cameras to measure skin temperature patterns of the breast.
- Acquisition date/year: when the scan was taken; equipment, protocols or staff can drift over time.
- Cross-label same-date pairs: patients with different diagnoses scanned on the same date, which would allow fairer comparisons; the paper notes there are only eight such pairs. · level: intermediate

<details><summary>Original abstract</summary>

Patient-level splitting is the standard safeguard against subject leakage in medical imaging evaluation, but it cannot remove a confounder that every fold inherits: an acquisition variable aligned with the diagnosis across the whole cohort. We present a five-question audit of a candidate confounder: how well it predicts the diagnosis, whether it can be decoded from the images, whether diagnostic scores depend on it, whether the image adds predictive value beyond it and how much discrimination survives once it is controlled. We apply it to DMR-IR, the public dataset on which most machine-learning results in breast thermography rest. On 236 patients under a strict patient-disjoint protocol, the acquisition date alone predicts malignancy at AUROC 0.980, above the best of nine imaging arms (0.949), because benign and malignant patients were recruited in different years. The acquisition year is decodable from the pixels among patients who share a diagnosis, largely through a global thermal offset outside the breast, yet only one arm, the one pooling every frame of a visit, demonstrably carries it into its diagnostic score. No arm improves on the date on paired folds, and once the date is controlled, discrimination either collapses or survives only on comparisons the benchmark cannot attribute. The dataset contains only eight cross-label same-date pairs, from ten patients, which limits reliable evaluation within recorded acquisition-date groups. A second, independently acquired cohort, whose dominant channel is patient age, returns the same audit outcome from a different confounder. Mitigation may suppress such a confounder, but without cross-label acquisition support no evaluation on the benchmark can certify that what remains is pathology.

</details>

### [When Perception Collides with Priors: Diagnosing Modal Polarization in Video Understanding Models](https://arxiv.org/abs/2611.26972)
*Yao Tong, Jiaxin Qi, Yan Cui et al.* · `cs.CV` · arXiv:2611.26972v1 · relevance 0.14

- **In one sentence**: The paper names a failure mode, "Modal Polarization," in video-understanding multimodal LLMs when what they see clashes with their built-in priors, and introduces TheaterBench to probe it with counter-intuitive video scenarios.
- **In plain words**: Video AI models are trained on realistic footage, so they can struggle when a video shows something that breaks physics or common sense. The authors describe two opposite ways these models go wrong: they either stick to what they expect despite the visual evidence, or they trust the video blindly and ignore that the scene makes no sense. They built a test set, TheaterBench, of such surprising scenes and report that current top models show this polarization, and that some methods meant to reduce hallucinations mostly shift the problem from one extreme to the other.
- **Why it matters**: Models that cannot reconcile what they see with what they know could be unreliable in unusual real-world situations, which matters for any use that depends on accurate video interpretation. The text presents the benchmark as an early step for evaluation rather than a solved problem, and its broader impact is not established beyond the reported experiments.
- **Background needed**: - Multimodal Large Language Models (MLLMs): AI systems that take in several input types, here video and text, and answer questions about them.
- Hallucination: when an AI states something unsupported by its input, such as describing an event that did not happen.
- Priors: the expectations a model learned from training data, such as "objects fall downward."
- Benchmark: a standardized test set used to compare models.
- De-hallucination methods: techniques intended to reduce made-up or unsupported outputs.
- Counter-intuitive scenarios: deliberately constructed videos that violate physical laws or common sense. · level: intermediate

<details><summary>Original abstract</summary>

Multimodal Large Language Models (MLLMs) have achieved strong video comprehension, largely benefiting from extensive training on realistic video data. However, when video perception severely conflicts with internal priors or common sense, we identify a critical failure pattern termed Modal Polarization, where models fail to integrate modalities and instead bifurcate into two distinct extremes: Cognitive Inertia, where models rigidly adhere to priors despite contradictory visual evidence, and Perceptual Inertia, where they blindly trust video perception while ignoring logical inconsistencies. To investigate this, we introduce TheaterBench, a benchmark designed to expose Modal Polarization using counter-intuitive scenarios that violate physical laws or common sense - situations rarely encountered in standard training distributions. Extensive experiments reveal that current state-of-the-art (SOTA) models exhibit severe Modal Polarization, and many de-hallucination methods merely rebalance the trade-off between Perceptual and Cognitive Inertia rather than fundamentally resolving the conflict. This work serves as a foundational step for evaluating and enhancing the perceptual-cognitive equilibrium of future video understanding models.

</details>

## Reinforcement learning

### [Learning Inside Types: Epistemic Typestates for Safe Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.27631)
*Lorenzo Bacchiani, Mario Bravetti, Giovanni Pau et al.* · `cs.AI` · arXiv:2611.27631v1 · relevance 0.17

- **In one sentence**: The paper proposes "epistemic typestates," a type discipline in which each agent's type is a protocol over its beliefs about which worlds are still possible, permitting only actions safe in every such world, and reports soundness and team-safety proofs (mechanised in Rocq) plus benchmark results for safe multi-agent reinforcement learning.
- **In plain words**: The paper is about teaching groups of learning software agents to act safely while they learn together. The authors treat safety like a type rule in programming: each agent gets a type that limits which actions it may take, based on what it can rule out from its own observations, and each agent's type is built and checked separately without the agents talking to each other. Their tests on nine benchmarks report no safety violations from the typed learners, task performance comparable to two recent shielding methods, and fast type construction for ten agents.
- **Why it matters**: Safety guarantees that hold for every policy a learner might produce, rather than only for those tested, would matter for robots or systems where errors are costly. The text reports proofs and benchmark comparisons, but these are the authors' own results, and how well they transfer to real-world settings is not shown in the text.
- **Background needed**: - Reinforcement learning: an agent learns by trial and error which actions earn rewards.
- Multi-agent setting: several learners act in a shared environment, and each one's safety can depend on what the others do.
- Type system: a rule set in programming that rejects code that could go wrong in specified ways before it runs.
- Typestate: a type that tracks what state an object is in and which operations are allowed then.
- Shield: a runtime filter that blocks unsafe actions chosen by a learner.
- Lagrangian method: a common way to add safety limits to learning by penalising constraint violations, which can still allow violations during training.
- Mechanised proof (Rocq): a mathematical proof checked by a computer proof assistant. · level: research-level
- Matched keywords: reinforcement learning

<details><summary>Original abstract</summary>

Type disciplines make programs safe by construction: components checked against each other's types compose into programs that cannot go wrong in the ways the types exclude. Types suit reinforcement learning: a type constrains what an agent may choose, not how it chooses, so the guarantee holds for every policy a learner produces. We introduce epistemic typestates, a type discipline for safe multi-agent reinforcement learning. An agent's type is a protocol whose states record its beliefs, the worlds it cannot rule out from its own observations and actions, and permits only actions that are safe in every world of the belief, whatever the others do within their public types. Agents learn inside their types, which are built and checked one agent at a time and run without communication. We prove type soundness and team safety, give a synthesis that is sound and complete, build types from guards when worlds are infinite, and show that shields are a special case. All proofs are mechanised in Rocq. On nine benchmarks, no typed learner causes a safety violation, and task performance does not differ significantly from that of two recent multi-agent shielding methods. Where a contract-based method fails at five and ten agents, types for ten agents are built in under a second. In the two continuous benchmarks, Lagrangian learners cause thousands of violations in every training run.

</details>

### [SLICR: Strategy Logic-Guided Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.27865)
*Arshia Rafieioskouie, Matthew Lucas, Tzu-Han Hsu et al.* · `cs.AI` · arXiv:2611.27865v1 · relevance 0.17

- **In one sentence**: SLICR uses Strategy Logic specifications (with LTL objectives and constraints) to shape rewards for multi-agent reinforcement learning under adversarial settings and partial observability, evaluated on Predator-Prey, Google Research Football, and an extended SMAC-HARD.
- **In plain words**: This paper is about teaching groups of software agents to act well when they compete against other agents and can only see part of what is happening. The authors write goals as formal logic rules, so the agents get rewarded for meeting them. They report testing the method on three standard game-like benchmarks and say it works, scales, and adapts to different opposing strategies.
- **Why it matters**: Writing goals as precise logical rules could make it easier to say exactly what an AI agent should do, including how it should respond to rivals. The text gives only the abstract, so the strength of the results and how they compare with existing methods cannot be judged from it; the "paradigm shift" wording is the authors' own framing.
- **Background needed**: - Reinforcement learning: an agent learns by trying actions and getting rewards or penalties.
- Multi-agent setting: several learning agents act at once, sometimes against each other.
- Partial observability: each agent sees only part of the situation.
- Specification-guided RL: formal rules describing desired behavior are turned into reward signals.
- Linear temporal logic (LTL): a notation for rules about how things must unfold over time, such as "eventually reach X and never do Y".
- Strategy Logic (SL): an extension that lets you state rules about the strategies agents choose, not just their single actions.
- Benchmarks: standard test games (Predator-Prey, Google Research Football, StarCraft Multi-Agent Challenge) used to compare methods. · level: research-level
- Matched keywords: reinforcement learning

<details><summary>Original abstract</summary>

Specification-guided reinforcement learning (RL) translates formal specifications of desired behavior of agents into shaped rewards. This paper introduces SLICR, a significant paradigm shift that advances the state of the art to specification-guided RL in adversarial settings under partial observability. We employ Strategy Logic (SL), which allows explicit quantification over agents' strategies and uses the linear temporal logic (LTL) to specify the agents' objectives and constraints. This enables reasoning not only about how agents should act to satisfy a specification, but also about how they should respond to the strategies and behaviors of other agents. We evaluate SLICR on three popular benchmarks: Predator-Prey, Google Research Football, and our home-grown extension of SMAC-HARD, demonstrating its effectiveness, scalability, and ability to adapt to diverse adversarial strategies.

</details>

## AI safety and alignment

### [Jagged Robustness: Uneven Safety Transfer and Emerging Vulnerabilities under LLM Quantization](https://arxiv.org/abs/2611.27424)
*Ramneek Agnihotri, Yingte Xu, Hans Vath* · `cs.AI` · arXiv:2611.27424v1 · relevance 0.20

- **In one sentence**: An audit of how weight quantization (compressing a language model's parameters) affects safeguards, instruction-following, ethics/bias and truthfulness in Qwen3-4B, introducing the term "Jagged Robustness" for uneven transfer of these properties to compressed models.
- **In plain words**: Language models are often shrunk with a technique called quantization so they run faster and on cheaper hardware. This paper checks whether a shrunken model keeps the same behavior across different areas: some areas, like refusing unsafe requests and bias, got worse, while others, like truthfulness, stayed fairly steady. The authors also found that a specially crafted text suffix that does nothing harmful to the full model could push the compressed version into producing content it should refuse.
- **Why it matters**: Many people run compressed models in practice, so if safety behavior shifts after compression without anyone noticing, deployed systems could be less safe than their original tests suggest. The text reports results for one model (Qwen3-4B), so how far the pattern generalizes is not established from this text alone.
- **Background needed**: - Quantization: storing a model's numbers (weights) at lower precision to save memory and speed up inference, with some loss of detail.
- Safeguards / jailbreaks: training that makes a model refuse harmful requests; a jailbreak is an input that gets around that refusal.
- Adversarial suffix: a string of seemingly random text appended to a prompt to steer the model's output.
- Benchmarks: standard test sets used to score model behavior on tasks.
- Qwen3-4B: a specific open-weight language model with about 4 billion parameters. · level: intermediate
- Matched keywords: jailbreak

<details><summary>Original abstract</summary>

Quantization enables efficient inference in language models through model parameter compression. This work audits the impact of quantization on capability and safety domains including model safeguards, instruction-following, ethics and bias. Through benchmarks, we find that model safeguards and bias can degrade under quantization, while other capabilities such as truthfulness remain more stable in Qwen3-4B. We define this uneven transfer of LLM capabilities under quantization as Jagged Robustness. We find multiple factors driving Jagged Robustness: task complexity, evaluation method and generation coherence. Moreover, we verify the degradation of model safeguards by observing increased compliance with unsafe requests under quantization, and demonstrate universal adversarial suffix attacks that are benign for the full model but jailbreak quantized models. The findings indicate that it is risky to assume that the performance and robustness can transfer evenly across different capability domains from full models to quantized models.

</details>

### [No Perfect Guardrail & No Perfect Guard: On the Decidability of Output Policies for Large Language Models](https://arxiv.org/abs/2611.27260)
*Ahmed Amer, Loren Kinczel, Darrell D. E. Long* · `cs.AI` · arXiv:2611.27260v1 · relevance 0.15

- **In one sentence**: The paper uses computability theory to show that a computable guard can exactly separate forbidden from permitted language-model outputs only when the output policy is decidable, and that undecidable policies force infinite misclassification.
- **In plain words**: The paper asks whether a safety filter (a "guardrail") can perfectly block forbidden text from an AI model while letting all allowed text through. It proves that this is possible only when the rule being enforced is one a computer can always settle yes or no, and that for harder rules any filter must make infinitely many mistakes. The authors also argue that treating guardrails as a guarantee of safety is an ethical failure, so people remain responsible for the rules themselves.
- **Why it matters**: It gives a formal limit on what automated output filtering can guarantee, which bears directly on how AI safety claims are made and evaluated. The text is a theoretical and philosophical argument; its practical reach for real deployed guardrails is not shown in the excerpt.
- **Background needed**: - Guardrail: a filter or check placed on an AI system's outputs to block unwanted content.
- Decidable policy: a rule for which a computer program can always correctly answer yes or no for every input, in finite time.
- Undecidable problem: a question that provably no general algorithm can always answer correctly (the classic example is the halting problem).
- Misclassification: wrongly blocking an allowed output or letting a forbidden one through.
- Computable guard: a filter that some algorithm can actually run.
- Execution monitor: a runtime checker that watches a program's behavior as it runs, distinct from a filter on finished outputs.
- The paper's examples include arithmetic truth, program behavior, and harmful instructions. · level: research-level
- Matched keywords: oversight

<details><summary>Original abstract</summary>

Expecting guardrails to provide a general guarantee of safety fails to recognize the limits of computational enforcement and policy specification. We argue that promising such perfection is an ethical failure of precision, and that invoking it to abdicate responsibility is a moral failure. Guardrails can support responsible action, but cannot relieve researchers, developers, policymakers, or users of their obligations to examine what they claim, permit, and prevent. We establish a precise computational boundary. If every finite string is a possible output of a language model, a computable guard that blocks every forbidden output and passes every permitted one exists if and only if the policy is decidable. For an undecidable policy, every guard misclassifies infinitely many strings, and every guard that blocks all forbidden outputs excludes infinitely many permitted ones. We apply this characterization to arithmetic truth, program behavior, and harmful instructions to an idealized recipient. We distinguish guards from execution monitors, identify bounded and interceptable cases admitting exact enforcement, and explain why the results establish no positive lower bound on average error. Exact enforcement does not establish that a policy adequately captures safety. Conservative exclusion may withhold warnings, remedies, or challenges needed to recognize the policy's own defects. Human oversight cannot substitute for judgment: an apparent controller can become an instrument of purposes they have ceased to examine. Responsible governance requires continued critical challenge and the intellectual and moral humility to recognize possible flaws in our machines, rules, policies, and ourselves. The impossibility of a general assurance of perfection is a condition responsible practice must confront, not a responsibility that another guardrail - or another guard - can remove.

</details>

## Interpretability

### [H-MSAE: Hierarchical Sparse Concept Coverage for Efficient and Diverse Instruction Data Selection](https://arxiv.org/abs/2611.27329)
*Bohan Cui, Jingyi Cui, Hongwei Wen et al.* · `cs.AI` · arXiv:2611.27329v1 · relevance 0.20

- **In one sentence**: H-MSAE selects compact, diverse, high-quality instruction-tuning subsets by building a coarse-to-fine concept hierarchy from a Matryoshka sparse autoencoder, avoiding generated tags and explicit graphs.
- **In plain words**: Companies train AI chatbots on huge collections of example instructions and answers, and many of these examples repeat each other. This paper proposes a way to pick a smaller set of examples that keeps the useful variety and good quality while costing less to train on. The authors report that on the Tulu 3 data pool their selected 50K subsets scored highest on their average benchmark measure among the selectors they tested, and that their method ran roughly five times faster end-to-end than the MIG baseline.
- **Why it matters**: Training cost and data redundancy are practical concerns for anyone fine-tuning language models, so a cheaper selection method is of interest. The text does not show how broadly the gains hold beyond the Tulu 3 pool and the evaluated selectors, so its general significance is unclear.
- **Background needed**: - Instruction tuning: further training a language model on example prompts paired with good responses so it follows instructions.
- Data selection: choosing a subset of a large training pool to save compute while keeping performance.
- Sparse autoencoder: a model that re-expresses internal representations as a small number of active "concept" features; a Matryoshka version learns features at several nested levels of detail.
- Diversity and redundancy: many training examples cover the same content, so keeping one representative of each topic can be enough.
- Effective rank: a measure of how many independent directions a set of representations spans, used here as a rough diversity indicator.
- Baseline comparison: MIG is an existing selection method the authors compare against for runtime. · level: research-level
- Matched keywords: sparse autoencoder

<details><summary>Original abstract</summary>

Large instruction-tuning corpora contain substantial semantic redundancy, motivating the selection of compact subsets that preserve useful supervision while reducing training cost. Existing diversity-aware selectors often rely on generated semantic tags and explicit graph structures, introducing considerable annotation and preprocessing overhead. We introduce H-MSAE, a hierarchical sparse instruction selection framework that organizes multi-resolution concepts learned by a Matryoshka sparse autoencoder into a coarse-to-fine hierarchy. Quality-weighted, diminishing-return coverage with ancestor propagation promotes high-quality and non-redundant semantic coverage, while pool-relative length constraints regulate subset composition. We motivate this design through a local quality-diversity analysis of subset SFT utility and examine it using example-quality and representation-space diversity diagnostics. On Tulu 3 data pool, H-MSAE achieves the highest Final Avg among the evaluated 50K selectors across scales and initialization. The selected subset also exhibits the highest mean quality and effective rank among the evaluated methods. By avoiding full-pool generative tagging and supporting efficient sparse selection, H-MSAE reduces measured end-to-end runtime by approximately $5\times$ relative to MIG.

</details>

### [Can Language Models See the Circuit in Pixelated RFIC Passives?](https://arxiv.org/abs/2611.27559)
*Jonathan Zhou, Kaushik Sengupta* · `cs.AI` · arXiv:2611.27559v1 · relevance 0.16

- **In one sentence**: A frontier language model, run without tools, is tested on reading, predicting, and debugging pixelated (inverse-designed) RFIC passive structures against full-wave EM simulation, with a limited simulation budget for the debugging step.
- **In plain words**: Chip designers use computer-optimized patterns for small electrical components on microwave chips. These patterns look like QR codes and are hard for people to read or fix when they misbehave. This paper asks whether a language model can look at such a pattern, predict how it will respond to signals across 20 to 100 GHz, and suggest edits to fix a failing design.
- **Why it matters**: It tests whether language models could serve as a reading and debugging aid for designs that people find opaque, which matters for the growing use of automatically designed chip parts. The text does not show how general these results are beyond the specific layouts tested, so the broader claim should be treated cautiously.
- **Background needed**: - RFIC: radio-frequency integrated circuit, a chip handling radio and microwave signals.
- Passives: components like inductors, resistors and capacitors that do not amplify signals; here, metal patterns on a grid of tiles.
- Inverse design: an optimization algorithm searches for a layout that meets a performance target, rather than a human drawing it.
- Tile grid: the layout is a square grid (18x18 or 27x27) where each cell is filled or empty.
- Input impedance and Smith chart: a way of describing how a circuit resists and reacts to a signal at each frequency, drawn as a curve on a circular chart.
- Full-wave EM simulation: a detailed physics simulation of electromagnetic fields, used as the reference truth here and expensive to run.
- GA (genetic algorithm): a search method that evolves candidate designs by mutation and selection.
- Transmission-line model: a simpler approximation that treats the structure as a straight wire; the paper says it ignores bends. · level: research-level
- Matched keywords: interpretability

<details><summary>Original abstract</summary>

The emergence of inverse-designed, pixelated passives for microwave and millimeter-wave applications has been a major development in the field of RFIC design. These devices, which appear to be QR-code-like in structure, exist in a generalizable, high-dimensional design space that includes conventional passive topologies. However, these structures are naturally unintuitive for designers, and failures or deviations in performance are difficult to debug. In this work, we ask whether a frontier language model can understand, predict, and edit the responses and layout structure of pixelated passives. The agent, run with all tools disabled, is first asked to read layouts on 18x18 and 27x27 tile grids and, in a single reply, predict the input impedance and loss of the structure from 20-100 GHz. On eight GA-synthesized layouts and five random fills, the predicted Smith-chart locus follows full-wave simulation results closely, with a systematic shift that places features about 16% lower in frequency than EM. On multipath loop structures it identifies notches successfully but shows a smaller frequency bias, about half that of an ideal transmission-line model that ignores bends. The agent is then asked to debug seven designs that fail their specification, and given a budget of five EM simulations and at most twelve changed tiles, it is able to improve all seven and bring five designs within specification. These experiments suggest language models can serve as an interpretability and debugging tool for traditionally non-intuitive inverse-designed passives.

</details>

## AI for mathematics

### [Isolating the Language Shell: A Content-Controlled Study of Multilingual Reasoning](https://arxiv.org/abs/2611.27053)
*Hoejoon Kwon, Jinhee Jang, Byeonggeuk Lim et al.* · `cs.CL` · arXiv:2611.27053v1 · relevance 0.15

- **In one sentence**: A controlled study showing that, with the same verified English math reasoning content, the language "shell" used to present training data (English, translated, or mixed) changes how well small student models reason in several target languages.
- **In plain words**: Some AI models learn to solve math problems by copying worked solutions from a stronger "teacher" model. This paper asks whether the language those solutions are written in matters, when the actual reasoning stays the same. The authors wrote the same verified solutions in English, in translated target languages, and in mixed-language versions, then trained two student models and tested them on math problems in three languages.
- **Why it matters**: The paper suggests that the wording language of training data is a separate design choice, not just a side effect of how data is generated or translated. This matters for building math-capable AI for non-English speakers, though the abstract alone does not show how large or general the effects are.
- **Background needed**: - Distillation: training a smaller "student" model to imitate a larger "teacher" model's outputs.
- Chain-of-thought reasoning: step-by-step written working that a model produces before its final answer.
- Content control: holding the underlying math content fixed so that only the surface form (the "shell") varies.
- Pre-training compatibility: how well a model's original training on many languages already fits a given language.
- Output-language behavior: which language the student actually writes its answers in, which can differ from the language it was trained on.
- The abstract reports that effects vary by student, language, and difficulty, and that no single pattern clearly predicts them. · level: research-level
- Matched keywords: mathematical reasoning

<details><summary>Original abstract</summary>

Multilingual reasoning distillation requires choosing the language in which teacher reasoning is presented, yet existing recipes often entangle linguistic form with differences in generation, translation, and filtering. We construct content-controlled supervision by rendering the same verified English trajectories into English, translated target-language, and language-mixed shells, and fine-tune two pretrained students in three target languages, evaluating them on multilingual mathematical reasoning at two difficulty levels. Even with the underlying reasoning content held fixed, we find that shell choice can change downstream accuracy, with effects varying across students, languages, and difficulty levels. Pre-training compatibility does not consistently track these outcomes, and even when our tests find no clear accuracy difference between shells, their output-language behavior can still differ substantially. These results suggest that the supervision shell is a distinct design choice in multilingual reasoning distillation.

</details>

### [Reinforcement Learning Unlearns Corrupted SFT Reasoning](https://arxiv.org/abs/2611.26756)
*Anika Misra, Shreyas Vinod, Huteng Dai* · `cs.CL` · arXiv:2611.26756v1 · relevance 0.14

- **In one sentence**: On GSM8K math word problems, the paper reports that GRPO reinforcement learning recovers accuracy from heavily corrupted supervised fine-tuning data, and that a few minimal, incorrect "form-only" traces make a better RL starting point than gold traces.
- **In plain words**: Language models are often first taught with worked examples (supervised fine-tuning) and then refined with reward-based trial and error (reinforcement learning). This paper asks what happens when the worked examples are badly corrupted. The authors deliberately damaged training solutions in 361 settings, up to 100% of the data, and found that the reinforcement learning stage largely recovered accuracy to about 60%.
- **Why it matters**: The finding challenges the assumption that the quality of the first training stage strongly determines final performance, which matters for how training data is collected and curated. The text reports only one dataset (GSM8K) and a specific RL method, so how far the result generalizes to other tasks or models is not shown here.
- **Background needed**: - Supervised fine-tuning (SFT): training a model to imitate example solutions.
- Reinforcement learning (RL): improving a model by rewarding correct final outcomes rather than copying examples.
- GRPO (Group Relative Policy Optimization): a specific RL method that compares several sampled answers to the same question against each other.
- GSM8K: a benchmark set of grade-school math word problems.
- "Form" versus "function": here, form means the layout or structure of a reasoning trace; function means whether the reasoning actually works.
- Correlation (r approximately 0): the SFT score and the final score showed essentially no linear relationship across the runs. · level: research-level
- Matched keywords: mathematical reasoning

<details><summary>Original abstract</summary>

We show that reinforcement learning (RL) in reasoning tasks can succeed even when the supervised fine-tuning (SFT) data is severely corrupted. In a mathematical reasoning dataset (GSM8K), we systematically corrupt training trajectories across 361 configurations by injecting realistic error types, varying error locations, trace-answer consistency, and corruption ratios up to 100%. While aggregated SFT-only performance steadily deteriorates under corruption (dropping from 43.61% to 13.80%), Group Relative Policy Optimization (GRPO) post-training consistently restores model accuracy back to gold-baseline levels (approximately 60%). Crucially, initializing RL with as few as N = 8 minimal, incorrect, three-line "form-only" traces boosts post-RL performance to 69.30%, outperforming standard gold SFT initialization (60.71%) and GRPO without SFT (35.00%). Further, we show that SFT accuracy is largely uncorrelated with post-RL accuracy (r approximately 0), demonstrating a fundamental asymmetry in post-training: SFT primarily establishes structural layout (form), while RL independently discovers functional reasoning (function).

</details>

## Robotics and embodied AI

### [Analysis of Multi-Client Inference Techniques for Vision-Language-Action Models](https://arxiv.org/abs/2611.26944)
*Stefan de Lasa, Mohammadreza Mofayezi, Gennady Pekhimenko et al.* · `cs.DC` · arXiv:2611.26944v1 · relevance 0.18

- **In one sentence**: A systems characterization of how standard multi-client serving techniques (batching and co-execution) trade off latency, throughput, power, and hardware utilization when serving Vision-Language-Action robot control models.
- **In plain words**: Robot control models that take camera images and text instructions and output motor actions are often run on shared computer hardware. This paper asks what happens when several robots (clients) send requests to the same model at once, and it measures how well common ways of sharing that hardware work for these models. The text says the authors measured trade-offs across speed, capacity, power use, and how busy the hardware is, but it does not list specific numbers in the summary provided.
- **Why it matters**: Robots running these models often leave expensive accelerator hardware idle between computations, so better sharing could make serving cheaper and more practical. The text frames the work as groundwork for future systems that serve several robot models at once, though it is unclear from the summary how far the findings extend beyond the tested setups.
- **Background needed**: - Vision-Language-Action model (VLA): a neural network that reads camera images and a written instruction and outputs robot movements.
- Inference: running a trained model to get an output, as opposed to training it.
- Serving: hosting a model on a server so that many clients can send it requests.
- Batching: grouping several requests together so the hardware processes them in one pass, which usually raises throughput but can add waiting time.
- Co-execution: running several models or tasks on the same hardware at the same time.
- Latency, throughput, utilization: how long one request takes, how many requests are handled per second, and what share of the hardware's capacity is in use. · level: intermediate

<details><summary>Original abstract</summary>

Vision-Language-Action models (VLAs) are a new class of machine learning model for generalizable robot control. While they enable robots to perform complex tasks in unseen environments, serving VLAs leaves hardware idle between inference passes and under-utilized during inference. Serving multiple clients at once can improve utilization, but fundamental multi-client techniques such as batching and co-execution have not been characterized for VLAs. We therefore characterize the trade-offs these known techniques impose across latency, throughput, power, and hardware utilization. Our findings inform trade-offs and challenges for future multi-VLA serving systems.

</details>

### [Generalist Action Critic: Harnessing Frontier Models in Autonomous Driving](https://arxiv.org/abs/2611.27804)
*Yun Yan, Shizhi Hu, Zhichao Li et al.* · `cs.RO` · arXiv:2611.27804v1 · relevance 0.16

- **In one sentence**: GAC is a zero-shot, inference-time harness in which a frozen frontier vision-language model acts as a critic that checks, and may swap, trajectories proposed by specialized driving planners, evaluated on HUGSIM and NAVSIM v1.
- **In plain words**: Self-driving systems often pick a planned path that turns out unsafe. This paper proposes a setup where a large general-purpose AI model reviews the path a specialized driving planner chose, looking at camera images with marked overlays and written driving rules, and either keeps it or picks a better one from the planner's other options. No retraining is needed; the cooperation happens only when the system runs.
- **Why it matters**: It suggests a way to add the broad reasoning of large AI models to driving safety without retraining the specialized systems, which is a practical question for the field. The reported gains are from the paper's own benchmarks (HUGSIM and NAVSIM), so how well they carry over to real roads is not shown in the text.
- **Background needed**: - Autonomous driving planners: software that proposes several candidate paths (trajectories) and picks one.
- Frontier models: the largest general-purpose AI models, which can read images and text.
- Zero-shot / inference-time: used on new tasks without extra training, only at the moment of running.
- Frozen model: a model whose internal weights are not changed.
- Closed-loop simulation (HUGSIM): the car's own choices affect what it sees next, unlike replaying recorded scenes.
- NAVSIM: a benchmark that scores planned paths against recorded human driving.
- HD-Score: a combined driving-quality score used in HUGSIM; the text does not define its components.
- Relative gain: improvement expressed as a percentage of the prior score. · level: research-level

<details><summary>Original abstract</summary>

Frontier models have demonstrated remarkable general-purpose reasoning capabilities, opening new possibilities for intelligent decision making in the physical world. In autonomous driving, many recent approaches seek to leverage these capabilities through additional adaptation for action output, particularly in scenarios where existing models underperform. We introduce Generalist Action Critic (GAC), a zero-shot framework that combines frontier models' general-purpose reasoning with the planning competence of specialized driving models through an inference-time harness. In GAC, specialized planners generate multiple candidate trajectories and make an initial selection, while a frozen frontier model serves as an action critic that assesses the selected trajectory against scene evidence and either retains it or reselects from the available candidates. The harness combines camera images with spatial overlays, provides driving context and reasoning principles through textual instructions, and regulates the information available at each stage to support trajectory assessment and reselection. On HUGSIM, GAC raises DrivoR's HD-Score to 43.2, achieving state-of-the-art performance among methods trained without additional simulation data. GAC also consistently improves closed-loop driving safety across three planners, with relative HD-Score gains of up to 32.1%. Experiments on NAVSIM v1 further reveal how GAC improves planning performance by correcting up to 52.13% of eligible unsafe trajectory selections while introducing new failures in only 0.67% of originally high-quality selections. These results demonstrate the potential of harnessing frontier models to improve driving safety through inference-time cooperation with specialized planners.

</details>

## Security and cryptography

### [A Unified Framework for Intelligent Cyber Attack Detection and Alert Correlation](https://arxiv.org/abs/2611.26824)
*Miguel Silva, Jo\~ao Vitorino, Daniela Pinto et al.* · `cs.CR` · arXiv:2611.26824v1 · relevance 0.08

- **In one sentence**: The paper proposes a unified framework that combines signature rules, machine learning, and sequential pattern mining to classify network traffic and correlate alerts for multi-stage attacks in a Security Operations Center, evaluated in a controlled testbed.
- **In plain words**: Security teams that watch computer networks (called Security Operations Centers) are flooded with alerts, and real attacks that unfold in several steps can be missed among them. This paper describes a single system that sorts network traffic and links related alerts together so that a multi-step attack shows up as one story. The authors tested it on a controlled, simulated network that mimicked attacks such as malware, lateral movement, reconnaissance and data theft.
- **Why it matters**: Alert overload and missed multi-stage attacks are widely recognized problems for security teams, so a tool that ties alerts into attack sequences while keeping analysts in the loop is relevant to that practical concern. The text reports that the results show effectiveness, but gives no figures, comparisons or details on how well it works outside the testbed, so its real-world value remains unclear.
- **Background needed**: - Security Operations Center (SOC): a team and facility that monitors an organization's networks for attacks.
- Alert correlation: grouping separate warning alerts that likely belong to the same attack.
- Signature rules: fixed patterns of known attack activity, like a wanted-poster description.
- Machine learning: software that learns patterns from example data to flag unusual traffic.
- Sequential pattern mining: finding recurring orders of events, such as scan then break-in then data copying.
- Lateral movement: an attacker spreading from one compromised machine to others.
- Exfiltration: stealing data out of a network.
- Human-in-the-loop: a design where people review and decide on the automated system's output.
- Testbed: a controlled lab network used for experiments instead of live systems. · level: intermediate

<details><summary>Original abstract</summary>

A Security Operations Center (SOC) plays a critical role in detecting, correlating, and responding to modern cyber threats. However, SOCs continue to face challenges related to alert overload, fragmented detection capabilities, and limited collaboration between analysts and automated systems. These issues often result in delayed incident response, analyst fatigue, and an increased risk of overlooking sophisticated, multi-stage attacks that unfold gradually across different layers of the network. To address these challenges, this paper proposes a unified framework for network traffic classification and alert correlation through the use of signature rules, machine learning, and sequential pattern mining algorithms. The solution was evaluated in a controlled testbed environment emulating realistic, multi-stage attack scenarios, including malware exploitation, lateral movement, reconnaissance, and data exfiltration. The obtained results demonstrate the effectiveness of the proposed framework in detecting and correlating complex attack behaviors, while providing analysts with actionable insights in line with a human-in-the-loop approach to SOC operations.

</details>

### [Exploring Early Vulnerability Analysis via Automatic Identification of Vulnerability-Introducing Commits](https://arxiv.org/abs/2611.26739)
*Weiliang Qi, Shu Wang, Youpeng Li et al.* · `cs.CR` · arXiv:2611.26739v1 · relevance 0.07

- **In one sentence**: The paper builds manually annotated datasets of vulnerability-introducing commits (VICs) and proposes D-SZZ, a data-state-aware framework that traces security fixes back to the commits that first introduced the flaws, then evaluates detectors on early-stage vulnerable code.
- **In plain words**: Software bugs that create security holes often sit unnoticed in code for a long time before anyone fixes them. Most existing datasets only mark the code just before a fix as "vulnerable," missing the earlier versions where the flaw first appeared. This paper builds new labeled datasets that point to the original introducing changes, and a tool, D-SZZ, that finds them automatically.
- **Why it matters**: Security tools that learn from current labeled data may be missing vulnerabilities in their early, hidden stages, which matters for catching flaws sooner. The paper also reports that its method corrected 16 inaccurate affected-version records in the NVD (the US National Vulnerability Database), which were officially confirmed, though the wider impact beyond these reported results is not established in the text.
- **Background needed**: - Vulnerability: a flaw in software that could be exploited for an attack.
- CVE: a public ID assigned to a specific known vulnerability.
- Commit: a saved set of code changes recorded in a version-control system such as Git.
- Vulnerability-fixing commit (VFC): a commit that repairs a security flaw.
- SZZ algorithm: a classic method that traces a bug fix back to the earlier commit that introduced the bug, typically using the code changes and history.
- Vulnerability detector: a tool, often machine-learning based, that flags likely vulnerable code.
- NVD: the US government's database of vulnerability records, including which software versions are affected.
- LLM: large language model, a type of AI text model used here as a baseline. · level: research-level

<details><summary>Original abstract</summary>

Developing effective vulnerability analysis techniques requires high-quality datasets that capture how vulnerabilities appear and evolve in real software codebase. Existing datasets, however, typically label as vulnerable only the code immediately preceding vulnerability-fixing commits (VFCs), overlooking the earlier versions in which vulnerabilities were first introduced and subsequently evolved. This practice limits both dataset coverage and our understanding of whether current detectors can identify vulnerabilities during their early, latent stages. In this paper, we present three manually annotated datasets of vulnerability-introducing commits (VICs) based on recent CVEs and widely used open-source projects. We further propose D-SZZ, a data state-aware VIC identification framework that analyzes security-fixing patterns and performs vulnerability scope slicing to recover the semantics implied by a fix. Experimental results demonstrate that D-SZZ outperforms existing SZZ and LLM-based baselines in identifying VICs. In addition, we evaluate six representative vulnerability detectors and find that models trained only on pre-VFC code struggle with original vulnerabilities, while incorporating early-stage samples improves detection performance. We also show that D-SZZ improves downstream vulnerable-version identification, and use it to uncover 16 inaccurate affected-version records in the NVD, all of which were officially confirmed and updated.

</details>

## Algorithms and complexity

### [Pushdown Reachability Requires $N^{3/2}$ Time on Multitape Turing Machines](https://arxiv.org/abs/2611.27814)
*A. R. Balasubramanian, Rupak Majumdar* · `cs.CC` · arXiv:2611.27814v1 · relevance 0.17

- **In one sentence**: The paper proves unconditionally that no deterministic multitape Turing machine can decide pushdown reachability (equivalently PDA language non-emptiness) in time O(N^{3/2-ε}) even on sparse instances, and extends the bound to intersecting one PDA with k-1 NFAs.
- **In plain words**: The paper studies a basic question about "stack-based" machines: given a pushdown automaton (a simple machine with a stack memory), can it ever reach an accepting state? The authors prove that a standard model of computer, a multitape Turing machine, cannot solve this faster than roughly N to the power 1.5 steps, where N is the size of the input. This is a lower bound, meaning a limit on how fast any such algorithm can be, and the text says it is the first such unconditional result of this kind for this problem.
- **Why it matters**: Pushdown reachability is a core problem in program analysis, and the text notes that many other program-analysis problems are equivalent to it up to quasi-linear time, so the lower bound carries over to them. The text does not discuss practical consequences, and the bound applies to multitape Turing machines specifically, so its relevance to real hardware or other models is not addressed here.
- **Background needed**: - Pushdown automaton (PDA): a finite-state machine with a stack, a last-in-first-out memory.
- Pushdown reachability: deciding whether a PDA can reach an accepting configuration (equivalently, whether its language is non-empty).
- NFA: nondeterministic finite automaton, a simpler machine with no stack.
- Multitape Turing machine: an idealized computer with several tapes read and written in parallel; a standard model for measuring time.
- Lower bound: a proof that no algorithm in a given model can be faster than some amount of time.
- Super-linear: growing faster than the input size N, so a bound like N^{3/2} is super-linear.
- Quasi-linear time: essentially linear time, up to logarithmic factors.
- Sparse instance: one where the number of transitions is proportional to the number of states. · level: research-level

<details><summary>Original abstract</summary>

Pushdown reachability, or equivalently, language non-emptiness of pushdown automata (PDA), is a fundamental problem in automata theory and program analysis. We show that, for every $\epsilon >0$, no deterministic multitape Turing machine can decide pushdown reachability in $O(N^{\frac{3}{2}-\epsilon})$ time, where $N$ is the input size. The lower bound already holds for \emph{sparse instances}, i.e., instances in which the number of transitions is linear in the number of states. This gives the first unconditional super-linear lower bound for pushdown reachability. Furthermore, we also extend this result and show that for any $\epsilon > 0$ and $k \ge 1$, no deterministic multitape Turing machine can decide the intersection non-emptiness problem of one PDA and $k-1$ NFAs in time $O(N^{\frac{3k}{2}-\epsilon})$, where $N$ is the input size. Finally, pushdown reachability is well-known to be quasi-linear time equivalent to many different problems in program analysis. Our result translates to all of those problems as well and provides the first unconditional super-linear lower bounds for those problems on multitape Turing machines.

</details>

### [The Power of Sampling for Finding Far-Apart Bases in Matroids](https://arxiv.org/abs/2611.27934)
*Mayank Goswami, Vasilis Livanos, Pasin Manurangsi et al.* · `cs.DS` · arXiv:2611.27934v1 · relevance 0.14

- **In one sentence**: The paper studies how far apart bases of a matroid can be in its basis-exchange graph, showing that two random bases are a constant-factor proxy for the diameter, and gives approximation algorithms and hardness results for maximally diverse k-tuples of bases, including a Farthest Matroid Basis primitive.
- **In plain words**: A matroid is an abstract structure generalizing independent sets such as sets of columns in a matrix or edge sets forming forests in a graph; its bases are the maximal such sets. The paper asks how to find bases that are as different from each other as possible, measuring difference by how many single swaps separate them. It reports that picking two random bases already gets, on average, at least about 1/16 of the largest possible separation, and that picking k of them gives a tight log k-factor approximation.
- **Why it matters**: The work gives the first constant-factor polynomial-time algorithm for max-min diversity on arbitrary matroids, which the text describes as a new result for this problem, with the k=2 case already solvable by matroid intersection. The authors also note a graph with strong expansion where random sampling fails, so intuition from expansion alone does not suffice; the broader connections beyond this are not discussed in the text.
- **Background needed**: - Matroid: an abstract system of "independent" sets (generalizing forests in a graph or independent columns of a matrix); a basis is a maximal independent set.
- Basis-exchange graph: vertices are bases; two are joined if one can be obtained from the other by swapping one element.
- Diameter: the longest shortest-path distance between any two vertices in a graph.
- Approximation algorithm: a fast method guaranteed to find a solution within a fixed factor of the best possible.
- Max-min diversity: choose k objects so that the smallest pairwise distance among them is as large as possible.
- LP rounding: solve a relaxed linear program and convert the fractional answer into a valid integer solution.
- W[1]-hardness: a parameterized-complexity signal that the problem is unlikely to admit a fast algorithm when the parameter is fixed-size. · level: research-level

<details><summary>Original abstract</summary>

We study the geometry of matroids via the \emph{diameter} and \emph{dispersion} of the metric space of their bases. Given a matroid $M$, we ask if the diameter of its basis-exchange graph $\mathcal{G}(M)$ can be approximated by sampling two uniformly random bases. As our main result, we show that their expected distance is always at least $1/16$ of the diameter of $\mathcal{G}(M)$. While this might appear to follow from the edge-expansion properties established by Anari, Liu, Gharan and Vinzant (STOC'19), we show that this inutition is false by constructing a graph $G$ with edge-expansion at least $1$ for which sampling two random vertices does \emph{not} give a constant-factor approximation to its diameter. We turn to finding $k\geq 2$ maximally-diverse bases of a matroid, the $k$ (max--min) diversity problem. When $k=2$, the problem is solvable via matroid intersection. However, for $k\geq 3$ no polynomial-time approximation or hardness is known, even for diverse spanning trees. We show that sampling $k\geq 3$ bases provides a tight $\Theta(\log k)$ approximation. We then combine structural insights about the local density of $\mathcal{G}(M)$ with classical LP-rounding techniques to obtain a polynomial-time $1/6$-approximation algorithm for the $k$-diversity problem in arbitrary matroids, the first constant-factor polynomial-time approximation for max--min diversity on any matroid. A key ingredient for our result is the \emph{Farthest Matroid Basis} problem: given a collection of bases, find a new basis as far as possible from all of them. We give a polynomial-time $1/3$-approximation algorithm for this, which is our main algorithmic primitive for $k$ max--min diversity. We also show it is $W[1]$-hard when parameterized by the optimal distance. We also improve the $1/6$-approximation for $k$-diversity, for partition matroids and graphic matroids of constant arboricity.

</details>

## Programming languages and formal methods

### [Schema-Validated LLM Workflows: A Benchmark Protocol and Comparative Evaluation Across Six Python Implementations](https://arxiv.org/abs/2611.27106)
*Sidney Shapiro, Sanad Al-Khatib, Aurora Pinz\'on Arzola et al.* · `cs.SE` · arXiv:2611.27106v1 · relevance 0.05

- **In one sentence**: A benchmark protocol and live API evaluation that separates whether LLM outputs are structurally valid (parse against a schema) from whether they are task-correct, across five business workflow tasks and six Python implementations (PydanticAI, LangGraph, DSPy, CrewAI, Agno, and a framework-free SDK reference).
- **In plain words**: Companies increasingly use language models to pull data out of documents, write database queries, and route work, and the output has to fit a required format for software to use it. This paper argues that output which fits the format can still be wrong, and it measures both properties separately across six ways of wiring up the same model. In the reported confirmatory run, about 68% of outputs were schema-valid and the average automated quality score was about 0.64, with three setups keeping near-perfect format compliance and scoring roughly 0.91 to 0.94 on quality.
- **Why it matters**: It suggests that checking only whether an LLM's output parses is not enough to know if it does the job, which matters for anyone wiring models into business systems. The results are specific to one package and model configuration, and the authors say the contrasts describe system setups rather than causal effects of particular library features.
- **Background needed**: - Large language model (LLM): an AI system that generates text from a prompt.
- Structured output / schema: a required format (fields and types) that software can read automatically, like a fixed form.
- Schema validity vs. task correctness: a output can fill the form correctly and still contain wrong content.
- Python framework / library: prewritten code that helps build LLM applications; the paper compares several.
- Benchmark protocol: a fixed, repeatable test design with pre-set analysis rules.
- Holm-adjusted contrasts: statistical corrections for making many pairwise comparisons without inflating false positives.
- Ablation: a test that removes or changes one component to see its effect.
- Condition-by-task interaction: when the ranking of setups changes depending on the task. · level: intermediate

<details><summary>Original abstract</summary>

Large language models are increasingly used to extract records, generate SQL, summarize reports, answer policy questions, and route operational work. At these software boundaries, parseable output is necessary but does not establish task correctness. We present a reproducible benchmark protocol, a public executable artifact, and a confirmatory live API evaluation that separate structural validity from task-specific correctness across five business workflow tasks and six Python implementation conditions: PydanticAI, LangGraph, DSPy, CrewAI, Agno, and a framework-free SDK reference. We hypothesize that (H1) schema validity and task quality are separable, (H2) structured-output binding paths are heterogeneous under a shared model and lowest-common-denominator contract, and (H3) condition-by-task interactions concentrate failures rather than shifting all tasks equally. Confirmatory analysis uses distinct task instances (100 extraction and 50 per other task, with three nested replicates) under a frozen analysis plan, yielding a 5400-row primary matrix with equivalence margins and Holm-adjusted contrasts against the SDK reference. In the eligible confirmatory run, overall schema validity was 0.684 and mean automated quality was 0.638. PydanticAI, LangGraph, and DSPy retained near-ceiling schema validity with mean quality 0.91-0.94, while the plain SDK, Agno, and CrewAI conditions were substantially lower in this package and model configuration. Schema-valid rows still produced many task-score flags, especially in extraction and compliance QA, and quality residuals show strong condition-by-task interactions (including a workflow collapse for CrewAI). Labelled ablations address retry budgets and feature-using mechanisms; primary contrasts remain system-configuration findings, not causal attributions to marketed library features.

</details>

### [How developers split roles among them and a coding agent and what "collaboration" means](https://arxiv.org/abs/2611.26668)
*Linus Ververs, Helya Dadkhah, Lutz Prechelt* · `cs.SE` · arXiv:2611.26668v1 · relevance 0.04

- **In one sentence**: A mixed-methods study of how developers divide work between themselves and AI coding agents (such as Claude Code), comparing 2025 early-adopter blog posts with a 2026 practitioner survey, and characterizing what developers mean by "collaboration" with the agent.
- **In plain words**: Software developers are increasingly handing coding tasks to AI agents that can write and change code on their own. This paper asks how developers describe the split of work between themselves and such an agent, and what kind of collaboration they would ideally want. The authors read early adopters' 2025 blog posts, surveyed practitioners in 2026, and used an AI agent to help sort the survey's free-text answers.
- **Why it matters**: Teams are deciding in real time who does what when an AI agent writes code, so a clear picture of how developers think about this split is useful for planning and management. The paper suggests that differing views on collaboration may create friction within teams, though the text does not measure this directly.
- **Background needed**: - A "coding agent" is an AI tool that can carry out multi-step programming tasks, not just suggest single lines of code.
- "Open coding" is a qualitative research method where a researcher labels passages of text with descriptive categories, which are then grouped into themes.
- A "mixed-methods" study combines qualitative (interpretive, text-based) and quantitative (counted, survey-based) approaches.
- The paper reports that in 2025 agents were used only in supporting roles and humans were firmly accountable; in 2026 this is still largely true, but agents are taking on more involvement.
- Collaboration, in the authors' findings, has three facets: clear human-only, agent-only, and shared work steps; personal preferences not justified by engineering needs; and a view that covers the whole development process. · level: intermediate

<details><summary>Original abstract</summary>

Background: Coding agents such as Claude Code become more and more competent, so that their role in the development process can grow. Objective: How do developers characterize the role-split between them and their agent? How would they ideally want to collaborate with their agent? Methods: We perform a 3-step, mixed-methods study. We apply qualitative open coding to 2025 early adopters' blog articles; perform a quantitative survey of 2026 practitioners; develop and apply a method for coding-agent-supported open coding of survey freetext responses. Results: The 2025 practitioners have the agent work in supporting roles only. Accountability was firmly human. In 2026, both are fundamentally still true. Gradually, however, the role-split is now different, with much more agent involvement. The developers' notion of collaboration has three facets: Predominantly a separation into human-only, agent-only, and collaborative work steps, with defined conditions and goals. Second, accommodating personal preferences without engineering justification. Third, a holistic view of collaboration covering the entire development process. Conclusions: Defining one's role relative to the agent will need to be a recurring activity. The different views on collaboration are likely a source of friction and conflict for teams; future work should find out how to cope with that.

</details>

## Systems and networking

### [Exploring the Potential of Ultra-Low-Bit Inference on LLM Accelerators](https://arxiv.org/abs/2611.27561)
*Hao Wang, Yang Shi, Jiageng Shi et al.* · `cs.AR` · arXiv:2611.27561v1 · relevance 0.09

- **In one sentence**: The paper proposes VQACC, a modest change to a systolic-array LLM accelerator's operand buffer access logic and data mapping so that vector-quantized weight codebook lookups reuse existing storage and ports, reporting a 2.63x speedup over the EVA baseline at 0.17% extra compute-array area.
- **In plain words**: Large language models are very big, and one way to shrink them is to store their numbers as short codes that point into a small lookup table, called a codebook. Turning those codes back into usable numbers requires many lookups, which clash with how existing AI chips move data, so past fixes added special-purpose hardware. This paper argues that today's chips already have the spare memory and access ports needed, and that the way they are wired just needs rethinking; the authors report that their version runs about 2.63 times faster than a prior baseline (EVA) while adding very little chip area.
- **Why it matters**: Running large models on cheaper, lower-power hardware is a practical concern for deploying AI, and this shows a way to get the benefit of extreme compression without building a separate accelerator. The claims come only from the abstract; the workloads, measurement setup, and comparison details are not given here, so the size of the gain should be read with that in mind.
- **Background needed**: - Quantization: storing model numbers with fewer bits to save memory and time.
- Vector quantization (VQ): grouping several values and replacing them with one index into a shared codebook.
- Codebook lookup: fetching the stored values that an index points to, then using them in computation.
- Systolic array: a grid of simple processing units that passes data across neighbors, common in AI accelerators.
- Operand buffer: on-chip memory that holds the inputs fed to the compute array; its ports limit how fast data can be read.
- Dataflow: the order and route by which data moves through hardware.
- Dequantization: converting compressed codes back into full values before computing with them.
- EVA: the prior accelerator design used as the comparison point in the paper. · level: research-level

<details><summary>Original abstract</summary>

Vector quantization (VQ) enables ultra-low-bit compression of large language models (LLMs) by encoding groups of values as compact codebook indexes. However, reconstructing these values for computation requires frequent codebook lookups, which conflict with the dataflows of conventional LLM accelerators and limit the performance gains from VQ compression. Consequently, prior work has resorted to VQ-specific accelerator designs, which either incur substantial additional hardware overhead or support only a limited range of inference scenarios. In this work, we argue that existing systolic-array-based LLM accelerators already possess the essential hardware resources for efficient VQ inference, but lack the mechanisms to effectively exploit them. To bridge this gap, we present VQACC, an architectural enhancement that jointly redesigns the existing operand buffer's access logic and data mapping to reuse its storage and port resources for codebook lookups, seamlessly integrating dequantization into the normal operand-addressing dataflow. Evaluation shows that VQACC achieves a 2.63$\times$ speedup over the EVA baseline, with additional hardware occupying only 0.17\% of the compute array's area.

</details>

### [Acceleration of Sparse and Irregular Workloads through Energy-Efficient Stream Extensions](https://arxiv.org/abs/2611.26939)
*Paul Scheffler* · `cs.AR` · arXiv:2611.26939v1 · relevance 0.05

- **In one sentence**: A thesis proposing a core-coupled hardware stream extension for RISC-V processors that accelerates sparse and irregular workloads (affine and indirect streams, sparse tensor intersection and union), evaluated in a 432-core 2.5D system in 12nm FinFET and extended to chip-level interconnects.
- **In plain words**: Modern chips are built to run orderly, predictable computations well, but many real tasks involve scattered, unpredictable data access, so the chip's calculating units sit idle most of the time (the text cites under 10% utilization). This thesis designs add-on hardware that fetches and feeds such scattered data streams to the processor so it stays busy, and reports tests on a large chip built from many small processors.
- **Why it matters**: Sparse and irregular workloads underlie sparse neural networks, physics simulations, and graph analytics, so efficiency gains here could matter for those fields. The text reports benchmark results on its own prototype, but it does not show how these gains would carry over to commercial systems, so that remains open.
- **Background needed**: - Hardware "stream" units: separate helpers that fetch data from memory in a planned sequence while the main processor computes.
- Sparse data: arrays where most entries are zero, so only a few values need storing and processing.
- Functional unit utilization: the share of time a chip's arithmetic units are actually doing useful work.
- RISC-V: an open processor instruction set design.
- Stencil computation: updating each point in a grid using its neighbours, common in physics simulations.
- Dennard scaling and Moore's law: historical trends of faster, cheaper transistors that have slowed down.
- 2.5D integration: placing several chips side by side on a shared connecting base rather than stacking them. · level: research-level

<details><summary>Original abstract</summary>

The slowdown of Moore's law and Dennard scaling has motivated computer architects to uphold performance scaling through architectural specialization. So far, most efforts have focused on highly regular workloads, which exhibit good data locality, ample reuse, and a data-independent execution flow. As this specialization hits diminishing returns, attention shifts towards sparse and irregular workloads, which are essential to applications like sparse neural networks, multiphysics simulations, and graph analytics. However, they lack the convenient properties of highly regular compute that modern architectures are optimized for, resulting in very low (<10%) functional unit utilization on traditional CPUs and GPUs. The most promising approaches to their general hardware acceleration leverage memory streams, which decouple data movement from execution. In this thesis, we explore energy-efficient hardware stream extensions that significantly accelerate sparse and irregular workloads in general-purpose systems without specializing to specific application domains or compromising on regular-workload performance. We design a flexible, core-coupled stream extension supporting affine and indirect streams as well as intersection and union of sparse tensors. We integrate it into an energy-efficient RISC-V compute cluster, achieving significant performance and energy efficiency benefits on general sparse linear algebra, and further use it to accelerate stencil computations, spiking neural network inference, and model-predictive control. We evaluate it at scale in a 432-core 2.5D RISC-V system fabricated in 12nm FinFET, achieving leading compute utilization and energy efficiency on sparse and irregular workloads while remaining competitive on regular workloads. Finally, we extend chip-level interconnects with end-to-end irregular streams, improving performance, energy efficiency, and bus utilization.

</details>

## Human-computer interaction

### [Standard-Anchored Delegation in Teachers' Use of Generative AI](https://arxiv.org/abs/2611.27533)
*Muhammad Saleh Farooq, Muhammad Ahmad Khan, Muhammad Jon Raza* · `cs.HC` · arXiv:2611.27533v1 · relevance 0.05

- **In one sentence**: A qualitative mixed-methods study of 13 teachers (plus administrators and a student) in Punjab, Pakistan, proposes "standard-anchored delegation," where teachers hand AI tasks when an outside standard such as a rubric or textbook defines a correct output they can check.
- **In plain words**: Teachers using generative AI have to decide which parts of their work to hand to the tool, even though they stay responsible for what students receive. The authors interviewed teachers in Pakistan and coded each teacher's stance on twelve teaching tasks. Teachers were comfortable using AI for lesson-planning help, but none accepted AI-written learning objectives, and most did not use it to encourage or emotionally support students.
- **Why it matters**: The paper gives a concrete account of when people are willing to delegate work to AI, and it names a check on output (an outside standard) as the key condition. Its suggestions, such as asking for the standard before generating and showing it beside the output, are design ideas the authors propose rather than tested results. The study covers one region and a small sample, so its wider reach is uncertain.
- **Background needed**: - Generative AI: software that produces text, such as lesson plans or feedback, from a prompt.
- Delegation: handing part of a task to someone or something else while keeping responsibility for the outcome.
- Rubric or answer key: an outside standard that says what a correct or good answer looks like, which makes it possible to check AI output.
- Qualitative, mixed-methods study: research based mainly on interviews and coding of what people say, sometimes with some counting added.
- Verifiability: how easily a person can confirm that an output is correct.
- Government vs. private schools: the paper reports that private schools gave teachers more support for checking AI output. · level: intermediate

<details><summary>Original abstract</summary>

Teachers who use generative AI must decide which parts of their work to hand over, while they remain accountable for what reaches students. We studied these decisions in Punjab, Pakistan, through a qualitatively driven mixed-methods study. We interviewed 13 teachers from government, private, NGO and vocational institutions, four administrators and one student, and coded each teacher's position on twelve educational tasks. Nine teachers accepted AI drafts or substantial assistance with lesson planning, but none accepted AI-drafted learning objectives, and eleven did not use AI to encourage or emotionally support students. Teachers who would accept AI marking required that the model be given a rubric or marking criteria. Building on assessment research and HCI work on verifiability, we call this pattern standard-anchored delegation: teachers handed a component of a task to AI when a standard outside the model, such as a textbook or rubric, defined a correct output and the teacher could apply that standard to the result. Having a standard was not always enough. Several government-school teachers did not use AI to mark quizzes even though the quizzes had answer keys, because they expected students to look for evidence of the teacher's effort. Checking AI output required subject knowledge and time, and private schools gave teachers more support for this than government schools did. Participants also read disclosure of AI use as a statement about whether the teacher had reviewed the work. We propose that teacher-facing AI tools ask for the relevant standard before generating and show each output beside it, and that schools account for the time that checking takes.

</details>

### [On the Challenges of Using LLMs in High-Risk AI Recruitment: Guiding Questions for Legal Conformity with the AI Act](https://arxiv.org/abs/2611.27462)
*Clara Punzi, Stefano Tramacere, Andrea Fedele et al.* · `cs.CY` · arXiv:2611.27462v1 · relevance 0.05

- **In one sentence**: The paper proposes a legal-by-design toolkit that translates the AI Act's conformity-assessment duties (Articles 9–15 and Annex IV) into technical requirements and guiding questions for AI recruitment tools built on third-party general-purpose AI models, and analyzes the information gaps along the supply chain.
- **In plain words**: The EU's AI Act sets detailed rules for "high-risk" AI, such as software that screens job applicants, but gives companies little practical guidance on how to meet them. This paper offers a toolkit of guiding questions that turns the legal duties into concrete technical requirements, and illustrates it with a simplified example. It also finds that when a recruitment tool is built on a general-purpose AI model made by another company, the builder often cannot get the technical details needed to prove compliance, which can weaken the employer's ability to oversee the tool.
- **Why it matters**: Hiring algorithms affect people's job prospects, and the AI Act's compliance rules are new, so practical translations of legal text matter for developers and regulators. The text does not report any tested results from using the toolkit, so its practical value is not yet shown.
- **Background needed**: - EU AI Act: a European law that regulates AI systems by risk level; "high-risk" systems face the strictest duties.
- Conformity assessment: the process of showing a system meets legal requirements before and during sale or use.
- Articles 9–15 and Annex IV: the parts of the Act listing duties such as risk management, data quality, record-keeping, transparency, human oversight, and technical documentation.
- General-purpose AI (GPAI) model: a broad AI model (like a large language model) that many products are built on top of.
- Upstream vs. downstream providers: the company that makes the base model versus the company that builds a specific product on it.
- Deployer: the organization that uses the AI system in practice, here an employer or recruiter.
- "Legal-by-design": building compliance into the system from the start rather than adding it afterwards. · level: intermediate

<details><summary>Original abstract</summary>

The EU Artificial Intelligence Act (AI Act) imposes detailed obligations on providers of high-risk AI systems but offers limited operational guidance, particularly when these systems integrate third-party General-Purpose AI (GPAI) models. This paper introduces a toolkit that fosters the development of legal-by-design AI-assisted recruitment systems by translating the core legal obligations of the AI Act's conformity assessment---specifically Articles 9--15 and Annex IV---into techno-normative requirements and corresponding guiding questions. While recruitment pipelines may involve components with varying technical complexity and differing levels of algorithmic transparency, this paper focuses on the most challenging case: the integration of third-party GPAI models into critical stages of the selection process, including resume and job description parsing, applicant scoring, and shortlist generation. This scenario presents significant challenges for downstream providers of high-risk AI systems, as it underscores the difficulties in obtaining the technical information needed to demonstrate compliance with the AI Act's techno-normative requirements, both prior to and during market deployment. After introducing the toolkit and illustrating its application through a simplified example, the paper explores informational dependencies between upstream and downstream GPAI model providers. These dependencies may produce informational gaps across the AI supply chain, potentially hindering the collection of evidence necessary for the AI system provider to ensure legal compliance. The resulting lack of technical transparency negatively affects the deployer, who may struggle to maintain meaningful oversight of the system, and ultimately impacts the persons subject to the AI output.

</details>

## Information theory

### [User-Irrepressible Sequences for Multiple-Packet Reception](https://arxiv.org/abs/2611.27248)
*Yen-Ling Shih, Yuan-Hsun Lo, Yijin Zhang et al.* · `cs.IT` · arXiv:2611.27248v1 · relevance 0.04

- **In one sentence**: The paper gives an explicit Chinese Remainder Theorem-based construction of periodic binary protocol sequences that guarantee every user at least one successful transmission per period under multiple-packet reception with capability γ ≥ 2, without feedback or phase synchronization.
- **In plain words**: Many users share one radio channel that can sometimes receive several packets at once, and each user follows a fixed repeating on-off pattern of transmissions. The paper studies how to design these patterns so that, no matter how the users' patterns are offset in time, every user gets at least one packet through in each cycle. The authors give a general explicit recipe for this, and they also work out the exact average waiting time (delay) for a user across all possible time offsets.
- **Why it matters**: Guaranteeing that every user gets through within a bounded time, without coordination or feedback, matters for random-access wireless networks. The text does not show practical deployment results, so its real-world impact is unclear from this summary alone.
- **Background needed**: - Multiple-packet reception (MPR): a receiver that can decode up to γ simultaneous packets; a slot with at most γ transmitters succeeds.
- Protocol sequence: a fixed repeating binary pattern (1 = transmit, 0 = stay silent) assigned to each user.
- Cyclic shift: the same pattern started at a different point in the cycle; users are not synchronized, so shifts are arbitrary.
- Hamming cross-correlation: a count of how often two patterns line up on a transmit slot under a given shift; used to bound collisions.
- Chinese Remainder Theorem: a number-theory result used here to build sequences of a chosen length from smaller moduli.
- Conflict-avoiding codes: a known family of sequence sets with low mutual interference, used as an alternative starting point.
- Average individual delay: the expected wait until a user's first success, averaged over shifts. · level: research-level

<details><summary>Original abstract</summary>

This paper studies deterministic transmission schemes based on protocol sequences for slot-synchronous multiple-packet reception (MPR) channels without feedback or synchronization of sequence phases. Each user schedules its transmissions according to a preassigned periodic binary sequence. A sequence set has the user-irrepressible property with MPR capability $\gamma$ ($\gamma$-UI) if every user is guaranteed at least one successful transmission per period, regardless of the relative cyclic shifts. We propose a unified explicit construction based on the Chinese Remainder Theorem (CRT) for arbitrary MPR capability $\gamma\geq 2$. To the best of our knowledge, this is the first unified CRT-based construction framework for $\gamma$-UI sequences over this full range, without requiring conflict-avoiding codes with prescribed parameters. We establish the $\gamma$-UI property through bounds on pairwise Hamming cross-correlations and show that suitably selected subsets support one additional active user without increasing the sequence length. We also derive exact average individual delay expressions over all possible cyclic shifts and extend the delay analysis to $\gamma$-UI sequence sets obtained from conflict-avoiding codes.

</details>

### [Semi-regular admixed arrays: asymptotic enumeration and when information is additive](https://arxiv.org/abs/2611.26990)
*Alan J. Aw* · `q-bio.PE` · arXiv:2611.26990v1 · relevance 0.04

- **In one sentence**: Asymptotic counts of doubly constrained two-way diploid admixed arrays (local ancestry tallies plus ancestry-specific allele sums) in the semi-regular regime, with a test of whether the two constraint families combine additively in information.
- **In plain words**: This paper studies grids of numbers that record, for a group of mixed-ancestry people, which ancestral origin and which allele each stretch of their genetic material carries. The authors count how many such grids satisfy two kinds of summary totals at once, and find that the count is governed by an entropy formula, with a different correction near the edges of the allowed range. They then ask whether the two summaries together narrow things down as much as you would guess by combining their individual effects, and report that, in general, they do not.
- **Why it matters**: Genomic studies of admixed populations often release only summary statistics, so knowing how much those summaries reveal about individuals matters for both analysis and privacy. The text does not say how these results would be used in practice, so the practical reach is unclear from the abstract alone.
- **Background needed**: - Admixed population: people whose ancestry comes from more than one source population.
- Local ancestry: which source population each segment of a person's chromosomes came from.
- Diploid: each person carries two copies of each chromosome, so two haplotypes.
- Contingency-table style counting: counting arrays that match fixed row and column totals.
- Shannon entropy: a measure of how spread out or uncertain a set of frequencies is; exponential growth of counts is often governed by it.
- Asymptotic formula: an approximation that becomes accurate as the array size grows.
- Martingale techniques: probability tools for controlled random processes, used here as the main proof method.
- Additivity heuristic: the guess that two pieces of information combine independently, so their effects simply add. · level: research-level

<details><summary>Original abstract</summary>

In genomic data analysis, admixed arrays are pairs of matrices recording the local ancestry and the allele at each position of the haplotypes of admixed individuals. We study two-way diploid admixed arrays with $N$ individuals and $P$ loci under two families of constraints: local ancestry tallies, which fix the number of ancestry assignments per individual, and ancestry-specific sums, which fix the allele count per locus and ancestry. These two constraint families correspond to summaries of admixed genetic data investigated in biomedical and genomic applications. In the semi-regular regime, where all tallies and sums are uniform, we use complex martingale techniques to derive asymptotic formulas for the number of doubly constrained arrays as $N$ and $P$ grow with bounded ratio, over the whole feasible region. The leading term is governed by the Shannon entropy of the frequencies of the four possible pairs of entries at a position of the two matrices; on the boundary one or two of them vanish, changing the Gaussian correction. We then ask whether the two families carry information additively, that is, whether an independence heuristic predicts the doubly constrained count up to a bounded factor. Measured against the smallest set of arrays defined by a constraint that each family implies on its own, additivity holds only on a set of measure zero. It includes an edge of the feasible region with correction factor $e^{-1/4}$, extending our earlier result at the symmetric point. Thus, how far the two summaries jointly narrow down individual-level ancestry and genotype configurations cannot generally be predicted from how far each does on its own.

</details>

## High-energy theory and gravity

### [Disk 2-point functions for conformal loop ensemble: a derivation from the SLE loop CFT](https://arxiv.org/abs/2611.27767)
*Shengzhi Jin, Xin Sun, Baojun Wu* · `cond-mat.stat-mech` · arXiv:2611.27767v1 · relevance 0.15

- **In one sentence**: The paper derives bulk two-point functions for two-dimensional critical loop models in a disk from conformal loop ensembles, using the SLE loop conformal field theory, and expresses them as absolutely convergent contour integrals whose residues reproduce discrete spectra predicted by analytic bootstrap for irrational central charges.
- **In plain words**: The paper studies random systems of closed loops drawn on a flat two-dimensional surface at a critical point, where the loops look the same at every scale. It shows how to compute how two marked points on such a disk are statistically related, by writing the answer as a contour integral built from known ingredients. For irrational values of the central charge, evaluating these integrals by residues recovers the list of allowed discrete states and matches earlier predictions made by a different method.
- **Why it matters**: Correlation functions of this kind are the basic data of two-dimensional critical phenomena, and a single formula covering both rational and irrational central charges is a technical advance in the field. The text does not indicate applications beyond this mathematical-physics setting, so wider significance is uncertain.
- **Background needed**: - Critical loop models: random collections of non-crossing closed loops in a plane, modeling boundaries of percolation clusters or spin domains at a phase transition.
- Conformal loop ensemble (CLE): the continuum limit of such loop models, described by random fractal curves.
- SLE (Schramm–Loewner evolution): a family of random fractal curves used to describe interfaces in critical systems.
- Conformal field theory (CFT): a framework for scale-invariant two-dimensional physics; its central charge is a number labeling the theory.
- Two-point function: a measure of how quantities at two locations are correlated.
- Virasoro conformal blocks: building-block functions that organize correlation functions in CFT.
- Structure constants and bootstrap: coefficients fixing how operators combine, and consistency methods that constrain them.
- Residues: a complex-analysis technique that evaluates contour integrals by summing contributions from poles. · level: research-level

<details><summary>Original abstract</summary>

We give a derivation of the bulk two-point functions of two-dimensional critical loop models in the disk based on conformal loop ensembles (CLE) and the conformal field theory of SLE loop measures developed by Baverez--Jego. Combining local Ward identities with the spectral resolution of the SLE-loop CFT, we express the two-point functions as contour integrals involving known CLE three-point structure constants and Virasoro conformal blocks. With a suitable choice of contour, these integrals are absolutely convergent and provide a unified representation of a broad class of correlation functions, valid for both irrational and rational central charges. For irrational central charges, evaluating these integrals by residues determines the discrete closed-channel spectrum and yields expansions that agree with the analytic bootstrap predictions of Downing--Jacobsen--Nivesvivat--Ribault--Saleur.

</details>

### [Perturbative $S$-matrix Unitarity in Higher-Derivative Theory of Fermions](https://arxiv.org/abs/2611.27021)
*Yugo Abe, Takeo Inami, Keisuke Izumi et al.* · `hep-th` · arXiv:2611.27021v1 · relevance 0.14

- **In one sentence**: The paper builds a higher-derivative four-fermion theory, argues that its fermionic ghost states always carry negative norm, and shows that, unlike conventional four-Fermi theory, it satisfies perturbative S-matrix unitarity at tree level.
- **In plain words**: Physicists use a rule of thumb that a theory is well-behaved (renormalizable) if its predicted scattering probabilities do not blow up at very high energies. This paper studies a modified theory of fermions, the particles that make up matter, whose equations contain extra derivative terms. The authors report that this modified theory keeps its high-energy predictions well-behaved, unlike the standard four-fermion theory, but it needs extra "ghost" particles that have negative norm, a kind of unphysical bookkeeping quantity.
- **Why it matters**: The question of whether a theory can be consistent at high energies without a standard renormalizable form matters for how far quantum field theory can be extended. The text presents the results as supporting evidence for renormalizability and as an extension of the authors' earlier scalar-theory work, but the text alone does not establish whether the conclusion holds beyond this setup.
- **Background needed**: - Quantum field theory describes particles as excitations of fields; scattering amplitudes predict how particles collide.
- The S-matrix collects all scattering amplitudes; unitarity means probabilities add up to one.
- Renormalizability means infinities arising from quantum corrections can be absorbed into a finite number of parameters.
- Four-Fermi interaction: a contact interaction where four fermions meet at a single point; the standard version is non-renormalizable.
- Higher-derivative theory: the kinetic (motion) term contains more derivatives than usual, changing the scaling of the field and allowing better high-energy behavior.
- Ghost states: extra particle states with wrong-sign or negative norm, normally a sign of inconsistency unless handled carefully.
- Tree-level: the leading-order approximation with no quantum loops. · level: research-level

<details><summary>Original abstract</summary>

We construct a higher-derivative fermion theory with four-Fermi interactions. In quantum field theory, it is conjectured that good high-energy behavior of tree-level scattering amplitudes implies renormalizability, a notion referred to as the tree-unitarity criterion. To investigate whether this criterion is satisfied in a higher-derivative fermion theory, we examine the structure of the $S$-matrix in detail. Owing to the higher-derivative kinetic term, the mass dimension of the spinor field differs from that of a conventional fermion, rendering four-Fermi interactions renormalizable at the cost of introducing ghost states. We show that, unlike bosonic ghosts, fermionic ghosts inevitably give rise to negative-norm states regardless of the sign of their energy eigenvalues. We further demonstrate that, in contrast to conventional four-Fermi theories, the higher-derivative four-Fermi theory satisfies perturbative $S$-matrix unitarity. In light of the tree-unitarity criterion, these results provide supporting evidence for the renormalizability of higher-derivative fermion theories and generalize our previous findings on higher-derivative scalar theories to the fermionic case.

</details>

## Statistical physics

### [Cyclic perturbations encode memories in trained neural networks without loss of performance](https://arxiv.org/abs/2611.27647)
*Max Kerr Winter, Liesbeth M. C. Janssen* · `cond-mat.dis-nn` · arXiv:2611.27647v1 · relevance 0.15

- **In one sentence**: Cyclically displacing all weights of a trained overparameterized deep network and relaxing by gradient descent writes retrievable memories into the weight structure, with deterministic and noisy write protocols, without measurably hurting performance on unseen data.
- **In plain words**: Some physical materials, such as certain disordered solids and suspensions, remember how they were repeatedly nudged back and forth. This paper asks whether a trained artificial neural network can do the same. The authors repeatedly shake all of the network's weights (its adjustable numbers), let it settle back through training, and find that the size of the shake can be read back out later.
- **Why it matters**: It suggests that neural networks may have a hidden storage capacity that can be used without damaging what they were trained to do, which the text reports as holding on unseen data. The link to memory effects in sheared suspensions is a conceptual bridge between machine learning and statistical physics; the text does not show practical applications.
- **Background needed**: - Weights: the adjustable numbers in a neural network that set its behaviour.
- Gradient descent: a standard training method that nudges weights step by step to reduce error.
- Overparameterized: a network with more weights than strictly needed, which gives many settings that work equally well.
- Cyclic perturbation memory: in some disordered materials, repeated back-and-forth driving leaves a lasting imprint, such as a point where motion turns from reversible to irreversible.
- Reversible vs irreversible motion: reversible means the system returns to its starting state when the drive is removed; irreversible means it has permanently rearranged.
- Noisy write: adding randomness to each perturbation cycle, which the authors borrowed from sheared suspensions to keep multiple memories alive. · level: research-level

<details><summary>Original abstract</summary>

Many disordered materials exhibit a remarkable form of memory: they retain information about the history of cyclic perturbations. Whether this phenomenon also occurs in artificial neural networks, whose mathematical structure and dynamics share many similarities with disordered physical systems, is unknown. Here we show that cyclically perturbing a trained, overparameterized deep neural network encodes information in the structure of the weights that can subsequently be retrieved, thus retaining memory of the perturbation history. During each write cycle, all weights are displaced, after which the network relaxes through gradient descent. Repeated cycles organise the neural network into a state that is reversible for perturbations up to the write amplitude, allowing the encoded value to be read from the onset of irreversible weight motion. Multiple memories can also be encoded, although under deterministic writing only the largest persists at long times. Inspired by cyclically sheared suspensions, we introduce a novel noisy-write protocol that preserves all encoded memories at long times. Remarkably, neither deterministic nor noisy memory writing measurably affects the network's performance on unseen data from its original learning task. Our results establish cyclic memory as a phenomenon shared by disordered physical systems and deep neural networks, and show that networks can exploit as yet unexplored memory capabilities without compromising their original function.

</details>

### [From non-universal spectra at the RS-RSB transition to the universal $\omega^4$ regime inside the glassy phase](https://arxiv.org/abs/2611.27564)
*Tommaso Pettinari, Edan Lerner, Gustavo D\"uring* · `cond-mat.dis-nn` · arXiv:2611.27564v1 · relevance 0.10

- **In one sentence**: Using the mean-field KHGPS model of interacting anharmonic oscillators, this paper links the universal omega^4 low-frequency density of states of glasses to the replica-symmetry-broken glassy phase, contrasts it with non-universal gapless spectra at the replica-symmetric boundary, and shows a discontinuous RS-RSB transition can arise from a suitable choice of quenched disorder.
- **In plain words**: Glasses contain a universal pattern of very low-energy vibrational modes: the number of modes at low frequency grows as the fourth power of frequency. This paper uses a simplified, idealized mean-field model of oscillators with random couplings to study where that pattern comes from. The authors report that the universal pattern appears inside the glassy phase, while the spectrum at the edge of the non-glassy phase depends on the details of the disorder.
- **Why it matters**: The origin of the universal low-frequency spectrum in glasses is still poorly understood, so tying it to a specific glassy phase in a solvable model is a useful step. The text also reports that a glass-like transition can become discontinuous without an external field, but how far this carries over to real glasses is not established by the text.
- **Background needed**: - Glass: a solid without long-range crystal order; its low-energy excitations are not fully explained by ordinary crystal vibrations.
- Density of states: how many vibrational modes exist at each frequency; a power law like omega^4 means very few low-frequency modes, with a specific scaling.
- Mean-field model: an idealized model where each part interacts with an average effect of all others, making the math solvable.
- Anharmonic oscillator: a vibrating unit whose restoring force is not a simple linear spring, so it can have multiple stable positions (bistable potentials).
- Quenched disorder: random interactions fixed at random when the system is formed and not changing over time, like the frozen randomness in a glass.
- Replica symmetry breaking (RSB): a mathematical description of the many-valley energy landscape of spin glasses; the replica-symmetric (RS) phase is the simpler, less structured one.
- Continuous vs. discontinuous transition: continuous transitions show smooth changes and diverging susceptibilities (responses); discontinuous ones jump abruptly.
- Susceptibility: how strongly a system responds to a small applied influence. · level: research-level

<details><summary>Original abstract</summary>

The universal low-frequency nonphononic density of states $\mathcal{D}_\mathrm{G}(\omega)\sim\omega^4$ is a robust feature of structural glasses, yet its origin remains poorly understood. Here we investigate this question using the mean-field KHGPS model of interacting anharmonic oscillators. We show that the universal quartic spectrum is deeply rooted in the glassy, replica-symmetry-broken (RSB) phase, whereas the gapless density of states found at the boundary of the replica-symmetric (RS) phase is non-universal and depends sensitively on the details of the quenched disorder. We formulate a simplified variant of the KHGPS model that allows us to characterize the crossover between these two regimes and provides a physical interpretation of the associated crossover frequency scale. We further show that the conventional, spin-glass-like, continuous RS-RSB transition, accompanied by diverging susceptibilities, can be suppressed by an appropriate choice of the quenched disorder, allowing for a discontinuous RS-RSB transition even in the absence of an external field. Our results establish a direct connection between the emergence of the universal $\omega^4$ spectrum and the glassy phase, and provide a simple framework for exploring the low-temperature properties of glasses and the soft localized excitations that emerge from bistable local potentials.

</details>

## Condensed matter

### [Magnetic-Field Response of a Hyperbolic Kitaev Spin Liquid](https://arxiv.org/abs/2611.27819)
*Tao Yang, Baigeng Wang, Rui Wang et al.* · `cond-mat.str-el` · arXiv:2611.27819v1 · relevance 0.14

- **In one sentence**: Using infinite tensor-network (iPEPS) simulations on a Kitaev honeycomb-type model placed on a hyperbolic {8,3} lattice, this paper compares how the fractionalized spin liquid responds to uniform versus staggered [111] magnetic fields.
- **In plain words**: The paper studies a quantum magnet whose spins are arranged on a lattice with negative curvature, like a saddle surface extended forever. Such magnets can host a "spin liquid," a state where the spins stay disordered and their collective excitations behave like split-apart particles. The authors ask how this state reacts when a magnetic field is applied, and they find that a uniform field and a staggered field produce quite different responses.
- **Why it matters**: It connects the geometry of the lattice to the behaviour of an exactly solvable spin liquid under perturbations that break its conserved structure, which is useful for understanding how such states can be probed. The text does not establish broader implications beyond this model, so the wider significance is uncertain.
- **Background needed**: - Spin liquid: a magnetic state with no ordered pattern even at low temperature, whose excitations can be fractionalized.
- Kitaev model: an exactly solvable spin model whose spins split into emergent Majorana particles moving on a background of fixed "flux" values.
- Hyperbolic lattice: a tiling of negatively curved space; {8,3} means eight-sided polygons with three meeting at each vertex.
- Flux conservation: in the Kitaev model, the local flux through each plaquette (loop) is conserved unless a perturbation like a magnetic field breaks this.
- Tensor network (iPEPS): a numerical method that represents an infinite quantum state compactly, used here to approximate ground states.
- Effective Majorana model: a simplified description of the low-energy particles, here derived to third order in perturbation theory. · level: research-level

<details><summary>Original abstract</summary>

Hyperbolic geometry can give rise to Kitaev spin liquids with distinct flux structures and Majorana spectra, raising the question of how these fractionalized states respond beyond exactly solvable limits. We address this question on the Kekul\'e-colored hyperbolic {8,3} lattice by developing an infinite projected entangled-pair-state approach with flux-resolved loop-gas initialization and geometry-adapted tensor-network contraction. Under uniform and staggered [111] magnetic fields, we find markedly different many-body responses. The uniform field induces a sharp change between competing variational branches at weak field, whereas the polarization and mean plaquette flux evolve over a much broader field range under the staggered field. Exchange-energy competition helps explain the different response scales, while third-order effective Majorana models in a fixed-flux background exhibit contrasting low-energy spectra. Our results connect the geometry-dependent fractionalized structure of a solvable hyperbolic spin liquid to its many-body response under physical perturbations that break flux conservation.

</details>

### [Quantum-Chaos-Assisted Measure Synchronization in a Double-Well Ultracold Bose Gas](https://arxiv.org/abs/2611.27256)
*Xianchao Le, Jiaxin Peng, Weiping Zhang et al.* · `cond-mat.quant-gas` · arXiv:2611.27256v1 · relevance 0.14

- **In one sentence**: A theoretical study of measure synchronization, and its speed-up by quantum chaos, in a two-component ultracold Bose gas trapped in a double-well potential modeled as a many-body bosonic Josephson junction.
- **In plain words**: This paper studies a question about how parts of a quantum system can fall into step with each other. The system is a cloud of ultracold atoms held in a trap with two wells, where atoms can slosh back and forth between them. The authors report that, in a certain chaotic regime found by looking at energy-level statistics, the system reaches this synchronization, and that chaos makes it happen faster while the quantum entanglement between parts moves toward what a random state would show.
- **Why it matters**: It links quantum chaos, synchronization, and entanglement in a closed (conservative) many-body system, which may guide later work on how chaos can help synchronization. The text does not show how broadly these findings apply beyond this specific model, so the wider significance is uncertain.
- **Background needed**: - Measure synchronization: a form of synchrony in which the measured quantities of coupled subsystems fall into step, even when the full dynamics is not simply in lockstep.
- Bosonic Josephson junction: two trapped clouds of bosons (particles that can pile into the same state) that exchange particles through a barrier, analogous to a superconducting Josephson junction.
- Ultracold atoms: atomic gases cooled to temperatures near absolute zero and held by laser or magnetic fields.
- Quantum chaos: signatures of chaotic behavior in quantum systems, often detected by statistics of energy levels (spectral statistics).
- Entanglement entropy: a measure of how strongly quantum correlations link one part of a system to the rest; a "random-state prediction" is the value expected for a generic, scrambled state.
- Conservative system: one with no energy loss to the environment. · level: research-level

<details><summary>Original abstract</summary>

This paper investigates measure synchronization (MS) in a two-component ultracold atomic system confined in a double-well potential, which realizes a quantum many-body bosonic Josephson junction. Through spectral-statistics analysis, we identify the quantum chaotic parameter regime and confirm that the system achieves MS within this regime with weak dependence on the initial energy imbalance. We further show that chaotic dynamics not only significantly shortens the time scale for establishing synchronization but is also accompanied by entanglement entropy approaching the random-state prediction. These results reveal close connections among quantum chaos, MS, and quantum entanglement in conservative quantum many-body systems and may motivate further studies on the underlying mechanisms of chaos-assisted synchronization.

</details>

## Particle physics

### [nuSTORM: a unique GeV electron-(anti)neutrino machine](https://arxiv.org/abs/2611.27549)
*Xianguo Lu* · `physics.acc-ph` · arXiv:2611.27549v1 · relevance 0.17

- **In one sentence**: A conference review arguing that the nuSTORM concept, a neutrino beam produced from a muon storage ring, could supply well-characterised electron-(anti)neutrino beams needed for cross-section inputs to Dirac CP phase measurements.
- **In plain words**: This is a short conference write-up about tiny, nearly massless particles called neutrinos. It reviews current experiments that study how neutrinos change type, which may help explain why matter dominates over antimatter in the universe. The author argues that a proposed facility, nuSTORM, could produce especially clean beams of one neutrino type that would help other measurements.
- **Why it matters**: Better measurements of how neutrinos interact could reduce uncertainty in experiments that look for differences between neutrinos and antineutrinos, which bear on the matter-antimatter puzzle. The text is a position argument from a conference talk and does not show results from an actual facility, so its practical impact is uncertain.
- **Background needed**: - Neutrinos are very light, electrically neutral particles that rarely interact with matter.
- Neutrinos come in types (electron, muon, tau), and they can switch between types as they travel, called oscillation.
- The Dirac CP phase (δCP) is a parameter describing a possible difference in how neutrinos and antineutrinos oscillate; a nonzero value would mean a CP violation.
- Accelerator experiments send beams of neutrinos over long distances and compare what arrives with what was sent.
- Cross sections measure how likely a particle is to interact with a target; they must be known precisely to interpret oscillation data.
- A muon storage ring is a circular magnet loop that holds muons, which decay to produce neutrino beams with known composition. · level: research-level

<details><summary>Original abstract</summary>

In this conference contribution, I briefly review current experimental programmes measuring the Dirac CP phase {\delta}CP using accelerator neutrinos. I argue that the nuSTORM concept---neutrino beams from a muon storage ring---could provide high-quality electron-(anti)neutrino beams needed for the cross-section inputs to {\delta}CP measurements.

</details>

### [Optimized solver algorithms for computing $\mathrm{Tr}(A^{-1})$](https://arxiv.org/abs/2611.26854)
*Benjamin Luke, Sudip Shiwakoti, Shayan Nadeem et al.* · `hep-lat` · arXiv:2611.26854v1 · relevance 0.14

- **In one sentence**: The paper proposes "Twin" Krylov solvers (Twin-BiCG and Twin-BiCGStab) that build the solver's polynomial once and reuse it across noise vectors, plus a polynomial approximation and singular-value deflation scheme, to speed up Hutchinson-style estimation of Tr(A^{-1}) for lattice QCD quark matrices.
- **In plain words**: Physicists studying the strong force on a computer grid often need the trace of the inverse of a huge matrix, which is a single summary number that is expensive to get exactly. The standard shortcut uses many random noise vectors, and each one requires solving a large system of equations. This paper introduces solver methods that reuse work from one solve on the others, and a cheaper scheme that handles most noise vectors with an approximation, reporting a 17-fold speedup over the standard method in the authors' tests.</plain>
<parameter name="why">Lattice QCD calculations are computationally expensive, so a sizeable reduction in the cost of this trace step could matter for them. The text reports the speedup only from the authors' own tests, and does not show how it carries over to other problems or hardware.</plain>
<parameter name="background">- Matrix inverse and trace: the trace is the sum of diagonal entries; the inverse of a matrix A is the matrix that undoes A.
- Linear system Ax = b: solving for x is the core computational cost.
- Hutchinson's method: estimates a trace by averaging over random noise vectors b.
- Krylov solvers (BiCG, BiCGStab): iterative algorithms that solve Ax = b by building up a sequence of vectors and a polynomial.
- Lattice QCD: a numerical simulation of quarks and gluons on a discrete space-time grid, which produces very large sparse matrices.
- Singular value deflation: removing the few directions where the matrix is most ill-conditioned so the rest converges faster.
- **Background needed**:  · level: research-level

<details><summary>Original abstract</summary>

Estimating the trace of the inverse of a large quark matrix is a longstanding problem in lattice QCD. The standard approach is Hutchinson's method, which uses random noise vectors to estimate the trace to a desired statistical tolerance. Each noise vector $b$ requires solving a system of linear equations $Ax = b$. In this work, we introduce a new class of Krylov solvers for this task, called Twin methods. Twin methods generate the Krylov polynomial once then reuse it on all other right-hand sides. This reduces the number of basic linear algebra operations in the algorithm and therefore lowers the trace computation time. We apply the Twin approach to BiCG and BiCGStab and test them on lattice QCD matrices of varying size and in a range of computing contexts. We also present a more economical estimation of $\mathrm{Tr}(A^{-1})$ which implements a polynomial approximation of $A^{-1}$ and a singular value deflation. In this scheme, the solvers are applied to only a few noise vectors, and the remainder are treated by the polynomial and the deflation. In our tests, the polynomial approximation combined with the deflation yield a 17-fold speedup in the time required to compute the trace over standard Hutchinson's method.

</details>

## Nuclear physics

### [Thermal photon production in massless boost-invariant gases: hydrodynamization without thermalization](https://arxiv.org/abs/2611.27332)
*Caio V. P. de Brito, Gabriel S. Denicol* · `nucl-th` · arXiv:2611.27332v1 · relevance 0.09

- **In one sentence**: Using relativistic kinetic theory with a relaxation-time Boltzmann equation solved by the method of moments, this paper studies hydrodynamization versus thermalization in a boost-invariant expansion of a massless gas and how the resulting non-equilibrium state affects thermal photon emission rates in the forward-scattering approximation.
- **In plain words**: This paper looks at the hot, dense matter formed in heavy-ion collisions, such as those at particle colliders, as it expands and cools. The authors model it as a simple gas of massless particles and compute how it evolves. They find that its overall energy and pressure behave like a smooth fluid well before the particles reach a fully equilibrated distribution, and that the way this non-equilibrium state changes the rate of emitted thermal photons (particles of light) can be significant.
- **Why it matters**: Thermal photons are one of the few signals that carry information from inside the collision fireball, so how much early non-equilibrium behaviour shifts their predicted yield matters for interpreting experiments. The claim that fluid-like behaviour can appear without full thermalization is a modelling result from a simplified setup, so its reach to real collisions is uncertain.
- **Background needed**: - Heavy-ion collisions: nuclei smashed at near light speed to create a quark-gluon plasma, a very hot state of matter.
- Hydrodynamics: describing a fluid by its averaged quantities (energy, pressure, flow) rather than each particle.
- Thermalization: when particles reach a standard equilibrium energy distribution; hydrodynamics can apply before this is complete.
- Boltzmann equation: a kinetic equation tracking how the distribution of particles changes through motion and collisions.
- Relaxation-time approximation: a simplified model where collisions push the system toward equilibrium at a set rate.
- Method of moments: solving for averaged properties (moments) of the distribution instead of the full distribution.
- Boost-invariant longitudinal expansion: a idealized expansion along the beam direction that looks the same to observers moving at any speed along that axis.
- Thermal photons: light emitted by the hot matter itself, not from the initial collision. · level: research-level

<details><summary>Original abstract</summary>

We study hydrodynamization and thermalization in ultrarelativistic heavy-ion collisions using relativistic kinetic theory. Modelling the quark-gluon plasma as a classical gas of massless particles undergoing a boost-invariant longitudinal expansion, we solve the Boltzmann equation in the relaxation-time approximation via a semi-analytical method based on the method of moments. We show that the energy-momentum tensor is well described by relativistic fluid dynamics even when the system is far from local equilibrium. The single-particle distribution function, on the other hand, is not well approximated by a hydrodynamic truncation, suggesting that the onset of hydrodynamic behaviour does not require thermalization. We then quantify how the departure from equilibrium affects the emission rate of thermal photons in the forward scattering approximation, and show that non-equilibrium corrections beyond the hydrodynamic limit can have a significant impact on this observable.

</details>

### [Nuclear Urca cooling in magnetar crust and anomalous heating](https://arxiv.org/abs/2611.27628)
*LInjing Qi, Qiye Hu, Xinxu Wang et al.* · `nucl-th` · arXiv:2611.27628v1 · relevance 0.09

- **In one sentence**: The paper argues that in magnetars, strong magnetic fields and finite-temperature effects alter the nuclear Urca neutrino-cooling process for the 29Na-29Mg pair, which may help explain the high surface temperatures observed in these stars.
- **In plain words**: Magnetars are dense, collapsed stars with extremely strong magnetic fields, and they are often hotter on the surface than ordinary neutron stars of their age would be. Neutron stars cool partly by releasing neutrinos, tiny nearly massless particles, and one channel for this is the "nuclear Urca" process, which involves pairs of atomic nuclei changing into each other. This paper reports that, using a new calculation that includes both the magnetic field and heat, the cooling from this process can be weakened or strengthened depending on the field strength and crust density, which could leave the star hotter.
- **Why it matters**: The surface temperature of magnetars is an open puzzle, and the authors suggest a cooling-based explanation that would be new if confirmed. The text does not show how strongly the result depends on its nuclear inputs or whether it matches observations, so it should be read as a proposed possibility rather than an established answer.
- **Background needed**: - Neutron star: the collapsed core of a massive star, roughly city-sized and extremely dense.
- Magnetar: a neutron star with a magnetic field far stronger than typical ones.
- Neutrino cooling: a star loses heat by emitting neutrinos, which pass through matter almost unimpeded.
- Nuclear Urca process: a cycle in which nuclei capture electrons and emit neutrinos, then reverse, cooling the star.
- Urca pair: the two nuclei (here 29Na and 29Mg) that convert into each other in this process.
- Finite temperature: at higher heat, some nuclei sit in excited energy states that can change the cooling rate.
- Crust density: the density of the outer layer of the star, where these nuclei exist. · level: research-level

<details><summary>Original abstract</summary>

We present a new result that the nuclear Urca process in magnetars, associated with ultrastrong magnetic field, dramatically alters the neutrino cooling efficiency to support higher surface temper ature, which is not common in ordinary neutron stars. A new formalism for neutrino luminosity accommodating finite temperature on top of magnetic field is extended with the use of realistic nuclear structure inputs for the Urca pair 29Na-29Mg. We find that the neutrino luminosity of Urca pair shows a spiral variation as a function of magnetic field and crust density, while the Urca pair persists, in contrast to previous studies. Applying geometrically correct volumetric energy loss rate to Urca shell at fixed density with varying magnetic field strength, our results show that thermally populated excited states at finite temperature enhance neutrino luminosity, whereas conditions con strained Urca-pair formation driven by ultrastrong magnetic field reduce cooling efficiency, which can explain high temperature of magnetar surface as a new possibility.

</details>

## Quantum information and computing

### [Detection of genuine multipartite entanglement by means of entanglement monotones](https://arxiv.org/abs/2611.27660)
*Sylvain Carrozza, Johann Chevrier, Luca Lionni* · `quant-ph` · arXiv:2611.27660v1 · relevance 0.17

- **In one sentence**: The paper looks for entanglement monotones (quantities that cannot increase under local operations) that certify "irreducible" genuine multipartite entanglement, proves a no-go result for combining LOCC-monotonicity with subadditivity, and shows a subfamily of the proposed monotones detects genuine tripartite entanglement in three-qubit systems.
- **In plain words**: The paper studies how to measure whether several quantum particles are entangled in a truly joint way, not just in pairs or as a product of smaller linked groups. The authors first show that one natural way of scoring this cannot satisfy two desirable rules at once. They then relax one rule and build a simple method for producing scores that do work, and report that a subset of these scores detects every form of genuine three-particle entanglement in three-qubit systems.
- **Why it matters**: Entanglement is a central resource for quantum computing and communication, and reliable ways to tell its genuinely multipartite forms apart are needed to characterise such resources. The text does not indicate applications beyond this theoretical characterisation, so its wider practical significance is unclear from the given material.
- **Background needed**: - Entanglement: a correlation between quantum particles that has no classical counterpart.
- Multipartite entanglement: entanglement shared among three or more particles (parties), as opposed to just two.
- Irreducible entanglement (as defined here): an n-party state that cannot be written as a product of states each involving at most n-1 parties.
- LOCC (local operations and classical communication): the operations each party can perform on its own particle while talking classically to the others; an entanglement measure should not increase under these.
- LO-monotonicity: the weaker requirement that the measure does not increase under local operations alone, without classical communication.
- Subadditivity: a rule that a combined quantity is at most the sum of its parts.
- Entanglement monotone: a function of a quantum state that does not increase under the allowed operations, used as an entanglement score.
- Three-qubit system: a set of three two-level quantum systems, the simplest case for genuine tripartite entanglement. · level: research-level

<details><summary>Original abstract</summary>

We look for pure state entanglement monotones that may serve as certificates of a strong form of genuine multipartite entanglement, that we refer to as irreducible entanglement: a $D$-partite state (with $D\geq 3$) is irreducibly $D$-partite entangled if it cannot be decomposed as a product of states that are at most $(D-1)$-partite entangled. We start by establishing a no-go result proving that no reasonable genuine multipartite entanglement entropy can simultaneously obey LOCC-monotonicity and subadditivity. After relaxing the first condition to LO-monotonicity, we provide a simple method generating genuine multipartite entanglement monotones with the desired properties. Focusing on a subfamily of these monotones, we show that they are able to detect any form of genuine tripartite entanglement in three-qubit systems.

</details>

### [Gravity-induced entanglement assisted by an additional interaction using magic angle calibration](https://arxiv.org/abs/2611.26755)
*Daisuke Miki, Alfred Li, Yanbei Chen* · `quant-ph` · arXiv:2611.26755v1 · relevance 0.13

- **In one sentence**: A proposed protocol for testing whether gravity alone can entangle two masses, using an added controllable coupling calibrated at a magic-angle null of the projected tidal coupling so that the protocol needs less absolute force-noise suppression than direct schemes.
- **In plain words**: The paper asks whether gravity can create quantum entanglement between two small masses, which would indicate that gravity is not just a classical force that works through local operations and classical communication. Gravity is so weak that direct attempts require extremely low force noise, so the authors propose adding a controllable extra interaction that sits just below the threshold where it could itself create entanglement. Gravity then only has to supply the small remaining part, and an angle-based null setting is used to calibrate the extra interaction and noise.
- **Why it matters**: The question bears on whether gravity must be quantized, a long-running open problem in physics. The text is a theoretical protocol only and reports no experimental result, so its practical feasibility is not shown here.
- **Background needed**: - Entanglement: a quantum link between two objects whose states cannot be described independently.
- LOCC (local operations and classical communication): the set of operations that cannot by themselves create entanglement; a classical-only description of gravity would respect this.
- Gravity-induced entanglement: the idea that if gravity entangles two masses, gravity must have some quantum character.
- Test masses and force noise: small objects whose motion is disturbed by unwanted random forces that must be kept small.
- Tidal coupling: how the gravitational pull between two nearby masses varies with their relative position; the "magic angle" is a geometry where its projected effect vanishes.
- Markovian model: an assumption that the environment has no memory of past effects. · level: research-level

<details><summary>Original abstract</summary>

Gravity-induced entanglement provides an operational test of whether gravitational dynamics are compatible with local operations and classical communication (LOCC), but the weakness of the gravitational interaction and the presence of force noise make direct entanglement generation extremely demanding. We introduce a controllable additional coherent interaction that biases two test masses close to, but within, a separability-preservation bound, so that the weak Newtonian coupling supplies only the remaining coherent contribution needed for entanglement. If the additional interaction alone is shown to be incapable of generating entanglement, while entanglement is observed when gravity is included, the gravitational interaction provides a non-LOCC contribution. Since gravity cannot be turned off, we use a magic-angle null of the projected tidal coupling to calibrate the additional interaction and force noise. If the additional dynamics is certified to preserve separability at the magic angle and entanglement is subsequently observed in a non-null configuration, the gravitational contribution is incompatible with an LOCC description within the Markovian model. The protocol trades the stringent absolute force-noise requirement of direct schemes for precision in controlling the additional coupling, its backaction, and angle-dependent systematics.

</details>

## Optics and atomic physics

### [Benchmark Ne-like Transitions of W, Re, Os, Ir, and Bi Measured by High-resolution TES x-ray Spectroscopy with Absolute Energy Calibration](https://arxiv.org/abs/2611.26801)
*G. Mondeel (Clemson University, Massachusetts Institute of Technology), C. A. Faiyaz (Clemson University) et al.* · `physics.atom-ph` · arXiv:2611.26801v1 · relevance 0.13

- **In one sentence**: High-resolution TES microcalorimeter measurements of n=2-3 transitions in Ne-like W, Re, Os, Ir and Bi, using an X-ray fluorescence source calibrated with K-shell lines of metals to reach sub-eV absolute energy accuracy.
- **In plain words**: This paper reports precise measurements of the X-ray light emitted by heavy metal atoms (tungsten, rhenium, osmium, iridium and bismuth) that have been stripped of most of their electrons, leaving only ten. The authors used a very sensitive X-ray detector and a new X-ray source made from metals whose emission lines are well known, so the energy scale could be fixed to within a fraction of an electron volt. The results are offered as reference values that theories of how these atoms hold together can be checked against.
- **Why it matters**: Atoms this heavy are a demanding test of relativistic atomic theory, and the text says the data are meant as stringent benchmarks for it. The text does not go beyond that, so any wider application (for example to fusion plasmas or astrophysical X-ray spectra) is not established here.
- **Background needed**: - Highly charged ion: an atom that has lost many electrons; Ne-like means it keeps the 10-electron configuration of neon.
- Transition: an electron dropping between energy levels and emitting light of a specific energy (here X-rays).
- n=2-3 transitions: jumps between the second and third electron shells.
- Z: the number of protons in the nucleus; Z > 74 covers elements heavier than tungsten.
- Relativistic effects: corrections needed because inner electrons in heavy atoms move close to the speed of light; they shift the energies measured.
- TES (transition-edge sensor): a superconducting microcalorimeter that measures the energy of single X-ray photons by the small heat they deposit.
- EBIT (electron beam ion trap): a device that produces and holds highly charged ions using an electron beam.
- Sub-eV accuracy: energy uncertainty below one electron volt, a very fine level of precision for X-rays.
- K-shell lines: X-ray emission from the innermost electron shell of a metal, used here as known reference energies. · level: research-level

<details><summary>Original abstract</summary>

We present high-resolution measurements of $n=2$-3 transitions in Ne-like tungsten, rhenium, osmium, iridium, and bismuth using a transition-edge sensor (TES) microcalorimeter. These measurements provide new benchmarks for Ne-like ions in the high-$Z$ regime ($Z > 74$), extending previous EBIT studies of the sequence. To achieve sub-eV accuracy, we developed a dedicated x-ray fluorescence source employing well-characterized K-shell emission lines from metallic elements. Our results offer stringent tests for relativistic atomic structure theories and demonstrate the advantage of TES spectroscopy for precision measurements in highly charged ions.

</details>

### [Monolithic ultraviolet-to- near infrared photodetection enabled by an aluminium oxide photonic platform](https://arxiv.org/abs/2611.27333)
*Firehun T. Dullo, Marco Povoli, Ozhan Koybasi et al.* · `physics.optics` · arXiv:2611.27333v1 · relevance 0.10

- **In one sentence**: The paper demonstrates atomic-layer-deposited aluminium oxide waveguides evanescently coupled to on-chip silicon p-i-n photodiodes, giving waveguide-integrated photodetection from 375 nm to 780 nm, including centimetre-scale ultraviolet Mach-Zehnder circuits.
- **In plain words**: Light-guiding chips are used to route and measure light in tiny circuits, much like wires carry electricity. This work builds such a chip from aluminium oxide, a transparent material deposited one thin atomic layer at a time on top of silicon, and adds silicon light sensors that can detect light from ultraviolet to near-infrared. The authors report that the sensors respond to light at 375, 658 and 780 nm, with very low dark current (the small signal present when no light is shining).
- **Why it matters**: Ultraviolet light is hard to handle on integrated chips, and most silicon-based sensors do not work well there, so a platform that covers this range could matter for sensing, spectroscopy and quantum experiments. The text reports a roughly 15-fold higher response at 375 nm than a silicon nitride version of the same detector, but the wider impact is not established by this text alone.
- **Background needed**: - Photonic integrated circuit: a chip that guides light through tiny waveguides, as electronic circuits guide current through wires.
- Waveguide loss: how much light leaks or scatters as it travels; lower loss allows longer circuits.
- Evanescent coupling: light passing through one waveguide leaks into a nearby structure through its faint outer field, letting light reach a detector without being blocked.
- Photodiode (p-i-n): a semiconductor device that turns light into an electrical current; a p-i-n structure is a common, efficient design.
- Dark current: the small leakage current a detector produces with no light, a measure of its noise.
- Mach-Zehnder interferometer: a circuit that splits light into two paths and recombines them, used for measuring phase and for switching.
- Atomic-layer deposition (ALD): a coating method that builds materials one atomic layer at a time, giving precise, uniform films.
- Silicon nitride (Si3N4): another material commonly used for chip waveguides, used here as a comparison. · level: research-level

<details><summary>Original abstract</summary>

Broadband photonic integrated circuits require waveguide platforms that combine low optical loss across a wide spectral range with integrated photodetection. Here we demonstrate a monolithically integrated atomic-layer-deposited (ALD) aluminium oxide (Al$_2$O$_3$)-on-silicon platform enabling waveguide-coupled photodetection from the ultraviolet to the near-infrared. The architecture employs evanescent coupling between low-loss Al$_2$O$_3$ waveguides and silicon p-i-n photodiodes. The platform supports photodetection at 375, 658 and 780 nm, extending integrated silicon photodetection into the ultraviolet. The devices exhibit linear photocurrent scaling with optical power, dark currents of approximately 2 pA at 50 V reverse bias and nanosecond-scale temporal response. We further demonstrate centimetre-scale ultraviolet Mach-Zehnder interferometer circuits with integrated photodiodes. The same detector architecture is implemented with Si$_3$N$_4$ waveguides, whereas the lower ultraviolet propagation loss of Al$_2$O$_3$ enables an approximately 15-fold higher photodetection response at 375 nm. These results establish ALD Al$_2$O$_3$ as a broadband integrated photonics platform for sensing, spectroscopy and quantum technologies.

</details>

## Fluids and plasma

### [Stabilized negative viscosity governs ocean jets before, during and after they leave the coast](https://arxiv.org/abs/2611.24399)
*Boris Galperin, Alexei Chekhlov, Ilya Staroselsky et al.* · `physics.flu-dyn` · arXiv:2611.24399v1 · relevance 0.08

- **In one sentence**: Using two years of SWOT wide-swath altimetry across five subtropical western boundary currents, the paper measures eddy momentum fluxes in each current's frame and reports a stabilized negative viscosity (negative Laplacian balanced by a positive biharmonic term) along the slope, a sign reversal at separation, and a return of negative viscosity in the free jets, with an eddy-resolving reanalysis said to show the same form across three basins.
- **In plain words**: Ocean currents such as the Gulf Stream are fed by swirling eddies, and sometimes those eddies push energy back into the current that created them, which acts like negative friction. This paper uses two years of satellite measurements of sea-surface height to track how eddies push on five major ocean currents, both while they hug the coast and after they break away into open water. The authors report that the eddies speed the flow up along the slope, slow it down where the current separates from the coast, and speed it up again further out.
- **Why it matters**: Eddy effects on large currents are usually represented in climate and ocean models with simple friction-like terms, so a sign-changing, stabilized form would matter if it holds up for how models should handle eddies. The text does not show how far the result extends beyond these currents or what it means for model performance, so its broader significance is unclear from this brief alone.
- **Background needed**: - Eddy viscosity: a model term describing how turbulent swirls transfer momentum, normally acting like friction that smooths the flow.
- Negative viscosity: the opposite case, where eddies move momentum toward the stronger flow and sharpen it, so the jet feeds on its eddies.
- Laplacian and biharmonic terms: mathematical smoothing operators; the second is a sharper, higher-order version. Combining a negative Laplacian with a positive biharmonic keeps the problem mathematically well behaved.
- Potential vorticity: a conserved quantity combining spin and stratification, used to describe how ocean flows mix.
- Beta effect: the change of the Coriolis force with latitude (or with sloping topography), which steers eddies and jets.
- Western boundary current: a strong, narrow current on the western side of an ocean basin, such as the Gulf Stream or Agulhas.
- SWOT: a satellite mission that maps sea-surface height across a wide swath, resolving eddies.
- Deformation radius: the natural length scale over which rotation and stratification constrain eddies. · level: research-level

<details><summary>Original abstract</summary>

Eddies in rotating turbulence can feed the jets that spawn them, resulting in the negative viscosity phenomenon. Taken alone, a negative viscosity represents up-gradient eddy fluxes and is often referred to as "antifriction" or "antidiffusion". Mathematically, it leads to an ill-posed problem. In two-dimensional turbulence theory, this problem can be resolved by representing the transfer from small to large scales by a stabilized negative viscosity (SNV), in which a negative Laplacian viscosity is balanced by its positive biharmonic counterpart. In purely two-dimensional turbulence, by the Taylor identity, a negative viscosity is up-gradient transport of vorticity, which mixing cannot produce; on a slope, mixing of potential vorticity can mimic it, and we test for this. Using two years of wide-swath satellite altimetry (SWOT), we measure the eddy momentum flux across the five subtropical western boundary currents in each current's own frame. Along the continental slope the eddies act with a negative viscosity of order $-10^{3}$ m$^{2}$ s$^{-1}$, with the SNV structure resolved in the Gulf Stream and the Agulhas. At separation from the slope the sign reverses in all five currents, and the eddies brake the flow. Downstream, in the free jets, the negative viscosity returns on the cyclonic flank, strengthened to $-10^{4}$ m$^{2}$ s$^{-1}$. Separation is where the current leaves the strong topographic $\beta$ of the slope, the constraint that orders the eddy transfer. In an eddy-resolving reanalysis the SNV form holds across three ocean basins, with its shape parameter set by the deformation radius.

</details>

### [Shear thinning confines the wall forcing: laminar chaotic mixing of Carreau fluids in a rotating arc-wall mixer](https://arxiv.org/abs/2611.27150)
*Teodor Burghelea* · `physics.flu-dyn` · arXiv:2611.27150v1 · relevance 0.06

- **In one sentence**: Two-dimensional simulations show that shear thinning (viscosity dropping under fast shear) reduces laminar chaotic mixing in a rotating arc-wall mixer mainly by shortening the layer near the moving walls that the forcing reaches, with the penetration length predicting mixing efficiency (r² = 0.97).
- **In plain words**: This paper looks at how stirring a thick, syrup-like liquid works when its thickness drops as it is pushed harder. The stirrers are curved wall segments that swing back and forth in a channel, and the author simulated fluids with different degrees of shear thinning. The main finding is that mixing gets about 14 percent worse as the fluid thins less, and this comes from the stirring effect being confined to a thin layer near the walls rather than from changes in the main flow.
- **Why it matters**: The paper suggests that in wall-driven mixers the useful quantity is how far the wall forcing reaches, not the bulk viscosity, and that mixing per unit energy can improve for shear-thinning fluids at higher rotation speeds. These are simulation results for one two-dimensional geometry, so how far they carry to real mixers is not established by the text.
- **Background needed**: - Shear thinning: a fluid whose resistance to flow (viscosity) falls as it is sheared faster; the power-law index N measures this, with N = 1 meaning ordinary (Newtonian) behaviour.
- Laminar chaotic mixing: stirring without turbulence, where smooth flow folds and stretches fluid so that blobs of dye spread through the mixture.
- Chaotic saddle: a region of the flow where fluid particles linger and get stretched before escaping.
- Strouhal number: a dimensionless measure of how fast the walls oscillate relative to the flow.
- Peclet number: the ratio of how fast material is carried by flow to how fast it spreads by molecular diffusion; higher means mixing is harder to achieve by diffusion alone.
- Lamellar model: a simplified model that treats the mixture as thin stretched sheets of fluid.
- Carreau fluid: a standard mathematical model of a shear-thinning fluid. · level: research-level

<details><summary>Original abstract</summary>

With two-dimensional simulations of Carreau fluids of power-law index $N$ from 1 to 0.4, I study how shear thinning modifies laminar chaotic mixing in an open channel stirred by three arc-shaped wall segments rotating back and forth periodically, the upper one in anti-phase with the two lower ones. The outlet mixing efficiency falls monotonically, by 14 percent from $N=1$ to 0.4, mostly between $N=0.85$ and 0.6. The bulk flow and its chaotic saddle are nearly unaffected. Shear thinning acts instead through a thin layer of reduced viscosity around the moving arcs: the geometric penetration length of the wall forcing shortens as the 0.3 power of the time-mean wall viscosity, within 4 percent over a fourfold range of forcing. This confinement weakens the stretching, and the penetration length predicts the mixing efficiency ($r^2=0.97$). The optimal Strouhal number stays close to 0.7 for all fluids, but shear thinning narrows the range of efficient periods. A lamellar model indicates that the relative penalty of shear thinning grows with the Peclet number. As the injected power scales with the wall viscosity, the mixing efficiency per unit energy rises 2.6-fold from $N=1$ to 0.4, and at equal energy per unit volume, with a faster rotation, the fluid with $N=0.4$ mixes as well as the Newtonian one, and better at larger energies. In wall-driven mixers, the reach of the forcing, not the bulk viscosity, is the quantity to control.

</details>

## Biological physics

Nothing notable this time.

## Climate, atmosphere and Earth

Nothing notable this time.

## Cosmology

### [Baryon-Enhanced Strong Lensing Signatures of Self-Interacting Dark Matter Subhalos](https://arxiv.org/abs/2611.27249)
*Meiwen Yang, Daneng Yang, Siyuan Hou et al.* · `astro-ph.CO` · arXiv:2611.27249v1 · relevance 0.15

- **In one sentence**: The paper argues that baryons (ordinary matter such as stars) can make self-interacting dark matter subhalos in galaxy clusters into more efficient gravitational lenses than cold dark matter subhalos, and that this could help explain an observed excess of galaxy-galaxy strong lensing.
- **In plain words**: Dark matter may be a little "sticky," with its particles bumping into each other, and this paper asks how that stickiness changes the way small clumps of dark matter bend light around galaxies in clusters. The authors find that when compact stars sit at the centre of these clumps, the dark matter core does not puff out as expected, so the clumps can bend light more strongly than they would under ordinary cold dark matter. They then apply a simplified model to three of the most massive clusters in a large simulation and estimate that the lensing cross sections come out 1.4 to 2.7 times larger than in the standard model.
- **Why it matters**: Recent observations reportedly show more galaxy-galaxy strong lensing than standard cold dark matter predicts, and this work offers a possible explanation tied to self-interacting dark matter. It is a theoretical estimate from a parametric model rather than a direct simulation of the clumps, so the size of the effect should be treated as provisional until tested against data.
- **Background needed**: - Dark matter: invisible matter that makes up most of the mass of galaxies and clusters, detected only through gravity.
- Cold dark matter (CDM): the standard model in which dark matter particles barely interact apart from gravity.
- Self-interacting dark matter (SIDM): a variant in which dark matter particles scatter off each other, reshaping the density profiles of halos.
- Subhalo: a smaller dark matter clump orbiting inside a larger halo, such as a cluster.
- Strong lensing: strong bending of background light by foreground mass, producing arcs and rings.
- Galaxy-galaxy strong lensing (GGSL): lensing by individual galaxies or their subhalos, rather than the whole cluster.
- Core formation and gravothermal collapse: the dark matter centre first flattens into a core, then can later contract to a dense state.
- Baryons: ordinary matter such as gas and stars; here compact stars deepen the gravitational well at the centre.
- TNG300-1: a large cosmological simulation whose clusters are used as test cases. · level: research-level

<details><summary>Original abstract</summary>

Self-interacting dark matter (SIDM) is generally expected to suppress subhalo strong lensing through core formation, with subsequent gravothermal collapse potentially enhancing it. We show that compact stars can make a viable population of galaxy-hosting SIDM subhalos more efficient lenses than their cold dark matter (CDM) counterparts. When the baryonic potential weakens or reverses the inner velocity-dispersion gradient, SIDM halos suppress or bypass core formation, allowing inner densities to grow from early times. The evolved SIDM subhalos produce larger deflection angles and tangential caustics than in CDM. Such galaxy-hosting subhalos also dominate the galaxy-galaxy strong-lensing (GGSL) budget in clusters, yet lie far below the resolution of cosmological simulations. We calibrate a baryonic parametric SIDM model to predict their effects in the three most massive TNG300-1 clusters, finding GGSL cross sections 1.4--2.7 times those in CDM, comparable to the excess inferred in recent analyses. Baryon-enhanced SIDM lensing can thus account for the observed GGSL excess and predicts stronger perturbations from luminous satellites, testable through resolved distortions of background arcs and rings.

</details>

### [SciPIC-lite: A flexible Halo Occupation Distribution pipeline aimed at clustering observables](https://arxiv.org/abs/2611.26785)
*Gabriele Parimbelli, Martin Crocce, Giosu\`e Gambardella et al.* · `astro-ph.CO` · arXiv:2611.26785v1 · relevance 0.13

- **In one sentence**: SciPIC-lite is a public Python library for Halo Occupation Distribution (HOD) modelling that populates simulated dark matter haloes with galaxies, validated by fitting the two-point clustering of H-alpha-selected galaxies from the Flagship 2 simulation using AbacusSummit haloes.
- **In plain words**: Astronomers simulate the invisible dark matter structure of the universe, but galaxies are what we actually observe, so they need rules for where galaxies sit inside that structure. This paper presents a free, modular software tool that places galaxies into simulated dark matter clumps using such rules. The authors test it by matching how galaxies cluster in one large simulation, and they report that the best-fit results hold up across different rule choices.
- **Why it matters**: Surveys of galaxies on the sky will be large, and reliable mock catalogues made from simulations are needed to interpret them and check analysis methods. The paper's main claim is that the fitted results are not sensitive to which modelling choices are made, which is useful for trusting such mocks; the text does not show how widely the tool will be adopted.
- **Background needed**: - Dark matter haloes: dense clumps of invisible matter in simulations where galaxies form.
- Halo Occupation Distribution (HOD): a statistical recipe giving the probability and number of galaxies hosted by a halo of a given mass.
- Two-point correlation function: a measure of how much more likely galaxy pairs are to be found at a given separation than random chance; it describes galaxy clustering.
- Redshift: a measure of distance and look-back time, from the stretching of light as the universe expands; redshift bins split the data by cosmic epoch.
- H-alpha-selected galaxies: galaxies identified by emission from hydrogen's H-alpha spectral line, a marker of star formation.
- Extensions named in the text: assembly bias, velocity bias, conformity and halo profile rescaling, which are refinements to the basic recipe.
- Reduced chi-squared: a standard goodness-of-fit score; values near a common value indicate similar fit quality. · level: research-level

<details><summary>Original abstract</summary>

The Halo Occupation Distribution (HOD) framework provides a flexible approach to modelling the galaxy--halo connection in cosmological simulations, encoding the statistical relationship between galaxies and their host dark matter haloes. We present SciPIC-lite, a new public Python library for fast, flexible, and user-friendly HOD modelling, designed to populate dark matter haloes extracted from cosmological simulations with galaxies and to provide a comprehensive suite of tools for their subsequent analysis. The library is built around a modular and extensible codebase that incorporates the full breadth of the HOD framework, from the core occupation functions to a wide range of physically motivated extensions, making it suitable for a broad spectrum of galaxy clustering applications. We validate and characterise the performance of SciPIC-lite by developing a pipeline to fit the two-point correlation functions of H$\alpha$-selected galaxies from the Flagship~2 simulation across multiple redshift bins. To this end, we populate AbacusSummit dark matter haloes with galaxies according to a variety of HOD parametrisations. We assess the robustness of the fits with respect to the choice of HOD parametrisation and the inclusion of physically motivated extensions, including assembly bias, velocity bias, conformity, and halo profile rescaling. The best-fit models are found to be remarkably robust across different HOD parametrisations and fitting configurations, with reduced $\chi^2$ values clustering tightly around a common value regardless of the model adopted. We exploit these results to generate new AbacusSummit-based galaxy mocks that accurately reproduce the clustering properties of the Flagship~2 H$\alpha$ galaxy population.

</details>

## Galaxies

### [Predicting HCN, HCO$^{+}$, multi-transition CO, and dust emission of star-forming galaxies](https://arxiv.org/abs/2611.27419)
*B. Vollmer (Observatoire astronomique de Strasbourg, France), D. Iung (Observatoire astronomique de Strasbourg et al.* · `astro-ph.GA` · arXiv:2611.27419v1 · relevance 0.13

- **In one sentence**: An analytical model of a turbulent, clumpy star-forming disk is fitted to resolved molecular-line and continuum emission from the central 30 pc of the Circinus Galaxy to infer gas, star-formation and energetics properties.
- **In plain words**: The paper studies the dense, star-forming core of the nearby Circinus Galaxy, using radio and submillimetre light emitted by several gas molecules and by dust. The authors built a simplified mathematical model of a turbulent, lumpy disk of gas and tuned it until it matched the observed emission. From that match they estimate things that are hard to measure directly, such as how gas is inflowing, how fast stars are forming, and how well different molecules trace the amount of gas.
- **Why it matters**: The model suggests that CO(3-2) is a poor guide to the gas mass on these small scales, while HCO+(3-2) may do better, which matters for how extragalactic gas is measured. The claim that gas inflow, rather than supernovae, dominates energy input in this compact region, and its possible link to nested spiral structure, is interesting but rests entirely on one model fitted to one galaxy, so it should be treated as provisional.
- **Background needed**: - Galaxies are often mapped using emission from molecules such as CO, HCN and HCO+, which glow when they are excited by collisions and so reveal where dense gas sits.
- The CO-to-H2 conversion factor (alpha_CO) is the scaling used to turn measured CO brightness into the mass of molecular hydrogen, the main constituent of star-forming gas.
- "Critical density" is the gas density above which a molecule's emission is efficiently excited; molecules with higher critical density trace denser gas.
- The Toomre Q parameter measures how stable a rotating disk is against collapsing into clumps; low values favour clump formation.
- A starburst is a region forming stars much faster than normal; a galactic wind is gas blown out by stellar energy.
- The Circinus Galaxy is a nearby spiral galaxy, and 30 pc is a very small region at its centre. · level: research-level

<details><summary>Original abstract</summary>

We present an analytical model of a turbulent clumpy star-forming disk that reproduces the spatially resolved observations for 6 molecular lines and 3 continuum bands at 250-700~GHz in the central 30~pc of the Circinus Galaxy. Using the properties of the stellar disk as input, and when matched to the line and continuum emission, the model yields the Toomre $Q$ parameter, mass accretion rate $\dot{M}$, metallicity $Z$, and cosmic ray ionization rate $\zeta_{CR}$. These in turn are used to infer the gas properties (surface density, velocity dispersion, and radial velocity) as well as the star formation rate. Our main findings from the model include a low CO-to-H$_2$ conversion factor that varies with radius in the range $\alpha_{\rm CO}=0.5$--1.5 $M_{\odot}$pc$^{-2}/({\rm K\,km\,s}^{-1})$, close to the canonical value for such environments. It shows that CO(3-2) is a poor tracer of the gas mass surface density $\Sigma_{{\rm H}_2}$ on these small scales, which is better represented by molecules such as HCO$^+$(3-2) with higher critical density. The steep relation between $\Sigma_{{\rm H}_2}$ and star formation rate surface density $\dot{\Sigma}_*$ is typical of compact starburst systems, and the star formation rate (10~$M_{\odot}$kpc$^{-2}$yr$^{-1}$ averaged over the disk) is high enough to drive a wind. Despite this, and in contrast to typical large scale galactic disks, the energy injection rate into the ISM is dominated by gas inflow through the disk rather than the supernova rate. As such, the decreasing inflow rate at smaller radii could be caused by a wind, or indicate a recent increase of the mass inflow from larger scales. We suggest that such variations in the inflow rate could be associated with the nested spiral structures which have been observed in Circinus.

</details>

### [A TESS Search for Optical Variability in Intermediate-mass Black Hole Candidates](https://arxiv.org/abs/2611.27890)
*Jinghuai Yao, Wenwen Zuo, Hengxiao Guo et al.* · `astro-ph.GA` · arXiv:2611.27890v1 · relevance 0.13

- **In one sentence**: Using TESS high-cadence photometry with the Quaver pipeline and artifact-aware metrics, the authors search for optical variability in IMBH-mass AGN candidates, fit damped random walk models, and cross-check amplitudes with ZTF difference-image photometry.
- **In plain words**: Some galaxies have supermassive-looking centers fed by gas falling onto a black hole, and their brightness flickers. This paper looks for that flicker in a mid-sized class of black holes (roughly 100 to a million times the Sun's mass) using the TESS space telescope, which photographs the sky often. The authors found 3 sources with high-confidence flickering and 17 with medium-confidence flickering.
- **Why it matters**: Black holes in this mass range are hard to detect, so a way to spot them through variability is useful. The paper also reports a tentative link between flicker timescale and black hole mass, but only in a small subset, so that link is not yet established.
- **Background needed**: - Active galactic nuclei (AGN): galaxy centers where material falling onto a black hole makes them unusually bright.
- Intermediate-mass black hole (IMBH): a black hole of roughly 100 to 1,000,000 solar masses, between stellar-mass and supermassive types.
- Optical variability: changes in brightness over time; the timescale of the changes can hint at the black hole's mass.
- Damped random walk (DRW): a standard statistical model for random-looking brightness wandering that settles toward an average over a characteristic timescale.
- TESS: a NASA space telescope originally built to find exoplanets, observing large sky areas in roughly 28-day sectors.
- Quaver: a pipeline that reduces TESS images into light curves (brightness versus time).
- ZTF: a ground-based sky survey; difference-image photometry measures changes relative to a reference image.
- Artifacts: false signals from the instrument or data processing that can mimic real variability. · level: research-level

<details><summary>Original abstract</summary>

Optical variability of active galactic nuclei (AGNs) probes accretion onto black holes. We study the optical variability of AGNs in the mass range of intermediate-mass black holes (IMBHs, $10^{2-6}\,M_\odot$), whose expected variability damping timescales are of order days. We use the high-cadence photometry of the Transiting Exoplanet Survey Satellite (TESS) to search for optical variability within its individual 28-day sectors. By applying the Quaver light-curve reduction pipeline and designing artifact-aware variability metrics, we identify 3 sources with high-confidence variability and 17 sources with medium-confidence variability. Fitting damped random walk (DRW) models reveals a tentative timescale-mass correlation in a small, metric-selected subset, but not in the full sample. ZTF difference-image aperture photometry reveals long-term fractional variability of 1.8-7.4% in the high-confidence sources, while most medium-confidence sources have variability below 1%. This study demonstrates that the dense cadence and repeated full-sky observations of TESS are valuable for detecting IMBH optical variability, while also being limited by its instrumental artifacts and relatively shallow field.

</details>

## Exoplanets and planetary science

### [Searching for substellar companion candidates with Gaia IV. New planetary-mass companions found in debris disks](https://arxiv.org/abs/2611.26774)
*A. -M. Lagrange, S. Toucheboeuf, F. Kiefer et al.* · `astro-ph.EP` · arXiv:2611.26774v1 · relevance 0.06

- **In one sentence**: Applies the GaiaPMEX tool, which combines Gaia DR3 astrometric signature and Gaia-Hipparcos proper motion anomaly, to 94 resolved debris-disk stars to find stellar or planetary-mass companions, then refines candidates with high-contrast imaging and radial velocity data.
- **In plain words**: Many dusty debris disks around young stars show gaps, rings and spirals that could be carved by unseen planets, but those planets are rarely seen directly. This paper uses a method based on how a star's position and motion wobble in Gaia satellite measurements to search 94 such stars for hidden companions. The authors report companions around five stars, including a possible 2-6 Jupiter-mass planet orbiting HD 107146 at 2-10 au, and tentative planetary-mass companions around TWA 7 and HD 120326.
- **Why it matters**: It opens a way to find planets at separations and masses that direct imaging often misses, which matters for explaining disk structures. The companion detections are reported as ranges and some are only tentative (2 sigma), so they should be treated as candidates pending follow-up observations.
- **Background needed**: - Debris disk: a ring or cloud of dust and rock fragments left around a young star after planet formation, often with visible gaps or rings.
- Astrometry: precise measurement of star positions and motions; a companion makes the star wobble, which shows up in the data.
- Gaia and Hipparcos: European space astrometry missions; comparing their measured motions reveals hidden companions (proper motion anomaly).
- Jupiter mass and astronomical unit (au): Jupiter mass is the reference for planet masses; 1 au is the Earth-Sun distance.
- Substellar companion: an object too small to be a star, such as a planet or brown dwarf.
- High-contrast imaging and radial velocity: direct photography that blocks starlight, and measuring a star's speed toward or away from us, both used to confirm companions.
- Sigma: a measure of statistical confidence; 2 sigma is a fairly weak signal. · level: research-level

<details><summary>Original abstract</summary>

When spatially resolved, debris disks often exhibit structures (gaps, rings, and spirals) that may indicate the presence of unseen planetary-mass companions. However, such planets have not been detected in most cases. Gaia opens a new mass-separation parameter space for detecting unseen planets. A tool named GaiaPMEX has been developed to detect and characterize companions to stars. It is based on two binarity indicators derived from DR3: the Gaia astrometric signature and, when the sources were also observed by Hipparcos, the Gaia-Hipparcos proper motion anomaly. We used GaiaPMEX on 94 stars hosting resolved debris disks to search for companions. When companions were identified, we combined GaiaPMEX results with high-contrast imaging and radial velocity data to further constrain their mass and orbital properties. We found stellar or substellar companions around five targets (HD 54341, HD 146897, HD 206893, HD 107146, and HD 106906) and indications (2 sigma) for companions around three additional targets (BD+45 598, TWA 7, and HD 120326). The companion to the 150 Myr star HD 107146, which harbors a ring-like dust disk, is found to be a 2-6 Jupiter-mass planet orbiting between 2-10 au. A massive 3-20 Jupiter-mass companion is found 3-10 au from the close binary HD 106906, which already hosts a remote planet orbiting at more than 700 au, and an edge-on disk. The tentative companions to TWA 7 and HD 120326 are planetary-mass companions at 1-3 au. Both stars host a multiple-ring system. We finally provide meaningful upper limits on the possible presence of companions in the range of 0-100 au around a few emblematic stars (49 Cet, AU Mic, beta Pic, and epsilon Eri) and stars hosting well-defined ring-like structures.

</details>

### [PLATON 7: An ultra-fast exoplanet atmospheric retrieval code](https://arxiv.org/abs/2611.26680)
*Michael Zhang, Tyler Fairnington, Yayaati Chachan et al.* · `astro-ph.IM` · arXiv:2611.26680v1 · relevance 0.05

- **In one sentence**: PLATON 7 is a rewrite of an open-source Python atmospheric retrieval code for exoplanet transmission spectra, using JAX and single precision to run about 60 times faster, plus new features such as two-limb retrievals, patchy clouds, and additional OCS and CS2 opacities.
- **In plain words**: This paper describes a new version of PLATON, a free software tool that works backward from starlight filtered through a distant planet's atmosphere to estimate what gases and clouds that atmosphere contains. The authors rewrote the code and report it now runs about 60 times faster, computing a near-infrared spectrum in about 0.35 milliseconds on a single high-end graphics card, with little loss of accuracy according to the text. They also added features such as modeling patchy clouds and two different sides (limbs) of a planet.
- **Why it matters**: Retrieval fits many models to observed spectra, so a faster code can make large analyses practical; the text gives the speed figures but does not show detailed accuracy tests here, so the real-world gain is worth checking against the full paper. The paper also states the rewrite was done using "Claude Fable 5," an AI tool, which is a notable detail about how the code was produced.
- **Background needed**: - Exoplanet transmission spectrum: the pattern of starlight whose colors are slightly absorbed as a planet passes in front of its star, revealing which gases are present.
- Atmospheric retrieval: a statistical method that adjusts model parameters (gas amounts, temperature, clouds) until the model matches observations.
- Opacity: how strongly a gas absorbs light at each wavelength; OCS (carbonyl sulfide) and CS2 (carbon disulfide) are sulfur-bearing molecules.
- Single vs. double precision: how many digits a computer stores for each number; fewer digits run faster.
- JAX: a Python library for fast numerical computing on GPUs.
- Patchy clouds: clouds that cover only part of the planet's limb rather than uniformly. · level: research-level

<details><summary>Original abstract</summary>

PLATON is an open source Python package for atmospheric retrieval, first released in 2018. We introduce PLATON 7, a complete rewrite of PLATON using Claude Fable 5. The biggest changes are that PLATON now uses JAX for all intensive calculations, and these calculations are now performed in single precision instead of double precision. These two changes speed up the code by a factor of ~60 with negligible decrease in accuracy, allowing it to compute a 0.8--5.3 um transmission spectrum at R=20k in 0.35 ms on a RTX 5090. We also introduce several new features, including support for two-limb retrievals, patchy clouds, and more opacities (particularly OCS and CS2). PLATON is available on GitHub at https://github.com/ideasrule/platon.

</details>

## High-energy astrophysics

### [Probing for relativistic outflows in the Ultraluminous X-ray pulsar RX J0209.6-7427](https://arxiv.org/abs/2611.27693)
*F. Barra, C. Pinto, T. di Salvo et al.* · `astro-ph.HE` · arXiv:2611.27693v1 · relevance 0.12

- **In one sentence**: An XMM-Newton study of the Be-star-fed, 9.3-second-spin ultraluminous X-ray pulsar RX J0209.6-7427 uses very deep RGS spectra to test for relativistic outflows during its 2019 super-Eddington outburst.
- **In plain words**: The paper looks at a bright X-ray source in a neighbouring galaxy, a neutron star (a very dense collapsed star) that pulls gas from a companion star and spins about once every 9 seconds. It was studied during a 2019 outburst that briefly reached about 10^39 erg/s, roughly a million times the Sun's total power output. The authors find that the X-ray spectrum can be explained either by fast-moving gas flowing outward at about 10% and possibly 20% of light speed, or by a different gas model that fits about as well, so fast outflows are plausible but not the only explanation.
- **Why it matters**: Winds from ULXs are thought to matter for how such systems feed energy and material back into their surroundings, but they are hard to detect at large distances. This source is relatively close and well observed, so it offers a cleaner test; the result remains ambiguous, so it should be read as a candidate rather than a confirmed detection.
- **Background needed**: - ULX (ultraluminous X-ray source): an X-ray point source far brighter than typical stellar X-ray sources; many appear to be neutron stars or black holes feeding at very high rates.
- Neutron star: a collapsed star about the mass of the Sun packed into a city-sized ball; a "pulsar" is one that spins and sweeps beams of radiation past us.
- Be-XRB: a binary where a neutron star orbits a rapidly spinning "Be" star and pulls gas from its disc.
- Super-Eddington accretion: feeding matter faster than radiation pressure can balance gravity, which tends to drive winds.
- Outflow / absorber: gas moving away from the source that imprints narrow dips (absorption lines) in the X-ray spectrum; its speed is shown by the shift of these lines, here quoted as a fraction of light speed c.
- RGS and EPIC-pn: instruments on XMM-Newton, an X-ray space telescope; RGS resolves fine spectral lines.
- Photoionised vs collisionally ionised plasma: gas whose charge state is set by incoming radiation versus by heat; the two can produce similar-looking spectra. · level: research-level

<details><summary>Original abstract</summary>

Context. Relativistic winds have been observed in Ultraluminous X-ray sources (ULXs), but their detection at large distances remains limited. Galactic neutron stars accreting matter from Be-star companions provide a valuable opportunity to improve our understanding of these outflows. Aims. RX J0209.6-7427 is a Be-XRB, powered by a neutron star with a spin period of 9.3 seconds, that underwent an outburst in 2019, exceeding a bolometric luminosity of $10^{39}$ erg s$^{-1}$ at its peak. Owing to its relatively low distance and a high-resolution XMM-Newton observation, this source is a strong candidate for investigating outflows associated with super-Eddington accretion. Methods. The RGS spectrum yields 105,000 counts, a factor of two higher than any other deep ULX RGS spectrum. RGS and EPIC-pn data sets were modelled with a phenomenological continuum accounting for emission from the accretion disc and accretion column. The emission and absorption features were fitted with the optically-thin plasma models available in SPEX, exploring the temperature-velocity parameter space. Results. The modelling of emission features suggests the presence of a multiphase photoionised plasma approximately at rest with respect to the source. The absorption features can be reproduced either by blueshifted photoionised absorbers moving at approximately $0.1c$ and $0.2c$, the latter being more tentative, or by an alternative collisionally ionised absorption model, which provides a comparably acceptable fit. The presence of ultrafast outflows therefore remains a plausible, but non-unique, interpretation of the data. If associated with outflows, the inferred column densities appear lower than those reported for some persistent ULXs, potentially reflecting differences in the accretion-flow properties or the shorter super-Eddington phase of RX J0209.6-7427.

</details>

### [Disrupted stars and captured compact objects: Combining observations from multiple messengers to infer the population of massive black holes](https://arxiv.org/abs/2611.27742)
*Shashwat Singh, Luca Broggi, Christopher P. L. Berry et al.* · `astro-ph.HE` · arXiv:2611.27742v1 · relevance 0.11

- **In one sentence**: A joint hierarchical inference framework that combines predicted LISA extreme mass-ratio inspiral (EMRI) gravitational-wave detections with ZTF and LSST tidal disruption event (TDE) catalogues, built on two-dimensional Fokker-Planck simulations, to constrain the formation and occupation of massive black holes.
- **In plain words**: Massive black holes sit at the centres of galaxies, but how they formed and grew is still unclear. This paper looks at two kinds of events linked to them: stars torn apart when they pass too close (TDEs, seen with telescopes) and small compact objects spiralling into them (EMRIs, which would be seen as gravitational waves by the future LISA detector). The authors show how combining the two kinds of data can constrain the black hole population, even though few events will be seen by both instruments at once.
- **Why it matters**: The approach offers a way to learn about black hole populations that neither telescopes nor gravitational-wave detectors can reach alone, such as spin and orbital eccentricity from EMRIs. The results are model-based predictions from simulations rather than measurements, so the forecasts depend on the assumptions made and should be read as projections for future surveys.
- **Background needed**: - Massive black hole (MBH): a black hole with millions to billions of solar masses, typically at a galaxy's centre.
- Tidal disruption event (TDE): a star is shredded by a black hole's gravity, producing a flash of light.
- Extreme mass-ratio inspiral (EMRI): a small compact object (such as a stellar-mass black hole) slowly spiralling into a massive black hole, emitting gravitational waves.
- LISA: a planned space-based gravitational-wave detector.
- ZTF and LSST: optical sky surveys (the Zwicky Transient Facility, and the Vera Rubin Observatory's Legacy Survey of Space and Time).
- Fokker-Planck simulation: a statistical method tracking how stars or orbits in a cluster diffuse and change over time.
- Hierarchical inference: a statistical method that fits population-level parameters while accounting for each event's detection biases.
- Credible width / dex: a 90% credible width gives the range the parameter is 90% likely to lie within; a dex is a factor of ten in log scale. · level: research-level

<details><summary>Original abstract</summary>

Massive black holes (MBHs) are found in galactic centres, but their formation and evolution remain elusive. Tidal disruption events (TDEs) and extreme mass-ratio inspirals (EMRIs) both arise from stellar dynamics in the nuclear star clusters around MBHs, and are observed with electromagnetic surveys and gravitational waves, respectively. To overcome the scarcity of coincident detections, we formulate how to combine gravitational-wave detections from LISA-EMRIs with observations from ZTF-TDEs to measure properties of the MBH population. Building on two-dimensional Fokker-Planck simulations of EMRIs and TDEs, we model how their populations are affected by the MBH-host scaling relation, the nucleation fraction and the MBH occupation fraction, and analyse the resulting catalogues using joint hierarchical inference accounting for their individual selection biases. With current ZTF-TDE detections, we can already identify combinations of MBH formation favoured by and consistent with the observed TDE population, and derive corresponding predictions for the EMRI population detectable by LISA. Across a range of astrophysical assumptions, the ratio of detectable TDEs to EMRIs is high: ZTF detecting 2.7-84.3 times as many TDEs as LISA detects EMRIs. TDEs, through their numbers, set the shared mass and redshift distributions: LSST constrains the characteristic MBH mass to a 90% credible width of 0.31 dex and the power-law index of the redshift evolution to a precision of 0.11. EMRIs make up ~3.4% of the joint catalogue, yet carry more information than the whole ZTF sample and are the only probe of MBH spin and orbital eccentricity. TDEs will constrain the abundance of low-mass MBHs before LISA flies, while EMRIs will measure properties that electromagnetic surveys cannot. EMRI and TDE observations offer complementary insights into MBH growth and evolution that neither can provide alone.

</details>

## Stars and the Sun

### [Machine learning reveals new Galactic C-rich and O-rich AGB sources](https://arxiv.org/abs/2611.26701)
*Tanya Kushwahaa, Mikako Matsuura, Jason A. S. Hunt et al.* · `astro-ph.GA` · arXiv:2611.26701v1 · relevance 0.04

- **In one sentence**: A machine-learning classification of Gaia DR3 Galactic AGB candidates into carbon-rich and oxygen-rich groups, with mass, age, spatial, vertical-profile and warp/spiral-arm analyses of the resulting samples.
- **In plain words**: This paper sorts a huge catalogue of stars in our Milky Way into two chemical types, carbon-rich and oxygen-rich, using a computer model trained on a small set of carefully checked examples. The authors identify about 304,000 oxygen-rich and about 4,200 carbon-rich aging stars, then use their colours, brightness and distances to estimate their masses and ages. They report how these groups are spread across the galaxy, how far they sit above the galactic plane, and hints of links to the galaxy's warp and spiral arms.
- **Why it matters**: Aging giant stars like these return gas and dust to space, so mapping them helps show where dust comes from and how the disc is structured and moving. The results depend on the classification being accurate and on mass and age estimates from models, and the spiral-arm link is described only as tentative, so the findings should be read as a useful map rather than settled physics.
- **Background needed**: - AGB (asymptotic giant branch) stars: old, bright, late-stage stars that have expanded and are losing material.
- Carbon-rich vs oxygen-rich: a chemical split in the outer layers of these stars that depends on their composition; it affects the dust they make.
- Gaia DR3: a European space telescope catalogue measuring positions, brightness and colours for about 140 million stars in the Milky Way.
- Machine learning / XGBoost: a method where a computer learns to classify objects from labelled examples, here using colours and spectral features.
- Colour-magnitude diagram: a plot of star brightness against colour, used to infer stellar type and evolutionary stage.
- Isochrones: model tracks showing how stars of a given age and composition look in such plots, used to estimate mass and age.
- Scale height: how far stars spread vertically above and below the galactic plane.
- Galactic warp and spiral arms: large-scale bending of the galaxy's disc and its arm-shaped density patterns. · level: research-level

<details><summary>Original abstract</summary>

Identification of carbon-rich (C-rich) and oxygen-rich (O-rich) Asymptotic Giant Branch (AGB) stars is crucial to understanding the structure and dust sources of the Milky Way. We present a machine-learning (ML) classification of Galactic AGB candidates using Gaia DR3, identifying 304,090 O-rich and 4,227 C-rich sources. Our two-step approach, which involves similarity-based selection, followed by XGBoost classification that combines colour and spectroscopic features, demonstrates that a small, but high-quality training sample is sufficient for accurate identification even in massive datasets such as ~140 million sources from Gaia DR3. The ML-identified stars occupy distinct regions in colour-magnitude and Gaia-2MASS diagrams, and comparison with stellar isochrones combined with Gaia distances allows estimates of their masses and ages. Spatial distributions show that O-rich AGB stars dominate the inner Galaxy, while C-rich AGB stars are concentrated toward the anti-Galactic centre. Vertical profiles indicate that massive O-rich (5-8 M$_\odot$) stars remain near the Galactic mid-plane, whereas C-rich (2.3-2.5 M$_\odot$) and low-mass O-rich (1-1.5 M$_\odot$) AGB stars are more vertically extended, with scale heights that increase with decreasing stellar mass and increasing stellar ages. C-rich AGB stars trace the Galactic warp at intermediate ages (1 Gyr), with warp amplitudes appearing larger than those traced by Cepheids. Intermediate-mass O-rich AGB stars (~300 Myr) show tentative correspondence with several spiral arm features, while the C-rich distribution is too smooth for reliable identification with the current sample. These results highlight AGB stars as powerful probes of stellar evolution and Galactic dynamical processes.

</details>

### [Recovering buoyancy-glitch parameters in low-luminosity red giants from global stellar properties with machine learning](https://arxiv.org/abs/2611.27954)
*Jiang Chen* · `astro-ph.SR` · arXiv:2611.27954v1 · relevance 0.04

- **In one sentence**: Machine-learning regressors (XGBoost and LightGBM) trained on 12,580 synthetic low-luminosity red-giant models test whether buoyancy-glitch amplitude, location and width can be predicted from global stellar properties, with location and width recovered well and amplitude only moderately.
- **In plain words**: Red giants are aging stars whose pulsations carry clues about their deep interiors, but extracting those clues usually requires detailed, case-by-case modelling. This paper asks whether a sharp feature inside these stars, a "buoyancy glitch" near the boundary of the outer convective layer, can be estimated from simpler overall properties such as brightness, temperature and pulsation frequency. The authors trained computer models on a large set of simulated stars and found that the position and width of the feature were predicted very well, while its strength was predicted only moderately.
- **Why it matters**: If global measurements can give a usable first estimate of these interior features, large surveys such as Kepler and the upcoming PLATO mission could prioritise which stars need costly detailed analysis. The result is limited to a synthetic grid, so it shows what is possible for these simulations rather than for real stars.
- **Background needed**: - Red giants: evolved stars that have exhausted core hydrogen and expanded; their brightness and pulsations change as they age.
- Asteroseismology: studying stars through their oscillations, much as seismologists study earthquakes to infer Earth's interior.
- Buoyancy glitch: a localized sharp change in the star's internal structure (a rapid change in how quickly gas is buoyancy-driven) near the base of the convective envelope.
- Global properties here include the frequency of peak oscillation power (nu_max), surface temperature (T_eff), and large frequency separation (Delta nu).
- Gradient-boosted trees: a machine-learning method that builds many simple decision rules in sequence to predict a number.
- R^2: a score from 0 to 1 for how well predictions match the true values on unseen data.
- SHAP: a method for showing which input variables most influence a model's predictions.
- Synthetic grid: a set of computer-generated stellar models rather than observed stars. · level: research-level

<details><summary>Original abstract</summary>

Buoyancy glitches in red giants provide localized information on the interior structure near the base of the convective envelope, but their properties are typically inferred from dedicated seismic modelling rather than global properties, limiting large-sample applications. We investigate whether the buoyancy-glitch amplitude ($A_g$), location ($W_{\rm g}^{\star}$), and width ($D_g$) can be recovered from global stellar properties using gradient-boosted tree regressors (XGBoost and LightGBM). The models were trained on a grid of 12580 synthetic stellar models of low-luminosity red giants, with target parameters derived from fits to the local buoyancy frequency profile. We find that $W_{\rm g}^{\star}$ and $D_g$ exhibit excellent recoverability, achieving test-set $\mathcal{R}^2$ values of 0.98 and 0.97, respectively. In contrast, $A_g$ shows moderate recoverability overall ($\mathcal{R}^2=0.68$). This reduced recoverability of $A_g$ is concentrated in the large frequency separation range $\Delta\nu = 4.6$--$18.9\,\mu$Hz, where the glitch resides in the evanescent-zone transition between the convective envelope and the gravity-mode cavity, increasing intrinsic scatter. SHAP analysis shows that $\nu_{\rm max}$ and $T_{\rm eff}$ dominate the predictions across all targets, indicating that the regressors rely primarily on evolutionary state. While $W_{\rm g}^{\star}$ and $D_g$ are tightly constrained by global evolutionary trends, the lower recoverability of $A_g$ reflects localized structural complexity associated with red-giant evolution. Overall, for the synthetic grid adopted here, these results indicate that global properties provide a direct estimate of the buoyancy-glitch parameters and a way to prioritise dedicated mixed-mode inversions for large asteroseismic samples such as Kepler and PLATO.

</details>

## Chemical physics

### [Tensor cluster expansion as an efficient surrogate for multi-ACE](https://arxiv.org/abs/2610.41969)
*Jacob Jeffries, Enrique Martinez, Eva Zarkadoula* · `cond-mat.mtrl-sci` · arXiv:2610.41969v2 · relevance 0.04

- **In one sentence**: The paper generalizes an on-lattice tensor cluster expansion (TCE) to arbitrary correlation order, shows its features span a subspace of MACE features, and uses maximum-entropy subset sampling so cheaper TCE features can pre-screen chemically diverse configurations for fine-tuning a MACE potential on alloyed transition metal dichalcogenide monolayers.
- **In plain words**: Researchers want computer models that predict how mixed-element thin materials behave at room and higher temperatures, but the accurate machine-learned models are expensive to train. This work uses a cheaper, simpler description of atomic arrangements to pick out a small, varied set of example configurations, and then trains the expensive model only on those. The authors report that this selection recovers the chemical variety found in the full description and supports predictions of temperature-dependent vibrations in alloyed monolayers.
- **Why it matters**: Making fine-tuning of accurate atomic-scale models cheaper could make finite-temperature alloy studies feasible on modest hardware. The text supports this as a computational efficiency claim for one class of materials; its wider applicability beyond these TMD monolayers is not shown here.
- **Background needed**: - Alloy: a mixture of two or more elements arranged on a crystal lattice.
- Transition metal dichalcogenide (TMD) monolayer: a single atomic layer of a metal bonded to sulfur, selenium or tellurium, used as a thin semiconductor.
- Cluster expansion: a way to describe a configuration by summing contributions from groups of nearby atoms (pairs, triplets, and so on).
- Correlation order: how many atoms are grouped together in each term of that sum.
- Machine-learned interatomic potential (MACE, ACE): a learned model that estimates the energy and forces between atoms, far cheaper than quantum calculations but costly to train.
- Fine-tuning: adjusting a pretrained model using new data.
- Maximum-entropy subset sampling: a way to choose a small subset of examples that covers the variety in the full set.
- Finite-temperature thermodynamics and vibrational properties: how a material's energy and atomic vibrations change with heat. · level: research-level

<details><summary>Original abstract</summary>

In this work, we generalize an on-lattice tensor cluster expansion (TCE) framework to an arbitrary correlation order. We show that these generalized tensor cluster expansion features span a subspace of MACE features, suggesting that TCE features can sufficiently pre-screen MACE features for chemical diversity in alloyed transition metal dichalcogenide (TMD) monolayers. We show that, using maximum-entropy subset sampling, we can empirically recover chemical diversity from MACE features using a cheaper TCE representation. We then fine-tune a multi-ACE (MACE) potential with both subsets, and use this potential to predict temperature-dependent vibrational properties in alloyed TMD monolayers with varying chemical ordering. In our approach, TCE features can be used as cheap surrogate features for pre-screening chemically rich configurations using MACE features, allowing for the more efficient finetuning of atomic cluster expansion (ACE) potentials, thus achieving a tractable prediction of finite-temperature alloy thermodynamics on modest hardware.

</details>

### [Power Law Transients in Perovskite Photoluminescence](https://arxiv.org/abs/2611.27163)
*Anas M. M., Pradeep R. Nair* · `cond-mat.mtrl-sci` · arXiv:2611.27163v1 · relevance 0.03

- **In one sentence**: The paper shows that transient photoluminescence decays in perovskite thin films often follow power laws in time rather than sums of exponentials, links the power-law exponents to trap-state distributions, and reports that a t^-2 decay can arise even under dominant monomolecular recombination, which existing theory ties only to bimolecular recombination.
- **In plain words**: Solar-cell materials called perovskites glow after being hit with a light pulse, and the way that glow fades over time reveals how charges are lost inside the material. The authors point out that many published fading curves follow a simple power law (a steady slope on a log-log plot) rather than the usual sum of exponential decays, and that current theory does not explain this well. They develop an analysis that connects these power-law slopes to how traps are distributed in the material.
- **Why it matters**: Decay curves are routinely used to judge how efficient perovskite devices can become, so misreading their shape could mislead material design. The text suggests the work also marks the limits of the "differential lifetime" concept, but its broader impact beyond this model system is not established in the text.
- **Background needed**: - Photoluminescence (PL): light a material emits after being excited by a short pulse; its fading over time tracks charge carriers (electrons and holes) being lost.
- Transient PL: measuring that fading curve over time.
- Exponential decay: fading at a rate proportional to what remains, giving a single characteristic lifetime; multi-exponentials are sums of several such terms.
- Power law: intensity proportional to time raised to a fixed exponent (e.g., t^-2), which has no single characteristic lifetime and appears as a straight line on log-log axes.
- Recombination: electrons and holes annihilating each other. Monomolecular means one carrier type decays alone (often at defects or traps); bimolecular means an electron and hole meet and recombine.
- Trap states: defect sites in the crystal that capture carriers and hold them, delaying or altering recombination.
- Differential lifetime: an effective, time-dependent lifetime derived from the decay curve. · level: research-level

<details><summary>Original abstract</summary>

Carrier dynamics and recombination in perovskite thin films are often explored through transient photoluminescence (PL) measurements and subsequent analysis based on single/multi-exponentials. In contrast, here we show that several experimental PL transients reported in literature vary as power laws with time and are not multi-exponentials. Puzzlingly, the existing theoretical methods are ill-equipped to explain the origin and implications of such power law trends. Our analysis resolves this puzzle and correlates the power law exponents with the trap distributions. Curiously, we show that PL transients could vary as $t^{-2}$ even in the presence of dominant monomolecular recombination while the existing theory associates this unique trend exclusively with dominant bimolecular recombination. These findings identify the limits of applicability of concepts such as differential lifetime and highlight the need for predictive modeling synergistic with insightful data analysis towards performance optimization of perovskite optoelectronic devices.

</details>

## Materials science

### [Group-III doping of the p-type oxide SnO](https://arxiv.org/abs/2611.27938)
*Nicola Gutmann, Georg Hoffmann, Aidan Flynn Campbell et al.* · `cond-mat.mtrl-sci` · arXiv:2611.27938v1 · relevance 0.08

- **In one sentence**: Molecular-beam-epitaxy growth of Al-, Ga- and In-doped p-type SnO films, reporting Hall-measured hole concentrations, doping efficiencies, and an unexpected acceptor behavior for Al that contradicts a prior calculation.
- **In plain words**: Tin monoxide is a transparent oxide that conducts electricity by carrying positive charges ("holes"), and making it conduct well depends on adding small amounts of other elements. This paper grew thin films of tin monoxide with aluminium, gallium, or indium added, and measured how many holes each dopant produced. The hole counts stayed low, peaking around 10^19 to 3×10^19 per cubic centimetre, and aluminium behaved unexpectedly as a hole-making dopant, which the authors could not fully explain even after growing films in an oxidizing atmosphere.
- **Why it matters**: Good p-type oxides are scarce, so a clear picture of why SnO stops at modest hole densities matters for transparent electronics. The text suggests the limit may reflect basic defect chemistry in SnO, but the authors leave the explanation open, so this is a measured finding rather than a settled answer.
- **Background needed**: - SnO (tin monoxide) is a transparent oxide semiconductor studied as a p-type (hole-conducting) material.
- Dopants are small amounts of foreign atoms added to change conductivity; group-III elements (Al, Ga, In) are typically expected to act as acceptors in SnO, meaning they add holes.
- Hall measurements determine the sign and density of charge carriers in a film.
- Doping efficiency is the fraction of added dopant atoms that actually produce a carrier.
- Molecular beam epitaxy is a method of growing thin films one atomic layer at a time under vacuum.
- Oxidation state (e.g., Al1+ vs Al3+) describes how many electrons an atom has given up; the authors suspect a different charge state of Al explains its behavior.
- The text gives only the abstract-level summary; full methods, error bars, and defect calculations are not included here. · level: research-level

<details><summary>Original abstract</summary>

Al-, Ga-, and In-doped tin monoxide (SnO) films were grown by molecular beam epitaxy. Hall measurements reveal acceptor character of all investigated group-III dopants in SnO, which correspond to theoretical calculations and previous experiments for Ga and In, but contradicts theoretical calculations predicting donor character for Al in SnO. Doping concentrations of 10e18-1e22 cm-3 were tested and maximum hole concentrations of 2e19, 3e19, and 1e19 cm-3 with doping efficiencies of 3 percent, 9 percent, and 1 percent were found for Al, Ga, and In, respectively. The observed doping limit in the mid e19 cm-3 aligns with the limits observed in literature for different dopants, hinting to fundamental aspects of the SnO defect chemistry. Due to the unexpected Al acceptor behavior, we hypothesized Al1+ being present instead of Al3+. To stabilize the higher Al3+ oxidation state, another sample series of Al-doped SnO was grown in an oxidizing atmosphere. Despite the oxidizing atmosphere, these samples showed p-type character. A more complex defect chemistry is thus expected to explain the Al acceptor character.

</details>

### [Frustration-Stabilized Hexamerons and Their Topological Magnons in Janus MXene](https://arxiv.org/abs/2611.27384)
*C. B. Subba, Z. Pachuau, Samy Brahimi et al.* · `cond-mat.mtrl-sci` · arXiv:2611.27384v1 · relevance 0.08

- **In one sentence**: First-principles and atomistic spin simulations of the Janus MXene MnHf2C2FI predict a frustrated 120-degree Néel ground state with a metastable hexameron (six merons and antimerons) whose in-gap magnons carry Chern numbers and a sign-dependent thermal Hall response.
- **In plain words**: This paper studies a two-dimensional material in which the magnetic moments of manganese atoms are arranged in a triangular pattern that cannot all point in opposing directions at once, so they settle into a tilted, frustrated arrangement. The authors used computer calculations to find a metastable cluster of swirling spin patterns, called a hexameron, sitting on top of that arrangement. They report that this cluster traps specific wave-like spin excitations (magnons) and that, in an ordered array, these waves could carry heat sideways in a direction set by the cluster's handedness.
- **Background needed**: - MXenes: a family of thin, layered two-dimensional materials built from metal, carbon or nitrogen layers.
- Janus material: a layered material whose two outer faces differ chemically, so it lacks inversion symmetry (a mirror-like flip changes it).
- Magnetic frustration: when neighbouring magnetic moments cannot all satisfy their preferred antialignment on a triangular lattice, forcing a compromise arrangement such as 120-degree order.
- Dzyaloshinskii-Moriya interaction: a spin-orbit-driven coupling that twists neighbouring spins and favours swirling textures.
- Merons and antimerons: half-units of a swirling spin texture, carrying topological charge of plus or minus one half; a hexameron is a six-unit bound cluster with zero net charge.
- Magnons: quantized waves of spin disturbance in a magnet, analogous to phonons for lattice vibrations.
- Chern number and Berry curvature: topological quantities describing how wave bands twist; they control edge-directed heat flow (thermal Hall effect).
- Metastable: a state that is a local, not global, energy minimum and could persist but is not the lowest-energy state. · level: research-level

<details><summary>Original abstract</summary>

Frustrated magnets on triangular lattices favour noncollinear order, and when inversion symmetry is broken they can host localized topological textures on top of that order. Here we show that the Janus MXene MnHf2C2FI is such a system. Combining first-principles calculations with atomistic spin simulations, we find that magnetism is confined to the Mn layer, where a strong antiferromagnetic nearest-neighbor exchange together with a sizable Dzyaloshinskii-Moriya interaction stabilizes a frustrated 120 Neel ground state. On top of this ground state we identify a metastable hexameron: a composite of six merons and antimerons, one vortex-antivortex pair on each of the three sublattices, whose sublattice-resolved topological charges compensate. Linear spin-wave theory confirms that the hexameron is a local energy minimum, and its noncoplanar cores act as potential wells that bind discrete in-gap magnon modes below the bulk continuum. In a periodic hexameron array the magnon bands carry nonzero Chern numbers, and the resulting Berry curvature produces a magnon thermal Hall response whose sign depends on which of the two time-reversal partners of the hexameron is realized. Our results establish Janus MXenes as a two-dimensional platform in which frustration, broken inversion symmetry, and spin-orbit coupling combine to produce metastable antiferromagnetic solitons with distinct spectroscopic and transport fingerprints.

</details>

## Soft matter and polymers

### [Minkowski Correlation Functions (MCF): Long-range, robust shape descriptors for point patterns](https://arxiv.org/abs/2611.27948)
*Dominik Pabst, Michael A. Klatt, Klaus Mecke* · `cond-mat.dis-nn` · arXiv:2611.27948v1 · relevance 0.05

- **In one sentence**: The paper introduces ring-based Minkowski correlation functions, which describe disordered planar point patterns by placing a spherical shell around each point and tracking the Minkowski functionals (covered area, boundary length, Euler characteristic) of the resulting two-phase morphology as a function of the outer ring radius.
- **In plain words**: Researchers wanted a better way to describe how scattered dots are arranged, such as particles, trees, or galaxies. They put a ring around each dot, measured the shape of the combined covered region as the ring grows, and used this to build a summary of the pattern. The text reports that the method is exact, fast, and tolerant of noise, and that it shows consistent differences from purely random arrangements in three test systems.
- **Why it matters**: Standard shape measures of point patterns stop being informative at larger distances, while standard correlation functions are not additive, which limits how they combine. The ring-based approach is presented as covering longer length scales while keeping useful shape information, but the text alone does not show how it compares with other established methods in practice.
- **Background needed**: - Point pattern: a set of locations (e.g., particle centres, tree positions, galaxies) in a plane.
- Homogeneous Poisson reference: a completely random arrangement with no clustering or regularity, used as a baseline.
- Minkowski functionals: three shape numbers for a region, namely its area, its boundary length, and its Euler characteristic (a count of connected pieces minus holes).
- Correlation function: a statistic describing how likely points are to sit at a given distance from each other.
- Structure factor: a related description of spatial arrangement, often used in soft matter and scattering.
- Additive descriptor: a measure whose value for a union of regions can be obtained by adding values of the parts.
- Quincke rollers: self-propelled microscopic particles driven by an electric field, used as model active matter. · level: research-level

<details><summary>Original abstract</summary>

A morphometric analysis of point patterns using Minkowski functionals is short-sighted, whereas correlation functions do not provide robust, i.e., additive shape descriptors. To combine the advantages of both standard techniques and to overcome their weaknesses, we introduce ring-based Minkowski correlation functions (MCFs) as robust and sensitive descriptors of disordered point patterns. By assigning to each point a spherical shell and quantifying the resulting two-phase morphology via Minkowski functionals, MCFs capture structural information across multiple length scales, remain sensitive at radii where conventional disk-based Minkowski functionals have saturated, and implicitly encode higher-order correlations beyond the pair correlation and structure factor. We present an exact and efficient algorithm for planar patterns extending the established disk-based morphological approach to long ranges. Applications across scales -- active colloids (Quincke rollers), longleaf pine trees, and the Hubble Ultra Deep Field -- demonstrate clear and systematic deviations from homogeneous Poisson references, with distinct responses of covered area, boundary length, and Euler characteristic. The approach combines short computation times, robustness to noise, and straightforward edge handling with clear interpretability as low-dimensional functions of the outer ring radius.

</details>

### [Corrections to the Fick-Jacobs Description of Diffusion across Pickering Droplet Interfaces](https://arxiv.org/abs/2611.27818)
*Rohit Khandoori, Wim Thielemans, Joost de Graaf* · `cond-mat.soft` · arXiv:2611.27818v1 · relevance 0.05

- **In one sentence**: The paper compares the standard Fick-Jacobs approximation for diffusion through varying cross-sections against fully resolved 2D simulations of Pickering droplets, and finds the approximation's errors grow with interfacial particle crowding and can be fixed with a simple geometric correction.
- **In plain words**: Some liquid droplets are coated with tiny solid particles that form a porous skin, and molecules move through that skin at rates that matter for encapsulation. This paper checks a common shortcut used to predict how fast molecules pass through such narrowing and widening passages, against detailed computer simulations of 2D droplets. The shortcut becomes less accurate as the particles pack more densely, and the authors say the needed correction can be understood from simple geometry.
- **Why it matters**: Predicting transport through particle-coated interfaces matters for designing encapsulation and controlled-release materials such as bijels. The geometric correction may also inform diffusion in other complex geometries, though the text is limited to 2D droplets and does not show how far it extends.
- **Background needed**: - Pickering droplets: emulsion droplets stabilized by solid particles sitting at the liquid-liquid interface rather than by surfactant molecules.
- Bijels: bicontinuous interfacially jammed emulsion gels, where two interpenetrating liquids are held apart by a jammed layer of particles.
- Diffusion: random molecular motion that carries substances from high to low concentration.
- Fick-Jacobs formalism: a reduced one-dimensional description of diffusion through a channel whose width changes slowly along its length; it assumes the molecules quickly equilibrate across the channel width.
- Higher-order geometric derivatives: mathematical measures of how sharply the channel width changes; corrections built from them are the usual way to extend the approximation.
- Fully resolved simulation: a computer model that tracks the geometry in full detail rather than averaging it away. · level: research-level

<details><summary>Original abstract</summary>

Particle-laden interfaces give rise to important classes of multiphase materials, including Pickering-Ramsden systems and bicontinuous interfacially jammed emulsion gels (bijels). In these systems, colloidal particles adsorb at fluid-fluid interfaces and form semipermeable layers that provide structural stability and controlled diffusive transport. These properties make them attractive for encapsulation applications and motivate understanding transport across particle-laden interfaces. Diffusion through geometries with varying cross-section, including those found at particle-laden interfaces, is commonly described using the Fick-Jacobs formalism. However, this approach relies on the assumptions of slowly varying geometries and rapid equilibration in the transverse direction. Subsequent studies have developed corrections based on higher-order geometric derivatives, but an elegant closed-form description remains elusive. Here, we compare predictions of the Fick-Jacobs model with fully resolved simulations of 2D Pickering droplets. We find that discrepancies in model predictions increase with interfacial particle crowding, revealing the limits of the Fick-Jacobs approximation. We show that the required correction can be understood through simple geometrical arguments. Our results provide an effective framework for describing transport across particle-laden interfaces and lay the foundation for a more general description of diffusion in complex geometries.

</details>

## AI for chemistry and materials

### [E2Former-V3: Atom-Role-Aware Equivariant Interatomic Potentials](https://arxiv.org/abs/2611.27111)
*Frank Peng, Lin Huang, Arthur Jiang et al.* · `physics.chem-ph` · arXiv:2611.27111v1 · relevance 0.15

- **In one sentence**: E2Former-V3 assigns each atom a fixed chemical role before the network runs, so hydrogens and water oxygens get narrower latent features and fewer update blocks, trading some force accuracy for speed in conservative machine-learned interatomic potentials for all-atom simulations.
- **In plain words**: Simulating molecules in water, such as a protein in a salt solution, requires a computer model of how atoms push and pull on each other, and these models are slow when most atoms are light hydrogens and water. This paper proposes giving each atom a fixed role up front and spending less computing effort on the less demanding roles, without dropping any atoms. The authors report a small accuracy gain on one standard test over their previous version and a speedup of about 1.75 to 1.84 times, with a faster variant reaching up to about 5.85 times while losing some force accuracy.
- **Why it matters**: Faster yet still physically consistent models of solvated biomolecules and electrolytes would make longer and larger simulations practical, which matters for drug and materials work. The text reports clear trade-offs, though: energy error is higher than the previous model, the method is worse on biomolecules and metals, and water density is about 7.5% too high, so its practical value depends on the system being studied.
- **Background needed**: - Interatomic potential: a learned function giving the energy of a set of atoms from their positions; forces are its gradient.
- Density-functional theory (DFT): a standard quantum-mechanical calculation that the learned model tries to match.
- Equivariant network: a neural network whose outputs rotate correctly with the molecule, so physical quantities stay consistent.
- Latent width / channels: the number of numbers used to describe each atom inside the network; more means more capacity and cost.
- Conservative force: force computed as the gradient of one energy, so energy is conserved in simulations.
- Force MAE (meV/Å): average size of error in the predicted forces; lower is better.
- OMol25: a large public dataset of molecular quantum calculations used for training and testing.
- MD, NVE, NVT: molecular dynamics runs; NVE keeps energy fixed, NVT keeps temperature fixed.
- RDF (radial distribution function): a measure of how atoms are spaced around each other, compared with experiment. · level: research-level
- Matched keywords: protein

<details><summary>Original abstract</summary>

Machine-learned interatomic potentials approach density-functional accuracy, but explicit-solvent atom counts are dominated by hydrogens and water. Uniform equivariant architectures still give every atom the same latent width and number of expensive block updates. To our knowledge, no prior method reallocates capacity by chemical role while retaining every atom and its first-principles force. We introduce E2Former-V3, which treats capacity as an atom-level resource: a static chemical role, assigned before the backbone runs, sets each atom's latent width and update count. No atom is removed, no coordinate is integrated out, and every force remains the gradient of one conservative energy. Standard reduces only the update count, sending hydrogen through half as many full-width block updates; on OMol25 validation it reaches a force mean absolute error (MAE) of 8.146 meV/Angstrom, against E2Former-V2's published 8.38, at 1.75-1.84x V2's throughput with lower peak memory on one H200. Flash also narrows the low-resolution stream to one eighth of the high-resolution width (32 vs 256 channels) and routes water oxygen with hydrogen, reaching 4.00-4.88x on three solvated systems (up to 5.85x in the pure-water all-low-resolution limit) at 11.272 meV/Angstrom, trading force accuracy for speed. Across 54 20 ps MD legs, a 100 ps NVE check, and a 1 ns NVT run on a 32,437-atom solvated protein, all runs complete; the MD legs show no non-finite values, clashes, or water fusion, and water O-O and Na-O RDF peak positions match experiment within 0.04 Angstrom. E2Former-V3 therefore moves the accuracy-throughput frontier for all-atom, conservative simulation, not a uniform accuracy win: Standard is worse on biomolecules and metals, better on electrolytes and organics; energy MAE is higher than E2Former-V2's; and water densities remain about 7.5% too high. Code: https://github.com/IQuestLab/UBio-MolFM.

</details>

### [Hierarchical Hybrid-Coordinate Flow Matching for Accurate and Physically Plausible Apo-to-Holo Protein Generation](https://arxiv.org/abs/2611.27162)
*Minjong Kim, Jaemin Sim, Dongwoo Kim et al.* · `cs.LG` · arXiv:2611.27162v1 · relevance 0.14

- **In one sentence**: CrypticFlow is a hierarchical flow-matching model that predicts holo (ligand-bound) protein conformations from apo (unbound) structures by first placing sparse C-alpha anchors in Cartesian space and then filling the gaps in internal coordinates, constraining distances to the apo reference.
- **In plain words**: Proteins change shape when a drug or other molecule binds to them, and drug designers would like a computer to predict the bound shape from the unbound one. This paper proposes a two-stage method: it first sketches the rough skeleton of the protein's backbone as widely spaced points, then fills in the details between those points using local angles and lengths. The authors report that this combination gives lower overall position error than the baselines they compared against, and that the local geometry looks more physically sensible.
- **Background needed**: - Apo vs. holo: a protein's unbound (apo) shape versus its bound (holo) shape.
- C-alpha (C-alpha) trace: the backbone skeleton of a protein, one point per amino acid.
- RMSD (root-mean-square deviation): average distance between predicted and reference atom positions, in angstroms; lower is better.
- Cartesian vs. internal coordinates: describing positions as x, y, z versus as bond lengths and angles between neighbouring atoms.
- Flow matching: a generative AI method that learns to transform random noise into realistic samples.
- Equivariant graph network: a neural network whose outputs rotate and move consistently with its inputs in 3D space.
- ESM-3: a large protein language model used here to supply sequence information.
- MolProbity: a standard tool that scores the physical and geometric quality of an all-atom protein structure.
- Lever-arm effect: errors in angles accumulate and grow along a chain when building structures step by step. · level: research-level
- Matched keywords: protein

<details><summary>Original abstract</summary>

Predicting holo-like protein conformations from apo structures is essential in structure-based drug design. Most existing apo-to-holo models operate in Cartesian space and achieve strong global accuracy. However, high global accuracy does not ensure physically valid local backbone geometry. Internal-coordinate models offer local control and validity, but regressive generation can amplify angular errors, known as the lever-arm effect. We introduce CrypticFlow, a hierarchical flow-matching model that combines these two complementary representations. An ESM-3-conditioned E(3)-equivariant graph network first generates sparse C$\alpha$ anchors in Cartesian space. A conditional midpoint Transformer then recursively fills the gaps in local internal coordinates. During recursive generation, the decoder constrains the distance between each midpoint and any sequence-adjacent parent anchor to the corresponding apo C$\alpha$-C$\alpha$ distance. On the D3PM test split, CrypticFlow achieves the lowest median and mean C$\alpha$ RMSD at published baseline capacities. Across five independent training models, the median and mean direct RMSD are 1.333 $\pm$ 0.056 angstroms and 2.766 $\pm$ 0.041 angstroms, respectively. The quality of local geometry also improves substantially. Our model achieves 99.58 $\pm$ 0.02% adjacent-distance fidelity and 95.87 $\pm$ 0.25% pseudo-angle fidelity, measured within 0.2 angstroms and 20{\deg} of the holo reference. Then, we reconstruct the predicted C$\alpha$-only traces into all-atom structures using the cg2all coarse-to-all-atom backmapping method and evaluate their physical and geometric quality with MolProbity. Our model achieves a MolProbity score of 3.034 $\pm$ 0.054, outperforming the evaluated baselines. These results show that a hierarchical flow-matching model with hybrid coordinates can recover global accuracy while retaining local fidelity.

</details>

## Biochemistry

### [Synthesis of Cellulose Nanofiber Hydrogel Beads from Typha angustifolia for the Immobilization of Protease](https://www.biorxiv.org/content/10.64898/2026.11.18.767499v1)
*Ameh, B. E.; Egwim, E. C.; Ossamulu, F. i.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.18.767499 v1 · relevance 0.07

- **In one sentence**: Cellulose nanofibers extracted from the invasive aquatic plant Typha angustifolia were oxidized, blended with PVA, and crosslinked into hydrogel beads that serve as a support for immobilizing a crude protease, which raised specific activity and broadened its thermal and pH optima.
- **In plain words**: Typha angustifolia is an invasive water plant that causes problems for wetlands and irrigation channels. This study turned its fibrous plant material into small, water-swollen beads that hold an enzyme (a protein that speeds up chemical reactions), letting the enzyme be attached to a solid support.
- **Why it matters**: Attaching enzymes to a solid carrier can make them easier to reuse and more stable in industrial processes, and this work suggests a use for an invasive plant as the carrier material. The text reports lab measurements only, so its practical value for industry is not yet shown.
- **Background needed**: - Cellulose: the structural fiber in plant cell walls; cellulose nanofibers are very thin fibers of it.
- Hydrogel: a water-swollen, soft network material; here the beads absorbed about 400% of their weight in water.
- Protease: an enzyme that breaks down proteins.
- Immobilization: fixing an enzyme onto a support so it stays in place and can be reused.
- Specific activity: enzyme activity per milligram of protein (units U/mg); higher means more active.
- Optimum temperature and pH: the conditions under which the enzyme works best.
- Half-life: how long the enzyme keeps half its activity under the stated conditions.
- Crosslinking with glutaraldehyde and oxidation with periodate: chemical steps that create reactive groups to bind the network together and attach the enzyme. · level: intermediate

<details><summary>Original abstract</summary>

Typha angustifolia, an invasive aquatic macrophyte, poses a persistent challenge to wetland and irrigation management, yet its cellulose-rich biomass represents an underexploited feedstock for value-added biomaterials. This study reports the synthesis of cellulose nanofiber (CNF) hydrogel beads from T. angustifolia and evaluates their performance as a support matrix for protease immobilization. Cellulose was isolated by chlorite delignification and alkaline treatment, oxidized with sodium periodate to introduce aldehyde functional groups, blended with polyvinyl alcohol (PVA), and crosslinked with glutaraldehyde to form hydrogel beads. The beads exhibited a high water-absorption capacity of 399.67 {plus minus} 0.53% and a mechanical strength of 1.27 MPa. Covalent immobilization of crude protease onto the beads increased specific activity nearly threefold, from 24.56 {plus minus} 0.39 U/mg for the free enzyme to 59.20 {plus minus} 1.06 U/mg for the immobilized enzyme, corresponding to a loading efficiency of 50.61%. The immobilized enzyme also displayed broadened thermal and pH optima, shifting from 40 {degree sign}C to 50 {degree sign}C and from pH 8.0 to 9.0, respectively, and an extended operational half-life from 4.40 h to 11.37 h. These findings support the valorization of invasive Typha biomass into a robust, biodegradable support system with potential application in industrial biocatalysis.

</details>

### [AlphaFold-assisted design of a modular Laminin E8 Fragment Panel](https://www.biorxiv.org/content/10.64898/2026.11.20.768189v1)
*Litzau, L. A.; Kruse, A. C.; Blacklow, S. C.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.20.768189 v1 · relevance 0.06

- **In one sentence**: Uses AlphaFold structure prediction to optimize recombinant laminin E8 fragments and builds a modular panel of interchangeable α, β, and γ chains that can be combined to make all laminin isoforms, shown to support adhesion of cells bearing cognate integrins.
- **In plain words**: Laminins are large proteins that form a web-like scaffold in the tissue around cells, but they are too big to make easily in the lab. This paper uses an AI protein-structure tool, AlphaFold, to design smaller versions of one key piece, called E8, that can be produced in cells. The authors built a set of interchangeable pieces that can be mixed to make the different laminin forms, and report that these pieces let cells stick to them through their matching surface receptors.
- **Why it matters**: Having a ready supply of laminin-like fragments could make it easier to study stem cells, organoids, and the cell-surface receptors (integrins) that grip laminin. The text does not go beyond these stated uses, so its wider impact is uncertain.
- **Background needed**: - Laminins: large, three-chain (heterotrimeric) proteins that are a main structural part of basement membranes, the thin tissue layers under cell sheets.
- Recombinant: produced in engineered cells rather than extracted from tissue.
- E8 fragment: a smaller, functional piece of laminin that still supports cell attachment and migration.
- Integrins: cell-surface receptors that bind laminin and anchor cells to the matrix.
- AlphaFold: an AI tool that predicts the 3D shape of proteins from their sequence.
- Isoform: a variant form of the protein built from a different combination of chains. · level: intermediate

<details><summary>Original abstract</summary>

Laminins are large, heterotrimeric glycoproteins that are a major structural component of basement membranes and the extracellular matrix. Although they are difficult to produce recombinantly because of their large size, a smaller fragment of the laminin heterotrimer that supports cell adhesion and cell migration, termed E8, can be recombinantly expressed. Here, we use AlphaFold to optimize laminin E8 fragments and design a panel of interchangeable laminin , {beta}, and {gamma} chains that can be combined to produce all isoforms recombinantly. These recombinant E8 fragments support adhesion of cells bearing their cognate integrins, and will be useful tools for stem-cell, organoid, and laminin-binding integrin biology research.

</details>

## Pharmacology and drug discovery

Nothing notable this time.

## Computational and systems biology

### [Koopman Analysis Reveals Collective Modes Governing Cellular Dynamics](https://www.biorxiv.org/content/10.64898/2026.11.18.767672v1)
*Dutta, S.; Yu, W.; Zheng, Z. et al.* · `biophysics` · bioRxiv doi:10.64898/2026.11.18.767672 v1 · relevance 0.10

- **In one sentence**: The paper applies Koopman operator theory to whole-cell dynamical models to identify global collective modes, including slow modes that govern cell-cycle dynamics and link to specific cell-cycle and cell-state transition processes.
- **In plain words**: The paper asks how a cell's complicated, constantly changing activity can be described more simply. The authors use a mathematical method called Koopman analysis on computer models of whole cells, which turns the tangled behavior into a small set of coordinated patterns. They report that a few slow patterns dominate the long-term cell-cycle behavior, and that these patterns line up with known steps such as cell division and DNA repair.
- **Why it matters**: It offers a global, rather than local, way to simplify nonlinear systems that are far from equilibrium, and it links that idea to physics concepts such as normal modes. Its practical value for biology is not established by this text alone; it rests on computational models, and the claims would need testing against real cell data.
- **Background needed**: - Nonlinear system: one where outputs do not scale in proportion to inputs, so behavior is hard to predict by simple addition.
- Linearization: approximating a complex system by simpler linear equations; most common versions only work near one point.
- Koopman operator: a mathematical tool that re-describes a nonlinear system's evolution in a form where it behaves linearly, across the whole state space.
- Normal modes: independent patterns of collective motion in a system, like vibration patterns in a drum or molecule.
- Slow manifold: a low-dimensional surface that a system's long-term behavior settles onto.
- Gene regulatory network: the web of genes that switch each other on and off.
- Cell cycle: the sequence of events by which a cell grows, copies its DNA, and divides, including mitosis. · level: research-level

<details><summary>Original abstract</summary>

Living systems are complex nonlinear systems that operate far from thermodynamic equilibrium, and this nonlinearity makes their dynamics difficult to analyze. Several linearization techniques have been developed to address this problem, but most are local. Koopman operator theory is a powerful alternative that linearizes a system globally. Here we show that it not only achieves global linearization but also reveals collective modes that govern the dynamics of complex, out-of-equilibrium nonlinear systems. Applying the approach to whole-cell dynamical models, we find that these collective modes have physical and biological significance and relate to distinct processes in the cell cycle and in cell-state transitions. Collective and normal modes are widespread in many-body systems, particularly in condensed matter (e.g., magnons, phonons, hydrodynamic modes) and in macromolecular dynamics (e.g., normal mode analysis). By demonstrating that such modes also exist in cell-state transition dynamics, and in non-equilibrium nonlinear systems more generally, we offer a new theoretical-physics perspective on these systems. The collective modes separate into slow and fast modes. Long-term dynamics are governed by a few dominant slow modes that form a slow manifold of much lower dimension than the original state space. Thus, although the cell is a very high-dimensional system, its cell-cycle dynamics ultimately reduce to a low-dimensional space. Each mode comprises the coordinated behavior of groups of genes and reflects the structure of the underlying gene regulatory network. The modes can also be decomposed into terms that behave like damped harmonic oscillators, drawing an analogy between the modes of a nonlinear system and the normal modes of many-body systems. Finally, our analysis suggests that the dominant modes are closely associated with biological processes in the cell cycle, including mitosis, spindle checkpoint signaling, and DNA replication and repair.

</details>

### [NanoHIV-DR: a Nextflow workflow for consensus and read level HIV-1 drug resistance profiling from Oxford Nanopore sequencing](https://www.biorxiv.org/content/10.64898/2026.11.20.768148v1)
*Lule, D.; Ssemwanga, D.; Kaleebu, P. et al.* · `bioinformatics` · bioRxiv doi:10.64898/2026.11.20.768148 v1 · relevance 0.08

- **In one sentence**: NanoHIV-DR is a Nextflow workflow that takes raw Oxford Nanopore HIV-1 sequencing data through basecalling, read cleaning, alignment and consensus building, then reports drug-resistance mutations both at the consensus level (via Sierra) and at the read level for minority variants.
- **In plain words**: HIV treatment can stop working when the virus carries mutations that resist specific drugs, so clinics test the virus's genetic code to guide treatment. This paper describes a software pipeline that handles the many computing steps needed to turn raw data from a portable DNA sequencer into a readable resistance report. The authors say it can also pick up mutations present in only a fraction of virus copies, which a standard consensus approach would miss.
- **Why it matters**: Portable long-read sequencing could make HIV drug-resistance testing faster and more accessible, especially where specialist bioinformatics staff are scarce. The text describes the workflow and its goals but gives no accuracy or validation results, so how well it performs in practice cannot be judged from this text alone.
- **Background needed**: - HIV-1 drug resistance: viral mutations that reduce the effect of antiretroviral drugs; genotyping reads the viral genetic sequence to detect them.
- Oxford Nanopore sequencing: a portable method that reads long DNA/RNA strands by measuring electrical signal changes as they pass through a pore; raw signal files (POD5) must be "basecalled" into letters.
- Demultiplexing: separating pooled samples back into individual samples by their barcodes.
- Read alignment and consensus: mapping short or long sequence reads onto a reference genome and combining them into one most-common sequence.
- Minority variants: mutations found in only a subset of viral copies in a patient, which a consensus sequence can hide.
- Nextflow: a workflow system that chains analysis steps so they run reproducibly on different computers. · level: intermediate

<details><summary>Original abstract</summary>

Oxford Nanopore sequencing offers a rapid and portable approach for HIV-1 drug resistance (HIVDR) genotyping, but analysis of the resulting long-read data requires multiple bioinformatics steps and currently available nanopore workflows are limited. We developed NanoHIV-DR, a Nextflow-based workflow that streamlines the analysis of Oxford Nanopore sequencing data and generation of HIVDR reports. NanoHIV-DR processes raw POD5 files through basecalling, demultiplexing, host-read removal, quality filtering, read alignment and consensus generation, before identifying resistance-associated mutations and interpreting predicted drug susceptibility. The workflow provides two complementary approaches to HIVDR analysis: consensus-based resistance interpretation using Sierra and read-level detection of resistance-associated variants, enabling mutations below the consensus level to be identified and quantified. Outputs are integrated with clinical metadata to generate human-readable HIVDR reports. NanoHIV-DR provides a reproducible and accessible workflow for Nanopore-based HIVDR analysis with reduced bioinformatics expertise and manual processing for translating long-read sequencing data into interpretable resistance profiles.

</details>

## Neuroscience

### [Cross-domain competition for memory reactivation resources during sleep](https://www.biorxiv.org/content/10.64898/2026.11.20.768209v1)
*Temudo, A.; Nicolas, J.; King, B. R. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.20.768209 v1 · relevance 0.07

- **In one sentence**: In a within-subject nap study (n=24), cueing object-task memories during NREM sleep with targeted memory reactivation did not indirectly strengthen a linked motor memory, and sleep EEG slow oscillation and spindle activity appeared to favor the motor trace over the object memory.
- **In plain words**: When we learn two related skills, our brains may replay memories of them during sleep, and the two can end up competing. This study used sound or scent-style cues tied to one task during a 90-minute nap to see whether replaying an object-task memory would also replay a linked motor-task memory. The object memory got worse rather than better, and brain-wave patterns suggested the motor memory received the sleep processing instead.
- **Why it matters**: It suggests memories that share a common structure may compete for limited sleep-time consolidation resources, which matters for how we design memory-boosting sleep interventions. The text does not establish how general this competition is or whether it holds beyond this task pairing, so the finding should be treated as preliminary.
- **Background needed**: - Targeted memory reactivation (TMR): pairing a cue (often a sound) learned during waking practice with that memory, then presenting the cue again during sleep to reactivate it.
- NREM sleep: the deeper, non-dream sleep stages where memory consolidation is thought to occur.
- Slow oscillations (0.5-2 Hz) and sleep spindles (12-16 Hz): rhythms in sleep EEG (brain electrical recordings) thought to help move and protect memories.
- Declarative vs. procedural memory: facts/events versus learned motor or skill sequences.
- Within-subject design: each participant does all conditions, so comparisons are made within the same people.
- Covert consolidation: memory processing that happens without a behavioral change being directly visible. · level: research-level

<details><summary>Original abstract</summary>

Targeted Memory Reactivation (TMR) enhances the consolidation of both declarative and procedural memories. As previous research highlights the importance of cross-domain interactions in shaping memory consolidation, we investigated here whether interacting memories from different domains can be co-reactivated by TMR during post-learning sleep, and in turn enhance consolidation. In a fully within-subject design, twenty-four young, healthy participants learned both a motor and an object sequence learning task that were linked or not by a shared ordinal structure. TMR cues associated only with the object task were presented during post-learning non-rapid eye movement (NREM) sleep which was monitored with electroencephalography (EEG) during a 90-minute nap. We tested whether reactivating object memories would indirectly reactivate the linked motor memory. Behavioral results showed no overall effect of association but indicated that TMR disrupted object memory consolidation without indirectly affecting performance on the linked motor task. Sleep EEG data point to a competition for reactivation resources whereby slow oscillation (SO; 0.5-2 Hz) and spindle activity (12-16 Hz) involved in both memory protection and potentiation during sleep were preferentially allocated to the covert consolidation of the motor trace at the expense of object memory. These findings suggest that cross-domain memories sharing a common learning structure compete for consolidation resources during post-learning sleep.

</details>

### [Reduced bushy cell firing limits binaural coding after cochlear synaptopathy](https://www.biorxiv.org/content/10.64898/2026.11.21.768331v1)
*Ashida, G.; Tollin, D. J.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.21.768331 v1 · relevance 0.06

- **In one sentence**: A computational model of the auditory brainstem tests how cochlear synaptopathy (loss of auditory nerve inputs to bushy cells) and increased temporal jitter in bushy cell outputs, modeled as central myelin dysfunction, each impair binaural coding in the lateral superior olive.
- **In plain words**: People can have trouble hearing in noisy settings and locating sounds even when their standard hearing tests look normal. This paper uses a computer model of the hearing pathway to test two possible causes: losing some of the nerve connections from the ear, and nerve signals that arrive with less precise timing. The model found that each cause reduces the brain's ability to compare the two ears' signals, but in different ways.
- **Why it matters**: It offers a mechanistic account of how hidden hearing damage could affect spatial hearing and speech in noise, which may matter for people with normal audiograms. The text is a model-based study, so its predictions about real listeners are not tested here, and the link to human hearing difficulties remains a hypothesis.
- **Background needed**: - Cochlear synaptopathy: loss of connections between inner hair cells in the ear and auditory nerve fibers, which can occur without raising the hearing threshold.
- Bushy cells: neurons in the cochlear nucleus (first brainstem hearing station) that receive auditory nerve input and relay timing information.
- Lateral superior olive (LSO): a brainstem site that compares loudness between the two ears, helping locate sounds.
- Interaural envelope phase differences: small timing differences in the loudness fluctuations of a sound reaching each ear, used for spatial hearing.
- Phase locking: how precisely a neuron's spikes follow the timing of a sound wave.
- Temporal jitter: random variation in spike timing, here used to model myelin-related transmission problems.
- Computational model: a simulation built from physiological data, not a study with human or animal recordings in this text. · level: research-level

<details><summary>Original abstract</summary>

Listeners can experience difficulties with spatial hearing and speech understanding in complex acoustic environments despite near-normal hearing thresholds. Cochlear synaptopathy, which reduces auditory nerve input without elevating thresholds, is one candidate mechanism, but how this peripheral deafferentation disrupts binaural processing remains unclear. We adapted a physiologically constrained computational model incorporating the auditory periphery, spherical and globular bushy cells of the cochlear nucleus and the lateral superior olive (LSO) to examine the separate and combined effects of reduced afferent input and degraded spike timing. Synaptopathy was modeled as loss of auditory nerve inputs to bushy cells, whereas central myelin dysfunction was modeled as increased temporal jitter in bushy cell outputs. Loss of auditory nerve input substantially reduced bushy cell firing rates without degrading phase locking. Despite this preserved temporal precision, binaural tuning in the LSO declined disproportionately, where moderate afferent loss produced substantial reductions in sensitivity to interaural envelope phase differences. In contrast, temporal jitter preserved bushy cell firing rates but degraded phase locking and binaural tuning. Selective loss of input to excitatory versus inhibitory pathways produced opposite changes in overall LSO firing rate, yet both reduced binaural interaction. These results identify two mechanistically distinct routes to impaired binaural coding: too few precisely timed spikes, and a sufficient number of spikes arriving with inadequate temporal precision. These results predict that correcting myelin-related timing deficits alone would leave substantial binaural coding impairment when cochlear deafferentation persists, motivating interventions that address both diminished afferent drive and impaired transmission.

</details>

## Genetics and genomics

### [Reproductive competition amplifies purifying selection and reduces genetic load](https://www.biorxiv.org/content/10.64898/2026.11.20.768053v1)
*van Oosterhout, C.; Marsters, J.; Birley, T.* · `genetics` · bioRxiv doi:10.64898/2026.11.20.768053 v1 · relevance 0.08

- **In one sentence**: Forward-time simulations express competitive and sexual selection as an effective selection coefficient calibrated against hard selection, showing that reproductive competition can purge deleterious mutations more efficiently and with lower genetic load.
- **In plain words**: The paper asks how a population gets rid of harmful genetic variants when individuals compete for mates or reproductive success, rather than simply dying off when they are unfit. Using computer simulations, the authors convert the strength of competition into an equivalent "effective selection" strength so it can be compared with simple culling. They report that competition with several rivals strongly speeds up removal of harmful variants, and that repeated contests help by averaging out noise, which lowers the overall burden of harmful mutations.
- **Why it matters**: The work offers a population-genetic mechanism for how competition could cut the demographic cost of purging harmful mutations, which may matter for small or bottlenecked populations where harmful variation tends to build up. The text does not show direct tests in real populations, so its practical relevance remains to be established.
- **Background needed**: - Genetic load: the reduction in average fitness caused by harmful (deleterious) mutations carried in a population.
- Purifying (negative) selection: the process by which harmful variants are removed over generations.
- Hard selection: selection in which unfit individuals die or fail to reproduce regardless of others, which can impose a large demographic cost.
- Competitive and sexual selection: selection through differences in success when individuals contest mates or resources, so reproduction is ranked rather than all-or-nothing.
- Effective selection coefficient: a single number expressing how strong a selection process is, here calibrated so competition can be compared with hard selection.
- Genetic drift: random change in variant frequencies, which can dominate for weakly harmful mutations in small populations.
- Forward-time simulation: modelling a population generation by generation on a computer.
- Genic capture: a term from the paper's framing, linking overall genome quality to how effectively selection acts; its meaning here is only briefly stated in the text. · level: research-level

<details><summary>Original abstract</summary>

Deleterious mutations impose genetic load, and purging them through hard selection can carry substantial demographic costs. Competitive and sexual selection can instead remove deleterious variation through differential reproductive success. What remains unclear is when this process is more efficient than equivalent hard selection, and how competition generates this advantage. Here, we use forward-time simulations to express the impact of competition as an effective selection coefficient (se) calibrated against hard selection. Competition with multiple rivals strongly amplified purifying selection, whereas repeated contests improved discrimination by averaging stochastic and environmental variation. Strong competition also reduced genetic load relative to hard selection. These effects can shift weakly deleterious mutations from drift-dominated behaviour towards efficient purging. By front-loading purifying selection into reproduction, competitive selection can reduce genetic load at lower demographic cost. This provides a population-genetic mechanism by which genic capture can translate genome-wide genetic quality into more effective purifying selection. This may be particularly important in bottlenecked populations, where demographic recovery can relax purifying selection and allow genomic erosion to persist.

</details>

### [A genetic toolkit of visible mutants for Caenorhabditis briggsae](https://www.biorxiv.org/content/10.64898/2026.11.19.767928v1)
*Johnsen, R.; Mah, A.; Thillainathan, B. et al.* · `genetics` · bioRxiv doi:10.64898/2026.11.19.767928 v1 · relevance 0.08

- **In one sentence**: A resource paper reporting 183 visible EMS-induced mutants of the nematode Caenorhabditis briggsae, their genetic mapping to six linkage groups, and molecular identification of several genes, with comparisons to C. elegans orthologs.
- **In plain words**: This paper is about a set of tiny worm mutants, made in a close relative of the lab worm C. elegans, that scientists can use as genetic tools. The authors collected 183 mutants with easy-to-see features, worked out where many of them sit on the worm's chromosomes, and linked several to specific genes. They also say some earlier records of these mutants were corrected.
- **Why it matters**: Genetic research depends on mutants that show clear traits, and C. briggsae is useful for comparing how related species evolved. The paper supplies data and strains that other labs can use, which may help comparative studies across Caenorhabditis worms; the text does not claim broader impact beyond this.
- **Background needed**: - Mutant: an organism carrying a changed gene that produces a visible or measurable difference.
- EMS: a chemical mutagen used to create random mutations in animals.
- C. elegans and C. briggsae: two closely related roundworms; C. elegans is the standard lab model.
- Linkage group: a set of genes that tend to be inherited together, roughly corresponding to a chromosome.
- Complementation test: a cross that checks whether two mutations affect the same gene.
- Ortholog: a gene in one species that descends from the same ancestral gene as one in another species.
- Transgene rescue: putting a normal copy of a gene into a mutant to see whether the trait is restored, which confirms the gene's identity.
- Levamisole: a drug that acts on nerve-muscle receptors; resistant worms reveal receptor genes. · level: research-level

<details><summary>Original abstract</summary>

Caenorhabditis briggsae is a widely used model for comparative genetic studies involving C. elegans. Genetic analysis in C. briggsae depends on mutations with clear, easily recognizable phenotypes, yet most mutants reported so far have been mentioned only as names and linkage groups, without underlying experimental data. This study reports 183 C. briggsae mutants belonging to 11 phenotypic classes, which represent the most comprehensive collection to date. Almost all mutants were recovered in EMS screens of the reference strain AF16. Our analysis revealed that 121 mutations define 55 loci and 62 remain unassigned. A combination of complementation tests, linkage tests, two- and three-factor crosses, and polymorphism-based mappings helped place 51 loci and 15 further mutations to the six linkage groups. We report the supporting data, map distances, linkage groups, and corrections to several earlier assignments. Twenty-three loci correspond to molecularly identified orthologs of C. elegans genes, including six for which we report genetic, rescue, or sequence evidence here. The levamisole-resistant mutants fall into at least three complementation groups, two of which correspond to Cbr-unc-38 and Cbr-unc-29 (levamisole-sensitive nicotinic acetylcholine receptor a and non-a subunit, respectively). Transgene rescue experiments identify Cbr-dpy-1 (mucin-like), Cbr-sma-6 (TGFb type receptor kinase), and Cbr-unc-4 (homeodomain transcription factor), genes that have long been in use as genetic markers. In all cases, molecularly identified genes are located on the same chromosome as their C. elegans orthologs, although gene order within chromosomes differs. The strains, map, and underlying data provide a resource for genetic and comparative studies in Caenorhabditis nematodes.

</details>

## Cell and molecular biology

### [Identification of SAMD4B as a Centrosome-Associated Regulator of the Sonic Hedgehog Signaling Pathway](https://www.biorxiv.org/content/10.64898/2026.11.19.767524v1)
*Bernatik, O.; Vyslouzil, D.; Paclikova, P. et al.* · `cell biology` · bioRxiv doi:10.64898/2026.11.19.767524 v1 · relevance 0.09

- **In one sentence**: Proximity-labeling screen under ciliogenesis-restrictive versus permissive conditions identifies SAMD4B, a centrosome-associated protein, as required for Shh signaling in NIH3T3 cells and eye development in zebrafish, possibly via ciliary recruitment of ARL13B and SMO.
- **In plain words**: Cells build tiny antenna-like structures called primary cilia that help them receive developmental signals, including the Sonic hedgehog (Shh) signal that guides how embryos form. This study used a labeling method that tags proteins near each other to find new factors involved in building or using these cilia. It found that a protein called SAMD4B, which sits near the cell's central organizing structure (the centrosome), is needed for Shh signaling in mouse cells and for normal eye development in zebrafish.
- **Why it matters**: Cilia defects are linked to many developmental disorders, so new regulators of Shh signaling are of interest. The paper suggests a link between SAMD4B, previously known for RNA condensates in the cytoplasm, and ciliary signaling; the text does not establish how general this role is or whether it matters in human disease.
- **Background needed**: - Primary cilia: small hair-like projections on cells that act as signal-receiving hubs.
- Sonic hedgehog (Shh): a signaling pathway essential for embryo development and tissue maintenance.
- Centrosome: a cell structure that organizes microtubules (cell's internal scaffolding) and anchors cilia formation.
- ARL13B and SMO: proteins that must move into the cilium for Shh signaling to work.
- Proximity labeling: a method that marks proteins lying close to a target protein so their interactions can be mapped.
- siRNA depletion: a way to switch off a gene temporarily to test its function.
- NIH3T3 cells (mouse cell line) and zebrafish are the model systems used.
- RNA condensates: droplet-like clusters of RNA and proteins inside the cell. · level: research-level

<details><summary>Original abstract</summary>

Background: Many protein-protein interactions are required for the assembly and function of primary cilia, microtubule-based organelles critical for the Sonic hedgehog (Shh) signaling pathway and, in turn, for embryonic development and tissue homeostasis. However, our understanding of this complex process remains incomplete. Methods: To identify new regulators of primary cilia formation or function, we carried out proximity labeling experiments and compared interactomes under ciliogenesis-restrictive and permissive conditions. Using an unbiased strategy, we selected candidates that were tested functionally by siRNA-mediated depletion or gene editing, in combination with gene expression analysis and various microscopy techniques, using either vertebrate cell lines or zebrafish as model systems. Results: We demonstrate that one of our identified candidates, protein SAMD4B, is associated with the centrosome and is required for Shh signaling in NIH3T3 cells and eye development in zebrafish. Our data implicate defective ciliary recruitment of Shh pathway regulators ARL13B and SMO as a plausible mechanism underlying the SAMD4B-mediated regulation of Shh signaling. Conclusions: Together, our data identify a previously unrecognized link between SAMD4B, a protein known to be associated with cytoplasmic RNA condensates, and ciliary signaling.

</details>

### [Smyd1 regulates H3K4me3 to support adaptive fatty acid oxidation in the adult heart during lipid overload](https://www.biorxiv.org/content/10.64898/2026.11.18.763125v1)
*Mukai, R.; Oka, S.; Sung, E.-A. et al.* · `cell biology` · bioRxiv doi:10.64898/2026.11.18.763125 v1 · relevance 0.09

- **In one sentence**: In mice, high-fat diet transiently raises the histone methyltransferase Smyd1 and H3K4me3 in heart muscle cells, and cardiac Smyd1 heterozygous knockout worsens fatty acid oxidation gene responses, dysfunction and survival, with a Smyd1–PPARα interaction proposed as a mechanism.
- **In plain words**: Obesity can weaken the heart over time, partly because heart muscle cells stop burning fat efficiently. This study looked at a protein called Smyd1 that helps control gene activity, and found that in mice fed a high-fat diet it rises early on, which appears to help the heart keep burning fat. Mice with less Smyd1 in the heart did worse: their hearts weakened faster, enlarged, scarred more, and they were less likely to survive.
- **Why it matters**: It suggests a possible molecular route by which the heart adapts to fatty diets and where that adaptation could fail, which may matter for obesity-related heart disease. The findings are from mice, and the text does not show that the same mechanism operates in people or that targeting it would help.
- **Background needed**: - Fatty acid oxidation (FAO): the process by which cells break down fats to produce energy; the heart relies on it heavily.
- Obesity-related cardiomyopathy: weakening of the heart muscle linked to excess body fat.
- Histone methylation: chemical tags on the protein spools that DNA wraps around, which change how genes are switched on; H3K4me3 is one such tag linked to active genes.
- Smyd1: a histone methyltransferase, an enzyme that adds these tags, found mainly in muscle.
- PPARα: a nuclear receptor (a gene-switching protein) that turns on fat-burning genes.
- Co-immunoprecipitation: a lab method for testing whether two proteins physically bind together.
- Single-cell RNA sequencing: a method that measures gene activity in individual cells.
- Heterozygous knockout: a model where one of two working copies of a gene is removed. · level: research-level

<details><summary>Original abstract</summary>

Obesity and metabolic syndrome are major risk factors for heart failure, and impaired fatty acid oxidation (FAO) is a key contributor to metabolic dysfunction in obesity-related cardiomyopathy. However, how the heart maintains FAO and adapts to chronic lipid overload remains poorly understood. Here, we identify SET and MYND domain-containing protein 1 (Smyd1), a muscle-specific histone methyltransferase, as an early compensatory regulator of cardiac metabolism in response to lipid overload. In wild-type mouse hearts, high-fat diet (HFD) feeding induced transient increases in Smyd1 expression and H3K4me3 levels during the early-to-mid phase of metabolic stress, both of which returned to baseline levels during prolonged HFD exposure. Single-cell RNA sequencing further revealed that this adaptive increase in Smyd1 expression occurred predominantly in cardiomyocytes. In contrast, cardiac-specific Smyd1 heterozygous knockout mice exhibited accelerated cardiac dysfunction, left ventricular dilation, increased myocardial fibrosis, and reduced survival following HFD feeding. Mechanistically, Smyd1 deficiency impaired the adaptive upregulation of key FAO-related genes and reduced cardiac FAO activity. Furthermore, co-immunoprecipitation analysis revealed an interaction between Smyd1 and peroxisome proliferator-activated receptor alpha (PPAR), suggesting a potential mechanism by which Smyd1 supports FAO gene expression. Taken together, these findings identify Smyd1 as an early compensatory regulator that supports FAO-dependent metabolic adaptation and protects the heart against lipid overload-induced cardiac dysfunction. This adaptive mechanism, involving H3K4me3 regulation and the Smyd1-PPAR interaction, may provide potential therapeutic targets for therapeutic strategies aimed at preserving cardiac metabolic flexibility in obesity-related cardiomyopathy.

</details>

## Immunology and microbiology

### [Oral microbiome and DNA virome profiling in pigs reveals age-associated dynamics and extracellular recovery of Streptococcus suis-associated phage lineages](https://www.biorxiv.org/content/10.64898/2026.11.21.768310v1)
*Osei, E. K.; Ornelas, M. A. S.; Garcia Manzanilla, E. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.21.768310 v1 · relevance 0.11

- **In one sentence**: Shotgun metagenomic profiling of oral fluids from pigs on 15 Irish farms, with paired bulk and virus-like-particle enrichment, maps age-linked succession in oral bacteria and DNA phages and flags 26 vOTUs predicted to infect Streptococcus suis.
- **In plain words**: Researchers sampled the saliva-like oral fluid of pigs at several ages across 15 commercial farms and read out all the DNA in it, both the bacteria and the viruses that infect them. The mouth's microbial community changed in a fairly predictable way as pigs aged, moving from environmental bacteria shortly after weaning to lactic acid bacteria and anaerobes later on. Most of the viral sequences could not be matched to a known genus, but 26 were predicted to infect Streptococcus suis, a pig pathogen.
- **Why it matters**: Pig oral fluids are already used to monitor herd health, so a catalogue of the viruses living there could inform both disease surveillance and the search for phages that might be used against S. suis. The text is a descriptive survey; it does not show that these phages work against the bacterium or that they would be useful as treatments.
- **Background needed**: - Microbiome: the community of bacteria and other microbes living in a body site.
- Virome: the set of viruses in a sample; here, DNA viruses only.
- Bacteriophage (phage): a virus that infects bacteria; phages are being studied as possible alternatives to antibiotics.
- Shotgun metagenomics: sequencing all DNA in a sample without first culturing organisms, then identifying what is there computationally.
- VLP (virus-like particle) enrichment: a lab step that concentrates viral particles before sequencing.
- vOTU (viral operational taxonomic unit): a computational grouping of viral sequences treated as one viral species.
- Streptococcus suis: a bacterium that causes disease in pigs and can occasionally infect people.
- Resistome: the collection of antibiotic resistance genes in a sample. · level: research-level

<details><summary>Original abstract</summary>

The pig oral cavity is a critical interface for microbial transmission and herd health monitoring, yet its microbiome and virome remains poorly characterised. We performed shotgun metagenomic sequencing of oral fluids from pigs across 15 commercial farms in Ireland, using paired bulk and virus-like particles (VLP) enrichment to capture comprehensive microbial and DNA virome diversity. Microbial communities shifted progressively with age, with early post-weaning animals enriched in environmental genera such as Pseudomonas and Staphylococcus and later stages dominated by lactic acid bacteria and anaerobes. Only 20.6% of vOTUs could be assigned to a known genus, with the most abundant being Astrithrvirus, which increased with age. Both microbiome and DNA virome exhibited predictable, coordinated age-associated succession with strong cross-domain coupling supported by virus-host networks. Functional profiling of the microbiome revealed that predicted carbohydrate substrates tracked the dietary transitions, while accessory viral functions partitioned by lifestyle and host. The early post-weaning stage was characterised by high abundance of viral integration and excision functions, as well as elevated resistome diversity that was almost exclusively of prokaryotic origin rather than viral. Importantly, 26 of the 25,223 vOTUs identified were predicted to target Streptococcus suis, providing the first metagenomic catalogue of such phages from pig oral environments. These findings expand our understanding of oral microbiome-virome dynamics and establish a framework for integrated microbiome and viromics approaches that could enable therapeutic phage discovery and inform microbiome-targeted interventions in pig production systems.

</details>

### [Spatial Transcriptomics Reveals Host Gene Expression Patterns Associated with Naegleria fowleri Infection in the Murine Brain](https://www.biorxiv.org/content/10.64898/2026.11.18.767516v1)
*Dainis, J.; Bailey, M.; Sievert, M. A. C. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.18.767516 v1 · relevance 0.11

- **In one sentence**: Spatially resolved transcriptomics of mouse brains at several time points after intranasal Naegleria fowleri inoculation maps region-specific host gene expression, including inflammatory and putative immune and neural cell signatures.
- **In plain words**: Naegleria fowleri is a free-living amoeba that can enter the brain through the nose and cause a rare, usually fatal infection called primary amoebic meningoencephalitis. The researchers infected mice through the nose, collected brain tissue at several time points, and measured which genes were active in different brain regions. They found strong inflammatory gene activity that differed by region and over time, including in areas where no amoebae were detected.
- **Why it matters**: The infection is extremely deadly, and little is known about where and when the brain's immune response happens. Mapping this by location in the brain may help guide later studies of how inflammation damages brain tissue, though the text is a descriptive profiling study and does not test treatments.
- **Background needed**: - Naegleria fowleri: a free-living amoeba found in warm fresh water that can invade the nervous system through the nose.
- Primary amoebic meningoencephalitis (PAM): the brain and lining infection it causes, with a mortality rate above 97% as stated in the text.
- Transcriptomics: measuring which genes are switched on (expressed) in a tissue, usually via their RNA.
- Spatial transcriptomics: gene activity measured while keeping track of where in the tissue each signal came from.
- Neuroinflammation: inflammation inside the brain, driven by immune cells such as macrophages, neutrophils and natural killer T cells.
- Cell-type signatures: patterns of genes that suggest which kinds of cells are present, inferred rather than directly counted.
- Intranasal inoculation: infecting animals by placing the organism in the nose. · level: intermediate

<details><summary>Original abstract</summary>

Primary Amoebic Meningoencephalitis (PAM), caused by the free-living amoebae Naegleria fowleri, is a devastating disease with a mortality rate exceeding 97%. Despite its severity, the spatial and temporal characteristics of the host immune response to infection within the brain remain poorly understood. Here, we used spatially resolved transcriptomic profiling to characterize region-specific gene expression patterns in brain tissue collected at multiple time points following intranasal inoculation of N. fowleri in mice. Our analysis revealed pronounced pro-inflammatory transcriptional signatures that varied across brain regions and over the course of infection. Cell type-associated gene expression profiles suggested the involvement of several immune cell populations, including macrophages, neutrophils, and natural killer T cells, alongside transcriptional changes associated with neural cell populations. Notably, inflammatory transcriptional signatures also were detected in brain regions without detectable amoebae, indicating that host responses extend beyond regions of apparent parasite localization. Collectively, these findings provide a spatial and temporal characterization of the host transcriptional response during experimental PAM, highlighting inflammatory gene expression signatures and putative immune and neural cell populations associated with disease progression. This study provides a foundation for future investigations into the cellular and molecular processes underlying neuroinflammation during N. fowleri infection.

</details>

## Cancer biology

### [Media matters: A resource for understanding the determinants of migratory potential of malignant and non-malignant cells](https://www.biorxiv.org/content/10.64898/2026.11.18.767665v1)
*Kim, B.; Lopez, A.; Osuna, M. F. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.18.767665 v1 · relevance 0.08

- **In one sentence**: A high-throughput wound-healing/invasion screen of more than 60 non-malignant and malignant epithelial cell lines from several organs, probing how growth media and glucose metabolism shape migratory potential.
- **In plain words**: Cells have to move to repair wounds, and cancer cells move to spread through the body. This paper tested dozens of normal and cancerous cell lines from the pancreas, colon, skin, breast, prostate and lung to see how well each one migrates and invades in a lab dish. The authors report that, surprisingly, many normal cells moved faster than their cancerous counterparts, and that the nutrient content of the culture medium changed how cells moved.
- **Why it matters**: The work is offered as a reference dataset of migration behavior and as a way to look for drugs that slow cell movement, which could matter for cancer spread and for wound-healing disorders. The text is an abstract only, so the strength of the findings and how well they transfer to patients cannot be judged from it.
- **Background needed**: - Migration/invasion assay: a lab test where cells are grown to a confluent layer, a gap ("wound") is scratched, and the speed at which cells fill the gap is measured.
- Metastasis: the spread of cancer from its original site to other organs; antimetastatic and migrastatic drugs aim to block this spread.
- Glycolysis and oxidative phosphorylation: the two main ways cells produce energy from glucose, one without oxygen and one using the mitochondria.
- Culture medium: the nutrient broth cells grow in; "low-nutrient" here means low or no serum, low calcium and physiological glucose levels, closer to conditions in the body.
- Malignant vs non-malignant: cancerous versus normal cells; "carcinoma" is a cancer arising from epithelial (lining) tissue. · level: intermediate

<details><summary>Original abstract</summary>

Cell mobility is critical for homeostatic processes such as wound repair and diseases like cancer metastasis. While the advent of migrastatic and antimetastatic therapies has promise, the identification and translation of pathways important for migratory plasticity into druggable targets approved in clinical trials are considerably lacking. To better understand why, we developed an unbiased high-throughput wound-healing/invasion assay to screen for the migratory potential of >60 non-malignant and malignant cell lines derived from the pancreas, colon, skin, breast, prostate, and lung. The goal of this phenotypic screen was to provide a resource of migration/invasion potential and insight into the differential properties not only between malignant and non-malignant cells but also the various carcinomas. Surprisingly, we found non-malignant epithelial cells of the lung, skin, and pancreas migrated/invaded faster than their malignant counterparts. We observed perturbation of glucose metabolism, via inhibition of glycolysis, restricted the migration of non-malignant but not cancer cells, whereas inhibition of oxidative phosphorylation limited the mobility of malignant more than normal cells of the lung, skin, and pancreas. Short-term acclimation of cancer cells in low-nutrient media, containing low/no serum, low calcium, and physiological concentrations of glucose, increased in vitro migration/invasion and in vivo metastatic potential of lung but not pancreatic carcinomas. Phenotypic and metabolic screens presented here could identify prospective therapeutics not only for cancer metastasis, but also diseases driven by the dysregulation of wound-healing/regeneration.

</details>

### [Metabolic priming recruits tumour cells across a mitochondrial vulnerability threshold and sensitizes them to chemotherapy](https://www.biorxiv.org/content/10.64898/2026.11.13.766410v1)
*Iborra, F. J.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.13.766410 v1 · relevance 0.05

- **In one sentence**: Single-cell study using TMRM fluorescence excursions during pulsed illumination as a readout of mitochondrial vulnerability to photodynamic damage, shown to be recruitable by metabolic priming (TEPP46, ethyl pyruvate) and to show descriptive combination effects with camptothecin or TRAIL in cultured cells.
- **In plain words**: Some cancer cells in a tumour survive treatments that kill their neighbours. This paper asks whether a drug-like nudge to the cells' energy machinery can push more of them into a state where their mitochondria (the cell's power plants) are easier to damage with light. The authors followed individual cells with a dye that lights up in healthy mitochondria, and found that a fluorescence "rise then fall" pattern, the difference from each cell's own resting level, best predicted which cells died.
- **Why it matters**: It offers a way to watch single-cell vulnerability over time and to test whether a short pre-treatment could widen the window for a later therapy. The work is limited to cultured cells and some human tumour sections, has not been tested in vivo, and the combination results are described by the authors as needing independent replication, so its wider relevance is still unclear.
- **Background needed**: - Intratumour heterogeneity: cells within one tumour differ, so some resist treatment.
- Mitochondria: organelles that produce cellular energy; their membrane voltage drives dye accumulation.
- TMRM: a fluorescent dye that accumulates in mitochondria depending on membrane voltage; here it also acts as a light-activated photosensitizer that generates reactive oxygen species (damaging chemical byproducts).
- Photodynamic damage: killing cells by combining a light-activated agent with light.
- PKM2 and TEPP46: PKM2 is a metabolic enzyme; TEPP46 is a chemical that activates it.
- Camptothecin and TRAIL: an anticancer drug and a death-signalling protein used as combination partners.
- Bliss independence: a standard baseline for expected combined effect of two treatments acting independently; survival below it suggests interaction.
- AUC (area under the curve): a 0 to 1 score of how well a predictor separates outcomes; 0.5 is chance. · level: research-level

<details><summary>Original abstract</summary>

Intratumour heterogeneity allows a fraction of cancer cells to escape otherwise effective treatment. Here we ask whether metabolic priming can recruit heterogeneous tumour cells into a transient mitochondrial state that is selectively vulnerable to photodynamic damage. Tetramethylrhodamine methyl ester (TMRM) has previously been shown to act as a mitochondria targeted photosensitizer; we exploit its voltage-dependent accumulation and dynamic fluorescence during pulsed illumination to quantify vulnerability in single cells. The response is a reproducible fluorescence excursion, a rise to a maximum followed by a decay, accompanied by reactive oxygen species production. Comparing seventeen descriptors of this excursion against subsequent fate in 195 cells across four arms shows that quantities referenced to each cell's own resting value outperform static intensity. The simple difference Fmax F0 predicts death with held-out areas under the curve of approximately 0.75 to 0.79, whereas resting intensity alone carries little transferable information and time to peak does not discriminate fate in the datasets tested. Metabolic priming with the PKM2 activator TEPP46 or with ethyl pyruvate increases the fraction of responding cells; under TEPP46 almost the whole population enters the responding state. PKM2 abundance is associated with faster entry into that state, and PKM2 is heterogeneous in human skin tumour sections. Four hours of camptothecin shifts the response distribution, increasing the fraction of cells above the untreated median from 50% to 76%, identifying a candidate intervention window. In combination experiments, TMRM photodynamic treatment produced survival below the Bliss-independence expectation with camptothecin or TRAIL, in both treatment orders and across three cell lines; these combination measurements are descriptive and require independent replication. The study therefore identifies a perturbation-revealed mitochondrial vulnerability that can be pharmacologically recruited and followed dynamically at single-cell resolution. It is a proof of concept in cultured cells and human tumour sections and has not been tested in vivo.

</details>

## Ecology and evolution

### [Social information use promotes breeding synchrony but constrains adaptation to rapid environmental changes](https://www.biorxiv.org/content/10.64898/2026.11.20.767538v1)
*Zheng, J.; Kuijper, B.; Aplin, L. M. et al.* · `animal behavior and cognition` · bioRxiv doi:10.64898/2026.11.20.767538 v1 · relevance 0.10

- **In one sentence**: An evolutionary individual-based model shows that breeders copying their neighbours' timing synchronises populations and speeds adaptation in stable or spatially varied conditions, but slows tracking of directional climate change, creating a synchrony-versus-flexibility trade-off.
- **In plain words**: The paper asks whether birds or other animals that time their breeding by watching their neighbours do better or worse than those relying only on their own sensing, especially as climate shifts the best timing. Using a computer simulation of individuals on territories with fluctuating, peaked resources, the authors found that copying neighbours makes breeding dates converge, which helps populations adapt faster and raises output when conditions are stable. When the climate shifts steadily, the same convergence leaves populations lagging behind the moving optimum and reduces reproduction.
- **Why it matters**: Breeding phenology is already shifting with climate change in many species, so whether copying others helps or hinders adjustment matters for conservation and forecasting. The results are from a model, so they show a mechanism that could operate in the wild rather than confirmed field effects; the text does not report empirical tests.
- **Background needed**: - Social information: cues gained by observing others' choices, such as neighbours' timing of breeding.
- Private information: an individual's own sensing of conditions, such as food or weather.
- Phenology: the timing of seasonal events like breeding.
- Individual-based model: a simulation in which each animal is tracked separately and can evolve over generations.
- Synchrony and positive feedback: when individuals copy each other, their behaviour converges and reinforces itself.
- Adaptive lag: when a population's average response trails a shifting environmental optimum.
- Trade-off: a gain in one property (coordination) that costs another (flexibility). · level: intermediate

<details><summary>Original abstract</summary>

Animals use social information to make decisions, yet how such processes influence predictions in reproductive timing and population adaptation under environmental change remains unclear. While social information can improve decision accuracy through information pooling, spatiotemporal heterogeneity in conditions and patterns of environmental changes creates noise that potentially limits the value of social information use among breeding individuals. Here, we established an evolutionary individual-based model to examine how social and private sensing interact to shape breeding phenology in species distributed across territories with peaked resources and facing annual fluctuations and rapid climate change. We show that when individuals incorporate social information from neighbours, behavioural responses become increasingly synchronised through positive feedback in decision-making. This emergent synchrony helps populations to adapt faster and can increase reproductive output under stable environmental conditions relative to relying only on private information. However, under directional climate change, the same mechanism reduces population responsiveness by constraining variation in individual responses, leading to systematic lag in tracking shifting environmental optima and reduced population reproductive output. Our results demonstrate that social information use can produce a general trade-off at the population level between synchronisation and adaptive flexibility across environmental contexts. Social interaction enhances population performance when environments are either consistent or changing drastically across both spatial and temporal scales. Rather than uniformly improving performance, social interaction may create conditions under which collective behaviour becomes maladaptive when environments change rapidly.

</details>

### [From individual movement to ecosystem response: how landscape structure shapes herbivore impacts](https://www.biorxiv.org/content/10.64898/2026.11.19.766513v1)
*Suarez, D. L.; Guisoni, N.; Laguna, M. F.* · `ecology` · bioRxiv doi:10.64898/2026.11.19.766513 v1 · relevance 0.10

- **In one sentence**: A spatially explicit stochastic individual-based model with Monte Carlo simulations of two herbivore populations with contrasting movement and foraging strategies sharing renewable, heterogeneous resources, including predation and refuge effects, examining how landscape structure and movement shape resource depletion and population dynamics.
- **In plain words**: This paper uses a computer simulation to ask how grazing animals that move differently affect the plants they share a landscape with. The authors track many individual animals across a patchy environment with uneven plant growth, predators, and safe refuges. They report that movement mainly controls where plants get depleted, and that a larger productive area can paradoxically lead to a larger relative loss of plants.
- **Why it matters**: The findings suggest that more food in a landscape does not automatically protect it from overgrazing, which matters for managing wildlife and rangelands. The text is a modelling study, so its results depend on the model's assumptions and it does not report field tests; how far they transfer to real ecosystems is not shown here.
- **Background needed**: - Individual-based model: a simulation where each animal is tracked separately and its local behaviour produces larger patterns.
- Monte Carlo simulation: running a model many times with random variation to see the range of likely outcomes.
- Consumer-resource dynamics: how the number of grazers or predators and the amount of plant food change each other over time.
- Heterogeneous landscape: an environment where resources are unevenly spread in patches rather than uniform.
- Refuge: a place where prey can hide from predators, which changes how much time they spend feeding in exposed areas.
- Resource biomass: the total mass of living plant material available as food.
- Vulnerability: how easily a part of the plant community can be depleted, here linked to overlap between where plants are and where herbivores go. · level: research-level

<details><summary>Original abstract</summary>

Understanding how local interactions generate large-scale ecological dynamics is a central challenge in ecology. In heterogeneous environments, consumer movement links resource distribution with exploitation, producing responses that may not be predicted from consumer abundance or resource availability alone. Here, we develop a spatially explicit stochastic individual-based model of two herbivore populations with contrasting movement and foraging strategies that share renewable resources. The model incorporates heterogeneous resources, consumer movement and feeding, resource regeneration, predation, and refuge availability. Using Monte Carlo simulations, we examine how herbivore pressure and landscape structure shape population dynamics and resource depletion. Movement strongly determines the spatial pattern of depletion, while resource vulnerability depends on the overlap between resource distribution and consumer activity. Counterintuitively, increasing the extent of a productive region increases initial resource biomass but can also increase relative resource loss. Additional resources sustain consumer activity where herbivores concentrate, showing that greater resource availability does not necessarily buffer ecosystems against herbivory. Resource biomass can also decline substantially before major reductions in vegetation occupancy become apparent. These results demonstrate how individual behaviour and landscape structure jointly shape ecosystem responses. The model provides a framework for investigating how spatially coupled consumer-resource interactions generate ecological dynamics.

</details>

## Plant biology

### [High-throughput phenotyping reveals natural variation in tomato pollen responses to heat stress](https://www.biorxiv.org/content/10.64898/2026.11.19.767983v1)
*Warman, C.; Perkins, C. J.; McKinley, S. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.19.767983 v1 · relevance 0.07

- **In one sentence**: A high-throughput microscopy pipeline with automated pollen classification and single-tube tracking quantifies how 218 tomato accessions and wild relatives respond to 26 °C versus 34 °C during pollen germination and tube growth.
- **In plain words**: Heat during flowering can make pollen fail, which can reduce fruit set in crops such as tomato. The authors built an automated system that photographs pollen grown in a dish at normal and high temperature, uses software to sort each grain and tube into categories, and follows individual pollen tubes over time. They applied it to 218 tomato types and wild relatives and found wide differences in how each responds to heat.
- **Why it matters**: Pollen heat tolerance is hard to measure at scale, so a faster, automated way to score many genetic lines could help breeders and geneticists look for the genes behind heat tolerance. The text reports strong agreement between automated and manual counts, but it does not show that these pollen measurements predict fruit yield in the field.
- **Background needed**: - Pollen: the male reproductive grains of a flowering plant; each must germinate and grow a tube to reach the egg.
- Germination and bursting: a healthy grain sprouts a tube; under stress it may burst instead and fail.
- Accession: a distinct line or variety held in a seed collection, used here as a unit of genetic variation.
- Wild relatives: undomesticated species related to crop tomato, often carrying useful stress-tolerance traits.
- Thermotolerant vs thermosensitive: able or unable to withstand high temperature without harm.
- R² (coefficient of determination): a 0–1 measure of how closely two sets of values agree; values near 0.9 or higher indicate close agreement.
- Bright-field microscopy: ordinary light microscopy used to image the grains.
- Time to 50% germination: the time at which half the grains have sprouted. · level: intermediate

<details><summary>Original abstract</summary>

Scalable measurements of pollen function are needed to investigate genetic variation in reproductive responses to heat. We developed a high-throughput phenotyping framework integrating automated bright-field microscopy, object detection, individual-tube tracking, and temporal analysis. We quantified pollen performance at 26 and 34 C across 218 tomato accessions and wild relatives by analyzing approximately 300,000 images collected over two-hour growth periods. Automated counts of pollen classes - aborted pollen grains, ungerminated, germinated, and burst pollen grains, and pollen tube tips - agreed closely with manual counts (R2 = 0.915-0.967). Heat stress shortened the mean time to 50% germination from 24.0 to 20.5 minutes but increased mean percent bursting at 2 hours from 14.9% to 83.1%. A burst integral metric combined the extent and timing of bursting and revealed apparently substantial variation among accessions. Mean pollen tube length was shorter at 34 C than at 26 C in 72% of accessions and was equal or greater at 34 C in the remaining 28%. Individual-tube tracking revealed contrasting growth-speed distributions in representative thermosensitive and thermotolerant accessions, including persistence of faster-growing tubes in the thermotolerant Tamaulipas variety. This framework enables population-scale analysis of dynamic pollen traits and provides quantitative phenotypes for investigating the genetic basis of pollen thermotolerance.

</details>

### [Arabidopsis histone demethylase RSI1/FLD self-regulates its pathogen-induced expression](https://www.biorxiv.org/content/10.64898/2026.11.19.767995v1)
*Singh, U.; Patil, V.; Kumar, R. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.19.767995 v1 · relevance 0.05

- **In one sentence**: In Arabidopsis, the histone demethylase RSI1/FLD, which is needed for systemic acquired resistance, appears to dampen its own pathogen-induced expression by removing H3K4me2/me3 marks near its own transcription start site, with GSTT2 required for that induction.
- **In plain words**: When a plant is attacked by a microbe, it can switch on a whole-plant defense called systemic acquired resistance, which protects leaves that were not infected too. This paper studies a plant gene, RSI1/FLD, that is needed for that defense and that is itself switched on by infection. The authors found that the gene seems to switch itself off again, which they suggest keeps the defense response at a moderate level.
- **Why it matters**: The work points to a self-limiting feedback loop that may help explain how plants keep immune responses from running too strong. The text is a short summary, so the mechanism is described only at the level of the reported experiments, and its wider importance for plant immunity is not established here.
- **Background needed**: - Systemic acquired resistance (SAR): a plant-wide defense triggered by a local infection, protecting distant tissues.
- Histone: the protein spool around which plant DNA is wrapped; chemical marks on histones affect whether nearby genes are read.
- H3K4me2 and H3K4me3: methyl tags on histone H3 that are generally linked to genes being active; removing them (demethylation) tends to repress genes.
- Histone demethylase: an enzyme that removes these methyl tags.
- Transcription start site (TSS): the point where reading of a gene begins.
- ChIP (chromatin immunoprecipitation): a lab method to find which DNA regions a protein or chemical mark sits on.
- GUS reporter assay: a method that links a gene's control region to an easily measured enzyme to gauge how active it is.
- rsi1 mutant: a plant lacking a working RSI1 gene, used to test its role. · level: research-level

<details><summary>Original abstract</summary>

REDUCED SYSTEMIC IMMUNITY 1(RSI1)/FLOWERING LOCUS D (FLD) is essential for the activation of systemic acquired resistance (SAR). RSI1 functions as a repressor of gene expression by demethylating H3K4me2 and H3K4me3. RSI1 expression is induced both in local and systemic tissues upon pathogen inoculation. However, the mechanism of its induction or its expression regulation upon pathogenesis is not known. Here we show that RSI1 expression in SAR-induced rsi1 mutant plants is higher than WT plants, suggesting self-regulation. Pathogen-induced expression of RSI1 requires the function of GSTT2, a SANT domain-containing protein essential for SAR activation. Co-expression of RSI1 suppresses pRSI1:GUS activity in a transient assay system. Chromatin-immunoprecipitation (ChIP) experiments reveal that RSI1 physically associates near the transcription start site (TSS) of the RSI1 locus and facilitates demethylation of H3K4me2 and H3K4me3 at RSI1 locus. Our data altogether demonstrate that RSI1 negatively regulates its own expression as a possible mechanism of keep the SAR expression at an optimal level.

</details>

## Bioengineering and synthetic biology

### [EEG Source Localization with High-Resolution 40-Tissue Head Models: A Comparative Study with MEG during Photic Driving](https://www.biorxiv.org/content/10.64898/2026.11.20.768219v1)
*Nunez Ponasso, G.; Drumm, D. A.; Oppermann, H. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.20.768219 v1 · relevance 0.06

- **In one sentence**: The paper presents an EEG source-localization pipeline that uses 40-tissue, AI-segmented head models computed with a fast boundary element method, and compares results against 5-layer models and simultaneous MEG during photic (light-flash) driving.
- **In plain words**: Brain-activity recordings from EEG (electrodes on the scalp) and MEG (magnetic sensors near the head) must be mapped back to their likely sources in the brain, which depends on a computer model of the head. This study builds much more detailed head models with 40 separate tissue types, generated automatically from scans, and tests them on six people who were shown flickering light. The authors report that the detailed and simpler models gave very similar EEG source estimates, and both agreed reasonably well with MEG in the visual cortex.
- **Why it matters**: Standard EEG analysis usually assumes only a few layers of head tissue, while this work tests whether finer detail changes results in practice, which matters for patients or infants whose heads do not fit simple layered models. The text reports the agreement with MEG and the linear link to source orientation, but its practical benefit beyond these six participants is not yet shown.
- **Background needed**: - EEG records electrical potentials from scalp electrodes; MEG records the magnetic fields from the same brain currents.
- Source localization estimates where in the brain the signals come from, using a "forward model" of how currents produce signals at the sensors.
- Head models split the head into tissues (scalp, skull, brain, etc.) with assigned electrical conductivities; simpler models use 3 to 5 nested layers.
- Boundary element methods (BEM) compute electric fields on the surfaces between tissues; the "fast multipole" variant speeds this up.
- Photic driving: the brain's rhythm is entrained by flickering light at a set frequency, here half the person's alpha peak (about 8–12 Hz in typical adults).
- Source orientation (the direction of the current dipole) matters in fixed-orientation models.
- Results are from six participants and a single workstation; the text gives no broader clinical validation. · level: research-level

<details><summary>Original abstract</summary>

While MEG source localization pipelines often employ head models of one single compartment with homogeneous conductivity, researchers and clinicians use at least 3 different layers in head models for EEG source localization. Recent AI-based segmentation makes it possible to generate individualized head models with 40 high-resolution, non-nested tissues. We present a pipeline that can make use of, and test, these highly realistic models for EEG source localization: with the boundary element fast multipole method (BEM-FMM), we compute transcranial electric stimulation (TES) solutions on the full 40-tissue geometry and use them reciprocally to obtain the EEG leadfields. Out approach runs on a single modest workstation, requiring approximately 4.5 min per EEG channel for a mesh of about one million elements at a relative residual of 1e-4. We applied the pipeline to six participants undergoing intermittent photic stimulation at half their individual alpha peak frequency, comparing 61-channel EEG source localizations from 40-tissue and 5-layer models with each other and with localizations from simultaneously recorded MEG. We further compared noiseless synthetic EEG topographies of the two models across the entire cortex. The two models produced highly consistent EEG source localizations (weighed relative difference below 3%), both in close agreement with the MEG localizations within the visual cortex. The synthetic topographies also agreed closely, with differences scaling approximately linearly with the angle between the source orientations of the two models, underscoring the importance of accurate source normals in fixed-orientation source models. These results establish 40-tissue models as a practical and robust basis for EEG source localization, and open the way to applications where nested geometries cannot represent the anatomy, such as infants or patients with skull defects, injuries, or tumors.

</details>

### [Synthesis of Plasma Membrane-Enriched Nanodiscs from Giant Plasma Membrane Vesicles](https://www.biorxiv.org/content/10.64898/2026.11.20.768238v1)
*Jacobs, C. O.; Santee, R. R. S.; Pizarro Carbajal, B. S. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.20.768238 v1 · relevance 0.05

- **In one sentence**: The paper reports a method for making plasma-membrane-enriched nanodiscs (PMNDs) from giant plasma membrane vesicles (GPMVs), which retain functional membrane proteins and bind specifically to cells expressing a matching receptor.
- **In plain words**: Cells are wrapped in an outer skin called the plasma membrane, which holds many proteins that do useful jobs. Getting a clean sample of this skin is hard, because it makes up only a small part of the membrane material in a cell. The authors describe a way to build tiny disc-shaped pieces of this skin, starting from large bubbles of membrane (GPMVs), and report that these discs keep a working membrane protein and stick specifically to cells carrying the matching receptor.</plain>
<parameter name="why">Keeping membrane proteins in their natural fatty surroundings is useful for studying how they work and how particles or drugs might target cells. The text suggests possible uses in nanomaterial targeting and vaccine development, but these are proposed directions, not demonstrated results.
- **Background needed**: - Plasma membrane: the outer boundary of a cell, studded with proteins that receive signals and move substances.
- Membrane proteins: proteins embedded in fatty membranes; many are drug targets.
- Nanodisc: a small, flat disc of lipid bilayer held together by a scaffold, used to hold membrane proteins in a stable, soluble form.
- GPMVs (giant plasma membrane vesicles): large bubbles that cells release when their membrane is chemically treated, carrying the native surface proteins.
- Specific, dose-dependent binding: the discs stick to target cells more strongly as more discs are added, and only to cells with the matching receptor.
- The text is a short abstract; methods details and quantitative results are not included here. · level: research-level

<details><summary>Original abstract</summary>

Nanodiscs are highly versatile biomaterials with applications in cell membrane mimicry, membrane protein (MP) characterization, and hybrid biological-abiological material synthesis. The plasma membrane (PM) is an ideal starting material for nanodisc synthesis because it naturally houses a diverse array of functionally important MPs in their native lipid environment. However, the PM comprises a small fraction of the total membrane material in a typical eukaryotic cell. Traditional methods to isolate the PM suffer from undefined relative PM enrichment compared to other cellular membranous structures. Here, we introduce a method to synthesize PM-enriched nanodiscs (PMNDs) from giant plasma membrane vesicles (GPMVs). We show that GPMV-derived PMNDs retain functional membrane-anchored protein, exhibit uniform size and morphology, and bind specifically and dose-dependently to the PM of cells expressing a cognate receptor. This strategy offers broad applicability for synthesizing nanodiscs with novel MPs for investigating PM-nanomaterial interactions, cellular targeting, and vaccine development using immunologic MPs.

</details>

## Mathematical biology (arXiv)

### [Classical visual illusions in vision-language models under an instruction ladder](https://arxiv.org/abs/2611.27242)
*Eiji Watanabe* · `q-bio.NC` · arXiv:2611.27242v1 · relevance 0.04

- **In one sentence**: A controlled study of 25 classical visual illusions, each drawn in illusion, reversed, and control versions, tests how vision-language models answer under graded instructions, separating stimulus-driven illusion effects from memory of famous figures.
- **In plain words**: Image-reading AI models often name the illusory answer when shown a famous optical illusion, which raises the question of whether they are actually seeing the picture or just recalling the illusion's name. The authors drew 300 new illusion images and asked two Claude models, with thinking on and off, about them under eight levels of instruction, from a false claim up to giving the true answer. When asked for the physical fact, the models almost never gave the illusion answer, but when asked how the picture looks, the illusion answer kept returning even after the truth was given.
- **Why it matters**: It offers a way to tell whether a model's error comes from the image or from memorised knowledge, which matters for judging how far model outputs can be trusted on visual tasks. The released stimuli and code could also be reused for tests with other models or human observers, though the text reports results for only two models from one family.
- **Background needed**: - Vision-language model (VLM): an AI system that takes both images and text and answers questions about them.
- Visual illusion: a picture where the brain (or here, a model) perceives something that does not match the physical facts, such as lines that look bent but are straight.
- Control and reversed images: versions with the inducing elements removed or reversed, used to check whether an answer depends on the actual picture.
- Instruction ladder: a series of prompts of increasing explicitness, from a misleading false claim to telling the model the illusion's name and the true answer.
- Confidence interval: a range that likely contains the true value; here, 74–96% for one reported measure.
- Position preference: a bias toward picking the first or second option regardless of content, which the design cancels out. · level: intermediate

<details><summary>Original abstract</summary>

Vision-language models (VLMs) often name the "illusory" answer when shown a classical visual illusion, but it is unclear whether that answer comes from the picture or from knowledge about famous figures. We drew 300 new stimuli of 25 classical illusions in three conditions--the illusion, the illusion with its inducing elements reversed, and a control with the inducing elements removed--and asked about each image at eight rungs of an instruction ladder that runs from a false fact, through a neutral question and an instruction to report the physical truth, to telling the model the name of the illusion and finally the true answer. Claude Sonnet 5.5 and Claude Haiku 5.5, with thinking off and on, gave 460,800 answers. When asked for the physical fact, all four settings almost never gave the illusion answer, and they resolved real 10% differences in the same displays. When asked how the picture looks, the illusion answers returned, and they did not vanish after the true answer was stated. Two measures that cancel position preferences and recognition of the figure suggest that much of this depends on the stimulus: among side answers, Sonnet with thinking chose the illusion side in 85% of cases after being told the truth (95% CI 74--96%), with 16 of the 25 illusions showing a stimulus-driven effect. Yet for five figures--the Fraser spiral, Kanizsa triangle, Pinna--Brelstaff rings, Ouchi pattern and, for Haiku, the rotating snakes--the models gave the illusion answer to the control images as well, which suggests that they answered from the figure rather than from the effect. A false fact was mostly followed on control images but not on illusion images. The stimuli, prompts, all responses and the code are released for testing further models; the Python code that draws the stimuli is parametric and can generate new illusion images for other studies with models or human observers.

</details>

### [Causal Event Networks: Entangled Tensor Graphs, Connectome Quotient Topology, and Subjective Experience as Geometric Dual](https://arxiv.org/abs/2611.26646)
*Vahid R. Ramezani* · `q-bio.NC` · arXiv:2611.26646v1 · relevance 0.04

- **In one sentence**: The paper builds sparse recurrent graphs with a chromatic (graph-coloring) bound on sequential execution phases, coarsens them to the scale of the Budapest Reference Connectome, and compares their topology and spectral, controllability and clique measures to the real connectome, then tests one graph as a deep-feature module in a U-Net for image inpainting, ending with a conjectural holographic account of subjective experience.
- **In plain words**: The paper proposes a way to generate large networks of computing units connected by one-way message channels, where a coloring rule keeps the number of sequential processing steps fixed however large the network grows. The authors then shrink one such network to the size of a published map of a fruit-fly-scale brain wiring diagram (the Budapest Reference Connectome) and report how closely its shape matches the real wiring under a range of tests. They also plug one version into an image-repair network and report that it improves inpainting over a standard convolutional baseline, and they close with a speculative theory linking the graph to subjective experience.
- **Background needed**: - Graph: a set of nodes (units) joined by edges (connections); "sparse" means few edges relative to possible ones.
- Connectome: the map of connections between neurons or brain regions.
- Coarsening: grouping many nodes into fewer "community" nodes, like zooming out on a map.
- Chromatic number/graph coloring: the minimum number of colors so that no two connected nodes share one; here used to bound sequential steps.
- Tensor product: a standard way of combining two structures into a larger one.
- Spectral measures: properties derived from the eigenvalues of a graph's connection matrix.
- Controllability: how well inputs can steer the network's state.
- U-Net: an encoder-decoder neural network often used for image tasks such as inpainting (filling in missing pixels).
- Holographic duality: a physics idea where a description on a boundary encodes a description in a higher-dimensional bulk; used here only as an analogy. · level: research-level

<details><summary>Original abstract</summary>

We introduce a chromatically constrained tensor-product construction that generates sparse recurrent computational graphs whose coloring bounds the number of sequential execution phases: vertices are computational units, edges are causal message-passing channels, and the graph can grow arbitrarily large while its chromatic causal depth stays fixed. Coarsened to the scale of the Budapest Reference Connectome, the community quotient of a simple local construction reproduces the connectome's broad degree profile, passes a nine-criterion topological test and comes close to the connectome on most of a further battery of complexity, spectral, controllability and clique measures, while the fine parent graph shows a scale separation: multiscale organization is intrinsic to the fine graph, and short-path integration appears only under coarsening. Placing short-path integration directly in the fine substrate, with chromatically admissible bridges and targeted sparsification, yields quotients far less modular than the connectome across a wide range of coarsening schemes. Relocating edges into the interiors of quotient nodes instead produces a quotient that matches the connectome's degree profile, edge count and fiber-bundle distribution, passes the full nine-criterion test and comes close on most complexity and spectral measures; its fine substrate fails only the two near-random path criteria. Used as the deep-feature pathway of a U-Net encoder-decoder, the graph-derived recurrent module improves image inpainting over the convolutional baseline. We close with a conjectural, structural account of subjective experience in holographic terms: the graph acts as an evolution operator that fixes the admissible causal order and the geometries the substrate can support, and experience occupies the position of the bulk dual of a particular activity state.

</details>

## Epidemiology

### [Epidemiology of Cardiac Structure and Function Among African Caribbeans in Tobago: A Population-based Cohort Study](https://www.medrxiv.org/content/10.64898/2026.11.18.26368418v1)
*Deb Nath, N.; Miljkovic, I.; Katz, R. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.18.26368418 v1 · relevance 0.07

- **In one sentence**: A population-based cohort study of 924 African Caribbean adults in Tobago reporting echocardiographic prevalence of left ventricular remodeling, diastolic dysfunction, and reduced strain, stratified by sex, age, and heart failure stage.
- **In plain words**: Heart failure is a serious condition in which the heart cannot pump blood as well as it should, and people of African descent are known to be at higher risk. This study looked at heart ultrasound scans from 924 adults in Tobago, an island in the Caribbean, to see how common early heart changes were. It found that most participants had some thickening of the heart's main pumping chamber, and that these changes were more common in women and in older adults.
- **Why it matters**: Little was previously known about heart structure and function in this Afro-Caribbean population, so the descriptive data may help local public health planning. The text does not show how these findings compare with other groups or whether they predict later heart failure, so its wider significance is uncertain.
- **Background needed**: - Heart failure: the heart's pumping ability is weakened; it often follows earlier changes in heart shape and function.
- Echocardiography: an ultrasound scan of the heart, used to measure its size, wall thickness, and pumping.
- Left ventricular (LV) mass index and geometry: measures of how thick and large the heart's main chamber is; "concentric remodeling" means thickened walls without much enlargement.
- Diastolic dysfunction: the heart's filling phase is stiff or impaired; E/e' ratio is one marker of this.
- Ejection fraction (LVEF): the share of blood pumped out per beat; below 50% is considered reduced.
- Global longitudinal strain (GLS): a measure of how much the heart muscle squeezes along its length; the study used -18% as the abnormal cutoff.
- Heart failure stages A to C: A is at risk without symptoms or structural change, B is structural change without symptoms, C is symptomatic.
- Population-based cohort: a study of a defined community rather than a clinic group, where participants were followed or sampled as part of a general population. · level: intermediate

<details><summary>Original abstract</summary>

Background: Individuals of African genetic ancestry are at high risk for heart failure (HF), which is often preceded by cardiac structural and functional abnormalities. Nevertheless, little is known about cardiac structure and function among Afro-Caribbeans residing in Tobago. This study aimed to investigate the epidemiology of cardiac structure and function among African Caribbeans in Tobago. Methods: A total of 924 participants (41-83 years) underwent clinical evaluation and transthoracic echocardiography. Images were analyzed for left ventricular (LV) mass index (MI), left atrial volume index, diastolic dysfunction (DD), LV ejection fraction (LVEF), global longitudinal strain (GLS), E/e' ratio, E/A ratio, and other echocardiographic measures. Cardiac structure and function were evaluated by age, sex, and HF stage. Results: The mean age was 61.7 years, with 61.4% women, 47.8% obesity, and 20.2% diabetes. Average systolic blood pressure was approximately 140 mmHg, and 76.7% had hypertension. Abnormal LV geometry was present in 77.1% of participants, predominantly concentric remodeling (69.5%). The prevalence of DD was 13.4%, LVEF <50% was 1.5%, and abnormal GLS ([&le;]-18%) was 5.2%. Women had significantly higher E/e' ratios and a higher prevalence of Stage A and Stage B HF, whereas men had a higher prevalence of symptomatic (Stage C) HF. Participants aged 65-83 years had significantly higher E/e' ratio, concentric remodeling, and LV hypertrophy than those aged 41-57 years. Conclusions: Women and older adults have higher LV structural abnormalities and DD than men and younger adults. These results will be helpful to inform public health priorities related to cardiovascular health in Tobago.

</details>

### [Improving UK Biobank algorithms for Parkinson's disease ascertainment using drug claims](https://www.medrxiv.org/content/10.64898/2026.11.18.26368409v1)
*Kimmerling, V.; Jaber, E.; Proust-Lima, C. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.18.26368409 v1 · relevance 0.06

- **In one sentence**: Compares three ways of identifying Parkinson's disease cases in UK Biobank (hospital/death records, GP diagnoses, and a new drug-prescription-based algorithm) and how each choice changes incidence estimates and associations with sex, walking speed and mortality.
- **In plain words**: Researchers using the UK Biobank, a large health database of volunteers, need to work out who has Parkinson's disease, a brain condition that slowly affects movement. This paper compares three ways of finding those cases, including one that looks at which Parkinson's drugs people were prescribed. The authors found that the hospital-and-death-records method missed about 20% of cases that the drug-based method found and underestimated incidence by 36% against UK reference rates.
- **Why it matters**: How a disease is identified in a large database can change the conclusions drawn about risk factors and death rates, so this matters for anyone relying on UK Biobank for Parkinson's research. The authors suggest combining several data sources; the text does not show how widely such changes would be adopted.
- **Background needed**: - UK Biobank: a large research database of UK volunteers with health records linked to hospital, death and (for about 45% of people) primary care data.
- Ascertainment: working out which people have a condition, here from coded records rather than direct examination.
- Misclassification: labelling people wrongly, or missing true cases, which biases results.
- Incidence: how many new cases appear in a population over time.
- Parkinsonism: a group of movement symptoms that can have causes other than Parkinson's disease, so some people may be wrongly counted.
- Anti-PD drugs: medicines such as levodopa used to treat Parkinson's; a prescription can indicate a diagnosis before it is recorded elsewhere. · level: research-level

<details><summary>Original abstract</summary>

Background: Accurate ascertainment of Parkinson's disease (PD) is a major challenge in large-scale epidemiological studies. The UK Biobank (UKB) is widely used for PD research, but ascertainment based on hospital and death records may result in misclassification and delayed PD diagnoses. Objectives: We compared different strategies for ascertaining PD in the UKB, and examined their impact on incidence and associations with risk factors and mortality. Methods: We compared PD ascertained through hospital and death records (ADO-PD) to two approaches that rely on primary care data available for ~45% of participants: diagnoses from general practitioner consultations (Clinical-PD); a novel drug-based algorithm (Drug-PD). We compared incidence, age at diagnosis, and associations with sex, walking speed, and mortality across all algorithms. Results: ADO-PD identified ~20% fewer prevalent and incident cases than Drug-PD over 15y of follow-up, and estimated age at diagnosis to be 4.2y (median) later than age at anti-PD drugs initiation. ADO-PD identified never treated participants or with other causes of parkinsonism as PD patients. While Drug-PD yielded incidence rates consistent with UK reference rates, ADO-PD underestimated incidence by 36% compared to reference rates. Associations with sex, walking speed, and mortality were significantly different for ADO-PD compared to Drug-PD. Clinical-PD and Drug-PD yielded similar findings, although Clinical-PD included patients with other causes of parkinsonism. Conclusions: We draw attention to methodological issues regarding PD ascertainment in the UKB and their consequences. These results can help inform strategies for PD ascertainment by combining multiple data sources, thereby improving the validity of epidemiological analyses.

</details>

## Infectious diseases

Nothing notable this time.

## Public and global health

### [Partitioning lifespan inequality in hierarchical study designs with an application to global healthy longevity](https://www.medrxiv.org/content/10.64898/2026.11.22.26368689v1)
*Caswell, H.* · `public and global health` · medRxiv doi:10.64898/2026.11.22.26368689 v1 · relevance 0.08

- **In one sentence**: The paper proposes a variance-partitioning method for hierarchical study designs, splitting lifespan inequality into between-region, between-country-within-region, and within-country components, and applies it to global healthy longevity data from 194 countries.
- **In plain words**: People differ in how long they live for two reasons: some groups have different death rates, and chance alone makes individuals in the same group die at different ages. This paper offers a way to split the total spread in lifespans into pieces that match how the data are nested, such as countries within regions. The authors apply it to healthy-longevity estimates for 194 countries and report that most of the spread lies within countries rather than between them.
- **Why it matters**: Health inequality is usually discussed as a gap between rich and poor countries, and this work suggests that most of the variation sits inside countries instead. The method may be useful for other nested datasets, such as regions within states, though the text does not show how it performs beyond this application.
- **Background needed**: - Lifespan inequality: how widely individual ages at death vary, here measured by variance (a standard measure of spread).
- Mixture distribution: treating a population as a blend of several subgroups, each with its own pattern of deaths.
- Hierarchical design: data nested in layers, such as countries inside regions.
- Partitioning variance: splitting total variation into separate parts that add up to the whole.
- Healthy longevity: a measure of expected years lived in good health, here drawn from the Global Burden of Disease study.
- Flat versus population-weighted mixing: whether each country counts equally or in proportion to its population when combining them.
- The paper reports that within-country chance variation makes up 85% to 95% of total inequality; the text gives no further detail on how this was estimated. · level: research-level

<details><summary>Original abstract</summary>

Background: Demographic inequality arises from two sources: heterogeneity among individuals subject to different rates, and stochastic variation among individuals subject to identical rates. Partitioning lifespan inequality into these components has been limited to heterogeneity in single factors or, very recently, factorial study designs with multiple factors. Methods for hierarchical designs have been lacking. Objectives: The goal of this paper is to present a generally applicable method to partition inequality of lifespan (and other demographic outcomes) into components within and between levels in a hierarchical study design. Methods: The analysis treats a heterogeneous population as a mixture distribution. Inequality is measured by the variance and partitioned into components between groups (e.g., geographical or economic regions), between sub-groups within groups (e.g., countries within regions), and stochasticity within sub-groups. The method is applied to global inequality in healthy longevity, using data for 194 countries from the Global Burden of Disease study, divided into four regions according to the World Bank income categories and into countries within each region. Results are compared for flat and population-weighted mixing distributions. Results: The protocol for variance partitioning in hierarchical study designs provides variance among regions, among countries within regions, and within countries. It extends naturally to multiple levels (e.g., states within countries) and to factorial components (e.g., regions defined by combinations of income and education). When applied to global healthy longevity, the dominant source of inequality is stochastic variation within countries, which accounts for 85\%-95\% of the overall inequality. The population-weighted mixing distribution reduces the contribution of between-group variance. Contribution: Some of the largest demographic data sets have a hierarchical organization. The methods presented here make it possible to partition inequality, measured by variance, in such studies.

</details>

### [Monitoring SNAP and Food Insecurity After the One Big Beautiful Bill Act: Early Evidence from a National Longitudinal Cohort](https://www.medrxiv.org/content/10.64898/2026.11.19.26368514v1)
*Robertson, M.; Sanborn, J.; Penrose, K. et al.* · `health policy` · medRxiv doi:10.64898/2026.11.19.26368514 v1 · relevance 0.05

- **In one sentence**: An early longitudinal cohort study of 844 low-income U.S. adults (household income under 200% of the federal poverty guideline) tracking SNAP receipt and food insecurity from August 2025 to March 2026, comparing states that did and did not yet enforce the expanded work requirement under the One Big Beautiful Bill Act.
- **In plain words**: In July 2025, a new U.S. federal law tightened eligibility for the food assistance program SNAP (formerly called food stamps) and expanded its work requirements. This study followed a national group of lower-income adults from August 2025 to March 2026 to see how many still got SNAP and how many struggled to afford food. SNAP receipt dropped slightly, from 40.4% to 38.4%, while the share screening positive for food insecurity (not always having enough food) rose from 48.1% to 51.2%.
- **Why it matters**: It offers early, real-time evidence on what happens to people when food aid is cut back, at a time when the government is scaling back its own tracking of food insecurity. The authors report that people who left SNAP were about as food insecure as those who stayed, which suggests need did not disappear with the benefit. Because the study is early and its sample is modest, the findings should be read as preliminary.
- **Background needed**: - SNAP: the U.S. federal program that helps low-income households buy food, often through an electronic benefit card.
- Work requirement: a condition that certain adults work or train a set number of hours to keep benefits; the law expanded who must meet it.
- Recertification: periodic re-checking of eligibility to keep receiving benefits.
- Food insecurity: limited or uncertain access to enough food because of money or resource problems; "screening positive" means a short questionnaire flagged it.
- Federal poverty guideline: the income threshold the government uses to define poverty; 200% means twice that amount.
- Longitudinal cohort: the same group of people is surveyed repeatedly over time, so changes within individuals can be tracked.
- Staggered state implementation: states started enforcing the new rule at different times, which the authors used as a comparison. · level: intermediate

<details><summary>Original abstract</summary>

The One Big Beautiful Bill Act (OBBBA), signed in July 2025, restricted eligibility for the Supplemental Nutrition Assistance Program (SNAP) and expanded its work requirement, while federal tracking of food insecurity was scaled back. Using a national, community-based longitudinal cohort, we examined changes in SNAP receipt and food insecurity between August 2025 and March 2026 among 844 adults with household income below 200% of the federal poverty guideline, comparing participants in states that had and had not begun enforcing the expanded work requirement. SNAP receipt fell from 40.4% to 38.4%, and the share screening positive for food insecurity rose from 48.1% to 51.2%, with no detectable difference by state implementation timing. Adults who discontinued SNAP were as likely to be food insecure (71.1% in March 2026) and as worried about affording food, housing, and utilities as those who continued SNAP, and few had moved above 200% of the poverty guideline. These early findings suggest that need persisted after SNAP ended. As enforcement expands, policy makers should consider measures that keep benefits flowing to eligible people, such as extended certification periods and simplified recertification, and should support longitudinal monitoring of food insecurity.

</details>

## Psychiatry and neurology

### [Geographic heterogeneity of gut microbiome biomarkers across neurological conditions: sub-national discordance in ten cohorts from eleven cities in six countries](https://www.medrxiv.org/content/10.64898/2026.11.19.26368539v1)
*Tello Meryk, J.* · `neurology` · medRxiv doi:10.64898/2026.11.19.26368539 v1 · relevance 0.13

- **In one sentence**: Reprocessing ten public 16S rRNA gut-microbiome cohorts (Alzheimer's, Parkinson's, autism; 1,185 samples, eleven cities, six countries) shows that classifiers and discriminant taxa do not transfer between cohorts, even between recruitment centers in the same city.
- **In plain words**: Researchers have linked gut bacteria to brain conditions such as Alzheimer's, Parkinson's and autism, and some have proposed bacterial patterns as diagnostic markers. This paper re-analysed ten existing public studies from eleven cities to test whether those patterns hold up in other populations. They mostly do not: a pattern that works within one study drops to close to chance when applied to another.
- **Why it matters**: It bears directly on whether gut-microbiome tests could ever be used as diagnostic markers, and it suggests that the problem is not only distance between countries, since cities within one country also failed to transfer. The text does not establish the causes of this variation (for example, differences in sampling, diet or lab methods), so those explanations remain open.
- **Background needed**: - The gut microbiome is the community of bacteria living in the intestine; 16S rRNA sequencing is a common, relatively inexpensive way to identify which bacterial groups are present.
- A "biomarker" here means a pattern of bacteria that can help sort people into groups (for example, patients versus healthy controls).
- AUC (area under the curve) measures how well a classifier separates two groups: 0.5 is chance, 1.0 is perfect.
- "Transfer" means training a model on one cohort and testing it on a different cohort, which is the real test of whether a pattern generalizes.
- A cohort is a study group of participants recruited and sampled under defined conditions.
- Public-data reanalysis means the authors reprocessed raw data from earlier studies using one common pipeline rather than collecting new samples. · level: research-level

<details><summary>Original abstract</summary>

Gut microbiota composition has been associated with multiple neurological conditions, and candidate biomarkers have been proposed on the basis of these associations. Their usefulness presupposes that taxa altered in one population are also altered in others, a condition that is rarely verified. This work quantifies the extent to which it holds, and the geographic scale at which it ceases to do so. Ten public 16S rRNA gene sequencing cohorts of Alzheimer's disease, Parkinson's disease and autism spectrum disorder, collected in eleven cities across six countries, were reprocessed from raw data, comprising 1,185 samples with uniform processing within each condition. Models trained and evaluated within a single cohort reached a mean AUC of 0.751 in Alzheimer's disease, 0.741 in autism spectrum disorder and 0.673 in Parkinson's disease. When applied to a different population, these values fell to 0.569, 0.542 and 0.551 respectively. The decline was not associated with geographic distance: transfer between cities within the same country was equivalent to transfer between continents. No taxon appeared among the twenty most important features in all cohorts of a given condition, and no correlation between rankings reached significance. Classifiers trained to predict cohort of origin, disregarding clinical group, reached AUC values of 0.87 to 1.00 using control subjects, and equivalent values using affected subjects. In one cohort with two recruitment centers and a single protocol, controls from both cities were separable (AUC 0.947), models did not transfer between centers (0.562 and 0.515), and their rankings correlated 0.003. Geographic heterogeneity of discriminant taxa operates below the national scale, which constrains the generalization of microbiome signatures derived from individual cohorts.

</details>

### [Remote auditory task performance, cognition, and APOE4 across two dementia-risk cohorts](https://www.medrxiv.org/content/10.64898/2026.11.19.26368469v1)
*Happs, C.; Toma, A.; Koychev, I. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.19.26368469 v1 · relevance 0.07

- **In one sentence**: Two independent cohorts (older Great Minds register, n=164; mid-life PREVENT, n=90) completed the same remote auditory battery, and the paper finds no APOE ε4 association but modest links between auditory performance and memory in the older group only.
- **In plain words**: Hearing speech in background noise is linked to later memory and dementia risk, so researchers want simple online hearing tests that might flag problems early. This study ran a set of remote listening and memory-related tasks in two groups of people, one older and one middle-aged, and checked them against a common gene linked to Alzheimer's risk. The gene carrier status did not track with any hearing task in either group.
- **Why it matters**: Remote tests that can be done at home could make it cheaper to screen many people for early cognitive change, which is a practical goal. The result is modest: auditory performance related to one memory test in the older group only, and the authors note the samples may have been too small to rule out small gene effects.
- **Background needed**: - APOE ε4: a gene variant that is the strongest common genetic risk factor for Alzheimer's disease.
- Digits-in-noise and speech-in-babble: tests where people repeat numbers or words heard against background sound; they measure how well speech is understood in noise.
- Working-memory precision: how accurately someone holds and recalls a sound (tone frequency or loudness rhythm) in mind.
- Robust regression with false-discovery-rate (FDR) correction: statistical methods that reduce false positives when many tests are run.
- Cohort: a group of people followed over time for research.
- Paired-associate learning and spatial-memory tasks: standard tests of learning word pairs and navigating locations.
- Cross-sectional design: data are from a single time point, so cause and effect cannot be established. · level: intermediate

<details><summary>Original abstract</summary>

Background. Difficulty hearing speech in noise is associated with cognitive ageing and dementia risk. It is unclear whether performance on remote auditory tasks reflects the apolipoprotein E (APOE) {epsilon}4 allele, the strongest common genetic risk factor for Alzheimers disease, or broader cognitive and ageing processes. Methods. We analysed two independent cohorts: the Great Minds research register of older adults and the mid-life PREVENT Dementia programme. Both completed the same remote auditory battery: digits-in-noise, speech-in-babble, auditory working-memory precision for tone frequency and for amplitude-modulation rate, and the Goldsmiths Musical Sophistication Index. Cognitive outcomes were paired-associate learning in Great Minds, and the Four Mountains Task, Supermarket Task and selected COGNITO scores in PREVENT. Associations were tested with covariate-adjusted robust regression and false-discovery-rate (FDR) correction. Results. The analytic samples comprised 164 Great Minds and 90 PREVENT participants (mean age 70.6 vs 56.8 years). APOE {epsilon}4 carrier status was not associated with any auditory measure in either cohort (all FDR-corrected p>0.70). In Great Minds, better speech-in-babble performance and better amplitude-modulation-rate working-memory precision were each associated with better paired-associate learning (both FDR-corrected p=0.019). In PREVENT, no auditory measure was associated with spatial-memory or COGNITO scores after age and sex adjustment and FDR correction. Conclusions. Remote auditory task performance was associated with memory in the older cohort but not with APOE {epsilon}4 carrier status in either cohort, although the samples could not exclude small genotype effects. Longitudinal studies are needed to determine whether remote auditory testing predicts cognitive change.

</details>

## Oncology

### [Circulating miRNA profiling identifies hsa-miR-23a-3p and a three-miRNA signature associated with serous ovarian cancer](https://www.medrxiv.org/content/10.64898/2026.11.18.26368404v1)
*Garcia-Llorens, G.; Tierno-Martin, A.; Serra, A. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.18.26368404 v1 · relevance 0.03

- **In one sentence**: A small case-control study of plasma miRNAs in serous ovarian cancer finds hsa-miR-23a-3p lower in patients (AUC 0.755), with a three-miRNA model whose advantage shrinks under repeated cross-validation (mean AUC 0.716).
- **In plain words**: Ovarian cancer is often found late, so doctors want simple blood tests that could spot it earlier. This study looked at tiny genetic messengers called microRNAs in the blood of 47 women with ovarian cancer and 47 women without it. One of them, miR-23a-3p, was present at lower levels in the cancer patients and separated the two groups moderately well.
- **Why it matters**: A blood-based marker for ovarian cancer would be useful because the disease is usually detected late and is highly lethal. The authors are cautious: the result is moderate, the groups were unevenly sourced, and the combined model did not hold up well when tested internally, so it needs independent validation before any clinical use.
- **Background needed**: - Ovarian cancer: the most common deadly gynecologic cancer; high-grade serous is its most lethal subtype.
- Liquid biopsy: detecting disease from a blood sample rather than tissue.
- microRNAs (miRNAs): short RNA molecules that regulate genes; they circulate in blood and can be measured.
- RT-qPCR: a lab method that measures how much of a specific RNA is present.
- ROC curve / AUC: a way to measure how well a test separates two groups; 0.5 is chance, 1.0 is perfect.
- Sensitivity and specificity: the share of sick people correctly flagged and the share of healthy people correctly cleared.
- Cross-validation: repeatedly splitting data to test whether a model works on unseen samples, guarding against overfitting.
- Pre-analytical variability: differences introduced before measurement, such as how samples were collected and stored. · level: research-level

<details><summary>Original abstract</summary>

High-grade serous ovarian carcinoma (HGSOC) is the most lethal subtype of epithelial ovarian cancer, highlighting the need for minimally invasive biomarkers that support disease detection and molecular characterization. Circulating microRNAs (miRNAs) have emerged as promising candidates, although their clinical applicability remains limited by methodological variability and insufficient validation. Plasma samples from 100 individuals (50 patients with ovarian cancer and 50 cancer-free controls) were initially collected from four biobanks. Following quality control, 94 samples (47 patients and 47 controls) were included in the final analysis. Eight candidate miRNAs were quantified using RT-qPCR, and relative expression was assessed following global mean normalization. Differential expression was evaluated using the Wilcoxon rank-sum test, while discriminatory performance was assessed using receiver operating characteristic (ROC) curve analysis. Three-miRNA logistic regression models were additionally explored using repeated stratified five-fold cross-validation. Among the eight candidates, hsa-miR-23a-3p exhibited significantly lower circulating expression in patients with ovarian cancer than in controls (p = 2.14 x 10-5), achieving an area under the ROC curve (AUC) of 0.755 (95% CI, 0.657-0.852), with 93.6% sensitivity and 53.2% specificity at the selected threshold. Exploratory analysis across FIGO stages revealed heterogeneous expression patterns, although the limited number of early-stage cases precluded definitive conclusions regarding stage-specific performance. A three-miRNA signature comprising hsa-miR-23a-3p, hsa-miR-21-5p, and hsa-miR-20a-5p achieved an apparent AUC of 0.798. However, repeated cross-validation yielded a mean AUC of 0.716 {+/-} 0.022, indicating reduced performance after internal validation. Variability in exogenous spike-in Ct values and the marked imbalance in biobank representation between study groups highlighted potential pre-analytical confounding. Circulating hsa-miR-23a-3p showed moderate discriminatory performance between patients with ovarian cancer and cancer-free controls, supporting its further investigation as a candidate liquid biopsy biomarker. Although combining three miRNAs improved apparent classification performance, this advantage was not established through internal validation. These findings underscore the importance of accounting for sample provenance, technical variability, and model overfitting when evaluating circulating miRNA signatures. Independent validation in appropriately balanced cohorts is required before clinical applicability can be established.

</details>

## Health informatics and medical AI

### [Task-specific fine-tuning versus frontier large language models for RoB 2 risk of bias assessment: development and external benchmark evaluation of RoB-BERT](https://www.medrxiv.org/content/10.64898/2026.11.19.26368519v1)
*Pitre, T.; Mah, J.; Azlan, A. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.19.26368519 v1 · relevance 0.08

- **In one sentence**: A paper describing RoB-BERT, a model fine-tuned for RoB 2 risk-of-bias assessment of randomized trials, benchmarked against three frontier LLMs and against agreement between human assessors on 419 published judgements.
- **In plain words**: Medical reviewers grade how trustworthy each randomized trial is, using a standard checklist called RoB 2. This paper builds a specialised AI tool, RoB-BERT, to do that grading and compares it with three large general-purpose AI models and with human graders. The tool agreed with published human judgements about as often as two humans agreed with each other, and was roughly on par with or better than the general models at a much lower cost.
- **Why it matters**: Trial bias grading is slow and labour-intensive in systematic reviews, so a cheap and consistent automated rater could matter for evidence synthesis. The paper also reports that human graders agree with each other only modestly, which bears on how such ratings are produced; the agreement figures are modest, though, and the reference standard is a single published judgement rather than expert consensus, so the claims should be read cautiously.
- **Background needed**: - Randomized controlled trials are studies that assign people to treatments at random; their results can be biased by how they were run.
- Risk of bias (RoB 2) is a standard tool in which reviewers answer 22 signalling questions across five bias domains, then rate each domain and the overall trial as low risk, some concerns, or high risk.
- Systematic reviews combine many trials, so the quality grading of each trial matters.
- Large language models (LLMs) are general AI text systems; "fine-tuning" means further training a model on a specific task.
- Cohen's kappa measures agreement beyond what chance would produce; values near 0 are weak and near 1 strong.
- Sensitivity is the share of true high-risk cases caught; specificity is the share of low-risk cases correctly passed.
- Overall agreement figures are low for all raters, and the reference judgements are single published ratings, not expert-verified truth. · level: research-level

<details><summary>Original abstract</summary>

Background: Researchers increasingly use large language models (LLMs) to assess risk of bias in randomized trials, but how task-specific fine-tuned models compare with frontier models remains uncertain. Objective: To develop RoB-BERT, a fine-tuned RoB 2 assessment system, and to compare its agreement with human assessments against that of three frontier LLMs. Methods: RoB 2 rates five bias domains and the trial overall as low risk, some concerns or high risk, based on answers to 22 signalling questions. RoB-BERT answers each question, quotes the supporting sentences from the trial report, and applies the official RoB 2 algorithm. We trained RoB-BERT on 5,304 reviewer-checked assessments, none from a test trial, and compared it with Claude Fable 5.1, GPT-6 Astra and Gemini 4 Argon, each given identical prompts and text, against 419 published human assessments (ROBoto2, LogiMed-RoB and Cochrane reviews) made without AI assistance. Each reference was the single published judgement for that trial, made by one assessor or agreed by two, rather than an expert reference standard, so we also report agreement between two human assessors of the same trial. Results: In ROBoto2, pairs of human assessors who rated the same trial agreed on 61.2% to 64.7% of domain judgements ({kappa} 0.15 to 0.35) and 46.2% to 50.0% of overall judgements ({kappa} 0.15 to 0.17); across the 185 ROBoto2 trials, RoB-BERT agreed with the human judgement on 67.4% ({kappa} 0.35) and 53.5% ({kappa} 0.20). Across all 419 assessments, domain agreement was 67.9% ({kappa} 0.29) for RoB-BERT, 65.0% ({kappa} 0.24) for Claude Fable 5.1, 52.7% ({kappa} 0.21) for GPT-6 Astra and 66.7% ({kappa} 0.26) for Gemini 4 Argon; overall agreement was 46.1% ({kappa} 0.16), 47.3% ({kappa} 0.17), 31.0% ({kappa} 0.03) and 46.5% ({kappa} 0.14), respectively. For domains the reference rated high risk, sensitivity was 22.2% for RoB-BERT, 23.1% for Claude Fable 5.1, 41.9% for GPT-6 Astra and 24.8% for Gemini 4 Argon, with specificity of 92.5%, 92.8%, 80.0% and 95.0%. On the 52 ROBoto2 trials rated by two assessors, the second assessor's sensitivity for the reference assessor's high-risk domains was 23.1% (specificity 90.3%) and RoB-BERT's was 30.8% (specificity 92.7%). RoB-BERT located 95.7% of its quotations verbatim in the report and cost US$0.005 per trial, 2% to 6% of the frontier models' cost. Conclusions: RoB-BERT agreed with single human assessors at least as closely as two human assessors agreed with each other, and matched or exceeded frontier LLMs at a fraction of their cost. The results show the poor reliability of human assessors using RoB 2 and the need for consensus ratings, with RoB-BERT potentially serving as one rater.

</details>

### [What Does an Agent-Run Clinic Cost? Protocol for a Prospective Observational Study of the Compute Cost of Completed Work in a Clinical Agent Fleet](https://www.medrxiv.org/content/10.64898/2026.11.19.26368538v1)
*Elalfy, O.; Youssef, S.; Davids, J.* · `health informatics` · medRxiv doi:10.64898/2026.11.19.26368538 v1 · relevance 0.07

- **In one sentence**: A protocol for a prospective observational study that will estimate the compute cost of completed work by a deployed multi-agent LLM system in a London outpatient clinic, using estimators, data-quality gates and a pre-fixed analysis plan.
- **In plain words**: This is a plan for measuring how much computing cost it takes for AI agents to finish real clinic tasks, such as writing up documentation and supporting decisions, over a 12-week period. The authors describe how they will count finished work, handle retries and failed attempts, and report missing or imperfect records. No results are reported yet; the data collection had not started when the paper was submitted.
- **Why it matters**: Deciding whether to use AI agents in health care depends on what finished work actually costs in practice, not only on list prices or benchmark scores. The paper may matter as a template for how deployed systems could report this, but its usefulness will depend on the results, which are not yet available.
- **Background needed**: - LLM agent: a large language model that carries out multi-step tasks by calling tools and other models, often in a pipeline.
- Compute cost: the money paid to model providers for processing requests, measured here in GBP pence.
- Telemetry: automatically logged records of system activity, such as each run's start and end.
- Retry and failure: a task that is attempted again or does not finish; these add cost without producing usable output.
- Protocol / pre-registration: a plan written and publicly registered before data are analysed, to limit choices made after seeing results.
- Bootstrap interval: a way of estimating uncertainty by resampling the data, here over weeks.
- Small-cell suppression: hiding counts that are too small to report safely, for privacy. · level: intermediate

<details><summary>Original abstract</summary>

Background: Decisions about deploying large language model (LLM) agents in health care require the cost of completed work in production. Published evidence reports benchmark accuracy, benchmark-level cost, and time or financial outcomes for ambient documentation, and list prices alone do not determine the cost of completed work. To our knowledge, no deployed clinical agent fleet has published a measurement method that ties compute cost, latency, failures and retries to completed work. Objective: This study aims to estimate the compute cost of completed work by the orchestrated clinical agents of a deployed LLM agent fleet over a 12-week window of production telemetry, using estimators, data-quality gates and an analysis plan fixed before any window data are extracted for the study. Methods: The setting is a private outpatient clinic in London, United Kingdom, where wai, a multi-agent system supporting clinic operations, is deployed. The population is every run of the 20 orchestrated clinical documentation and decision-support agents starting between September 21 and December 13, 2026. The run store writes 2 records for every run, a non-terminal record before the model call and a terminal record after it, and has no attempt counter or parent-run link. Estimators defined on that structure cover cost per resolved execution and per completed intention, retry and failed-intention shares of compute, error and failure rates, latency, cost per draft offered for clinician review and a latency-cost frontier, by agent, task class and acceptance stratum. Cost is recorded in GBP pence, converted from provider-returned US dollar cost at a fixed rate and rounded per model call. The plan fixes weekly aggregation, small-cell suppression, bootstrap intervals over weeks, 2 prespecified comparisons, 5 sensitivity analyses and 4 data-quality gates whose failure converts an estimate into a bound or an unmeasured stratum. Two staff-level measures in an earlier version were dropped. Revenue, pricing, margin and staffing inference are excluded. Results: The measurement window opened on September 21, 2026, and closes on December 13, 2026, and telemetry is being recorded in routine operation. No window data had been extracted for this study at submission. Aggregate whole-table counts that include window records were extracted on November 19, 2026, for companion manuscripts and are disclosed. Extraction will begin no earlier than December 15, 2026, and the results are expected to be submitted for publication in 2027. Conclusions: The compute cost of completed clinical agent work can be specified as estimators over the run-level telemetry this deployment records, provided paired recording rows are separated from retries, missing terminal states are bounded and rounding of recorded cost is reported. This protocol fixes those estimators, and the reporting consequence of each known instrumentation defect, before extraction. Trial Registration: None. The analysis plan will be registered on Open Science Framework Registries before any window data are extracted for this study.

</details>

## Econometrics and applied economics

### [The Rural Margin of Territorial Peace: Within-Municipality Evidence from Colombia](https://arxiv.org/abs/2611.26882)
*Hector Galindo-Silva* · `econ.GN` · arXiv:2611.26882v1 · relevance 0.03

- **In one sentence**: A triple-difference event study using repeated Social Capital Barometer waves finds that rural-urban engagement gaps narrowed in Colombian municipalities covered by both the peace agreement's participatory development programs and conflict-victim congressional seats, with the clearest evidence on coordination around shared problems.
- **In plain words**: After Colombia's 2016 peace agreement, the government added local participatory development programs and reserved congressional seats for conflict victims in rural areas. This paper asks whether people in rural parts of municipalities that got both reforms became more engaged in civic life, compared with rural parts of other municipalities and with urban areas. The author reports that rural engagement improved relative to urban engagement in the covered areas, most clearly in how well people coordinate around shared problems.
- **Why it matters**: Most work on post-conflict politics measures engagement through voting, so a change in civic life beyond the ballot is a useful addition. It may connect to research on how peace reforms and local participation can rebuild trust and organization in regions that suffered violence, though the text does not test those links directly.
- **Background needed**: - Peace agreement: Colombia's 2016 accord between the government and the FARC guerrilla group, which included rural development and political inclusion measures.
- Participatory development programs: local initiatives where residents help decide on public projects.
- Congressional constituencies for conflict victims: seats set aside so that people affected by the armed conflict have representation.
- Social Capital Barometer: a survey run in repeated waves, used here to track civic engagement over time.
- Event study: compares outcomes before and after a policy, against areas that did not receive it.
- Triple difference: adds a third comparison (here, rural versus urban) on top of a standard before-and-after, treated-versus-untreated comparison, to net out general trends.
- Engagement index: a combined score of coordination, civic participation and party ties. · level: research-level

<details><summary>Original abstract</summary>

Colombia's peace agreement introduced participatory development programs and congressional constituencies reserved for conflict victims with a rural electorate. I use repeated waves of the Social Capital Barometer and a triple-difference event study to compare changes in rural-urban engagement gaps in municipalities covered by both reforms with those elsewhere. Rural engagement evolved more favorably relative to urban engagement in the covered municipalities. The index captures coordination around shared problems, civic participation and party linkage, with coordination providing the clearest evidence. The result persists when the reference period precedes the agreement and the baseline wave is excluded. Program activity and organizational membership patterns are consistent with participatory investment and political mobilization. The findings document a change in engagement beyond voting under the joint territorial reforms.

</details>

## Economic theory

Nothing notable this time.

## Game theory and algorithmic economics

### [Epistemic Social Learning: Latent Behavioral Structure under Endogenous Multi-Agent Interaction](https://arxiv.org/abs/2611.27545)
*Jainendra Shukla, Dhruv Jaiswal, Divyanshi Beniwal et al.* · `cs.MA` · arXiv:2611.27545v1 · relevance 0.09

- **In one sentence**: Proposes Epistemic Social Learning (ESL), which couples fast per-interaction Bayesian beliefs about opponents with slower online learning of population-shared behavioral prototypes, and evaluates it on twelve synthetic 3x3 games against other online latent-adaptation methods.
- **In plain words**: When you play a repeated game against other agents, what you do changes what you get to see of them, so your picture of their behavior depends on your own choices. This paper proposes a learning method that keeps a quick, per-game guess about each opponent and also slowly learns a shared set of typical behavior patterns across a population. On twelve simulated small games, the authors report that it had the lowest total regret after opponents switched strategies, compared with the other online methods they tested.
- **Why it matters**: The paper makes a point that a model can predict observed behavior well yet still adapt poorly when opponents change, because the learner's own actions shape what it observes. This matters for any setting where learning and acting feed back on each other, such as multi-agent AI or economic modeling, though the evidence here is limited to synthetic games and its wider relevance is unclear.
- **Background needed**: - Game theory: a small game (here 3x3) is a setting where each player picks one of three actions and payoffs depend on everyone's choices.
- Regret: how much worse an approach did compared with the best fixed choice in hindsight; "post-switch regret" measures this after an opponent changes behavior.
- Bayesian belief: a running probability estimate about hidden facts (here, an opponent's strategy), updated as new observations arrive.
- Stochastic approximation: a standard mathematical framework for analyzing learning rules updated step by step with noisy data.
- Endogenous interaction: the data a learner sees depends on the learner's own actions, which complicates standard learning analysis.
- Prototypes: representative patterns summarizing typical behavior across many agents. · level: research-level

<details><summary>Original abstract</summary>

In multi-agent interaction, a learner's actions shape the observations from which it infers other agents' behavior. A behavioral model may predict these observations well yet support poor adaptation when opponents change. We introduce Epistemic Social Learning (ESL), which couples fast, interaction-specific Bayesian beliefs with slower online learning of population-shared behavioral prototypes. Belief-conditioned decisions influence subsequent observations and, in turn, the representations learned from them. Under explicit regularity and averaging assumptions, we provide a conditional stochastic-approximation characterization of these coupled dynamics. Across twelve synthetic $3\times3$ cooperative, coordination, and adversarial games, ESL achieves the lowest aggregate post-switch regret among the evaluated online latent-adaptation methods, including a switch-aware Bayesian filter. Additional experiments examine observation loss, noise, and asymmetric incentives. These findings illustrate how predictive fit can differ from decision-relevant adaptation under policy-dependent interaction.

</details>

### [Incentive Compatible Mechanisms for Sequential Fair Resource Allocation with Private Demands](https://arxiv.org/abs/2611.26800)
*Ramtin Salamat, Sean R. Sinclair, Seyed M. R. Iravani* · `cs.GT` · arXiv:2611.26800v1 · relevance 0.06

- **In one sentence**: The paper studies a strategic version of online fair resource allocation where agents privately know their demands and may misreport them, characterizes incentive-compatible allocation rules, identifies conditions for a simple cap-structured optimal mechanism, and approximates the optimum via a longest-path reduction on a directed acyclic graph.
- **In plain words**: A planner has to hand out a divisible resource over several rounds to people whose needs only they know. Since no money changes hands, people may exaggerate or understate their needs to get more, so the paper designs allocation rules that make honest reporting the best choice. The authors find conditions under which the best such rule is a simple capped one, and they give a computational method to approximate the optimal rule.
- **Why it matters**: Many nonprofit and public allocation settings (food, housing, or aid distribution) rely on self-reported need and cannot use payments to enforce honesty. The numerical experiments suggest that ignoring strategic behavior can be substantially costlier than designing for it, though the text does not show how broadly this applies.
- **Background needed**: - Fair allocation: splitting a shared, divisible resource among agents so that no one is treated unjustly.
- Online/sequential problem: decisions are made stage by stage, without knowing future demands.
- Mechanism design: designing the rules of a process so that participants' self-interest leads to a desired outcome.
- Incentive compatibility (IC): a rule is IC if reporting your true demand is never worse for you than lying.
- Monetary transfers unavailable: the planner cannot use payments to discourage misreporting, so the rule itself must do the work.
- Dynamic programming: solving a multi-stage decision problem by working backward through possible states; here it is discretized.
- Longest-path problem on a directed acyclic graph: a standard graph problem used here as a computational reformulation of the optimization. · level: research-level

<details><summary>Original abstract</summary>

We study a strategic variant of the canonical online fair allocation problem, where a planner must sequentially allocate a divisible resource to agents with privately known demands. At each stage, the planner announces an allocation rule, the agent reports their demand, and the planner allocates resources according to the rule and the reported demand. Unlike the standard model, we allow agents to strategically misreport their needs, as can arise in nonprofit settings where demand is self-reported and monetary transfers are unavailable. We characterize the structure of incentive-compatible (IC) allocation rules in this model, and use this to identify conditions under which the optimal mechanism has a simple cap structure. We then develop an approximation method for the optimal IC mechanism through a careful reduction of the discretized dynamic program to a longest-path problem on a directed acyclic graph. Numerical experiments show that ignoring strategic reporting can be substantially more costly than imposing incentive compatibility.

</details>

## Mathematical finance

### [Reconstructing risk preferences from data](https://arxiv.org/abs/2611.27692)
*Anastasis Kratsios, Silvana M. Pesenti, Philipp Zimmermann* · `q-fin.RM` · arXiv:2611.27692v1 · relevance 0.06

- **In one sentence**: The paper gives necessary and sufficient conditions for a finite set of claim-price evaluations to come from a finite-valued, cash-additive, convex, Lipschitz risk measure, constructs a "universal risk measure" reconstruction for compatible data, extends this to monotone measures with sharp Lipschitz constants, and illustrates with Expected Shortfall and European options.
- **In plain words**: The paper asks how to infer a rule for measuring financial risk from a finite list of examples, where each example pairs a financial contract (a payoff that depends on an uncertain future) with the value someone assigned to it. It gives a test for when such a list could have come from a consistent risk rule, and a formula that builds one from the list when it could. The authors also show how the formula handles linear preferences and Expected Shortfall, and they close with a numerical example using European options.
- **Why it matters**: Regulators and firms often observe prices or capital requirements without knowing the rule behind them, so a principled way to recover that rule from data is of practical interest. The text does not indicate how the results have been applied outside the paper's own numerical example, so its broader impact is uncertain.
- **Background needed**: - Risk measure: a function that assigns a number (a capital requirement or risk level) to an uncertain payoff.
- Cash-additive: adding a sure amount of cash to a position changes its risk by exactly that amount.
- Convex: diversifying or mixing positions never increases risk beyond the average of the parts.
- Lipschitz continuous: small changes in the payoff cause only bounded, proportionally small changes in risk.
- Monotone: a payoff that is never worse in any scenario is never assigned higher risk.
- Contingent claim: a contract whose payoff depends on which scenario occurs, such as an option.
- Expected Shortfall: the average loss in the worst fraction of scenarios, a standard risk measure.
- Compatible dataset: a list of claims and values that could all be produced by one single risk measure. · level: research-level

<details><summary>Original abstract</summary>

We consider the problem of reconstructing risk preferences from data. Specifically, for a finite dataset consisting of contingent claims and their evaluations, we aim at reconstructing a risk measure that is finite-valued, cash-additive, convex, and Lipschitz continuous. Our first result establishes necessary and sufficient conditions for a dataset to be compatible with a risk measure, that is the evaluations are stemming from a risk measure applied to the contingent claims. Our second result provides a reconstruction formula for compatible datasets, which we term \emph{universal risk measure}. We further extend the reconstruction to monotone risk measures and establish sharp Lipschitz constants for both general and monotone reconstructions. We further show that we explicitly reconstruct linear preferences and evaluations by the Expected Shortfall. We conclude with a numerical application to European options.

</details>

### [Held-to-Maturity Accounting: Hidden Losses and Systemic Fragility](https://arxiv.org/abs/2611.26700)
*Dongxu Li, Steve Y. Yang* · `q-fin.RM` · arXiv:2611.26700v1 · relevance 0.04

- **In one sentence**: A theoretical model of how Held-to-Maturity accounting, which lets banks carry bonds at cost rather than market value, delays loss recognition and can amplify systemic risk through correlated asset exposures and interbank linkages.
- **In plain words**: The paper looks at what happens when banks are allowed to record their bonds at their original purchase price instead of today's market value, a practice called held-to-maturity accounting. This matters because rising interest rates pushed down the market value of many bonds, creating large unrecorded losses. The authors build a model in which banks are linked to each other through lending, and report that this accounting choice can let losses pile up hidden and then hit many banks at once when they are forced to sell under stress.
- **Why it matters**: The text suggests accounting rules are not neutral for financial stability, which bears on policy debates after the recent rise in bond-related losses at banks. The abstract gives only a qualitative account, so how large the effect is and how well it matches real data cannot be judged from this text alone.
- **Background needed**: - Held-to-maturity (HTM) accounting: banks can record certain bonds at their original cost, not their current market price, as long as they plan to hold them to repayment.
- Interest rate risk: when interest rates rise, existing bonds with lower fixed rates lose market value.
- Unrealized losses: losses on paper that are not booked until an asset is sold.
- Interbank network: the web of loans and obligations between banks, so one bank's failure can spread to others.
- Systemic risk: the chance that trouble at some institutions spreads across the whole financial system.
- Correlated exposures: many banks holding similar assets, so they are hit by the same shocks together.
- Nonlinear: small changes in conditions can produce disproportionately large changes in outcomes. · level: research-level

<details><summary>Original abstract</summary>

This paper studies how accounting-induced opacity affects systemic risk in the banking system. Motivated by the buildup of unrealized losses during recent monetary tightening episodes, we develop a model in which banks hold correlated interest rate sensitive assets and are connected through an endogenous interbank network. We show that Held-To-Maturity (HTM) accounting amplifies systemic risk by delaying loss recognition, allowing losses to accumulate and become synchronized across institutions. When losses are realized under liquidity stress, the interaction of correlated exposures and network linkages generates nonlinear increases in defaults. These findings suggest that accounting regimes are not neutral from a financial stability perspective, as they influence both the buildup and propagation of systemic risk, particularly in environments with common asset exposures and strong interconnectedness.

</details>

## Financial markets

Nothing notable this time.

## Signal processing

### [Graph-XGB: A Hybrid GNN Framework for Outdoor-to-Indoor 5G Signal Reconstruction via Aerial-Only UAV RF Sensing](https://arxiv.org/abs/2611.26828)
*David Hason Rudd, Eunkwang Shin, Nithiwat Pattrapong et al.* · `cs.LG` · arXiv:2611.26828v1 · relevance 0.05

- **In one sentence**: Graph-XGB combines a modified graph neural network (SpiderGNN), PCA compression, and per-target XGBoost regressors to predict indoor 5G signal strength (RSSI, RSRP) from UAV measurements taken only outside a 10-floor building, with interference-dependent metrics (RSRQ, SNR, CQI) predicted less accurately.</one_liner>
<parameter name="plain">Mobile phone signals often weaken badly when they pass through building walls, so indoor coverage is hard to plan. This paper uses drones flying outside a building to estimate the signal strength inside it, without taking any indoor measurements as model inputs. The authors report that their method predicts two signal-strength measures (RSSI and RSRP) better than a simpler baseline, while predicting measures affected by interference less reliably.</plain>
<why>Planning indoor 5G and future 6G coverage without sending people inside to measure is a practical problem for operators, and the paper's use of outdoor-only drone data is the distinctive part. The text reports results on one building's dataset of 613 nodes, so how well it generalizes to other buildings is not shown here.</why>
<background>
- Outdoor-to-indoor (O2I) attenuation: signal loss as radio waves pass through exterior walls, which grows at higher frequencies (mid-band, mmWave, sub-THz).
- UAV (drone) RF sensing: using drones to carry radio receivers and record signal levels.
- RSSI, RSRP, RSRQ, SNR, CQI: standard 5G/LTE signal-quality measures (received power, reference-signal power, reference-signal quality, signal-to-noise ratio, channel quality index).
- Graph neural network (GNN): a model that passes information between connected points in a graph, here locations in a building.
- PCA (principal component analysis): a method that compresses many features into fewer ones while keeping most of the variation.
- XGBoost: a gradient-boosted decision-tree regression method.
- R²: a score for how well predictions match measured values; 1 is perfect, 0 is no better than the average.
</background>
<difficulty>research-level</difficulty>
</invoke>

<details><summary>Original abstract</summary>

Delivering robust In-Building Coverage (IBC) is critically impeded by severe Outdoor-to-Indoor (O2I) attenuation, a constraint that intensifies as deployments move from 5G mid-band towards mmWave and prospective 6G sub-THz carriers, where losses of 60-80 dB have been reported across modern building envelopes. While Unmanned Aerial Vehicles (UAVs) offer scalable exterior RF sensing platforms, a fundamental inversion problem persists: interior 3D signal states cannot be directly sampled from constrained exterior flight paths. This paper proposes Graph-XGB, a hybrid inference framework that decouples spatial topology reasoning from non-linear signal regression to resolve this challenge. A modified SpiderGNN encoder, operating on a topology-aware graph constructed with a physically grounded Floor-Aware 3D Distance metric and Bridge Edge Guarantees, propagates UAV boundary measurements into 128-dimensional indoor embeddings. Principal Component Analysis (PCA) compresses these into a 10-dimensional manifold retaining 96.6% of embedding variance, fused with raw spatial features and decoded by independent, physics-tailored XGBoost regressors. This decoupling mitigates the optimization conflict between smoothly decaying path-loss signals and volatile interference-dependent metrics. Evaluated on a real-world 5G NR dataset of 613 verified nodes spanning the 10 floors of a single building, Graph-XGB attains the strongest accuracy among the architectures compared, with $R^2$ of 0.759 (RSSI) and 0.770 (RSRP), improvements of 35.5% and 64.9% over the SimpleGNN baseline, using no interior RF measurement as a model input; indoor observations enter only as training supervision, with evaluation on held-out internal nodes. Interference-dependent targets (RSRQ, SNR and CQI) remain bounded well below the path-loss metrics, delimiting the reach of purely spatial inference.

</details>

### [On the Complete Feature Set for ADHD Classification in Children and Adolescents Based on EEG Signals](https://arxiv.org/abs/2611.27970)
*Javier Sanchis, \'Alvaro Navarro, Jorge Garc\'ia-Carrasco et al.* · `cs.LG` · arXiv:2611.27970v1 · relevance 0.05

- **In one sentence**: A curated, quality-documented EEG dataset from 156 children and adolescents with and without ADHD, released with 115 precomputed feature definitions across seven feature families on shared time windows, plus a descriptive participant-held-out classification example.
- **In plain words**: This paper describes a shared collection of brain-wave (EEG) recordings from young people, some of whom have ADHD, made while they did attention-related tasks. The authors cleaned and aligned the recordings so that different kinds of measurements can be compared fairly on the same time segments, and they noted the quality checks they made along the way. They also show a simple example of predicting group membership from the measurements, but say these results do not show that the tests can diagnose ADHD.
- **Why it matters**: Many EEG studies of ADHD use different preprocessing and time windows, which makes results hard to compare; a common, documented dataset could make those comparisons more consistent. Its value depends on how well the released files are used, and the text itself does not claim it will change clinical practice.
- **Background needed**: - EEG (electroencephalography): recording electrical activity from the scalp using electrodes.
- ADHD: a neurodevelopmental condition affecting attention, activity level and impulse control.
- Feature: a numerical summary computed from a signal, such as power in a frequency band.
- Feature family: a group of related measurement types (seven are compared here).
- Preprocessing and artefacts: cleaning steps, and unwanted signals such as eye movement or muscle noise.
- Participant-held-out evaluation: testing a model on people it never saw during training, so the same person does not appear in both sets.
- XGBoost: a common machine-learning method that combines many decision trees.
- Repeated measures: several recordings from the same person, which must be handled carefully in analysis.
- Diagnostic validity: whether a test reliably identifies who has a condition; the paper states this is not established. · level: research-level

<details><summary>Original abstract</summary>

Attention-deficit/hyperactivity disorder is a neurodevelopmental condition that can affect attention, activity and impulse control. Electroencephalography (EEG) records brain activity as children and adolescents perform cognitive tasks. However, comparing features derived from these recordings requires consistent signal preparation, shared analysis windows and documented quality decisions. We curated 669 existing BALLADEER recordings from 156 participants across five task conditions so that researchers can compare seven EEG feature families on the same time intervals for each participant and task. The dataset links continuous signals to precomputed measurements from 115 feature definitions or templates and records the quality decisions made for each recording. Analyses must still account for repeated measurements within participants, residual artefacts and differences between acquisition systems. Technical validation covered signal integrity, numerical checks on feature estimators and completeness of the released files. In every task, the median proportion of recording time retained after preprocessing was 100%. To illustrate reuse, we report saved participant-held-out evaluations comparing XGBoost using all seven families on eight-second windows with a predictor based only on recruitment-group prevalence in the training fold. Recruitment-group discrimination was stronger in Robots than in the three Slackline conditions. These descriptive results from overlapping cohorts do not establish diagnostic validity. The dataset, curation software and aggregate results for the predictive example are publicly available.

</details>

## Audio and speech

### [Bird-Call Recognition Across Distance: Acoustic Degradation and BirdNET Performance](https://arxiv.org/abs/2611.26757)
*Hasmik Gharibyan, Bhaskar Krishnamachari* · `eess.AS` · arXiv:2611.26757v1 · relevance 0.06

- **In one sentence**: Controlled playback of 20 bird species at seven distances (1 to 48 ft) tests how a STM32-based recorder and the BirdNET classifier hold up as calls degrade, reporting top-1 accuracy and median upper spectral edge trends.
- **In plain words**: This study asks how well a computer program can still tell which bird species is calling when the sound has travelled farther. The researchers played back ten-second bird calls from 20 species at distances from about 1 to 48 feet, recorded them with a small custom device, and ran the recordings through the BirdNET identification tool. They found accuracy stayed high up to 24 feet, dropped somewhat at 36 feet, and fell further at 48 feet, while the high-frequency part of the sound became weaker as distance grew.
- **Why it matters**: Automated bird monitoring often relies on recordings made at unknown distances, so knowing where recognition starts to fail helps set sensible limits on how such tools are used. The text does not say how the results would transfer to wild birds or other recording setups, so that link is uncertain.
- **Background needed**: - Spectral content: how a sound's energy is spread across pitches (frequencies); high-frequency detail is often lost over distance.
- Playback experiment: a recorded call is played through a speaker at set distances, so the original sound is known.
- BirdNET: an existing machine-learning program that identifies bird species from audio clips.
- Top-1 accuracy: the share of recordings where the program's single best guess is correct.
- Metadata configurations: different sets of extra information (such as location or date) supplied to the classifier; the text does not specify them.
- Mean-aggregated: results averaged across the four configurations. · level: intermediate

<details><summary>Original abstract</summary>

As bird calls weaken with distance, their recordings lose spectral detail. We examine how species recognition varies with distance using controlled playback of ten-second excerpts from 20 bird species at seven distances from 1 to 48 ft. An STM32-based recording system acquires and stores the audio, which is subsequently analyzed on a computer using acoustic measurements and BirdNET. Across four metadata configurations, mean-aggregated top-1 accuracy is 95--100% through 24 ft, 90--95% at 36 ft, and 80--90% at 48 ft, with 20 recordings evaluated per configuration at each distance. Across the screened recordings, the median upper spectral edge is below its 1-ft reference at every evaluated distance from 4 to 36 ft, indicating an overall reduction in upper-frequency content with distance. These results show that recognition remains high through 24 ft despite measurable spectral degradation, followed by greater and configuration-dependent losses at longer distances.

</details>

### [Impact of Edge Software Evolution on Audio Tagging Models: An Empirical Study on NVIDIA Jetson Orin Nano](https://arxiv.org/abs/2611.26831)
*Guillem Fustier-Castillo, Ruben Ribes-Serrano, Jordi Grau-Haro et al.* · `cs.SD` · arXiv:2611.26831v1 · relevance 0.05

- **In one sentence**: An empirical benchmark of PANNs (CNN and ResNet variants), AST and PaSST audio tagging models on an NVIDIA Jetson Orin Nano, comparing latency, energy, utilization and memory across JetPack 6.2 and JetPack 7.2 software stacks and several inference backends and power modes.
- **In plain words**: This paper asks whether the software a small edge computer runs on changes how fast and how efficiently sound-recognition AI models work. The authors ran several well-known audio models on one small NVIDIA board, once with the older software release (JetPack 6.2) and once with the newer one (JetPack 7.2). They report that the newer software cut time and energy use by more than 50% for some convolutional models when paired with TensorRT, while the Transformer-based AST model gained little and PaSST fell in between.
- **Why it matters**: Edge benchmarks are often reported as if the hardware alone determines speed, so a software update changing which model looks best is a useful caution for anyone choosing models for embedded deployment. The text does not show how broadly these results hold beyond this board and these software versions.
- **Background needed**: - Audio tagging: labeling which sound events (e.g., alarms, machinery, birdsong) occur in a recording.
- Edge deployment: running AI models on small, local devices instead of cloud servers.
- Latency and energy: how long one prediction takes and how much power it consumes.
- CNN vs. Transformer: two families of neural network architectures; CNNs use local filters, Transformers use attention across the whole input.
- PANNs, AST, PaSST: specific pretrained audio models of these two families.
- JetPack: NVIDIA's software bundle (drivers, libraries) for its Jetson embedded boards.
- TensorRT: NVIDIA's library that optimizes neural networks for faster inference on NVIDIA GPUs.
- Power modes: preset settings that trade performance against power draw on the device. · level: intermediate

<details><summary>Original abstract</summary>

Audio tagging is a fundamental task in machine listening, enabling the automatic identification of acoustic events in applications such as intelligent monitoring, industrial inspection, environmental sensing, and smart environments. As these applications increasingly migrate to edge platforms, deployment-oriented metrics such as latency, energy consumption, and resource utilization become critical alongside predictive performance. However, most existing studies evaluate audio tagging models under a single software environment, overlooking the potential impact of software stack evolution on deployment efficiency. This paper investigates how software ecosystem updates affect the execution characteristics of state-of-the-art audio tagging architectures on edge devices. We evaluate representative convolutional and Transformer-based models, including PANNs (CNN and ResNet variants), AST, and PaSST, on an NVIDIA Jetson Orin Nano platform using two generations of NVIDIA's software ecosystem: JetPack 6.2 and JetPack 7.2. Under identical hardware conditions, we analyze inference latency, energy consumption, CPU/GPU utilization, and memory footprint across multiple inference backends and power modes. The results show that software stack evolution can substantially affect deployment performance. JetPack 7.2 reduces latency and energy consumption by more than 50% for several convolutional architectures when combined with TensorRT, while significantly increasing GPU utilization. In contrast, AST exhibits only marginal gains, whereas PaSST shows intermediate behavior. These findings demonstrate that software evolution is a critical factor in Edge AI evaluation and can alter the relative deployment efficiency of competing architectures. Consequently, software stack versions should be explicitly considered when benchmarking and selecting audio tagging models for embedded deployment.

</details>

## Control systems

### [Connectivity-Constrained Linear System Realization: Feasibility and Realizable Sets](https://arxiv.org/abs/2611.26811)
*Yaozhi Du (Lisa), Jing Shuang (Lisa), Li* · `eess.SY` · arXiv:2611.26811v1 · relevance 0.08

- **In one sentence**: The paper studies which state-space realizations of a given transfer function fit an arbitrary prescribed connectivity pattern (support), solving the realization problem exactly via polynomial equations and characterizing which transfer functions a given pattern can realize, using algebraic geometry.
- **In plain words**: The paper asks how to build a simple internal model of a linear system, with its internal parts wired together only in a specified pattern of allowed connections. It shows this can be turned into a system of polynomial equations and solved exactly, without approximation. It also asks the reverse question, which input-output behaviors a given wiring pattern can produce, and reports that a pattern can either realize nearly all behaviors or very few.
- **Why it matters**: Most prior work on this kind of problem concerns networked plants, whereas this paper targets arbitrary connection patterns, which the text says matter for modeling in sensorimotor neuroscience. The text does not show how far the results have been applied beyond the examples given, so its practical reach is uncertain.
- **Background needed**: - Transfer function: a compact description of how a linear system turns inputs into outputs.
- State-space realization: an internal model with explicit state variables that reproduces a given transfer function.
- Connectivity pattern (support): which internal variables are allowed to influence which others; zeros in a matrix mean no connection.
- Structured/distributed control: control design where the controller's structure or communication is restricted.
- Multivariate polynomial equations: equations in several unknowns where each term is a product of powers of those unknowns.
- Algebraic geometry: the branch of mathematics that studies solution sets of polynomial equations and their shapes. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we first study the problem of finding a state-space realization of a given transfer function that adheres to a given connectivity pattern (i.e., support). While variants of this problem have been studied in distributed and structured control, existing work typically focuses on connectivity patterns relating to some networked plant. In contrast, we are interested in arbitrary connectivity patterns, which are relevant to modeling problems in sensorimotor neuroscience. We show that this problem is equivalent to solving a system of multivariate polynomial equations, and can be solved exactly without relaxation or approximation. We then study the reverse problem: given a connectivity pattern, what transfer functions have a state-space realization that adheres to this pattern? In other words, what transfer functions can this pattern realize? A surprising finding is that any given pattern can realize nearly all transfer functions, or very few transfer functions. We provide rigorous results and algorithms for both problems, leveraging technical machinery from algebraic geometry. The efficacy of our approach is demonstrated in examples at the end of the paper.

</details>

### [Active Learning of Flows from Curve Observations using Gaussian Processes](https://arxiv.org/abs/2611.27400)
*Konrad Reichel, Sandra Hirche* · `eess.SY` · arXiv:2611.27400v1 · relevance 0.06

- **In one sentence**: The paper proposes a local optimization method, using a Gaussian process model of an unknown control system, that plans the trajectory whose observation most reduces uncertainty about the system's flow, and reformulates the planning problem as a fixed end time optimal control problem via time rescaling.
- **In plain words**: Engineers often need to learn how a machine or system behaves by running it under chosen inputs, but each run is costly. This paper describes a way to pick the most useful input sequence to try, so that the recorded motion teaches the most about how the system responds. The authors also account for the fact that the real system may drift away from the planned path, and they test their planners on a numerical example against benchmark methods.
- **Why it matters**: Choosing informative experiments automatically can reduce the time and wear needed to identify a system, which matters for robotics and other real-world control. The text itself does not report how large the gains are, so the practical value is not established from this description alone.
- **Background needed**: - Control system: a system whose behavior (e.g., a robot arm) can be steered by inputs over time.
- Flow: the rule describing how the system's state evolves from a starting point under given inputs.
- Gaussian process: a statistical model that gives a predicted value plus an uncertainty estimate, learned from observed data.
- Active learning: choosing which data to collect next, rather than collecting it at random.
- Posterior kernel: the updated description of the model's uncertainty after data are observed.
- Pontryagin-type necessary condition: a standard calculus-of-variations rule that an optimal input must satisfy.
- Time rescaling: stretching or compressing time along a trajectory so a problem with variable duration becomes one with fixed duration. · level: research-level

<details><summary>Original abstract</summary>

The active learning of real control systems requires informative roll-outs of controls. In this paper, we present a local optimization algorithm that finds the trajectory that most reduces uncertainty about the flow of a control system modeled by a Gaussian process. Therefore, we derive an approximation scheme for the posterior kernel of the Gaussian process after observing it on an entire continuous-time trajectory and establish a Pontryagin-type necessary condition for the optimizer. As the flow is unknown, the actual trajectory can deviate from the planned trajectory. We propose a trajectory planner that searches for the most informative control within a maximal allowed deviation horizon instead of a fixed time horizon. We show by trajectory-wise time rescaling that the underlying optimal control problem is equivalent to a fixed end time optimal control problem. Finally, we study both the fixed end time planner and the fixed maximum deviation planner in a numerical example and compare them with benchmarks.

</details>

## Fetch statistics

| Topic | Fetched | New | Selected |
|---|---|---|---|
| Probability | 33 | 27 | 2 |
| Differential geometry | 20 | 18 | 2 |
| Partial differential equations | 57 | 52 | 2 |
| Harmonic analysis | 21 | 17 | 2 |
| Complex analysis | 12 | 9 | 2 |
| Operator algebras and spectral theory | 15 | 12 | 2 |
| Algebra | 29 | 24 | 2 |
| Representation theory | 19 | 16 | 2 |
| Number theory | 21 | 19 | 2 |
| Algebraic geometry | 24 | 17 | 2 |
| Topology | 13 | 11 | 2 |
| Dynamical systems | 17 | 14 | 2 |
| Combinatorics | 57 | 52 | 2 |
| Numerical analysis | 33 | 29 | 2 |
| Logic and foundations | 6 | 3 | 1 |
| Mathematical physics | 41 | 36 | 2 |
| Optimization and control | 36 | 30 | 2 |
| Statistics theory | 12 | 10 | 2 |
| Statistical methods and applications | 28 | 26 | 2 |
| AI industry news | 32 | 24 | 5 |
| Model architectures and training | 57 | 55 | 2 |
| Machine learning theory | 14 | 11 | 2 |
| Large language models | 58 | 53 | 2 |
| Computer vision | 132 | 130 | 2 |
| Reinforcement learning | 25 | 21 | 2 |
| AI safety and alignment | 30 | 23 | 2 |
| Interpretability | 7 | 5 | 2 |
| AI for mathematics | 9 | 6 | 2 |
| Robotics and embodied AI | 89 | 87 | 2 |
| Security and cryptography | 35 | 33 | 2 |
| Algorithms and complexity | 28 | 26 | 2 |
| Programming languages and formal methods | 19 | 16 | 2 |
| Systems and networking | 28 | 26 | 2 |
| Human-computer interaction | 14 | 12 | 2 |
| Information theory | 9 | 6 | 2 |
| High-energy theory and gravity | 48 | 42 | 2 |
| Statistical physics | 37 | 30 | 2 |
| Condensed matter | 52 | 49 | 2 |
| Particle physics | 45 | 43 | 2 |
| Nuclear physics | 16 | 14 | 2 |
| Quantum information and computing | 73 | 66 | 2 |
| Optics and atomic physics | 33 | 31 | 2 |
| Fluids and plasma | 22 | 19 | 2 |
| Biological physics | 3 | 2 | 0 |
| Climate, atmosphere and Earth | 5 | 3 | 0 |
| Cosmology | 12 | 9 | 2 |
| Galaxies | 29 | 24 | 2 |
| Exoplanets and planetary science | 13 | 8 | 2 |
| High-energy astrophysics | 19 | 13 | 2 |
| Stars and the Sun | 20 | 13 | 2 |
| Chemical physics | 12 | 6 | 2 |
| Materials science | 32 | 25 | 2 |
| Soft matter and polymers | 19 | 14 | 2 |
| AI for chemistry and materials | 17 | 8 | 2 |
| Biochemistry | 14 | 10 | 2 |
| Pharmacology and drug discovery | 3 | 3 | 0 |
| Computational and systems biology | 88 | 82 | 2 |
| Neuroscience | 69 | 64 | 2 |
| Genetics and genomics | 30 | 25 | 2 |
| Cell and molecular biology | 52 | 48 | 2 |
| Immunology and microbiology | 54 | 48 | 2 |
| Cancer biology | 26 | 22 | 2 |
| Ecology and evolution | 31 | 27 | 2 |
| Plant biology | 17 | 13 | 2 |
| Bioengineering and synthetic biology | 16 | 13 | 2 |
| Mathematical biology (arXiv) | 15 | 10 | 2 |
| Epidemiology | 18 | 14 | 2 |
| Infectious diseases | 3 | 1 | 0 |
| Public and global health | 10 | 6 | 2 |
| Psychiatry and neurology | 22 | 18 | 2 |
| Oncology | 6 | 3 | 1 |
| Health informatics and medical AI | 13 | 9 | 2 |
| Econometrics and applied economics | 4 | 1 | 1 |
| Economic theory | 3 | 1 | 0 |
| Game theory and algorithmic economics | 9 | 5 | 2 |
| Mathematical finance | 11 | 5 | 2 |
| Financial markets | 6 | 2 | 0 |
| Signal processing | 17 | 13 | 2 |
| Audio and speech | 8 | 4 | 2 |
| Control systems | 32 | 27 | 2 |

<!-- {% endraw %} -->
