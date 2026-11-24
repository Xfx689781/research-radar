# Research digest · 2026-11-24
<!-- {% raw %} -->

New papers posted from about 2026-11-23 to 2026-11-24 (UTC).

> Papers are picked by how closely their wording matches each topic's description (the "relevance" score), not by quality. Summaries are written by AI from the abstract only; open the paper before relying on them.

## Highlights

- **[Global well-posedness and scattering for the fractional inhomogeneous nonlinear Schrodinger equation with time-dependent damping](https://arxiv.org/abs/2611.28530)** (Partial differential equations): The paper studies a wave-type equation that describes how a quantum-style wave spreads out and can lose energy over time. It asks whether solutions exist for all time and eventually behave like free waves that no longer interact. The authors show this holds for solutions that are symmetric around a center (radial data), using a fairly direct argument.
- **[The Hamilton cycle space in the Erd\H{o}s--R\'enyi random graph process](https://arxiv.org/abs/2611.30619)** (Combinatorics): The paper studies a graph that grows by adding random edges one at a time, starting from no edges. It looks at the moment when every vertex has at least three edges, and shows that from that point on, with high probability, the closed loops that visit every vertex exactly once are rich enough to generate all the cycles of the graph under a simple "add or remove" rule. It also shows that the graph is then Hamilton-connected, meaning any two vertices can be joined by a path that passes through every vertex.
- **[Categorical Torelli theorem for quintic threefolds](https://arxiv.org/abs/2611.30760)** (Algebraic geometry): The paper studies a particular kind of shape studied in algebraic geometry: smooth quintic threefolds, which are high-dimensional surfaces cut out by fifth-degree polynomial equations. It asks whether the bookkeeping of sheaves on such a shape (a structured record of how functions and data sit on it) is enough to recover the shape itself. The authors show that if two such shapes have equivalent categories of sheaves, then the shapes are in fact the same up to isomorphism.

## Probability

### [Epidemic random model under vaccination regime and non-permanent immunity driven by time-changed Levy noise](https://arxiv.org/abs/2611.28254)
*Giulia Di Nunno, Jasmina Djordjevic, Nenad Suvak* · `math.PR` · arXiv:2611.28254v1 · relevance 0.18

- **In one sentence**: A stochastic SIRV epidemic model with waning (non-permanent) immunity and variable population size, where the contact rate is a random process driven by time-changed Lévy noise, is shown to have a unique positive global solution, a random basic reproduction number, and sufficient conditions for disease extinction and persistence in mean.
- **In plain words**: This paper studies how a contagious disease might spread in a population when the rate of contact between people fluctuates unpredictably over time. The model splits people into groups (susceptible, infected, recovered, and vaccinated), and immunity from infection or vaccination can wear off. The authors prove the model has a sensible, always-nonnegative solution and give conditions under which the disease dies out or lingers on average, expressed in terms of the model's parameters and two long-run measures.
- **Why it matters**: Real contact rates are rarely constant, so models that let them fluctuate randomly are a more realistic way to ask whether an outbreak will fade out. The text does not say how the results compare with data or other models, so their practical use is unclear from the summary alone.
- **Background needed**: - Compartmental epidemic models: populations split into Susceptible, Infected, Recovered, Vaccinated groups, linked by differential equations.
- Basic reproduction number: the average number of new infections caused by one case in a fully susceptible population; above a threshold the disease can spread.
- Non-permanent immunity: recovered or vaccinated people can become susceptible again after immunity wears off.
- Stochastic differential equations: equations with a random noise term, used for quantities that fluctuate unpredictably.
- Lévy noise: random fluctuations that can include both smooth wiggles (Brownian motion) and sudden jumps (Poisson-type events).
- Time change: running the randomness on a random clock, so activity can speed up or slow down.
- Extinction vs. persistence in mean: whether the disease dies out, or its average level stays above zero over the long run. · level: research-level

<details><summary>Original abstract</summary>

A random version of the Susceptible-Infected-Recovered-Vaccinated (SIRV) epidemic model with non-permanent immunity and a population of non-constant size is studied. The compartments satisfy a system of differential equations in which the contact rate is a random coefficient, and the contact rate itself is driven by a stochastic differential equation with time-changed Levy noise. This noise is constructed from a conditional Brownian motion and a doubly stochastic Poisson random field, both governed by a stochastic clock. When the clock is independent of the Brownian and Poisson components, the two parts of the noise are a time-changed Brownian motion and a time-changed Poisson random measure. The equation for the contact rate decouples from the compartment equations and enters them as a random parameter, which allows the compartments to be treated pathwise. The existence, uniqueness, and positivity of the global solution are proven, and the basic reproduction number of the model is shown to be random. Furthermore, sufficient conditions for extinction and persistence in mean of the disease are derived. The conditions are expressed in terms of the parameters of the model and two long-run characteristics.

</details>

### [Regularity of invariant measures of solutions for fractional stochastic partial differential equations with memory and nonlinear noise](https://arxiv.org/abs/2611.29406)
*Ran Li, Jiaohui Xu, Dingshi Li et al.* · `math.PR` · arXiv:2611.29406v1 · relevance 0.17

- **In one sentence**: Proves existence and regularity of invariant measures for stochastic fractional PDEs with memory and nonlinear multiplicative noise, using a Dafermos-type past-history variable to restore a Markov structure.
- **In plain words**: This paper studies random evolution equations that depend on both their past and random disturbances, the kind used to model materials or processes with memory. The authors recast the problem using a new variable that sums up the past history, which makes the system behave Markov-style, meaning the future depends only on the present state. Using that device, they show that long-run statistical equilibria (invariant measures) exist and that these equilibria have additional smoothness.
- **Why it matters**: Long-term behaviour of random systems with memory is hard to analyse because the usual Markov tools fail, so a workable reformulation is of interest to specialists in stochastic PDEs. The text does not discuss applications, so any connection to particular physical or engineering models is not stated here.
- **Background needed**: - Stochastic PDE: a partial differential equation driven by random noise.
- Fractional operator: a generalised derivative of non-integer order, used to model nonlocal or anomalous behaviour.
- Memory (non-Markovian) effect: the current evolution depends on the whole past, not just the present state.
- Multiplicative noise: the random disturbance's strength depends on the current state.
- Markov semigroup and invariant measure: the probability distribution a random system settles into and keeps over time.
- Dafermos method: a standard trick that replaces the past history with an auxiliary variable to remove memory.
- Galerkin approximation and Minty's technique: standard tools for proving well-posedness of nonlinear equations.
- Krylov-Bogoliubov approach: a classical way to construct invariant measures from time averages. · level: research-level

<details><summary>Original abstract</summary>

We are concerned with stochastic fractional partial differential equations involving memory and nonlinear multiplicative noise. Based on the well-known Dafermos method, a suitable variable defined by the integrated past history is introduced. This transformation not only overcomes the non-Markovianity of the original problem which prevents us from analyzing invariant measures for the associated Markov semigroup, but also facilitates the analysis of the well-posedness together with the Faedo-Galerkin approximations and Minty's technique. Moreover, we prove the existence of invariant measures by the classical Krylov-Bogoliubov approach, and further establish the regularity of invariant measures by virtue of a control argument.

</details>

## Differential geometry

### [Cylindrical Ricci flows and the PDE-ODI principle](https://arxiv.org/abs/2611.29246)
*Richard H. Bamler, Yi Lai* · `math.DG` · arXiv:2611.29246v1 · relevance 0.24

- **In one sentence**: The paper derives precise asymptotics for ancient asymptotically cylindrical Ricci flows, showing a linear-or-quadratic dichotomy in the leading deviation from the cylinder, and uses a PDE-ODI principle and a harmonic map heat flow gauge that works without a curvature sign assumption.
- **In plain words**: This paper studies how a curved shape evolving over time (a Ricci flow, which smooths out a geometric space much like heat spreads through metal) behaves when it looks like a long cylinder in the far past. The authors show that the first correction away from a perfect cylinder is either linear or quadratic in the stretched-out directions. In the linear case, the flow closely matches a known special shape (a Bryant soliton) times a flat Euclidean factor.
- **Why it matters**: The results are technical but structural: they give a unified treatment of Ricci flow and mean curvature flow via one shared principle, and the tools are said to be part of a program toward Ricci flow with surgery in dimension 4. The text does not claim wider consequences beyond this.
- **Background needed**: - Ricci flow: a process that deforms a geometric space over time, shrinking regions of high curvature; it is a central tool in the proof of the Poincaré conjecture.
- Ancient flow: a flow defined for all negative times, i.e. one studied looking backward into the far past.
- Asymptotically cylindrical: the shape looks more and more like a cylinder (a round tube times a line) as one goes back in time.
- Soliton: a special self-similar shape that evolves in a predictable way; a Bryant soliton is a particular steady-type example.
- Asymptotics: precise description of how a quantity behaves in a limit, here the leading correction terms.
- Mean curvature flow: a related geometric evolution of surfaces, whose cylindrical case the authors treated earlier.
- Harmonic map heat flow: a standard PDE tool used here as a coordinate (gauge) choice.
- Ricci flow with surgery: a method of continuing the flow past singularities by cutting and capping; the paper says these tools are aimed at this in dimension 4. · level: research-level

<details><summary>Original abstract</summary>

We derive precise asymptotics for ancient asymptotically cylindrical Ricci flows. We establish a dichotomy in which the leading deviation from the cylinder is either linear or quadratic in the axial variables. In the linear case, we show that the flow is exponentially asymptotic to a Bryant soliton times a Euclidean factor. For $\kappa$-solutions, we further show that the flow is isometric to such a product, up to parabolic rescaling. In the quadratic case, we obtain higher-order asymptotics governed by a finite-dimensional invariant. We also establish propagation of cylindrical regions and uniqueness of cylindrical tangent flows. These results closely parallel those in our earlier work on cylindrical mean curvature flows. Both analyses use the same PDE-ODI principle and yield a unified treatment of cylindrical Ricci flow and mean curvature flow. The essential new ingredient in the Ricci flow setting is a coherent harmonic map heat flow gauge, which allows us to apply this principle without assuming a sign for the curvature. The local analytic tools developed here also form part of a program aimed at constructing Ricci flow with surgery in dimension 4.

</details>

### [Scaling limits for equivariant Szeg\H{o} kernels near a singular point of the moment map and applications to K\"ahler reduction](https://arxiv.org/abs/2611.30311)
*Andrea Galasso* · `math.SG` · arXiv:2611.30311v1 · relevance 0.23

- **In one sentence**: Studies scaling limits of equivariant Szegő kernels near a singular point of the moment map for a compact group action on a Hodge manifold, and applies them to the quantization of the singular Kähler reduced space.
- **In plain words**: This paper looks at a symmetry-based construction in geometry: when a group of symmetries acts on a space, one can build a smaller "reduced" space by keeping only the symmetric parts. The authors study what happens near a special point where this reduction becomes singular (the reduced space is no longer smooth). They use a rescaling technique that zooms in on that point to describe the behaviour of the relevant kernels there.
- **Why it matters**: The text describes how the method applies to several questions about invariant sections near singular strata, including whether the Guillemin–Sternberg map stays asymptotically unitary there. Its wider significance beyond this specialist setting is not stated in the text, so I cannot say more about it.
- **Background needed**: - Hodge manifold: a complex geometric space with a line bundle whose curvature is positive, so holomorphic sections are well behaved.
- Compact Lie group action: a compact symmetry group acting holomorphically on the space.
- Moment map: a function that encodes the group action; zero being a singular value means the reduction at zero is singular.
- Kähler (symplectic) reduction: forming a quotient space by fixing the moment map level and dividing out the symmetry.
- Szegő kernel: the reproducing kernel for holomorphic sections, which acts as a density-type object in quantization.
- Guillemin–Sternberg map: a map relating quantization before and after reduction.
- Asymptotic unitarity and scaling limits: statements about behaviour as a power of the line bundle grows large, examined after rescaling near a point. · level: research-level

<details><summary>Original abstract</summary>

Suppose that a compact and connected Lie group acts holomorphically on a Hodge manifold, and that the action linearises to the associated Hermitian ample line bundle. Assume that zero is a singular value of the associated moment map. The spaces of global holomorphic sections of powers of the line bundle decompose over the finite dimensional irreducible representations of the group. The main goal of this paper is to study the scaling limits for equivariant Szeg\H{o} kernels near a singular point of the moment map. As an application, we discuss the quantization of the singular reduced space: the behaviour of invariant sections along the singular strata, the failure of the asymptotic unitarity of the Guillemin--Sternberg map near the singular strata, and the number of invariant sections concentrated near a singular orbit.

</details>

## Partial differential equations

### [Global well-posedness and scattering for the fractional inhomogeneous nonlinear Schrodinger equation with time-dependent damping](https://arxiv.org/abs/2611.28530)
*Boyu Jiang, Kexue Li* · `math.AP` · arXiv:2611.28530v1 · relevance 0.29

- **In one sentence**: The paper proves global well-posedness and scattering for a fractional, inhomogeneous nonlinear Schrödinger equation with time-dependent damping, for radial initial data, using Strichartz estimates and mixed-norm bounds on the nonlinear term.
- **In plain words**: The paper studies a wave-type equation that describes how a quantum-style wave spreads out and can lose energy over time. It asks whether solutions exist for all time and eventually behave like free waves that no longer interact. The authors show this holds for solutions that are symmetric around a center (radial data), using a fairly direct argument.
- **Why it matters**: The result gives a rigorous guarantee that these damped equations are well behaved over infinite time, which matters for the mathematical theory of dispersive equations. The text does not say how the result might be applied outside pure mathematics, so its wider significance is uncertain.
- **Background needed**: - Nonlinear Schrödinger equation: a model for waves whose evolution depends on their own strength, used in quantum physics and optics.
- Fractional Laplacian: a generalized spreading operator that replaces the usual second-derivative term with a fractional power.
- Inhomogeneous nonlinearity: the nonlinear term has a spatially varying or power-type coefficient, not a single uniform form.
- Time-dependent damping: a friction-like term that drains energy at a rate that changes over time.
- Global well-posedness: solutions exist, are unique, and depend continuously on the starting data, for all times.
- Scattering: for large times, the solution looks like a free wave with no nonlinear effects.
- Strichartz estimates: inequalities that control how dispersing waves decay in space and time.
- Mixed-norm spaces: function spaces that measure size using different norms in space and time.
- Radial data: starting conditions that depend only on distance from a center. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we prove the global well-posedness and scattering of solutions for a nonlinear Schrodinger type equation with fractional Laplacian, inhomogeneous nonlinearity and time-dependent damping.We give an elementary proof based on Strichartz estimates combined with estimates of the nonlinear term in mixed-norm spaces. To avoid the loss of regularity in the Strichartz estimates, we consider the radial data.

</details>

### [Sharp global well-posedness for the defocusing nonlinear wave equation outside a ball with radial data](https://arxiv.org/abs/2611.30302)
*Guixiang Xu* · `math.AP` · arXiv:2611.30302v1 · relevance 0.19

- **In one sentence**: The paper proves sharp global well-posedness for the defocusing nonlinear wave equation with Dirichlet boundary conditions outside a unit ball in R^3, for radial data in the critical homogeneous Sobolev space, for 3<p<5, improving a prior result by Xu, Yang and You (2025).
- **In plain words**: The paper studies how a wave-type equation that includes a nonlinear term evolves over all time, in the region of three-dimensional space outside a fixed sphere, with the boundary held at zero. It considers only initial conditions that are symmetric around the center, and the starting size of the data is set at the "critical" level where the equation is scale-balanced. The authors state they prove that solutions exist and are unique for all time in this setting, which they describe as sharp.
- **Why it matters**: The text itself is a short abstract, so its main value is as a sharpened result in a specialized area of PDE theory: it claims to extend a previous theorem to a sharper range of data. It is not clear from the text what wider applications, if any, it has; I cannot say how it connects to physical or engineering problems.
- **Background needed**: - Wave equation: a PDE describing propagating disturbances, such as vibrations or waves.
- Nonlinear term: the equation's behavior depends on the solution's size in a non-proportional way, which makes it harder to analyze.
- Defocusing: the nonlinearity tends to spread energy out rather than concentrate it, which helps prevent blow-up.
- Dirichlet boundary condition: the solution is fixed (here, zero) on the boundary of the region, here the sphere of radius 1.
- Radial data: initial conditions depend only on distance from the center.
- Global well-posedness: for any starting data in the class, a unique solution exists for all time and depends continuously on the data.
- Critical space: a function space scaling-matched to the equation, where the problem is at the borderline between easy and hard.
- Distorted Fourier transform: a generalized Fourier analysis adapted to a region with a boundary, rather than all of space.
- Energy–Morawetz estimates: integral inequalities that control energy and spread of waves, used to rule out blow-up. · level: research-level

<details><summary>Original abstract</summary>

Let $\Omega=\mathbb{R}^3\setminus\overline{B(0,1)}$ and $3<p<5$. We prove sharp global well-posedness of the defocusing Dirichlet boundary value problem of nonlinear wave equation with radial data in the critical space $\dot H^{s_c}_{D,\mathrm{rad}}(\Omega)\times \dot H^{s_c-1}_{D,\mathrm{rad}}(\Omega)$, where $s_c=\frac32-\frac{2}{p-1}$, thereby improve the result in \cite{XuYangYou2025}. The proof combines the distorted Fourier transform in \cite{LiSZ:NLS,XuYang2024} with the energy--Morawetz estimate by Dodson in \cite{DodsonCubic2018,Dodson2018}.

</details>

## Harmonic analysis

### [On the Bourgain-Rudnick eigenfunction restriction conjecture in four dimensions](https://arxiv.org/abs/2611.29806)
*Ciprian Demeter* · `math.CA` · arXiv:2611.29806v1 · relevance 0.21

- **In one sentence**: The paper proves a uniform L^2 upper bound for eigenfunctions of the four-dimensional flat torus restricted to the compact paraboloid, using Fourier restriction estimates and the Du–Zhang fractal restriction theorem applied on two-dimensional slices.
- **In plain words**: The paper studies the standing-wave patterns (eigenfunctions) that live on a four-dimensional flat, repeating space, and how much they can concentrate when measured on a curved surface inside that space. The authors prove an upper limit on that concentration, which is a version of a conjecture by Bourgain and Rudnick. Their method reinterprets counts of lattice points on spheres as a measure of how spread out certain points are, and then uses a known theorem about that spread.
- **Why it matters**: Bounds of this type control how large wave-like functions can get on a surface, a question that links number theory (lattice point counts) with analysis of waves. The text does not discuss applications beyond this setting, and it only mentions that further extensions are possible without specifying them.
- **Background needed**: - Flat torus: a space with no curvature that wraps around like a video game screen, in which opposite edges are glued together.
- Eigenfunction: a wave-like pattern that keeps its shape under the Laplace operator, roughly a standing wave with fixed frequency.
- L^2 norm: a way of measuring the overall size of a function; bounds on it limit how strongly waves can focus.
- Paraboloid: a curved bowl-shaped surface; here, a compact piece of it.
- Lattice point statistics: how integer grid points are distributed on a sphere, which relates to eigenfunction sizes.
- Fourier restriction: the study of how Fourier transforms behave when restricted to curved surfaces.
- Fractal restriction theorem: a result (by Du and Zhang) about how restriction estimates hold for sets with fractal-like spread. · level: research-level

<details><summary>Original abstract</summary>

We prove a uniform upper $L^2$ bound for eigenfunctions of the four-dimensional flat torus on the compact paraboloid $\mathbb{P}^3$. The main novelty is the use of Fourier restriction estimates. We interpret spherical lattice point statistics as non-concentration inequalities of the strength needed to apply the Du--Zhang fractal restriction theorem. We apply their result on two-dimensional slices of $\mathbb{P}^3$. Further possible extensions are also discussed.

</details>

### [The $T1$ theorem under Dini regularity](https://arxiv.org/abs/2611.30870)
*Kangwei Li* · `math.CA` · arXiv:2611.30870v1 · relevance 0.21

- **In one sentence**: The paper proves the T1 theorem for Calderón-Zygmund operators assuming only the classical Dini regularity condition on the kernel, which the authors describe as resolving a long-standing open problem in singular integral theory.
- **In plain words**: The paper is about a standard test in harmonic analysis: a rule for deciding when an operator that smooths and rearranges functions stays well-behaved (bounded) when measured in standard size norms. The authors show this test works under the Dini condition, a classical smoothness requirement on the operator's kernel. The text states that this answers a question that had been open for a long time.
- **Why it matters**: The T1 theorem is a central tool for checking boundedness of singular integrals, which underlie much of modern analysis and partial differential equations. The provided text gives only the abstract, so its precise scope and how it compares with earlier results cannot be judged from it.
- **Background needed**: - Harmonic analysis: the study of how functions decompose into waves or frequencies and how operators act on them.
- Singular integral operator: an averaging operator whose kernel blows up near the diagonal, so it needs careful treatment.
- Calderón-Zygmund operator: a major class of singular integral operators with kernel size and smoothness estimates.
- T1 theorem: a criterion saying such an operator is bounded if it is bounded on a test function like the constant 1 (plus related conditions).
- Dini regularity: a slightly weaker-than-Hölder smoothness condition on a function, measured by an integral condition on its modulus of continuity.
- Operator boundedness: the operator does not blow up the size of inputs beyond a fixed constant factor. · level: research-level

<details><summary>Original abstract</summary>

We prove the $T1$ theorem for Calder\'on-Zygmund operators under the classical Dini regularity condition on the kernel, solving a longstanding open problem in singular integral theory.

</details>

## Complex analysis

### [Quantum walks and conformal mappings](https://arxiv.org/abs/2611.30403)
*Fedor Kuyanov, Michael Drmota, Mikhail Skopenkov et al.* · `math-ph` · arXiv:2611.30403v1 · relevance 0.20

- **In one sentence**: The paper derives uniform asymptotic formulas for the wave function of the discrete quantum walk (Feynman checkers, six-vertex model with special complex weights) across the whole space-time plane, using conformal mappings to handle Airy- and gamma-function transitions.
- **In plain words**: The paper studies a simple discrete model of a quantum particle, an electron hopping step by step along a line, and asks how its wave function behaves at every position and time. It finds the expected change between wavy and fading behaviour, described by the Airy function, and a second change near the speed of light, described by the gamma function. The authors prove two general theorems giving single formulas valid across these transitions, using a change of coordinates in the complex plane.
- **Why it matters**: Exact, uniform formulas that work across transition regions are useful tools for quantum walks, which appear in quantum computing and physics models, and the authors say the methods apply to other situations. The text does not establish wider impact beyond this, so its reach outside this setting is uncertain.
- **Background needed**: - Quantum walk: the discrete, step-by-step analogue of a quantum particle moving randomly, with amplitudes rather than probabilities.
- Wave function: a complex-valued function whose squared size gives the probability of finding the particle at a position.
- Asymptotic formula: an approximation that becomes accurate for large distances or times.
- Airy function: a special function describing the boundary between oscillating and exponentially decaying behaviour.
- Gamma function: a standard special function generalising factorials, here governing behaviour near the maximal speed.
- Conformal mapping: a smooth change of variables in the complex plane that preserves angles, used to simplify integrals.
- Six-vertex model: a lattice model from statistical physics, here with special complex weights. · level: research-level

<details><summary>Original abstract</summary>

We study the most elementary discrete model of an electron moving along a line, known as Feynman checkers, quantum walk, or the six-vertex model with special complex weights, and provide a uniform asymptotic formula for the wave function in the whole xt-plane. In addition to the well-known appearance of the Airy function that describes the transition between the oscillating and exponentially decaying regimes, we observe a second transition governed by the gamma function when the electron speed approaches the speed of light. We prove two general theorems producing uniform asymptotic formulae involving the Airy and gamma functions, using conformal mappings associated with the underlying integral representations. They are applicable in several other situations as well.

</details>

### [Central limit theorem for energies of determinantal point processes on complex manifolds I](https://arxiv.org/abs/2611.31229)
*Hao Wu* · `math.CV` · arXiv:2611.31229v1 · relevance 0.12

- **In one sentence**: The paper proves a central limit theorem for the Green energy, and for the logarithmic energy, of Bergman determinantal point processes on compact Riemann surfaces and complex manifolds, using local Bergman kernel asymptotics and a cumulant expansion.
- **In plain words**: The paper studies random arrangements of N points on a curved complex surface, where the points are shaped by a probabilistic rule that discourages them from clustering. For a measure of how the points interact, called the Green energy, it gives the typical size of that quantity and its spread. It then shows that, once N is large, the fluctuations of this energy behave like the familiar bell-shaped (Gaussian) curve.
- **Why it matters**: Central limit theorems tell us when random fluctuations become predictable, which matters for understanding how well such random point models can be tested or simulated. The text does not say what wider applications it has, so its broader significance is uncertain from this excerpt alone.
- **Background needed**: - Point process: a random collection of points, here N points on a surface.
- Determinantal point process: a random point model where correlations are governed by a kernel (a function describing how strongly points relate), which tends to spread points apart.
- Bergman kernel and positive line bundle: geometric objects on complex surfaces that define the point model.
- Riemann surface: a one-dimensional complex surface, such as a sphere or torus.
- Green function and energy: the Green function measures influence between two points; the energy sums this over all pairs of points.
- U-statistic: an average over all pairs of sample points.
- Cumulants: summary quantities of a random variable; a central limit theorem is shown by controlling them.
- Central limit theorem: the statement that suitably normalized sums of random quantities approach a bell curve. · level: research-level

<details><summary>Original abstract</summary>

We study the Bergman determinantal point process associated with a positive line bundle on a compact Riemann surface. Consider the U-statistic given by the Green function, called the Green energy. For a configuration of $N$ points, the expectation of Green energy is $\frac12 N\log N+O(N)$, and the variance is $(\log 2-\pi^2/24)N+O(\log^2 N)$. We prove a central limit theorem for the Green energy by combining local Bergman kernel asymptotics with an expansion for the cumulants. A central limit theorem also holds for the logarithmic energy of Bergman determinantal point process on complex manifolds.

</details>

## Operator algebras and spectral theory

### [The Kaplansky-Aupetit conjecture for C*-algebras](https://arxiv.org/abs/2611.29761)
*Ilja Gogi\'{c}, Bojan Kuzma* · `math.OA` · arXiv:2611.29761v1 · relevance 0.16

- **In one sentence**: The paper proves the Kaplansky–Aupetit conjecture, that unital invertibility-preserving linear surjections between certain Banach algebras (one of them a C*-algebra) are Jordan homomorphisms, and weakens the hypotheses to invertibility of products of two exponentials or of single exponentials.
- **In plain words**: The paper concerns maps between two collections of mathematical objects (algebras of operators, which generalize matrices and functions) that keep "invertible" objects invertible. It shows that when one of the two sides is a C*-algebra, every such map must respect a weaker form of multiplication, called a Jordan homomorphism. The text says the result was obtained with help from two AI systems, with one AI system finding the original proof in the special case where both sides are C*-algebras.
- **Why it matters**: This settles a long-standing question in functional analysis, which the text presents as a conjecture now resolved in the stated cases. Its connection to wider areas is not discussed in the text, so any further significance is unclear from this text alone.
- **Background needed**: - Banach algebra: a space of objects (such as bounded operators or functions) that can be added, multiplied and measured by a norm.
- C*-algebra: a special Banach algebra with a built-in "adjoint" operation, common in quantum physics and operator theory.
- Invertible element: one with a multiplicative inverse, such as a nonsingular matrix.
- Linear surjection: a linear map that hits every element of the target space.
- Jordan homomorphism: a map preserving the symmetrized product (ab+ba)/2 and squares, a weaker notion than preserving full multiplication.
- Exponential: the power series e^a of an element a, used to build invertible elements.
- Semisimple: a property meaning the algebra has no nonzero "trivial" pieces that obstruct analysis.
- Kaplansky–Aupetit conjecture: a question asking whether invertibility-preserving maps must be Jordan-type maps, dating from the study of spectral theory. · level: research-level

<details><summary>Original abstract</summary>

We settle the Kaplansky--Aupetit conjecture when either algebra is a $C^*$-algebra. More precisely, if $A$ is a unital Banach algebra and $B$ is a unital $C^*$-algebra, or if $A$ is a unital $C^*$-algebra and $B$ is a unital semisimple Banach algebra, then every unital invertibility-preserving linear surjection $\phi: A\to B$ is a Jordan homomorphism. In fact, it suffices to assume that $\phi$ preserves the invertibility of products of two exponentials, or of individual exponentials when both algebras are $C^*$-algebras. Claude Opus 5.5 found the original proof when both $A$ and $B$ are $C^*$-algebras by adapting a resolvent estimate from a recent preprint of Colbrook and Stepaniants, while OpenAI's GPT-6.1 further generalized this to the case where only one algebra is a $C^*$-algebra.

</details>

### [On the extension of non-faithful and non-normal traces of von Neumann algebras to their affiliated operators](https://arxiv.org/abs/2611.30036)
*Comlan Edmond Koudjinan* · `math.OA` · arXiv:2611.30036v1 · relevance 0.15

- **In one sentence**: The paper extends a possibly non-faithful, non-normal positive trace on a finite von Neumann algebra to affiliated (unbounded) operators via a resolvent-based definition, proves additivity and a quasi-triangle inequality, identifies the resulting bimodule with the span of finite-trace operators, and shows that for faithful normal traces it recovers the classical L^p spaces.</one_liner>
<parameter name="plain">The paper studies how to measure the "size" of possibly unbounded operators in a generalized matrix-like setting, where a trace is a way of summing up diagonal contributions. The authors define such a size, tau_Y, through a limit of resolvents (a smoothing device) and show it behaves additively and gives a distance between operators. For the well-behaved case of faithful normal traces, they confirm that this construction matches the standard L^p spaces.
- **Why it matters**: It removes the usual assumptions (faithfulness and normality) under which trace-based function spaces are built, which matters for noncommutative analysis and quantum probability. The text does not indicate applications beyond this framework, and the claimed role of Chernoff families is only briefly stated, so its wider significance is uncertain from the abstract alone.</why>
<parameter name="background">- Von Neumann algebra: an algebra of bounded operators on a Hilbert space, closed in a suitable topology; the noncommutative analogue of measurable functions.
- Trace: a linear functional tau with tau(XY)=tau(YX); "finite" means tau of the identity is finite.
- Faithful / normal: faithful means only zero has trace zero; normal means continuous under increasing limits of positive operators.
- Affiliated operator: a possibly unbounded operator that commutes with the algebra's unitaries in a suitable sense.
- Resolvent (I+hA)^{-1}: a smoothed inverse used to define the trace of unbounded operators.
- L^p spaces: spaces of p-integrable functions, here generalized to operator algebras.
- Chernoff family: a sequence of operators approximating a semigroup, here used in the approximation part of the paper.</history>
<parameter name="difficulty">research-level

<details><summary>Original abstract</summary>

Let $\tau$ be a positive tracial functional on a finite von Neumann algebra ${\mathcal{M}}$, not necessarily normal. For a positive self-adjoint operator $A$ affiliated with ${\mathcal{M}}$ we define ${\tau_{\mathrm{Y}}}(A)=\lim_{h\downarrow0}\tau(A(\mathrm{I}+hA)^{-1})\in[0,\infty]$. We show that $\tau_{\mathrm{Y}}(A)=\sup_R\tau(\min(A,R \mathrm{I}))$. We prove that ${\tau_{\mathrm{Y}}}$ is additive on positive affiliated operators, by a form--resolvent comparison valid for arbitrary positive traces. As a consequence, $\tau$ has a positive linear extension to the span $\mathscr D_\tau$ of the positive affiliated operators of finite extended trace, and $\tau_{\mathrm{Y}}(T^*T)$ defines a pre-Hilbert structure for every positive trace. For every trace, $\tau_{\mathrm{Y}}(|S+T|)^{2/3}\le \tau_{\mathrm{Y}}(|S|)^{2/3}+\tau_{\mathrm{Y}}(|T|)^{2/3}$; hence the operators $T$ with $\tau_{\mathrm{Y}}(|T|)<\infty$ form a ${\mathcal{M}}$-bimodule $\mathscr L_Y^1$, on which the linear extension is defined and cyclic. It turns out that $\mathscr L_Y^1=\mathscr D_\tau$; $d(S,T)={\tau_{\mathrm{Y}}}(|S-T|)^{2/3}$ is a translation-invariant pseudometric on $\mathscr L^1_Y$ and is a metric iff $\tau$ is faithful. On the approximation side, a Chernoff family in ${\mathcal{M}}$ forces affiliation of its generator. Trace defects of Chernoff families need not converge to ${\tau_{\mathrm{Y}}}(A)$, even for faithful normal traces, while two-sided resolvent comparison suffices. For faithful normal traces, ${\tau_{\mathrm{Y}}}$ is the canonical extension and the associated space $\mathscr L_Y^p$ coincide with the classical $L^p({\mathcal{M}},\tau)$ as well as their norms ($1\leq p<\infty$).

</details>

## Algebra

### [The Fourth-Power Formula for the Antipode in AS-Gorenstein Hopf Algebras](https://arxiv.org/abs/2611.30340)
*Quanshui Wu, Ruipeng Zhu* · `math.RA` · arXiv:2611.30340v1 · relevance 0.23

- **In one sentence**: The paper proves an S^4 formula for the antipode of left AS-Gorenstein Hopf algebras (infinite-dimensional generalization of Radford's finite-dimensional result), via a twisted Yetter–Drinfeld structure on the space of left homological integrals, and applies it to antipode bijectivity and finite-order bounds.</one_liner>
<parameter name="plain">The paper studies a class of algebraic structures called Hopf algebras, which carry a built-in "reversal" map called the antipode. It shows that applying this reversal four times returns to the start up to a controlled twist, extending a known result that was previously proved only for finite-dimensional cases. The authors also use this formula to say when the reversal map is a bijection and to give explicit bounds on how many repetitions are needed in certain settings.
- **Why it matters**: The result extends a known formula (Radford's S^4 formula) to a much broader, infinite-dimensional class, and refines an earlier formula by Brown and Zhang by identifying a specific conjugating element. The text does not indicate wider applications beyond algebra, so its significance is mainly within this area of research.
- **Background needed**: - Hopf algebra: an algebraic structure combining multiplication, comultiplication and an antipode (a kind of inverse-like map), used to describe symmetries.
- Antipode S: a linear map generalizing inversion; its fourth power S^4 is the object of the formula.
- Radford's S^4 formula: a known result for finite-dimensional Hopf algebras expressing S^4 as conjugation by a group-like element.
- AS-Gorenstein property: a homological regularity condition (from Artin–Schelter) that allows homological integrals to be defined.
- Homological integrals and Yetter–Drinfeld modules: advanced tools from homological algebra and representation theory used to carry out the argument.
- Coradical, noetherian, faithfully flat: standard technical conditions under which the main results hold. · level: research-level

<details><summary>Original abstract</summary>

AS-Gorenstein Hopf algebras, for which homological integrals are defined, form a broad class of (infinite-dimensional) Hopf algebras. We establish an $S^4$ formula for left AS-Gorenstein Hopf algebras, thereby generalizing Radford's $S^4$ formula for finite-dimensional Hopf algebras and refining the formula of Brown and Zhang by identifying a group-like conjugating element in the Hopf algebra $H$. Our approach is to endow the space of left homological integrals $\int^{\ell}_H$ with a canonical right $H^*$-module structure compatible with its natural right $H$-action. If the $H^*$-action is rational, then $\int^{\ell}_H$ carries a canonical $(\mathrm{id}_H,S^4)$-twisted right-left Yetter--Drinfeld module structure. The right $H$-action and left $H$-coaction on this one-dimensional space determine a character and a group-like element in $H$, respectively; the twisted Yetter--Drinfeld compatibility condition then yields the $S^4$ formula. The $H^*$-action on $\int^{\ell}_H$ is rational if either the coradical of $H$ is coreflexive or the trivial left module $\Bbbk$ admits a finitely generated projective resolution. In particular, the latter condition holds when $H$ is left noetherian. We also establish a corresponding result for right AS-co-Gorenstein Hopf algebras with coreflexive coradical. As applications, we use the $S^4$ formula to study the bijectivity of the antipode and derive explicit finite-order bounds when $H$ is module-finite and faithfully flat over a central right coideal subalgebra, or finitely cogenerated and faithfully coflat over a cocentral quotient.

</details>

### [Products of supersoluble groups](https://arxiv.org/abs/2611.29591)
*Jinbao Li, Yong Yang* · `math.GR` · arXiv:2611.29591v1 · relevance 0.20

- **In one sentence**: If a finite group is a product of two supersoluble subgroups, then its nonabelian composition factors are all PSL_2(p) with p at least 5, and its nonsoluble length is at most one.
- **In plain words**: This paper is about finite groups, which are collections of symmetries that can be combined, and how they can be built from smaller pieces. It asks what happens when a group can be written as the product of two "supersoluble" subgroups, which are groups that are especially simple in structure. The author shows that any non-abelian building blocks of such a group must be one specific family of groups, and that the group is only mildly complicated in how it stacks non-solvable layers.
- **Why it matters**: This is a structural classification result within group theory: it narrows down exactly what the pieces of a factorised group can look like. The text does not say what wider applications it has, so any connection beyond pure algebra is unclear from the summary alone.
- **Background needed**: - Finite group: a group with finitely many elements, such as the symmetries of a shape.
- Product of subgroups G = AB: every element of G can be written as a times b, with a in A and b in B.
- Supersoluble group: a group whose structure breaks into a chain of cyclic pieces, a fairly restricted kind of solvable group.
- Soluble (solvable) group: a group that can be built step by step from abelian (commutative) pieces.
- Composition factor: the simple building blocks that a finite group is assembled from.
- PSL_2(p): a specific simple non-abelian group, defined for each prime p.
- Nonsoluble length: how many layers of non-solvable structure the group has, counted in stages. · level: research-level

<details><summary>Original abstract</summary>

Let $G=AB$ be a finite group, where $A$ and $B$ are supersoluble. We prove that every nonabelian composition factor of $G$ is isomorphic to $\PSL_2(p)$ for some prime $p\ge5$ and that the nonsoluble length of $G$ is at most one.

</details>

## Representation theory

### [Principal subspaces of affine vertex algebras at admissible levels](https://arxiv.org/abs/2611.29412)
*Hao Li, Antun Milas* · `math.QA` · arXiv:2611.29412v1 · relevance 0.15

- **In one sentence**: The paper classifies generic principal subspaces of admissible affine vertex algebras across all simple Lie algebras, and studies the exceptional (nongeneric) cases through their C_2-algebras and arc algebras, proving classical freeness and product character formulas in some of them.
- **In plain words**: The paper studies a family of algebraic structures built from symmetry groups (Lie algebras) at special "admissible" settings of a parameter called the level. It sorts out which cases behave generically and which are exceptional, and then looks closely at the exceptional ones. For a few specific cases, the author(s) prove a tidy counting formula for the structure's size, and for one more case the counting formula is proved but a related freeness property is only conjectured.
- **Why it matters**: The text gives a complete classification of generic cases, and it notes that the null vectors needed for this were already known in the literature. The exceptional cases are the main new results, but the text does not say what applications they have beyond this area, so the wider significance is unclear from the text alone.
- **Background needed**: - Lie algebra: a mathematical object describing continuous symmetries, such as rotations in space; types (A, B, C, D, G_2, F_4, and so on) label the families.
- Affine vertex algebra: an infinite-dimensional algebraic structure built from a Lie algebra with a parameter called the level, used in conformal field theory in physics.
- Admissible level: a special family of values of that parameter where the structure is well behaved.
- Principal subspace: a particular subspace of the vertex algebra, built from the highest-weight part of the symmetry.
- Null vector: an element that must be set to zero in the quotient; it encodes the relations the structure satisfies.
- Character formula: a generating function that counts the dimensions of the pieces of the structure by degree.
- C_2-algebra and arc algebra: finite-type and infinite-jet versions of the structure, used to test its size; classical freeness means the structure is as large as the generic case predicts.
- Denominator: a number in the admissible-level formula that determines which levels are exceptional. · level: research-level

<details><summary>Original abstract</summary>

We classify generic principal subspaces of admissible affine vertex algebras for all simple Lie algebras. The nongeneric cases occur precisely at denominator two in types $B,C,F_4$ and at denominator three in type $G_2$. The proof uses geometry of nilpotent orbits combined with positive root null vectors. Surprisingly, null vectors needed for our classification are explicitly known and already studied in the literature. We then study the exceptional principal subspaces at the level of their $C_2$-algebras and arc algebras. For $\mathfrak{sp}_4$ at level $-\frac12$ and $G_2$ at level $-\frac53$, we prove classical freeness and obtain product character formulas. In type $C_n$ at level $-\frac12$, classical freeness fails for $n\ge4$. For $n=3$, we combine the functional model method of Feigin and Stoyanovsky, and a flat degeneration of the explicit realization of $L_{-3/2}(\mathfrak{sl}_3)$ to prove a product character formula, while classical freeness in this case remains conjectural. The principal subspace of $L_{-5/2}(F_4)$ is also conjecturally classically free.

</details>

### [Lie Algebra Cohomology and Seiberg-Witten Theory](https://arxiv.org/abs/2611.29713)
*Ahsan Z. Khan* · `hep-th` · arXiv:2611.29713v1 · relevance 0.13

- **In one sentence**: The paper computes the perturbative holomorphic-topological local operator algebra of pure N=2 SU(2) gauge theory, identifying it as a Poisson vertex algebra with a central-charge-zero Virasoro generator X (with X^2=0) and an odd weight-three primary Y, and equivalently the relative Lie algebra cohomology of sl_2[z,w]/(w^2) and self-Ext groups of the unit in the coherent Satake category.
- **In plain words**: This paper is about a precise algebraic answer to a question coming from physics: which local observables exist in a particular four-dimensional gauge theory (pure SU(2) theory with extended supersymmetry) when one looks at its perturbative, holomorphic-topological part. The author proves a previously stated conjecture, showing the answer is a specific algebraic structure built from two generators, and shows the same answer can be phrased as a cohomology computation for a Lie algebra. The proof relies on tools such as factorization over configurations of points on a line and two deformations of a coefficient algebra.
- **Why it matters**: The result turns a conjectured description from physics into a proven algebraic statement, and it links three areas: Seiberg-Witten-type gauge theory, Lie algebra cohomology, and the Satake category used in geometric representation theory. The text does not say more about broader consequences, so the wider significance is best judged by specialists.
- **Background needed**: - Gauge theory: a physical theory built from symmetry groups such as SU(2); "pure" means no matter fields.
- Supersymmetry (N=2): an extra symmetry relating particles of different spin; it is what makes the Seiberg-Witten framework possible.
- Local operators: observables attached to single points of spacetime; their algebra records how they combine.
- Vertex algebras and Poisson vertex algebras: algebraic structures modelling local operators in two-dimensional conformal field theory and its classical limits; a Virasoro element is a generator obeying the Virasoro algebra, the symmetry algebra of conformal transformations.
- Lie algebra cohomology: a way of extracting invariants of a Lie algebra (a linear structure encoding continuous symmetries, here sl_2) relative to a subalgebra; sl_2[z,w]/(w^2) is the sl_2 Lie algebra with coefficients in a ring of "dual numbers."
- Ext groups: measure how an object fails to be projective or how it deforms, in a category.
- Factorization: a rule for how local observables on configurations of points combine as the points collide or separate. · level: research-level

<details><summary>Original abstract</summary>

We compute the algebra of perturbative holomorphic-topological local operators of pure $\mathcal N=2$ gauge theory with gauge group $SU(2)$, proving a conjecture of the author: it is the Poisson vertex algebra generated by a Virasoro element $X$ of central charge zero and an odd primary $Y$ of weight three, subject only to $X^2=0$. Equivalently, we compute the relative Lie algebra cohomology $H^*(\mathfrak{sl}_2[z,w]/(w^2),\mathfrak{sl}_2)$ and the self-Ext groups of the unit in the coherent Satake category for $SL_2$ and $PGL_2$. The proof uses factorization on configuration spaces of points on the affine line, a depth argument, and two deformations of the coefficient algebra $\mathbb C[z,w]/(w^2)$.

</details>

## Number theory

### [The Birch and Swinnerton-Dyer formula for CM elliptic curves of analytic rank one](https://arxiv.org/abs/2611.29641)
*Xin Wan, Zerui Xiang, Ruichen Xu* · `math.NT` · arXiv:2611.29641v1 · relevance 0.31

- **In one sentence**: The paper proves the Birch and Swinnerton-Dyer formula for elliptic curves over the rationals that have complex multiplication and analytic rank one.
- **In plain words**: The paper is about a family of equations of the form y² = cubic in x, called elliptic curves, which have a special symmetry called complex multiplication. These curves have a count of rational solutions, the "rank," and the paper concerns a conjectured formula linking that rank to a value computed from an analytic (infinite-sum) function attached to the curve. For the special case where that analytic count equals one, the author(s) prove the formula holds.
- **Why it matters**: The Birch and Swinnerton-Dyer conjecture is one of the Clay Millennium Prize problems, so a proof for a well-defined class of curves is a notable partial result. The text does not say how far the result extends beyond this class, so its wider significance is unclear from the abstract alone.
- **Background needed**: - Elliptic curve: the set of solutions to a cubic equation in two variables, with a natural group structure.
- Rational numbers: fractions; the paper considers solutions in rationals.
- Rank: how many independent rational solutions a curve has, in a loose sense.
- Complex multiplication: a special symmetry of a curve, tied to imaginary quadratic number fields.
- Analytic rank: a rank-like number read off from an analytic function (an infinite sum or product), which is conjectured to equal the algebraic rank.
- L-function: the analytic function attached to a curve whose behaviour at a specific point encodes the rank.
- Birch and Swinnerton-Dyer conjecture: the claim that the algebraic and analytic ranks agree and that a specific leading constant matches arithmetic data. · level: research-level

<details><summary>Original abstract</summary>

In this article, we prove the Birch and Swinnerton-Dyer formula for elliptic curves over the field of rational numbers with complex multiplication and analytic rank one.

</details>

### [Elliptic curves with torsion Z/5: exact rank four over Q(k) and rank at least five infinitely often](https://arxiv.org/abs/2611.28977)
*Andrej Dujella, Juan Carlos Peral* · `math.NT` · arXiv:2611.28977v1 · relevance 0.22

- **In one sentence**: The paper constructs two elliptic curves over Q(k) with torsion Z/5Z and generic rank exactly 4 (with unconditional upper bounds via reduction of elliptic surfaces modulo primes), and uses a further quadratic-twist condition to obtain a fifth independent point, giving infinitely many rational elliptic curves with torsion Z/5Z and rank at least 5.
- **In plain words**: This paper is about elliptic curves, a family of smooth curves defined by cubic equations that carry a group structure, and specifically about how many independent "rational points" (solutions with rational coordinates) they can have. The authors write down two explicit families whose number of independent points is exactly four in general, and they check that no more exist using a modular-arithmetic argument. By adding one extra condition to one family, they find a fifth independent point and conclude there are infinitely many rational curves with at least five.
- **Why it matters**: Rank records for curves with a fixed small torsion group are a standard benchmark in arithmetic geometry, and this moves the known lower bound for that torsion from 4 to 5. The text does not discuss wider applications, so its connections beyond this area are unclear.
- **Background needed**: - Elliptic curve: a smooth cubic curve with a group law on its rational points.
- Rational points: solutions whose coordinates are rational numbers; their group is finitely generated, with a finite torsion part and a free part of rank r.
- Rank: the number of independent points of infinite order; higher rank means more independent rational solutions.
- Torsion Z/5Z: the finite part of the group has five elements.
- Q(k): the curves depend on a parameter k, so this is a one-parameter family over the rationals.
- Elliptic surface and reduction modulo primes: a way to bound the rank from above by counting points over finite fields.
- Quadratic twist: a related curve obtained by a square-root-type modification, used here to add a condition.
- Genus-one curve: a curve of genus 1 with its own rank, here of rank two. · level: research-level

<details><summary>Original abstract</summary>

We give two elliptic curves over $\mathbb{Q}(k)$ with torsion group $\mathbb{Z}/5\mathbb{Z}$ and rank exactly $4$, with four explicit independent points. The upper bounds come from reducing the relevant elliptic surfaces modulo suitable primes and are unconditional. They match the known lower bound for the generic rank with this torsion, due to Eroshkin, and are not isomorphic to Eroshkin's curve or to each other: their parametrising maps to $X_1(5)$ have degree $8$ instead of $12$, the constructions are dihedral rather than biquadratic, and their branch loci differ. In each case, two of the points come from a ``doubling'' step in the spirit of Jaswal. Adding one further condition to the second curve, coming from a quadratic twist over an intermediate conic, gives a fifth independent point over a genus-one curve of rank two. Hence there are infinitely many elliptic curves over $\mathbb{Q}$ with torsion $\mathbb{Z}/5\mathbb{Z}$ and rank at least $5$, improving the known bound $C(\mathbb{Z}/5\mathbb{Z})\ge 4$ to $C(\mathbb{Z}/5\mathbb{Z})\ge 5$.

</details>

## Algebraic geometry

### [Categorical Torelli theorem for quintic threefolds](https://arxiv.org/abs/2611.30760)
*Genki Ouchi* · `math.AG` · arXiv:2611.30760v1 · relevance 0.26

- **In one sentence**: The paper proves a categorical Torelli theorem for smooth quintic threefolds over the complex numbers: equivalence of bounded derived categories of coherent sheaves implies isomorphism of the varieties.
- **In plain words**: The paper studies a particular kind of shape studied in algebraic geometry: smooth quintic threefolds, which are high-dimensional surfaces cut out by fifth-degree polynomial equations. It asks whether the bookkeeping of sheaves on such a shape (a structured record of how functions and data sit on it) is enough to recover the shape itself. The authors show that if two such shapes have equivalent categories of sheaves, then the shapes are in fact the same up to isomorphism.
- **Why it matters**: This is a rigidity result: the algebraic data determines the geometry, which is a clean answer to a question of the form "how much of a shape does its derived category remember?" The text gives only the statement, so its wider significance and methods cannot be judged from it here.
- **Background needed**: - Complex numbers and algebraic varieties: solution sets of polynomial equations over the complex numbers.
- Quintic threefold: a smooth variety of complex dimension three in projective space, defined by one degree-five polynomial.
- Coherent sheaves: a standard way to attach algebraic data (like functions or vector bundles) to a variety.
- Derived category: a larger organized category built from complexes of sheaves, encoding homological information.
- Equivalence of categories: a structure-preserving correspondence; here, two varieties having equivalent derived categories.
- Torelli theorem: the general type of result that a geometric object is determined by associated data (originally for curves and Hodge structures). · level: research-level

<details><summary>Original abstract</summary>

We prove that two smooth quintic threefolds over $\mathbb{C}$ are isomorphic if their bounded derived categories of coherent sheaves are equivalent.

</details>

### [Holomorphic Foliations with a Single Singularity on Orbifold Projective Surfaces](https://arxiv.org/abs/2611.31111)
*Ruben Lizarbe, Liliana Puchuri, Rudy Rosas* · `math.AG` · arXiv:2611.31111v1 · relevance 0.16

- **In one sentence**: The paper studies holomorphic foliations on orbifold projective surfaces with cyclic divisor class group that have a single singular point of algebraic multiplicity one, and shows that when the normal degree is large enough there is no invariant algebraic curve, with examples showing the bound is sharp.
- **In plain words**: This is about a way of splitting a surface with mild "cone-like" points into smooth flowing paths, called a foliation, which has only one special point where the paths meet. The authors ask whether such a splitting can be built around a fixed algebraic curve, and show that once a certain numerical measure of the foliation is large enough, it cannot. They also give examples showing that their threshold cannot be lowered.
- **Why it matters**: Results of this type classify which geometric structures are possible on a space, a central theme in algebraic geometry. The text does not say how it connects to other areas, so wider significance is unclear from this abstract alone.
- **Background needed**: - Projective surface: a two-dimensional space described by polynomial equations, the complex analogue of a sphere or plane.
- Orbifold point: a point where the surface looks like a quotient by a finite symmetry group, a mild kind of singularity.
- Holomorphic foliation: a decomposition of the surface into a family of non-crossing curves (leaves), like parallel threads, defined by complex-smooth rules.
- Singularity of a foliation: a point where the leaves fail to form a smooth family; here there is exactly one, with algebraic multiplicity one (the simplest kind).
- Invariant algebraic curve: a curve made of solutions of polynomial equations that the foliation preserves, i.e. each leaf-path that starts on it stays on it.
- Normal degree: a number measuring how the foliation bends relative to the surface; larger means more complicated.
- Divisor class group: a finite-type algebraic bookkeeping object for curves on the surface; cyclic means it is generated by one element. · level: research-level

<details><summary>Original abstract</summary>

We investigate holomorphic foliations on orbifold projective surfaces with cyclic divisor class group, assuming that the foliation has a unique singular point of algebraic multiplicity one. If the normal degree of the foliation is sufficiently large, then we prove that it admits no invariant algebraic curve. Furthermore, we present several examples showing that the bound obtained is optimal.

</details>

## Topology

### [Tame homotopy theory and the Goodwillie tower of the identity](https://arxiv.org/abs/2611.31031)
*Nicolas Gu\`es* · `math.AT` · arXiv:2611.31031v1 · relevance 0.31

- **In one sentence**: The paper modernizes Dwyer's tame homotopy theory, extends it to non-simply connected spaces using Heuts's work on the Goodwillie tower of the identity, and builds spectral Lie algebraic models for Hess's r-mild homotopy theory.
- **In plain words**: This paper is about a way of describing the shape of spaces (such as surfaces or more abstract higher-dimensional objects) using algebraic structures, so that questions about shape become questions about algebra. The author revisits an existing approach by Dwyer, extends it to spaces that have loops which cannot be shrunk to a point, and links it to a series of increasingly refined approximations of shape called the Goodwillie tower. The text summarizes this as a set of constructions, and does not report further findings beyond these.
- **Why it matters**: The work tries to connect two existing lines of research, Dwyer's tame homotopy theory and Heuts's study of the Goodwillie tower, and to extend the first beyond simply connected spaces. Its significance for wider mathematics is not stated in the text, so readers should treat the value as provisional and check the full paper.
- **Background needed**: - Homotopy theory: classifies spaces by when continuous deformations can be considered equivalent, ignoring rigid geometry.
- Simply connected space: a space in which every loop can be shrunk to a point; the paper extends beyond this case.
- Lie algebra: an algebraic structure (with a bracket operation) used here as a algebraic model of a space.
- Goodwillie tower: a sequence of successively finer polynomial approximations to a functor, here applied to the identity functor on spaces.
- Model (in this context): an algebraic object that encodes the homotopy type of a space, so that topology can be studied by algebra.
- Spectral: refers to objects from stable homotopy theory (spectra), a more linear, additive setting. · level: research-level

<details><summary>Original abstract</summary>

The purpose of this note is to provide a modern treatment of Dwyer's tame homotopy theory and extend it to non-simply connected spaces, exploiting a connection with the work of Heuts on the Goodwillie tower of the identity. As an application, we construct spectral Lie algebraic models for Hess's $r$-mild homotopy theory.

</details>

### [The M\"obius Homology Laplacian for Persistence Modules](https://arxiv.org/abs/2611.28292)
*Tatum Rask* · `math.AT` · arXiv:2611.28292v1 · relevance 0.18

- **In one sentence**: The paper defines a Laplace operator on the Möbius chain complex of persistence modules (the "Möbius homology Laplacian"), whose kernel gives canonical cycle representatives, and analyzes its spectrum for one-parameter modules and birth-death modules from simplicial filtrations.
- **In plain words**: The paper studies how shapes in data change as a parameter grows, a setting called persistent homology, which tracks when loops and holes appear and disappear. The authors build a matrix-style operator, analogous to the Laplacian used in graph and spectral analysis, on a structure that categorifies Möbius inversion, a counting tool from combinatorics. They report that for one-parameter modules they fully determine the eigenvalues of the degree-one version, and for birth-death modules the trace and determinant of the degree-zero version reflect the structure of the persistence diagram.
- **Why it matters**: It offers a way to attach analytic, spectral information to persistence modules, which standard persistence diagrams do not directly encode. Its connection to applications is not established in the text, so its practical reach is uncertain.
- **Background needed**: - Persistent homology: tracking holes and loops in a growing family of spaces, summarized by a persistence diagram of birth and death times.
- Persistence module: the algebraic object (vector spaces with maps linking stages of the filtration) that persistent homology studies.
- Chain complex: a sequence of vector spaces with boundary maps, used to compute homology (cycles modulo boundaries).
- Möbius inversion: a combinatorial rule for recovering values from cumulative data over a partially ordered set; "categorifying" it means replacing numbers with vector spaces and maps.
- Laplace operator and spectrum: a matrix-like operator whose eigenvalues and kernel describe structure; its kernel gives harmonic representatives.
- Simplicial complex and filtration: spaces built from vertices, edges, triangles, etc., added in stages. · level: research-level

<details><summary>Original abstract</summary>

Persistent homology provides a framework for studying the evolution of topological features across filtered spaces. While persistence diagrams give discrete invariants that record the birth and death of homological features, they do not directly encode analytic or geometric structure associated to persistence modules. This paper develops a spectral framework for persistent homology by introducing and studying a Laplace operator on the M\"obius chain complex, called the M\"obius homology Laplacian. M\"obius homology categorifies M\"obius inversion for persistence modules by replacing integer-valued data with vector-space-valued chain complexes. By equipping these chain complexes with inner products, we define a Laplace operator on the M\"obius chain complex whose kernel provides canonical cycle representatives for the associated M\"obius homology space. We analyze the spectral properties of this operator in two primary settings: one-parameter persistence modules and birth-death modules arising from filtrations of simplicial complexes. For one-parameter modules, we completely characterize the eigenvalues of the degree-one M\"obius homology Laplacian. For birth-death modules, we show that the trace and determinant of the degree-zero M\"obius homology Laplacian reflect the combinatorial structure of the persistence diagram.

</details>

## Dynamical systems

### [A transitive $C^{1+\alpha}$ surface diffeomorphism with positive entropy has at most one measure of maximal entropy](https://arxiv.org/abs/2611.29387)
*Wanshan Lin, Xueting Tian* · `math.DS` · arXiv:2611.29387v1 · relevance 0.25

- **In one sentence**: For a topologically transitive C^{1+α} diffeomorphism of a closed surface with positive topological entropy, the measure of maximal entropy is shown to be unique (at most one exists).
- **In plain words**: This paper studies smooth rules for moving points around a closed surface, such as a sphere or torus, in a way that is chaotic but still follows a pattern. Such a rule can be described by many probability distributions over its long-run behaviour, and some are "most chaotic" in a precise sense. The paper shows that, under these conditions, there is at most one such most-chaotic distribution.
- **Why it matters**: Uniqueness of the maximal-entropy measure is a standard question in dynamical systems, because it tells you that the system's chaos has one canonical statistical description. The text itself gives only the statement, so its wider significance and links to other results are not established here.
- **Background needed**: - Diffeomorphism: a smooth, invertible map of a surface onto itself, with a smooth inverse.
- C^{1+α}: the map and its derivative are smooth enough, with a mild Hölder-type regularity condition (α between 0 and 1).
- Topological entropy: a number measuring how fast the orbits of a map become complicated; positive means genuinely chaotic.
- Topologically transitive: some orbit eventually comes arbitrarily close to every point of the space.
- Invariant measure: a way of assigning probabilities to regions that the map leaves unchanged.
- Measure of maximal entropy: an invariant measure whose entropy equals the topological entropy of the map. · level: research-level

<details><summary>Original abstract</summary>

Let $0<\alpha\le 1$. On a closed surface, every topologically transitive $C^{1+\alpha}$ diffeomorphism with positive topological entropy has at most one measure of maximal entropy.

</details>

### [Algorithms and topological invariants for dynamic systems. IV. Topological Equivalence of Functions and Hamiltonian Dynamical Systems](https://arxiv.org/abs/2611.30510)
*Alexandr Prishlyak* · `math.DS` · arXiv:2611.30510v1 · relevance 0.16

- **In one sentence**: This fourth part of a series classifies smooth functions and Hamiltonian flows on surfaces up to topological equivalence using Reeb graphs and cell decompositions, with recursive counts and generating functions for simple cases on the disc and sphere.
- **In plain words**: The paper asks when two ways of describing motion or height on a curved surface, such as a landscape or a sphere, count as "the same" once you ignore smooth stretching and only keep the overall shape of how things rise, fall and flow. The authors use simple tree-like diagrams (Reeb graphs) and grid-like cell decompositions as fingerprints that capture this shape. They then count how many essentially different cases exist for a given number of saddle points.
- **Why it matters**: Counting topologically distinct flows and height functions gives a concrete, checkable way to organize a classical area of dynamical systems. The text does not say how these counts will be used beyond the paper itself, so its wider impact is unclear from this excerpt.
- **Background needed**: - Topological equivalence: two systems are considered the same if one can be continuously deformed into the other without tearing, ignoring exact shape and speed.
- Structural stability: a system whose overall behaviour survives small perturbations.
- Morse function: a smooth height function whose critical points (peaks, pits, saddles) are non-degenerate.
- Saddle point: a point where a surface is flat but rises in one direction and falls in another.
- Reeb graph: a graph built by collapsing each level set of a function to a point, recording how components merge and split.
- Cell decomposition: splitting a surface into simple pieces (points, edges, faces) for combinatorial bookkeeping.
- Hamiltonian flow: the motion generated by an energy function in classical mechanics.
- Generating function: a formal series whose coefficients are the counts of interest.
- This is part IV of a series; earlier parts cover differential topology, discrete structures and manifold recognition algorithms. · level: research-level

<details><summary>Original abstract</summary>

This is the fourth part of a series on algorithms and topological invariants for dynamical systems. We study the topological equivalence of smooth functions and of Hamiltonian flows on surfaces, and the discrete invariants, Reeb graphs and cell decompositions, that classify them. We recall the notions of topological equivalence and structural stability, introduce two equivalences of functions (with and without the order of the critical values) and show that simple Morse functions on closed orientable surfaces are classified by their Reeb graphs with vertex odering, while simple Hamiltonian flows are classified by Reeb graphs with marked edges. For the disc and for the sphere we obtain a recursive description and a generating function for the numbers of such trees, and compute the numbers of topologically non-equivalent simple Morse functions and Hamiltonian flows with a given number of saddles. We also describe functions with isolated, possibly degenerate, critical points by cell decompositions, and give an algorithm and computational results for functions with three critical points. In the first part (arXiv:2501.15657) we discussed the basic concepts of differential topology. In the second part (arXiv:2502.00506) we discussed the discrete topological structures used in the topological theory of dynamical systems. In the third part (arXiv:2502.09958) we constructed algorithms that recognize $2$- and $3$-manifolds in simplicial complexes and regular CW-complexes and determine the topological type of a $2$-manifold (connectivity, orientability, genus, number of boundary components).

</details>

## Combinatorics

### [The Hamilton cycle space in the Erd\H{o}s--R\'enyi random graph process](https://arxiv.org/abs/2611.30619)
*Hao Zhang, Wensheng Sun, Panpan Cheng* · `math.CO` · arXiv:2611.30619v1 · relevance 0.19

- **In one sentence**: The paper shows that, for the Erdős–Rényi random graph process on an odd number of vertices, with high probability the Hamilton cycles span the cycle space over F2 simultaneously for all steps from the first time minimum degree reaches three onward, and that the graph is then Hamilton-connected at each such step, answering a question of Christoph, Nenadov and Petrova.
- **In plain words**: The paper studies a graph that grows by adding random edges one at a time, starting from no edges. It looks at the moment when every vertex has at least three edges, and shows that from that point on, with high probability, the closed loops that visit every vertex exactly once are rich enough to generate all the cycles of the graph under a simple "add or remove" rule. It also shows that the graph is then Hamilton-connected, meaning any two vertices can be joined by a path that passes through every vertex.
- **Why it matters**: This settles a question posed by Christoph, Nenadov and Petrova, so it closes a specific open problem about how structure in random graphs develops over time. The text does not say what wider applications it has, so any connection beyond combinatorics is unclear from the text alone.
- **Background needed**: - Graph: vertices joined by edges; here the graph is random and gets one new uniformly chosen edge per step.
- Random graph process G(n,m): the graph after m steps on n vertices; "with high probability" means the chance of the claim tends to 1 as n grows.
- Minimum degree: the fewest edges at any vertex; τ3 is the first step where this reaches three.
- Hamilton cycle: a closed loop visiting every vertex exactly once.
- Cycle space over F2: the collection of edge sets formed by combining cycles, where combining means taking the symmetric difference (edges in exactly one of the two sets); the Hamilton cycles generating this space means every cycle is a combination of Hamilton cycles.
- Hamilton-connected: every pair of distinct vertices is joined by a Hamilton path.
- The result requires n to be odd. · level: research-level

<details><summary>Original abstract</summary>

Let $G(n,m)$ denote the graph at step $m$ of the Erd\H{o}s--R\'enyi random graph process on $n$ vertices. The process starts with the edgeless graph and adds one edge at each step, chosen uniformly at random from the missing edges. Let $\tau_3$ be the first step at which the minimum degree of $G(n,m)$ reaches three. We answer a question of Christoph, Nenadov and Petrova [J. Combin. Theory Ser. B 176 (2026) 254--267] by proving that, as $n$ tends to infinity through odd integers, with high probability the Hamilton cycles of $G(n,m)$ span its cycle space over $\Ftwo$ simultaneously for all $m\ge\tau_3$. On the same event, $G(n,m)$ is Hamilton-connected for every $m\ge\tau_3$.

</details>

### [A characterization of Ramsey property with application to dynamical systems](https://arxiv.org/abs/2611.28425)
*Teturo Kamae* · `math.CO` · arXiv:2611.28425v1 · relevance 0.15

- **In one sentence**: The paper gives an ultrafilter-based characterization of when a set of k-element subsets of the natural numbers has the Ramsey property, i.e. when an infinite homogeneous subset exists inside one cell of a finite partition.
- **In plain words**: The paper is about a classic question in combinatorics: if you colour every group of k numbers from an infinite set using a finite number of colours, must some infinite piece of the numbers have all its k-groups in one colour? The author gives a new way to test which colour classes have this property, using a tool from logic called an ultrafilter. The text provided is only a short abstract, so the specific result and its proof are not shown here.</plain>
<parameter name="why">The Ramsey property is a central notion in combinatorics, and a clean criterion for it could make it easier to check in concrete cases. The abstract mentions an application to dynamical systems in the title, but the text given does not describe that application, so its connection is unclear from what is provided.</why>
<parameter name="background">- Ramsey theory: when enough objects are split into finitely many colour classes, some class must contain a large structured piece.
- Infinitary Ramsey theorem: the version where the objects are infinite; here, k-element subsets of the natural numbers.
- Partition: splitting a collection into finitely many non-overlapping classes.
- Ultrafilter: a maximal family of "large" sets in a logical sense; used here as a way to encode which colour classes are big enough.
- Dynamical systems: models of things that change over time, mentioned only in the title.</background>
<parameter name="difficulty">research-level

<details><summary>Original abstract</summary>

The infinitary Ramsey theorem says that in any finite partition {V^i;~i=1,2,\cdots,n} of the the family of k-subsets of N, there exists V^i having an infinite subset M of N such that any k-set from M is in V^i. This property of V^i is called the Ramsey property. We characterize this property in term of ultrafilter.

</details>

## Numerical analysis

### [On mesh transfers and time error estimation in adaptive finite element methods for parabolic problems](https://arxiv.org/abs/2611.29379)
*Stefan Karch* · `math.NA` · arXiv:2611.29379v1 · relevance 0.19

- **In one sentence**: The paper shows that transferring the discrete solution and its time derivative to a new spatial mesh in space-time adaptive finite element solvers for the heat equation (implicit Euler) can break the discrete equation, causing the time error estimator to overestimate local error by a factor inversely proportional to the time step, and proposes elliptic-reconstruction-based transfers to reduce or remove this residual.
- **In plain words**: Computer simulations of heat spreading often change the grid of points they use as they go, and each change requires copying the current solution onto the new grid. The paper points out that this copying, even when the grid is only refined, can leave a mismatch that makes the software's own error check too pessimistic for small time steps. The authors propose a different copying method, based on an elliptic reconstruction, that greatly reduces or removes this mismatch, and they test it on an adaptive example.
- **Why it matters**: Adaptive solvers rely on error estimates to decide where to refine and how large each time step can be, so a systematic overestimate can make them waste effort. The text only covers the implicit Euler method applied to the heat equation and a single adaptive example, so how far the findings extend to other methods or problems is not established here.
- **Background needed**: - Finite element method: a standard way to approximate solutions of partial differential equations by splitting space into a mesh of small cells.
- Parabolic problem / heat equation: a model of how a quantity such as temperature spreads over space and time.
- Implicit Euler method: a basic time-stepping scheme that advances the solution in small time steps.
- Adaptive mesh refinement: automatically making the mesh finer where the error is large, and coarser elsewhere, which requires transferring the solution between meshes.
- A posteriori error estimator: a computable quantity that estimates the size of the numerical error during the calculation, used to guide adaptivity.
- Elliptic reconstruction: an auxiliary smooth approximation of the discrete solution, used here as the basis of the new transfer.
- Residual: the amount by which an approximate solution fails to satisfy the governing equation. · level: research-level

<details><summary>Original abstract</summary>

In space and time adaptive finite element methods, the discrete solution is transferred onto a different mesh whenever the spatial mesh changes. Refinement is commonly regarded as harmless, since nodal interpolation then reproduces the discrete solution exactly. However, we show that for the implicit Euler method applied to the heat equation, the transferred solution and time derivative, in general, violate the discrete equation on the new mesh. Unless the resulting transfer residual vanishes, the corresponding time error estimator overestimates the local error, for small time steps, by a factor inversely proportional to the time step size. To address this issue, we propose transfers based on the elliptic reconstruction, which significantly reduce the transfer residual or even remove it. In numerical experiments, we confirm the analysis and demonstrate the advantages of the proposed transfers in a space and time adaptive example.

</details>

### [A High-Order Geometry-Conforming Selective Discontinuous Galerkin Method and Its Error Analysis for Elliptic Interface Problems on Curved Domains](https://arxiv.org/abs/2611.30169)
*Fang Liu, Yuanhui Liu, Tao Lin et al.* · `math.NA` · arXiv:2611.30169v1 · relevance 0.19

- **In one sentence**: A high-order immersed finite element method on curved domains with interfaces, using a boundary-conforming triangular mesh, Frenet–Serret coordinates, and a symmetric selective discontinuous Galerkin formulation, with a priori error analysis giving O(h^m) energy and O(h^(m+1)) L2 bounds.
- **In plain words**: The paper studies how to compute approximate solutions to physics-style equations (elliptic partial differential equations) where the material has an internal boundary, called an interface, inside a curved region. The mesh only has to match the outer curved edge, not the internal interface, which avoids costly remeshing. The authors build a high-order version of this method, prove how accurate it is, and report numerical tests that match the predicted convergence rates and show fewer unknowns than a fully discontinuous method.</plain>
<parameter name="why">Interface problems on curved domains appear in many engineering and science models, and a method that avoids meshing around interfaces while keeping accuracy and reducing unknowns may be useful there. The text itself only supports these modest claims about accuracy and degrees of freedom; its practical impact beyond the reported tests is not established here.</plain>
<parameter name="background">- Partial differential equation (PDE): an equation describing how a quantity such as heat or stress varies over space.
- Interface problem: a PDE where material properties jump across an internal boundary.
- Finite element method: approximating a solution with simple piecewise polynomial pieces on a mesh of small triangles.
- Mesh and degrees of freedom: the mesh is the set of small cells; degrees of freedom are the unknown values the computer solves for.
- Immersed finite element: a method whose elements need not align with the interface, so the interface can cut through them.
- Discontinuous Galerkin: a method that allows the approximate solution to jump between cells, weakly enforced through penalty terms.
- Error bound O(h^m): the error shrinks roughly like the mesh size h raised to power m; higher m means faster convergence.
- Energy norm and L2 norm: two ways of measuring the size of the error.
- Frenet–Serret coordinates: a local coordinate system that follows a curve, used to describe curved boundaries.
- Trace inequality: a bound relating a function's size on an element's boundary to its size inside.</background>
<parameter name="difficulty">research-level

<details><summary>Original abstract</summary>

We develop and analyze a high-order geometry-conforming immersed finite element (GC-IFE) method for elliptic interface problems on curved domains. The method uses a triangular mesh that conforms to the outer boundary but need not fit the internal interface. Using Frenet--Serret coordinates, the method combines GC-IFE spaces on interface elements, geometry-conforming finite element spaces on curved boundary elements, and standard Lagrange spaces elsewhere. The global degrees of freedom of the proposed method are asymptotically the same as that of the standard continuous finite element method on the same mesh. The main analytical contributions are approximation estimates and trace inequalities for triangular GC-IFE functions. These estimates are used to establish stability and an optimal $O(h^m)$ error bound in an energy norm for the proposed method, which is based on a symmetric selective discontinuous Galerkin formulation. An optimal $O(h^{m+1})$ error bound in the $L^2$ norm is also obtained under the standard regularity assumption on the dual problem. Numerical experiments confirm theoretical convergence rates and demonstrate a reduction in global degrees of freedom to a fully discontinuous Galerkin method.

</details>

## Logic and foundations

### [$\Sigma^1_3$ Gandy-Harrington Forcing](https://arxiv.org/abs/2611.29432)
*William Chan, Sandra M\"uller, Farmer Schlutzenberg et al.* · `math.LO` · arXiv:2611.29432v1 · relevance 0.17

- **In one sentence**: The paper builds a higher-level version of Gandy-Harrington forcing for the projective hierarchy under a local determinacy hypothesis, and uses it for a reverse mathematics result at the Δ^1_2-Determinacy level and an inner-model basis theorem for Σ^1_3 sets.
- **In plain words**: This is a paper in mathematical logic about the structure of "definable" sets of infinite sequences of whole numbers, which are the objects studied in descriptive set theory. The authors adapt a known proof technique, Gandy-Harrington forcing, to a more complex level of that hierarchy. The text says this new version lets them prove a result about which axioms are needed for certain determinacy statements, and a new basis theorem for a class of sets.
- **Why it matters**: The abstract points to two concrete outcomes: a reverse mathematics result (identifying the exact axioms needed for a statement) and a basis theorem for Σ^1_3 sets. Its significance rests on how well the new forcing generalises, which the short text does not show; the connections to wider logic are the authors' claims and I have not checked them.
- **Background needed**: - Descriptive set theory: the study of definable sets of reals (infinite binary sequences) and their complexity, organised in the projective hierarchy (Σ, Π, Δ levels).
- Forcing: a technique for building new models of set theory by adding generic objects; Gandy-Harrington forcing is a specific forcing that builds sets with prescribed definability.
- Silver's dichotomy: a theorem saying that analytic equivalence relations have either countably many classes or a perfect set of inequivalent elements; Harrington's proof used this forcing.
- Determinacy: the assertion that certain two-player infinite games have a winning strategy for one player; its strength is measured by level in the projective hierarchy.
- Reverse mathematics: determining which axioms are logically necessary to prove a given theorem.
- Inner models and basis theorems: results saying that definable sets have members constructible in a suitable inner model (a restricted universe of sets). · level: research-level

<details><summary>Original abstract</summary>

Gandy-Harrington forcing is an important tool in descriptive set theory, first developed by Gandy and later used by Harrington to give a simple proof of Silver's dichotomy theorem. In this paper, we develop a new version of Gandy-Harrington forcing higher up in the projective hierarchy, under an appropriate local determinacy hypothesis. Using this new forcing, we prove a reverse mathematics result at the level of $\Delta^1_2$-Determinacy as well as new inner-model-theoretic basis theorem for $\Sigma^1_3$ sets.

</details>

### [On Cohen Generic Sets in Supercompact Prikry Extensions](https://arxiv.org/abs/2611.30821)
*Tom Benhamou, Gabriel Goldberg* · `math.LO` · arXiv:2611.30821v1 · relevance 0.16

- **In one sentence**: Under a supercompactness assumption on κ and a diamond-type principle on stationary subsets of λ, the paper shows that small strategically closed forcings are projections of λ-supercompact Prikry forcing, and it studies limits on κ-distributive projections, including size-λ examples that fail to be projections.
- **In plain words**: This is set theory work on the forcing method, a way of extending the universe of sets by adding new objects. The paper asks which kinds of forcing notions can be reproduced, in a precise "projection" sense, by one particular forcing called supercompact Prikry forcing. The text reports that, under a set-theoretic guessing principle and a cardinal-size condition, the answer is yes for a broad class, while in some other cases the answer is shown to be independent of the usual axioms, and some specific examples are shown not to fit.
- **Why it matters**: It maps which forcing notions can be realized inside a single canonical model-building tool, which clarifies the structure of large-cardinal forcing extensions. The abstract gives no wider applications, so its significance beyond this area is unclear from the text alone.
- **Background needed**: - Forcing: a method for adding new sets to a model of set theory, using a partially ordered set of finite approximations.
- Cardinals and cofinality: the size of infinite sets and the length of cofinal sequences; "singular" cardinals are those that are not regular.
- Large cardinals: κ being λ-supercompact is a strong infinity axiom about embeddings of the universe; it is a very strong consequence of set theory.
- Prikry-type forcing: a forcing that changes the cofinality of a measurable-type cardinal without collapsing cardinals.
- Projection: a map between forcings that preserves generic extensions, so one forcing is essentially a quotient of another.
- Diamond principle (◇) on stationary sets: a combinatorial guessing principle that holds in some models and fails in others.
- Strategic closure and distributivity: closure properties of forcings that limit the new sets they add.
- Independence: a statement neither provable nor refutable from the standard axioms. · level: research-level

<details><summary>Original abstract</summary>

Let $\kappa$ be $\lambda$-supercompact for a regular $\lambda>\kappa$. We show that if $\lambda$ is not the successor of a singular of cofinality below $\kappa$, $\diamondsuit(S^\lambda_{\geq\kappa})$ implies that every ${<}\kappa$-strategically closed forcing of size at most $\lambda$ is a projection of the $\lambda$-supercompact Prikry forcing. We show that the situation for successors of singulars of small cofinality is independent. Finally, we provide more limitations about the class of $\kappa$-distributive projections of the $\lambda$-supercompact Prikry forcing and give examples of $\kappa$-distributive forcings of size $\lambda$ which cannot be projections of this forcing.

</details>

## Mathematical physics

### [Gradient formula from the sphere for perturbative RG flows near critical dimensions](https://arxiv.org/abs/2611.31050)
*Marten Reehorst* · `hep-th` · arXiv:2611.31050v1 · relevance 0.12

- **In one sentence**: The paper derives a gradient formula for perturbative renormalisation group flows near critical dimensions, built from a renormalised functional on the sphere S^d, and checks its properties in several specific field theories in d = d_c − ε.
- **In plain words**: Physicists describe how a quantum field theory changes with the scale at which you look at it, and this flow is often described by a "beta function". The paper studies when such flows behave like the downhill motion of a ball on a landscape, which is the gradient property. The authors put the theory on a round sphere, derive a formula of this kind, and show that its potential at fixed points is related to the sphere free energy, for several example theories in dimensions just below a critical value.
- **Why it matters**: A gradient structure would give a general way to organise which scale-dependent theories can flow to which fixed points, and it links the flow to a sphere free energy that is a known quantity. The text does not show how far these results reach beyond the listed theories; for interacting gauge theories the authors state the properties only as assumptions.
- **Background needed**: - Renormalisation group (RG): the systematic way physicists track how a theory's couplings change with energy or length scale.
- Beta function: the rate of change of a coupling along the RG flow; fixed points are where it vanishes.
- Critical dimension d_c and ε: the paper works in a spacetime dimension d = d_c − ε, expanding in the small number ε.
- Weyl anomaly: a scaling symmetry that fails to hold exactly once quantum effects are included.
- Sphere free energy F̃: a scheme-independent number attached to a conformal theory placed on a sphere; it is used as a measure of degrees of freedom.
- Gradient flow: a flow that follows the downhill direction of a scalar potential under a metric.
- Two-point function: the correlation between field values at two points, here on the sphere. · level: research-level

<details><summary>Original abstract</summary>

We study the gradient property of perturbative renormalisation group flows in $d=d_c-\varepsilon$, with a potential and a metric regular at $\varepsilon=0$ up to logarithms of gauge couplings. We state properties of the renormalised functional with local couplings on the sphere $S^d$: finiteness, a local Weyl anomaly, the Ward identity of a conformal Killing vector, rotation properties and statements on the free theory. From them we derive a Ward identity without anomaly for a combination of the functional and its anomaly. Its first variation is a gradient formula whose symmetric metric contains the two-point function on the sphere and whose potential at fixed points is, in an extended form of the properties, proportional to the sphere free energy $\tilde F$ up to a constant. Sources of relevant operators enter through their Weyl variation, and in a scheme which we construct the gradient formula persists, with a nondegenerate metric if a matrix of the free theory is invertible. For multiscalar $\phi^4$ theory and for scalars and Dirac fermions with Yukawa and quartic couplings in $d=4-\varepsilon$, for sextic scalars in $d=3-\varepsilon$ and for cubic scalars in $d=6-\varepsilon$, we derive all these properties from a finiteness hypothesis. The gradient formula then holds to all orders for the beta function defined on the sphere. For interacting gauge theories the properties remain assumptions.

</details>

### [$\mu$- and $q$-extension of special functions in quantum field theory](https://arxiv.org/abs/2611.29543)
*J. Bl\"umlein, A. M. Gavrilik, U. Y. Lunha et al.* · `math-ph` · arXiv:2611.29543v1 · relevance 0.11

- **In one sentence**: The paper constructs μ- and q-extended versions of the special functions and nested sums (harmonic sums, polylogarithms, cyclotomic and root-valued objects) that arise in perturbative quantum field theory loop calculations.
- **In plain words**: Calculations in particle physics often produce a family of named mathematical functions and sums. This paper builds generalized versions of these functions, each with an extra parameter (called μ or q) that deforms the usual algebra. The abstract reports that the μ-versions mostly keep the same classes of functions, except for the case involving roots, while the q-versions produce new, higher-level functions.
- **Why it matters**: These deformed functions are said to be expected in loop calculations in theories modified by changed commutation rules, so the work is a mathematical groundwork for that possibility. Whether it connects to physical predictions is not shown in the text provided, so that link remains unclear.
- **Background needed**: - Perturbative quantum field theory: approximating particle interactions as a series of terms, each computed as a loop integral.
- Polylogarithms and harmonic sums: standard families of special functions and sums that appear in these integrals.
- Mellin transform: a mathematical change of variables that links integrals to sums.
- q- and μ-extensions: deformations of ordinary algebra (q-numbers, or commutation rules modified by a parameter) used to generalize these functions.
- Transcendental functions: functions that cannot be expressed as roots of polynomials with simple coefficients; "higher" means more complex in this classification. · level: research-level

<details><summary>Original abstract</summary>

Analytic calculations up to single-scale quantities in perturbative quantum field theory result into special numbers and functions, which are generalizations as iterative integrals over special alphabets. In this way one obtains polylogarithms, Nielsen integrals, the iterated integrals over linear denominator terms, cyclotomic letters, letters induced by quadratic forms, and square-root valued letters. The inverse Mellin transform relates special nested sums to these quantities, which are harmonic sums, generalized harmonic sums, nested sums implied by quadratic forms, cyclotomic harmonic sums, and nested sums containing central binomials. We construct the $\mu$- and $q$-extensions of all these special functions. They are expected to occur in loop calculations within $\mu$- and $q$-extended quantum field theories via modified (anti)commutation relations. The $\mu$-extended special functions are quite different form the corresponding $q$-extended functions. While in the former case one observes class-preservation characterized by the polynomial $\mu$-parameter, except for the case of root-valued letters. In the latter case new higher transcendental functions are obtained.

</details>

## Optimization and control

### [Low-Rank Tensor Representations for Efficient Multimarginal Optimal Transport](https://arxiv.org/abs/2611.30376)
*Johann Cl{\'e}ment-Cottuz (UNIROUEN, LITIS, LITIS - App) et al.* · `cs.LG` · arXiv:2611.30376v1 · relevance 0.23

- **In one sentence**: The paper proposes LRMOT, which restricts multimarginal optimal transport plans to tensors of bounded multilinear rank to cut the exponential cost of computing them, and reports approximation bounds and experiments showing faster runs with low transport cost.
- **In plain words**: Optimal transport is a way of finding the cheapest way to move a pile of material so it matches several target distributions at once. When many distributions are involved, the plan for moving things becomes a huge high-dimensional table whose size grows exponentially, so it quickly becomes too slow and memory-hungry. This paper restricts the plan to a compressed, structured form (low-rank tensors) that is much smaller to store and work with, and reports that the resulting algorithms run substantially faster while still giving low-cost solutions.
- **Why it matters**: Many problems that involve matching several probability distributions at once, such as combining multiple datasets or sensor views, run into this exponential cost. The text does not say how far the approach extends beyond the experiments it reports, so its wider reach is uncertain.
- **Background needed**: - Optimal transport: finding the least-costly way to rearrange one distribution into another, given a cost for each move.
- Marginals: the individual distributions a joint plan must match; multimarginal means more than two at once.
- Transport plan: a table (tensor) saying how much mass moves between every combination of locations.
- Tensor: a multi-dimensional array, a generalisation of a matrix to more than two indices.
- Multilinear rank: a measure of how compressible a tensor is; low rank means it can be described by far fewer numbers.
- Approximation bounds: guarantees on how close the restricted solution is to the true optimum. · level: research-level

<details><summary>Original abstract</summary>

Multimarginal Optimal Transport (MOT) suffers from exponential computational and memory costs in the number of marginals, as transport plans are represented by high-dimensional tensors. We introduce Low-Rank Multimarginal Optimal Transport (LRMOT), which restricts transport plans to tensors with bounded multilinear rank, providing a compact and structured representation of multimarginal couplings. This structure enables efficient algorithms with a low memory footprint. We establish approximation bounds for the resulting low-rank formulations and demonstrate experimentally that the proposed algorithms substantially reduce computational time while achieving solutions with low transport cost.

</details>

### [On convergence rate bounds for Markovian push-sum algorithms](https://arxiv.org/abs/2611.30824)
*Bal\'azs Gerencs\'er, Mikl\'os Kornyik* · `math.OC` · arXiv:2611.30824v1 · relevance 0.23

- **In one sentence**: The paper derives an almost sure upper bound on the convergence rate of push-sum averaging algorithms whose message-passing events follow a Markov chain or hidden Markov model, gives tools to make that bound cheap to compute, and proposes a transformation that provably improves the bound.
- **In plain words**: The paper studies distributed computing, where many connected devices each hold a number and try to agree on the average by passing messages to one another. Here the timing of who sends to whom follows a random pattern with memory (a Markov chain or hidden Markov model), and the authors work out a guaranteed bound on how fast the devices converge. They also give methods to compute that bound more cheaply and a way to modify the scheme so the bound gets better, with numerical experiments supporting all three parts.
- **Why it matters**: Reliable guarantees on how quickly distributed averaging converges matter for sensor networks and decentralized learning, where communication is unreliable or asymmetric. The text does not say how far the results extend beyond the numerical examples it reports, so the practical reach is unclear from the abstract alone.
- **Background needed**: - Consensus / averaging: nodes in a network repeatedly combine their values so all converge to a common value, ideally the average.
- Push-sum: a variant that works on directed networks where links are one-way, tracking an extra weight to correct for uneven sending.
- Markov chain: a random process where the next state depends only on the current state; a hidden Markov model adds unobserved states that drive what is seen.
- Almost sure convergence: convergence that holds with probability one, not just on average.
- Convergence rate: how quickly the error shrinks over iterations, often expressed as an exponential decay bound. · level: research-level

<details><summary>Original abstract</summary>

In this work we establish an upper bound on the almost sure convergence rate of a broad class of push-sum algorithms, more precisely for those where message passing events follow a Markovian dynamics, or a Hidden Markov Model. In this context, having a computationally accessible quantity at hand is of top priority; we thus formulate tools to cut down the complexity of obtaining the stated bound. Furthermore, we introduce a transformation to adjust a given push-sum scheme in a way that the bound on the rate provably improves -- and often so does the true convergence rate. Theoretical understanding is complemented by numerical results, where the quality of all three directions is demonstrated: for the bound on the rate, for the computational complexity and for the improvement strategy.

</details>

## Statistics theory

### [Nonparametric estimation of a common marginal hazard function under censoring and spatio-temporal dependence](https://arxiv.org/abs/2611.28953)
*Ibrahim Loudy, Kowir Pambo Bello, St\'ephane Bouka et al.* · `math.ST` · arXiv:2611.28953v1 · relevance 0.18

- **In one sentence**: Proposes Nadaraya-Watson and k-nearest-neighbor estimators for a pooled marginal hazard function from right-censored, spatially and temporally dependent durations, with pointwise and uniform convergence rates and a simulation comparison.
- **In plain words**: The paper studies how long until an event happens (such as a patient relapsing or a city service request being closed) when the observations are linked by where and when they occur, and some cases are only partly observed because the study ended first. The authors build two statistical tools for estimating the underlying rate at which the event happens over time, one based on local weighted averaging and one based on the k nearest neighbors in space and time. They test both on simulated data and on two real datasets: a multicenter clinical trial and 1,746 geolocated requests to New York City's 311 service.
- **Why it matters**: Durations that are censored and also clustered in space and time are common in medicine, public services and other fields, and standard methods often assume independence that does not hold. The text reports theoretical convergence rates and empirical results on two applications, but the abstract alone does not show how the methods compare with existing alternatives in practice.
- **Background needed**: - Hazard function: the instantaneous rate at which an event occurs, given that it has not yet occurred.
- Right censoring: some durations are only known to exceed a recorded time, e.g. the study ended or the case was still open.
- Nonparametric estimation: estimating a curve from data without assuming a fixed formula for it.
- Nadaraya-Watson estimator: a local averaging method that weights nearby observations more heavily.
- k-nearest-neighbor (k-NN) estimator: averages over the k observations closest in the chosen distance measure.
- Spatio-temporal dependence: observations close in place or time tend to be related, which violates the independence assumed by many standard methods.
- Convergence rate: how quickly the estimate approaches the true function as the sample grows. · level: research-level

<details><summary>Original abstract</summary>

This article investigates the nonparametric estimation of a common pooled marginal hazard function from right-censored durations exhibiting spatio-temporal dependence. We propose two estimators based respectively on the Nadaraya-Watson method and the (k)-nearest neighbors (k)-NN) approach. Under assumptions of stationarity, regularity, non-informative censoring, and weak spatio-temporal dependence, we establish their pointwise and uniform convergence rates as well as their optimal asymptotic order. A simulation study compares their finite-sample performance. Two real-data applications with right censoring are considered: a multicenter clinical trial with 53.8 percent censoring and 1,746 geolocated and time-stamped requests submitted to New York City's 311 municipal service, of which 35.5 percent are censored. The empirical results illustrate the relevance of the proposed methods in the presence of spatial and temporal dependence.

</details>

### [Sequential Selection against an Adaptive Opponent](https://arxiv.org/abs/2611.30006)
*Zhongyuan Lyu, Xiaocong Xu* · `stat.ML` · arXiv:2611.30006v1 · relevance 0.09

- **In one sentence**: The paper studies sequential strategy selection against an adaptive opponent, proposing SPAR for a single strategy (with privately randomized stopping and a rate inversely proportional to the error tolerance) and Screen-then-SPAR for choosing among several candidates, with simulations and two real-data studies.
- **In plain words**: The paper looks at how a player can pick a good strategy by testing it in practice games against an opponent that may change its behavior in response. The goal is to choose a strategy that meets a target win rate while rarely choosing one that has already dropped below that rate. The authors propose a stopping rule (SPAR) that builds up evidence from the games and stops using a randomly drawn threshold, and they extend it to screen several candidates before choosing one.
- **Why it matters**: Testing AI systems against opponents that adapt, such as in red-teaming or safety evaluations, is a practical problem where a strategy that looked good earlier may no longer work. The text reports that the sample-size rate is optimal even when the opponent does not adapt, and it tests the methods on coding-agent attack records and human rock-paper-scissors play; how far these results carry to other settings is not something the text establishes.
- **Background needed**: - Sequential testing: deciding when to stop collecting data based on what has been seen so far.
- Likelihood ratio: a measure of how much the data favor one hypothesis over another; "capped" means its contribution is limited.
- Error tolerance: the allowed chance of making a wrong selection.
- Minimax rate: the best worst-case rate, over all possible methods, at which the number of games needed can shrink as the tolerance is tightened.
- Randomized stopping: a rule that uses a random threshold drawn in advance, which the paper argues is necessary here.
- Adaptive opponent: one whose behavior changes in response to what it has observed. · level: research-level

<details><summary>Original abstract</summary>

Selecting a strategy by testing it against an opponent is common in game-playing AI, red-teaming of language models, and safety evaluations of AI agents. In many of these settings, the opponent adapts to what it observes, so a strategy that keeps winning in practice may already have stopped working by the time it is used. Motivated by these settings, we study a player who tries strategies in practice games against an adaptive opponent, decides when to stop, and then either selects one strategy for the next game or abstains. The goal is to select a strategy that meets a target win probability while rarely selecting one that has already fallen below it. For a single strategy, we propose the Sequential Private Accumulated-excess Rule (SPAR), which accumulates evidence through a capped likelihood ratio and selects the strategy once this evidence reaches a privately drawn uniform threshold. We show that the stopping time must involve such private randomness. The number of games SPAR needs is inversely proportional to the error tolerance, and this rate is optimal even when the opponent happens not to adapt. To select among multiple strategies, we introduce Screen-then-SPAR, which screens candidates in stages before applying SPAR. The procedure adapts to the best strategy's unknown initial margin above the target and achieves the minimax rate up to logarithmic factors. The performance of Screen-then-SPAR is demonstrated through simulations and two real-data studies, one using recorded coding-agent attacks from MonitoringBench and the other using rock-paper-scissors matches between human players and an adaptive bot.

</details>

## Statistical methods and applications

### [Targeted Learning for Externally Controlled Trials and Beyond](https://arxiv.org/abs/2611.28421)
*Yixin Fang, Weili He* · `stat.ML` · arXiv:2611.28421v1 · relevance 0.16

- **In one sentence**: The paper develops efficient influence function and targeted maximum likelihood estimators for a class of balancing-weight estimands in externally controlled trials, with extensions to trials augmented by external covariate data and to indirect treatment comparisons using individual and aggregate patient data.
- **In plain words**: When a new drug is tested in a single group of patients, researchers sometimes compare it with a control group drawn from older trials, patient registries, or real-world records instead of randomizing a concurrent control. This paper gives a statistical recipe for estimating the treatment effect in that setting while adjusting for differences between the two groups. The authors describe a method that is designed to be more reliable in finite samples, and they also show how the same approach can be applied to two related situations.
- **Why it matters**: Externally controlled trials are used when randomization is hard or unethical, so better-justified estimators matter for regulatory and medical decisions. The text does not report empirical results or comparisons, so its practical benefit beyond the stated theoretical properties cannot be judged from this summary alone.
- **Background needed**: - Externally controlled trial: a single-group trial whose control comparison comes from outside the trial (old trial, cohort study, or real-world data).
- Estimand: the precise quantity being estimated, such as an average treatment effect in a defined population.
- Balancing weights: numerical weights given to patients in the external group so that their covariates resemble those of the trial group.
- Efficient influence function: a mathematical object that describes how precisely an estimate can be made, used to derive the best-possible estimator.
- Targeted maximum likelihood estimation (TMLE): a two-step method that first models outcomes, then nudges them to reduce bias for the target quantity.
- Individual patient data (IPD) vs aggregate data (AgD): row-level records versus summary statistics published for a group.
- Indirect treatment comparison: comparing two treatments that were never tested head-to-head, via a common comparator. · level: research-level

<details><summary>Original abstract</summary>

This paper focuses on externally controlled trials (ECTs), which consist of a single-arm clinical trial supplemented by an external control arm (ECA). Potential data sources for the ECA can be broadly classified into three categories: (i) the control arm of a historical clinical trial, (ii) a concurrent cohort study, and (iii) external real-world data (RWD). In this paper, we consider a broad class of estimands defined through balancing weights. For a given estimand in the class, we discuss the efficient influence function (EIF) and the targeted maximum likelihood estimator (TMLE), together with practical implementation algorithms. Within the targeted learning framework, TMLE is a substitution estimator that enjoys several desirable theoretical properties and favorable finite-sample performance. Finally, the proposed framework is extended to two additional settings: (1) randomized controlled trials (RCTs) augmented with external covariate information to define a target population, and (2) indirect treatment comparisons (ITCs) that combine individual patient data (IPD) from an internal RCT with aggregate data (AgD) from an external RCT.

</details>

### [Threshold Generalized Autoregressive Moving Average Models](https://arxiv.org/abs/2611.28271)
*Katerine Zuniga Lastra, Airlane Pereira Alencar* · `stat.ME` · arXiv:2611.28271v1 · relevance 0.15

- **In one sentence**: The paper proposes threshold GARMA models, an observation-driven extension of generalized autoregressive moving-average models for non-Gaussian time series that switch between regimes based on a lagged threshold variable, with partial-likelihood estimation, information-criterion model selection, and an application to monthly respiratory hospitalization counts in São Paulo.
- **In plain words**: Many real-world counts, such as monthly hospital admissions, do not follow a simple steady pattern and can behave differently depending on the situation, for example in high versus low periods. This paper builds a statistical model that lets the rules governing the data switch between regimes depending on a past value of a chosen variable. The authors test it on monthly respiratory hospitalizations among older adults in São Paulo, Brazil, and report that it fits better in-sample than the single-regime version, measured by mean squared error.
- **Why it matters**: Count data with changing behavior are common in health and environmental monitoring, so a model that allows regime-dependent dynamics may be useful there. The evidence shown is limited to one application and in-sample error, so its value for forecasting or other datasets is not established by this text alone.
- **Background needed**: - Time series: data recorded in order over time, where past values help predict future ones.
- Non-Gaussian data: outcomes that are not bell-curve shaped, such as counts of events.
- GARMA models: extensions of ARMA models that handle non-normal outcomes by linking the mean to past observations and past errors.
- Threshold models: models that use different sets of rules depending on whether a variable is above or below a cutoff (the threshold).
- Partial likelihood: a way of estimating parameters when a full probability model is hard to specify completely.
- Information criteria (such as AIC or BIC): scores that balance model fit against complexity to choose among models.
- Mean squared error: the average squared gap between predicted and observed values; lower is better. · level: research-level

<details><summary>Original abstract</summary>

Non-Gaussian time series often exhibit nonlinear dynamics and changes in dependence structures that may not be adequately captured by conventional single-regime models. To address this limitation, we introduce a class of threshold generalized autoregressive moving-average (TGARMA) models that combines observation-driven GARMA dynamics with threshold-based regime switching. The proposed framework accommodates multiple regimes, determined by a lagged endogenous or exogenous threshold variable, and allows regression coefficients, autoregressive and moving-average orders and coefficients, and, where applicable, dispersion parameters to vary across regimes. Parameters are estimated by maximum partial likelihood, while model selection is conducted using information criteria. We examine model admissibility and stability, assess model adequacy through residual diagnostics, and conduct a Monte Carlo simulation study to investigate the finite-sample performance of the estimators. The proposed methodology is illustrated using monthly counts of hospitalizations due to respiratory diseases among older adults in S\~ao Paulo, Brazil. In this application, the TGARMA model outperforms its single-regime GARMA counterpart in terms of in-sample mean squared error, highlighting the potential benefits of incorporating regime-dependent dynamics into the analysis of non-Gaussian time series.

</details>

## AI industry news

### [Maple raises $5.3M to build AI products that protect your data, even from itself](https://techcrunch.com/2026/11/24/maple-raises-5-3m-to-build-ai-products-that-protect-your-data-even-from-itself/)
*Sarah Perez* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.18

- **In one sentence**: A funding announcement for Maple, a startup that says its encrypted AI architecture is built so the company itself cannot read users' private data.
- **In plain words**: A startup called Maple has raised $5.3 million to build AI products. The company says its design keeps users' private information locked up so that even Maple cannot see it. The article is short and gives only this high-level description, so the details of how it works are not clear from the text.
- **Why it matters**: Many AI tools require users to share personal data with the company running them, so a design that avoids this is of interest to people concerned about privacy. The text does not show how well the approach works in practice, so its value is still unproven.
- **Background needed**: - AI products often send user data to company servers to process it.
- "Encrypted" means data is scrambled so only holders of a secret key can read it.
- Some privacy designs aim for "zero-knowledge" setups, where a service can run without seeing the content, but the article does not say whether Maple uses one.
- Venture funding of $5.3 million is a modest seed-stage round.
- The article is a brief company announcement with little technical detail. · level: introductory

<details><summary>Original abstract</summary>

The startup's encrypted AI architecture is designed to prevent even the company itself from accessing users' private data.

</details>

### [Even the best AI agents struggle with everyday life](https://techcrunch.com/2026/11/24/even-the-best-ai-agents-struggle-with-everyday-life/)
*Rebecca Bellan* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.16

- **In one sentence**: A news piece reporting that a new benchmark finds even leading AI models often fail to complete everyday tasks reliably and safely, sometimes creating new problems while trying.
- **In plain words**: Millions of people now use personal AI assistants, the kind that can act on your behalf. The article describes a new test, called a benchmark, which found that even the most advanced AI models often fail to finish ordinary tasks dependably and safely, and can cause new problems along the way.
- **Why it matters**: It points to a gap between how widely these assistants are being adopted and how reliable they are in routine use. The text does not give details of the tasks, scores, or the test design, so its broader significance is hard to judge from this piece alone.
- **Background needed**: - AI agent: an AI system that does multi-step tasks for a user, such as booking, emailing, or browsing, rather than only answering questions.
- Benchmark: a standard test set used to measure and compare how well AI systems perform.
- Reliability and safety: whether the assistant gets tasks right consistently and avoids side effects, such as sending the wrong message or making an unwanted change.
- The article is short and gives no specific figures, named tests, or named models, so it should be read as a summary of a claim rather than a full account. · level: introductory

<details><summary>Original abstract</summary>

As millions embrace personal AI assistants, a new benchmark reveals that even the most advanced AI models struggle to complete everyday tasks reliably and safely without introducing potential new problems.

</details>

### [Microduck Obstacle Avoidance: A Sim2Real Workflow with Isaac Lab and Newton](https://huggingface.co/blog/nvidia/microduck-obstacle-avoidance)
** · `huggingface.co` · Hugging Face - Blog · relevance 0.09

- **In one sentence**: A news item titled "Microduck Obstacle Avoidance: A Sim2Real Workflow with Isaac Lab and Newton" describes a simulation-to-real-robot workflow for obstacle avoidance, but the body text is unavailable, so its specific methods and results cannot be confirmed.
- **In plain words**: This item is about teaching a small robot, called Microduck, to avoid obstacles by first training it in a computer simulation and then moving that training onto a real machine. The text provided is empty, so I cannot say what was built, how well it worked, or what results were reached.
- **Why it matters**: Moving robot skills from simulated training to physical hardware is a known challenge in robotics, so the topic may be of interest to people following robot learning. Beyond the title, I cannot judge its significance or what it connects to.
- **Background needed**: - Simulation (sim): a computer model of a robot and its surroundings where it can practice safely and quickly.
- Sim2Real ("sim to real"): the step of transferring a skill learned in simulation to a physical robot, which often behaves differently than the model predicted.
- Obstacle avoidance: a robot sensing and steering around objects in its path.
- Isaac Lab and Newton: software tools for robot simulation and training; the item's text does not explain their roles in detail.
- Microduck: the name of the small robot in the title; no further details are given in the provided text. · level: intermediate

<details><summary>Original abstract</summary>



</details>

### [Walmart teams up with Meta to bring Black Friday deals to AI agent Muse](https://techcrunch.com/2026/11/24/walmart-teams-up-with-meta-to-bring-black-friday-deals-to-ai-agent-muse/)
*Lauren Forristal* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.08

- **In one sentence**: Walmart says customers can now shop its Black Friday deals through Muse, an AI agent built by Meta.
- **In plain words**: Walmart has added its Black Friday sale items to Muse, a Meta AI assistant. Shoppers can use the assistant to look for and buy these deals without leaving the chat. The text is a short announcement and does not say how the feature works in detail.
- **Why it matters**: It is a small example of retailers putting their products inside AI assistants, a trend that could change how people find and buy things online. The text gives no sales figures or user numbers, so its wider impact is uncertain.
- **Background needed**: - An AI agent is a chatbot-style program that can carry out tasks for a user, such as searching for or buying products, not just answering questions.
- Muse is described here as Meta's AI agent; the text does not explain its features or how widely it is available.
- Black Friday is the November shopping day in the US when many retailers run large discounts.
- Partnerships like this one usually mean a store's product listings are connected to an AI platform, but the text does not describe the terms or data arrangements.
- The source is a brief news item, so the details of the deal are thin. · level: introductory

<details><summary>Original abstract</summary>

Walmart now lets customers shop Black Friday deals through Muse, Meta’s AI agent.

</details>

### [GPT-6 models demonstrate intrinsic protein-design capabilities](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities)
** · `openai.com` · OpenAI News · relevance 0.08

- **In one sentence**: A news item reports that GPT-6 models can design protein structures and sequences through reasoning and code, with lab tests reportedly finding evidence of binding across five targets.
- **In plain words**: The article says a new AI model called GPT-6 can help design proteins, the small molecular machines that make up much of living cells. According to the text, the AI reasoned its way to designs and wrote code to produce them, and lab tests found signs that these designs attached to five chosen targets. The text is very short, so it gives no details on how the tests were run or how strong the binding was.
- **Why it matters**: If accurate, AI that designs working proteins could speed up drug and biotech research, which is why it draws attention. The article is too brief to show how significant the result is, and it does not name a source, paper, or independent check, so the claim should be treated cautiously until more detail appears.
- **Background needed**: - Proteins are chains of molecules that do most of the work in living cells; their shape determines their job.
- "Protein design" means creating new protein sequences or shapes for a purpose, such as treating disease.
- "Binding" means one molecule sticking to another, often a key step in how drugs act.
- A "target" is the specific molecule a designed protein is meant to bind to.
- "Lab tests" usually mean experiments in a physical lab, but the article gives no details of them.
- "GPT" refers to a family of large language models; the article does not explain what GPT-6 is or who built it. · level: intermediate

<details><summary>Original abstract</summary>

GPT-6 models design protein structures and sequences using reasoning and code. Lab tests found evidence of binding across five targets.

</details>

## Model architectures and training

### [PVFormer: Proper Velocity Transformer for Stable and Scalable Hyperbolic Representation Learning](https://arxiv.org/abs/2611.30785)
*Xianglong Shi, Nicu Sebe, Bernhard Sch\"olkopf et al.* · `cs.LG` · arXiv:2611.30785v1 · relevance 0.32

- **In one sentence**: PVFormer is a Transformer that performs all three self-attention steps (transformation, similarity, aggregation) natively in the proper velocity model of hyperbolic space, aiming to keep the whole block intrinsic to that geometry and scalable to large graphs.
- **In plain words**: Many AI models store data as points in a curved space, which suits data with tree-like hierarchies, such as family trees or taxonomies. Building the standard Transformer (the attention-based architecture behind many language models) in this curved space has been awkward, so existing versions often rely on workarounds. This paper proposes PVFormer, which redesigns the Transformer's parts directly in a different coordinate system called proper velocity space, and reports that it works across graph, text, and vision tests.
- **Why it matters**: It addresses a real design gap: earlier hyperbolic Transformers used bounded coordinates or projection steps that can make them harder to keep stable and to scale. Whether this gives practical gains beyond the reported benchmarks is not something the summary text can establish.
- **Background needed**: - Hyperbolic space: a curved geometry in which tree-like data can be embedded with less distortion than in flat space.
- Transformer self-attention: a mechanism where each item compares itself with others (similarity) and then blends their information (aggregation), with a transformation step beforehand.
- Models of hyperbolic space: Poincaré and Lorentz models are common coordinate systems; the paper argues their constraints cause trouble.
- Proper velocity: an alternative, unconstrained coordinate system for the same hyperbolic geometry.
- Busemann score and midpoint: geometric analogues of a dot-product score and an average, adapted to curved space.
- Linear attention: a cheaper variant of attention whose cost grows more gently with data size, relevant for large graphs. · level: research-level
- Matched keywords: transformer, attention, linear attention, architecture

<details><summary>Original abstract</summary>

Hyperbolic representations have shown remarkable success on hierarchical and tree-like data, and Transformers have become a central architecture for representation learning. However, a principled construction of hyperbolic Transformers remains challenging because the self-attention layer decomposes into three coupled primitives, transformation, similarity, and aggregation, that should all respect the underlying geometry. Existing hyperbolic Transformer designs are typically built in the Poincar\'e or Lorentz models, where bounded domains, time-like constraints, tangent-space detours, or projection steps make it difficult to keep the full block intrinsic and scalable. To address this gap, we propose PVFormer, to the best of our knowledge, the first Transformer architecture that operates natively in proper velocity (PV) space. The proper velocity model provides an unconstrained representation of hyperbolic geometry, and PVFormer exploits this structure to redesign the Transformer block in PV space. On the transformation side, we use PV homomorphism transformations to update query and value representations. On the similarity side, we generalize Euclidean inner-product attention with a PV Busemann score inspired by Busemann-based hyperbolic learning and a PV point-to-hyperplane key transformation. On the aggregation side, we replace Euclidean averaging with PV midpoint aggregation and further derive a scalable PV linear attention variant for large graphs. Extensive experiments support the effectiveness of PVFormer across graph, text, and vision benchmarks.

</details>

### [Orthogonally Mixed Sign Coding with Progressive Residual Refinement for Transformer Weight Compression](https://arxiv.org/abs/2611.31089)
*Anindya Roy Chowdhury, Atanu Barai, Nandakishore Santhi* · `cs.AI` · arXiv:2611.31089v1 · relevance 0.30

- **In one sentence**: A training-free, residual sign-based weight quantization method for Transformers that uses randomized orthogonal mixing to make residuals more Gaussian-like, evaluated on GPT-2 Large and Llama-3-8B.
- **In plain words**: Large language models store huge numbers of weights, and compressing them usually hurts how well they predict text. This paper proposes a way to compress a model's weights by repeatedly storing only the sign (positive or negative) of the leftover error, after first shuffling the weights with a randomizing rotation. On GPT-2 Large and Llama-3-8B, the authors report perplexity (a measure of how surprised the model is by text, where lower is better) of 32.16 and 12.73 after five stages, versus 29.89 and 11.07 for the uncompressed models.
- **Why it matters**: Compressing models without any retraining or calibration data would make them cheaper to store and run, which matters for deploying them on modest hardware. The text reports the accuracy gap at five stages and says ablations support the design choices, but it does not show how the storage savings compare in practice with established quantizers beyond a general claim of trade-offs.
- **Background needed**: - Quantization: storing model weights with fewer bits to save memory.
- Perplexity: a standard score for language models; lower means better prediction. Going from 29.89 to 32.16 is a measurable but modest loss.
- Residual coding: storing an approximation, then storing the leftover error, and repeating to refine it.
- Sign coding: keeping only whether a value is positive or negative, which costs about one bit per value.
- Orthogonal mixing: a reversible rotation of values that spreads information out so they look more like a bell-curve (Gaussian) distribution.
- Training-free: the method needs no gradient-based retraining of the model. · level: research-level
- Matched keywords: transformer, attention, quantization

<details><summary>Original abstract</summary>

LLM quantization reduces storage but often degrades predictive fidelity at low bit rates. We propose a training-free, CDF-free, Gaussian-CLT-motivated progressive residual-sign quantization framework that uses randomized orthogonal mixing to promote Gaussian-like residual distributions and improve sign based reconstruction of Transformer weights. Each stage independently normalizes residuals and analytically calibrates reconstruction, progressively recovering quantization errors. The framework enables flexible storage-fidelity trade-offs without learned codebooks, empirical CDFs, or trellis optimization. We evaluate GPT-2 Large and Llama-3-8B across attention and MLP projections. At five residual stages, joint quantization preserves near-baseline predictive fidelity, achieving perplexities of 32.16 and 12.73, compared with full-precision values of 29.89 and 11.07, respectively. Ablations further demonstrate that orthogonal mixing substantially improves reconstruction over identity-based sign coding, while activation-aware scaling improves output fidelity and reduced-precision statistics lower storage overhead with negligible perplexity degradation. Comparisons with conventional quantizers establish the method's progressive fidelity recovery and characterize its storage-quality and runtime trade-offs. These results demonstrate the effectiveness of orthogonally mixed residual-sign coding for flexible, training-free Transformer weight compression.

</details>

## Machine learning theory

### [Nearly Minimax-Optimal Sample Complexity of Natural Policy Gradient with a Matching Information-Theoretic Lower Bound](https://arxiv.org/abs/2611.28628)
*Asha Barua, Sajad Khodadadian* · `cs.LG` · arXiv:2611.28628v1 · relevance 0.28

- **In one sentence**: This paper gives last-iterate sample-complexity guarantees for sample-based natural policy gradient in tabular finite-horizon MDPs with a generative model, showing an O~(SAH^4/ε^2) upper bound that matches a stated information-theoretic lower bound up to logarithmic factors, plus an iteration lower bound for exact NPG with step size 1/H.
- **In plain words**: The paper asks how many sampled experiences a learning agent needs to find a nearly optimal decision policy, and whether a particular method that adjusts the policy directly (natural policy gradient) can reach that minimum. The authors build sample-based versions of this method that update the policy by sweeping backward through the time steps, without estimating the transition probabilities. They report that the number of samples needed matches a lower bound on what any method must use in the worst case, up to logarithmic factors.
- **Why it matters**: It addresses whether a widely used policy-optimization method can be statistically optimal, which bears on the theory of reinforcement learning. The claim of matching a lower bound is the central point, but the text alone does not let me verify the proofs or compare against the wider literature, so readers should check the technical details.
- **Background needed**: - Markov decision process (MDP): a model of sequential decisions where outcomes depend on the current state and chosen action.
- Policy: a rule for choosing actions in each state.
- Horizon H: the number of time steps in an episode; transition kernel: the probabilities of moving between states.
- Generative model: an oracle that lets the learner query any state-action pair for a sampled next state.
- Natural policy gradient: a policy update that takes gradient steps adjusted for the geometry of the policy space.
- Sample complexity: how many samples are needed to reach error ε; minimax/lower bound: a worst-case limit no method can beat.
- Last-iterate guarantee: a performance bound on the final policy, not an average over iterations. · level: research-level
- Matched keywords: sample complexity, minimax

<details><summary>Original abstract</summary>

A fundamental question in reinforcement learning is how many sampled transitions are needed to learn a near-optimal policy, and whether direct policy optimization can attain this statistical limit. To answer this question, we consider natural policy gradient (NPG), a widely used policy optimization method. We study tabular finite-horizon Markov decision processes (MDPs) with known rewards and unknown horizon-dependent transition kernels, accessed through a generative model. Our sample-based NPG algorithms update the policy by backward sweeps and do not estimate transition probabilities. Under three different batch-size and step size schedules, we establish last-iterate guarantees with sample complexity $\widetilde O(SAH^4/\varepsilon^2)$, where $S$, $A$, and $H$ denote the number of states, the number of actions, and the horizon length, respectively. In this setting, horizon-dependent transition kernels contribute a factor of $H$ to our transition-query bound. Our information-theoretic lower bound of $\Omega(SAH^4/\varepsilon^2)$ shows that the resulting $H^4$ dependence is unavoidable in the worst case, even for agents that select their queries adaptively. To the best of our knowledge, these are the first last-iterate guarantees for NPG whose sample complexity matches an information-theoretic lower bound up to logarithmic factors. Consequently, our results demonstrate that direct policy-space optimization through NPG can achieve the fundamental statistical limits of reinforcement learning while guaranteeing the performance of the final policy. Furthermore, for known kernels, we prove that exact NPG with a constant step size $\eta=1/H$ requires $\Omega(H^2/\varepsilon)$ iterations in the worst case, matching the known upper bound for that step size.

</details>

### [Optimal User-Level Private Stochastic Convex Optimization and Mean Estimation with Heavy Tails](https://arxiv.org/abs/2611.28460)
*Andrew Lowy* · `cs.LG` · arXiv:2611.28460v1 · relevance 0.25

- **In one sentence**: This paper gives minimax-optimal excess risk bounds for user-level (ε, δ)-differentially private stochastic convex optimization and mean estimation when per-sample Lipschitz parameters are heavy-tailed, requiring only bounded second and k-th moments, and it closes an approximate-DP gap in directional-moment mean estimation.
- **In plain words**: The paper studies how to learn a good model from data held by many different users while protecting each user's whole set of records from being revealed. It allows the gradients used in learning to be extremely variable, with occasional very large values, instead of assuming they are capped. The authors report matching upper and lower bounds (up to logarithmic factors) on how accurate the learned result can be, and an algorithm that reaches this with about 1/ε users.
- **Why it matters**: Real data often has heavy tails, where a few extreme values break standard privacy guarantees that assume bounded inputs, so relaxing that assumption while keeping optimal accuracy is a meaningful theoretical step. The text presents the results as tight and optimal, and the mean-estimation byproducts improve on prior work by named authors; I cannot judge from the abstract alone how practical the algorithm is.
- **Background needed**: - Differential privacy: a guarantee that an algorithm's output barely changes if one person's data is swapped out; (ε, δ) is the standard parameterization, with δ a small failure allowance.
- User-level privacy: protects all samples belonging to one user, not just a single record, which is stronger than item-level privacy.
- Stochastic convex optimization: minimizing a convex loss function using noisy gradient samples drawn from an unknown distribution; "excess population risk" measures how far the result is from the best possible model.
- Lipschitz constant: a bound on how fast a function can change; here it is allowed to be random and unbounded.
- Heavy tails: distributions where extreme values occur more often than in a bell curve, so higher moments may be infinite or hard to bound.
- Moments: summary measures of how large values get (second moment relates to variance, k-th moment to higher tail behavior).
- Mean estimation: estimating the average of a distribution from samples.
- Minimax optimal: the best worst-case rate any algorithm could achieve. · level: research-level
- Matched keywords: sample complexity, minimax

<details><summary>Original abstract</summary>

We study stochastic convex optimization with heavy-tailed stochastic gradients under $(\varepsilon, \delta)$-user-level differential privacy, which protects each user's entire collection of samples. Instead of assuming a uniformly bounded Lipschitz constant, we only assume bounds on the second- and $k$-th moments of the random sample Lipschitz parameters. This allows for unbounded, heavy-tailed stochastic gradient distributions and can lead to sharper excess risk bounds. We characterize the minimax optimal excess population risk up to logarithmic factors. Our algorithm achieves the optimal rate with only $\widetilde{O}(1/\varepsilon)$ users. As a byproduct of our algorithmic developments, we obtain tight bounds for user-level private mean estimation under norm-moment assumptions, improving over the guarantees of Esfandiari et al. (2022) and Zhao et al. (2024). Finally, for mean estimation under the directional-moment assumption of Agarwal et al. (2025), we close their remaining approximate-DP gap by removing the additional $d/\varepsilon$ user requirement and attaining the optimal sample complexity up to logarithmic factors.

</details>

## Large language models

### [Retrieval-Augmented Generation in the Agentic Era: Tradition, Present, and Prospect](https://arxiv.org/abs/2611.30181)
*Chenming Tang, Haolin Li, Yiran Li et al.* · `cs.CL` · arXiv:2611.30181v1 · relevance 0.20

- **In one sentence**: A survey that organizes retrieval-augmented generation (RAG) along one lifecycle axis, from offline indexing through pre-retrieval, retrieval, post-retrieval and orchestration, and treats agentic workflows as a paradigm of their own.
- **In plain words**: Language models answer questions from what they memorized during training, which can be outdated or wrong. This paper is a review of a common fix: letting the model look up material from an external, updatable source before it answers. It maps the whole process, from preparing the document store to deciding how the model uses what it finds, and it covers newer setups where the model acts as an agent that plans and repeats lookups.
- **Why it matters**: Retrieval is one of the main ways people try to make language model answers more current and checkable, so a structured overview is useful for anyone building or evaluating these systems. The text does not give evidence of new experimental results; its value is as a map of existing work, and its significance for the field is for readers to judge.
- **Background needed**: - Language models generate text from patterns learned in training (their "parametric memory").
- RAG adds a step that searches an outside collection of documents and feeds relevant passages to the model.
- Indexing means preparing searchable representations of documents ahead of time.
- Pre-retrieval and post-retrieval refer to steps before the search (e.g., rewriting the question) and after it (e.g., filtering or condensing results).
- Orchestration means coordinating these steps, often with an agent that decides what to do next.
- "Agentic" refers to systems that plan, take actions, and loop through tool use rather than producing a single answer. · level: intermediate

<details><summary>Original abstract</summary>

Retrieval-augmented generation (RAG) couples frozen language models with external, updatable knowledge, so that generation is grounded in retrieved evidence rather than in parametric memory alone. This work maps RAG in the agentic era by joining them on a single lifecycle axis, from offline indexing through pre-retrieval, retrieval, post-retrieval, and orchestration over these stages. It treats indexing and orchestration as first-class components and agentic workflows as a paradigm of their own, and it covers the agentic work that has appeared since those reviews. Beyond these components, it covers evaluation, applications, and the questions that remain open for future exploration. From tradition to present and beyond, this work systematically reviews RAG from a perspective of the agentic era.

</details>

### [FiRE: Fine-grained Ranking Evaluation for Machine Translation](https://arxiv.org/abs/2611.30168)
*Wenyang Gao (Zhejiang University, School of Engineering, Westlake University) et al.* · `cs.CL` · arXiv:2611.30168v1 · relevance 0.18

- **In one sentence**: FiRE proposes reference-free, criterion-driven pairwise ranking of machine translations by off-the-shelf LLMs along faithfulness, fluency, and style consistency, plus a new human-annotated benchmark and an analysis of LLM evaluator biases.
- **In plain words**: Companies and researchers need a reliable way to tell which machine translation is better, without a human-written reference translation to compare against. This paper proposes asking a large language model to compare two translations side by side on three separate qualities (accuracy to the source, smoothness of the language, and consistent style), rather than giving one overall score. The authors also built a new set of translations ranked by human annotators to test the method, and report that it agrees with human comparisons better than the older scoring approaches they tested.
- **Why it matters**: Better evaluation is what lets translation systems be improved and compared fairly, and the paper's finding that LLM judges show position and self-preference biases is useful for anyone using LLMs as graders. The claimed gains are based on the authors' own benchmark and existing MQM datasets, so they should be checked by independent work.
- **Background needed**: - Machine translation (MT): software that converts text from one language to another.
- Reference-free evaluation: judging a translation using only the source and the output, with no human "correct" translation.
- Pairwise comparison: showing a judge two outputs and asking which is better, instead of scoring each one.
- Large language models (LLMs) as judges: using a general AI chat model to grade outputs.
- Regression-based metrics: scoring methods trained to predict human ratings with a numeric formula.
- MQM (Multidimensional Quality Metrics): a framework where human experts label and weight translation errors.
- Inter-annotator agreement: how consistently different human raters give the same judgments; a measure of label reliability.
- Position and self-enhancement bias: tendencies for a judge to favor an option based on its order or on the judge's own style of output. · level: intermediate

<details><summary>Original abstract</summary>

Developing reliable machine translation (MT) systems hinges on our ability to distinguish superior translations from inferior ones. However, existing evaluation paradigms, whether limited to coarse overall rankings or misaligned with human preferences, fail to deliver interpretable, fine-grained feedback in reference-free settings. We present a Fine-Grained Ranking Evaluation method (FiRE) that leverages off-the-shelf large language models to perform criterion-driven pairwise comparison across three complementary dimensions: faithfulness, fluency, and consistency of style, instead of producing a single holistic judgment. To enable rigorous meta-evaluation of evaluation paradigms in the absence of any suitable testbed, we construct the first human-annotated, reference-free benchmark for fine-grained ranking evaluation, achieving substantial inter-annotator agreement. Through meta-evaluation on this benchmark and existing MQM datasets, FiRE demonstrably outperforms regression-based and error-analysis metrics in aligning with human comparative judgments, while providing more informative insights into translation quality. Finally, our examination of LLM evaluator biases (position and self-enhancement) and their handling of tied cases offers guidance for more nuanced MT evaluation. Code and benchmark resources are available at https://github.com/wygao8/FiRE-MT.

</details>

## Computer vision

### [Benchmarking VLM Medical Hallucination across 5 Modalities](https://arxiv.org/abs/2611.29934)
*Zhixing Cao, Yusen Peng* · `cs.CV` · arXiv:2611.29934v1 · relevance 0.18

- **In one sentence**: Introduces Multi-Med, a 1,000-item medical hallucination benchmark spanning five imaging modalities, and uses it to evaluate 10 vision-language models across four question categories.
- **In plain words**: Vision-language models are AI systems that answer questions about images, and they sometimes make up details that the picture does not show. This paper builds a test set of 1,000 medical image and question pairs covering five kinds of medical imaging, then checks how 10 popular models perform. The authors report that accuracy varies a lot by imaging type and question type, while the top models are not clearly different from one another statistically.
- **Why it matters**: Medical AI tools that describe scans can be wrong in ways that matter, so knowing where they fail is useful for deciding where they can be trusted. The text does not say how the benchmark will be used beyond this study, so its wider impact is unclear.
- **Background needed**: - Vision-language model (VLM): an AI system that takes both an image and a text question and produces a text answer.
- Hallucination: when an AI states something confidently that is not supported by its input, such as describing a finding that is absent from a scan.
- Benchmark: a standard set of test questions used to compare systems fairly.
- Imaging modality: the type of medical image, such as X-ray, MRI, CT, or ultrasound.
- Statistical significance: whether a difference in scores is likely real rather than due to chance in a limited test.
- The abstract does not name the five modalities or the four question categories, so those details are not covered here. · level: intermediate

<details><summary>Original abstract</summary>

Hallucinations in Vision-Language Models (VLMs) within the medical domain remain a difficult and not well-understood problem, and it is still unclear where these models break down. Although several benchmarks targeting medical hallucination have been introduced, they often lack broad coverage across different medical imaging modalities. We introduce Multi-Med, a medical hallucination benchmark containing 1,000 image-question pairs spanning five distinct modalities. Using this benchmark, we perform an in-depth experimental study of 10 widely used VLMs across five modalities and four question categories. Our findings indicate that model performance differs substantially depending on the imaging modality and question type, and that the differences among the best-performing models are not statistically significant.

</details>

### [SVUBench: A Comprehensive Benchmark for Proactive Streaming Video Understanding](https://arxiv.org/abs/2611.30541)
*Yuxuan Liang, Bohan Zhang, Haiyang Yu et al.* · `cs.CV` · arXiv:2611.30541v1 · relevance 0.17

- **In one sentence**: SVUBench is a benchmark of about 12,000 questions across ten tasks for testing whether video models can proactively respond to unfolding streaming video, using a new Proactive Response Score that accounts for correctness, timeliness, historical consistency, and content quality.
- **In plain words**: This paper introduces a test set for AI systems that watch live or streaming video and must speak up at the right moment, rather than only answering questions after a clip has finished. The benchmark has over 12,000 questions and about 63,000 answer points, built with help from AI models and checked by humans. The authors also propose a scoring method that judges not just whether answers are right, but whether they arrive on time and stay consistent with earlier events.
- **Why it matters**: Streaming video assistants, such as those that monitor a camera feed and alert a user, need to act in real time, and standard benchmarks do not measure that well. The paper reports that extensive experiments reveal strengths and limitations of existing models, but the text does not give specific results, so its practical impact is not yet clear from this summary alone.
- **Background needed**: - Streaming video: video that arrives continuously, so the model sees only the past and present, not the full clip.
- Proactive response: the model decides on its own when to answer, rather than waiting for a question.
- Benchmark: a standardized test set used to compare models fairly.
- Answer window: the time span during which an answer counts as on time.
- Historical recovery: recalling relevant earlier moments in the video to answer correctly.
- Duration tiers: the test groups videos by length to see how performance changes as videos get longer. · level: intermediate

<details><summary>Original abstract</summary>

Proactive streaming video understanding requires models to interpret unfolding events, respond timely, and retrieve relevant historical evidence. To systematically evaluate these capabilities, we introduce SVUBench, a comprehensive proactive streaming video benchmark comprising 12,131 questions and 62,881 answer points across ten proactive tasks spanning Perception, Understanding, and Reasoning. Constructed through model-assisted annotation and human verification, SVUBench introduces two complementary interaction modes. Basic evaluates sustained proactive responses from video onset, while Trajectory requires historical recovery and continuous response updates following task activation during streaming. A Duration-Scaled Challenge further evaluates these capabilities across four video duration tiers. We develop the Proactive Response Score (PRS) with task-adaptive answer windows to jointly assess answer correctness, response timeliness, historical consistency, and content quality. Extensive experiments and analysis reveal the strengths and limitations of existing models, highlighting directions for advancing proactive streaming video understanding.

</details>

## Reinforcement learning

### [Adopting AI Technologies without Traps: A Multi-Agent Reinforcement Learning Framework](https://arxiv.org/abs/2611.30200)
*Jitong Yang, Avinash Reddy Mudireddy, Ziqing Lu et al.* · `cs.AI` · arXiv:2611.30200v1 · relevance 0.27

- **In one sentence**: The paper proposes a general multi-agent Markov decision process (MARL) framework, covering human and AI agents, for finding long-term optimal strategies for adopting AI, and applies it to skill erosion from AI offloading, firm workforce structure, and labor/trading equilibria.
- **In plain words**: The paper asks how people and firms can adopt AI tools without falling into long-term traps, such as losing skills, losing jobs, or losing training opportunities. It builds a modeling framework in which human and AI agents make decisions over time, and negative effects appear as bad state changes or negative rewards. The authors apply this framework to three cases: skill erosion from handing tasks to AI, the best mix of human staff for a firm using AI, and the economic balance of trading and employment between humans and AI.
- **Why it matters**: Concerns about AI reducing human skills and jobs are widely discussed, and this paper offers a formal way to model those long-term effects using decision-making tools. The text is a framework description and does not show what the optimal strategies turn out to be in concrete numbers, so its practical value is not yet established from this excerpt alone.
- **Background needed**: - Markov decision process (MDP): a standard way to model decisions over time, where an agent picks actions, the world moves to a new state, and the agent receives a reward.
- Reinforcement learning (RL): a method where an agent learns which choices lead to the best long-term reward through trial and feedback.
- Multi-agent RL (MARL): several learning agents interacting in the same environment, here both human and AI agents.
- State transition: a change in the situation (for example, a worker's skill level) caused by an action.
- Economic equilibrium: a stable point where no participant gains by changing behavior on their own.
- Skill erosion: losing a capability through disuse, such as when a task is always done by a machine. · level: research-level
- Matched keywords: reinforcement learning, Markov decision process

<details><summary>Original abstract</summary>

AI technologies and AI agents play increasingly important roles in human society, including in education, economics, and research. Adopting AI technologies can bring immediate, and sometimes tremendous, rewards such as through productivity boost, but they can also bring negative effects including but not limited to losses of job and training opportunities, and cognitive capability declines. Thus, it is important to investigate the optimal ways of adopting AI technologies without different traps. In this paper, we develop a general multi-agent Markov decision process (MDP) based reinforcement learning (RL or MARL) modeling framework for determining and analyzing optimal adoption of AI technologies. This framework can model the long-term dynamic effects of AI adoption, and lead to finding the optimal AI adoption strategies. In our modeling framework, the negative effects of AI adoption are modeled by undesirable state transitions or negative rewards in the MDPs. The proposed multi-agent RL MDPs incorporate both human agents and AI agents. The key idea of our models is that incorporating AI technologies may not only increase the immediate rewards for AI agents but also alter the states of the involved human and AI agents. In particular, we apply this framework to analyzing AI offloading leading to skill erosion, to analyzing optimal human resource structures for a firm adopting AI, and to analyzing the economic equilibria in the trading/employment among human and AI agents. Since the multi-agent MDP based RL technique is from control, machine learning and AI, this research is essentially using an AI technique to determine the optimal ways of adopting or co-existing with AI without traps.

</details>

### [From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](https://arxiv.org/abs/2611.29303)
*Saadh Jawwadh* · `cs.CL` · arXiv:2611.29303v1 · relevance 0.27

- **In one sentence**: A review that walks through 22 influential publications on large language models (1997 to 2026), organized as a chronological cause-and-effect taxonomy, covering RNNs, LSTMs, Word2Vec, Transformers, scaling laws, RLHF, jailbreaks, and recent work on model collapse and self-improving agents.
- **In plain words**: This is a survey that tries to sort out which AI research results were real turning points and which were small refinements, by following one line of work from older neural networks through today's chatbots. It explains each step in everyday terms, such as a memory mechanism that decides what to keep, and then covers newer concerns like safety guardrails being easy to bypass and AI systems being trained on AI output. The text provided is a short abstract-style description, so it does not show the detailed evidence behind each claim.
- **Why it matters**: It offers a single narrative connecting early sequence models to current safety problems, which may help non-specialists see how the pieces relate. The abstract gives only the outline, though, so readers should check the cited papers themselves before relying on its judgments of which work mattered most.
- **Background needed**: - Recurrent neural network (RNN): a model that reads text one word at a time and carries a running memory; it tends to lose early context.
- Long Short-Term Memory (LSTM): an RNN variant with gates that control what is kept, updated, or output.
- Word2Vec: a method that represents words as numerical vectors so that meaning relationships become arithmetic.
- Transformer and attention: an architecture where every word can look at every other word; powerful but costly as text grows.
- Scaling laws (Chinchilla): the finding that model size and training data should grow together.
- RLHF: training a model using human preference ratings to make it behave more helpfully and safely.
- Jailbreak: a crafted prompt that gets a model to ignore its safety training.
- Model collapse: quality degradation when models are trained on output generated by other models. · level: introductory
- Matched keywords: reinforcement learning, RLHF

<details><summary>Original abstract</summary>

The rapid proliferation of Large Language Model (LLM) research makes it increasingly difficult to distinguish incremental refinements from true paradigm shifts. This review evaluates 22 of the most influential publications spanning nearly three decades (1997-2026), organized through a causal, chronologically anchored taxonomy centered on the author's birth year (1999). Beginning "before 1999" with how recurrent neural networks (RNNs) forgot earlier context (much like forgetting Chapter 1 by the time a reader reaches Chapter 9), we trace how Long Short-Term Memory (LSTM) networks introduced a "bouncer" mechanism of forget, input, and output gates to selectively preserve long-term memory. We then examine how Word2Vec turned language into vector mathematics (king - male + female ~ queen), why sequential RNNs hit a parallelization wall, and how the Transformer's all-to-all attention weights launched the modern LLM era alongside a quadratic bottleneck. Next, we analyze why scaling parameters alone leaves capacity under-trained unless data scales equally (Chinchilla), how Reinforcement Learning from Human Feedback (RLHF) left alignment superficial, and how that gap compounded into adversarial jailbreaks and single-direction refusal subspaces (J-space), where instructing a model not to think of a restricted concept surfaces it much like the human "red ball" paradox. Finally, we synthesize the current state of AI (2024-2026), encompassing recursive model collapse, autonomous reasoning-model jailbreak agents, machine-speed agentic intrusions, and closed-loop recursive self-improvement (AIDE^2).

</details>

## AI safety and alignment

### [Tracing Attacker Diversity Reduction in Adaptive LLM Red Teaming](https://arxiv.org/abs/2611.29960)
*Chris Tava* · `cs.LG` · arXiv:2611.29960v1 · relevance 0.22

- **In one sentence**: A controlled study of reinforcement-learning-based automated red teaming finds that the attacker's diversity collapses over training, traces the narrowing to a success-only reward signal acting through the group-relative advantage, and reports winner-neighbor and common-opening effects.
- **In plain words**: Researchers use one AI model to generate attacks that try to make another AI model misbehave, and they train the attacker to get better at succeeding. This paper asks how the attacks become less varied over time, and where in that training loop the narrowing starts. Across three experiment setups over 24 training rounds, they found that a frozen defender narrowed diversity earlier than a co-trained one, that defender updates delayed but did not stop the narrowing, and that rewarding only successes appears to be the main source.
- **Why it matters**: If automated red teaming keeps producing a narrow set of attacks, safety testing may miss whole classes of failures, so the finding bears on how reliable such testing is. The text does not show how far these results generalize beyond the authors' setup, so the broader significance is uncertain.
- **Background needed**: - Red teaming: deliberately trying to make an AI system fail, to find weaknesses before deployment.
- Attacker, defender, judge: in this setup, one model writes attacks, another model responds, and a third model decides whether each attack succeeded.
- Reinforcement learning: training by rewarding outcomes, here rewarding the attacker for successful attacks.
- Group-relative advantage: a training signal that scores each attack against the average of its batch, so attacks are pushed up or down relative to their peers.
- Attack diversity retention (ADR): a measure of how much variety remains among generated attacks; lower means narrower.
- Winner-neighbor advantage: attacks similar to past successful ones succeed more often than those similar to past failures.
- Percentage points: the difference between two success rates, e.g. going from 40% to 50% is 10 points. · level: research-level
- Matched keywords: red teaming

<details><summary>Original abstract</summary>

Reinforcement learning can increase the success of automated red teaming but it also narrows the attack vector. This study asks where in the attacker-defender-judge learning loop does the narrowing begin and which mechanisms lead to a narrowing attack. Six mechanisms (defender adaptation, success edge, reward reinforcement, row cap, update size, and measurement) are tested across three experiment arms (co-trained, frozen defender, half learning rate) for twenty-four iterations. A frozen defender narrows attack diversity retention (ADR) earlier 0.496 relative to co-trained 0.891 at iteration twelve. Defender updates delay narrowing but dont prevent it. Successful attacks ("winners") have narrower attack diversity than the full set of generated attacks. Attacks closest to previous winners succeed 10-15 percentage points more often than those closest to previous failures. This winner-neighbor advantage holds after a defender update and for a fixed defender too. Attacks with a common opening have a common-opening advantage of 5-16 percentage points. The training row cap and update size account for little impact on ADR, and attack length accounts for only part of the ADR decrease. Narrowing appears to originate from the success only reward through the group-relative training advantage to the attacker update, with a persistent success edge setting the direction.

</details>

### [Uncovering Hidden Behaviours in Language Models via Limited-Parameter Finetuning](https://arxiv.org/abs/2611.30672)
*Boyd Kane, Jo J. Jiao, Elizabeth Donoway et al.* · `cs.AI` · arXiv:2611.30672v1 · relevance 0.20

- **In one sentence**: The paper proposes limited-parameter finetuning (LPF), which trains a small fraction (3-25%) of LoRA parameters on examples of a target behaviour, as a way to reveal hidden behaviours in language models that standard behavioural evaluations miss.
- **In plain words**: AI models can sometimes act in unwanted ways, but only in situations that are hard to predict, so testers who check the model with ordinary questions may miss the problem. This paper tries a different check: it briefly retrains a small slice of the model on examples of the suspected behaviour and sees whether the hidden behaviour shows up. The authors report that this works on test models with planted hidden behaviours and on some naturally occurring ones in larger open models.
- **Why it matters**: Safety audits depend on what testers think to try, so a method that can detect hidden behaviour without needing the triggering context could be a useful addition to auditing toolkits for frontier models. The authors themselves say they have not compared it against other methods in a realistic auditing setting, so its practical value is still unclear.
- **Background needed**: - Alignment audit: checking whether an AI model behaves in ways its developers did not intend.
- Hidden behaviour: a model behaviour that appears only in rare or hard-to-anticipate contexts, so ordinary testing does not reveal it.
- Finetuning: further training of an existing model on new examples to change or probe its behaviour.
- LoRA: a method that adds small trainable adapter layers, so only a small share of the model's parameters are updated.
- Model organism: a deliberately built test model with a known behaviour, used to check whether detection methods work.
- Open-weight model: a model whose trained parameters are publicly downloadable. · level: research-level
- Matched keywords: alignment

<details><summary>Original abstract</summary>

Large language models can have behaviours which only arise in hard-to-anticipate contexts. These hidden behaviours pose a challenge to alignment audits, which seek to uncover problematic model behaviour but are limited by the scenarios the auditor can anticipate. To address this challenge, we explore limited-parameter finetuning (LPF) on examples of a target behaviour. While training 3-25% of LoRA parameters, LPF reveals whether the model has a hidden behaviour, even when standard behavioural evaluations cannot. LPF succeeds on a suite of model organisms with hidden behaviours (8-14B parameters), and also surfaces naturally occurring hidden behaviours in open-weight models (27-35B parameters). LPF can thus distinguish between models which appear behaviourally identical to an auditor, and does not require the context in which the hidden behaviour surfaces. LPF provides a novel affordance that may be useful for auditing frontier AI models. However, we do not evaluate LPF against baselines in a realistic auditing setting, so further work is needed to determine its practicality.

</details>

## Interpretability

### [Beyond Patching: Consistent Circuit Discovery via Gradient Spectral Analysis](https://arxiv.org/abs/2611.30939)
*Yujie Zhang, Tianyi Zhao, Guanghui Min et al.* · `cs.LG` · arXiv:2611.30939v1 · relevance 0.23

- **In one sentence**: Proposes Spectral Circuit Analysis (SCA), a counterfactual-free method that finds circuits in GPT-2 Small and Pythia-160M from the singular-value structure of gradients across paraphrased prompts, and reports results compared against EAP-family attribution-patching baselines.
- **In plain words**: Researchers studying how language models work often look for small sub-networks, called circuits, that carry out a specific behavior. The usual method requires carefully built pairs of prompts, one normal and one altered, and the result can depend on how those prompts were written. This paper proposes a way to find these sub-networks by looking at patterns across several rewordings of the same task, without building the altered prompts.
- **Why it matters**: If the method holds up, it could make circuit discovery less dependent on hand-built prompt pairs and let researchers compare circuits shared across tasks. The text reports comparable or better scores than baselines on twelve tasks, but these are the authors' own claims and I have not verified them.
- **Background needed**: - Mechanistic interpretability: reverse-engineering neural networks to find the parts responsible for a behavior.
- Circuit: a small subgraph of units (such as attention heads) that implements a behavior.
- Activation patching / attribution patching: methods that test a unit's importance by swapping in activations from a corrupted prompt.
- Gradients: how much each output changes when a unit's value is nudged; here, gradients are collected over paraphrases of a task.
- SVD (singular value decomposition): a way to split a matrix into directions ranked by how much variation they capture.
- Recovery score and Precision@K: standard measures of how well a found circuit reproduces behavior and how many known important units appear in a top-K list.
- GPT-2 Small, Pythia-160M: small open language models used as test subjects.
- IOI (indirect object identification): a well-studied task with known "canonical" attention heads. · level: research-level
- Matched keywords: interpretability, mechanistic interpretability

<details><summary>Original abstract</summary>

Mechanistic interpretability seeks to reverse-engineer neural networks by identifying small, faithful subgraphs--circuits--that implement specific behaviors. The dominant paradigm scores each unit by replacing its clean activation with a corrupted counterpart as causal intervention. While effective, this approach rests on a brittle prerequisite: the structure prompt pairs are task-specific, expensive to engineer, and silently couple the discovered circuit to prompt-design choices. In this work, we propose Spectral Circuit Analysis (SCA), a gradient-spectral pipeline that achieves consistent circuit discovery along both axes: stable across input formulations of the same task, and natively exposing structure shared across tasks. Our contributions are threefold. First, we provide a counterfactual-free reframing of circuit discovery: causally relevant directions are recoverable from the spectral structure of forward gradients across paraphrases, with leading directions concentrating task signal and trailing ones absorbing paraphrase noise, yielding circuits tied to the task rather than the prompt. Second, we introduce SCA, a block-wise SVD pipeline that extracts a task subspace per architectural block and redistributes spectral energy onto constituent units via a consistency-weighted share, producing per-unit rankings competitive with attribution-patching baselines under strictly less supervision. Finally, on twelve circuit-discovery tasks in GPT-2 Small and Pythia-160M, SCA performs comparably or exceeds EAP-family methods under the standard recovery-score protocol and recovers IOI canonical heads with Precision@K = 1.0 in top-10 slices on GPT-2 Small; the same machinery extends to a unified cross-task analysis classifying units as universal, family-shared, or task-specific and exposing compositional structure invisible to per-task analyses.

</details>

### [Self-WSP: Can Language Models Improve Themselves Through Weight-Space Programming?](https://arxiv.org/abs/2611.28833)
*Guoming Ling, Shanshan Zhong, Kaixuan Zhang et al.* · `cs.CL` · arXiv:2611.28833v1 · relevance 0.22

- **In one sentence**: The paper tests Self-WSP, where a small language model (Qwen3.5-0.8B) reads and edits its own weights and then keeps working with the edited version, reporting large benchmark gains from sometimes very small edits but finding that the gains are hard to interpret and that random search can perform comparably.
- **In plain words**: Researchers asked whether a language model could improve itself by reading its own internal settings (its weights), proposing a small change, and then using the changed version to solve problems and make further changes. On math tests, the reported accuracy rose sharply in some cases, sometimes from changing only 16 parameters. However, the authors also found that the model seemed to understand little about why its edits helped, and that a random search over edits sometimes did about as well.
- **Why it matters**: It bears on whether AI systems can improve themselves in a loop, a long-discussed idea called recursive self-improvement. The text's own caveats mean the gains should not be read as evidence that this works reliably or for understood reasons.
- **Background needed**: - Weights: the numerical settings inside a neural network that determine its behavior; editing them changes what the model does.
- Weight-Space Programming (WSP): treating those weights like code that a strong model reads and modifies to improve a smaller model.
- Self-WSP: the variant in this paper, where the model edits itself rather than another model.
- Benchmarks used: GSM8K (grade-school math word problems) and MATH500 (harder competition-style math problems).
- Random search: trying edits at random as a baseline; if it matches the proposed method, the method's advantage is unclear.
- Interpretability: understanding why a model behaves as it does; the paper argues its gains lack this.
- Recursive self-improvement: a system repeatedly improving its own ability to improve. · level: research-level
- Matched keywords: interpretability

<details><summary>Original abstract</summary>

Frontier language models can now read and edit the weights of a neural network much like code and thereby improve a small model, an approach known as Weight-Space Programming (WSP). We further explore applying WSP to a language model itself, which we call Self-WSP. Specifically, Qwen3.5-0.8B reads its own weights, proposes an edit, and then continues with the edited weights as both problem solver and editor. We find many cases of genuine self-improvement. Self-edits can raise GSM8K accuracy from 11.8% to 62.2% and MATH500 accuracy from 7.0% to 32.2%, sometimes by changing only 16 parameters, and in some cases repeated self-editing keeps improving the model. A closer look, however, reveals that these gains lack interpretability. The model shows little understanding of the edits it makes, and WSP driven by random search sometimes performs comparably. Self-WSP thus holds promise as a path toward recursive self-improvement (RSI), but realizing this promise requires further exploration.

</details>

## AI for mathematics

### [Lean Census: A Distributional Analysis of AI-Generated Lean Code](https://arxiv.org/abs/2611.28430)
*Justin Asher, Pietro Pellegrino* · `cs.LG` · arXiv:2611.28430v1 · relevance 0.28

- **In one sentence**: A distributional comparison of code statistics (inline claims, proof length, declaration reuse, instances, private declarations) across two human-written and four AI-generated Lean libraries, benchmarked against the variation within Mathlib.
- **In plain words**: This paper looks at computer code written in Lean, a language for writing mathematical proofs that a computer can check. The authors counted simple features of the code in several libraries: some written by people, and some generated by AI. They then compared these counts against the natural variation seen within Mathlib, the main shared Lean library.
- **Why it matters**: As AI systems begin producing formal proof code at scale, it helps to have measurable profiles of what that code looks like. The text reports that the AI-generated libraries differ from the human-written ones in several measured ways, but it does not say what those differences mean for proof quality or usefulness. The released analysis package may let others repeat the comparison.
- **Background needed**: - Lean: a programming language and proof assistant in which mathematical statements and their proofs are checked by computer.
- Mathlib: a large, community-maintained library of formalized mathematics in Lean.
- Inline claims: intermediate statements a proof asserts along the way (in Lean, often written with keywords like "have").
- Declarations: named pieces of code such as theorems, definitions, or lemmas.
- Instances: Lean declarations that tell the system how to automatically apply structures or operations to a type.
- Private declarations: declarations hidden from other modules.
- Distributional analysis: comparing the spread or shape of a statistic across many items, not just its average. · level: intermediate
- Matched keywords: Lean, mathlib

<details><summary>Original abstract</summary>

We compare two human-written and four AI-generated Lean libraries with Mathlib through the distributions of simple statistics of their code. For each library we measure inline claims in proofs, proof length, how often each declaration is used, and design choices such as instances and private declarations, and we read each against the variation among Mathlib's own areas. The AI-generated libraries have more inline claims per theorem, longer proofs, fewer instances, and more private declarations than the human-written ones. We release the code for the analysis as a package, lean-census, at https://github.com/project-numina/lean-census.

</details>

### [Hashing Theorems Modulo Rewrites and Binder Permutation Enables Equivalence Search over 200k Mathlib Theorems](https://arxiv.org/abs/2611.29603)
*Samuel Le{\ss}mann, Simon Henniger, Gabriel Poesia et al.* · `cs.LO` · arXiv:2611.29603v1 · relevance 0.27

- **In one sentence**: A hashing-based method that detects duplicate theorems in the Lean/Mathlib library when they differ only in argument order or in how dependent-type arguments are curried, and that scales to over 200k theorems.
- **In plain words**: Large collections of mathematical proofs, like the Lean library Mathlib, sometimes contain the same result written twice in different places, which wastes upkeep effort. This paper describes a way to automatically spot such repeats even when the statements are written with their inputs in a different order or grouped differently. The authors report that the method is cheap to run and works on Mathlib's more than 200,000 theorems.
- **Why it matters**: Keeping a large formal math library tidy is a real maintenance problem, and the existing duplicate checker misses equivalences that need reordering or regrouping of arguments. The text does not go beyond this practical scope, so its wider impact on AI-for-math work is unclear from the excerpt alone.
- **Background needed**: - Lean is a programming language and proof assistant in which mathematical theorems are written as checkable code.
- Mathlib is the large, community-maintained Lean library of mathematics.
- A theorem's "type" is its statement; two theorems can state the same thing in different notations.
- "Binders" are the named inputs of a statement; permuting them means reordering those inputs.
- Currying means turning a function of several inputs into a chain of single-input functions (and back).
- Hashing means computing a short fingerprint of an object so that equal objects get equal fingerprints, allowing fast comparison.
- The paper's scope is detecting equivalence up to argument order and currying, not deeper logical equivalence. · level: research-level
- Matched keywords: Lean, mathlib

<details><summary>Original abstract</summary>

Like all code, Lean libraries accumulate technical debt and structural deficiencies over the course of their development. A particular concern is duplicate theorems: different parts of a big library can unwittingly contain and prove the same theorem, duplicating maintenance efforts. Tools can help detect redundancy and clean up. For instance, Mathlib's duplicate-declarations linter compares theorem types syntactically after sorting top-level binders and erasing binder information and universe levels. If detecting an equivalence requires unfolding, reorientation, or logical transformations, it escapes this comparison. In this work, we present a method to detect theorems which are equivalent with regard to argument order and currying/uncurrying of dependent types. We implement our method for Lean. By applying it to Mathlib, a library of more than 200k theorems, we demonstrate that it is computationally cheap and scalable. We discuss how our work may enhance efforts to tackle the maintenance burden of Lean libraries.

</details>

## Robotics and embodied AI

### [Imagine Smarter, Drive Faster: Efficient World Modeling for Decision-Aware Autonomous Driving](https://arxiv.org/abs/2611.28779)
*Feiyang Jia, Lin Liu, Zhicheng Bao et al.* · `cs.CV` · arXiv:2611.28779v1 · relevance 0.17

- **In one sentence**: FastWorld is a lightweight world-model planner for autonomous driving that imagines short-horizon, action-conditioned futures over compact scene representations and selectively verifies candidate trajectories, without teacher distillation or extra domain-specific pre-training.
- **In plain words**: Self-driving planners can be made to "imagine" how the road will look after each possible move, but that imagining is usually expensive to run. This paper describes FastWorld, a version designed to be cheap from the start: it uses compact summaries of the scene, looks only a short way ahead, and checks and rescores only a selected set of candidate driving plans. The authors report that it scores well on standard driving benchmarks while running quickly on a single consumer GPU.
- **Why it matters**: Making future-aware planning fast enough for real vehicles is a practical bottleneck, and the paper's claim is that efficiency can come from the model design itself rather than from large teacher models or costly pre-training. Its relevance beyond the reported benchmarks (NAVSIM and nuScenes) is not established by the text.
- **Background needed**: - World model: a learned model that predicts how an environment will change, used here to forecast the road ahead.
- Planning in autonomous driving: choosing a trajectory for the car from several candidates.
- Knowledge distillation: training a small model to copy a large "teacher" model, which the paper says it avoids.
- Action-conditioned prediction: forecasting future scenes given the specific action (driving move) taken.
- Benchmarks: NAVSIMv1 and v2 use PDMS and EPDMS scores (higher is better) for driving quality; nuScenes uses L2 error, the distance from the planned path to the human-driven path (lower is better).
- FPS: frames per second, a measure of speed; 132 FPS on one RTX 4090 GPU is the reported figure. · level: research-level

<details><summary>Original abstract</summary>

World models hold great promise for autonomous driving planning, yet their ability to imagine the future often comes at a formidable computational cost. Efficiency efforts, such as knowledge distillation and domain-specific pre-training, often shift this burden to costly teachers or training pipelines, leaving lightweight world modeling an open challenge. We introduce FastWorld, a natively lightweight world-model framework for efficient autonomous driving planning. FastWorld reduces computation through compact scene representations, short-horizon action-conditioned prediction, and selective candidate verification and score refinement. These designs support efficient future-informed planning without teacher distillation or additional domain-specific pre-training. On NAVSIMv1, FastWorld achieves 92.2 PDMS at 132 FPS on a single 4090 GPU. It also achieves 89.4 EPDMS on NAVSIMv2 and an average L2 of 0.40 over 3 seconds at 17 FPS on nuScenes. Code and models can be found at https://github.com/MoyangSensei/FastWorld.

</details>

### [AXE: AlpaSim E2E Closed Loop Challenge Technical Report](https://arxiv.org/abs/2611.30511)
*Joonhee Lim, Seonmyeong Lee, Sihwan Hwang et al.* · `cs.RO` · arXiv:2611.30511v1 · relevance 0.15

- **In one sentence**: A technical report describing an end-to-end autonomous driving pipeline for a closed-loop challenge, which pairs imitation learning and simulator-based reinforcement learning with a perception-based filter that rejects trajectory candidates likely to collide or leave the drivable area.
- **In plain words**: This report describes a system for teaching a self-driving car to plan its own path directly from sensor data, and tests it in a simulator where the car's actions affect what happens next. The team's main idea is to generate a fixed set of possible driving paths, score them for safety and progress, and pick the best one that passes a safety check based on object detection and a top-down map of the road. The text presents the design; it does not report detailed benchmark results.
- **Why it matters**: Closed-loop testing, where a driving model's choices change the scenes it sees next, is harder to get right than offline tests, so a safety filter layered on a learned planner is a practical design question for the field. The text gives only the approach and not measured outcomes, so its real-world value is uncertain from this report alone.
- **Background needed**: - End-to-end driving: a single learned model maps camera or sensor input to driving actions, rather than using separate hand-built modules.
- Imitation learning: the model learns by copying recorded human driving.
- Reinforcement learning: the model improves by trial and error, here using rollouts in a simulator.
- Closed-loop evaluation: the simulated car's own actions shape later inputs, which makes testing stricter than replaying fixed recordings.
- BEV (bird's-eye view) segmentation: labeling a top-down map of the road, such as drivable areas.
- Trajectory candidates: a fixed list of possible short paths the car can follow; the system scores each one.
- HD map: a detailed, high-precision map of roads, here generated by automatic labeling. · level: research-level

<details><summary>Original abstract</summary>

This report presents a comprehensive pipeline for developing an end-to-end (E2E) autonomous driving model for the Physical AI AV Track. The framework consists of data curation, HD map auto-labelling, data-driven imitation learning, and simulator-based reinforcement learning. To ensure safety in the closed-loop setting, we introduce a selection-based E2E planning approach that leverages object detection and BEV segmentation to filter out trajectory candidates likely to cause collisions or off-road driving. Trained on NVIDIA NuRec and the NVIDIA PAI-AV dataset, our method scores a fixed vocabulary of trajectory candidates for collision, drivable-area compliance, and progress learned from simulated rollouts, and selects the best candidate that passes the filter. This design highlights the effectiveness of combining E2E planning with perception-based trajectory filtering for safe and reliable closed-loop autonomous driving.

</details>

## Security and cryptography

### [Ziv Meets Sumcheck: Zero-Knowledge Proofs of Floating-Point LLM Inference](https://arxiv.org/abs/2611.29188)
*Hassan Khodaiemehr, Khadijeh Bagheri, Chen Feng* · `cs.LG` · arXiv:2611.29188v1 · relevance 0.16

- **In one sentence**: The paper gives an interactive zero-knowledge proof that a transformer language model's floating-point forward pass was computed correctly, by proving the correctly rounded result of each dot product, and reports a GPT-2 small instance.
- **In plain words**: The paper is about proving that an AI language model produced a specific output, without revealing the model's internal numbers. Existing methods mostly checked simplified integer versions of the model, not the decimal-style floating-point arithmetic models actually run on. The authors show a way to check the real floating-point computation by rounding each dot product (a sum of products) only once, which makes the result the same regardless of hardware.
- **Why it matters**: Being able to verify model outputs without access to the weights bears on trust in AI systems and on privacy of proprietary models. The text reports a full GPT-2 small forward pass proved in 19 minutes on two cores, with verification in 21 seconds, and 236 tested attacks rejected. These are the authors' own reported results, not independently checked, and the text does not show how this scales to larger models.
- **Background needed**: - Zero-knowledge proof: a way to convince a verifier that a computation was done correctly without revealing its secret inputs, such as model weights.
- Interactive proof: a protocol where a prover and verifier exchange messages, with the verifier checking random challenges.
- Floating-point arithmetic: how computers store approximate real numbers; rounding after each operation makes results depend on the order of operations.
- Dot product and matrix multiplication: the core repeated sum-of-products operation in neural networks.
- Transformer and GPT-2: the neural network architecture behind modern language models; GPT-2 small is a small, older model used as a test case.
- Sumcheck: a standard interactive-proof technique for checking large sums cheaply.
- Quantization (16-bit inference): running models with lower-precision numbers to save compute. · level: research-level

<details><summary>Original abstract</summary>

Zero-knowledge proofs can show that a neural network produced a given output without revealing the network, but current systems for language models prove integer approximations of the model rather than the floating-point arithmetic that is actually deployed. Proving floating-point matrix multiplication has been regarded as hard, because rounding after every addition makes the result depend on the order of the additions. We avoid this obstacle by proving the correctly rounded product, in which every dot product is computed exactly and rounded once. This result is independent of the hardware and at least as accurate as standard kernels. We give an interactive proof for this relation whose cost is close to that of integer matrix multiplication, with roughly a thousand times fewer committed values than per-operation floating-point circuits need constraints, extend it to every layer of a transformer, and give a privacy construction for the complete argument whose zero knowledge we prove under explicit hypotheses. We implement the system and prove the full forward pass of GPT-2 small, including all twelve blocks and the output over the whole vocabulary, in 19 minutes on two processor cores; verification takes 21 seconds. The verifier rejects all 236 attacks we tested, and the model's outputs agree with high-precision inference at least as closely as standard 16-bit inference does.

</details>

### [Reporting Differential Privacy Guarantees via Operationally Equivalent $\varepsilon$: What Does $\varepsilon=19.61$ Mean for the 2020 U.S. Census?](https://arxiv.org/abs/2611.28790)
*Masayuki Terada, Shinsuke Ito, Takumasa Ishioka et al.* · `cs.CR` · arXiv:2611.28790v1 · relevance 0.13

- **In one sentence**: The paper defines an alpha-operationally equivalent epsilon that re-expresses approximate differential privacy (ADP) or zCDP guarantees as the pure DP epsilon giving the same power bound at a chosen significance level, and applies it to the 2020 U.S. Census figure of epsilon = 19.61.
- **In plain words**: The 2020 U.S. Census reported a privacy number of 19.61, which many people found alarmingly large. This paper asks what that number actually limits: how well an attacker could tell whether a given person's data was included. It translates the official guarantee into a more interpretable form and reports that, at common significance levels, the guarantee constrains such attacks much more tightly than the single large number suggests.
- **Why it matters**: The 19.61 figure has drawn public doubt about Census privacy protection, so a way to read it in terms of concrete attack limits is directly relevant. The text does not establish how the method will be received by the Census Bureau or other researchers, so its wider impact is uncertain.
- **Background needed**: - Differential privacy (DP): a guarantee that the output of a data release barely changes whether or not any one person's record is included.
- Epsilon (ε): the DP parameter; smaller means stronger privacy. Large values are usually read as weak protection, but the meaning depends on how the value was obtained.
- Approximate DP (ADP): a version with an extra small slack term δ (here 10^-10).
- zCDP (zero-concentrated DP): an alternative privacy accounting method, which the Census used before converting to ADP.
- Power / true positive rate: how often an attacker correctly identifies a real member when testing for membership.
- Significance level α: the tolerated false alarm rate of that test (e.g., 1%, 5%, 10%).
- Trade-off function / Gaussian DP: a richer way to describe the attacker's achievable power across all significance levels. · level: research-level

<details><summary>Original abstract</summary>

The large value $\varepsilon=19.61$, reported as an approximate differential privacy (ADP) parameter for the 2020 U.S. Census, has prompted doubts about the adequacy of Census privacy protection. It was obtained by converting component zero-concentrated differential privacy (zCDP) guarantees to ADP at $\delta=10^{-10}$. A single ADP pair can substantially loosen the original upper bound on the power (true positive rate) of a distinguishing test. At significance level $\alpha$, we express the original bound as the smallest pure differential privacy (DP) parameter giving the same power bound. We call this the $\alpha$-operationally equivalent $\varepsilon$. The full curve represents the original bound exactly on $(0,1)$, even when the bound is nonconcave. For maximum-power curves and bounds derived from trade-off functions, we characterize the extrema of operationally equivalent $\varepsilon$ over an interval of significance levels. When finite, they give the parameters of the pure DP bounds that enclose the original power bound on that interval. The mapping preserves the ordering of power bounds at each significance level. For Laplace and Gaussian mechanisms with equal noise variance, conversion to single ADP pairs or Gaussian DP envelopes can reverse this ordering. For the P.L. 94-171 redistricting data, we reproduce the reported $\varepsilon=19.61$ as the sum of rounded component ADP values. The published zCDP guarantee yields operationally equivalent $\varepsilon$ values of approximately 4.25, 2.94, and 3.18 at significance levels of 1%, 5%, and 10%, respectively. Converting the same guarantee to a single ADP pair at $\delta=10^{-10}$ gives power bounds near 1 at all three levels. The pure DP scale thus clarifies constraints on distinguishing attacks that are difficult to discern from the reported $\varepsilon=19.61$.

</details>

## Algorithms and complexity

### [A $(17/7-o(1))n$ Circuit Lower Bound for Binary-Encoded 3-SAT](https://arxiv.org/abs/2611.30887)
*Theodoros Yianni, Sahibzada Allahyar* · `cs.CC` · arXiv:2611.30887v1 · relevance 0.15

- **In one sentence**: The paper improves the circuit-size lower bound for a specific binary encoding of 3-SAT to (17/7)n minus lower-order terms over the full two-input Boolean basis, using weighted gate elimination and a nonlinear-degree argument, with Lean-verified proofs of the key inequality and asymptotic bound.
- **In plain words**: This paper is about how many logic gates a computer circuit needs to solve a standard hard logic puzzle (3-SAT) when the puzzle's input is written as a string of bits in one particular encoding. The authors prove that such circuits need at least about 17/7 times the input length, which is a modest improvement over the previous known bound of roughly n minus 1. They also checked key parts of the argument with the Lean proof assistant, a software tool that verifies mathematical proofs.
- **Why it matters**: Proving lower bounds on circuit size is a central open problem in theoretical computer science, and even small improvements are technically hard to obtain. The result is limited to one specific encoding of one problem, so its reach beyond that case is unclear from the text alone.
- **Background needed**: - Boolean circuit: a network of logic gates (AND, OR, XOR and similar) that computes a yes/no answer from input bits.
- Circuit size / gate count: how many gates are needed; a lower bound says no circuit can do better than a given count.
- 3-SAT: a standard hard problem asking whether a set of 3-literal clauses can all be satisfied by some true/false assignment.
- Encoding: a fixed rule for writing a formula as a bit string; here the bound depends on this encoding.
- Gate elimination: a proof method that shows each gate removed under a restriction eliminates a set number of gates, giving a total lower bound.
- Algebraic degree over F_2: a measure of how complex a Boolean function is as a polynomial over the two-element field; nonlinear functions need more than trivial gates.
- Lean: a proof assistant that machine-checks mathematical proofs. · level: research-level

<details><summary>Original abstract</summary>

We strengthen the elementary $n-1$ circuit lower bound for a specified binary encoding of 3-SAT to $(17/7)n-O(n\log\log n/\log n)$ gates over the full two-input Boolean basis, with unrestricted depth and sharing. For each integer $w\ge5$, we encode 3-CNF formulas with exactly $m=2^w-1$ clauses over $m$ available variables using $n=3m(w+1)$ bits. The proof embeds Boolean tests in variable identifiers while retaining $n-o(n)$ free bits, and combines weighted gate elimination with a nonlinear-gate lower bound from the tests' full algebraic degree over $\mathbb F_2$. We provide Lean proofs of the finite inequality and the asymptotic bound for arbitrary acyclic binary circuits.

</details>

### [An $n^{1/O(\log^* n)}$ Lower Bound for Online Coloring of $k$-Colorable Graphs](https://arxiv.org/abs/2611.29672)
*Sajad Faghfoor Maghrebi* · `cs.DS` · arXiv:2611.29672v1 · relevance 0.13

- **In one sentence**: The paper proves that deterministic and randomized online algorithms for coloring k-colorable graphs (k≥3) must sometimes use n^{1/(log* n+3)} colors, via iterated clique blow-up instances, and shows a matching-type upper limit on such adversaries.
- **In plain words**: The paper studies a graph-coloring task where vertices of a network show up one at a time and each must be given a color right away, without changing it later. The question is how many colors such a procedure is forced to use when the network could be split into a small number of color classes. The authors show the number of colors needed grows almost as fast as a small power of the network size n, which is much more than the older logarithmic bound.
- **Why it matters**: This narrows a long-standing gap between the best known online algorithms and lower bounds for coloring k-colorable graphs, a classic problem in theoretical computer science. The paper also reports that all numbered results were checked in the Lean 4 proof assistant, which is a notable feature for a theory result; the broader practical significance is limited to the theory itself.
- **Background needed**: - Graph coloring: assigning labels (colors) to vertices so that adjacent vertices differ; a k-colorable graph can be colored with k colors.
- Online algorithm: must make each decision on arrival, with no knowledge of future input and no revisions.
- Competitive/lower-bound reasoning: an adversary chooses the arrival order to force an algorithm to waste colors.
- Deterministic vs. randomized algorithms: the second uses random choices; the paper gives bounds for both.
- Blow-up of a graph: replacing each vertex with a set of independent copies, which keeps some structure while changing others.
- Iterated logarithm (log*): the number of times you must take the logarithm before the value drops below 1; it grows extremely slowly.
- Lean 4: a computer proof assistant used to machine-check mathematical proofs. · level: research-level

<details><summary>Original abstract</summary>

In online coloring, the vertices of a graph arrive one at a time with their edges to earlier vertices, and each vertex must be colored irrevocably on arrival. For graphs promised to be $k$-colorable, with $k\ge 3$ fixed, the best deterministic algorithms use $n^{1-\Theta(1/k^2)}$ colors, while the best lower bound was Vishwanathan's $\Omega(\log^{k-1}n)$ from 1990 until Li recently proved $2^{\Omega((\log n)^{1/3}(\log\log n)^{2/3})}$. For every fixed $k\ge 3$ and all sufficiently large $n$, we prove a lower bound of $n^{1/(\log^*n+3)}$ colors for deterministic online algorithms on $n$-vertex $k$-colorable graphs, and the same lower bound in expectation for randomized online algorithms. Both bounds hold on a single triangle-free $3$-colorable graph: even an algorithm that is shown this graph in advance, but is not told which of its vertices each arriving vertex is, can be forced to use this many colors by a suitable arrival order. The hard instances are iterated blow-ups of a clique, in which every vertex becomes a block of independent vertices and every edge a private server in the earlier block; each blow-up keeps the forced colors and replaces the chromatic number $\chi$ by about $\log\chi$, so about $\log^*n$ blow-ups bring it down to $k$. We also show that deterministic lower bounds for different values of $k\ge 3$ are polynomially equivalent, and that no adversary presenting such iterated blow-ups can force more than $n^{1/(\log^*n-O(1))}$ colors. All numbered results are formalized in Lean 4.

</details>

## Programming languages and formal methods

### ["What Should I Do?" Guidelines for Responsibly Integrating AI in Software Engineering](https://arxiv.org/abs/2611.28996)
*Rudrajit Choudhuri, Fatima A. Moussaoui, Carmen Badea et al.* · `cs.SE` · arXiv:2611.28996v1 · relevance 0.13

- **In one sentence**: A two-phase survey study of 1,118 developers at Microsoft, GitHub, and Pfizer that derives and then validates 35 guidelines for how software engineers should responsibly integrate AI into their work.
- **In plain words**: Software developers are now using AI tools in their daily work, but the advice on how to use them well is thin and sometimes contradictory. The researchers first surveyed 860 Microsoft developers about where they did and did not want AI help, and turned their answers into 35 practical guidelines. A year later, they checked those guidelines with 258 developers at Microsoft, GitHub, and the drug company Pfizer, and most said the guidelines were clear, relevant, and something they wanted to follow.
- **Why it matters**: As AI tools spread into software that people depend on, the question of who is accountable for AI-assisted code matters, and this paper offers practitioner-sourced guidance and shared terms teams could adopt. The text does not show how much the guidelines change actual outcomes, so their practical effect is still unclear.
- **Background needed**: - Software engineering (SE): the work of designing, building, testing and maintaining software.
- Generative AI coding assistants: tools that suggest or write code from natural-language prompts.
- Survey study: collecting self-reported experiences from many people; results reflect what respondents say, not measured performance.
- Validation phase: a second round where a new group rates whether the derived guidelines are clear and useful.
- Delegation vs. judgment: the paper's framing of handing checkable tasks to AI while keeping decisions and responsibility with the human.
- Relationship-centric work: SE tasks that depend on collaboration and interpersonal communication, where the paper reports more variation in endorsement. · level: intermediate

<details><summary>Original abstract</summary>

Speculations abound about the "right" ways for developers to integrate AI into their software engineering (SE) work, but the evidence that exists is sparse and contradictory. Yet, developers are held responsible for the products they ship with (or without) AI's help, so they need to integrate AI in responsible ways. To address this gap, we conducted a two-phase, large-scale investigation with 1,118 developers at Microsoft, GitHub, and Pfizer. In Phase 1, we surveyed 860 developers at Microsoft on where they sought and resisted AI support in their daily work, and from their accounts, synthesized 35 developer-facing guidelines: 29 across five categories of SE work and 6 cross-cutting ones. A year later, as AI capabilities and developers' experiences co-evolved, we validated them in Phase 2 with 258 developers in technology (Microsoft, GitHub) and biopharmaceutical (Pfizer) domains. Developers in our study found the guidelines clearly worded (92%) and relevant to their work (91%), and most wanted to adopt them in their own work (89%). We also report how developers described operationalizing these guidelines in practice: using AI to refine their craft and delegate verifiable work, while keeping judgment and accountability for themselves. For relationship-centric work, endorsement varied with developers' domain and their SE and AI experience. Overall, we offer concrete advice from in-the-trenches developers to other in-the-trenches developers, and a shared vocabulary that engineering teams can adopt to integrate AI well in their work.

</details>

### [Micro Operational Robustness of LLMs on Code Generation](https://arxiv.org/abs/2611.28957)
*Debalina Ghosh Paul, Hong Zhu, Ian Bayley* · `cs.SE` · arXiv:2611.28957v1 · relevance 0.13

- **In one sentence**: The paper proposes "scenario domain analysis," a method that searches for the smallest expected change in natural-language coding-task descriptions that causes an LLM to generate incorrect code, and uses it to compare four LLMs and several task types.
- **In plain words**: Developers increasingly ask AI language models to write program code from a short written description of a task. This paper asks how sensitive those models are to small changes in the wording of that description, and it introduces a way to measure that sensitivity. The authors report that they could rank four models from most to least robust, and that the models did worse on more complex tasks and on advanced topics such as multi-threading and data structures.
- **Why it matters**: Code generated by AI is only useful if it stays correct when people phrase their requests slightly differently, so measuring this sensitivity matters for trusting such tools. The text does not say how the method performs beyond the four models and tasks tested, so its broader reach is unclear.
- **Background needed**: - Large language model (LLM): an AI system trained on large amounts of text, here used to write code from instructions.
- Robustness: how much a system's output stays correct when its input is changed a little.
- Natural-language (NL) description: the plain-English statement of what a program should do.
- Discrete and sparse input space: the possible wordings are separate, countable options with large gaps between them, so ordinary tests for smooth changes do not apply.
- Multi-threading: running several parts of a program at the same time.
- Formal proof: a mathematical argument that a property always holds, which the authors say they provided for their method. · level: intermediate

<details><summary>Original abstract</summary>

It is now common practice in software development for large language models (LLMs) to be used to generate program code. It is desirable to evaluate the robustness of LLMs for this usage. This paper is concerned in particular with how sensitive LLMs are to variations in descriptions of the coding tasks. However, existing techniques for evaluating this robustness are unsuitable for code generation because the input data space of natural language (NL) descriptions is discrete and sparse. To address this problem, we propose a robustness evaluation method called scenario domain analysis, which aims to find the expected minimal change in the NL descriptions of coding tasks that would cause the LLMs to produce incorrect outputs. We have formally proved the theoretical properties of the method and also conducted extensive experiments to evaluate the robustness of four state-of-the-art LLMs: Gemini-pro, Codex, Llamma2 and Falcon 7B, and have found that we are able to rank these with confidence from best to worst. Moreover, we have also studied how robustness varies in different scenarios, including the variations with the topic of the coding task and with the complexity of its sample solution, and found that robustness is lower for more complex tasks and also lower for more advanced topics, such as multi-threading and data structures.

</details>

## Systems and networking

### [Which $\Diamond \mathcal{P}$ Algorithm is Suitable for You? An Empirical Benchmark on Real Network Traces](https://arxiv.org/abs/2611.30815)
*Yenan Wang, Jens Kollberg, Elad Michael Schiller et al.* · `cs.DC` · arXiv:2611.30815v1 · relevance 0.08

- **In one sentence**: The paper systematizes 14 unreliable failure detectors (mostly diamond-P style), implements 13 of them, and benchmarks them on replayed real network traces and live deployments using common QoS metrics, framing detector choice as a constrained algorithm-selection problem.
- **In plain words**: Computers in a distributed system need to notice when another machine has crashed, but the tools that do this (failure detectors) are usually tested under different conditions, making them hard to compare. This paper collects 14 such detectors, implements 13, and tests them on the same recorded network traffic and in live deployments, measuring how fast they spot crashes and how often they wrongly flag healthy machines. The main finding is that no single detector is best everywhere; the text reports that 2W was the most frequently chosen detector when a detection-time limit of 500 ms or more was allowed.
- **Why it matters**: Choosing the right failure detector affects how reliable consensus and fault-tolerant services are, so a shared, reusable benchmark could help practitioners pick one. The authors also suggest the benchmark can serve as a baseline for future detectors, including learning-based ones, though the text does not show results for such detectors.
- **Background needed**: - Distributed systems: many networked machines that must agree on things despite failures.
- Failure detector: software that guesses whether a remote machine has crashed, based on missing heartbeat messages; it can be wrong, hence "unreliable."
- Diamond-P (◇P): a formal class of failure detectors that eventually stops making mistakes about healthy machines.
- QoS metrics: quality-of-service measures such as detection time (how long until a crash is noticed), mistake rate (false alarms), and query accuracy (how often answers are correct).
- Trace replay: re-running recorded network timing data through a detector so that each one sees identical input.
- Algorithm selection: choosing the best method for a given task and set of constraints. · level: research-level

<details><summary>Original abstract</summary>

Unreliable failure detectors (UFDs) are a fundamental abstraction for dependability and fault tolerance in distributed systems, supporting core distributed algorithms, such as consensus. Yet selecting a suitable detector remains difficult because existing implementations are evaluated under different environments, workloads, parameterizations, and quality-of-service (QoS) requirements. We address this problem by systematizing 14 $\Diamond \mathcal{P}$ and closely related $\Diamond \mathcal{P}$-style UFDs, implementing 13 of them, and providing a reusable benchmark for their empirical comparison. Our methodology evaluates detectors through common QoS metrics, such as detection time, mistake rate, and query accuracy, and combines same-input replay of network traces with live deployment for detectors whose active probing or cooperative behavior requires online execution. We then formalize failure-detector selection as a constrained algorithm-selection challenge, mapping operational requirements to suitable detector candidates. We instantiate this methodology under controlled variations of communication rate, host load, and crash regime. Applying the selection process shows that no detector is uniformly preferable across the evaluated settings. At relaxed detection-time budgets, 2W [Tomsic et al., IPDPS 2015] is the most frequently selected detector, appearing in 12 of 16 scenario-metric combinations for $T_D \le 500$ ms, whereas stricter budgets yield substantially more scenario- and metric-dependent selections. The benchmark and selection methodology provide a reusable basis for practical detector selection and for establishing stronger analytical baselines for future failure-detection approaches, including learning-based detectors.

</details>

### [LIELLA: Private Edge Adaptation with Photonic Weight Streams](https://arxiv.org/abs/2611.29343)
*Yuexun Huang, Kfir Sulimany, Ke Lin et al.* · `cs.AR` · arXiv:2611.29343v1 · relevance 0.06

- **In one sentence**: LIELLA proposes a weight-streaming design in which several edge devices personalize a shared language model through small private photonic adapters, supporting both backpropagation and forward-only training, evaluated in simulation under hardware noise.
- **In plain words**: Many phones or sensors would like to tailor one large AI model to their own data without sending that data elsewhere, but they have little memory and power. This paper proposes a setup where the big shared model is streamed in as light signals from a photonic (light-based) chip, while each device keeps only a small private add-on, called an adapter. In simulations with hardware noise, the devices reached nearly noise-free accuracy on two language tasks, QNLI and SST-2, and the authors report lower modeled electrical energy use than with electronic adapters.
- **Why it matters**: It addresses a real tension between privacy, energy, and memory limits for on-device AI, and it suggests that hardware constraints might guide the design of smaller fine-tuning methods. The results are simulated only, so how well they hold on real photonic hardware is not shown in the text.
- **Background needed**: - Photonic accelerator: a chip that does some computation with light instead of electrons, which can be energy-efficient.
- Fine-tuning / adapters: adjusting a pretrained model with a small added module instead of retraining all of it (parameter-efficient fine-tuning, PEFT).
- Backpropagation: the standard way neural networks learn by passing error signals backward through the network.
- Forward-only optimization: learning that uses only forward passes through the model, which can suit hardware that cannot store intermediate values.
- Weight streaming: loading model parameters piece by piece rather than holding the whole model in memory.
- Benchmarks: QNLI and SST-2 are standard language-understanding tasks; TinyLlama is a small open language model of about a gigabyte.
- Attojoule: an extremely small unit of energy (10^-18 joules) per multiply-accumulate operation. · level: research-level

<details><summary>Original abstract</summary>

Although photonic accelerators have shown promise for energy-efficient machine learning inference, privately personalizing large models across multiple edge clients remains difficult under tight memory, precision, and hardware constraints. We present LIELLA, a weight-streaming architecture that enables multiple edge clients to personalize a shared model through compact private adapters. The two proposed photonic adapter architectures accommodate both backpropagation and forward-only optimization while substantially reducing modeled client-side electrical energy consumption compared with electronic adapters. Under simulated hardware noise, clients sharing the same streamed backbone achieve nearly clean accuracy on QNLI and SST-2, even with attojoule-scale optical energy per MAC at each receiver. The architecture also enables hardware-aware adaptation among clients performing the same task, allowing their individual private adapters to achieve further accuracy improvements. For a gigabyte-scale TinyLlama backbone, LIELLA maintains a megabyte-scale inference memory footprint and kilobyte-scale persistent adapter storage per client, while achieving strong performance through forward-only adaptation. These findings further highlight hardware-driven opportunities to develop smaller yet more effective parameter-efficient fine-tuning (PEFT) methods and more accurate, noise-robust forward-only optimization algorithms.

</details>

## Human-computer interaction

### [Neurosymbolic Human-AI Collaboration: Foundations, Conceptual Framework, and Applications](https://arxiv.org/abs/2611.28011)
*Vito Scaraggi, Andrea Passarella, Marco Conti* · `cs.HC` · arXiv:2611.28011v1 · relevance 0.13

- **In one sentence**: This paper proposes NeSy-HAIC, a conceptual framework that uses neurosymbolic AI (combining neural networks with symbolic reasoning) to give humans and AI a shared, human-readable interface for collaborating on tasks, illustrated with semi-autonomous driving and security alert prioritization.
- **In plain words**: Many workplaces now have people and AI systems working on the same tasks, but it is still hard for them to understand each other. This paper proposes a conceptual blueprint, called NeSy-HAIC, that mixes two styles of AI so the machine's internal workings can be expressed as concepts people already understand. The authors sketch how this could work in two example settings, self-driving cars that still need a human driver and ranking security alerts, but the text describes the framework rather than reporting tested results.
- **Why it matters**: Getting humans and AI to communicate clearly is a long-standing obstacle in human-AI collaboration, and the paper ties that problem to explainable AI and neurosymbolic methods. Because it is a framework proposal without reported experiments in the text, its practical value is still to be shown.
- **Background needed**: - Human-AI collaboration (HAIC): people and AI sharing a task, each covering the other's weaknesses.
- Machine learning: software that learns patterns from data, such as recognizing images or speech.
- Explainable AI: methods that try to make a model's reasoning understandable to people.
- Neurosymbolic AI: combining neural networks (pattern learning from data) with symbolic reasoning (explicit rules and concepts).
- Semantic gap: the mismatch between how a machine represents information and how humans think about it.
- Human-in-the-loop vs. human-on-the-loop: a person actively approves each AI decision versus a person supervising and intervening when needed. · level: intermediate

<details><summary>Original abstract</summary>

The growing adoption of Artificial Intelligence (AI) across workplaces and industries, ranging from manufacturing plants to healthcare facilities, has paved the way to the design of systems in which humans and AI collaborate on shared tasks. The first developments of Human-AI Collaboration (HAIC) were driven by advances in Machine Learning (ML), which enabled the automation of numerous tasks, including large-scale data processing, image analysis, and speech recognition. However, ML automation have proven insufficient for certain applications due to methodological, safety, and ethical concerns. In such cases, researchers argue for integrating human expertise into operational workflows to improve performance, relying on the complementary skill sets of humans and AI. Despite long-standing research, the field of HAIC has not yet reached full maturity, largely due to the intrinsic difficulty of ensuring a seamless communication between humans and AI. This challenge is partially addressed by Explainable AI methods, which aim to make internal model reasoning more transparent through human-understandable explanations. Recognizing the need for a shared interface between humans and AI in collaborative settings, we propose a novel conceptual framework, NeSy-HAIC, that leverages Neurosymbolic AI (NeSy AI) to bridge the semantic gap between machine representations and human-understandable symbolic concepts. The framework builds on current research in NeSy AI and HAIC, supports multiple interaction paradigms, including Human-In-The-Loop and Human-On-The-Loop, and is characterized through its enabling methodologies and two illustrative use cases in semi-autonomous driving and security alert prioritization. We argue that the integration of data-driven learning and symbolic reasoning can substantially enhance human-AI interaction and mitigate limitations of collaborative systems.

</details>

### [Pharmacy stock and post-earthquake access to medicines in Tokyo: modeling choices that change recovery judgments](https://arxiv.org/abs/2611.29459)
*Juanning Liang, Hiroki Baba* · `cs.CY` · arXiv:2611.29459v1 · relevance 0.12

- **In one sentence**: A sensitivity study of a two-step floating catchment accessibility model for over-the-counter medicine access at Tokyo pharmacies after a scenario magnitude-7.3 earthquake, showing that stock-depletion assumptions, model type and floating-catchment method choices can change recovery verdicts.
- **In plain words**: After a major earthquake, people need nearby pharmacies to still be open, staffed and holding medicine. This paper simulates over-the-counter medicines at about 4,700 registered pharmacies in Tokyo's 23 wards during the first week after a scenario quake, and measures how walking access compares with pre-quake levels. The authors find that the answer to "is access recovering?" depends heavily on how one models pharmacies running low on stock, on the kind of model used, and on which method is chosen.
- **Why it matters**: Local decisions about where to prioritise pharmacy support may hinge on modelling choices that are rarely reported, so the paper argues for stating stock assumptions and worst-case (low-end) outcomes. The relevance beyond Tokyo is plausible but the text covers only one city and one scenario.
- **Background needed**: - Accessibility model: estimates how easily people can reach a service on foot, based on distance and how many providers are nearby.
- Floating catchment area method: a common accessibility calculation that assigns each location a supply-to-demand ratio using nearby providers and people; the paper compares four variants.
- Retention: post-disaster accessibility divided by the same location's pre-disaster accessibility (1 means no loss).
- Stock depletion: pharmacies run out of medicine over time, so their capacity to serve people falls even if the building is open.
- Scenario earthquake: a hypothetical event used for planning and simulation, not a real event.
- Rank correlation and Jaccard index: measures of how similar two rankings are overall, and how much two sets of "lowest 10%" areas overlap (0.56 means partial overlap).
- Percentile: the 10th-percentile result is a low-end outcome, worse than most sampled cases. · level: research-level

<details><summary>Original abstract</summary>

Community pharmacies sustain access to medicines after an earthquake only while open, staffed and stocked. Accessibility models rarely represent stock depletion, and the assumptions this requires may change conclusions about recovery. We examine these assumptions for over-the-counter (OTC) medicines supplied by 4,748 registered pharmacies in Tokyo's 23 wards during the first week after a magnitude-7.3 scenario earthquake. A two-step floating catchment area model computes walking accessibility for 2,651 grid cells (500 m) under 10,000 sampled combinations of stock duration, staffing, operation and demand. Results are expressed as Retention: post-disaster accessibility divided by the same cell's pre-disaster accessibility. First, the assumed link between stock and service, the supply a pharmacy can still provide, determines the recovery verdict. If service falls in proportion to remaining stock, mean Retention declines from 0.479 (days 2-3) to 0.273 (days 4-7). If service is maintained until stock falls below one quarter, the mean rises instead, although low-end (10th-percentile) outcomes still decline. Measuring at the start of each period rather than averaging over it also reverses the trend. Second, a simple model that rescales a fixed map by citywide supply and demand reproduces citywide patterns but cannot evaluate where pharmacies close or where capacity is added; a spatial model run once on average inputs can. Third, four floating catchment methods agree on overall rankings (rank correlation 0.81), but their lowest-ranked 10% of cells overlap only partially (Jaccard index 0.56). Disaster assessments should report stock assumptions and low-end outcomes, and treat local priority areas as method-dependent.

</details>

## Information theory

### [Optimal fidelity over zero-capacity erasure channels](https://arxiv.org/abs/2611.30902)
*Camilo Castro-Landolt, Rabsan Galib Ahmed, Graeme Smith* · `quant-ph` · arXiv:2611.30902v1 · relevance 0.15

- **In one sentence**: The paper exactly finds the optimal asymptotic entanglement fidelity of quantum erasure channels in the antidegradable regime (transmission probability at most 1/2), matching an upper bound from fractional extendibility with a permutation-invariant code family.
- **In plain words**: The paper asks how well a quantum message can survive a noisy channel that is too noisy to carry any reliable information at all, yet still preserves some of it. For a common noise model, where each piece of the message is either passed through or lost, the authors work out the best achievable fidelity (how closely the received quantum state matches the original). They find it equals a simple formula, and they show that codes can reach this value.
- **Why it matters**: It gives a precise answer to a question about what is possible in the regime where reliable quantum communication is impossible, which is a useful boundary for the theory. The text does not say how widely the result applies beyond erasure channels, so its broader significance is uncertain.
- **Background needed**: - Quantum channel: a physical process that sends quantum states (such as qubits) from sender to receiver, possibly adding noise.
- Erasure channel: a noise model where each transmitted piece either arrives intact (with probability γ) or is lost and flagged as missing.
- Channel capacity: the maximum rate at which reliable communication is possible; zero capacity means no reliable communication.
- Antidegradable channel: a channel where the environment can obtain at least as much information as the receiver, so the receiver cannot get reliable quantum information.
- Entanglement fidelity: a score from 0 to 1 measuring how well entanglement with a reference system is preserved; the formula γ + (1−γ)/d is the value found here, where d is the dimension of the logical message.
- Fractional extendibility: a mathematical tool used to derive the upper bound on achievable fidelity.
- Asymptotic: referring to the limit of long block lengths. · level: research-level

<details><summary>Original abstract</summary>

Antidegradable quantum channels have zero capacity for reliable quantum communication. However, they can nevertheless transmit quantum information with nontrivial fidelity. This raises the question: how well can quantum information be preserved through such channels? In this work, we exactly characterize the optimal asymptotic entanglement fidelity of quantum erasure channels throughout the antidegradable regime. Specifically, we show that it equals $\gamma+\frac{1-\gamma}{d}$ for transmission probabilities $0<\gamma\le \frac{1}{2}$ and logical dimension $d$. We use fractional extendibility to establish an upper bound on the entanglement fidelity achievable by arbitrary error-correcting protocols. Furthermore, we construct a family of permutation-invariant codes that asymptotically saturates this bound.

</details>

### [Super-Multiplicativity of the Noncommutative Minimum and Applications to Quantum Privacy and Hypothesis Testing](https://arxiv.org/abs/2611.30038)
*Theshani Nuradha, Sujeet Bhalerao, Christoph Hirche et al.* · `quant-ph` · arXiv:2611.30038v1 · relevance 0.12

- **In one sentence**: The paper proves that a noncommutative generalization of the minimum of two positive operators is super-multiplicative, and uses this to derive sub-additivity bounds for the quantum hockey-stick divergence on product states, with applications to quantum differential privacy and symmetric binary quantum hypothesis testing (including the exact Chernoff prefactor).
- **In plain words**: The paper studies how well two quantum states can be told apart when they are combined from separate parts, using a standard measure called the hockey-stick divergence. The authors prove an inequality for a quantity they call the noncommutative minimum, and show it implies that the divergence for combined systems is bounded in a clean way. They then apply this to privacy guarantees for quantum channels and to the error rate of distinguishing two quantum states from many copies.
- **Why it matters**: Quantum differential privacy and quantum hypothesis testing both rely on this divergence, so bounds on how it behaves for combined systems matter for how privacy budgets compose and how fast errors shrink with more samples. The text states the bounds are tight and that the Chernoff prefactor and sample-complexity result hold under stated conditions; its practical impact beyond these theory settings is not discussed in the text.
- **Background needed**: - Quantum states: mathematical descriptions of quantum systems, represented by positive semidefinite operators (matrices) with trace.
- Trace and trace norm: sum of diagonal entries; the trace norm measures how different two operators are.
- Hockey-stick divergence: a measure of distinguishability between two states, tied to differential privacy guarantees.
- Differential privacy: a guarantee that outputs barely change when one input record is swapped for a neighboring one.
- Binary hypothesis testing: deciding which of two states a system is in, given copies of it; error probabilities are the key quantity.
- Chernoff bound: the exponential rate at which the error probability of such tests decays with the number of copies; the paper finds its exact prefactor (the constant multiplying the exponential).
- Sub-additivity and super-multiplicativity: inequalities relating a quantity on combined systems to the same quantity on each part.
- Commuting vs. noncommuting states: classical (commuting) states behave like ordinary probability distributions; quantum (noncommuting) ones do not, which makes the analysis harder. · level: research-level

<details><summary>Original abstract</summary>

The hockey-stick divergence is a fundamental distinguishability measure in quantum information theory. It characterizes quantum differential privacy and determines the optimal error probability of binary quantum hypothesis testing with arbitrary priors. We study how it behaves on tensor-product states. To this end, we consider the noncommutative minimum $m(A,B):=(\mathrm{Tr}[A]+\mathrm{Tr}[B]-\|A-B\|_1)/2$ of positive semidefinite operators, which reduces to $\sum_x\min\{a_x,b_x\}$ when $A$ and $B$ commute, and we prove that it is super-multiplicative, i.e., $m(A\otimes C,B\otimes D)\ge m(A,B)\,m(C,D)$. As a consequence, we establish a sub-additivity property of the hockey-stick divergence on product states, in which the parameters of the individual systems are multiplied, and no additional prefactor appears. We show that this bound is tight, also for noncommuting states, and that it is strict for faithful states whenever at least two of the divergences are positive. Using this, we obtain sub-additivity of the Datta-Leditzky divergences, a parallel composition theorem for quantum differentially private channels under product neighboring inputs with at most linear degradation of the privacy parameters, and a sharp sub-additivity property of the hypothesis-testing relative entropy normalized by the acceptance probability. Finally, we apply the same tools to symmetric binary quantum hypothesis testing. We determine the exact prefactor of the quantum Chernoff bound for every pair of noncommuting states satisfying mild conditions including a nonlattice condition and, under a quantitative version of this condition, the full asymptotic expansion to every fixed order in $1/n$, with explicitly computable coefficients. As a consequence, we determine the sample complexity of symmetric binary quantum hypothesis testing up to one sample, as the error probability tends to zero.

</details>

## High-energy theory and gravity

### [Constraining Regular Black Hole Models with the Effective Field Theory treatment of General Relativity](https://arxiv.org/abs/2611.30616)
*Sami Viollet* · `gr-qc` · arXiv:2611.30616v1 · relevance 0.21

- **In one sentence**: The paper uses the known perturbative quantum correction to the static-particle interaction energy near a black hole, derived from treating general relativity as an effective field theory, as a test that non-perturbative "regular" (modified Schwarzschild) black hole metrics must satisfy, and applies it to the Hayward metric.
- **In plain words**: Physicists want to know what happens inside black holes once quantum effects of gravity are included, and one family of proposed answers is "regular" black holes, which replace the central singularity with a smooth core. This paper offers a way to check such proposals against a quantum correction that can be calculated with the well-established perturbative approach to gravity. The authors find that the Hayward model does not match this check, and they identify the most general modified metric that would reproduce the expected result.
- **Why it matters**: Regular black hole models are widely studied as possible outcomes of quantum gravity, but they are often hard to compare with anything firm. A concrete consistency test tied to a perturbative calculation gives a way to rule models in or out, though the text does not show how far this test reaches beyond the Hayward case.
- **Background needed**: - General relativity: Einstein's theory of gravity, in which mass bends spacetime; the Schwarzschild metric describes a non-rotating black hole.
- Singularity: a point where the classical equations break down, with curvature becoming infinite at the centre of a standard black hole.
- Regular black hole: a modified metric in which the centre is smooth and free of singularity, often proposed as a stand-in for quantum gravity effects.
- Metric: the mathematical rule giving distances and time intervals in spacetime.
- Effective field theory: treating a theory as valid only up to some energy scale, using corrections organised in powers of that scale; here it gives small, calculable quantum corrections.
- Perturbative vs non-perturbative: perturbative calculations expand in a small parameter; non-perturbative approaches aim to capture effects beyond such expansions. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we present a method for using perturbative predictions from treating general relativity as an effective field theory to constrain non-perturbative approaches to quantum gravity in black hole contexts. We start by reviewing a known result from this framework, which estimates the first quantum corrections to the interaction energy of a static particle near a black hole. We then propose a way to test non-perturbative quantum black hole models - specifically those formulated as modified Schwarzschild metrics, also known as regular black holes - against this perturbative result. To illustrate, we apply our method to the Hayward metric, showing that it does not align with the perturbative prediction, and we identify the most general metric that can reproduce the expected result.

</details>

### [For whom the Bell tolls: joint measurements and state updates in quantum field theory](https://arxiv.org/abs/2611.30468)
*Christopher J. Fewster, Christiane K. M. Klein* · `math-ph` · arXiv:2611.30468v1 · relevance 0.19

- **In one sentence**: The paper derives the joint probability distribution of commuting, normal smeared-field observables of the form A(f_i)*A(f_i) in the Fewster-Verch measurement framework (under assumed Fock-space representability), and uses it to build a CHSH Bell-test model with a coupled Proca-scalar polarization setup that violates the CHSH inequality up to Tsirelson's bound in the limit of perfect vacuum-effect rejection.
- **In plain words**: This paper asks how measurements in quantum field theory, the framework describing particles and fields, update the quantum state and whether those updates can produce the strong, "quantum" correlations seen in Bell tests. The authors compute the full joint statistics of several measurements of a field at once, under stated technical assumptions. They then build a simple Bell-test model based on a previously developed polarization model and report that it can exceed the CHSH limit, approaching the maximum allowed by quantum mechanics when background vacuum effects are removed.
- **Why it matters**: It shows that the state-update rules of a rigorous measurement framework for quantum fields are compatible with strongly nonclassical correlations, which matters for foundations of quantum field theory and quantum information. The reach beyond this model is unclear from the abstract alone, and the result depends on the stated assumptions and on the idealisation of perfect vacuum rejection.
- **Background needed**: - Quantum field theory: a description where particles are excitations of fields spread through spacetime.
- Smeared field operator A(f): a field measured with a weighting function f over a region, rather than at a single point.
- Fewster-Verch framework: a rigorous way to describe measurements and state updates in curved spacetime quantum field theory.
- Bell inequality and CHSH: a test of whether measurement correlations can be explained by local hidden variables; quantum mechanics can exceed the classical limit, up to Tsirelson's bound.
- Fock space: the standard mathematical space of states containing variable numbers of particles.
- Normal and commuting operators: technical conditions meaning the measurements can be performed together and their outcomes are well defined jointly.
- Moment generating functional: a tool that encodes all the statistics (averages, spreads) of a distribution in one object.
- Proca field: a massive vector (spin-1) field, used here to model polarization. · level: research-level

<details><summary>Original abstract</summary>

State update rules and their behaviour in Bell tests play an important role in the study of measurement schemes and quantum information. We consider the state updates of the Fewster-Verch measurement framework for quantum field theory using their connection to the probability distribution of measurement outcomes. We focus on a set of observables of the form $A(f_i)^*A(f_i)$, where $A(f)$ is the (complex) smeared field operator for any theory induced by a formally hermitian, Green hyperbolic differential operator, and where the $(A(f_i))_{i=1, \dots, m}$ are assumed to be normal and mutually commuting. Under the assumption that these operators have a sufficiently nice representation on a bosonic Fock space, we derive the joint moment generating functional and the unique joint probability distribution for the observables $(A(f_i)^*A(f_i))_{i=1,\dots,m}$. As an application of these results, we construct a model of a Bell inequality test within quantum field theory using a recently developed coupled Proca-scalar model for polarization measurements. We show that our Bell test model can violate the CHSH inequality, approaching Tsirelson's bound for maximally entangled states in the limit where vacuum effects are perfectly rejected. These results show that the state update rules derived in the Fewster-Verch framework are compatible with strongly quantum correlations. They also support a viewpoint in which state updates should be understood in relation to available information.

</details>

## Statistical physics

### [Statistical mechanics of noisy collisions in active matter: Dyson-Landau theory](https://arxiv.org/abs/2611.30910)
*Horst-Holger Boltz, Max-Robin Schultz, Thomas Ihle* · `cond-mat.stat-mech` · arXiv:2611.30910v1 · relevance 0.16

- **In one sentence**: The paper extends the Landau kinetic equation for weakly interacting particles to include microscopic noise, via a Dyson expansion of the noisy free propagator, and examines how noise and collisions interact in active matter models.
- **In plain words**: Many models of self-propelled or "active" particles, such as flocking animals or motile cells, describe motion with random jitter at the smallest scale, which standard physics derivations do not naturally produce. The authors ask how to build this kind of random noise properly into the kinetic theory that describes how particles collide and exchange momentum. They find that a common shortcut is correct at leading order in one case, but that for aligning particles and for noise acting only during collisions, the corrections are unusual: they are non-analytic, odd in the coupling strength, and their sign depends on the direction of alignment, which agent-based simulations support.
- **Why it matters**: The work addresses a foundational question about whether common modelling shortcuts for active matter are justified from microscopic dynamics. It may matter for the theory of flocking and active fluids, but the text alone does not show how broadly the results apply beyond the minimal models studied.
- **Background needed**: - Kinetic theory: describes many-particle systems by a distribution function evolving under collisions.
- Landau collision integral: the standard kinetic equation for weakly interacting particles.
- Fokker–Planck equation: describes diffusion driven by random noise.
- Dyson expansion: a perturbative series for corrections to a propagator (the evolution operator of a system), here applied to noisy dynamics.
- Active matter: systems whose components consume energy to self-propel, such as flocks or motile cells.
- Dry aligning active matter: self-propelled particles that align their directions without a surrounding fluid.
- Weak noise / high activity: the limit where the random forcing is small relative to the deterministic dynamics.
- Non-analytic and logarithmic corrections: terms that cannot be written as simple power series in the noise strength, indicating subtle long-time interaction effects. · level: research-level

<details><summary>Original abstract</summary>

Active systems and other coarse-grained descriptions are often modeled by generalized dynamics, effective equations of motion that are not bound by the constraints of genuinely microscopic physics. In particular, these equations are generally stochastic on the smallest resolved scale. This poses a challenge to first-principles statistical physics, which usually derives emergent noise on larger scales from deterministic interactions. Here, we show how to systematically incorporate microscopic noise into kinetic theory in the limit of weak noise, i.e., high activity. By means of a Dyson expansion of the noisy free propagator, we derive the leading correction to the Landau kinetic equation for weakly interacting systems. We find that the common practice of combining a deterministic collision integral with the diffusive terms of the Fokker--Planck equation is the correct leading order. For dry aligning active matter, however, the corrections are non-analytic in the noise strength, as nearly parallel particles interact for arbitrarily long times. For noise that acts only during interactions, a minimal model of stochastic interactions, noise and collisions do not decouple: the leading corrections are odd in the coupling strength, partly logarithmically enhanced, and amount to an orientation-dependent effective noise strength. Agent-based simulations confirm the predicted dependence on the sign of the coupling. Even in this minimal model, the effect of noise on collisions can thus not be inferred from symmetry alone.

</details>

### [Trajectory arclength reveals thermodynamic criticality](https://arxiv.org/abs/2611.30053)
*Jim\'enez-L\'opez, Javier, Garc\'ia-Garrido et al.* · `cond-mat.stat-mech` · arXiv:2611.30053v1 · relevance 0.15

- **In one sentence**: For the attractive Hamiltonian mean-field model, the equilibrium-averaged arclength of microscopic Hamiltonian trajectories, written as a normalized Lagrangian descriptor, develops a kink at the phase transition, with a leading finite-size correction scaling as N^(-1/2) and an analytically derived prefactor.
- **In plain words**: The paper asks whether a phase transition, the sudden change a system undergoes such as water freezing, leaves a visible trace in how far its tiny constituent particles travel along their paths of motion. The authors measure the length of those microscopic paths in a simple model of many interacting spins and find a sharp corner (a kink) right at the transition. They also derive how the difference from the infinite-system limit shrinks as the system grows, and report that simulations with up to 10^5 degrees of freedom match these predictions.
- **Why it matters**: The appeal is that the signal is computed from trajectories alone, without tangent-space evolution or a pre-chosen order parameter, which the text presents as a simpler route to detecting criticality. Whether this generalizes beyond the mean-field model studied here is not addressed in the text.
- **Background needed**: - Phase transition: a qualitative change in a system's collective state, such as magnetization appearing below a critical temperature.
- Thermodynamic limit: the idealized case of infinitely many particles; sharp non-smooth features (non-analyticity) appear only there.
- Hamiltonian: the function giving a system's energy, which determines how its particles move over time.
- Mean-field model: a simplified model in which each particle interacts equally with all others, making it analytically tractable.
- Arclength: the total length of a path traced through the system's state space.
- Lagrangian descriptor: a diagnostic computed by integrating a quantity along trajectories, used to probe dynamical behavior.
- Finite-size correction: the deviation from the infinite-system limit that appears in finite systems, here scaling as N^(-1/2) with N the number of particles. · level: research-level

<details><summary>Original abstract</summary>

Thermodynamic criticality arises at continuous phase transitions, where collective interactions produce non-analytic behavior in equilibrium thermodynamic quantities in the thermodynamic limit. We show that this criticality also leaves an analytically predictable signature in the arclength of microscopic Hamiltonian trajectories. For the attractive Hamiltonian mean-field model, we derive the thermodynamic limit of the equilibrium-averaged arclength, formulated as a normalized Lagrangian descriptor, and demonstrate that it develops a kink precisely at the phase transition. We trace this non-analyticity to spontaneous magnetization and derive the leading critical finite-size correction, scaling as $N^{-1/2}$ with an explicit analytical prefactor. Simulations with up to $10^5$ degrees of freedom confirm both predictions without adjustable parameters. Requiring neither tangent-space evolution nor prior specification of an order parameter for its computation, trajectory arclength provides a simple, quantitative link between microscopic Hamiltonian motion and collective thermodynamic criticality.

</details>

## Condensed matter

### [Quantum Hall Effect in a 3D Cross-Dimensional Quantum Anomalous Hall System](https://arxiv.org/abs/2611.28751)
*Liang-Liang Cheng, Ao-Long Li, Zhi-Qiang Zhang et al.* · `cond-mat.mes-hall` · arXiv:2611.28751v1 · relevance 0.24

- **In one sentence**: A theoretical study of how magnetic fields along three high-symmetry directions change Chern numbers, chiral edge-like modes, and multi-terminal Hall responses in a 3D system built by coupling two Weyl-semimetal Hamiltonians, reporting a breakdown of conventional Chern-number-based bulk-boundary correspondence.
- **In plain words**: This paper studies a three-dimensional material model that shows the quantum Hall effect, a precisely quantized electrical response usually seen in flat two-dimensional systems. The authors apply magnetic fields along three special directions and track how the topological counts (Chern numbers) and the paths electrons can travel along the surfaces change. They report that the usual rule linking the bulk count to the surface behavior does not fully hold here, and they check this with computer simulations of Hall transport.
- **Why it matters**: It challenges a standard rule that topological physicists use to predict edge behavior, which matters for interpreting Hall measurements in 3D materials. The text does not show experimental realization or applications, so its practical reach is unclear.
- **Background needed**: - Quantum Hall effect: quantized electrical resistance in a material under a magnetic field, carried by one-way edge currents.
- Chern number: an integer that counts topological twist in a material's electronic bands; it predicts how many one-way edge channels exist.
- Bulk-boundary correspondence: the principle that the interior topology determines what happens at a material's surface or edge.
- Weyl semimetal: a 3D material whose electrons behave like massless particles at points in momentum space, the building block here.
- Quantum anomalous Hall effect: a quantized Hall response produced without an external magnetic field, through internal magnetism.
- Multi-terminal transport: measuring currents and voltages at several electrical contacts to map how current flows. · level: research-level

<details><summary>Original abstract</summary>

We systematically investigate cross-dimensional transport and the resulting quantum Hall effect in 3D quantum anomalous Hall effect systems, which are constructed by coupling two Weyl-semimetal Hamiltonians. Our study unveils that the system hosts highly anisotropic surface states and chiral modes, leading to rich quantum Hall responses. Crucially, we clarify how magnetic fields applied along three high-symmetry directions dictate the evolution of the Chern numbers, chiral modes, and Hall responses. We discover that chiral modes along different directions can originate from distinct mechanisms, giving rise to various magnetic modulation characteristics. Furthermore, we unveil the breakdown of the conventional Chern-number-based bulk-boundary correspondence under magnetic fields, where the Chern numbers alone fail to fully characterize the evolution of the chiral states. This anomalous behavior is attributed to the unique momentum-space distributions of surface bands. These insights are further validated numerically through multi-terminal Hall transport simulations. Our findings expand the understanding of magnetic-field-driven mechanisms in 3D topological systems and provide deeper insights into the interplay between quantized Hall effects and Chern numbers in 3D systems.

</details>

### [Floquet-Induced Valley Polarization and Topological Phases in Twisted Bilayer Graphene Heterostructures](https://arxiv.org/abs/2611.28797)
*A. Belayadi, I. A. Assi, A. Johansson et al.* · `cond-mat.mes-hall` · arXiv:2611.28797v1 · relevance 0.17

- **In one sentence**: A theoretical study of twisted bilayer graphene under circularly polarized light, with broken inversion symmetry from an out-of-plane electric field and insulating substrates, reporting Floquet-induced valley polarization, Chern-number phase transitions (C = -2, -1, 0), valley-polarized domain-wall channels, and spin-valley filtering via adjacent 2D ferromagnetic contacts.
- **In plain words**: This paper is a computer-based theory study of a stack of two sheets of carbon atoms (graphene) twisted relative to each other. Shining circularly polarized light on the stack, and tilting its symmetry with an electric field and surrounding materials, the authors find conditions where one of the two "valleys" (electron energy-momentum sites) stays conducting while the other opens an energy gap and goes quiet. The text reports that this setup can produce topological phase changes and channels that carry only one valley's electrons, and that nearby magnetic layers may allow filtering by spin and valley.
- **Why it matters**: It is a proposal for controlling electron valley and spin with light and fields in a tunable material, which may matter for future electronics concepts. The text is theoretical only and gives no experimental confirmation, so the practical relevance is uncertain.
- **Background needed**: - Graphene: a one-atom-thick sheet of carbon; stacking two sheets with a small twist angle creates a "moiré" pattern that changes how electrons behave.
- Valley: a distinct low-energy momentum point in the electron band structure; "valley degree of freedom" means electrons can carry information in which valley they occupy.
- Dirac-like dispersion: electrons behaving like massless particles, with energy rising linearly with momentum; this gives conducting behavior.
- Band gap: an energy range with no allowed electron states; a gapped valley is effectively switched off.
- Floquet driving: treating a periodically oscillating light field as creating an effective, modified material during illumination.
- Inversion symmetry: a symmetry where the structure looks the same when flipped through a central point; breaking it is needed for the valley effects.
- Chern number: an integer describing the topological character of electron bands; changes signal topological phase transitions.
- Domain-wall channel: a boundary between differently ordered regions that conducts electrons along it.
- Spin-valley filtering: selecting electrons by spin and valley type. · level: research-level

<details><summary>Original abstract</summary>

We theoretically investigate twisted bilayer graphene (tTBG) heterostructures subjected to circularly polarized light. Inversion symmetry is broken through the combined application of an out-of-plane electric field and the incorporation of insulating substrates, enabling precise control of the valley degrees of freedom and associated topological phases. We identify a regime in which the valley degeneracy is lifted: one valley retains a gapless, linear Dirac-like dispersion, whereas the other develops a finite band gap and becomes electronically inactive. The interplay between Floquet driving and inversion-symmetry breaking induces topological phase transitions characterized by Chern numbers C = -2, C = -1, and C = 0, together with the emergence of perfectly valley-polarized domain-wall channels. Furthermore, magnetic asymmetry arising from proximity to adjacent two-dimensional ferromagnetic contacts enables spin-valley filtering. These findings establish the potential of graphene-based heterostructures as highly tunable systems for controlling spin and valley degrees of freedom.

</details>

## Particle physics

### [Dark matter mass fraction in axion stars](https://arxiv.org/abs/2611.30321)
*A. S. Dmitriev, D. G. Levkov, A. G. Panin et al.* · `astro-ph.CO` · arXiv:2611.30321v1 · relevance 0.20

- **In one sentence**: Using an recently derived analytic solution for how Bose stars grow inside QCD axion miniclusters, this paper estimates the present-day fraction of dark matter bound in Bose stars and their resulting mass function.
- **In plain words**: The paper looks at a proposed form of dark matter made of very light particles called axions. In this picture, the dark matter clumps into small, dense blobs, and inside those blobs it may condense into compact "Bose stars," which are like giant quantum clouds. The authors use a previously published mathematical solution for how these stars grow to work out how much of today's dark matter ends up locked in them and how their sizes are distributed.
- **Why it matters**: If dark matter is largely in these compact stars, that would change predictions for how it clusters and for any signals from detectors or astrophysical observations. The text does not state the actual fraction or mass values, so the size of the effect is not clear from the abstract alone, and its link to observations is not described here.
- **Background needed**: - Dark matter: unseen matter that makes up most of the mass of galaxies, detected only through gravity.
- QCD axion: a hypothetical very light particle proposed to solve a puzzle in the strong nuclear force; a candidate for dark matter.
- Minicluster: a small, dense clump of axion dark matter formed early in the universe.
- Bose-Einstein condensation: a state where many identical light particles all occupy the same quantum state, acting like one big wave.
- Bose star: a gravitationally bound, self-gravitating blob of such a condensate.
- Mass fraction and mass function: the share of total dark matter in these stars, and how many stars exist at each mass. · level: research-level

<details><summary>Original abstract</summary>

QCD axion dark matter is fragmented into small mass miniclusters of high density. With the natural parameters of miniclusters, the time for Bose-Einstein condensation is less than the age of the Universe, which leads to the formation of Bose stars inside these structures. Recently, the problem of the subsequent growth of Bose stars was solved analytically (Dmitriev et al, Phys. Rev. Lett. 132, 091001 (2024)). We use this solution to determine present day mass fraction of dark matter in Bose stars and their mass function.

</details>

### [Scotogenic dark matter from gauged $L_\mu+L_\tau$](https://arxiv.org/abs/2611.28223)
*J. Echeverria-Puentes, Sergey Kovalenko, Pablo San Martin Sartori et al.* · `hep-ph` · arXiv:2611.28223v1 · relevance 0.19

- **In one sentence**: A proposed "scotogenic" extension of the Standard Model, built on a gauged L_mu + L_tau lepton-number symmetry, that generates small Majorana neutrino masses at one loop and provides a weakly interacting dark matter candidate stabilized by a remnant matter parity, with analysis of its scalar dark matter, Z' boson, and collider constraints.
- **In plain words**: The paper proposes a theoretical model in which the tiny masses of neutrinos and the invisible dark matter in the universe share a common origin. A new force carrier (Z') linked to the difference between muon-type and tau-type lepton numbers is introduced, and its symmetry breaking leaves behind a leftover "parity" that keeps the lightest new particle from decaying. The authors study which parameter choices give a dark matter abundance matching observations, and check the model against precision electroweak measurements, existing searches for leptophilic gauge bosons, and possible collider signals.
- **Why it matters**: It offers a single framework that links two open problems, neutrino mass and dark matter, through a new gauge boson that could be tested in experiments. The text does not show how strongly the model is favored over alternatives, so its relevance to real data remains to be judged by further work.
- **Background needed**: - Standard Model: the established theory of known particles and forces.
- Neutrino mass: neutrinos have very small masses; Majorana nature means a neutrino is its own antiparticle.
- Scotogenic model: a scheme where neutrino masses arise from a loop of new particles, with a dark matter candidate in that loop.
- Gauged symmetry: a conserved quantity promoted to a force carrier, here L_mu + L_tau (muon and tau lepton numbers), whose boson is the Z'.
- Matter parity: a leftover symmetry (like a sign ±1 for particles) that makes the lightest odd particle stable.
- WIMP: weakly interacting massive particle, a common dark matter candidate with a thermal relic abundance.
- Kinetic mixing: a small coupling between the new force's field and the ordinary photon field, parameterized by epsilon.
- Electroweak precision constraints: high-precision measurements of W, Z and related quantities that limit new physics.
- Leptophilic: a particle that couples mainly to leptons. · level: research-level

<details><summary>Original abstract</summary>

In this work, we introduce the first scotogenic model based on a gauged $L_{\mu} + L_{\tau}$ symmetry whose spontaneous breaking by two units leaves a remnant matter parity $M_P$. The resulting light active neutrinos are of Majorana nature and the lightest electrically neutral state mediating the scotogenic loop is stabilized by $M_P$ and can be identified as a weakly interacting massive particle dark matter candidate. We analyze the phenomenology of a predominantly singlet-like CP-even scalar dark matter candidate and the representative regions of parameter space compatible with the observed thermal relic abundance. The $Z'$ boson is compatible with a broad range of parameters relevant for dark matter. In particular, electroweak precision constraints do not lead to significant tensions for kinetic mixing values up to $\epsilon\sim 10^{-2}$. We discuss the implications of existing searches for leptophilic gauge bosons and the conditions under which visible and invisible collider signatures become relevant.

</details>

## Nuclear physics

### [Emerging Topics for Hard Probes](https://arxiv.org/abs/2611.28688)
*Carlota Andres* · `hep-ph` · arXiv:2611.28688v1 · relevance 0.19

- **In one sentence**: A conference proceedings that gives a personal overview of emerging topics in jet and heavy-flavor physics in relativistic heavy-ion collisions, based on a plenary talk at Hard Probes 2026.
- **In plain words**: This is a short write-up of a survey talk given at a major nuclear physics conference on "hard probes," which are very energetic particles produced in collisions of heavy atomic nuclei at near light speed. The text is a brief preface-style summary, so it does not itself report specific measurements or results. It only says the author chose a personal selection of newer research directions in jets and heavy quarks.
- **Why it matters**: Reviews like this help researchers see which topics are gaining attention in the field. The provided text is too brief to say what specific findings or connections to other areas are made.
- **Background needed**: - Heavy-ion collisions recreate, for a tiny moment, a hot dense state of matter called the quark-gluon plasma.
- "Hard probes" are high-energy particles or jets produced early in a collision that travel through this matter and get altered by it.
- A "jet" is a narrow spray of particles left by an energetic quark or gluon.
- "Heavy flavor" refers to charm and bottom quarks, which are heavy enough to be produced early and track the matter's effects.
- Proceedings are written summaries of talks given at a scientific conference. · level: research-level

<details><summary>Original abstract</summary>

These proceedings present a personal selection of emerging topics in jet and heavy-flavor physics in relativistic heavy-ion collisions, based on a plenary talk delivered at Hard Probes 2026 in Nashville (USA).

</details>

### [Non-Equilibrium Steady States in Nucleosynthesis](https://arxiv.org/abs/2611.30370)
*Zewei Xiong, Gabriel Mart\'inez-Pinedo* · `astro-ph.HE` · arXiv:2611.30370v1 · relevance 0.16

- **In one sentence**: The paper develops a general framework that treats non-equilibrium steady states in nuclear reaction networks as a balance of reaction flows in a reduced linear system, and applies it to four nucleosynthesis scenarios including alpha-rich freeze-out, classical beta-flow r-process, neutrino-assisted r-process, and fission cycling.
- **In plain words**: The paper looks at how heavy elements are built in violent astrophysical settings, where the number of each type of nucleus stays roughly constant even though nuclear reactions are happening quickly. Instead of assuming the system has settled into full chemical balance, the authors describe these "steady" states directly, as a balance of flows between nuclei. They test this approach on four cases and report that it reproduces the expected abundance pattern in each, with an eigenvalue analysis (a standard way of finding the characteristic rates of a system) giving information about network structure and how quickly abundances settle.
- **Why it matters**: Many models of element formation rely on equilibrium shortcuts that may not hold in every setting, so a general way to handle steady states beyond equilibrium could make such calculations more transparent. The text suggests it could also support graph-based methods for large reaction networks, but the extent of that benefit is not shown in the excerpt.
- **Background needed**: - Nucleosynthesis: the formation of atomic nuclei (elements) through nuclear reactions, here mainly in stellar or explosive environments.
- Nuclear reaction network: a set of nuclei linked by reactions that convert one into another, often modeled as coupled equations for abundances.
- Chemical/nuclear equilibrium: a state where forward and reverse reactions balance; NSE and QSE are standard approximations of this.
- Steady state: abundances stay nearly constant over time because production and destruction balance, even though reactions continue; this need not be full equilibrium.
- r-process: rapid neutron capture that builds many heavy elements; beta-flow and fission cycling are specific regimes of it.
- Eigenvalues: characteristic numbers of a linear system that set its relaxation timescales. · level: research-level

<details><summary>Original abstract</summary>

Steady-state behavior underlies many nucleosynthesis processes in which the population number of nuclei can remain nearly constant despite the rapid nuclear reactions. While existing theoretical descriptions largely focus on established chemical equilibrium, as in nuclear statistical equilibrium (NSE) and quasi equilibrium (QSE), non-equilibrium steady states (NESSs) can form in process-specific approximations such as classical $\beta$-flow $r$-process. We develop a general framework for describing NESSs in nuclear reaction networks by formulating the steady-state condition as a balance of reaction flows within a reduced linear description of the relevant network subset. We apply the framework to four representative nucleosynthesis scenarios spanning different steady-state regimes: disequilibrium between nucleons and $\alpha$ particles during $\alpha$-rich freeze-out, the classical $\beta$-flow steady state, the neutrino-assisted $\nu r$-process, and the fission-cycling phase of the $r$-process. In particular, the fission-cycling scenario is described by a quasi-steady-state (QSS) approximation maintaining the population ratios between two nuclei while not conserving the total number of nuclei. The framework reproduces the characteristic abundance pattern for each case while providing a unified interpretation of the underlying steady-state behavior. The eigenvalue spectrum reveals network structure and characterizes the relaxation timescales of abundance distributions. These results establish a general approach for analyzing nucleosynthesis beyond the condition of chemical equilibrium and provide a foundation for extending graph-based methods to complicated nuclear reaction networks.

</details>

## Quantum information and computing

### [Impact of structured noise on bosonic quantum error correction](https://arxiv.org/abs/2611.30303)
*Guoyu Shu, Ling Hu, Hongbo Wu et al.* · `quant-ph` · arXiv:2611.30303v1 · relevance 0.20

- **In one sentence**: Experiments in a 3D superconducting circuit show that structured environmental noise makes single-photon loss depend on the photon-number state of a weakly nonlinear oscillator, deforming the error space assumed by bosonic quantum error correction, with transient dynamics matched by a second-order time-convolutionless theory.
- **In plain words**: Quantum computers can store information in microwave resonators, where photons are the carriers and sometimes leak out. The standard models assume every stored state leaks in the same simple way. This paper shows that when the surrounding environment is not flat in frequency, the leak rate can depend on how many photons are present, and that this changes which errors a correction scheme must handle.
- **Why it matters**: Bosonic error-correction schemes are designed around an idealized loss model, so a state-dependent leak could make them less effective than their design assumes. The text reports agreement between measurements and a theory for the transient behavior, and a demonstration with a logical qubit; its broader implications for hardware design are for the authors and readers to judge.
- **Background needed**: - Bosonic mode: a resonator (here a microwave cavity) whose excitations are photons, counted by the number of photons, or Fock state.
- Photon loss: photons leaking out of the cavity into its environment, the main error in these devices.
- Quantum error correction: encoding information redundantly so that certain errors can be detected and undone.
- Binomial code: a specific encoding of a logical qubit across several photon-number states.
- Markovian vs non-Markovian: Markovian means the environment forgets quickly, so loss rates are constant; non-Markovian means memory effects shape the early dynamics.
- Time-convolutionless theory: a mathematical method for describing open quantum systems with memory.
- Circuit QED: superconducting circuits coupled to microwave resonators, used to build and probe such oscillators. · level: research-level

<details><summary>Original abstract</summary>

Bosonic quantum error correction relies on an accurate description of single-photon loss dissipation using an ideal annihilation operator, under which correctable loss errors act equivalently on different logical code states. In realistic weakly nonlinear bosonic modes, however, coupling to a structured environment can render photon loss Fock-state dependent, thereby modifying the effective dissipation operator and deforming the associated error space. Here, we experimentally investigate this effect in a three-dimensional circuit quantum electrodynamics system. By injecting spectrally engineered environmental noise into a weakly nonlinear oscillator, we observe pronounced frequency selectivity in the measured Fock-state dynamics. While the long-time transition rates converge to the Markovian limit, the transient dynamics display distinctly non-Markovian behavior, in quantitative agreement with a second-order time-convolutionless theory. By applying narrowband noise to a binomially encoded logical qubit, we further demonstrate Fock-state-dependent dissipation channels that drive logical states beyond the nominally correctable error space. These results establish structured environmental noise as a mechanism for deforming photon-loss errors in weakly nonlinear bosonic systems and highlight the need to incorporate realistic, state-dependent dissipation into the design and characterization of bosonic quantum error correction.

</details>

### [Quantum Approximation and Integration in Sobolev Spaces -- Low Smoothness](https://arxiv.org/abs/2611.31000)
*Stefan Heinrich* · `quant-ph` · arXiv:2611.31000v1 · relevance 0.17

- **In one sentence**: The paper studies the query complexity of approximation and integration over Sobolev spaces in the quantum setting of information-based complexity, dropping a previously assumed embedding condition and using a quantum version of a stochastic discretization technique.
- **In plain words**: This paper is about how many questions a quantum computer needs to ask about a smooth function in order to estimate it or to compute its average (integral) to a given accuracy. The authors extend earlier results to functions with low smoothness, where a previously used condition no longer applies. They do this by adapting a random-sampling-based discretization method to the quantum setting.
- **Why it matters**: Work on the cost of approximating and integrating functions with quantum queries connects the theory of quantum algorithms to numerical analysis. The text given does not report specific results or bounds, so its significance beyond this extension cannot be judged from the excerpt.
- **Background needed**: - Sobolev space: a family of functions with limited smoothness, measured by how many derivatives are square-integrable.
- Information-based complexity (IBC): a field that asks how much information (number of function evaluations or queries) is needed to solve a continuous math problem to a target accuracy.
- Quantum setting: the algorithm can query the function through quantum operations, which can allow different cost scaling than classical sampling.
- Approximation vs. integration: approximation reconstructs the whole function; integration estimates its average value.
- Embedding condition: a technical assumption relating the smoothness space to a function space with weaker requirements; the paper drops it.
- Discretization: replacing a continuous function with a finite set of sampled or computed values.
- Only the abstract-level description is available; no formulas or numerical results are included in the text. · level: research-level

<details><summary>Original abstract</summary>

We study the complexity of approximation and integration in Sobolev spaces in the quantum setting of information-based complexity theory (IBC). Previous results have been obtained under the assumption that the embedding condition holds. Here we drop this assumption and use a quantum version of a previously developed stochastic discretization technique.

</details>

## Optics and atomic physics

### [Stellar Temporal Intensity Interferometry with Adaptive Optics at the Palomar Observatory](https://arxiv.org/abs/2611.30257)
*Darren Ming Zhi Koh, Xi Jie Yeo, Sam Halverson et al.* · `astro-ph.IM` · arXiv:2611.30257v1 · relevance 0.19

- **In one sentence**: The paper reports the first detection of temporal photon bunching (a correlation in photon arrival times, quantified by g^(2)(0)) from a resolved star, α Her, using narrowband filtering, fast single-photon counters, and the adaptive optics system at Palomar Observatory.
- **In plain words**: Starlight arrives as a stream of individual light particles, and their arrival times can be correlated in a way that depends on the star's size and on quantum statistics. The authors looked for this timing pattern in light from the red supergiant α Her, using a very narrow color filter, fast photon detectors, and the telescope's adaptive optics, which corrects for air turbulence. They report a peak correlation value of 1.3 ± 0.1 for this star.
- **Why it matters**: The text claims this shows temporal intensity interferometry can be a practical observing method, linking quantum optics with stellar astronomy. Whether it will yield stellar measurements beyond this one target is not shown in the text, so its broader reach remains uncertain.
- **Background needed**: - Photon bunching: photons from thermal sources like stars tend to arrive in clumps; g^(2)(0) measures the strength of this clumping at zero time delay (1 means no correlation, higher means more bunching).
- Intensity interferometry: combining light intensity fluctuations from two telescopes (rather than raw light waves) to measure a star's angular size; it is robust to air turbulence.
- Temporal vs spatial correlation: spatial intensity interferometry compares light between separated telescopes; temporal version compares arrival times of photons at one detector.
- Adaptive optics: deformable mirrors that cancel out atmospheric blurring in real time.
- Narrowband spectral filtering: restricting light to a very narrow color band so the quantum correlation is not washed out.
- Single-photon counting: detectors that register individual photons and their arrival times.
- Red supergiant: a very large, cool, luminous star near the end of its life. · level: research-level

<details><summary>Original abstract</summary>

Spatial intensity interferometry has seen a major resurgence in astronomy due to its immunity to atmospheric phase turbulence, but its temporal counterpart - a cornerstone of quantum optics - has remained largely unexplored for astronomical sources. Here, we demonstrate that high-visibility temporal photon bunching signatures from stellar sources are now accessible by combining ultra-narrowband spectral filtering with high-speed single-photon counting detectors. Leveraging the adaptive optics architecture at the Palomar Observatory, we report the first observation of resolved stellar temporal photon bunching, with a peak of $g^{(2)}(\tau=0) = 1.3 \pm 0.1$, from the red supergiant $\alpha$ Her. This advance establishes stellar temporal intensity interferometry as a viable observational modality, bridging quantum optics with high-resolution stellar astrophysics.

</details>

### [1.2 dB Insertion Loss in a Monolithically Integrated Silicon Mach-Zehnder Optical Isolator Using Stoichiometric Ce:YIG](https://arxiv.org/abs/2611.30501)
*Zhenyuan Ren, Di Wu, Tianchi Zhang et al.* · `physics.optics` · arXiv:2611.30501v1 · relevance 0.09

- **In one sentence**: Shows that making cerium-doped yttrium iron garnet (Ce:YIG) films closer to exact stoichiometry, via an iron-deficient sputtering target, removes nano-cluster defects and yields a silicon Mach-Zehnder optical isolator with 1.2 dB insertion loss at 1556 nm.
- **In plain words**: Optical isolators are devices that let light pass in one direction while blocking reflections going back, which keeps chip-based light circuits stable. This paper addresses why such isolators on silicon chips lose too much light, and traces the problem to the chemical makeup of the magnetic garnet film used in them. By adjusting the target material so the film has the intended chemical ratio, the authors removed small clusters of mismatched material and built an isolator that lost only 1.2 dB of light.
- **Why it matters**: Insertion loss is a main obstacle to putting isolators on photonic chips, so a lower loss figure matters for that goal. The text reports a figure of merit 1.7 times higher than non-stoichiometric films, but it describes a single device demonstration, so its broader practical impact is not yet shown.
- **Background needed**: - Optical isolator: a one-way valve for light; it stops back-reflected light from disturbing a laser or circuit.
- Photonic integrated circuit (PIC): a chip that guides light through tiny waveguides, analogous to an electronic chip for light.
- Magneto-optical (MO) effect: a material rotates the polarization of light when a magnetic field is applied; this rotation is what enables one-way behavior.
- Faraday rotation: the amount of polarization rotation per unit length; measured in degrees per centimeter.
- Figure of merit (FoM) here: Faraday rotation divided by optical loss, in degrees per dB; higher means less loss for a given rotation.
- Stoichiometry: the exact ratio of elements in a compound; deviations can form unwanted clusters.
- Ce:YIG: cerium-substituted yttrium iron garnet, a magneto-optical garnet material.
- Mach-Zehnder interferometer (MZI): a light-splitting and recombining layout used here to build the isolator.
- Insertion loss (dB) and isolation ratio (dB): how much light is lost passing forward, and how strongly backward light is blocked. · level: research-level

<details><summary>Original abstract</summary>

Integrated optical isolators play a crucial role in photonic integrated circuits (PICs) by effectively stabilizing optical signals, making them indispensable components for advanced photonic systems. However, integrated magneto-optical (MO) isolators suffer from their high insertion loss, which is mainly caused by the relatively low FoM of Ce:YIG MO thin films deposited on silicon. Here, we show that film stoichiometry plays a key role in controlling the FoM of Ce:YIG. We observed garnet phase Fe-rich and Ce-rich nano-clusters in non-stoichiometric Ce:YIG. By using an iron-deficient target, we demonstrated that nearly stoichiometric Ce:YIG films on Si(100) could be fabricated, eliminating the nano-cluster defects. Consequently, the film exhibited a saturation Faraday rotation angle of -5523 deg/cm and a figure of merit of 72.7 deg/dB, which is 1.7 times higher compared to nonstoichiometric films. An MZI-type optical isolator on SiN fabricated by this method demonstrated a record low insertion loss of 1.2 dB and isolation ratio of 27.6 dB at 1556 nm wavelength. Our results provide an important step toward the practical application of integrated MO nonreciprocal photonic devices.

</details>

## Fluids and plasma

### [Statistical Signatures of Velocity-Space Turbulence in the Earth's Magnetosheath](https://arxiv.org/abs/2611.28546)
*Tien Vo, Robert Ergun, Alexandros Chasapis et al.* · `physics.plasm-ph` · arXiv:2611.28546v1 · relevance 0.11

- **In one sentence**: Statistical study of MMS magnetosheath ion velocity-space spectra, reporting isotropic -3/2 and anisotropic -2 populations organized by ion beta and bulk flow, with velocity-space spectral index correlated with estimated real-space energy transfer rates.
- **In plain words**: Space plasmas, the hot electrically charged gas around Earth, often have particles whose speeds are far from a settled, evenly mixed state, which stores energy that can be passed around. This paper uses spacecraft data from NASA's Magnetospheric Multiscale mission, taken in the magnetosheath (the turbulent region just outside Earth's magnetic boundary), to look for signs of energy being passed between particle speeds, not just between locations in space. The authors report two main patterns in how ion speeds are spread out, and that these patterns follow plasma conditions.
- **Why it matters**: If energy cascades through velocity space as well as through physical space, it could help explain how turbulence heats plasmas and divides energy between thermal and non-thermal particles. The text presents this as observational evidence and notes broad implications for space and astrophysical plasmas, but the scope of those implications is not established in the abstract.
- **Background needed**: - Plasma: a gas of charged particles, common in space and stars.
- Magnetosheath: the turbulent region of plasma between Earth's bow shock and magnetopause.
- Velocity space: a map of how particles are distributed by their speed and direction, rather than by position.
- Power-law spectrum: a pattern where signal strength falls off as a fixed power of scale; the index (such as -3/2 or -2) describes how steep that fall-off is.
- Isotropic vs anisotropic: the same in all directions versus stronger in some directions than others.
- Ion beta: the ratio of particle pressure to magnetic pressure, describing which dominates.
- Energy cascade: energy moving from large scales to small scales, a standard idea in turbulence.
- Magnetospheric Multiscale (MMS): a NASA mission of four spacecraft measuring near-Earth plasma. · level: research-level

<details><summary>Original abstract</summary>

In collisionless plasmas, the particle distributions are often far from local thermodynamic equilibrium, providing a significant source of free energy that leads to complex velocity-space dynamics. In turbulent plasmas, the possibility of a cascade of the free energy in velocity space, analogous to the spatial cascade of fluid and electromagnetic field energies, has been suggested. However, observational evidence of plasma turbulence throughout phase space remains limited. Using measurements from the Magnetospheric Multiscale mission in a special campaign in the Earth's magnetosheath, we present the first statistical study of signatures consistent with velocity-space turbulence across a wide range of plasma conditions. We observe two main populations in the ion velocity-space spectrum -- an isotropic $-3/2$ spectrum and an anisotropic $-2$ spectrum organized by the ion $\beta$ and bulk flow. In addition, the spectral power laws in the spatial and velocity domains are uncorrelated, while the velocity-space spectral index is correlated with estimated real-space energy transfer rates. These results reveal how the ion spectral properties are systematically organized by plasma conditions and related to real-space turbulence. This connection has broad implications for turbulence and the energy partition between thermal and non-thermal particles in space and astrophysical plasmas.

</details>

### [Generation and characterization of unsteady inflows in a fan-vane wind tunnel](https://arxiv.org/abs/2611.29228)
*Yutong Liu, Gang Hu, Hongwei Zhang* · `physics.flu-dyn` · arXiv:2611.29228v1 · relevance 0.09

- **In one sentence**: The paper shows that pseudorandom angle commands to downstream vanes in a 768-fan wind tunnel can tune turbulence intensity and integral length scale, with measured spectra and downstream evolution reported for a 60% duty-cycle case.
- **In plain words**: Wind tunnels are used to test objects in moving air, and tests often need gusty air with a specific strength and size of swirls. This paper describes a fan-driven tunnel where rows of movable vanes are tilted by a control signal to create such gusts. The authors found that bigger vane tilts made the air much more turbulent, and changing the shape of the control signal changed how large the swirls were, while the strength stayed similar.
- **Why it matters**: Being able to set both how strong and how large the gusts are, independently, could make wind-tunnel tests more representative of real conditions such as wind over buildings or vehicles. The text does not establish how far these results transfer to other facilities or to real-world flows, so that link is uncertain.
- **Background needed**: - Turbulence intensity: the size of random air speed fluctuations relative to the average speed, given as a percentage.
- Integral length scale: a rough measure of the typical size of the swirling eddies in the flow.
- Fan-vane wind tunnel: a grid of fans whose output is steered by downstream vanes that can be tilted.
- Pseudorandom signal: a control signal that looks random but is generated by a fixed rule, so it can be repeated exactly.
- Power spectrum: a chart showing how much of the fluctuation energy sits at each frequency; low frequencies correspond to large, slow swirls.
- Hot-wire measurement: a very thin heated wire whose cooling by passing air is used to measure air speed. · level: intermediate

<details><summary>Original abstract</summary>

Wind-tunnel experiments often require inflows with specific combinations of turbulence intensity and integral length scale because both can influence the measured response. To broaden the range of attainable inflows, this study uses pseudorandom vane excitation to generate large-scale turbulence and examines how both quantities vary with the amplitude and spectral shape of the vane-angle command. In each test, the 15 servo-driven vanes downstream of a 768-fan array received the same angle command, and all fans operated at a common, constant duty cycle. Hot-wire measurements covered twenty heights and selected spanwise and downstream positions. At a fan-control duty cycle of 60%, increasing vane angular amplitude raised profile-mean turbulence intensity from 7.3% to 31.8% under periodic forcing and from 6.2% to 23.0% under pseudorandom forcing. With the normalized pseudorandom command spectrum held fixed, larger angular amplitudes increased the low-frequency share of velocity variance, accompanied by longer correlation times and larger integral scales. At a root-mean-square angular amplitude of 15 degrees, changing the command spectrum yielded profile-mean integral length scales of 0.88-1.67 m at similar turbulence intensities. The principal features of the velocity spectra persisted between 2 and 4 m downstream, while integral scales continued to change. Both forcing types exhibited middle-region minima in turbulence intensity and integral scale. Regional analysis of a representative pseudorandom case linked these minima to weaker low-frequency fluctuations and shorter correlation times. These findings provide a basis for selecting vane inputs according to the turbulence-intensity and integral-scale requirements of the intended test region.

</details>

## Biological physics

### [Impact of Topology and Sequence Length on the Pressure-Dependent Collapsibility of Proteins](https://arxiv.org/abs/2611.30336)
*Jiayi Wang, D. Thirumalai, Margaret S. Cheung et al.* · `physics.bio-ph` · arXiv:2611.30336v1 · relevance 0.07

- **In one sentence**: A theoretical study extending the protein "collapsibility" framework with a pressure-dependent desolvation (water-release) term, showing that pressure-induced changes in water-mediated collapse depend on native-state topology and especially on the share of non-local contacts.
- **In plain words**: This paper asks how squeezing a protein with hydrostatic pressure, the same kind of uniform pressure felt deep in the ocean, changes how readily its chain folds into a compact ball. The authors add a pressure-dependent term for how water interacts with the chain to a simple model, and find that higher pressure destabilizes the fully folded shape while still favoring compact, water-mediated conformations. How strongly pressure shifts this tendency depends on the protein's overall structure, and proteins or domains with more non-local contacts (amino acids far apart in the chain that touch in the folded shape) tend to show a larger pressure-induced effect.
- **Why it matters**: Pressure is a physical perturbation that helps separate the forces holding proteins together, and linking it to native-state structure may clarify why different proteins respond differently to environmental stress. The text does not show direct experimental tests or practical applications, so the wider significance remains uncertain.
- **Background needed**: - Protein folding: a chain of amino acids settles into a specific 3D shape, the "native state."
- Collapsibility: how strongly a sequence tends to pull into a compact blob, which is distinct from reaching the right final shape (foldability).
- Hydrostatic pressure: uniform squeezing from all sides, such as at great ocean depths.
- Desolvation: the cost or gain of stripping water away from chain surfaces when they come together.
- Native contacts: pairs of amino acids that touch in the folded structure; non-local ones are far apart along the chain sequence.
- Topology: the overall arrangement of secondary (local helices and sheets) and tertiary (global packing) structure.
- The work is computational/theoretical; the abstract does not describe the specific model details or quantitative results. · level: research-level

<details><summary>Original abstract</summary>

Several physical and evolutionary factors, including temperature, pressure, solvent quality, and natural selection, influence how amino acid sequences adopt their native structures. Although protein folding has been extensively studied, the physical determinants of protein collapse and their relationship to native-state folding remain less understood. In particular, "collapsibility", the intrinsic propensity of a protein sequence to form compact conformations, is distinct from but closely related to "foldability", the ability to reach the native structure. Previous theoretical studies suggested that collapsibility is encoded in native-state topology, potentially reflecting evolutionary selection. However, the roles of solvent-mediated interactions and hydrostatic pressure remain unclear. Here, we extend the theoretical framework of protein collapsibility by incorporating a pressure-dependent desolvation potential to investigate how hydrostatic pressure influences protein collapse. We find that increasing pressure destabilizes the fully folded native state, but can still favor the compact, water-mediated conformations. Furthermore, the magnitude and direction of pressure-induced changes in collapsibility depend strongly on native-state topology, including secondary and tertiary structures. Proteins and domains with a higher proportion of non-local native contacts generally exhibit greater pressure-induced water-mediated collapsibility. These findings highlight the role of native-state topology in determining the pressure sensitivity of protein collapse and provide insights into the interplay among protein structure, solvent-mediated interactions, and environmental perturbations.

</details>

### [Infrared Relaxation Modes and the Emergence of Collective Order in Neural Dynamics](https://arxiv.org/abs/2611.29880)
*Byung Gyu Chae* · `physics.bio-ph` · arXiv:2611.29880v1 · relevance 0.07

- **In one sentence**: The paper proposes a microscopic field theory in which the quadratic kernel of an effective action, after integrating out individual neural degrees of freedom, sets the threshold for collective ordering, with spectral weight and relaxation rates linked to instability and memory, and checks this with numerical constructions and Transformer Jacobian spectra.
- **In plain words**: The paper asks when a network of interacting nonlinear units, such as neurons, starts to act together in a coordinated way, and how that coordination relates to how long the network keeps a memory. The authors build a mathematical framework that averages out the individual units to get a single effective description, then study how the timescales of the system's responses control when order appears. They report that stronger low-frequency (slow-timescale) spectral content lowers the coupling needed for order and produces longer-lasting memory, and they add some numerical and Transformer-model checks.
- **Why it matters**: Understanding the link between collective order and persistent memory in neural-like systems could matter for both neuroscience and the study of learning in artificial networks. The text, however, gives only an abstract-level account without the detailed derivations, data, or comparisons needed to judge how general the claims are, so their significance remains unclear.
- **Background needed**: - Effective action: a compact mathematical function that summarizes a system after its individual parts have been averaged out.
- Quadratic kernel: the simplest (second-order) part of that function; its sign or value indicates when a uniform state becomes unstable.
- Landau expansion: a general way to describe an ordering transition (like a magnet forming or a liquid freezing) as a polynomial in an order parameter.
- Critical coupling: the strength of interaction at which collective order first appears.
- Spectral decomposition / relaxation rates: splitting a system's response into modes that decay at different speeds; slow modes dominate long-time memory.
- Infrared spectral weight: in this context, the share of response carried by slow, long-wavelength or low-frequency modes.
- Jacobian: a matrix of how small input changes propagate through a network; its spectrum describes how stable or sensitive the network's responses are.
- Critical-like response: behavior resembling systems poised near a phase transition, where responses are unusually long-lived. · level: research-level

<details><summary>Original abstract</summary>

We develop a microscopic field theory of collective order formation in interacting nonlinear neural systems. Integrating out microscopic neural degrees of freedom yields an effective action whose quadratic kernel determines the ordering threshold, while higher-order connected responses govern nonlinear stabilization. Spectral decomposition reveals that relaxation rates and collective-mode overlaps control collective instability and memory dynamics. Enhanced infrared spectral weight lowers the critical coupling and generates long-time memory, revealing a common spectral origin of collective ordering and persistent dynamics. Controlled numerical constructions verify the spectral dependence of collective instability and response, while nonlinear mean-field scaling follows from the microscopic Landau expansion. Transformer Jacobian spectra further reveal learning-induced infrared organization and transient memory enhancement consistent with critical-like response. Our results establish a microscopic framework linking neural interactions, collective order, and long-time memory.

</details>

## Climate, atmosphere and Earth

### [Competing climates of the present-day Earth: from Snowball to Hothouse](https://arxiv.org/abs/2611.28357)
*Laure Moinat, John Marshall, Maura Brunetti* · `physics.ao-ph` · arXiv:2611.28357v1 · relevance 0.15

- **In one sentence**: Using the BIG-MITgcm coupled climate model, which links atmosphere, ocean, ice sheets and vegetation over many millennia, the authors report five alternative stable climate states for present-day Earth's continents, solar output and pre-industrial CO2, and argue that ocean heat transport sets where the ice edge sits in each.
- **In plain words**: Earth's climate today is only one of several states it could settle into with the same continents, Sun output and carbon dioxide level. The authors ran a long-timescale computer model and found five such states, from a planet fully covered in ice (a "Snowball") to a much warmer one where the Atlantic's overturning ocean circulation has shut down. Each state is kept in place by its own balance of feedbacks, such as ice reflecting sunlight.
- **Why it matters**: If several climates are stable under today's conditions, the present one is not guaranteed, which bears on how past glacial-interglacial shifts happened and on the risk of crossing future tipping points. The text does not show how well the model captures real-world behaviour, so these links remain suggestions rather than established results.
- **Background needed**: - Climate "state": a long-lasting pattern of temperature, ice cover and ocean circulation that a system can stay in.
- Feedback: a process where a change amplifies or dampens the original change; for example, ice reflects sunlight, so more ice cools the planet further.
- Snowball Earth: a hypothesised episode in which ice covers the whole planet, pole to pole.
- Last Glacial Maximum: the peak of the most recent ice age, about 20,000 years ago.
- Ocean heat transport: the movement of heat from warm regions to cold ones by ocean currents.
- Atlantic overturning circulation: a large-scale current system that carries warm water north in the Atlantic and cold water south at depth.
- Coupled model: a computer model that links several parts of the Earth system (air, ocean, ice, plants) so they affect one another.
- Pre-industrial CO2: the atmospheric carbon dioxide level before the industrial era, used as a fixed reference. · level: research-level

<details><summary>Original abstract</summary>

Earth today has one climate, but it could have others. With the same continents, the same solar constant and the same pre-industrial CO2, our planet could settle into strikingly different ones. We explore this possibility with BIG-MITgcm, a model which couples atmosphere and ocean circulation with ice sheets and vegetation, and which can be integrated over many millennia. We find five different climates and describe them here. At one extreme is a Snowball, with ice from pole to pole. A Waterbelt also exists, in which sea ice reaches the tropics and only a thin equatorial ribbon of open ocean survives. There is a Cold world much like the Last Glacial Maximum, a Warm climate in which we live in today, and a Hot world in which the Atlantic overturning circulation has collapsed. Each state is held in place by its own balance of competing feedbacks. Ocean heat transport anchors each climate, holding the ice edge where that transport is weak. The familiar climate of the past 10 thousand years is perhaps just one of several possibilities. This has implications for glacial-interglacial transitions and the risk of crossing global tipping points in the future.

</details>

### [Stochastic climate emulation at reduced cost with ACE2.5-ERA5](https://arxiv.org/abs/2611.28315)
*Jeremy McGibbon, Troy Arcomano, Spencer K. Clark et al.* · `physics.ao-ph` · arXiv:2611.28315v1 · relevance 0.10

- **In one sentence**: ACE2.5-ERA5 is a stochastic, autoregressive AI emulator of ERA5 reanalysis that adds noise conditioning, a spectrally bottlenecked Spherical Fourier Neural Operator backbone, and a daily time step, yielding calibrated ensembles, improved small-scale precipitation spectra, and cheaper training and inference than its predecessor ACE2-ERA5.
- **In plain words**: This paper presents a new AI model that imitates the global weather and climate record (ERA5) and can produce many possible future weather paths, not just one. The authors report that its spread of possible outcomes matches its actual forecast errors well from about day 3 onward, that it keeps finer-scale rain patterns more faithfully than the previous version, and that it runs stably for 1000 simulated years. It is also smaller, faster, and cheaper to train, and the team released model checkpoints.
- **Why it matters**: Ensembles that are well calibrated, meaning their spread honestly reflects uncertainty, are central to useful weather and climate prediction, and cheaper emulators could make such experiments accessible to more groups. The text also notes that year-to-year variability of global mean temperature is not calibrated in either model, so the approach has a known limit. Broader impact is not established by the text alone.
- **Background needed**: - Emulator: a fast statistical or AI model trained to reproduce a slower physics-based simulation or observed data record.
- ERA5: a widely used global reanalysis dataset that combines past observations with a weather model to give a consistent history of the atmosphere.
- Autoregressive: the model predicts the next time step from the current state and repeats, producing long simulations.
- Ensemble: a set of runs from slightly different starting conditions or noise, used to express uncertainty.
- Calibrated: the ensemble spread matches how large the real errors actually are.
- CRPS (continuous ranked probability score): a loss function that rewards probabilistic forecasts that are both sharp and accurate.
- Spectral power / wavenumber: how much variation sits at each spatial scale; higher wavenumbers mean finer detail.
- ENSO: El Niño–Southern Oscillation, a recurring tropical Pacific climate pattern that affects rainfall worldwide.
- Spherical Fourier Neural Operator: a neural network design that works on the sphere of the Earth using spherical harmonics. · level: research-level

<details><summary>Original abstract</summary>

We introduce ACE2.5-ERA5 (Ai2 Climate Emulator of ERA5, version 2.5), a stochastic autoregressive weather-climate AI model that produces calibrated weather ensembles with realistic small-scale structure on timescales from days to centuries. Its deterministic predecessor, ACE2-ERA5, retains 36% of its ERA5 target's precipitation spectral power at total wavenumbers 100--179; ACE2.5-ERA5 retains 86%. In weather forecasts its ensemble spread matches its error to within 4% from day 3. Time-mean climate is on par with or better than ACE2-ERA5, the precipitation response to ENSO is improved, and the model is stable over 1000 years. Interannual variability of global mean surface temperature is shown not to be calibrated in either ACE2.5-ERA5 or its predecessor. ACE2.5-ERA5 differs from ACE2-ERA5 in three ways. Noise-conditioned layer normalization, trained with a combined CRPS and spectral energy score loss in place of mean squared error, makes it stochastic. Spectral bottlenecking with grouped convolutions cuts the Spherical Fourier Neural Operator's spectral filter parameters by more than two orders of magnitude and leaves a model a tenth the size of ACE2-ERA5. Its time step is daily rather than 6-hourly. ACE2.5-ERA5 has 3.2 times the inference throughput of ACE2-ERA5. A 6-hourly variant has weather prediction skill similar to ACE2-ERA5. A 4-degree variant reaches comparable climate skill at an order of magnitude lower training cost, enabling rapid iteration during development. We release 1-degree daily, 4-degree daily and 1-degree 6-hourly checkpoints.

</details>

## Cosmology

### [$w_0$ Is All You Need: Field-Level Matching of General Dark Energy Models to $w_0$CDM Simulations](https://arxiv.org/abs/2611.29776)
*Pavel Demidov, Carolina Cuesta-Lazaro, Peter L. Taylor* · `astro-ph.CO` · arXiv:2611.29776v1 · relevance 0.19

- **In one sentence**: The paper proposes that clustering of matter in general dynamical dark energy models w(z) can be reproduced by a constant-w0 CDM simulation via spectral equivalence, matching comoving distance to the last scattering surface, and tests this with N-body runs including spline-based w(z).
- **In plain words**: Cosmologists simulate how matter clumps together in the universe, and the outcome depends on the unknown "dark energy" that drives cosmic expansion. This paper asks whether a simpler, constant-strength dark energy simulation can stand in for many more complicated versions. The authors report that, in their simulations, matter patterns from the more complicated models match the simple reference case closely, within a fraction of a percent for the measured statistics.
- **Why it matters**: If the matching holds, researchers could test many dark energy models against survey data without running a new set of expensive simulations for each one, which matters for upcoming large sky surveys. The text does not show how well this generalizes beyond the models and statistics tested, so the broader claim remains to be checked by others.
- **Background needed**: - Dark energy: an unknown component thought to drive the accelerating expansion of the universe; its equation of state w describes how its pressure relates to its energy density.
- w0CDM: a standard model where w is a single constant value today (w0).
- w(z): a dark energy equation of state that changes with redshift (z, a measure of look-back time).
- CPL parametrization: a common two-parameter form w0 + wa(1-a) for time-varying dark energy.
- N-body simulation: a computer simulation that tracks many particles under gravity to model how cosmic structure forms.
- Power spectrum and bispectrum: statistics measuring how strongly matter clusters at different scales (two-point and three-point correlations).
- Wavelet scattering transform: a summary statistic for non-Gaussian patterns in a field.
- Spectral equivalence: the idea that two models give nearly identical matter fields under a specific matching rule. · level: research-level

<details><summary>Original abstract</summary>

We show that clustering in general dynamical dark energy models $w(z)$ can be predicted with constant dark energy $w_0\text{CDM}$ models at the field level via spectral equivalence. The prescription of this method requires equating comoving distances to the last scattering surface between predictor and target models, which is equivalent to requiring equal recent background expansion history averages. Dark energy models with the same distance thus form approximate equivalence classes, with nearly identical matter fields. To test the precision of spectral equivalence beyond the CPL parametrization, we run $N$-body simulations with various dynamical dark energy models, including spline-based $w(z)$, all matched to a single $w_0\text{CDM}$ run. Our measurements show that the power spectra of all matched dark energies agree with the predictor within $0.2\%$ up to $k = 0.5\,h\,{\rm Mpc}^{-1}$ and within $0.6\%$ up to $k = 1\,h\,{\rm Mpc}^{-1}$. We also compare the non-Gaussian information contained in the simulated fields. Bispectra differ by at most $0.26\%$ across all runs up to $k = 0.5\,h\,{\rm Mpc}^{-1}$ and $1.75\%$ up to $k = 1\,h\,{\rm Mpc}^{-1}$, while wavelet scattering transform coefficients are all within $0.05\%$. The decorrelation, $1 - r^2$, between each matched field and the predictor stays below $0.006\%$ up to $k = 1\,h\,{\rm Mpc}^{-1}$. We run a toy power spectrum analysis in the CPL parametrization demonstrating that a $w_0$-only emulator could produce the same posterior without any knowledge of the full $w_0w_a$ model. This matching prescription thus offers a new tool to constrain dynamical dark energy models with arbitrary equations of state at the field level, without running additional simulation suites.

</details>

### [Analytic $k$-essence Inflation](https://arxiv.org/abs/2611.30846)
*V. K. Oikonomou* · `gr-qc` · arXiv:2611.30846v1 · relevance 0.17

- **In one sentence**: The paper derives a fully analytic k-essence inflation model with kinetic term K(X)=X^n/X_s^(n-1) and a tracking condition, where constant sound speed avoids gradient instabilities and a pressure singularity after inflation is argued to be classically avoided once radiation and cold dark matter are included.
- **In plain words**: The paper studies a model of the very early universe in which a rapid expansion (inflation) is driven by a field whose energy depends on its motion in an unusual way, called k-essence. Earlier versions of such models needed approximations built into the equations; here the authors find solutions that can be written in closed form as functions of cosmic time. They report that the model fits the observational limits on inflation, but that its expansion develops a mathematical pressure singularity a few e-foldings after inflation ends. Using numerical arguments, they claim this singularity is avoided once ordinary matter (radiation and cold dark matter) is included.
- **Why it matters**: Analytic solutions are useful because they let researchers check predictions and stability without relying on numerical simulation or the slow-roll shortcut. The reported singularity and its possible resolution by ordinary matter are the points that a reader would need to weigh, since the claim rests on numerical arguments given in the text. Its connection to observations is limited to the statement that the inflation indices depend only on n and m.
- **Background needed**: - Inflation: a brief period of very rapid, accelerating expansion of the early universe, thought to seed the large-scale structure we observe.
- Scalar field: a hypothetical field whose value varies in space and time; inflation is often modeled with one.
- k-essence: a generalization in which the field's energy depends on a kinetic term X (roughly, how fast the field changes) in a non-standard, nonlinear way.
- Slow-roll assumption: the common approximation that the field changes slowly, used to simplify inflation equations.
- Hubble rate: the expansion rate of the universe; e-folding: a factor of e (about 2.7) growth in the scale factor.
- Sound speed of perturbations: the speed at which small density ripples propagate; if it is wrong, instabilities can arise.
- Pressure singularity: a point where pressure blows up in the model's equations, a sign the model breaks down there. · level: research-level

<details><summary>Original abstract</summary>

In this work we develop a fully analytic $k$-essence inflation solution which is compatible with the observational constraints on inflation, without the need for the slow-roll assumption being imposed dynamically in the field equations. The analytic solution is obtained for a kinetic scalar sector of the form $K(X)= \frac{X^n}{X_s^{n-1}}$ and for the scalar field satisfying a tracking condition $\dot{\phi}^2=\gamma H^{-m}$. For this class of theories, the sound speed of the primordial curvature perturbations is constant, so no gradient instabilities occur in the theory. The Hubble rate, the scale factor and the scalar field can be analytically expressed as functions of the cosmic time, and the observational indices of inflation depend solely on the parameters $n$ and $m$. The resulting evolution is inflationary and it develops a pressure singularity a few $e$-foldings after the end of inflation. However, using qualitative and quantitative numerical arguments, we show that the pressure singularity is classically avoided when the matter fluids of radiation and cold dark matter are taken into account.

</details>

## Galaxies

### [The Sensitivity of Gamma-Ray Searches for Dark Matter Annihilation in Milky Way Dwarf Galaxies: the LSST Era and Beyond](https://arxiv.org/abs/2611.31130)
*Ilumi Chavez, Aditya Ghosh, Chris Kelso et al.* · `astro-ph.HE` · arXiv:2611.31130v1 · relevance 0.19

- **In one sentence**: A forecast of how well gamma-ray telescopes (Fermi-LAT and the proposed APT) can constrain dark matter annihilation using Milky Way dwarf satellite galaxies, including the effect of the many satellites expected from LSST, via the BabyBison Monte Carlo pipeline.
- **In plain words**: Dark matter is thought to make up most of the mass in galaxies but cannot be seen directly. This paper asks how well gamma-ray telescopes could detect signs of dark matter particles destroying each other inside the small galaxies orbiting the Milky Way, and how much new galaxies found by the upcoming LSST survey would help. The authors' main finding is that the new discoveries would give only modest improvements, typically below 20%, while rare cases with undiscovered, very dense satellites could give much larger gains.
- **Why it matters**: Dwarf galaxies are among the cleanest places to search for dark matter annihilation signals, so knowing what future surveys can and cannot deliver helps plan observations. The finding that a few high-density satellites dominate the results, rather than the total count, is a useful point for planning, though the text alone does not show how robust it is to modeling assumptions.
- **Background needed**: - Dark matter: unseen matter whose gravity holds galaxies together; some models say pairs of its particles can annihilate and emit gamma rays.
- Dwarf galaxies: small, faint galaxies orbiting the Milky Way, which contain a lot of dark matter and little else that emits gamma rays, making them good targets.
- J-factor: a measure of how much dark matter lies along the line of sight toward a galaxy; a high J-factor means a brighter expected signal.
- LSST: the Vera C. Rubin Observatory's Legacy Survey of Space and Time, a large sky survey expected to find many new faint satellites.
- Fermi-LAT: NASA's space gamma-ray telescope now in operation; APT is a proposed future instrument.
- Monte Carlo pipeline: a computer method that runs many random simulated realizations to estimate the spread of possible outcomes. · level: research-level

<details><summary>Original abstract</summary>

We forecast the sensitivity of gamma-ray searches to dark matter annihilation in Milky Way satellite dwarf galaxies using BabyBison, a Monte Carlo pipeline combining cosmological satellite simulations and observational selection functions with a joint likelihood analysis of gamma-ray data. Although LSST is expected to substantially expand the catalog of known satellite galaxies, we find that these discoveries are likely to produce only modest improvements in the resulting dark matter annihilation constraints, typically below 20\%. Much more substantial gains are possible, however, in relatively rare realizations that contain yet-to-be-discovered satellites with large $J$-factors. These results reinforce the fact that indirect detection analyses using the population of dwarf galaxies are typically driven in large part by a small number of high-$J$-factor systems rather than by the total satellite count. We present projections for the sensitivity of Fermi-LAT and the proposed Advanced Particle-astrophysics Telescope (APT) to dark matter annihilation, finding that a complete census of the Milky Way dwarf sample could enable such instruments to probe dark matter with masses up to the TeV scale. We also investigate the dark matter discovery potential of these instruments and project their ability to measure the properties of an annihilating dark matter particle.

</details>

### [Multiphase Gas in the Ram-Pressure-Stripped Elliptical Galaxy NGC 1404](https://arxiv.org/abs/2611.29706)
*Ryan Eskenasy, Yuanyuan Su, Qinnan Zhu et al.* · `astro-ph.GA` · arXiv:2611.29706v1 · relevance 0.15

- **In one sentence**: Multi-instrument study (MUSE optical, Chandra and XMM-Newton X-ray) of gas motions in the hot and warm phases of the ram-pressure-stripped elliptical galaxy NGC 1404 falling through the Fornax Cluster, finding a Mach number of about 0.48 and warm-gas velocity structure consistent with Kolmogorov turbulence.
- **In plain words**: This paper looks at NGC 1404, an elliptical galaxy moving through the hot gas filling the Fornax Cluster. The wind of that gas pushes on the galaxy's own gas, a process called ram pressure stripping. The authors combined optical and X-ray observations to measure how fast and how turbulently the gas moves, in both its hot and warm forms.
- **Why it matters**: It gives a measured case of how an outside environment can stir up a galaxy's gas and may help explain how cooling produces off-center warm gas. The text reports these measurements for one galaxy, so it is unclear how far the result applies to other galaxies or clusters.
- **Background needed**: - Elliptical galaxy: a smooth, mostly old star population with little new star formation.
- Fornax Cluster: a nearby group of galaxies that holds a large volume of hot X-ray gas.
- Ram pressure stripping: gas is pushed out of a galaxy as it moves through surrounding gas, like rain blown off a moving car.
- Intracluster medium: the hot, thin gas between galaxies in a cluster.
- Warm ionized gas: gas heated to about ten thousand degrees, seen through its glow of hydrogen-alpha light.
- Mach number: the ratio of turbulent speed to the speed of sound in the gas; about 0.5 means turbulence is moderate.
- Kolmogorov turbulence: a standard statistical pattern for how energy cascades across scales in a turbulent fluid.
- Velocity structure function: a measure of how much gas velocity differs between points separated by a given distance.
- Power spectrum: a way of splitting brightness or velocity variations into their different sized components.
- Resonant scattering and line broadening: X-ray spectral effects used to infer gas motion. · level: research-level

<details><summary>Original abstract</summary>

Galaxy groups and low-mass galaxy clusters are major sites of environment-driven galaxy evolution. NGC 1404 is an X-ray-bright early-type galaxy traveling through the intracluster medium of the nearby low-mass Fornax Cluster, and it hosts off-center warm ionized gas. With minimal ongoing stellar feedback and negligible active galactic nucleus feedback, NGC 1404 provides an ideal laboratory for constraining the impact of environmental processes on the thermodynamics of the interstellar medium. We analyzed VLT/MUSE, 506 ks Chandra ACIS, and 119 ks XMM-Newton RGS observations to quantify gas motions in both the hot and warm phases of NGC 1404. We probed the kinematics of the warm gas by deriving the velocity structure function (VSF) from MUSE H$\alpha$ integral-field spectroscopy. To measure the kinematics of the hot gas, we derived the power spectrum of X-ray surface brightness fluctuations from the Chandra data, and independently constrained galaxy-scale hot gas motions by measuring Fe XVII resonant scattering and turbulent line broadening with RGS. Our RGS spectral analysis gives a three-dimensional Mach number of $0.48^{+0.22}_{-0.14}$, consistent with the power-spectrum results from Chandra for the same extraction region, and corresponding to a turbulent-to-thermal energy density ratio of $\sim0.13$. The warm-gas VSF follows the expectation for Kolmogorov turbulence and is broadly consistent with the hot-gas kinematics. The off-center warm gas in NGC 1404 may have formed through radiative cooling of the hot interstellar medium, triggered by the uplift of low-entropy hot gas during ram pressure stripping. Our study suggests that ram pressure stripping can drive substantial gas motions and reshape the thermodynamic state of the interstellar medium of cluster member galaxies.

</details>

## Exoplanets and planetary science

### [Shifting the snow line in protoplanetary disks by planet-induced multiple spiral shocks](https://arxiv.org/abs/2611.30158)
*Shizu Shimizu, Ryosuke T. Tominaga, Satoshi Okuzumi et al.* · `astro-ph.EP` · arXiv:2611.30158v1 · relevance 0.12

- **In one sentence**: Two-dimensional hydrodynamical simulations and a thermal-balance model show that spiral shocks driven by a giant planet can heat the inner disk enough to move the snow line (the radius where water ice forms) beyond 1 au, for a planet of about one-third Jupiter's mass at 5 au and an assumed opacity of 1 cm²/g.
- **In plain words**: Young planets form in thin disks of gas and dust around newborn stars. The "snow line" is the distance from the star inside which water is too warm to freeze, and where it sits affects whether rocky planets like Earth can form and keep their water. This paper asks whether shock waves in the disk, created by a growing giant planet's spiral arms, can heat the inner disk enough to push that line outward. The authors find that they can, when the planet is massive enough and the disk is dense enough to trap heat.
- **Why it matters**: Recent simulations had suggested the snow line might sit inside 1 au, which would make it hard to build Earth-like planets in place. If shock heating from a giant planet keeps the snow line farther out, it offers a physical route to forming rocky planets with water without special water-removal steps; the text suggests this may apply to the early formation of Jupiter in our solar system, though this is a model-based result.
- **Background needed**: - Snow line: the distance from a star where water vapor condenses into ice; it marks where icy solids become abundant.
- Protoplanetary disk: the rotating disk of gas and dust around a young star from which planets form.
- Accretion heating (Joule heating): warming of gas as it falls inward; recent magnetized simulations found this is weak, so the snow line may lie inside 1 au.
- Spiral shock: a shock wave in the gas, launched by a planet's gravity, that heats gas as it passes.
- Optical depth and opacity: how well the disk traps heat; higher opacity means heat escapes less easily.
- Hydrodynamical simulation: a computer model of gas flow that ignores magnetic fields.
- Entropy jump: a measure of how much a shock irreversibly heats gas.
- Jupiter-mass units: the planet here is about one-third of Jupiter's current mass. · level: research-level

<details><summary>Original abstract</summary>

The snow line location provides important constraints on rocky planet formation. Recent magnetohydrodynamical simulations suggest that Joule heating associated with gas accretion is so inefficient that the snow line can be located inside 1 au around a solar-type star. This challenges in-situ formation of the terrestrial planets in the solar system unless other internal heating processes are present. Previous studies have proposed that spiral shocks induced by an embedded planet potentially shift the snow line outward. In this study, we investigate the impact of shock heating induced by a giant planet on the location of the snow line in two steps. First, we perform two-dimensional hydrodynamical simulations of a disk with a giant planet to model shock heating rates. We construct an empirical formula for total entropy jumps due to multiple spiral shocks interior to the planetary orbit. Second, we calculate the radial temperature profile based on the thermal balance with the modeled shock heating rates. We find that shock heating can substantially increase the disk temperature in inner regions far from the planet when the planetary mass and disk optical depth are sufficiently high. For example, assuming a fixed surface density profile and an opacity of $\kappa = 1~\rm cm^2\,g^{-1}$, a planet with one-third of Jupiter's current mass at 5 au can shift the snow line outward beyond 1 au. Our results suggest that the early formation of proto-Jupiter in the solar nebula may have enabled rocky planetesimals and protoplanets to form in the present-day terrestrial planet region without invoking additional water removal processes.

</details>

### [Constraining Planet Nine with Pulsar Timing: Orbit Determination Method from the Acceleration, Jerk, and Snap of the Solar System Barycenter](https://arxiv.org/abs/2611.28471)
*Jackson D. Taylor, Emmanuel Fonseca, Joseph Glaser* · `astro-ph.EP` · arXiv:2611.28471v1 · relevance 0.10

- **In one sentence**: A method for using timing variations of millisecond pulsars to constrain the mass and orbit of a hypothesized distant Planet Nine via the acceleration, jerk, and snap of the solar system barycenter, with a check against Uranus and Neptune.
- **In plain words**: The paper asks whether a possible large, unseen planet beyond Neptune, called Planet Nine, could be detected by how it tugs the solar system's center of mass. The idea is to watch very regular radio pulses from spinning neutron stars (millisecond pulsars) and look for tiny, systematic shifts in their arrival times. The authors show which kinds of timing changes are needed to pin down the planet's orbit, and they test the method by estimating the masses of Uranus and Neptune.
- **Why it matters**: Planet Nine is proposed to explain why several distant small icy bodies cluster in their orbits, but it has not been observed, so a independent detection route would be valuable. The text says the method could be used after an optical detection to weigh such a planet, but it does not show that pulsar data are currently precise enough to find one.
- **Background needed**: - Planet Nine: a hypothesized planet far beyond Neptune, proposed to explain clustered orbits of distant trans-Neptunian objects.
- Solar system barycenter: the center of mass of the Sun and planets; it wobbles as planets orbit.
- Millisecond pulsar: a rapidly spinning neutron star whose radio pulses arrive with extremely steady timing.
- Pulse times of arrival and timing residuals: measured differences between when pulses are expected and when they actually arrive.
- Acceleration, jerk, snap: the first, second, and third time-derivatives of position (rate of change of acceleration and higher orders), which appear as progressively finer timing signatures.
- Orbit determination: inferring an object's orbit and mass from its gravitational effects. · level: research-level

<details><summary>Original abstract</summary>

Planet Nine is hypothesized to exist in the outer solar system in order to explain the physical orbital clustering of several trans-Neptunian objects. A Planet Nine would systematically change the location of the solar system barycenter (SSB). Therefore, the precise timing properties of millisecond radio pulsars would measure the acceleration, jerk, and snap of the currently-perceived SSB under the gravitational influence of a Planet Nine. We present a method on how to use pulsar spin frequency derivatives and binary pulsar orbital period derivatives to constrain the Planet Nine parameter space. We find that searches for unidentified massive objects in the solar system require at least cubic and quartic variations in the pulse times of arrival (corresponding to jerk and snap, respectively) in order to uniquely constrain an orbit. Otherwise, additional assumptions are required to fully constrain the mass and orbital parameters of the object. We use our method to weigh the ice giants Uranus and Neptune and obtain results consistent with the literature. This method could be used to weigh a Planet Nine after a putative optical detection. Future work will use updated pulsar timing datasets that benefit from longer observational baselines and advances in statistical modeling and noise characterization.

</details>

## High-energy astrophysics

### [Enhancing eccentricity through tidal resonance in binary neutron star systems](https://arxiv.org/abs/2611.31172)
*Ivan Markin, Natalie Williams, Tim Dietrich* · `gr-qc` · arXiv:2611.31172v1 · relevance 0.21

- **In one sentence**: Numerical-relativity simulations show that a highly spinning, retrograde neutron star can resonate with its own f-mode during the late inspiral of a binary neutron star, pumping eccentricity into an otherwise quasicircular orbit and transferring spin from the orbit to the star, with a simple resonance-locking model reproducing the spin change.
- **In plain words**: Two neutron stars, the dense collapsed cores of once-massive stars, can spiral toward each other and merge. Usually their orbits become almost perfectly circular before they merge, so a noticeably oval orbit is a hint that they formed in a crowded star cluster. This paper uses supercomputer simulations of Einstein's gravity to show that a rapidly spinning star can make its orbit oval on its own, through a resonance in how its body vibrates under the other star's pull.
- **Why it matters**: Measured orbital eccentricity is proposed as a clue to how a merging pair formed, so a non-formation-based source of eccentricity could complicate that inference. The text reports a specific mechanism and a simple model for it, but it is a simulation study of one configuration (two highly spinning stars, one prograde and one retrograde), so how common or large the effect is in real systems is not established here.
- **Background needed**: - Binary neutron star: two neutron stars orbiting each other; their merger emits gravitational waves that detectors can measure.
- Orbital eccentricity: how far an orbit departs from a perfect circle; circular is zero.
- Quasicircular inspiral: the slow spiral-in phase when the orbit is nearly circular.
- Numerical relativity: computer simulations solving Einstein's equations for strong gravity.
- f-mode (fundamental mode): a natural vibration pattern of a star's body; resonance occurs when an outside driving frequency matches it.
- Spin-orbit angular momentum transfer: the star's spin and the orbit exchange spin angular momentum, so a change in one changes the other.
- Prograde vs retrograde spin: spinning in the same direction as the orbit vs the opposite direction. · level: research-level

<details><summary>Original abstract</summary>

Orbital eccentricity of binary neutron star systems is a key parameter to reveal their formation history. Since binaries formed in isolation are expected to circularize long before merger, measurable eccentricity suggests dynamical formation in dense stellar environments. However, using numerical-relativity simulations, we show that eccentricity can be introduced in the late inspiral of an initially quasicircular binary, due to the $f$-mode resonance of one of the stars. We simulate the merger of two highly spinning neutron stars, one star spinning prograde and the other retrograde. Persistent tidal resonance with the $f$ mode of the retrograde-spinning star is observed, accompanied by a gradual change of its spin due to angular momentum transfer from the orbit. This spin change can be well explained by a simple resonance locking model that accounts for the spin-dependent shift of the $f$-mode frequency. These findings reveal an origin of eccentricity in binary neutron stars that is independent of their formation history and provide important information for modeling binary neutron star dynamics with rapidly spinning stars.

</details>

### [Probabilistic foreground diagnostics from dispersion measure excess in individual fast radio bursts](https://arxiv.org/abs/2611.28068)
*Qi Zhou, Ran Gao, Zhengxiang Li et al.* · `astro-ph.HE` · arXiv:2611.28068v1 · relevance 0.18

- **In one sentence**: A source-level Bayesian framework treats each fast radio burst's host-galaxy dispersion measure as a latent variable drawn from a shared lognormal population, fit by EM to 92 localized FRBs, to estimate the probability that each sightline retains a positive excess cosmological DM.
- **In plain words**: Fast radio bursts are brief flashes of radio waves from distant sources, and their signals are delayed by the electrons they pass through on the way to us. Part of that delay comes from the burst's own host galaxy, which is hard to measure directly, so the extra electrons along the line of sight are uncertain. This paper treats the host contribution as an unknown drawn from a shared population, and estimates for each of 92 localized bursts how likely it is that some electrons remain after subtracting that host share.
- **Why it matters**: The probability of a leftover excess gives a way to rank which bursts are worth follow-up searches for intervening galaxies, groups, clusters or large-scale structure. The paper reports that bursts previously linked to foreground material tend to score high, which supports the idea, though the 18 new candidates still need observational checks that the text does not describe.
- **Background needed**: - Dispersion measure (DM): how much a radio pulse is delayed by free electrons along its path; larger values mean more electrons.
- The total DM is a sum of parts: the Milky Way, the intergalactic medium (the cosmic baryon reservoir), the host galaxy, and any intervening galaxies or halos.
- Localized FRBs: bursts whose position on the sky has been pinned to a specific host galaxy, so host redshift is known.
- Lognormal distribution: a skewed distribution for positive quantities whose logarithm is normally distributed.
- Expectation–maximization (EM): an iterative statistical method for fitting models that include hidden (latent) variables.
- Marginalizing: averaging over an uncertain quantity instead of fixing it to one value.
- Foreground follow-up: deep imaging or spectroscopy of fields along a burst's sightline to look for intervening matter. · level: research-level

<details><summary>Original abstract</summary>

Fast radio bursts (FRBs) provide a unique probe of diffuse baryons through their dispersion measure (DM), but interpreting a large DM for an individual burst is limited by the uncertain contribution from its host galaxy, which is hard to directly observed. We address this gap with a source-level diagnostic framework that treats $\mathrm{DM_{host}}$ as a latent variable drawn from a shared lognormal population, thereby marginalizing over the uncertain host contribution. Applying an expectation--maximization (EM) inference scheme to 92 localized FRBs, we jointly estimate the host-DM population and obtain a model-conditioned host-DM distribution for each burst. We propagate these distributions into an excess cosmological DM for each sightline, quantifying both its uncertainty and the probability that a positive excess remains after accounting for the host contribution. FRBs previously reported to show evidence for foreground or intervening contributions preferentially exhibit high probabilities of retaining such an excess, indicating that this source-level probability can provide a useful statistic for prioritizing foreground follow-up observations. Using this diagnostic, we identify 18 additional localized FRBs as high-priority candidates for follow-up searches for possible intervening galaxies, groups, clusters, or large-scale structure.

</details>

## Stars and the Sun

### [Identifying Distant and Highly Reddened Star Clusters: 486 Open Clusters and Candidates in the Dusty Galactic Disk](https://arxiv.org/abs/2611.29181)
*Zhihong He, Xiaoping Wang, Qian Cui et al.* · `astro-ph.GA` · arXiv:2611.29181v1 · relevance 0.17

- **In one sentence**: Using Gaia DR3 astrometry with 2MASS near-infrared photometry and a Bayesian membership scheme, the authors report 486 clusters and candidates in the dust-obscured Galactic disk, 450 of them without a literature counterpart.
- **In plain words**: Star clusters are groups of stars born together and moving together through the Milky Way. Many distant clusters are hidden behind interstellar dust, which blocks visible light, so astronomers have found fewer of them. This paper searches for such groups by combining a European space telescope's motion and brightness catalogue with infrared measurements, which see through dust better.
- **Why it matters**: The sample adds hundreds of mostly distant, heavily dust-covered clusters to a region that has been poorly mapped, and the authors suggest it may serve as a baseline for the next Gaia data release. The text also reports that the new objects show the north-south tilt of the Galactic warp, though the strength of that link is for readers to judge from the full paper.
- **Background needed**: - Open cluster: a loose group of stars formed together, typically a few hundred to a few thousand stars.
- Gaia: an ESA satellite that measures positions, motions (proper motion) and distances (parallax) of over a billion stars.
- 2MASS: an earlier near-infrared sky survey; infrared light passes through dust more easily than visible light.
- Extinction (Av): how much starlight is dimmed by dust, measured in magnitudes; Av of 5 means roughly 100 times fainter in visible light.
- Kiloparsec (kpc): about 3,260 light-years; 6.9 kpc is roughly 22,000 light-years away.
- Galactic warp: a bending of the Milky Way's outer disk, with one side tilted up and the other down.
- DBSCAN: a standard computer algorithm that groups nearby points in data. · level: research-level

<details><summary>Original abstract</summary>

The Gaia mission has transformed the census of Galactic star clusters. Most discoveries were based on Gaia DR2 and EDR3, and the rate of new large cluster catalogues has declined since 2023. The distant and dusty part of the disk is still poorly sampled because optical data are strongly affected by extinction. We search for star clusters in the Galactic disk using Gaia DR3 astrometry and photometry, together with 2MASS near-infrared photometry. We scan trial cluster centers in Galactic position, proper motion, and parallax space, assign a Bayesian membership probability to each star, construct a relative density map, and use DBSCAN solely to separate neighboring peaks. We identify 486 clusters and candidates with astrometric quality comparable to that of previously reported clusters. Of these, 450 have no literature counterpart, while 36 are known clusters that were not recovered in earlier Gaia cluster searches. The median distance is 6.9 kpc, and 39% of the objects lie beyond 8 kpc. The median extinction is Av = 5.10 mag, and 16% of the objects have Av > 8mag. The new objects fill a sparsely sampled region of the distance--extinction plane. Their distribution reveals the north--south displacement of the Galactic warp, and high-latitude objects are on average farther, older, and less extincted. Gaia DR3 still offers room for distant, dust-obscured clusters, and this sample provides a baseline for Gaia DR4. All cluster parameters, member star information, spatial distribution maps, and color-magnitude diagrams can be downloaded from https://zenodo.org/records/24431850.

</details>

### [Multiplicity of Normal A-Type Field Stars of Low Projected Rotational Velocity](https://arxiv.org/abs/2611.28343)
*Daryl W. Willmarth, Francis C. Fekel, Helmut A. Abt* · `astro-ph.SR` · arXiv:2611.28343v1 · relevance 0.10

- **In one sentence**: A 30-year radial-velocity survey of 119 slowly rotating, non-peculiar A-type dwarf and subgiant stars finds a multiplicity fraction of 0.64 and argues that tidal braking in short-period binaries is unlikely to explain their slow spins.
- **In plain words**: Astronomers wanted to know how many of the moderately hot, ordinary "A-type" stars that spin slowly have companion stars. Over more than 30 years they tracked the back-and-forth motion of 119 such stars toward and away from us, which reveals hidden partners. They worked out the orbits for 43 of them and, adding other known companions, found that about 64% of these stars have at least one companion.
- **Why it matters**: The result bears on why some stars spin slowly while most fast spinners look normal, a question that connects star formation and binary evolution. The authors report that only 6 of the 80 companion-bearing stars have orbits shorter than 10 days, so tides are probably not the main reason for their slow spin; the text does not establish a single cause.
- **Background needed**: - A-type stars: hot, white-ish stars somewhat more massive than the Sun.
- Projected rotational velocity (vsini): how fast a star spins, measured only along our line of sight, so it is a lower limit.
- Radial velocity: the star's speed toward or away from us, measured from Doppler shifts in its light; periodic changes reveal an unseen companion.
- Orbital elements: numbers describing a companion's orbit (period, size, shape, orientation).
- Multiplicity fraction: the share of stars that have one or more companions.
- Tidal interaction: gravitational pull between close companions that can slow a star's spin, mainly when the orbit is tight.
- Main sequence: the long stable core-hydrogen-burning phase of a star's life.
- Peculiar spectra: unusual chemical patterns in a star's light. · level: research-level

<details><summary>Original abstract</summary>

While nearly all rapidly rotating (vsini > 120 km/s) A stars are observed to have normal spectra, a significant fraction (~43%) of slow rotators have peculiar spectra although many do not. For over 30 years, we conducted a radial velocity survey of 119 non-peculiar, slowly rotating dwarf or subgiant A stars. We determined orbital elements and related parameters for 43 systems and along with known visual binaries, common proper motion companions and stars with proper motion anomalies, find a multiplicity fraction of 0.64. We compared our results to recent findings concerning similar stars. We also examined whether the slow rotation of our sample of could have been caused by tidal interactions in short-period binaries. Of the 80 stars that we determined to be at least binary in nature or to show other evidence of having companions, only 6 have periods < 10 days. Thus, a large majority have periods that are much too long for tidal forces to have reduced their rotation rates while they are on the main-sequence. We also observed a small sample of rapid rotators (vsini = 125-230 km/s) over a shorter time interval to judge the accuracy of our measuring techniques on A stars with very broad lines. Orbital elements for 5 non-survey A-type stars, also with low vsini, are listed with our results, but are not included in the statistical discussion.

</details>

## Chemical physics

### [Nonempirical Determination of the Optimal TAO-DFT Fictitious Temperature for Molecular Systems in the Lowest Singlet State](https://arxiv.org/abs/2611.29414)
*Bing-Ying Li, Jeng-Da Chai* · `physics.chem-ph` · arXiv:2611.29414v1 · relevance 0.15

- **In one sentence**: The paper proposes a nonempirical, system-dependent way to choose the fictitious temperature in TAO-DFT, based on restoring spin symmetry, for molecules in their lowest singlet state.
- **In plain words**: Computer models of molecules often struggle when electrons are strongly tangled up, as happens when chemical bonds are stretched or broken. This paper tunes a built-in "fictitious temperature" in a particular method (TAO-DFT) so that it is chosen for each molecule rather than fixed in advance. The authors report that this per-molecule choice works better overall than a single fixed setting on the test cases they chose.
- **Why it matters**: Better handling of strongly tangled electrons matters for predicting how molecules break apart and react, which underlies chemistry and materials design. The text reports benchmarks only on a small set of diatomic molecules and one twisted ethylene case, so its wider usefulness is not yet shown.
- **Background needed**: - Density functional theory (DFT): a common computer method for estimating molecular electron distributions and energies, usually cheap but not always accurate.
- Single-reference vs. multi-reference systems: some molecules are well described by one simple electron arrangement; others need a mix of several, which standard DFT handles poorly.
- Static correlation: the electron effect that appears when several arrangements have similar energy, typical of bond breaking.
- Fictitious temperature (TAO-DFT): a mathematical smearing parameter that lets electrons occupy several orbitals partially; higher values capture more multi-reference character but can overcorrect simple molecules.
- Spin-symmetry restoration: enforcing the correct spin pattern of electrons as a physical consistency check used here to pick the temperature.
- Singlet state: a molecular state in which all electron spins are paired. · level: research-level

<details><summary>Original abstract</summary>

Thermally-assisted-occupation density functional theory (TAO-DFT) [J.-D. Chai, J. Chem. Phys., 2012, ${\bf 136}$, 154104] has been developed to investigate the ground-state properties of large electronic systems exhibiting varying multi-reference (MR) character. As a central parameter in TAO-DFT, the fictitious temperature $\theta$ is closely linked to the degree of static correlation in an electronic system. While the conventional system-independent $\theta$-scheme is computationally efficient and broadly applicable, a fixed, preassigned $\theta$ can be overly large for single-reference (SR) systems yet too small for strongly MR systems. To overcome this limitation, we propose a nonempirical scheme based on spin-symmetry restoration to determine the optimal system-dependent fictitious temperature $\theta^{*}$ for molecular systems in their lowest singlet states. Across benchmark tests encompassing both MR systems (the bond dissociation of H$_{2}$, N$_{2}$, Li$_{2}$, and LiH, as well as the torsional rotation of twisted ethylene) and pure SR systems (the dissociation of He$_{2}$ and Ne$_{2}$), our nonempirical approach demonstrates superior overall accuracy compared with the conventional fixed-$\theta$ scheme. Furthermore, relative to standard Kohn-Sham density functional theory (TAO-DFT with $\theta = 0$), TAO-DFT employing $\theta^{*}$ yields substantial improvements for MR systems while preserving comparable accuracy in SR systems.

</details>

### [Autonomous Multireference Quantum Chemistry with Artificial Intelligence Agents](https://arxiv.org/abs/2611.29902)
*Younghwan Kim, Ming-Hsiu Hsieh, Ankit Mathanker et al.* · `physics.chem-ph` · arXiv:2611.29902v1 · relevance 0.15

- **In one sentence**: CASPER is an AI-agent workflow that automates the choice of active orbital spaces for multireference quantum chemistry calculations along transition-metal reaction pathways, with independent assessment checks.
- **In plain words**: Computer simulations of chemical reactions can go wrong when electrons are tangled together, as happens when bonds are breaking and forming, especially with metal atoms. Getting these simulations right normally takes expert judgment about which electrons and orbitals to include. The authors built an AI-agent workflow, called CASPER, that makes these choices itself, checks its own results, and tracks the same setup along a reaction path.
- **Why it matters**: Reliable calculations of hard reaction chemistry are slow and expert-dependent, so automating them could help generate high-quality data at scale. The paper's main evidence is a demonstration on five transition-metal reactions, and it reports that in two cases CASPER caught problems that a separate, unstructured Claude session missed; the broader claim about future value is the authors' outlook rather than something the text establishes.
- **Background needed**: - Electronic structure: the quantum-mechanical description of electrons in molecules, used to predict energies and reaction paths.
- Strongly correlated electrons: electrons whose behavior cannot be captured by a single simple picture, common in bond breaking and transition-metal chemistry.
- Multireference methods: calculations that combine several electronic configurations; they need a chosen "active space" of orbitals and electrons.
- Active space: the subset of orbitals and electrons treated in detail; choosing it well is the hard, expert-driven step.
- Potential energy profile: how a molecule's energy changes as a reaction proceeds, used to find barriers and intermediates.
- Electronic-state crossing: where two electronic states swap in energy, which can change the reaction pathway.
- AI agent / language model workflow: a system where a large language model plans and runs calculations in steps, with checks at each stage. · level: research-level

<details><summary>Original abstract</summary>

Accurately describing chemical reactions that involve strongly correlated electrons remains a major challenge in computational chemistry. Multireference electronic structure methods can address this challenge, but their application requires expert decisions that are di!cult to automate, particularly when the electronic structure changes as chemical bonds form and break. Here we introduce CASPER, an autonomously agentic workflow that performs multireference calculations along chemical reaction pathways. CASPER combines chemical knowledge, electronic structure calculations, and iterative assessment to identify chemically meaningful active spaces and maintain their consistency as bonds form and break. We demonstrate its capabilities on five transition-metal reactions, for which CASPER generates consistent multireference potential energy profiles with minimal human intervention. Importantly, in two reactions, CASPER identifies critical electronic-structure problems that an independent Claude session fails to recognize without the structured workflow. These include an electronic-state crossing and the exclusion of an orbital involved in bond breaking. Our results show the importance of combining language models with chemical knowledge and independent assessment of computational results. Beyond automating calculations, such agents have the potential to help researchers better understand the underlying physics and chemistry and open new opportunities for investigating complex chemical reactivity and generating high-quality quantum chemical data at scale.

</details>

## Materials science

### [Unveiling the Complex high-pressure phases of Sodium at the Melting Curve Minimum via Data-Drive Crystal Structure Prediction](https://arxiv.org/abs/2611.29889)
*Zhenyu Wang, Chengqian Zhang, Xiaoyang Wang et al.* · `cond-mat.mtrl-sci` · arXiv:2611.29889v1 · relevance 0.18

- **In one sentence**: Combines CALYPSO structure prediction with concurrent-learning Deep Potential models to search for candidate crystal structures of high-pressure sodium phases near its melting-curve minimum, and compares their enthalpy, Gibbs free energy, and solid-liquid coexistence behavior.
- **In plain words**: Sodium, a simple metal, forms many complicated crystal arrangements under pressure, and several of these observed in experiments have never had their atomic layouts worked out. The authors used computer searches over more than 1.6 million candidate configurations, guided by machine-learned interaction models, to propose atomic arrangements for these phases. They report that one known structure is recovered, and that several candidate structures are energetically close to one another and to established sodium phases near the melting minimum.
- **Why it matters**: Sodium's unusually many high-pressure phases are a known puzzle, and the paper offers specific structural models that experimentalists could test against measured diffraction data. The text reports that the candidates are close in stability and that the ranking depends on model accuracy, so the conclusions are provisional rather than settled.
- **Background needed**: - Crystal structure: the repeating three-dimensional arrangement of atoms in a solid; phases are different such arrangements of the same material.
- Melting curve: the line on a pressure-temperature plot showing where a solid melts; its minimum is where melting temperature is lowest.
- Enthalpy and Gibbs free energy: energy-like measures used to judge which structure is most stable at given pressure and temperature (the lower, the more favored).
- Crystal structure prediction: computer searches that generate and rank possible atomic arrangements without prior experimental structure.
- Deep Potential models: machine-learned interatomic potentials that approximate quantum-mechanical forces much faster than direct calculation; concurrent learning means the training set is expanded iteratively during the search.
- First-principles calculations: energy calculations from quantum mechanics without fitted parameters.
- Solid-liquid coexistence simulations: simulations that find the temperature at which solid and liquid are in equilibrium.
- Labels such as tI50 or oC120 denote crystal lattice type (tetragonal, orthorhombic, etc.) and the number of atoms in the unit cell. · level: research-level

<details><summary>Original abstract</summary>

Sodium exhibits a remarkable concentration of complex crystalline phases near its melting-curve minimum, yet the atomic arrangements of several experimentally observed phases remain unresolved. Here, we combine CALYPSO crystal structure prediction with Deep Potential models developed through concurrent learning to explore this structural landscape. Searches over more than 1.6 million configurations recover the previously reported $I4/m$ structure of $tI50$ and identify candidate atomic arrangements for $oC120$ and $aP90$, together with three additional low-enthalpy structures, $tI52$, $oP72$, and $oP92$. The proposed candidates reproduce key features of the experimentally indexed cell geometries. First-principles enthalpy calculations, Gibbs free-energy comparisons, and solid--liquid coexistence simulations reveal close competition among these structures and established sodium phases. Near the calculated reference melting minimum, $tI50$ is favored over $cI16$ and $oP8$, whereas $oC120$ and $aP90$ remain closely competitive, with their relative stability sensitive to model accuracy. These results provide testable structural models for unresolved experimental phases and reveal multiple closely competing low-enthalpy configurations near sodium's melting minimum

</details>

### [Defect Engineering of the Water-Carbon Interface: Insights from First-Principles Calculations](https://arxiv.org/abs/2611.28201)
*Peikun Zhang, Hongbo Zhang, Ying Xu et al.* · `cond-mat.mtrl-sci` · arXiv:2611.28201v1 · relevance 0.14

- **In one sentence**: Using first-principles (quantum-mechanical, computer-based) calculations, this paper maps how topological, point, line, edge and doping defects in carbon materials change water-carbon interactions relevant to water splitting, evaporation-driven electricity, and catalysis.
- **In plain words**: Carbon materials that touch water are central to devices that turn evaporating water into electricity or split water to make hydrogen. Real carbon is full of small flaws, but how those flaws affect water has been poorly understood. The authors used computer simulations to test many kinds of flaws and reported how each one changes water splitting, charge transfer to evaporating water, and hydrogen formation.
- **Why it matters**: The text reports specific effects, such as edge defects lowering the water-dissociation energy barrier by up to 30 times and mono-vacancies boosting charge transfer by up to 12.4 times, which could guide the design of hydrovoltaic and catalytic devices. These are computed predictions from the abstract alone, so they still need experimental confirmation before any practical significance is clear.
- **Background needed**: - Solid-liquid interfaces: the boundary where a solid surface meets water, where chemical reactions happen.
- Hydrovoltaics: devices that generate electricity from water moving or evaporating across a material.
- First-principles calculations: simulations that compute material behavior directly from the laws of quantum physics, without fitted experimental inputs.
- Defects: imperfections in a material's atomic structure, such as missing atoms (vacancies), edges, or swapped-in foreign atoms (doping).
- Energy barrier: the energy hill a reaction must climb; lower barriers mean faster reactions.
- Gibbs free energy near zero for hydrogen evolution: a sign that a surface can bind and release hydrogen efficiently, which is favorable for making hydrogen.
- Dangling bonds: unpaired chemical bonds at a broken edge that tend to be chemically reactive.
- Charge transfer: movement of electrons between the material and water molecules, linked to electricity generation. · level: research-level

<details><summary>Original abstract</summary>

Interactions at solid-liquid interfaces are fundamental to hydrovoltaic and catalytic technologies. While carbon nanomaterials have been extensively studied, the role of abundant defects in amorphous carbon remains poorly understood. Here, using first-principles calculations, we systematically investigate how various defects (topological, point, line, edge, and doping defects) modulate water-carbon interactions. We find that armchair-edge defects with dangling bonds reduce the energy barrier for water dissociation by up to 30 times compared with pristine carbon, while di-vacancies exhibit a near-zero Gibbs free energy for hydrogen evolution, enabling potential hydrogen evolution reaction activity on a purely carbon-based interface. Moreover, mono-vacancy defects, characterized by reduced electronic localization, enhance charge transfer to evaporating water molecules by up to 12.4 times, a key factor in evaporation-induced electricity generation. Crucially, we demonstrate that coupling distinct defects produces synergistic effects that outperform individual defects, revealing a promising strategy for designing multifunctional interfaces. These insights establish a defect-engineering framework for the rational design of high-efficiency hydrovoltaic and catalytic devices.

</details>

## Soft matter and polymers

### [Growing Knot Embeddings into Spherical Graphs](https://arxiv.org/abs/2611.30245)
*Eren G\"ulmez, Joost de Graaf* · `cond-mat.soft` · arXiv:2611.30245v1 · relevance 0.10

- **In one sentence**: The paper introduces a growth-and-relaxation construction that turns a 3D knot embedding into a graph on the sphere, compares these growth graphs with standard Tait graphs for prime knots up to seven crossings, and tests whether they are knot invariants using non-minimal diagrams and connected sums.
- **In plain words**: The paper looks at knots, the tangled loops familiar from string, and asks whether a knot's shape can be captured as a network drawn on a sphere. The authors grow the knot outward and let the surface settle under interfacial energy, which is the same force that makes soap films and droplets smooth, and read a graph from the resulting regions. For simple prime knots with at most seven crossings, the resulting graphs generally differ from the standard Tait graphs, and the authors describe an empirical rule for building them.
- **Why it matters**: Knotted structures matter in soft matter and biology, where tangles can affect how polymers relax and organize, so a way to encode knot shape as a graph could be a useful tool. The text shows that these graphs are not knot invariants, and that some prime-factor features may survive in connected sums, but it leaves open whether they reveal anything invariant under isotopy (smooth deformation without cutting), so their long-term value is uncertain.
- **Background needed**: - Knot: a closed loop in 3D space that cannot be untangled without cutting it.
- Knot diagram: a 2D drawing of a knot showing where strands cross over or under each other.
- Crossings: the points where the drawing overlaps itself; the count is a rough measure of complexity.
- Prime knot: a knot that cannot be split into simpler knots joined together; a connected sum is the join of two knots.
- Tait graph: a standard graph built from a knot diagram's regions, used in knot theory.
- Knot invariant: a property that stays the same under any smooth deformation of the knot (isotopy).
- Interfacial energy: the surface-tension-like energy that drives soft materials such as films and droplets toward smooth shapes.
- Graph embedded on the sphere: a network of nodes and edges drawn on the surface of a ball without crossings. · level: research-level

<details><summary>Original abstract</summary>

Knotted structures occur throughout soft matter and biology, where topological constraints can shape relaxation and spatial organization. Here, we introduce a computational construction that maps a specific 3D knot embedding to a graph embedded on the sphere through growth and interfacial-energy relaxation. For standard 3D embeddings of prime knots with at most seven crossings, we obtain a family of growth-based graphs that generally differ from the corresponding Tait graphs. We further identify an empirical growth-graph reconstruction rule based on polygonal regions with alternating crossing structure in a knot diagram. Non-minimal diagrams demonstrate that these graphs are not knot invariants, while selected connected sums suggest that graph features associated with their prime factors can remain recognizable. Determining how these graphs transform under isotopy may reveal invariant features, which we leave for future study.

</details>

### [Geometry Reorganizes Nonequilibrium States that Gate Topological Switching in an Active Polymer](https://arxiv.org/abs/2611.29649)
*Shiqi Zhou* · `cond-mat.soft` · arXiv:2611.29649v1 · relevance 0.09

- **In one sentence**: In a confined, partially active polymer, the same unknotted starting configurations are shown to differ in their later chance of knotting, and a pore-radius change can reverse which starting states are more susceptible.
- **In plain words**: The paper studies when a long chain-like molecule that is pushed around and squeezed through a narrow opening will tie itself into a knot. Starting from configurations that all look unknotted, the authors find that some are more likely than others to knot later, and that changing the size of the opening can flip which group is more likely to knot.
- **Why it matters**: It suggests that a system's present mechanical arrangement, not only the outside conditions, can decide how it will later change, which matters for understanding rare transitions in driven systems. The text does not show how far this extends beyond this polymer model, so broader applications remain unclear.
- **Background needed**: - Polymer: a long chain of repeated units, here simulated on a computer.
- Knot (topological state): a tangle that cannot be undone by moving the chain without cutting it; "unknotted" means no such tangle yet.
- Confinement and pore: the chain is pushed through a narrow opening whose radius is a controllable parameter.
- Partially active polymer: some segments are driven by a self-propelled, out-of-equilibrium force, so the system is not in thermal equilibrium.
- Langevin noise: random thermal kicks used in simulations to model molecular jiggling.
- Replicas and branches: independent copies of the simulation, and new simulated runs launched from saved configurations to test their future.
- Classifier: a rule that predicts which starting states are more susceptible to knotting; here it was fixed on separate data before the test.
- Susceptibility ordering: which group is more likely to knot; "reversal" means the ranking flips. · level: research-level

<details><summary>Original abstract</summary>

Even under identical external conditions, a driven system can occupy distinct long-lived states with different susceptibilities to the same rare transition. We demonstrate this in a confined partially active polymer, where independent unknotted replicas occupy distinct mechanical states with different topological futures. Matched-control and event-resolved analyses reveal a susceptible reservoir and a short threading precursor. We test this state dependence prospectively by launching 2272 Langevin-noise branches from 71 preserved unknotted phase-space states using a classifier prespecified from independent data. Most strikingly, the same classifier strongly separates finite-time knotting at one pore radius, yet reverses its susceptibility ordering at a neighboring radius. Thus geometry does not merely shift an average knotting rate; it selects among long-lived nonequilibrium states and reorganizes the mapping between a pre-existing mechanical coordinate and future topological fate.

</details>

## AI for chemistry and materials

### [Electric polarizabilities with phaseless auxiliary-field quantum Monte Carlo](https://arxiv.org/abs/2611.29858)
*Leon Otis, Jo Kurian, James Shee* · `physics.chem-ph` · arXiv:2611.29858v1 · relevance 0.23

- **In one sentence**: The paper shows that electric (static) polarizability tensors can be computed with phaseless auxiliary-field quantum Monte Carlo using a correlated-sampling finite-difference scheme, with Hartree-Fock trial wave functions, for small molecules, polyacenes, ferrocene and stretched N2.
- **In plain words**: Quantum Monte Carlo is a family of computer methods that estimate how electrons in a molecule behave by sampling many random configurations. This paper asks whether such methods, which are good at predicting a molecule's energy, can also predict how strongly its electron cloud shifts when placed in an electric field. The authors report that they can, and they test the approach on small molecules, a series of polyacenes (chains of fused rings), and ferrocene, a metal-containing compound.
- **Why it matters**: Polarizability controls how molecules respond to light and electric fields, and it is useful for building training data for cheaper approximate models. The text claims the method scales to molecules with thousands of basis functions and stays reliable for a strongly correlated case (stretched N2), but it gives no comparison numbers here, so the accuracy relative to other methods cannot be judged from this text alone.
- **Background needed**: - Polarizability: how much a molecule's charge distribution distorts in an applied electric field; the static tensor is the second derivative of energy with respect to field strength.
- Quantum Monte Carlo: stochastic (random-sampling) methods for solving the electronic Schrödinger equation.
- Phaseless auxiliary-field QMC: a variant that avoids the sign problem by constraining the sampled walkers using a trial wave function.
- Trial wave function: an approximate guess of the electronic state that guides the sampling; here a simple Hartree-Fock state.
- Finite-difference: estimating a derivative by computing energies at slightly different field strengths; correlated sampling reuses random samples so the small differences are less noisy.
- Density functionals and semi-empirical methods: cheaper approximate quantum chemistry methods used as points of comparison. · level: research-level
- Matched keywords: molecule, molecular

<details><summary>Original abstract</summary>

While projector quantum Monte Carlo methods are known for producing accurate ground-state energies, the prediction of other properties that encode the electronic response to applied electric and magnetic fields has historically been challenging. In this work we demonstrate that the electric (static) polarizability tensor, which is formally a second-derivative of the energy with respect to electric fields, can be efficiently computed with phaseless auxiliary-field quantum Monte Carlo using a correlated sampling finite-difference strategy. With simple Hartree-Fock trial wave functions, we investigate a series of small molecules (some of which are difficult for approximate density functionals), polyacenes of increasing size, and ferrocene as a representative organometallic complex. The methodology is scalable to relatively large molecules involving thousands of basis functions, and with appropriate trial wave functions remains robust for strongly correlated electronic states, as we show for the stretched dinitrogen molecule. This work opens the door to the computation of a host of other second-order molecular properties with auxiliary-field quantum Monte Carlo, which will inform the ongoing search for optimal trial wave functions and extend benchmark-quality training data sets for the refinement of semi-empirical and machine learning models for quantum chemistry and molecular simulation.

</details>

### [De Novo Generation of Odorant Molecules with Targeted Olfactory Receptor Activation Patterns](https://arxiv.org/abs/2611.30509)
*Kexin Zhang, Manhao Guan* · `cs.LG` · arXiv:2611.30509v1 · relevance 0.19

- **In one sentence**: A reinforcement-learning framework that generates new candidate odorant molecules tuned to hit target activation patterns across a panel of 20 olfactory receptors, using a clustered binding matrix and a structured selectivity loss.
- **In plain words**: Smell works by a pattern: each odor molecule switches on a particular set of receptors in the nose, and the brain reads that combination as a scent. This paper proposes a computer method that designs new molecules aimed at a chosen receptor pattern, rather than screening existing ones. The authors report that it reaches high predicted selectivity on nine target patterns within 18,000 model evaluations, with the biggest gains on patterns that are uncommon among starting molecules.
- **Why it matters**: Designing molecules from a desired receptor response, instead of searching a fixed library, could matter for fragrance and flavor work and for studying how the nose encodes smell. The text does not show experimental validation, so the results are predictions from models, and their real-world odor relevance is unclear.
- **Background needed**: - Olfactory receptors (ORs): proteins in the nose that bind odor molecules; many receptors respond to each odor, and the overall pattern encodes the smell.
- Binding matrix: a table of predicted strengths of how each molecule binds each receptor.
- De novo generation: designing new molecules from scratch, rather than picking from a list.
- Reinforcement learning: training a generator by rewarding outputs that score well on a goal, here a predicted receptor pattern.
- Oracle calls: the number of times the scoring model is queried during the search; a measure of computational cost.
- Selectivity: how specifically a molecule activates the intended receptors and not others.
- Prior: the distribution of molecules the generator starts from before steering. · level: research-level
- Matched keywords: molecule, molecular

<details><summary>Original abstract</summary>

Odor perception arises from a combinatorial code in which each molecule activates a specific subset of olfactory receptors (ORs), and the resulting activation pattern determines the perceived smell. We present a framework for de novo generation of molecules predicted to match target multi-receptor activation profiles. We first construct a panoramic binding matrix over 20 ORs, then cluster it to discover representative activation patterns, and finally formulate a structured selectivity loss, combining pairwise ranking, distribution matching, and complexity constraints, to steer a molecular generator via reinforcement learning. Across nine target profiles of varying complexity, our method achieves high predicted selectivity within 18000 oracle calls and provides the largest gains on profiles that are rare under the prior, especially broad-spectrum and sparse-activator targets.

</details>

## Biochemistry

### [Synthesis of Cellulose Nanofiber Hydrogel Beads from Typha angustifolia for the Immobilization of Protease](https://www.biorxiv.org/content/10.64898/2026.11.18.767499v1)
*Ameh, B. E.; Egwim, E. C.; Ossamulu, F. i.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.18.767499 v1 · relevance 0.07

- **In one sentence**: Cellulose nanofibers extracted from the invasive aquatic plant Typha angustifolia were oxidized, blended with polyvinyl alcohol, and crosslinked into hydrogel beads that serve as a covalent support for immobilizing crude protease.
- **In plain words**: Typha angustifolia is an invasive water plant that causes trouble for wetlands and irrigation channels. This study turned its fibrous cellulose into small water-swollen gel beads, then attached a crude protease (a enzyme that breaks down proteins) to them. The enzyme on the beads kept more activity over time and worked across a somewhat wider range of temperature and pH than the free enzyme.</plain>
<parameter name="why">It offers one way to put an invasive plant to use while making enzyme catalysts easier to reuse, which matters for industrial processes. The text reports only laboratory measurements, so practical or industrial value is not yet shown.
- **Background needed**: - Cellulose: the structural fiber of plant cell walls; cellulose nanofibers are very thin strands of it.
- Hydrogel: a water-filled, soft, net-like material; here the beads absorb about four times their weight in water.
- Immobilization: fixing an enzyme onto a solid support so it stays in place and can be reused.
- Protease: an enzyme that cuts proteins into smaller pieces.
- Covalent binding: attaching the enzyme by strong chemical bonds rather than loose contact.
- Specific activity: enzyme activity per milligram of protein; higher means more active.
- Half-life: how long the enzyme keeps half its activity under operating conditions.
- Glutaraldehyde and sodium periodate: chemicals used to crosslink and to introduce reactive groups. · level: intermediate

<details><summary>Original abstract</summary>

Typha angustifolia, an invasive aquatic macrophyte, poses a persistent challenge to wetland and irrigation management, yet its cellulose-rich biomass represents an underexploited feedstock for value-added biomaterials. This study reports the synthesis of cellulose nanofiber (CNF) hydrogel beads from T. angustifolia and evaluates their performance as a support matrix for protease immobilization. Cellulose was isolated by chlorite delignification and alkaline treatment, oxidized with sodium periodate to introduce aldehyde functional groups, blended with polyvinyl alcohol (PVA), and crosslinked with glutaraldehyde to form hydrogel beads. The beads exhibited a high water-absorption capacity of 399.67 {plus minus} 0.53% and a mechanical strength of 1.27 MPa. Covalent immobilization of crude protease onto the beads increased specific activity nearly threefold, from 24.56 {plus minus} 0.39 U/mg for the free enzyme to 59.20 {plus minus} 1.06 U/mg for the immobilized enzyme, corresponding to a loading efficiency of 50.61%. The immobilized enzyme also displayed broadened thermal and pH optima, shifting from 40 {degree sign}C to 50 {degree sign}C and from pH 8.0 to 9.0, respectively, and an extended operational half-life from 4.40 h to 11.37 h. These findings support the valorization of invasive Typha biomass into a robust, biodegradable support system with potential application in industrial biocatalysis.

</details>

### [AlphaFold-assisted design of a modular Laminin E8 Fragment Panel](https://www.biorxiv.org/content/10.64898/2026.11.20.768189v1)
*Litzau, L. A.; Kruse, A. C.; Blacklow, S. C.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.20.768189 v1 · relevance 0.06

- **In one sentence**: Using AlphaFold structure predictions, the authors optimize recombinant laminin E8 fragments and build a modular panel of interchangeable α, β and γ chains that can be combined to make all laminin isoforms, with the fragments shown to support adhesion of cells expressing their matching integrins.
- **In plain words**: Laminins are large protein assemblies that form part of the scaffolding around cells in tissues, but they are too big to make easily in the lab. This work uses an AI protein-structure tool, AlphaFold, to design smaller working pieces of laminin, called E8 fragments, that can be produced in cells in culture. The authors built a set of interchangeable pieces that can be mixed to form the different laminin versions, and reported that these pieces help cells stick to them when those cells carry the matching receptors.
- **Why it matters**: Having a readily made, mix-and-match set of laminin fragments could make it easier to study stem cells, organoids and the cell receptors (integrins) that grip laminin. The text does not report how widely these tools have been adopted or how they compare with existing laminin preparations, so their practical impact is still to be seen.
- **Background needed**: - Laminins: large three-chain proteins (α, β, γ) that form a major part of basement membranes, the thin sheets that support tissues.
- Recombinant: made in engineered cells rather than extracted from animal tissue.
- E8 fragment: a shortened, functional piece of laminin that keeps its cell-adhesion activity.
- Integrins: cell-surface receptors that attach cells to the extracellular matrix.
- AlphaFold: an AI tool that predicts the 3D shape of proteins from their sequence, used here to guide the design of fragments.
- Isoform: a variant of the same protein built from a different combination of chains. · level: research-level

<details><summary>Original abstract</summary>

Laminins are large, heterotrimeric glycoproteins that are a major structural component of basement membranes and the extracellular matrix. Although they are difficult to produce recombinantly because of their large size, a smaller fragment of the laminin heterotrimer that supports cell adhesion and cell migration, termed E8, can be recombinantly expressed. Here, we use AlphaFold to optimize laminin E8 fragments and design a panel of interchangeable laminin , {beta}, and {gamma} chains that can be combined to produce all isoforms recombinantly. These recombinant E8 fragments support adhesion of cells bearing their cognate integrins, and will be useful tools for stem-cell, organoid, and laminin-binding integrin biology research.

</details>

## Pharmacology and drug discovery

### [A scalable method for preparation and long-term preservation of tea leaf plant-derived vesicles in tissue regeneration and drug encapsulation](https://www.biorxiv.org/content/10.64898/2026.11.15.766803v1)
*Rodriguez de Lope, M. M.; Rivera-Tenorio, A.; Moreno-Luque, A. et al.* · `pharmacology and toxicology` · bioRxiv doi:10.64898/2026.11.15.766803 v1 · relevance 0.04

- **In one sentence**: This study optimizes isolation (ultracentrifugation vs. size-exclusion chromatography), in vitro regenerative activity, quercetin loading, and six-month -80 °C storage of tea-leaf-derived plant vesicles (Tea PDVs) for tissue regeneration and drug delivery.
- **In plain words**: Plant cells release tiny fat-walled bubbles called vesicles, and researchers are exploring them as natural carriers for medicines. This paper compared several plants and found tea leaves gave the most vesicles and the cleanest preparations, and that a column-based separation method removed more protein contamination than the standard spinning method. The tea vesicles did not harm human cells in laboratory tests, appeared to help cells survive stress and heal and form tubes, and carried the drug quercetin better when treated with a soap-like agent.
- **Why it matters**: Vesicles that are cheap to grow, easy to scale up, and stable in storage would matter for making plant-based therapies practical. The work is laboratory-only (cell cultures and one proof-of-concept drug), so its clinical relevance is still unknown and the text does not show animal or patient data.
- **Background needed**: - Extracellular vesicles: tiny membrane-bound particles that cells release and that can carry molecules between cells.
- Plant-derived vesicles (PDVs): the same kind of particles obtained from plants, often proposed as cheaper, more sustainable alternatives.
- Ultracentrifugation: spinning samples at very high speed to separate particles by size and density.
- Size-exclusion chromatography (SEC): passing a sample through a column so that particles separate by size; smaller contaminants are retained longer.
- Mesenchymal stem cells (MSCs) and endothelial cells: cell types involved in tissue repair and in lining blood vessels, used here as test cells.
- Staurosporine: a chemical that triggers cell death, used to test whether a sample protects cells.
- Quercetin: a plant compound studied as a model drug.
- Cryopreservation: storing samples at very low temperature, here -80 °C, often with protective additives such as trehalose or sucrose. · level: intermediate

<details><summary>Original abstract</summary>

Plant-derived vesicles (PDVs) are emerging as sustainable nanotherapeutic platforms, although challenges regarding isolation, scalability, biological activity, drug loading, and storage stability hinder their biomedical translation. This study aimed to optimize PDV production, exploring different sources to assess the one with greater translation potential, in terms of for yield and purity. To that end, PDVs from tea and red cabbage leaves, as well as ginger and turmeric roots were isolated by differential ultracentrifugation and size-exclusion chromatography (SEC), comparing both methodologies. Tea provided the highest vesicle yield and purity, with SEC outperforming ultracentrifugation in reducing soluble protein contamination. SEC isolated tea leaf-derived PDVs (Tea PDVs) were therefore further optimization using scalable fast protein liquid chromatography. Proteomic characterization showed enrichment in hydrolases, which could be related to an inherent capacity to induce tissue remodelling. Hence, regenerative potential was tested in vitro on mesenchymal stem cells (MSCs) and endothelial cells (HAECs). Firstly, Tea PDVs showed no cytotoxicity in MSCs and HAECs, even at high concentrations. Importantly, they significantly attenuated staurosporine-induced MSC death and promoted endothelial wound closure and capillary-like network formation, supporting their regenerative potential. Drug delivery potential was also assayed using quercetin, as a proof-of-concept drug. Saponin-mediated permeabilization significantly improved quercetin loading compared with passive incubation. Another important hurdle towards clinical translation, is determination of the ideal storage conditions for PDVs, which is still missing. To address this, we performed a six-months storage study at -80 C, analysing different cryopreservatives. The results showed that PBS alone caused substantial particle loss and increased vesicle size, whereas HEPES + trehalose-, sucrose-, and trehalose + human albumin-containing cryoprotective formulations preserved vesicle size and mitigated particle loss, facilitating long-term stability. Overall, these findings identify Tea PDVs as promising biocompatible nanocarriers with intrinsic regenerative properties. The optimized isolation, drug-loading, and preservation strategies provide a foundation for further development of plant-based nanotherapeutics targeting tissue regeneration and drug delivery applications in regenerative medicine.

</details>

## Computational and systems biology

### [APEs: Agentic Prediction of Epitopes to Guide Antibody-Antigen Structure Prediction](https://www.biorxiv.org/content/10.64898/2026.11.23.768576v1)
*Kang, M.; Yoon, M. S.; Park, J. et al.* · `bioinformatics` · bioRxiv doi:10.64898/2026.11.23.768576 v1 · relevance 0.11

- **In one sentence**: APEs is an LLM-agent system that retrieves pre-target public evidence to propose ranked residue-level epitope patches, which are then used to steer Protenix-v1 sampling and select antibody-antigen complex models evaluated on CASP16 and CASP17 targets.
- **In plain words**: Antibodies stick to specific spots on a target protein, called the epitope, and computer models often struggle to predict where those spots are and how the two proteins fit together. This paper describes a system that searches public sources for clues about the target, uses them to suggest likely contact spots, and then uses those suggestions to guide a structure-prediction model's sampling and choice of final models. On retrospective CASP test targets, the top suggested spot was at least 50% correct for nine of 14 targets, and the best selected models scored higher on average than the unguided top-ranked models.
- **Why it matters**: Predicting antibody-antigen structures is a hard, practically important problem for drug and vaccine design, and the paper shows that public, target-specific evidence can be used at inference time to guide predictions. The gains are reported on a small set of targets, and the prospective CASP17 release is still untested in the text, so the broader value is unclear.
- **Background needed**: - Antibody: an immune protein that binds a specific target molecule (antigen).
- Epitope: the patch of residues (amino acids) on the antigen that the antibody contacts.
- Antibody-antigen complex: the 3D structure formed when the two proteins bind.
- CASP: a community blind contest in which groups predict protein structures before experimental results are published.
- DockQ: a 0-1 score for how accurately a predicted complex matches the true one.
- ipSAE: a confidence score for interface quality, used here to pick among models.
- Protenix-v1: a structure-prediction model; "sampling" means generating many candidate poses.
- Retrospective evaluation: testing on past targets while restricting searches to information available before each target's release date. · level: research-level

<details><summary>Original abstract</summary>

Antibody-antigen complex prediction remains difficult because the surface recognized by a specific antibody is often uncertain, and model confidence may not distinguish alternative poses. We developed APEs (Agentic Prediction of Epitopes for Structure Prediction), an agentic system that retrieves public evidence, interprets predicted antibody and antigen structures, and produces ranked residue-level epitope hypotheses. For retrospective evaluation, web retrieval was restricted to sources released before each CASP target entry date. Across eight CASP16 and six released CASP17 targets, the top-ranked patch reached residue precision of at least 0.5 for nine of 14 targets. We then used the predicted epitopes to steer additional Protenix-v1 sampling and to compare steered finalists with the highest ipSAE unsteered model. The retrospective best selection across three independent router calls increased mean DockQ from 0.306 to 0.375; DockQ increased from 0.089 to 0.679 for H2321 and from 0.005 to 0.379 for H2346. These results show that publicly available evidence specific to the target antibody-antigen complex can serve as an inference-time signal for epitope localization, guided complex sampling, and model selection. We also release predictions for CASP17 targets whose experimental structures had not been released when the predictions were finalized, providing a prospective test of APEs (https://github.com/CSSB-SNU/ape).

</details>

### [Koopman Analysis Reveals Collective Modes Governing Cellular Dynamics](https://www.biorxiv.org/content/10.64898/2026.11.18.767672v1)
*Dutta, S.; Yu, W.; Zheng, Z. et al.* · `biophysics` · bioRxiv doi:10.64898/2026.11.18.767672 v1 · relevance 0.09

- **In one sentence**: The paper applies Koopman operator theory to whole-cell dynamical models to extract globally defined collective modes, which separate into slow modes forming a low-dimensional manifold and are linked to cell-cycle and cell-state transition processes.
- **In plain words**: Living cells are very complicated systems whose behavior is hard to predict, especially when they are far from a steady state. This paper uses a mathematical tool called Koopman analysis to re-describe whole-cell computer models in a simpler form, looking for patterns that act across the whole system. The authors report that these patterns relate to specific cell-cycle processes such as mitosis and DNA replication.
- **Why it matters**: The approach aims to give a global, rather than only local, simplification of nonlinear biological dynamics, which is a long-standing difficulty. Its value depends on whether the reported links to biology hold up in other models and in experiments; the text alone does not show that.
- **Background needed**: - Nonlinear system: outputs do not scale simply with inputs, so small changes can have large or unexpected effects.
- Linearization: approximating a complicated system with simpler linear rules; most standard versions only work near one reference state.
- Koopman operator: a method that tracks how measurements of a system evolve, allowing a nonlinear system to be described linearly over its whole state space.
- Normal modes: independent patterns of collective motion in a system, familiar from vibrating molecules and crystals.
- Slow manifold: the lower-dimensional set of states that a system settles onto over long times.
- Gene regulatory network: the web of interactions by which genes switch each other on or off.
- Whole-cell model: a computer simulation that represents many cellular processes together. · level: research-level

<details><summary>Original abstract</summary>

Living systems are complex nonlinear systems that operate far from thermodynamic equilibrium, and this nonlinearity makes their dynamics difficult to analyze. Several linearization techniques have been developed to address this problem, but most are local. Koopman operator theory is a powerful alternative that linearizes a system globally. Here we show that it not only achieves global linearization but also reveals collective modes that govern the dynamics of complex, out-of-equilibrium nonlinear systems. Applying the approach to whole-cell dynamical models, we find that these collective modes have physical and biological significance and relate to distinct processes in the cell cycle and in cell-state transitions. Collective and normal modes are widespread in many-body systems, particularly in condensed matter (e.g., magnons, phonons, hydrodynamic modes) and in macromolecular dynamics (e.g., normal mode analysis). By demonstrating that such modes also exist in cell-state transition dynamics, and in non-equilibrium nonlinear systems more generally, we offer a new theoretical-physics perspective on these systems. The collective modes separate into slow and fast modes. Long-term dynamics are governed by a few dominant slow modes that form a slow manifold of much lower dimension than the original state space. Thus, although the cell is a very high-dimensional system, its cell-cycle dynamics ultimately reduce to a low-dimensional space. Each mode comprises the coordinated behavior of groups of genes and reflects the structure of the underlying gene regulatory network. The modes can also be decomposed into terms that behave like damped harmonic oscillators, drawing an analogy between the modes of a nonlinear system and the normal modes of many-body systems. Finally, our analysis suggests that the dominant modes are closely associated with biological processes in the cell cycle, including mitosis, spindle checkpoint signaling, and DNA replication and repair.

</details>

## Neuroscience

### [Cross-domain competition for memory reactivation resources during sleep](https://www.biorxiv.org/content/10.64898/2026.11.20.768209v1)
*Temudo, A.; Nicolas, J.; King, B. R. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.20.768209 v1 · relevance 0.06

- **In one sentence**: In a within-subject nap study (n=24), cueing object-task memories during NREM sleep with targeted memory reactivation did not indirectly strengthen a linked motor memory, and sleep EEG slow oscillation and spindle activity appeared to favor the motor trace over the object trace.
- **In plain words**: Sleep helps the brain strengthen what we learned during the day, and researchers can nudge this by playing a sound cue that was paired with a memory while people sleep. This study asked whether cueing one task (an object sequence) could also reactivate a second, related task (a motor sequence) that shared a similar underlying order. The cue did not help the linked motor skill; instead it seemed to hurt the object memory, and brain-wave patterns suggested the motor memory got the sleep processing resources.
- **Why it matters**: It suggests that memories from different skill areas may compete for limited sleep-related reactivation, which matters for how cueing methods are designed. The text alone does not show how robust or general this competition is, so it should be treated as a finding from one small study.
- **Background needed**: - Targeted memory reactivation (TMR): pairing a learned task with a sound or smell cue, then replaying the cue during sleep to re-activate that memory.
- NREM sleep: the deeper, non-dream stages of sleep, when memory consolidation is thought to happen.
- Slow oscillations (0.5–2 Hz): slow, large brain-wave rhythms during deep sleep, thought to coordinate memory processing.
- Sleep spindles (12–16 Hz): short bursts of faster brain activity during light-to-deep sleep, linked to memory stabilization.
- EEG: electrodes on the scalp that record the brain's electrical activity.
- Within-subject design: every participant takes part in all conditions, so each person serves as their own comparison.
- Consolidation: the process by which a newly learned memory becomes more stable over time. · level: research-level

<details><summary>Original abstract</summary>

Targeted Memory Reactivation (TMR) enhances the consolidation of both declarative and procedural memories. As previous research highlights the importance of cross-domain interactions in shaping memory consolidation, we investigated here whether interacting memories from different domains can be co-reactivated by TMR during post-learning sleep, and in turn enhance consolidation. In a fully within-subject design, twenty-four young, healthy participants learned both a motor and an object sequence learning task that were linked or not by a shared ordinal structure. TMR cues associated only with the object task were presented during post-learning non-rapid eye movement (NREM) sleep which was monitored with electroencephalography (EEG) during a 90-minute nap. We tested whether reactivating object memories would indirectly reactivate the linked motor memory. Behavioral results showed no overall effect of association but indicated that TMR disrupted object memory consolidation without indirectly affecting performance on the linked motor task. Sleep EEG data point to a competition for reactivation resources whereby slow oscillation (SO; 0.5-2 Hz) and spindle activity (12-16 Hz) involved in both memory protection and potentiation during sleep were preferentially allocated to the covert consolidation of the motor trace at the expense of object memory. These findings suggest that cross-domain memories sharing a common learning structure compete for consolidation resources during post-learning sleep.

</details>

### [Reduced bushy cell firing limits binaural coding after cochlear synaptopathy](https://www.biorxiv.org/content/10.64898/2026.11.21.768331v1)
*Ashida, G.; Tollin, D. J.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.21.768331 v1 · relevance 0.06

- **In one sentence**: A computational model of the auditory brainstem tests how cochlear synaptopathy (loss of auditory nerve inputs to bushy cells) and increased spike-timing jitter from myelin dysfunction separately and jointly degrade binaural tuning in the lateral superior olive.
- **In plain words**: Some people have trouble following speech in noisy rooms even though their ordinary hearing tests look normal. This paper uses a computer model of the hearing pathway to test one possible cause: losing some of the nerve connections from the ear, plus nerve signals arriving with less precise timing. The model found that losing connections cut how often brain cells fire and hurt the comparison of sounds between the two ears, while timing jitter kept firing rates up but blurred the timing and also hurt that comparison.
- **Why it matters**: It offers a mechanistic account of why hearing problems can occur with normal thresholds, and it suggests that fixing timing problems alone may not be enough if nerve input stays reduced. The text is a modeling study, so its predictions would need testing in real listeners or animals before any clinical conclusions.
- **Background needed**: - Cochlear synaptopathy: loss of connections between inner hair cells in the ear and auditory nerve fibres, which can occur without raising the hearing threshold.
- Bushy cells: neurons in the cochlear nucleus (first brainstem hub for hearing) that receive auditory nerve input and relay timing information.
- Lateral superior olive (LSO): a brainstem nucleus that compares loudness between the two ears.
- Binaural processing: using differences between the two ears' signals to locate sounds and separate them from background noise.
- Phase locking: neurons firing in step with the timing of a sound wave; temporal jitter is random timing error that blurs this.
- Myelin: the insulating sheath on nerve fibres that helps signals travel with precise timing. · level: research-level

<details><summary>Original abstract</summary>

Listeners can experience difficulties with spatial hearing and speech understanding in complex acoustic environments despite near-normal hearing thresholds. Cochlear synaptopathy, which reduces auditory nerve input without elevating thresholds, is one candidate mechanism, but how this peripheral deafferentation disrupts binaural processing remains unclear. We adapted a physiologically constrained computational model incorporating the auditory periphery, spherical and globular bushy cells of the cochlear nucleus and the lateral superior olive (LSO) to examine the separate and combined effects of reduced afferent input and degraded spike timing. Synaptopathy was modeled as loss of auditory nerve inputs to bushy cells, whereas central myelin dysfunction was modeled as increased temporal jitter in bushy cell outputs. Loss of auditory nerve input substantially reduced bushy cell firing rates without degrading phase locking. Despite this preserved temporal precision, binaural tuning in the LSO declined disproportionately, where moderate afferent loss produced substantial reductions in sensitivity to interaural envelope phase differences. In contrast, temporal jitter preserved bushy cell firing rates but degraded phase locking and binaural tuning. Selective loss of input to excitatory versus inhibitory pathways produced opposite changes in overall LSO firing rate, yet both reduced binaural interaction. These results identify two mechanistically distinct routes to impaired binaural coding: too few precisely timed spikes, and a sufficient number of spikes arriving with inadequate temporal precision. These results predict that correcting myelin-related timing deficits alone would leave substantial binaural coding impairment when cochlear deafferentation persists, motivating interventions that address both diminished afferent drive and impaired transmission.

</details>

## Genetics and genomics

### [Reproductive competition amplifies purifying selection and reduces genetic load](https://www.biorxiv.org/content/10.64898/2026.11.20.768053v1)
*van Oosterhout, C.; Marsters, J.; Birley, T.* · `genetics` · bioRxiv doi:10.64898/2026.11.20.768053 v1 · relevance 0.08

- **In one sentence**: Forward-time simulations quantify how competitive and sexual selection, expressed as an effective selection coefficient calibrated against hard selection, remove deleterious variation and reduce genetic load more efficiently than hard selection, with implications for bottlenecked populations.
- **In plain words**: The paper asks whether animals or plants that win mates or resources through competition clear out harmful genetic variants more effectively than a population where those with poor genes simply die off. Using computer simulations of evolution over time, the authors measure competition's effect as an equivalent strength of natural selection. They report that competing against several rivals, and repeating contests, strengthens the removal of harmful mutations and lowers the overall genetic burden at a smaller cost to population size.
- **Why it matters**: The idea that reproductive competition can purge harmful mutations with less demographic cost is relevant to conservation of small or recovering populations, where genetic load can persist. The text suggests a possible link to "genic capture" (the idea that mate choice reflects overall genetic quality), but this connection is framed as a possibility rather than shown directly, and the summary is based only on the abstract.
- **Background needed**: - Deleterious mutations: genetic changes that reduce fitness (survival or reproduction).
- Genetic load: the average fitness cost a population carries from these mutations.
- Hard selection: death or non-reproduction of individuals below a fitness threshold, regardless of others.
- Competitive/sexual selection: differences in reproductive success arising from contests among individuals, such as mate competition.
- Selection coefficient: a number expressing how strongly a variant is favoured or disfavoured.
- Forward-time simulation: computer models that track genetic changes generation by generation.
- Genetic drift: random changes in gene frequencies, stronger in small populations.
- Bottleneck: a sharp population decline that reduces genetic diversity.
- Genic capture: the idea that mate choice or competition reflects genome-wide quality. · level: research-level

<details><summary>Original abstract</summary>

Deleterious mutations impose genetic load, and purging them through hard selection can carry substantial demographic costs. Competitive and sexual selection can instead remove deleterious variation through differential reproductive success. What remains unclear is when this process is more efficient than equivalent hard selection, and how competition generates this advantage. Here, we use forward-time simulations to express the impact of competition as an effective selection coefficient (se) calibrated against hard selection. Competition with multiple rivals strongly amplified purifying selection, whereas repeated contests improved discrimination by averaging stochastic and environmental variation. Strong competition also reduced genetic load relative to hard selection. These effects can shift weakly deleterious mutations from drift-dominated behaviour towards efficient purging. By front-loading purifying selection into reproduction, competitive selection can reduce genetic load at lower demographic cost. This provides a population-genetic mechanism by which genic capture can translate genome-wide genetic quality into more effective purifying selection. This may be particularly important in bottlenecked populations, where demographic recovery can relax purifying selection and allow genomic erosion to persist.

</details>

### [A genetic toolkit of visible mutants for Caenorhabditis briggsae](https://www.biorxiv.org/content/10.64898/2026.11.19.767928v1)
*Johnsen, R.; Mah, A.; Thillainathan, B. et al.* · `genetics` · bioRxiv doi:10.64898/2026.11.19.767928 v1 · relevance 0.08

- **In one sentence**: A resource paper reporting 183 visible EMS-induced mutants of the nematode Caenorhabditis briggsae, their genetic mapping to six linkage groups, and molecular identification of several orthologs of C. elegans genes.
- **In plain words**: Researchers studying a tiny worm called Caenorhabditis briggsae, a close relative of the lab favorite C. elegans, built a catalogue of 183 mutant worms that show easy-to-spot differences such as changes in body shape or movement. They worked out which of the worm's six chromosome groups most of these mutations sit on, and matched several genes to their counterparts in C. elegans. The authors present the strains and underlying data as a shared resource for comparing these worm species.
- **Why it matters**: Visible mutants are the basic tools geneticists use to study how a gene produces a trait, so a documented, publicly usable set for a second model worm makes comparisons between species easier. The text describes this as a resource and does not claim a specific new biological finding beyond the mapping and gene identifications.
- **Background needed**: - Caenorhabditis elegans is a small roundworm used heavily in genetics; C. briggsae is a related species used for comparison.
- EMS (a chemical mutagen) randomly creates mutations in an organism's DNA; screeners then look for worms with obvious traits.
- A "locus" is a position on a chromosome where a gene or mutation sits; "linkage group" is a chromosome as defined by genetic crosses.
- Complementation tests check whether two mutations affect the same gene; linkage and multi-factor crosses measure how close mutations sit on a chromosome.
- Orthologs are genes in different species that descend from a common ancestor gene.
- Levamisole is a drug that acts on worm muscle receptors; mutants resistant to it help identify receptor subunit genes (unc-38, unc-29).
- Transgene rescue means inserting a working copy of a gene to see if it restores the normal trait, which confirms the gene's identity. · level: research-level

<details><summary>Original abstract</summary>

Caenorhabditis briggsae is a widely used model for comparative genetic studies involving C. elegans. Genetic analysis in C. briggsae depends on mutations with clear, easily recognizable phenotypes, yet most mutants reported so far have been mentioned only as names and linkage groups, without underlying experimental data. This study reports 183 C. briggsae mutants belonging to 11 phenotypic classes, which represent the most comprehensive collection to date. Almost all mutants were recovered in EMS screens of the reference strain AF16. Our analysis revealed that 121 mutations define 55 loci and 62 remain unassigned. A combination of complementation tests, linkage tests, two- and three-factor crosses, and polymorphism-based mappings helped place 51 loci and 15 further mutations to the six linkage groups. We report the supporting data, map distances, linkage groups, and corrections to several earlier assignments. Twenty-three loci correspond to molecularly identified orthologs of C. elegans genes, including six for which we report genetic, rescue, or sequence evidence here. The levamisole-resistant mutants fall into at least three complementation groups, two of which correspond to Cbr-unc-38 and Cbr-unc-29 (levamisole-sensitive nicotinic acetylcholine receptor a and non-a subunit, respectively). Transgene rescue experiments identify Cbr-dpy-1 (mucin-like), Cbr-sma-6 (TGFb type receptor kinase), and Cbr-unc-4 (homeodomain transcription factor), genes that have long been in use as genetic markers. In all cases, molecularly identified genes are located on the same chromosome as their C. elegans orthologs, although gene order within chromosomes differs. The strains, map, and underlying data provide a resource for genetic and comparative studies in Caenorhabditis nematodes.

</details>

## Cell and molecular biology

### [Monolayer, Spheroid, and Organoid Formats Elicit Proteomic States that Couple Organelle Organization to Metabolic Vulnerabilities](https://www.biorxiv.org/content/10.64898/2026.11.20.768195v1)
*Lum, K. K.; Pundel, O. J.; Hofstadter, W. A. et al.* · `molecular biology` · bioRxiv doi:10.64898/2026.11.20.768195 v1 · relevance 0.11

- **In one sentence**: Proteomic comparison of matched monolayer, spheroid, and organoid cultures of mouse high-grade serous tubo-ovarian cancer models, showing that 3D architecture and media shape cell state, and linking the PPN genotype's mitochondria-ER contacts and lipid droplet clustering to higher murine cytomegalovirus permissiveness.
- **In plain words**: Scientists grow cells in flat dishes or in 3D clumps (spheroids and organoids) to better mimic tissue, but it is not well known how these forms differ at the molecular level. This study measured thousands of proteins in ovarian cancer models grown each way and found that both the shape of the culture and the growth medium change the cells' protein makeup. One genetic variant, with loss of Trp53, Pten and Nf1, showed more changes in fat droplets, energy-producing structures and their contacts with other cell parts, and these cells were more easily infected by mouse cytomegalovirus.
- **Why it matters**: The paper offers a protein dataset that researchers may use when choosing between flat and 3D culture systems, which matters for experimental design. The link between a cancer genotype, organelle contacts and viral infection is an interesting hypothesis, but the text alone does not show that these connections cause one another or that they apply to human disease.
- **Background needed**: - Monolayer: cells grown as a flat sheet on a dish, the conventional lab format.
- Spheroid and organoid: 3D cell clusters; organoids are derived from tissue and better preserve tissue structure.
- Proteomics: large-scale measurement of the proteins present in cells.
- High-grade serous tubo-ovarian cancer (HGSC): the most common and aggressive type of ovarian cancer.
- Genotypes (PPN, PBM, P): mouse cell lines carrying specific gene losses or changes, named by the genes affected.
- Mitochondria and endoplasmic reticulum (ER): energy-producing compartments and a membrane network; their physical contacts help exchange lipids and calcium.
- Lipid droplets: storage units for fats inside cells.
- Cytomegalovirus: a herpes-family virus; here studied in mouse cells. · level: research-level

<details><summary>Original abstract</summary>

Three-dimensional (3D) cell culture systems are becoming more widely applied to model tissue organization, disease progression, and therapeutic response. Yet, the molecular characteristics that distinguish organoids and spheroids from conventional monolayer culture are incompletely defined. Here, using tumorigenic organoid models of high-grade serous tubo-ovarian cancer (HGSC), we establish a quantitative proteomic resource that reveals how cell architecture and media independently but jointly shape the cellular state in organoids, spheroids, and monolayers. We further pursue HGSC subtype-enriched features within this framework and identify that a poor prognosis-associated genotype with reported paclitaxel hypersensitivity, Trp53-/-;Pten-/-;Nf1-/- (PPN), is marked by increased microtubule-associated proteins, lipid-associated factors, and mitochondrial remodeling. PPN cells displayed clustered lipid droplets, whereby mitochondria-ER tethering increased. Relative to Trp53-/- (P) and a frequent HGSC genotype, Trp53-/-;Brca1+/-;MycOE (PBM), live-cell imaging showed that PPN exhibits the highest degree of stable mitochondria-ER encapsulations, coincident with fission-biased mitochondria and a high-flux respiratory state. Disruption of the mitochondria-ER contact protein PTPIP51 reduced lipid droplet clustering in the PPN state. Because cytomegalovirus is known to exploit host mitochondria remodeling, mitochondria-ER contacts, and metabolic output during infection, we tested whether this pre-existing host configuration is associated with cytomegalovirus permissiveness. PPN organoids exhibited greater murine cytomegalovirus infection and infectious output than matched monolayers or PBM. Together, these data define a resource of distinct protein characteristics between matched monolayer, spheroid, and organoid systems that should be considered for experimental design. We also uncover a mechanistic axis connecting 3D architecture, organelle contacts, metabolism, drug response, and viral permissiveness.

</details>

### [Phosphorylation of the ER-plasma membrane tether E-Syt2 facilitates the loss of contact sites in mitosis](https://www.biorxiv.org/content/10.64898/2026.11.21.768271v1)
*Machaca, K.; Al Hamaq, J.; Keyan, K. S. et al.* · `cell biology` · bioRxiv doi:10.64898/2026.11.21.768271 v1 · relevance 0.10

- **In one sentence**: Phosphorylation of the ER-plasma membrane tether E-Syt2 during mitosis is shown to promote the loss of ER-plasma membrane contact sites, and preventing that phosphorylation preserves the contacts and is linked to delayed growth and mitotic progression.
- **In plain words**: When a cell divides, its internal structures are reorganized so they can be shared between the two daughter cells. This paper looks at places where the cell's endoplasmic reticulum (an internal membrane network) touches the outer cell membrane, and at how those touching points disappear during division. The authors report that adding a chemical tag (phosphorylation) to a protein called E-Syt2 helps cause these contacts to break apart, and that stopping this tagging keeps the contacts in place.</plain>
<parameter name="why>The work offers a specific molecular mechanism for a known but poorly explained loss of membrane contacts during cell division. The text also links persistent contacts to slower growth and slower passage through mitosis, suggesting the contacts' removal matters for timely division. The text does not say how broadly this applies beyond the cells studied.
- **Background needed**: - Mitosis: the stage of cell division in which a cell's chromosomes are separated into two daughter cells.
- Organelles: compartments inside a cell (such as the ER) that carry out specific jobs.
- Endoplasmic reticulum (ER): an internal membrane network involved in making and transporting proteins and lipids.
- Membrane contact sites: places where two different membranes are held very close together by tethering proteins, allowing exchange of molecules and signals.
- Tether (E-Syt2): a protein that physically links the ER to the outer cell membrane.
- Phosphorylation: the addition of a phosphate chemical group to a protein, often a switch that changes how the protein behaves. · level: research-level

<details><summary>Original abstract</summary>

Mitosis is associated with dramatic remodeling of intracellular organelles that supports their equal distribution between daughter cells. Recent investigations into membrane contact sites (MCS) show that they also remodel in mitosis with a significant loss of ER-plasma membrane CS (ERPMCS). However, the mechanisms governing this loss are unknown. Here we show that phosphorylation of the ERPMCS tether extended synaptotagmin 2 (E-Syt2) facilitates the loss of ERPMCS in mitosis. Preventing E-Syt2 phosphorylation in mitosis rescues the loss of ERPMCS. The persistence of ERPMCS is associated with delayed growth and progression through mitosis. This shows that E-Syt2 mitosis specific phosphorylation regulates its tethering potential and that the loss of ERPMCS is important for timely cell division.

</details>

## Immunology and microbiology

### [Intradermal and intranasal vaccination with microparticulated ASFV proteins induces distinct immune profiles in pigs](https://www.biorxiv.org/content/10.64898/2026.11.23.768517v1)
*Coatu, E.; Pina-Pedrero, S.; Tort, A. et al.* · `immunology` · bioRxiv doi:10.64898/2026.11.23.768517 v1 · relevance 0.11

- **In one sentence**: In pigs, intradermal and intranasal vaccination with the same nanoparticle-delivered ASFV protein cocktail produced distinct immune profiles, but no group was protected against a virulent challenge.
- **In plain words**: African swine fever is a deadly virus that infects pigs and has no safe, widely approved vaccine. This study tested whether giving the same set of viral proteins by different routes, under the skin or into the nose, changes the kind of immune response pigs make. Skin injection produced antibodies in the blood but only modest cell-based immunity, while nasal delivery alone produced no detectable blood antibodies or cell responses before challenge.
- **Why it matters**: Vaccine research for this disease is limited by safety concerns with live vaccines, so comparing delivery routes helps show which immune responses matter. The authors report that antibodies alone did not protect, which supports the view that cell-mediated immunity is important; the text does not establish how this would translate to field vaccines.
- **Background needed**: - African swine fever (ASF) is a severe viral disease of pigs with large economic impact on the pig industry.
- Live attenuated vaccines (weakened live virus) work but raise biosafety concerns, so subunit vaccines (made from selected viral parts) are being explored.
- Vaccines can be given by different routes (intradermal = into the skin; intranasal = into the nose), which can shape the immune response.
- Two main immune arms: antibodies (proteins that b

<details><summary>Original abstract</summary>

African Swine Fever (ASF) is a major threat to the swine industry due to its severe socioeconomic impact and the lack of safe and effective vaccines. Although live attenuated vaccines (LAVs) can induce robust immunity, biosafety concerns restrict their use, making subunit vaccines the preferred alternative. In this context, understanding how vaccination routes modulate immunity is critical. A previous study using a viral vector-based vaccine, encoding for the ASFV antigens p30, p54, p72, p72c and CD2v, induced protection when combining intranasal (IN) and parenteral administrations. However, the relative contribution of each administration route to vaccine-induced immunity remains unclear. Here we investigated how independent and combined vaccination routes influence the immune responses induced by the same ASFV protein cocktail delivered as nanoparticle-based secretory granules. Following a prime-boost regime, pigs vaccinated via intradermal (ID) route seroconverted and developed strong systemic ASFV-specific IgG responses, despite inducing only modest ASFV-specific cellular responses. In contrast, IN administration alone failed to elicit detectable systemic humoral or cellular responses and did not improve the vaccine-induced immunogenicity when combined with the ID route. Following a challenge with a virulent ASFV strain, no protection was achieved in any of the immunized groups. Interestingly, intranasally vaccinated pigs exhibited an accelerated post-challenge ASFV-specific antibody boost in serum compared to controls, suggesting that vaccination through this mucosal route induced immune priming despite the absence of detectable systemic humoral responses before challenge. Overall, these findings reveal distinct route-dependent immune profiles elicited by the same ASFV antigen cocktail and highlight again that robust humoral responses alone are insufficient for protection, further supporting the importance of cellular immunity in vaccine-induced protection.

</details>

### [A multi-scale forecasting framework to prioritize clinically-relevant antibiotic resistance alleles](https://www.biorxiv.org/content/10.64898/2026.11.20.768016v1)
*Obeng, N.; Rodoni, A.; Niggli, Q. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.20.768016 v1 · relevance 0.11

- **In one sentence**: A computational framework combining mutation likelihoods, continuous-time stochastic modeling and population pharmacokinetics that prioritizes clinically common fluoroquinolone-resistance alleles (gyrA S81L) in Acinetobacter baumannii, with virtual-twin cohort simulations of drug penetration and immunity.
- **In plain words**: Bacteria can become resistant to antibiotics through specific genetic changes, but lab tests do not always predict which changes will spread once a drug is widely used. This paper builds a computer model that combines how likely each DNA change is to occur with how drug levels rise and fall in patients. Using the antibiotic ciprofloxacin and the bacterium Acinetobacter baumannii as a test case, the model ranks the common gyrA mutation S81L above rarer ones, matching what is seen in hospitals.
- **Why it matters**: Antibiotic resistance is a major global health threat, and better ways to anticipate which resistance mutations will take hold could inform drug development and risk checks. The authors also report limits: the same approach did not explain success in the pmrB and adeS genes, so it is a proof of concept rather than a general predictor.
- **Background needed**: - Antibiotic resistance: bacteria evolve changes that let them survive drugs that would normally kill them.
- Allele: a variant form of a gene; here, a specific DNA change in a gene.
- gyrA: a bacterial gene for an enzyme (DNA gyrase) that fluoroquinolone antibiotics like ciprofloxacin target.
- S81L: a specific single amino-acid change at position 81 of the GyrA protein, swapping serine for leucine.
- Nucleotide substitution likelihood: how readily a given DNA letter change happens by chance.
- Pharmacokinetics: how the body absorbs, distributes and clears a drug over time, which sets how drug levels fluctuate.
- Stochastic modeling: simulation that includes random chance in births, deaths and mutations.
- Virtual twin cohort: a simulated group of patients with varied characteristics, used to test scenarios. · level: research-level

<details><summary>Original abstract</summary>

Established in vitro measures for the emergence of antimicrobial resistance, a critical global threat, can fail to predict which in vitro discovered mutations will dominate in the real world following widespread antibiotic use. Here, we introduce a multi-scale computational framework integrating genetic constraints and population pharmacokinetics and apply it to explain resistance allele success in Acinetobacter baumannii for the historic case of resistance to the fluoroquinolone antibiotic ciprofloxacin. By coupling intrinsic nucleotide substitution likelihoods with continuous-time stochastic modeling under fluctuating drug exposures, our framework clearly prioritizes the most common real world gyrA fluoroquinolone resistance allele S81L over rarer alleles, reflecting its clinical success. While gyrA serves as a proof-of-concept case study for direct, active-site drug-target interactions where the target space is constrained, we observe that the nucleotide substitution likelihoods are not explaining allele success in resistance-determining genes pmrB and adeS. Furthermore, "virtual twin" cohort simulations reveal that restricted drug penetration or compromised immunity expands selective windows, rescuing rare, low-fitness alleles. This advances our understanding of prospective, model-informed risk prediction during antibiotic development.

</details>

## Cancer biology

### [Media matters: A resource for understanding the determinants of migratory potential of malignant and non-malignant cells](https://www.biorxiv.org/content/10.64898/2026.11.18.767665v1)
*Kim, B.; Lopez, A.; Osuna, M. F. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.18.767665 v1 · relevance 0.07

- **In one sentence**: A high-throughput wound-healing/invasion screen of more than 60 malignant and non-malignant cell lines from six tissues, probing how glycolysis, oxidative phosphorylation, and culture media affect migration and metastatic potential.
- **In plain words**: Cells move around the body to heal wounds, and cancer cells move to spread tumours to new organs. This paper tested dozens of normal and cancer cell lines from the pancreas, colon, skin, breast, prostate and lung to see how fast each kind moves and invades. It found that normal lung, skin and pancreas cells often moved faster than their cancer counterparts, and that the nutrient mix in the culture liquid changed how cancer cells behaved.
- **Why it matters**: Cell movement is central to both cancer spread and wound healing, and the authors argue that few migration-targeting drugs have reached clinical trials. The screen is offered as a reference resource, and the link to new drug targets is a proposal in the text rather than a demonstrated result.
- **Background needed**: - Migration/invasion assay: a lab test where cells close a scratch or gap in a dish, or push through a barrier, and researchers measure how fast they do so.
- Malignant vs non-malignant cells: cancerous cells versus normal cells taken from the same kind of tissue.
- Glycolysis and oxidative phosphorylation: two ways cells turn sugar into energy, one without oxygen and one using the mitochondria.
- Metastasis: the spread of cancer from its original site to other organs.
- Migrastatic/antimetastatic therapy: drugs meant to slow cell movement or spread rather than kill the tumour cells directly.
- Culture media: the nutrient liquid cells grow in; this paper varied serum, calcium and glucose levels. · level: research-level

<details><summary>Original abstract</summary>

Cell mobility is critical for homeostatic processes such as wound repair and diseases like cancer metastasis. While the advent of migrastatic and antimetastatic therapies has promise, the identification and translation of pathways important for migratory plasticity into druggable targets approved in clinical trials are considerably lacking. To better understand why, we developed an unbiased high-throughput wound-healing/invasion assay to screen for the migratory potential of >60 non-malignant and malignant cell lines derived from the pancreas, colon, skin, breast, prostate, and lung. The goal of this phenotypic screen was to provide a resource of migration/invasion potential and insight into the differential properties not only between malignant and non-malignant cells but also the various carcinomas. Surprisingly, we found non-malignant epithelial cells of the lung, skin, and pancreas migrated/invaded faster than their malignant counterparts. We observed perturbation of glucose metabolism, via inhibition of glycolysis, restricted the migration of non-malignant but not cancer cells, whereas inhibition of oxidative phosphorylation limited the mobility of malignant more than normal cells of the lung, skin, and pancreas. Short-term acclimation of cancer cells in low-nutrient media, containing low/no serum, low calcium, and physiological concentrations of glucose, increased in vitro migration/invasion and in vivo metastatic potential of lung but not pancreatic carcinomas. Phenotypic and metabolic screens presented here could identify prospective therapeutics not only for cancer metastasis, but also diseases driven by the dysregulation of wound-healing/regeneration.

</details>

### [Metabolic priming recruits tumour cells across a mitochondrial vulnerability threshold and sensitizes them to chemotherapy](https://www.biorxiv.org/content/10.64898/2026.11.13.766410v1)
*Iborra, F. J.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.13.766410 v1 · relevance 0.05

- **In one sentence**: Single-cell study showing that metabolic priming (TEPP46, ethyl pyruvate, camptothecin) can push a subset of cancer cells into a transient mitochondrial state that responds to TMRM-based photodynamic damage, with descriptors of the fluorescence response predicting cell fate.
- **In plain words**: Cancer tumours contain mixed populations of cells, and some survive treatments that kill most of the others. This paper asks whether drugs that shift cells' energy metabolism can move a fraction of them into a fragile state in their mitochondria (the cell's energy-producing parts) that is more easily damaged by light-activated dye. The authors tracked the dye's glow in individual cells and found that a measure relative to each cell's own resting level predicted whether the cell would die.
- **Why it matters**: It proposes a way to find and follow tumour cells that resist treatment one cell at a time, and suggests a timing window for combining drugs. The authors state it is only a proof of concept in cultured cells and human tissue sections, with no in vivo testing, and that the combination results are descriptive and need independent replication.
- **Background needed**: - Intratumour heterogeneity: cancer cells within one tumour differ, so some survive treatment.
- Mitochondria: small structures that produce cell energy; their membrane voltage matters for cell survival.
- TMRM: a fluorescent dye that accumulates in mitochondria depending on membrane voltage and can act as a photosensitizer (light-activated damage agent) producing reactive oxygen species.
- Photodynamic damage: killing cells with light plus a light-sensitive agent.
- PKM2 and TEPP46: PKM2 is an enzyme in energy metabolism; TEPP46 is a drug that activates it.
- Camptothecin and TRAIL: an anticancer drug and a cell-death signalling protein, used here in combination tests.
- Bliss independence: a standard expected-effect model for combined treatments; survival below this expectation suggests synergy.
- AUC (area under the ROC curve): a 0.5 score is chance and 1.0 is perfect prediction. · level: research-level

<details><summary>Original abstract</summary>

Intratumour heterogeneity allows a fraction of cancer cells to escape otherwise effective treatment. Here we ask whether metabolic priming can recruit heterogeneous tumour cells into a transient mitochondrial state that is selectively vulnerable to photodynamic damage. Tetramethylrhodamine methyl ester (TMRM) has previously been shown to act as a mitochondria targeted photosensitizer; we exploit its voltage-dependent accumulation and dynamic fluorescence during pulsed illumination to quantify vulnerability in single cells. The response is a reproducible fluorescence excursion, a rise to a maximum followed by a decay, accompanied by reactive oxygen species production. Comparing seventeen descriptors of this excursion against subsequent fate in 195 cells across four arms shows that quantities referenced to each cell's own resting value outperform static intensity. The simple difference Fmax F0 predicts death with held-out areas under the curve of approximately 0.75 to 0.79, whereas resting intensity alone carries little transferable information and time to peak does not discriminate fate in the datasets tested. Metabolic priming with the PKM2 activator TEPP46 or with ethyl pyruvate increases the fraction of responding cells; under TEPP46 almost the whole population enters the responding state. PKM2 abundance is associated with faster entry into that state, and PKM2 is heterogeneous in human skin tumour sections. Four hours of camptothecin shifts the response distribution, increasing the fraction of cells above the untreated median from 50% to 76%, identifying a candidate intervention window. In combination experiments, TMRM photodynamic treatment produced survival below the Bliss-independence expectation with camptothecin or TRAIL, in both treatment orders and across three cell lines; these combination measurements are descriptive and require independent replication. The study therefore identifies a perturbation-revealed mitochondrial vulnerability that can be pharmacologically recruited and followed dynamically at single-cell resolution. It is a proof of concept in cultured cells and human tumour sections and has not been tested in vivo.

</details>

## Ecology and evolution

### [From individual movement to ecosystem response: how landscape structure shapes herbivore impacts](https://www.biorxiv.org/content/10.64898/2026.11.19.766513v1)
*Suarez, D. L.; Guisoni, N.; Laguna, M. F.* · `ecology` · bioRxiv doi:10.64898/2026.11.19.766513 v1 · relevance 0.10

- **In one sentence**: A spatially explicit stochastic individual-based model of two herbivore populations with different movement and foraging strategies, sharing renewable resources across heterogeneous landscapes, examined with Monte Carlo simulations to show how movement and landscape structure shape resource depletion and population dynamics.
- **In plain words**: This paper asks how the way individual animals move and feed shapes what happens to plant resources across a whole landscape. The authors built a computer simulation of two grazing animal groups that share regrowing vegetation, with patchy resources, predators and places to hide, and ran many randomized runs. They report that movement largely determines where plants get depleted, and that more productive land can sometimes lead to a larger relative loss of resources.
- **Why it matters**: The text suggests that local behaviour can produce landscape-scale outcomes that simple abundance counts would miss, which matters for managing grazed ecosystems. Because the results come from a simulation model described only in this abstract, their relevance to real ecosystems is not established here.
- **Background needed**: - Consumer-resource interaction: herbivores (consumers) eating plants (resources) that regrow over time.
- Individual-based model: each animal is simulated separately with its own movement and feeding rules, and large-scale patterns emerge from these.
- Stochastic model and Monte Carlo simulation: the model includes random elements, and many randomized runs are averaged to see typical outcomes.
- Landscape heterogeneity: resources are unevenly distributed in space, so where animals go matters.
- Refuges and predation: prey can escape to safe areas, which affects where they feed.
- Resource biomass vs. vegetation occupancy: total plant mass can fall well before the area covered by plants shrinks. · level: research-level

<details><summary>Original abstract</summary>

Understanding how local interactions generate large-scale ecological dynamics is a central challenge in ecology. In heterogeneous environments, consumer movement links resource distribution with exploitation, producing responses that may not be predicted from consumer abundance or resource availability alone. Here, we develop a spatially explicit stochastic individual-based model of two herbivore populations with contrasting movement and foraging strategies that share renewable resources. The model incorporates heterogeneous resources, consumer movement and feeding, resource regeneration, predation, and refuge availability. Using Monte Carlo simulations, we examine how herbivore pressure and landscape structure shape population dynamics and resource depletion. Movement strongly determines the spatial pattern of depletion, while resource vulnerability depends on the overlap between resource distribution and consumer activity. Counterintuitively, increasing the extent of a productive region increases initial resource biomass but can also increase relative resource loss. Additional resources sustain consumer activity where herbivores concentrate, showing that greater resource availability does not necessarily buffer ecosystems against herbivory. Resource biomass can also decline substantially before major reductions in vegetation occupancy become apparent. These results demonstrate how individual behaviour and landscape structure jointly shape ecosystem responses. The model provides a framework for investigating how spatially coupled consumer-resource interactions generate ecological dynamics.

</details>

### [ADTSIM2.0: An updated simulation of American dog tick (Dermacentor variabilis Acari: Ixodidae) population dynamics](https://www.biorxiv.org/content/10.64898/2026.11.20.768101v1)
*Sanderson, S.; Zettle, M.; Dubovyk, O. et al.* · `ecology` · bioRxiv doi:10.64898/2026.11.20.768101 v1 · relevance 0.09

- **In one sentence**: ADTSIM 2.0 is an updated weekly-time-step simulation of the American dog tick's life cycle, covering questing, host-seeking, survival, and temperature effects on development, with the aim of explaining variable local tick densities.
- **In plain words**: American dog ticks carry diseases that affect people and animals, but it is unclear why their numbers rise and fall so much from year to year. The authors updated an existing computer model that simulates the tick's life stages week by week, including how hosts such as small and medium mammals and local weather affect the ticks. The abstract reports that accurate data on host numbers and weather are critical for predicting local tick densities.
- **Why it matters**: A working model of tick populations could support public health information and help compare tick control measures. The authors say it could later be extended to track tick-borne pathogens, but the abstract does not show that this has been done.
- **Background needed**: - Dermacentor variabilis (American dog tick): a hard-bodied tick found across central and eastern North America that can transmit pathogens to people and pets.
- Life stages: egg, larva, nymph, and adult; each stage must find a host to feed on.
- Questing: ticks climb vegetation and wait with their legs out to grab passing hosts.
- Simulation model: a computer program that uses rules and inputs (weather, host numbers) to project population change over time; a weekly time step means it updates once per week.
- Trade-off: a tick that quests more may find more hosts but may dry out or die sooner. · level: intermediate

<details><summary>Original abstract</summary>

The American dog tick, Dermacentor variabilis (Say), is found across most of the central and eastern portions of North America, and is a known vector of human and veterinary pathogens. While this tick has been found throughout this region for decades, there is still little understanding of the drivers for the highly variable annual densities. To explore the relative effects of hosts, environmental conditions, and tick biology, we introduce ADTSIM 2.0, an upgraded version of the ADTSIM model that simulates the lifecycle of D. variabilis. The model uses a weekly time step and follows the life stages (egg, larvae, nymph, and adult), questing behavior, host-seeking dynamics, and survival rates under varying environmental conditions. The model includes calculations for tick interactions with small- and medium-sized mammal hosts and factors in critical environmental influences such as temperature on tick development and questing activity. It addresses the effect of questing behavior on tick longevity, emphasizing the trade off between survival and host-seeking. The results show that accurate estimates of both host densities and weather information are critical to predict local D. variabilis densities. This model provides the first step to building a tool for public health information, offering a framework for assessing tick control measures and is adaptable to add tick-borne pathogen dynamics for both human and animal diseases.

</details>

## Plant biology

### [High-throughput phenotyping reveals natural variation in tomato pollen responses to heat stress](https://www.biorxiv.org/content/10.64898/2026.11.19.767983v1)
*Warman, C.; Perkins, C. J.; McKinley, S. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.19.767983 v1 · relevance 0.06

- **In one sentence**: A high-throughput microscopy pipeline with automated pollen classification and single-tube tracking was used to measure heat responses of pollen from 218 tomato accessions and wild relatives at 26 and 34 °C.
- **In plain words**: Heat during flowering can make pollen fail, which can reduce fruit set in crops. This study built an automated system that photographs pollen grains growing in a dish and uses software to sort them into categories (dead, germinated, burst, growing tubes) and track individual tubes over time. The team applied it to hundreds of tomato types and found that heat sped up early germination but caused far more pollen to burst, with large differences between types.
- **Why it matters**: Pollen heat tolerance is a plausible link to yield loss in warming climates, and a method that can score hundreds of lines quickly makes it practical to look for the genes behind tolerance. The text does not show that any specific gene or breeding outcome was found, so the practical value is still to be tested.
- **Background needed**: - Pollen grains are the male cells that must germinate and grow a tube to reach the ovule; if this fails, the flower does not set fruit.
- Heat stress (here 34 °C versus 26 °C) can damage pollen; the paper measures this in a lab dish, not in whole plants.
- "Accessions" are distinct stored varieties or seed lines of a crop, and "wild relatives" are non-domesticated species related to it.
- Bright-field microscopy is ordinary light microscopy; automated "object detection" means software locates and labels each grain in the images.
- R² measures how closely automatic counts match manual counts (values near 1 mean close agreement).
- "Time to 50% germination" is how long it takes half the grains to start growing a tube.
- The "burst integral" is a combined score of how many grains burst and how early. · level: research-level

<details><summary>Original abstract</summary>

Scalable measurements of pollen function are needed to investigate genetic variation in reproductive responses to heat. We developed a high-throughput phenotyping framework integrating automated bright-field microscopy, object detection, individual-tube tracking, and temporal analysis. We quantified pollen performance at 26 and 34 C across 218 tomato accessions and wild relatives by analyzing approximately 300,000 images collected over two-hour growth periods. Automated counts of pollen classes - aborted pollen grains, ungerminated, germinated, and burst pollen grains, and pollen tube tips - agreed closely with manual counts (R2 = 0.915-0.967). Heat stress shortened the mean time to 50% germination from 24.0 to 20.5 minutes but increased mean percent bursting at 2 hours from 14.9% to 83.1%. A burst integral metric combined the extent and timing of bursting and revealed apparently substantial variation among accessions. Mean pollen tube length was shorter at 34 C than at 26 C in 72% of accessions and was equal or greater at 34 C in the remaining 28%. Individual-tube tracking revealed contrasting growth-speed distributions in representative thermosensitive and thermotolerant accessions, including persistence of faster-growing tubes in the thermotolerant Tamaulipas variety. This framework enables population-scale analysis of dynamic pollen traits and provides quantitative phenotypes for investigating the genetic basis of pollen thermotolerance.

</details>

### [Mitochondrial H2S and cytochrome c coordinate guard cell redox dynamics during stomatal immunity](https://www.biorxiv.org/content/10.64898/2026.11.20.768174v1)
*Pantaleno, R.; Scuffi, D.; Coronel, F. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.20.768174 v1 · relevance 0.05

- **In one sentence**: In Arabidopsis guard cells, the mitochondrial H2S source CAS-C1 and the electron carrier cytochrome c are shown to link H2S signalling and mitochondrial H2O2 to flg22-triggered stomatal closure, with CYTc persulfidated in vivo and cytc plants more susceptible to P. syringae pv. tomato hrcC- at early infection.
- **In plain words**: Plants defend themselves partly by closing tiny pores on their leaves, called stomata, to keep out microbes. This paper studies how the power plants inside those guard cells (mitochondria) help trigger that closure when the plant detects a bacterial signal. The authors found that a mitochondrial H2S-releasing compound and the bacterial signal flg22 both raised mitochondrial H2O2 within minutes, and that plants lacking cytochrome c did not close their pores properly and were more vulnerable to a bacterium in early infection.</plain>
<parameter name="why">It connects a gas-signalling molecule (H2S), energy-producing mitochondria and plant immunity in one pathway, which may matter for crop disease resistance. The text reports these as laboratory findings in one plant species and one bacterial strain, so how far they generalise to crops is not established here.
- **Background needed**: - Stomata: microscopic leaf pores, each flanked by two guard cells, that open and close to control gas exchange and block pathogen entry.
- flg22: a short piece of a bacterial protein that plants recognise as a warning sign (a PAMP, pathogen-associated molecular pattern).
- Mitochondria: the cell's energy-producing organelles; they maintain a membrane voltage (membrane potential) and transfer electrons along a chain.
- Cytochrome c: a small mobile protein that carries electrons between two steps of that chain.
- H2S (hydrogen sulfide) and H2O2 (hydrogen peroxide): small signalling molecules; H2S can modify proteins by adding sulfur groups (persulfidation).
- Redox biosensors: genetically encoded reporters that glow or change signal when the local oxidation state changes.
- Pseudomonas syringae: a bacterium that infects plants; hrcC- is a mutant strain lacking a working type III secretion system.</background>
<parameter name="difficulty">research-level

<details><summary>Original abstract</summary>

Stomatal pores modulate gas exchange between plants and the environment and are the first layer of defense against pathogens entry. Hydrogen sulfide (H2S) is a recognized component of the signalling network in guard cells that control stomatal responses. We previously showed that the mitochondrial H2S source {beta}-cyanoalanine synthase (CAS-C1) is required for flg22-induced stomatal closure. Using genetically encoded redox biosensors in Arabidopsis thaliana guard cells, we found that the mitochondrially-targeted H2S donor AP39 and the pathogen-associated molecular pattern (PAMP) flg22 both increased mitochondrial H2O2 within 5 min, while the flg22-triggered rise was attenuated in cas-c1 mutants. Dissipating the mitochondrial membrane potential ({Delta}{psi}m) with the uncoupler 2,4-dinitrophenol prevented both mitochondrial oxidation and stomatal closure. Cytochrome c (CYTc), the mobile electron carrier between complexes III and IV, proved essential for this pathway. CYTc-deficient lines showed a stomatal response similar than wild-type (wt) to ABA and light but failed to trigger stomatal closure upon exposure to different PAMPs. In these plants, neither AP39 nor flg22 induced guard cell mitochondrial hyperpolarization or an increase in cytosolic H2O2. By the dimedone-switch method, we show that CYTc is persulfidated in vivo, identifying this respiratory protein as a target of H2S-mediated posttranslational modification. At the whole-plant level, cytc plants were more susceptible to spray inoculation with Pseudomonas syringae pv. tomato hrcC- at early stages of infection. Together, these results position CYTc as a mitochondrial node that links H2S signalling to guard cell redox dynamics during stomatal immunity.

</details>

## Bioengineering and synthetic biology

### [Synthesis of Plasma Membrane-Enriched Nanodiscs from Giant Plasma Membrane Vesicles](https://www.biorxiv.org/content/10.64898/2026.11.20.768238v1)
*Jacobs, C. O.; Santee, R. R. S.; Pizarro Carbajal, B. S. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.20.768238 v1 · relevance 0.05

- **In one sentence**: The paper describes a method for making plasma membrane-enriched nanodiscs (PMNDs) from giant plasma membrane vesicles (GPMVs), reporting that they keep membrane-anchored proteins, have uniform size and shape, and bind dose-dependently to cells expressing a matching receptor.
- **In plain words**: Cells are wrapped in an outer skin called the plasma membrane, which carries many of the proteins that let cells sense and interact with their surroundings. This paper describes a way to turn large pieces of that skin, collected as giant vesicles, into tiny disc-shaped fragments called nanodiscs that keep their native proteins. The authors report that these fragments stay intact in size and shape and bind specifically to cells that carry the matching receptor.
- **Why it matters**: Existing ways of isolating the cell's outer membrane mix it with many other membranes, so the material is hard to define. A cleaner, membrane-enriched nanodisc could help researchers study how drugs, particles or vaccine components attach to real cell surfaces. The text is a short abstract, so the extent of testing and the possible applications beyond the stated ones are not clear from it.
- **Background needed**: - Plasma membrane: the thin outer layer of a cell, studded with proteins that receive signals and handle exchange with the outside.
- Membrane proteins (MPs): proteins embedded in that layer; many are drug targets.
- Nanodisc: a tiny, soluble disc of lipid (fat) bilayer held together by a scaffold, used to keep membrane proteins in a water-based setting.
- Giant plasma membrane vesicles (GPMVs): large bubbles pinched off from living cells' outer membrane, used as a convenient membrane source.
- Dose-dependent binding: the amount of binding rises as more of the material is added, a standard sign of a real interaction.
- Cognate receptor: the matching cell-surface protein that a given ligand or particle is designed to recognize. · level: research-level

<details><summary>Original abstract</summary>

Nanodiscs are highly versatile biomaterials with applications in cell membrane mimicry, membrane protein (MP) characterization, and hybrid biological-abiological material synthesis. The plasma membrane (PM) is an ideal starting material for nanodisc synthesis because it naturally houses a diverse array of functionally important MPs in their native lipid environment. However, the PM comprises a small fraction of the total membrane material in a typical eukaryotic cell. Traditional methods to isolate the PM suffer from undefined relative PM enrichment compared to other cellular membranous structures. Here, we introduce a method to synthesize PM-enriched nanodiscs (PMNDs) from giant plasma membrane vesicles (GPMVs). We show that GPMV-derived PMNDs retain functional membrane-anchored protein, exhibit uniform size and morphology, and bind specifically and dose-dependently to the PM of cells expressing a cognate receptor. This strategy offers broad applicability for synthesizing nanodiscs with novel MPs for investigating PM-nanomaterial interactions, cellular targeting, and vaccine development using immunologic MPs.

</details>

### [EEG Source Localization with High-Resolution 40-Tissue Head Models: A Comparative Study with MEG during Photic Driving](https://www.biorxiv.org/content/10.64898/2026.11.20.768219v1)
*Nunez Ponasso, G.; Drumm, D. A.; Oppermann, H. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.20.768219 v1 · relevance 0.05

- **In one sentence**: The paper presents a BEM-FMM pipeline that computes EEG leadfields on AI-segmented 40-tissue head models and compares the resulting visual-cortex source localizations against 5-layer models and simultaneous MEG during photic driving in six participants.
- **In plain words**: Brain signals can be recorded from the scalp (EEG) or from magnetic fields just outside the head (MEG), and researchers must build a computer model of the head to work out where in the brain those signals come from. This paper tests a more detailed head model, built from 40 separate tissue types by an AI segmentation tool, against the simpler models usually used for EEG. In six people flashed with light at a rhythm tied to their alpha brain rhythm, the detailed and simpler models gave very similar EEG locations, and both roughly agreed with the MEG locations in the visual cortex.
- **Why it matters**: It shows that a more realistic, non-nested head model can be used practically for EEG source localization, with reported run times of about 4.5 minutes per channel on a single modest workstation. The authors suggest it may matter for infants or patients with skull defects, injuries, or tumors, where layered models do not fit the anatomy, but the text does not test those groups.
- **Background needed**: - EEG: electrodes on the scalp recording electrical activity from the brain.
- MEG: sensors outside the head recording the tiny magnetic fields from brain activity.
- Source localization: estimating where in the brain a signal originates, which depends on a model of the head.
- Head model: a computer mesh of tissues (skin, skull, brain, etc.) with assigned electrical conductivities; "5-layer" models are simpler than the 40-tissue model.
- Leadfield: a matrix linking each brain source to each sensor reading.
- Boundary element method (BEM-FMM): a numerical technique for computing electric fields across tissue boundaries efficiently.
- Photic driving: a brain response to rhythmic flashing light, used here at half each person's alpha peak frequency.
- Alpha peak frequency: the dominant rhythm of resting brain activity, typically around 8–12 Hz.
- Fixed-orientation source: a model where each source has a set direction, so its direction (normal) must be accurate. · level: research-level

<details><summary>Original abstract</summary>

While MEG source localization pipelines often employ head models of one single compartment with homogeneous conductivity, researchers and clinicians use at least 3 different layers in head models for EEG source localization. Recent AI-based segmentation makes it possible to generate individualized head models with 40 high-resolution, non-nested tissues. We present a pipeline that can make use of, and test, these highly realistic models for EEG source localization: with the boundary element fast multipole method (BEM-FMM), we compute transcranial electric stimulation (TES) solutions on the full 40-tissue geometry and use them reciprocally to obtain the EEG leadfields. Out approach runs on a single modest workstation, requiring approximately 4.5 min per EEG channel for a mesh of about one million elements at a relative residual of 1e-4. We applied the pipeline to six participants undergoing intermittent photic stimulation at half their individual alpha peak frequency, comparing 61-channel EEG source localizations from 40-tissue and 5-layer models with each other and with localizations from simultaneously recorded MEG. We further compared noiseless synthetic EEG topographies of the two models across the entire cortex. The two models produced highly consistent EEG source localizations (weighed relative difference below 3%), both in close agreement with the MEG localizations within the visual cortex. The synthetic topographies also agreed closely, with differences scaling approximately linearly with the angle between the source orientations of the two models, underscoring the importance of accurate source normals in fixed-orientation source models. These results establish 40-tissue models as a practical and robust basis for EEG source localization, and open the way to applications where nested geometries cannot represent the anatomy, such as infants or patients with skull defects, injuries, or tumors.

</details>

## Mathematical biology (arXiv)

### [LeCellModel: Interpretable Density Estimation over the Gene Expression Manifold](https://arxiv.org/abs/2611.30955)
*Gil Karin, Artemii Bakulin, Nir Yosef* · `q-bio.GN` · arXiv:2611.30955v1 · relevance 0.10

- **In one sentence**: LeCellModel uses the log-volume of a JEPA encoder's Jacobian (JEPA-SCORE) under an isotropic Gaussian latent as a typicality score for single-cell RNA-seq density estimation, rare-state detection, and gene-level attribution.
- **In plain words**: The paper asks whether machine-learned summaries of single-cell gene activity should be judged by how well they capture how cells are distributed across possible states, not just by whether they separate known cell types. The authors build a model on a recent self-supervised method (LeJEPA) and use a local stretching measure of its encoder as a "how typical is this cell" score. They report better results than established methods on a standard benchmark, detection of rare stimulated cells in a controlled experiment, and two biology findings that they say arise from the embedding alone.
- **Why it matters**: It proposes treating the shape of the cell-state distribution as the main training goal, and offers per-gene explanations of the typicality score, which could help interpret rare or disease-linked cell populations. The text does not establish how broadly these results hold beyond the datasets described, so the claims should be read as preliminary.
- **Background needed**: - Single-cell RNA-seq measures gene activity in individual cells, giving a high-dimensional profile per cell.
- An "embedding" is a compressed numerical summary of each cell learned by a neural network encoder.
- A "manifold" is the lower-dimensional curved surface that real cell profiles tend to lie on.
- Density estimation means estimating how likely or common a given kind of cell state is.
- JEPA (joint-embedding predictive architecture) is a self-supervised learning approach; SIGReg is a regularizer that pushes the latent space toward an isotropic Gaussian shape.
- The Jacobian measures how small input changes stretch the encoder's output; its log-volume here serves as a local density-like score.
- scIB is a standard benchmark for judging how well single-cell embeddings preserve biology and remove batch effects.
- Idiopathic pulmonary fibrosis is a chronic lung scarring disease; regulatory T cells are an immune cell type. · level: research-level

<details><summary>Original abstract</summary>

Representation learning for single-cell RNA-seq has been evaluated by the identities representations capture -- cell types, lineages, perturbations -- rather than how faithfully they model the distribution of cell states on the gene expression manifold. As a result, density estimation, rare-state detection, perturbation scoring, and gene-level attribution are bolted onto frozen embeddings as separate models, disconnected from the geometry of the data. We argue that modeling the distribution of cell states should be the primary objective, and that representation quality follows from it. Building on LeJEPA, whose SIGReg objective enforces a provably optimal isotropic Gaussian latent, we introduce LeCellModel, which reads the encoder's Jacobian log-volume (JEPA-SCORE) under this Gaussian latent as a relative typicality score. Across several datasets, LeCellModel outperforms established methods on the scIB benchmark for representation quality. Furthermore, we show that LeCellModel enables detection of rare expression states using JEPA-SCORE as a typicality measure, applying it to a controlled cytokine panel, where it identifies stimulated cells across minority fractions and tracks pathway-response magnitude. We introduce gene-level interpretability of the typicality score -- to our knowledge, the first method for analyzing JEPA-SCORE in feature space. Leveraging this framework, LeCellModel recapitulates the known association of a profibrotic macrophage program with idiopathic pulmonary fibrosis, and discovers a CD177+ activated regulatory T cell subpopulation previously described only in tumor contexts. Both findings emerge directly from the geometry of the learned embedding, without relying on supervised annotations.

</details>

### [Introduced cases, spread of infection in a community and travel control measures](https://arxiv.org/abs/2611.29584)
*Julien Arino, Clotilde Djuikem, Amy Hurford* · `q-bio.PE` · arXiv:2611.29584v1 · relevance 0.09

- **In one sentence**: A coupled Exporter–Importer epidemic model (deterministic ODEs plus stochastic Markov chain and branching-process approximations) analyses how timing and combinations of travel screening, quarantine and travel interruptions affect introduced SARS-CoV-2-type outbreaks in a destination community.
- **In plain words**: During COVID-19, many places used travel bans, border testing and quarantine to slow the spread of the virus between regions, but their results varied widely. This paper builds a mathematical model of two linked populations, the sending and receiving regions, to test how the timing and mix of these border measures interact with infected travellers arriving and spreading the disease locally.
- **Why it matters**: The paper's main claims are that screening only at departure cannot stop outbreaks in a receiving community whose reproduction number exceeds one, and that border triggers based on surveillance in the sending region act earlier than triggers based on local detections. These are model-based findings, and the text does not show how well they match real data, so they are best read as analytical guidance rather than established policy evidence.
- **Background needed**: - Reproduction number (R): the average number of new infections caused by one case; above 1 an outbreak can grow, below 1 it tends to die out.
- Compartmental model: a set of equations that sorts people into groups such as latently infected (infected but not yet infectious), detected infectious, and undetected infectious.
- Stochastic models: random-chance versions of the model, useful when only a few infections are introduced, where chance matters a lot.
- Branching process: a standard random model of how a small number of cases produce offspring cases, used to estimate the chance an outbreak dies out.
- Final epidemic size and attack rate: the total share of a population infected by the end of an outbreak.
- Exporter/Importer: the origin region sending travellers and the destination region receiving them. · level: research-level

<details><summary>Original abstract</summary>

Travel restrictions, border screening and quarantine were widely used during the COVID-19 pandemic to prevent or delay the spatial spread of SARS-CoV-2, yet their effectiveness varied greatly across jurisdictions. To investigate how the timing and combination of border control measures interact with pathogen introductions and local transmission, we formulate a coupled Exporter--Importer epidemic model in both deterministic (ordinary differential equations) and stochastic (continuous-time Markov chain and multitype branching process approximation) frameworks. The model distinguishes latently infected, detected infectious and undetected infectious individuals, and explicitly separates recently arrived travellers in an introduction layer from the destination community. We derive analytical expressions for the control and basic reproduction numbers, final epidemic sizes and probabilities of outbreak extinction, and complement them with stochastic simulations. We show that pre-departure screening in the Exporter alone cannot prevent outbreaks in an Importer community with reproduction number larger than unity because latently infected travellers cross borders undetected. Post-arrival quarantine and screening in the introduction layer, as well as travel interruptions, can substantially reduce the attack rate in the Importer, but only when implemented with high stringency and triggered early. Triggering border interventions based on local detections in the Importer almost always acts too late because silent introductions precede local case detection, whereas triggers informed by surveillance in the Exporter provide a wider window of action. Effective protection of the Importer ultimately requires combining proactive, Exporter-informed border measures with local public health interventions that keep the community reproduction number near or below one.

</details>

## Epidemiology

### [Epidemiology of Cardiac Structure and Function Among African Caribbeans in Tobago: A Population-based Cohort Study](https://www.medrxiv.org/content/10.64898/2026.11.18.26368418v1)
*Deb Nath, N.; Miljkovic, I.; Katz, R. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.18.26368418 v1 · relevance 0.07

- **In one sentence**: A population-based echocardiography study of 924 African Caribbean adults in Tobago describing the prevalence of left ventricular structural abnormalities, diastolic dysfunction, and reduced systolic and strain measures, stratified by sex, age, and heart failure stage.
- **In plain words**: Heart failure often develops after the heart's walls thicken or its filling and pumping function start to change, and people of African ancestry are at higher risk for it. This study scanned the hearts of 924 adults in Tobago using ultrasound (echocardiography) to see how common these early changes are. It found that most participants had an abnormal heart shape or thickened walls, and that women and older adults had more of these structural problems and filling difficulties than men and younger adults.
- **Why it matters**: Little was previously known about heart structure and function in people of African Caribbean descent in Tobago, so these prevalence figures give local health planners a baseline. The sex and age patterns may help guide cardiovascular prevention priorities, though the text does not show whether these findings change outcomes or care.
- **Background needed**: - Heart failure: the heart does not pump or fill well enough to meet the body's needs.
- Echocardiography: an ultrasound scan of the heart.
- Left ventricle: the main pumping chamber; "LV mass index" measures how much muscle it has, relative to body size.
- Concentric remodeling: the heart wall thickens without the chamber enlarging, a common early change linked to high blood pressure.
- Diastolic dysfunction: stiffness that makes the heart fill poorly between beats.
- Ejection fraction (LVEF): the share of blood pumped out each beat; below 50% is generally considered reduced.
- Global longitudinal strain (GLS): a measure of how much the heart muscle stretches and squeezes; less negative values indicate weaker function.
- E/e' ratio and E/A ratio: ultrasound-based estimates of filling pressure and filling pattern.
- Stages A–C of heart failure: A is at risk without symptoms, B has structural changes without symptoms, C has symptoms.
- Population-based cohort: a study drawing a general community sample rather than hospital patients. · level: intermediate

<details><summary>Original abstract</summary>

BackgroundIndividuals of African genetic ancestry are at high risk for heart failure (HF), which is often preceded by cardiac structural and functional abnormalities. Nevertheless, little is known about cardiac structure and function among Afro-Caribbeans residing in Tobago. This study aimed to investigate the epidemiology of cardiac structure and function among African Caribbeans in Tobago. MethodsA total of 924 participants (41-83 years) underwent clinical evaluation and transthoracic echocardiography. Images were analyzed for left ventricular (LV) mass index (MI), left atrial volume index, diastolic dysfunction (DD), LV ejection fraction (LVEF), global longitudinal strain (GLS), E/e' ratio, E/A ratio, and other echocardiographic measures. Cardiac structure and function were evaluated by age, sex, and HF stage. ResultsThe mean age was 61.7 years, with 61.4% women, 47.8% obesity, and 20.2% diabetes. Average systolic blood pressure was approximately 140 mmHg, and 76.7% had hypertension. Abnormal LV geometry was present in 77.1% of participants, predominantly concentric remodeling (69.5%). The prevalence of DD was 13.4%, LVEF <50% was 1.5%, and abnormal GLS ([&le;]-18%) was 5.2%. Women had significantly higher E/e' ratios and a higher prevalence of Stage A and Stage B HF, whereas men had a higher prevalence of symptomatic (Stage C) HF. Participants aged 65-83 years had significantly higher E/e' ratio, concentric remodeling, and LV hypertrophy than those aged 41-57 years. ConclusionsWomen and older adults have higher LV structural abnormalities and DD than men and younger adults. These results will be helpful to inform public health priorities related to cardiovascular health in Tobago.

</details>

### [Improving UK Biobank algorithms for Parkinson's disease ascertainment using drug claims](https://www.medrxiv.org/content/10.64898/2026.11.18.26368409v1)
*Kimmerling, V.; Jaber, E.; Proust-Lima, C. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.18.26368409 v1 · relevance 0.06

- **In one sentence**: Compares three ways of identifying Parkinson's disease cases in UK Biobank (hospital/death records, GP diagnoses, and a new drug-prescription-based algorithm) and how each choice changes incidence estimates and associations with sex, walking speed and mortality.
- **In plain words**: Researchers using a large UK health database often need to know which people have Parkinson's disease, but the database does not record this cleanly. This paper tests three ways of spotting cases: using hospital and death records, using family doctor diagnoses, and using a new method based on anti-Parkinson drug prescriptions. The authors found that the hospital-and-death-records approach missed about 20% of cases compared with the drug-based method and underestimated incidence by 36% against UK reference rates.
- **Why it matters**: Choices about how cases are identified can change study results, so this matters for anyone analysing Parkinson's risk factors in UK Biobank. The text does not show how far the drug-based method will hold up in other datasets, and it reports only the comparisons summarised in the abstract.
- **Background needed**: - UK Biobank: a large research database of health records and measurements from roughly half a million UK volunteers.
- Ascertainment: working out who has a condition, based on the records available.
- Misclassification: counting people with the wrong status, e.g. missing true cases or including people with similar conditions.
- Incidence: the rate of new cases over time.
- Parkinsonism: a group of movement symptoms that can have causes other than Parkinson's disease.
- Primary care data: records from family doctor (general practitioner) visits, available for only about 45% of participants here.
- Anti-PD drugs: medications such as levodopa commonly prescribed for Parkinson's; prescription records can hint at a diagnosis earlier than hospital records do. · level: intermediate

<details><summary>Original abstract</summary>

Background: Accurate ascertainment of Parkinson's disease (PD) is a major challenge in large-scale epidemiological studies. The UK Biobank (UKB) is widely used for PD research, but ascertainment based on hospital and death records may result in misclassification and delayed PD diagnoses. Objectives: We compared different strategies for ascertaining PD in the UKB, and examined their impact on incidence and associations with risk factors and mortality. Methods: We compared PD ascertained through hospital and death records (ADO-PD) to two approaches that rely on primary care data available for ~45% of participants: diagnoses from general practitioner consultations (Clinical-PD); a novel drug-based algorithm (Drug-PD). We compared incidence, age at diagnosis, and associations with sex, walking speed, and mortality across all algorithms. Results: ADO-PD identified ~20% fewer prevalent and incident cases than Drug-PD over 15y of follow-up, and estimated age at diagnosis to be 4.2y (median) later than age at anti-PD drugs initiation. ADO-PD identified never treated participants or with other causes of parkinsonism as PD patients. While Drug-PD yielded incidence rates consistent with UK reference rates, ADO-PD underestimated incidence by 36% compared to reference rates. Associations with sex, walking speed, and mortality were significantly different for ADO-PD compared to Drug-PD. Clinical-PD and Drug-PD yielded similar findings, although Clinical-PD included patients with other causes of parkinsonism. Conclusions: We draw attention to methodological issues regarding PD ascertainment in the UKB and their consequences. These results can help inform strategies for PD ascertainment by combining multiple data sources, thereby improving the validity of epidemiological analyses.

</details>

## Infectious diseases

### [Pre-conception PfSPZ Vaccine administration to Malian women prevents malaria in their offspring during infancy](https://www.medrxiv.org/content/10.64898/2026.11.19.26368501v1)
*Diawara, H.; Healy, S. A.; Wang, J. et al.* · `infectious diseases` · medRxiv doi:10.64898/2026.11.19.26368501 v1 · relevance 0.06

- **In one sentence**: A randomized, placebo-controlled trial in Mali testing whether pre-conception PfSPZ malaria vaccination of women reduces parasitemia and clinical malaria in their infants during the first year of life.
- **In plain words**: Malaria is especially dangerous for babies and pregnant women, and protecting infants is hard. In this trial in Mali, healthy women were given either a malaria vaccine (at one of two doses) or saline before they became pregnant, and their babies were then tracked for malaria during the first year of life. In the lower-dose vaccine group, far fewer infants had malaria parasites in their blood or clinical malaria than in the saline group, while the higher-dose group did not show a significant effect.
- **Why it matters**: Protecting infants through a vaccine given to mothers before pregnancy would be a new approach if it holds up, which is why it merits attention. The sample is small (104 infants, with wide confidence intervals), and the higher-dose group did not show a significant benefit, so the result should be read as promising rather than settled.
- **Background needed**: - Malaria is caused by Plasmodium parasites, spread by mosquitoes; Plasmodium falciparum is the most dangerous species.
- PfSPZ Vaccine is made of live but attenuated (weakened) parasite sporozoites, the stage that enters the body from a mosquito bite.
- "Pre-conception" means given before pregnancy begins.
- "Parasitemia" means malaria parasites detected in the blood, often via a blood smear under a microscope.
- "Vaccine efficacy (VE)" is the percentage reduction in cases among vaccinated versus control groups; a wide confidence interval (CI) means the estimate is uncertain.
- Placebo-controlled and double-blind means neither participants nor researchers knew who got the real vaccine.
- PfCSP antibodies are immune proteins against the parasite's circumsporozoite protein, measured as a sign of immune response. · level: intermediate

<details><summary>Original abstract</summary>

Background: Preconception administration of Plasmodium falciparum sporozoite (PfSPZ) Vaccine is safe and prevents malaria during pregnancies identified within 21 months post-vaccination. We evaluated pre-conception PfSPZ Vaccine effects on malaria risk in offspring during the first year of life. Methods: In a randomized, double-blind, placebo-controlled trial in Ouelessebougou, Mali, 300 healthy 18-38-year-old women were allocated 1:1:1 to receive 9x10^5 PfSPZ or 1.8x10^6 PfSPZ of PfSPZ Vaccine or normal saline on days 1-8-29, and followed up to 21 months for malaria endpoints and pregnancies. 104 infants from 103 pregnancies identified first year post-vaccination [9x10^5 PfSPZ (n=38); 1.8x10^6 PfSPZ (n=40); normal saline (n=26)] were seen every two months and during illnesses. Primary endpoints were blood-smear parasitemia and clinical malaria. Safety outcomes included newborn baseline characteristics and infant adverse events (AEs). Findings: Newborn baseline characteristics and infant AEs did not differ between arms; AEs were common but predominantly mild (91.9-96% Grade 1). Vaccine efficacy of 9x10^5 PfSPZ was 75.1% (95% CI 20.6-92.2) against parasitemia (10.5% parasitemic infants versus 38.5% of placebo) and 94.2% (54.9-99.3) against clinical malaria (2.6% malarious infants versus 38.5% of placebo). VE of 1.8x10^6 PfSPZ group was 40.3% (-43.6-75.2) against parasitemia and 36.3% (-50.3-73.0) against clinical malaria, both non-significant. At 6 and 12 months of age, PfCSP antibodies were similar in offspring of vaccinated and control mothers. Interpretation: Pre-conception PfSPZ Vaccine was safe and reduced Pf infection and clinical malaria during infancy in 9x10^5 PfSPZ group. Further development of preconception PfSPZ vaccines is warranted to protect mother-infant dyads.

</details>

## Public and global health

### [Partitioning lifespan inequality in hierarchical study designs with an application to global healthy longevity](https://www.medrxiv.org/content/10.64898/2026.11.22.26368689v1)
*Caswell, H.* · `public and global health` · medRxiv doi:10.64898/2026.11.22.26368689 v1 · relevance 0.09

- **In one sentence**: The paper proposes a variance-partitioning method for hierarchical study designs, splitting lifespan inequality into between-region, between-country-within-region, and within-country components, and applies it to healthy longevity data for 194 countries from the Global Burden of Disease study.
- **In plain words**: Some people die at very different ages, and part of that spread comes from differences between groups (such as countries) and part from pure chance among people who face the same risks. This paper offers a way to split the total spread in lifespans into layers: differences between large regions, differences between countries within those regions, and chance variation within each country. The authors apply it to healthy-life data for 194 countries grouped by World Bank income category.
- **Why it matters**: It gives researchers a systematic way to say how much of global inequality in healthy longevity lies in regional gaps versus chance, which matters for judging where health policy can reduce differences. The text does not show how the method performs against alternatives, so its practical reach is best treated as a methods contribution pending further use.
- **Background needed**: - Lifespan inequality: how much individuals' ages at death vary around the average.
- Variance: a standard measure of spread; larger variance means more variation.
- Mixture distribution: a population made of subgroups, each with its own rate, combined into one overall distribution.
- Hierarchical design: data nested in layers, such as people within countries within regions.
- Variance partitioning: splitting the total variance into parts attributable to each layer and to chance.
- Global Burden of Disease (GBD): a large international database of health measures.
- Healthy longevity: years lived in good health, as estimated in that database.
- Flat vs. population-weighted mixing: whether each country counts equally or in proportion to its population when combining them. · level: research-level

<details><summary>Original abstract</summary>

Background: Demographic inequality arises from two sources: heterogeneity among individuals subject to different rates, and stochastic variation among individuals subject to identical rates. Partitioning lifespan inequality into these components has been limited to heterogeneity in single factors or, very recently, factorial study designs with multiple factors. Methods for hierarchical designs have been lacking. Objectives: The goal of this paper is to present a generally applicable method to partition inequality of lifespan (and other demographic outcomes) into components within and between levels in a hierarchical study design. Methods: The analysis treats a heterogeneous population as a mixture distribution. Inequality is measured by the variance and partitioned into components between groups (e.g., geographical or economic regions), between sub-groups within groups (e.g., countries within regions), and stochasticity within sub-groups. The method is applied to global inequality in healthy longevity, using data for 194 countries from the Global Burden of Disease study, divided into four regions according to the World Bank income categories and into countries within each region. Results are compared for flat and population-weighted mixing distributions. Results: The protocol for variance partitioning in hierarchical study designs provides variance among regions, among countries within regions, and within countries. It extends naturally to multiple levels (e.g., states within countries) and to factorial components (e.g., regions defined by combinations of income and education). When applied to global healthy longevity, the dominant source of inequality is stochastic variation within countries, which accounts for 85\%-95\% of the overall inequality. The population-weighted mixing distribution reduces the contribution of between-group variance. Contribution: Some of the largest demographic data sets have a hierarchical organization. The methods presented here make it possible to partition inequality, measured by variance, in such studies.

</details>

### [Knowledge of antimicrobial Resistance in Bangladeshi Caregivers of School-going Children: A Cross-sectional study.](https://www.medrxiv.org/content/10.64898/2026.11.21.26368630v1)
*Chowdhury, R. T.; Asamoni, U. H.; Raiyan, R. et al.* · `public and global health` · medRxiv doi:10.64898/2026.11.21.26368630 v1 · relevance 0.07

- **In one sentence**: A cross-sectional survey of 225 Bangladeshi caregivers of school-going children examining their knowledge of antimicrobial resistance, antibiotic use habits, and information sources, with socio-demographic differences in knowledge.
- **In plain words**: Antibiotics are medicines that fight bacteria, and overusing them lets bacteria evolve so the drugs stop working; this is called antimicrobial resistance (AMR). In this study, researchers asked 225 caregivers of school-age children in Bangladesh what they knew about AMR and how they use antibiotics. They found many gaps: for example, only 35% knew antibiotics do not work against viral infections, and 30% stopped antibiotic courses early.
- **Why it matters**: Misuse of antibiotics is one of the main drivers of drug resistance, which makes common infections harder to treat worldwide. The paper gives a snapshot of one group in one country, so it is best read as a local picture that may help shape education and prescribing policy rather than as a general measure of the problem.
- **Background needed**: - Antibiotics kill bacteria but do not work against viruses (such as colds or flu).
- Antimicrobial resistance (AMR): bacteria become able to survive drugs meant to kill them, so infections become harder to treat.
- Self-medication: taking medicine without a doctor's prescription, often on a pharmacist's advice or from an old prescription.
- Cross-sectional study: a one-time survey of a group at a single point in time; it shows associations, not cause and effect.
- Socio-demographic factors: characteristics such as education, location (urban or rural), and household wealth.
- p<0.05: a statistical threshold suggesting a difference is unlikely to be due to chance alone.
- The text gives no details on how caregivers were chosen, the questionnaire itself, or the exact size of the group differences. · level: introductory

<details><summary>Original abstract</summary>

Antimicrobial resistance (AMR) is a critical global health threat exacerbated by inappropriate antibiotic use, yet evidence on caregivers' awareness and practices in Bangladesh remains limited. This cross-sectional study assessed AMR awareness, antibiotic use practices, and information sources among 225 caregivers using a structured questionnaire that also captured socio-demographic characteristics. Understanding of AMR was poor: although 78% recognized that antibiotics are effective against bacterial infections, only 35% acknowledged that they are ineffective against viral infections. Regarding practices, 30% discontinued antibiotic courses prematurely and 40% reported self-medication, primarily guided by pharmacy advice (45%) or previous prescriptions (30%). Healthcare professionals were the leading source of information (55%), followed by media (30%) and community programs (15%). Knowledge differed significantly across socio-demographic groups, with higher awareness among caregivers who were more educated, urban-dwelling, and from wealthier households (p<0.05). These findings reveal a substantial gap between AMR knowledge and antibiotic practices, particularly regarding misuse for viral infections, premature cessation, and self-medication. Targeted educational interventions, stronger enforcement of prescription regulations, and improved healthcare access are urgently needed, and behavioral interventions should address both knowledge deficits and practical barriers to help curb AMR in Bangladesh.

</details>

## Psychiatry and neurology

### [Disease-specific versus symptom-specific neuroimaging phenotypes across Alzheimer's Disease, Parkinson's Disease, and Small Vessel Disease](https://www.medrxiv.org/content/10.64898/2026.11.16.26368132v1)
*Lazari, A.; Broulidakis, J.; Gillis, G. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.16.26368132 v1 · relevance 0.15

- **In one sentence**: A case-control and transdiagnostic MRI study of 251 people with Alzheimer's, Parkinson's, small vessel disease, or healthy age-matched controls, using the UK Biobank imaging protocol, linking disease-specific and shared brain changes to symptoms such as apathy, fatigue, depression and cognitive deficits.
- **In plain words**: Several brain diseases that develop with age, including Alzheimer's, Parkinson's and small vessel disease, share symptoms like memory problems, low mood and tiredness. This study scanned 251 people with these conditions and healthy older adults using one standard brain-scan protocol, and compared their brain features. The authors found that each disease has some distinct brain changes, but also many changes that overlap across diseases.
- **Why it matters**: Shared symptoms are common across these conditions, and the study suggests that a few brain connections may be linked to particular symptoms regardless of diagnosis. This could help explain symptom variation in older people, but the findings come from a modest sample and would need confirmation in larger, independent studies before they guide care.
- **Background needed**: - Neurodegenerative disorders: diseases where brain cells or their connections gradually lose function, such as Alzheimer's and Parkinson's.
- Small vessel disease: damage to the tiny blood vessels deep in the brain, often seen on scans as white matter lesions.
- Case-control comparison: comparing people with a condition against similar people without it.
- Transdiagnostic: a pattern that cuts across diagnostic labels rather than belonging to one disease.
- MRI measures: brain volume, white matter microstructure (how well the wiring is organised), tract volume, iron content, and functional connectivity (how regions activity is synchronised at rest).
- UK Biobank protocol: a standardised brain-imaging method from a large UK population study, so results can be compared across groups.
- Medial frontal pole and cingulum: a front-middle brain region and a fibre bundle running along the inner brain; the paper links these to symptoms. · level: research-level

<details><summary>Original abstract</summary>

Background: Neurodegenerative disorders are common in ageing populations, and arise from several distinct pathophysiological causes. Yet, they also share many symptoms, including cognitive and neuropsychiatric ones. It is unclear to what extent the impact of neurodegeneration on brain systems is unique or shared across disorders, and whether shared symptoms are driven by degeneration of the same brain systems. Methods: We collected data from n=251 participants with Alzheimer's Disease, Parkinson's Disease, Small Vessel Disease, and age-matched healthy controls. All participants underwent harmonized cognitive and neuropsychiatric assessment and were scanned using the UK-Biobank MRI protocol capturing features including brain volume, white matter lesions and microstructure, tract volume, iron content, and functional connectivity. Results: We replicated established case-control brain changes in Alzheimer's Disease, Parkinson's Disease and Small Vessel Disease compared to healthy controls. Leveraging this joint standardised dataset, we identified distinct neuroimaging features of individual neurodegenerative disorders, providing evidence for robust diagnosis-specific brain changes. Importantly, however, there was also a large degree of transdiagnostic similarity across neuroimaging markers. Testing for transdiagnostic associations between symptoms and brain phenotypes, we found that lower medial frontal pole connectivity to primary motor cortex was preferentially associated with apathy, fatigue, and depression; whereas cingulum microstructure was associated with cognitive deficits across diagnoses. Conclusions: These results demonstrate that different neurodegenerative diseases are characterised by dissociable brain changes, but also common transdiagnostic and symptom-associated features. This suggests that shared symptoms across neurodegeneration may in part be driven by overlapping impact on key brain systems, such as changes in medial frontal pole connectivity and cingulum microstructure. Our work highlights that multimodal imaging biomarkers can help understand and parse symptomatic heterogeneity in neurodegenerative and ageing populations.

</details>

### [Geographic heterogeneity of gut microbiome biomarkers across neurological conditions: sub-national discordance in ten cohorts from eleven cities in six countries](https://www.medrxiv.org/content/10.64898/2026.11.19.26368539v1)
*Tello Meryk, J.* · `neurology` · medRxiv doi:10.64898/2026.11.19.26368539 v1 · relevance 0.13

- **In one sentence**: Reanalysis of ten public 16S rRNA gene sequencing cohorts (Alzheimer's, Parkinson's and autism; 1,185 samples from eleven cities in six countries) showing that gut microbiome classifiers trained in one cohort transfer poorly to another, even between recruitment sites within a single city pair.
- **In plain words**: Researchers have proposed that certain gut bacteria could serve as signs of brain conditions such as Alzheimer's, Parkinson's and autism. This paper asks whether those signs hold up in other groups of people, and it reprocessed public gut-bacteria datasets from many cities to test this. Models that worked reasonably well inside their own dataset became close to guesswork when applied to a different population, and the drop did not depend on how far apart the places were.
- **Why it matters**: It bears directly on whether gut microbiome tests could ever be used as diagnostic tools, and it suggests that signatures from a single study may not generalize even across nearby sites. The text does not show how this would translate into clinical practice, so the implications for diagnosis remain uncertain.
- **Background needed**: - The gut microbiome is the community of bacteria living in the intestine; 16S rRNA sequencing is a common, relatively inexpensive way to identify which bacterial groups (taxa) are present.
- A "biomarker" here means a set of bacterial features used to tell apart people with and without a condition.
- Machine-learning classifiers are models trained on one dataset and scored on held-out data; AUC (area under the curve) measures discrimination, where 0.5 is no better than chance and 1.0 is perfect.
- "Transfer" means training on one cohort and testing on a different one, the key test of whether a signature generalizes.
- A "cohort" is a group of study participants recruited in a particular way, and cohort-specific differences (diet, medication, lab protocol, local environment) can confound results.
- Feature rankings compare which bacterial taxa a model relies on most; the paper reports these rankings did not agree across cohorts. · level: research-level

<details><summary>Original abstract</summary>

Gut microbiota composition has been associated with multiple neurological conditions, and candidate biomarkers have been proposed on the basis of these associations. Their usefulness presupposes that taxa altered in one population are also altered in others, a condition that is rarely verified. This work quantifies the extent to which it holds, and the geographic scale at which it ceases to do so. Ten public 16S rRNA gene sequencing cohorts of Alzheimer's disease, Parkinson's disease and autism spectrum disorder, collected in eleven cities across six countries, were reprocessed from raw data, comprising 1,185 samples with uniform processing within each condition. Models trained and evaluated within a single cohort reached a mean AUC of 0.751 in Alzheimer's disease, 0.741 in autism spectrum disorder and 0.673 in Parkinson's disease. When applied to a different population, these values fell to 0.569, 0.542 and 0.551 respectively. The decline was not associated with geographic distance: transfer between cities within the same country was equivalent to transfer between continents. No taxon appeared among the twenty most important features in all cohorts of a given condition, and no correlation between rankings reached significance. Classifiers trained to predict cohort of origin, disregarding clinical group, reached AUC values of 0.87 to 1.00 using control subjects, and equivalent values using affected subjects. In one cohort with two recruitment centers and a single protocol, controls from both cities were separable (AUC 0.947), models did not transfer between centers (0.562 and 0.515), and their rankings correlated 0.003. Geographic heterogeneity of discriminant taxa operates below the national scale, which constrains the generalization of microbiome signatures derived from individual cohorts.

</details>

## Oncology

### [Beyond standardized health-related quality of life measures: Additional symptoms and problems reported through the EORTC WISP instrument in the EUonQoL-Kit study across European cancer populations](https://www.medrxiv.org/content/10.64898/2026.11.23.26368179v1)
*Rojas-Concha, L.; Adsersen, M.; Apolone, G. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.23.26368179 v1 · relevance 0.07

- **In one sentence**: A descriptive analysis of open-ended "write in three symptoms/problems" (EORTC WISP) responses from a 32-country European validation study of the EUonQoL-Kit, examining which additional symptoms patients raised beyond standardized quality-of-life items and how this differed across patients in treatment, survivors, and palliative care.
- **In plain words**: Standard questionnaires about quality of life in cancer ask about a fixed list of symptoms, so they can miss things that matter to a particular patient. This study looked at a free-text section where people could name up to three other problems they had. About 12% of the 4,284 participants wrote in problems, and roughly 40% of the 954 written items were not covered by the fixed questions.
- **Why it matters**: The findings suggest that an open-ended question could be added to a European cancer quality-of-life toolkit to catch concerns the fixed questions miss, without making the questionnaire longer for everyone. Whether this improves care or policy decisions is not shown in the text.
- **Background needed**: - Health-related quality of life (HRQoL): how a illness and its treatment affect daily physical, emotional and social wellbeing, usually measured by questionnaire.
- Patient-reported outcomes (PROs): symptoms and experiences reported directly by patients rather than by clinicians.
- EUonQoL-Kit: a toolkit developed with many stakeholders to inform health policy across Europe, combining standard closed questions with an open-ended section.
- EORTC WISP: an open-ended instrument from the European Organisation for Research and Treatment of Cancer where patients write in up to three symptoms or problems.
- Three groups studied: patients in active treatment, cancer survivors, and patients in palliative (comfort-focused) care.
- Descriptive study: it reports patterns and comparisons, not cause and effect. The text reports that differences between groups in the common additional symptoms were not statistically significant, while some subgroup differences in who responded were. · level: intermediate

<details><summary>Original abstract</summary>

Background: Standardized health-related quality of life (HRQoL) measures may not capture all symptoms/problems relevant to people with cancer. The European Oncology Quality of Life toolkit (EUonQoL-Kit), co-created with multiple stakeholders to inform health policy across Europe, combines standardized closed-ended patient-reported outcome (PRO) items with the European Organisation for Research and Treatment of Cancer (EORTC) open-ended Write In three Symptoms/Problems (WISP) instrument. We aimed to identify symptoms/problems reported via WISP beyond the EUonQoL-Kit, examine differences in background characteristics between WISP respondents and non-respondents, and compare additional symptom/problem reporting across three target cancer populations: patients in active treatment, survivors, and patients in palliative care. Methodology: This descriptive analysis used data from adults with current or previous cancer diagnoses participating in a multicenter validation study across 32 European countries (22 August 2024 - 7 July 2025). WISP responses were categorized, and subsequently their prevalence and severity were calculated. Participant characteristics and the ten most frequently reported additional symptoms/problems were compared across groups using t-tests, chi-square tests, or Fisher's exact tests, as appropriate. Results: Among 4,284 included participants, 519 (12.1%) reported 954 symptoms/problems on WISP, of which 383 (40.1%) were not covered by EUonQoL-Kit v2 closed-ended items. Women, participants from Western and Northern Europe, highly educated and those diagnosed with breast cancer were more likely to respond to the WISP than other subgroups (all p < 0.05). No statistically significant differences were found in the prevalence of common additional symptoms/problems (p [&ge;] 0.130). Descriptively, numbness/tingling, skin problems and bleeding were most reported by patients in active treatment; indigestion, incontinence, and vision problems in survivors; and edema, cough and itching in palliative care. Conclusions: The EORTC WISP complemented standardized PRO assessment by capturing additional symptoms/problems. Integrating open-ended WISP reporting into the final toolkit may enhance HRQoL assessment across European cancer populations while identifying population-specific concerns without expanding predefined items for all respondents.

</details>

### [Aneuploidy and structural genome complexity beyond the EWSR1 fusion is associated with evolution and outcome in clear cell sarcoma](https://www.medrxiv.org/content/10.64898/2026.11.20.26368414v1)
*Farswan, A.; Davies, C.; Krzeciesa, D. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.20.26368414 v1 · relevance 0.06

- **In one sentence**: Multi-omic profiling of clear cell sarcoma tumours and cell lines shows extra genomic complexity beyond the defining EWSR1-CREB fusion, and links aneuploidy, chromosomal instability, 17q gain, 9p21.3 loss and TERT alteration to poorer survival and a MYC-driven ribosome biogenesis signature.
- **In plain words**: Clear cell sarcoma is a very rare cancer whose outcomes range from slow-growing to resistant to chemotherapy, even though the tumours share the same core genetic change. This study examined primary, recurrent and metastatic tumours and cell lines using several layers of genetic and gene-activity data. The authors report that these tumours carry additional structural damage to chromosomes beyond the main fusion, and that the extent of these changes is linked to how the disease evolves and how patients fare.
- **Why it matters**: The work tries to explain why tumours with the same defining mutation behave so differently, and it proposes a possible molecular risk framework at diagnosis and a potential therapeutic target. Because the cancer is ultra-rare and the cohort details are not given in the text, these links should be treated as candidate findings that need independent confirmation.
- **Background needed**: - Clear cell sarcoma: an ultra-rare soft-tissue cancer, usually defined by a fusion of two genes (EWSR1 and a CREB-family gene).
- Gene fusion: an abnormal joining of parts of two genes, often driving cancer growth.
- Aneuploidy: having an abnormal number of whole chromosomes or chromosome pieces.
- Chromothripsis and chromoplexy: sudden, large-scale chromosome shattering and rearrangement events.
- Chromosomal instability: a tendency for chromosomes to be gained or lost repeatedly as cells divide.
- Subclonal diversification: the tumour splitting into genetically distinct sub-populations over time.
- MYC: a master growth-control gene; MGA normally restrains it.
- Ribosome biogenesis: the cell's manufacture of protein-building machinery, which fast-growing cancers often ramp up.
- Hazard of death: a statistical measure of risk of death at any given time, here compared between groups. · level: research-level

<details><summary>Original abstract</summary>

Clear cell sarcoma (CCS) is an ultra-rare cancer defined by EWSR1-CREB gene family fusions with clinical outcomes that range from indolent to chemotherapy-refractory metastatic disease. Through multi-omic profiling of primary, recurrent and metastatic tumours and cell lines, we show that CCS is more genomically complex than previously recognised. Beyond the fusion, tumours acquire chromoplexy, chromothripsis and an intermediate aneuploidy burden, with ongoing subclonal diversification. Recurrent events include chromosome17q gain and inactivation of the MYC antagonist MGA. Enriched transcriptional signatures of chromosomal instability,17q gain, 9p21.3 loss and TERT alteration each double the hazard of death, supporting a new molecular based CCS risk stratification framework at diagnosis. Transcriptomes converge on a MYC-driven ribosome biogenesis programme, a previously unrecognised therapeutic vulnerability. These findings address a central paradox of CCS, a shared oncogenic identity with divergent clinical fate, implicating tolerated aneuploidy and chromosomal diversification as candidate determinants of progression.

</details>

## Health informatics and medical AI

### [Continually pretrained open-weight language models can outperform traditional machine learning in EHR-based clinical prediction](https://www.medrxiv.org/content/10.64898/2026.11.20.26368580v1)
*Zhou, J.; Zhang, X.; Yan, C. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.20.26368580 v1 · relevance 0.17

- **In one sentence**: A single-site study extends a 12-billion-parameter open-weight language model's vocabulary with 17,601 clinical and audit-log codes, continues its pretraining on 4.7 billion tokens of 2019–2024 EHR records, and fine-tunes it for three prediction tasks, reporting AUROCs that match or beat gradient-boosted trees and the CEHR-BERT EHR foundation model on some tasks but not others.
- **In plain words**: Hospitals keep detailed electronic records of patients, and software can be trained to predict what will happen next, such as whether a patient will be discharged soon, come back within 30 days, or develop kidney injury in intensive care. This paper tests whether a general-purpose open AI language model, after being further trained on one medical center's records, can make these predictions better than standard machine-learning methods. The authors report that it beat the older methods on discharge and kidney-injury prediction in their tests, and did somewhat better than the comparison models on readmission, but it was below gradient-boosted trees on readmission.
- **Why it matters**: Many prior attempts to prompt language models with health records did worse than locally trained models, so showing that adapting an open model can close or reverse that gap is a useful result. It may matter for hospitals that cannot send patient data to outside services and need models they can run themselves, but the evidence comes from one academic center, so how well it transfers to other hospitals is unknown.
- **Background needed**: - Electronic health record (EHR): a hospital's digital patient chart, including diagnoses, medications, labs and notes.
- Large language model (LLM): an AI system trained on huge amounts of text to predict and generate language; here it is applied to coded medical data.
- Open-weight model: a model whose trained parameters are publicly downloadable, so it can be run and adapted locally.
- Continued pretraining: further training of an existing model on a new body of domain data before the final task-specific training.
- Vocabulary extension: adding new tokens (here, clinical and audit-log codes) so the model can represent them as units.
- Fine-tuning: training a pretrained model further on labelled examples for one specific task.
- AUROC: area under the receiver operating characteristic curve; a 0.5 score is chance and 1.0 is perfect ranking of patients by risk.
- Gradient-boosted trees: a standard, strong machine-learning method for tabular data, used here as a traditional baseline.
- CEHR-BERT: a transformer model pretrained specifically on EHR data, used here as a foundation-model comparator.
- Label efficiency: how well a model performs when only a fraction of the labelled outcome examples are available. · level: research-level

<details><summary>Original abstract</summary>

Large language models (LLMs) prompted with electronic health record (EHR) data have predicted clinical outcomes less accurately than locally trained machine-learning models. We developed VEX-EHR by extending the vocabulary of a 12-billion-parameter open-weight LLM (weights publicly available) with 17,601 clinical and audit-log codes from 170,483 patients' records at one academic medical center, continuing its pretraining on those 2019-2024 records (4.7 billion tokens) and fine-tuning it per task. AUROCs were 0.917 for next-24-hour discharge, 0.715 for 30-day readmission and 0.847 for intensive care unit acute kidney injury, against 0.868, 0.677 and 0.828 for gradient-boosted trees and 0.848, 0.650 and 0.791 for CEHR-BERT, an EHR foundation model. Continued pretraining added 0.031-0.053 AUROC on every task. With 10% of the labels, VEX-EHR exceeded both comparators using all labels for discharge, and CEHR-BERT for readmission, valuable where labels are costly. Adapted by continued pretraining, open-weight LLMs can outperform traditional machine learning in EHR-based prediction.

</details>

### [rendehR: a cohort-first, provenance-aware, agentic-ready pipeline for harmonizing multi-source electronic health records](https://www.medrxiv.org/content/10.64898/2026.11.19.26367722v1)
*Mussavi Rizi, M.; Shein, V.; Torres-Espin, A.* · `health informatics` · medRxiv doi:10.64898/2026.11.19.26367722 v1 · relevance 0.11

- **In one sentence**: rendehR is an R package and pipeline that builds disease-specific cohorts from MIMIC-III, MIMIC-IV, and eICU-CRD hospital records, harmonizing their differing schemas and coding while keeping the source-specific logic for cohort and concept definitions inspectable.
- **In plain words**: Public hospital record databases store similar information in different formats, with different codes, units, and layouts, which makes it hard to build the same patient group from several of them and check how it was done. This paper describes a software tool, rendehR, that defines a patient cohort first, then extracts and standardizes the matching records from three public ICU databases. It was demonstrated on a spinal cord injury and disease group and on a more complex sepsis definition, with counts of admissions and ICU stays reported for each database.
- **Why it matters**: Reproducibility and auditability are recurring problems in studies that reuse hospital data, and this work targets them by keeping cohort rules and SQL as saved, inspectable artifacts. The text reports case counts but does not evaluate whether the harmonized values are accurate, so its practical value for research quality remains to be shown by users and independent checks. The mention of AI-assistant tools (agent skills, an MCP server) reflects current interest in LLM-driven workflows, though the text gives little detail on how well they work.
- **Background needed**: - EHR (electronic health record): routine hospital data such as diagnoses, lab results, and medication records.
- MIMIC-III, MIMIC-IV, eICU-CRD: publicly available ICU databases with different structures and coding systems.
- Harmonization: converting data from different sources into a common format and units.
- Cohort: the group of patients who meet a defined set of criteria for a study.
- Sepsis-3: a clinical definition of life-threatening organ dysfunction caused by infection.
- Parquet: a compact, column-based file format for large tables.
- MCP server: a way for AI assistants to call defined tools to read data or configuration.
- Provenance: a record of where a data value or rule came from. · level: intermediate

<details><summary>Original abstract</summary>

Objective: Public electronic health record (EHR) databases differ in schema, identifiers, coding systems, units, and event structure, making disease-specific studies across multiple sources difficult to construct and audit. We developed rendehR, a computational pipeline and R package for cohort-centered extraction and harmonization of multi-source EHR data. Materials and Methods: rendehR treats cohort definition as an explicit executable component of dataset construction. Cohorts can be defined using diagnosis codes, identifiers, R callbacks, or source-specific SQL. After cohort selection, linked source tables are restricted to the selected population and can be retained as cohort-specific Parquet datasets or loaded into a persistent database. Clinical concepts are defined using source-aware mappings, generated, or curated SQL and are harmonized into flat, time-series, and duration representations. Configuration, executable SQL, cohort metadata, concept-origin metadata, and source-level values are retained to support inspection and traceability. In the current version rendehR provides interactive R assistant wizards for workflow configuration, a Shiny application for patient-level data visualization, three agent skills for AI-assisted workflow execution and extension, and an MCP server exposing nine read-only tools for AI-assisted configuration, concept discovery, and cohort exploration. The current implementation supports MIMIC-III, MIMIC-IV, and eICU-CRD. We demonstrate rendehR on a reference cohort of spinal cord injury and disease (SCID). Results: Using the reference cohort, rendehR identified 4,320, 39,850, and 2,343 qualifying hospital admissions in MIMIC-III, MIMIC-IV, and eICU-CRD, respectively. Patient-level extraction expanded these cohorts to 5,725, 104,988, and 2,823 hospital admissions, with 5,983, 17,405, and 3,441 associated ICU stays, respectively. Applying the more complex Sepsis-3 case identification, rendehR identified and extracted 34,460, 41,296, and 47,035 qualifying ICU stays across the same databases, respectively. The current concept library includes 22 flat, 123 time-series, and 75 duration harmonized concepts. Conclusion: rendehR provides a cohort-centered framework for constructing disease-specific datasets from multiple heterogeneous HER sources while preserving the source-specific logic used to define cohorts and clinical concepts. The package supports reusable cohort artifacts, inspectable SQL-based concept construction, harmonized analytical representations, and traceable study-specific data pipelines.

</details>

## Econometrics and applied economics

### [Measuring Colombia's Informal Output: Relative Earnings and Identification in a Bayesian Two-Sector Model, 1993-2026](https://arxiv.org/abs/2611.28297)
*Jaime Vera-Jaramillo* · `econ.EM` · arXiv:2611.28297v1 · relevance 0.08

- **In one sentence**: A Bayesian two-sector business-cycle model for Colombia that uses a new quarterly informal-to-formal earnings series to identify the size of the informal output share, 1993–2026.
- **In plain words**: The paper asks how much of Colombia's measured economic output comes from informal work, meaning jobs without formal contracts or social-security coverage. The authors argue that the share of workers who are informal cannot answer this, because informal jobs pay less and so produce less per worker. They estimate the informal output share from national accounts and household-survey data, and find it fell from about 30% of GDP in 1993 to about 20% in 2026Q2.
- **Why it matters**: Informal activity is hard to measure, and official output figures may miss or misstate it, which matters for tax policy and for reading growth and inflation. The paper's main methodological point, that relative earnings can identify the informal share where aggregate data cannot, may be useful to other countries with large informal sectors; the text does not show how well this carries over elsewhere.
- **Background needed**: - Informality rate: the share of workers without formal employment protection or social-security coverage. It is a labor measure, not an output measure.
- Two-sector model: a macroeconomic model with a formal sector (uses capital and labor) and an informal sector (uses labor only).
- Bayesian estimation: combining prior assumptions with data to estimate model parameters, giving a range of plausible values rather than a single figure.
- Identification: whether the data are rich enough to pin down a parameter; here, the paper says aggregate data alone cannot.
- Steady state: the long-run equilibrium a model settles to when shocks stop; the paper reports the quarterly path is nearly unaffected by it from 2007.
- Shadow-economy estimates: indirect statistical estimates (such as MIMIC models) of unrecorded economic activity; the paper compares its results to these.
- Capital share: the portion of formal output paid to capital rather than labor. · level: research-level

<details><summary>Original abstract</summary>

How much of Colombia's measured output is produced by informal work? The answer cannot be read from the labor-informality rate: Colombia combines an informality rate above 50% with a much smaller informal share of output, because informal work is less productive. We estimate a Bayesian two-sector business-cycle model on quarterly national accounts and on reconstructed employment and informality series for 1993-2026. Identification comes from a new quarterly series of informal-to-formal labor earnings built from household-survey microdata for 2007-2026. Formal production uses capital and labor, informal production is labor based, and an accounting relationship maps relative earnings, the informality rate and the formal capital share into the informal output share. We show that aggregate data alone cannot pin down the size of the informal sector, and that relative earnings identify its quarterly path: from 2007 the path is invariant, within 0.3 percentage points, to the model's steady state. The informal share declines from about 30% of GDP in 1993 to 20% in 2026Q2, while labor informality falls from about 69% to 54%. The estimates lie within the range of published shadow-economy series for Colombia, close to the enhanced MIMIC estimates of Asllani, Dell'Anno and Schneider for 2009-2020. Sensitivity analysis quantifies the role of the capital share and of non-wage labor costs.

</details>

### [AI-Assisted Programming and Labor Demand](https://arxiv.org/abs/2611.31083)
*Lindsey Raymond, Eleanor Wiske Dillon* · `econ.GN` · arXiv:2611.31083v1 · relevance 0.07

- **In one sentence**: A difference-in-differences style study of how adoption of the GitHub Copilot AI coding assistant across 5,414 multinational firms affected technical hiring, separations, headcount, vacancy duration, and the seniority mix of technical roles, using firms' predetermined software procurement cycles as a natural experiment.
- **In plain words**: This paper asks whether AI tools that write computer code are changing how many programmers companies hire. The authors track thousands of large firms that adopted GitHub Copilot, and use the timing of each firm's routine software purchasing cycle as a quasi-random source of when they adopted it. They report that, one year after adoption, quarterly technical hiring fell by 29% among firms that adopted because of a review, with no change in layoffs, total technical headcount, or how long jobs stayed open.
- **Why it matters**: It offers causal-style evidence on a question many people care about: whether generative AI reduces demand for workers doing the tasks it can perform. The effect appears concentrated in junior technical roles, and the paper suggests firms shift toward more experienced workers and roles that combine some coding with design work, though the text alone does not show how far these findings generalize beyond this sample.
- **Background needed**: - Generative AI: software that produces text or code from prompts; GitHub Copilot is an AI assistant that suggests code inside a programmer's editor.
- Natural experiment: a situation where something other than the researchers' choice (here, firms' scheduled software purchasing cycles) determines who gets a treatment, allowing cause-and-effect inference.
- Difference-in-differences style comparison: comparing changes over time between adopting and non-adopting groups.
- Labor demand: how many workers employers want to hire.
- Separations: workers leaving a firm through quits, layoffs, or firings.
- Vacancy duration: how long a job posting stays open before it is filled.
- Junior vs. senior roles: entry-level versus experienced positions; the paper finds the hiring drop is concentrated in junior technical roles. · level: research-level

<details><summary>Original abstract</summary>

Generative AI has demonstrated human-level performance on technical work tasks, yet evidence on how these task-level capabilities are changing labor demand remains scarce. We study the firm-level adoption of GitHub Copilot, an AI coding assistant, across 5,414 multinational firms accounting for 38% of the U.S. programming workforce. To identify causal effects, we exploit a natural experiment generated by firms' predetermined software procurement cycles. Early AI-adopting firms hired more workers before the launch of GitHub Copilot and had larger, more technical, and older workforces. After one year, GitHub Copilot adoption reduces quarterly technical hiring by 29% among review-induced adopters, with no effect on separations, overall technical headcount, or vacancy duration. The hiring slowdown is concentrated in the subset of junior technical roles that involve the highest share of coding work. Overall, AI coding assistance causes firms to shift demand towards more experienced workers and roles that pair some coding with broader design responsibilities.

</details>

## Economic theory

### [Decision Theory with Degree of Membership in the State Space](https://arxiv.org/abs/2611.28457)
*Jeff Dominitz, Charles F. Manski* · `econ.EM` · arXiv:2611.28457v1 · relevance 0.18

- **In one sentence**: The paper generalizes classical decision theory by letting each candidate state of the world have a degree of membership between 0 and 1 in the state space, rather than a yes-or-no possibility, and extends three standard decision criteria (subjective expected welfare, minimax regret, maximin) to this setting.
- **In plain words**: Standard decision theory assumes a decision maker lists the possible states of the world and treats each one as either possible or not. This paper relaxes that rule so that each possible state can count partially, with a number from 0 to 1 expressing how much it belongs in the set of states the decision maker is considering. The author then adapts three common rules for choosing under uncertainty to this more flexible setup.</plain>
<parameter name="why">The text is a theoretical framework and does not report empirical results, so its practical importance is unclear from the text alone. It may matter for researchers who want to model uncertainty about what the set of possible states even is, a question that ordinary probability over a fixed state space does not directly address.</plain>
<parameter name="background">- Decision theory: choosing an action by comparing how well each action does across possible states of the world.
- State space: the list of states the decision maker considers possible.
- Welfare/objective function: a score for how good an action is in a given state.
- Subjective probability (Bayesian approach): a personal belief distribution over states, which must add up to one.
- Fuzzy sets: a way of letting membership in a set be a matter of degree instead of yes or no.
- Minimax regret and maximin: rules for choosing under uncertainty that focus on the worst-case loss or worst-case payoff.
- **Background needed**:  · level: research-level

<details><summary>Original abstract</summary>

Classical decision theory considers a decision maker (DM) who faces a choice set C and believes that the true state of nature s* lies in a state space S. An objective function w(., .): C x S -> R1 maps actions and states into welfare. The DM wants to maximize w(., s*) but does not know s*. The state space specifies a labeled set of possible states. Possibility is binary: every state in S is possible and no state outside of S is possible. Thinking that this binary perspective on possibility is too rigid, we generalize the classical theory. We begin with a universe of labeled states U and a residual unlabeled state r. Classical theory associates a binary possibility indicator mu(s) with each s in (U, r). The residual state r is not possible, so mu(r) = 0. The state space is S = [s in U: mu(s) = 1]. We expand the range of mu to be the interval [0, 1]. Thus, mu is now a real number measuring degree of membership, a term we adopt from fuzzy set theory. The membership function mu(.): (U, r) -> [0, 1] differs substantively from but is consistent with the subjective probability distributions of Bayesian decision theory. Bayesian theory places a subjective distribution on the elements of a classical state space, each of whose members has degree of membership one. Degree of membership expresses the distinct idea that a DM may want to quantitatively express uncertainty regarding the composition of the state space. A mathematical distinction between subjective probabilities and degrees of membership is that the former must sum to one, but the latter need not. After formalizing basic ideas, we extend three prominent classical decision criteria--maximization of subjective expected welfare, minimax regret, and maximin--to our generalization of classical decision theory.

</details>

### [Large Economies with Social Types](https://arxiv.org/abs/2611.30620)
*Wei He, Yeneng Sun, Bin Wu et al.* · `econ.TH` · arXiv:2611.30620v1 · relevance 0.12

- **In one sentence**: The paper builds a general equilibrium framework for large economies with social externalities, where social types define reference groups, and shows that a competitive equilibrium exists for every admissible economy exactly when social anonymity holds, extending the result to incomplete preferences, indivisible goods, and production via conditional convexification.
- **In plain words**: This paper studies markets in which what a person wants depends on the people around them, such as neighbors, peers, or others of similar status. It asks when a market settling into a stable outcome (a competitive equilibrium, where prices make supply match demand) is guaranteed. The authors find that such an outcome always exists exactly when observable social groups do not fully pin down each individual within any sizeable part of the economy.
- **Why it matters**: Standard market theory assumes people do not affect each other through their social circles, so this work addresses a gap in that assumption. The extension to non-convex preferences, indivisible goods, and production may matter for applied questions like peer effects and social comparison, though the text alone does not show how far these results carry into practice.
- **Background needed**: - General equilibrium: a model of a whole economy where prices adjust until markets clear.
- Competitive equilibrium: a set of prices and choices where each person does their best and total demand equals total supply.
- Large economy: a model with a continuum of agents, where each individual is negligible and a "subeconomy" is a non-negligible group of them.
- Social externalities: one person's well-being or choices affect others, such as through envy, imitation, or status.
- Social type: an observable category (neighborhood, peer group, status class) that defines whom a person is compared with; distinct from an individual's name or identity.
- Social anonymity: the condition that social types do not uniquely identify people within a sizeable group.
- Convexity: the assumption that preferences or choice sets have no "dents" that favor mixing; non-convexity breaks standard existence proofs.
- Convexification: a proof technique that averages choices to restore convexity; the paper replaces the usual aggregate version with a conditional one. · level: research-level

<details><summary>Original abstract</summary>

This paper develops a new general equilibrium framework for large economies with social externalities, where agents have names as well as social types. Social types define the reference groups (neighborhoods, peers, or status classes) through which externalities operate, and are primitives of the market structure. We establish that every admissible economy admits a competitive equilibrium if and only if social anonymity holds. This condition requires that observable social types do not fully identify individuals within any non-negligible subeconomy. The framework extends to generalized large economies with incomplete preferences, indivisible goods, and production, and thus accommodates nonconvexity in preferences and consumption sets. Our proof replaces the standard aggregate convexification argument with conditional convexification. Applications include peer effects, social comparison, and risk sharing with local social benchmarks.

</details>

## Game theory and algorithmic economics

### [Reimbursement as a Revenue Instrument in Costly Clock Auctions](https://arxiv.org/abs/2611.28447)
*Miriam Nelson (Independent Researcher), Jack Stanick (Boston College), Edwin Lock (King's College London) et al.* · `cs.GT` · arXiv:2611.28447v1 · relevance 0.12

- **In one sentence**: The paper studies whether a seller in a clock (ascending-price) auction can raise net revenue by reimbursing bidders' per-round participation costs, such as blockchain transaction fees, and how those reimbursements should be timed, using a linear program for incentive-compatible payments plus two-bidder and four-bidder examples and learning-agent experiments.
- **In plain words**: In an auction where prices climb and bidders must actively confirm they are still in, each confirmation can cost the bidder something, such as a blockchain transaction fee. The paper asks whether the seller should pay some of these costs back, and when in the auction those payments should happen. In a two-bidder example, paying back only the final confirmation earned the seller the most net revenue among the schedules the authors checked, and in a four-bidder example, partial payments in earlier rounds did better.</plain>
<parameter name="why">Auctions that run on blockchains make per-bid fees a real design issue, so the question of whether a seller should subsidize them has practical weight. The findings are limited to the specific examples and schedules analyzed, so they show that the best timing can depend on the auction setting rather than giving a general rule.
- **Background needed**: - Ascending (clock) auction: the price rises over rounds, and bidders drop out when it gets too high.
- Participation cost: a small fee a bidder pays each time they confirm they are still bidding.
- Reimbursement: the seller paying part or all of those fees back, which can encourage bidders to stay longer.
- Net revenue: what the seller receives from the sale minus what the seller pays out in reimbursements.
- Incentive compatibility: a design where bidders' best strategy is to bid honestly, so their behavior can be predicted.
- Linear program: a standard optimization method for finding the cheapest payments that meet such constraints.
- Learning bidders: simulated bidders that adjust their behavior from experience rather than solving the game in advance. · level: research-level

<details><summary>Original abstract</summary>

Bidders in an ascending auction may incur a cost each time they choose to continue, for example when bidding requires a blockchain transaction. We therefore investigate whether a seller can increase net revenue by reimbursing these costs, and how reimbursements should be distributed across auction rounds. We study auctions in which bidders must actively confirm their participation as prices rise and the seller commits to reimbursements before bidding begins. We first show how a linear program can find the cheapest payments that keep bidders' strategies optimal when participation costs are introduced. Maximizing net revenue, however, can require changing those strategies. In a two-bidder example, we identify conditions under which reimbursing only the last scheduled decision earns the most net revenue among the schedules we analyze. This policy outperforms no reimbursement, full reimbursement, and the cheapest policy that maintains the original strategies. Some auctions end earlier than under full reimbursement, but the seller's savings exceed the resulting loss in sale receipts. Experiments with learning bidders reproduce these revenue comparisons. In a four-bidder example, they also identify a policy with partial reimbursements in earlier rounds that earns more than reimbursing only the final decision. These results show how the seller's preferred reimbursement timing can change across auction environments. Finally, we explain how requiring bidders to confirm continued participation limits the prices they can be charged when messages are missing, and discuss the requirements for implementing these auctions on a blockchain.

</details>

### [Stackelberg Games with Convex Risk Measures](https://arxiv.org/abs/2611.28974)
*Arunesh Sinha* · `cs.GT` · arXiv:2611.28974v1 · relevance 0.12

- **In one sentence**: Studies finite Stackelberg (leader-follower) games where payoffs are random due to environmental uncertainty and each player scores outcomes with a convex monetary risk measure, covering follower response uniqueness, hardness, an MPEC reformulation, and a smoothed implicit-gradient method with an additive approximation guarantee.
- **In plain words**: This paper looks at a two-player "leader and follower" game where the outcome is uncertain because of the environment, and each player judges that uncertain outcome with a cautious, risk-aware scoring rule rather than a simple average. The authors give conditions under which the follower's best response is unique and well-behaved, show that even finding an approximate equilibrium is computationally hard, and propose a mathematical reformulation together with a practical iterative method. They report experiments on synthetic and real data.
- **Why it matters**: Leader-follower commitments under uncertainty, such as security or pricing decisions, are a natural setting for risk-aware evaluation, so the work connects game theory with risk management. The text does not indicate how the results would be used in practice, and the approximation guarantee is conditional on the gradient method reaching global optimality.
- **Background needed**: - Stackelberg game: a leader commits to a strategy first, and a follower best-responds after seeing it.
- Mixed strategy: a randomized choice over actions, described by probabilities.
- Convex risk measure: a function that scores an uncertain reward, penalizing downside risk, with properties such as monotonicity and translation equivariance (adding a fixed amount to outcomes adds it to the score).
- Optimistic equilibrium: a solution concept where the follower breaks ties in the leader's favor.
- NP-hard: a class of problems believed to lack efficient exact algorithms in the worst case.
- Mathematical program with equilibrium constraints (MPEC): an optimization problem whose constraints include another player's best-response condition.
- Implicit gradient: a way to compute how a solution changes as parameters change, without solving the full inner problem explicitly. · level: research-level

<details><summary>Original abstract</summary>

Stackelberg games have important real-world applications in which reliable commitments require accounting for multiple sources of uncertainty. We study finite Stackelberg games in which environmental uncertainty makes each mixed strategy profile induce a random reward, and each player evaluates that reward with a convex monetary risk criterion. In reward form, it is a concave, monotone, translation-equivariant utility and also represented as penalized expected reward over distributions of environmental outcomes. We provide two conditions under which the follower has a unique continuous mixed response, which leads to inducible optimistic equilibrium. We show that even approximate equilibrium computation is NP Hard. We then derive an exact mathematical program with equilibrium constraints for the problem. We also develop an action entropy smoothed implicit-gradient method and prove an end-to-end additive approximation guarantee under the assumption that the gradient method reaches global optimality. We validate our scalability and other results with experiments on synthetic and real data.

</details>

## Mathematical finance

### [Quantum-Inspired Risk Portfolio Optimization via Exponential Tilting](https://arxiv.org/abs/2611.27990)
*Fabio Vitale, Francesca Cibrario, Davide Veronelli et al.* · `q-fin.PM` · arXiv:2611.27990v1 · relevance 0.17

- **In one sentence**: The paper proposes an exponential-tilting, constant-absolute-risk-aversion certainty-equivalent objective for portfolio selection, reduces it via a second-order approximation to a quadratic problem solved with MIQP and QUBO (with constraints handled by Lagrangian relaxation and slack variables), and compares classical and quantum-inspired solvers on a trading portfolio.
- **In plain words**: Investment portfolios are often chosen using a simple rule that assumes gains and losses follow a smooth bell-shaped curve, but real profit-and-loss outcomes are lumpy and skewed. This paper uses a mathematical "tilt" that reweights the possible outcomes to emphasise different parts of the distribution, then turns the resulting problem into a form that standard optimisation software or quantum-style hardware can solve. The authors report that tuning the tilt shifts the balance between average return, spread of returns, and tail losses, and that their approach stays competitive with other methods on a realistic trading portfolio.
- **Why it matters**: Portfolio selection under realistic, non-Gaussian loss distributions is a practical concern for risk managers, and the paper ties a tunable risk parameter to standard tail-risk measures. The claim that the QUBO formulation scales better than MIQP is a relevant comparison, though the text only says this is based on performance analysis with classical solvers, so its generality is unclear.
- **Background needed**: - Portfolio optimisation: choosing asset weights to balance expected return against risk.
- Mean-variance framework: the classic approach that measures risk by standard deviation and assumes roughly bell-shaped returns.
- Profit-and-loss (P&L) scenarios: a discrete list of possible gains and losses, each with a probability.
- Exponential tilting: reweighting outcomes by an exponential factor, controlled by a tilt parameter.
- Certainty equivalent under constant absolute risk aversion: a single number expressing the sure amount an investor would value equal to a risky outcome, given a fixed attitude to risk.
- Value at Risk (VaR) and Conditional Value at Risk (CVaR): measures of how bad losses get in the worst fraction of cases.
- Second-order approximation: replacing a complicated function with a quadratic (parabola-like) one that is accurate near a point.
- MIQP and QUBO: standard formulations for optimisation problems with integer choices; QUBO problems use binary 0/1 variables and can run on quantum-inspired or quantum hardware.
- Lagrangian relaxation and slack variables: techniques for folding constraints into the objective function. · level: research-level

<details><summary>Original abstract</summary>

Financial portfolio optimization is often framed through mean-variance objectives, yet real profit-and-loss (P&L) scenario distributions are typically discrete and non-Gaussian. To explore realistic P&L distributions, we propose an objective function based on exponential tilting and certainty equivalent under constant absolute risk aversion. We then derive a second-order approximation, recovering a quadratic optimization problem solvable through mixed integer quadratic programming (MIQP) and quadratic unconstrained binary optimization (QUBO). Constraints in the QUBO formulation are incorporated via Lagrangian relaxation and slack variable approaches, enabling a direct comparison between classical constrained MIQP and quantum-inspired methods. In order to study how exponential tilting affects mean, standard deviation, and tail-risk measures such as Value at Risk and Conditional Value at Risk, we design an experimental protocol based on scanning a grid of tilt parameters and solving the associated optimization problems. The results on a realistic trading portfolio show how the tilts can be tuned to optimize different risk-return profiles while remaining competitive with those found using other state-of-the-art approaches. Moreover, performance analysis suggests that, even using classical solvers, the QUBO formulation with Lagrangian relaxation scales better than the MIQP approach, providing the best constraint encoding strategy.

</details>

### [Marked INAR model and the rough Hawkes--Heston limit](https://arxiv.org/abs/2611.29565)
*Xiaoyu Wang, Yingli Wang, Lingjiong Zhu* · `q-fin.CP` · arXiv:2611.29565v1 · relevance 0.07

- **In one sentence**: The paper builds a discrete-time Monte Carlo scheme for the rough Hawkes-Heston stochastic volatility model using a nearly unstable marked integer-valued autoregressive process, proves its convergence to the continuous-time limit for several option payoffs, and reports FFT-based implementation and efficiency results.
- **In plain words**: Financial prices often move in bursts, and models of how volatility (the size of price swings) behaves try to capture this. This paper proposes a way to simulate such a model on a computer using a simple discrete counting process, where random "events" trigger further events. The authors prove that as the time steps get finer, the simulated prices, volatility and event records converge to the intended continuous model, and they test how accurately option prices come out.
- **Why it matters**: Simulating rough volatility models accurately and quickly is a practical problem for pricing options, since Monte Carlo methods are costly. The paper offers both a convergence proof and a computational speed-up claim, though the text does not establish how it compares with other existing simulation methods.
- **Background needed**: - Stochastic volatility: asset volatility itself is modelled as a random process that changes over time.
- Heston model: a standard, widely used stochastic volatility model with closed-form-style analysis.
- Rough volatility: volatility paths that are far more jagged than classical models, with roughness measured by a parameter (here, four roughness levels are tested).
- Hawkes process: a self-exciting random event process in which each event raises the chance of further events.
- Integer-valued autoregression (INAR): a discrete-time model for counts, here used to approximate the Hawkes-type event process.
- Monte Carlo simulation: estimating prices by averaging many simulated random paths.
- Fast Fourier transform (FFT): a fast algorithm for computing convolutions, used here to cut the cost of the memory-dependent sum.
- Convergence in law: the simulated distributions approach the limiting model's distributions as the grid is refined.
- Implied volatility: the volatility value that makes a model's option price match the market-style price; smiles show how it varies with strike. · level: research-level

<details><summary>Original abstract</summary>

We develop a discrete-time Monte Carlo algorithm for the rough Hawkes-Heston model based on a nearly unstable marked integer-valued autoregressive (INAR) process. We implement the algorithm with a block fast Fourier transform (FFT) scheme that evaluates the excitation convolution in $O(N\log^2 N)$ operations per path on an $N$-bin grid. We prove joint convergence in law of the spot variance, log price and common marked point measure to their rough Hawkes-Heston limits. We prove convergence of European call and put option prices, as well as convergence of arithmetic Asian and down-and-out put option prices to their continuously monitored values. For European options, the one-year implied volatility smiles computed from the grid transform approach the continuous affine reference across four roughness levels. Monte Carlo experiments on the same three grids compare arithmetic Asian and down-and-out put option prices with a finer-grid reference and demonstrate the efficiency of the proposed algorithm.

</details>

## Financial markets

### [Do Candlestick Charts Suffice? The Incremental Economic Value of Technical Indicators in Stock Return Prediction](https://arxiv.org/abs/2611.30584)
*Peng Liu, Yanyan Zheng* · `econ.GN` · arXiv:2611.30584v1 · relevance 0.09

- **In one sentence**: Using 1,707 Chinese A-share stocks (2013–2025), the paper tests whether volume and seven manually built technical-indicator groups add economic value beyond raw OHLC candlestick charts for predicting returns, using a 2D CNN plus simpler models as checks.
- **In plain words**: Traders often use chart patterns and formulas (called technical indicators) to guess where stock prices are heading. This paper asks whether those hand-made formulas still help when a deep learning model can read the raw daily price bars (open, high, low, close) directly. The authors found that each kind of input on its own, including the price bars alone, showed positive returns in out-of-sample tests, but adding the indicators to the price bars did not consistently improve results.
- **Why it matters**: It speaks to a live question in finance and machine learning: whether engineered features are still needed once neural networks can learn from raw data. The evidence comes from one large market (China's A-share stocks), so whether it generalizes to other markets is not established by the text.
- **Background needed**: - Candlestick chart (OHLC): daily open, high, low and close prices, drawn as bars.
- Technical indicator: a formula computed from past prices or volume, such as a moving average, used to signal trades.
- Convolutional neural network (CNN): a model that learns patterns from images; here the inputs are rendered as multi-channel images.
- Decile portfolio: ranking stocks by predicted return and grouping them into ten bins; "high-minus-low" compares the top and bottom bins.
- Sharpe ratio: return earned per unit of risk.
- Fama–French alpha: the return left over after adjusting for common market risk factors.
- Out-of-sample: testing on a later period (here 2021–2025) that the model did not see during training. · level: intermediate

<details><summary>Original abstract</summary>

Although technical analysis remains widely used in practice, the need for manually constructed indicators is increasingly questioned as deep learning models can extract features directly from OHLC price data. This paper examines the standalone economic value of trading volume and manually constructed technical-indicator groups and whether adding these groups to OHLC candlestick charts provides incremental economic value. Using daily data for 1,707 Chinese A-share stocks from 2013 to 2025, we construct approximately 3.36 million stock-window samples and encode them as multi-channel images containing candlestick charts, trading volume, and seven widely used manually constructed technical indicators. The primary analysis uses a 2D CNN on these images; complementary tests apply a logistic regression, a 1D CNN, and an LSTM to numerical representations of the same samples. Out-of-sample performance from 2021 to 2025 is evaluated using decile portfolios, Sharpe ratios, Fama--French alphas, and formal pairwise tests. Our empirical results yield two central findings. First, specifications based separately on OHLC, trading volume, and each technical-indicator group produce significantly positive high-minus-low returns and factor-adjusted alphas, together with economically meaningful Sharpe ratios; the OHLC-only specifications generally perform best under the nonlinear models. Second, adding these technical-indicator groups to OHLC does not systematically improve any of these performance measures in our setting. Together, these results provide the first large-scale evidence from the Chinese A-share market on the standalone and incremental economic value of these technical-indicator groups across multiple representations and model architectures.

</details>

### [Project financing in vanishing forests: Do investors care about nature protection?](https://arxiv.org/abs/2611.29281)
*Theodor Cojoianu, Mohammad Faour, Andreas Hoepner et al.* · `q-fin.GN` · arXiv:2611.29281v1 · relevance 0.07

- **In one sentence**: Using 9,037 project-loan pairs in 115 countries, the paper tests whether bank loan spreads and sponsor stock returns reflect a project's proximity to protected areas, nearby forest loss, and lenders' nature policies.
- **In plain words**: Large construction and energy projects, such as dams, mines or power plants, are often paid for with loans tied to one specific site. This study checks whether lenders charge higher interest when a project sits near protected nature or in areas where forest is disappearing. It finds that lenders charge more for protected-area proximity mainly when they also have explicit nature-risk policies, and the authors conclude that this pricing is not a strong push to stop serious harm to nature.
- **Why it matters**: Biodiversity loss is becoming a financial concern, and this paper ties it to specific physical sites rather than whole companies, which may matter for how banks and regulators think about nature risk. The text does not show how much this changes actual lending behaviour, so its practical reach is uncertain.
- **Background needed**: - Project finance: loans repaid from the cash flow of one specific asset (for example, a plant or road), not the whole company.
- Loan spread: the extra interest a borrower pays above a benchmark rate; a higher spread means the lender sees more risk.
- Protected areas and forest loss: measures of how close a site is to legally protected land and how much forest has been cleared nearby.
- Kunming-Montreal Global Biodiversity Framework: a 2022 international agreement setting nature-protection targets.
- Abnormal returns: stock price moves beyond what would normally be expected, used here to see whether markets react to loan announcements.
- Buffer zone: a distance band (here 1.5 km or 30 km) around a project used to define "nearby". · level: intermediate

<details><summary>Original abstract</summary>

Biodiversity risks are increasingly recognized by financial market participants, yet their measurement at the corporate-entity level obscures the locations and assets through which they arise. Project finance links identifiable physical assets to dedicated financing contracts, allowing us to examine this transmission more directly. By linking 9,037 project-loan pairs in 115 countries, we relate bank loan spreads to projects' proximity to protected areas, surrounding forest loss and lenders' nature policies. We find that lenders price proximity to protected areas only when they also have explicit nature risk policies and particularly within 1.5 km buffers from the project location. Realised forest loss around a project is priced more consistently than forest loss after the loan is signed, and risk pricing near protected areas strengthens after the Kunming-Montreal Global Biodiversity Framework. Listed company sponsors also experience negative, but short-lived, abnormal returns around loan signings for projects within 30 km of protected areas or in high-forest-loss landscapes. Our results suggest that while nature risk is partially priced in project finance, this is not a strong incentive to deter significant harm to nature.

</details>

## Signal processing

### [SA-GLRT-D: Sidelobe-Aware GLRT-Based Detector for FMCW Radar](https://arxiv.org/abs/2611.30008)
*Jiachen Zhu, Fangjiong Chen, Jie Wu et al.* · `eess.SP` · arXiv:2611.30008v1 · relevance 0.08

- **In one sentence**: Proposes SA-GLRT-D, a generalized likelihood ratio test (GLRT) detector for FMCW radar that models the spectral leakage of the cell under test and extends single-cell detection to local-region detection, with a fast implementation and parameter initialization scheme.
- **In plain words**: Radar systems must decide whether a reflected signal means a real object is present, but nearby objects and the radar's own signal spreading can create false echoes that hide real targets. This paper proposes a detector that accounts for how the signal from the target being tested spreads into neighboring frequency bins, and makes the decision jointly with estimating that spreading and suppressing the resulting side-echoes. The authors report simulation and real-measurement results showing high detection accuracy with a steady false-alarm rate and reasonable computing cost.
- **Why it matters**: Reliable target detection in dense, multi-object scenes matters for automotive and other FMCW radar applications. The text does not give quantitative comparisons with existing methods, so the size of the improvement cannot be judged from the abstract alone.
- **Background needed**: - FMCW radar: sends a frequency-swept signal and infers range and speed from the frequency of the returning echo.
- Detection as hypothesis testing: decide between "target present" and "only noise/clutter."
- GLRT: a standard statistical test that replaces unknown parameters with their best estimates from the data.
- CFAR (constant false alarm rate): a thresholding method that adapts to local noise so the rate of false alarms stays fixed.
- Spectral leakage and sidelobes: a finite observation window spreads a strong echo's energy into neighboring frequency bins, which can mimic or mask other targets.
- Reference cells: nearby bins used to estimate background level; contamination by other targets degrades this estimate. · level: research-level

<details><summary>Original abstract</summary>

This paper investigates adaptive detection for frequency-modulated continuous-wave (FMCW) radar in multi-target complex scenarios, where reference-cell contamination, spectral leakage from the cell under test (CUT), and the resulting sidelobe interference severely degrade detection performance. A sidelobe-aware detector based on the generalized likelihood ratio test (GLRT), termed SA-GLRT-D, is proposed. Unlike conventional filtering-then-constant false alarm rate (CFAR) schemes, the proposed method explicitly accounts for the non-ideal frequency-domain energy spreading of the CUT induced by the finite-window effect. Accordingly, conventional single-cell target detection is extended to local-region detection, and decision statistic construction, CUT-related parameter estimation, and sidelobe interference suppression are jointly accomplished within a unified hypothesis-testing framework. Furthermore, to reduce computational complexity, a fast implementation of SA-GLRT-D is developed, together with a dedicated parameter initialization strategy to enhance the stability of numerical optimization. Simulation and real-measurement results demonstrate that the proposed method achieves high-accuracy target detection while maintaining a constant false alarm rate, with favorable computational efficiency.

</details>

### [Beyond Raw IQ: Compact Semantic Representations for Task Oriented Automatic Modulation Classification](https://arxiv.org/abs/2611.28813)
*Omm Swarup, Shrishail M. Hiremath* · `cs.NI` · arXiv:2611.28813v1 · relevance 0.08

- **In one sentence**: The paper tests whether learned low-dimensional semantic representations (4 to 64 dimensions) can replace a 2048-dimensional raw IQ signal representation for automatic modulation classification under noise, with 16 dimensions reported as the best trade-off.
- **In plain words**: Wireless devices must figure out how a radio signal was encoded (its "modulation") before they can decode it. This paper asks whether the raw signal data, which is large, can be squeezed into a much smaller learned summary that still lets a classifier tell the modulation types apart, even when the signal is noisy. The authors report that a 16-number summary worked best overall, at 128 times compression, and kept classification accuracy at about 49% averaged over the tested noise levels.
- **Why it matters**: Smaller signal representations could reduce the cost of storing, processing and transmitting radio data, which matters for edge devices and networks. The text does not establish how this compares with the state of the art, and the accuracy figure is modest, so its practical value is still uncertain.</why>
<parameter name="background">- Modulation: the way information is encoded onto a radio carrier wave (for example, different digital schemes).
- IQ data: a standard way of recording a radio signal as two numbers per sample (in-phase and quadrature components).
- Automatic modulation classification (AMC): automatically identifying which modulation scheme a received signal uses.
- Compression ratio and dimensionality reduction: representing data with fewer numbers; here 2048 numbers are reduced to 16.
- Learned semantic representation: a compact summary produced by a trained model rather than the raw measurements.
- SNR (signal-to-noise ratio): how strong the signal is compared with background noise; lower means noisier.
- CNN (convolutional neural network): a common type of neural network for pattern recognition.
- Macro-F1: an accuracy-style score that averages performance equally across signal classes.</background>
<parameter name="difficulty">intermediate

<details><summary>Original abstract</summary>

Automatic modulation classification (AMC) is an important component of modern wireless communication systems, but conventional signal representations can be expensive to store, process, and communicate, particularly under noisy channel conditions. This work investigates whether learned semantic representations can provide a compact alternative to high-dimensional in-phase and quadrature (IQ) representations while retaining robustness to noise. Starting from a 2048-dimensional IQ representation, we evaluate learned semantic representations with dimensions of 4, 8, 16, 32, and 64. Across the evaluated configurations, a 16-dimensional representation provides the strongest overall trade-off between classification performance, robustness, and representation size. The resulting representation achieves a 128x compression ratio and a 99.22% reduction in dimensionality. We further evaluate representation stability across signal-to-noise ratios (SNRs), compare semantic representations with a raw-IQ CNN, analyze per-class robustness, and perform five-seed validation. The five-seed evaluation produces an average accuracy of (49.22 +- 0.52)% and Macro-F1 of (49.27 +- 0.53)% across the evaluated SNR range. These results indicate that learned semantic compression can produce a substan- tially smaller representation while preserving useful classification information and improving geometric stability under noise.

</details>

## Audio and speech

### [Preserving Prosody in Speaker Anonymization](https://arxiv.org/abs/2611.28290)
*Kevin Everson, Mari Ostendorf* · `eess.AS` · arXiv:2611.28290v1 · relevance 0.12

- **In one sentence**: This paper plugs a pretrained, privacy-preserving prosody encoder into a speech synthesis model so that speaker anonymization keeps intended prosody (rhythm, pitch, emphasis) while hiding the speaker's identity.
- **In plain words**: Voice anonymization tries to hide who is speaking by changing the voice, but the way someone's pitch and timing carry meaning is also tied to their identity, so changing the voice can also scramble that meaning. This work conditions the synthesized speech on prosody features taken from a privacy-preserving encoder, and reports that listeners more reliably perceive the intended prosodic meaning while anonymization stays competitive with earlier methods.
- **Why it matters**: Speech tools that hide identity are useful for privacy in voice assistants and recordings, and losing emotional or emphasis cues would make them less usable. The text reports only a modest, competitive comparison with prior work rather than a clear leap, so its practical impact is best judged from the full results.
- **Background needed**: - Speaker anonymization: altering recorded speech so a listener or machine cannot tell who the speaker is, while keeping the words understandable.
- Prosody: the melody, rhythm, stress and pacing of speech, which signal emotion, questions, and emphasis.
- Prosody encoder: a neural network that turns prosody into a compact numerical representation.
- Speech synthesis model: a system that generates audio from a representation such as text or features.
- Privacy-preserving encoder: one trained so the representation keeps useful prosody but drops identity-revealing information.
- Tradeoff: improving privacy often costs some naturalness or expressiveness, and the paper aims to reduce that cost. · level: research-level

<details><summary>Original abstract</summary>

Effective prosody modeling is essential in natural speech generation applications, but complications arise in speaker anonymization, since speaker attributes are present in acoustic correlates of prosody. Our work aims to improve previous reported tradeoffs between effective speaker obfuscation and preservation of prosodic content. To this end, we integrate an existing pretrained privacy-preserving prosody encoder into a speech synthesis model, enabling prosody-preserving speaker anonymization. By conditioning speech generation on prosody features, we find that human subjects more reliably perceive intended prosodic meaning, while anonymization performance is competitive with previous work.

</details>

### [Speech Emotion Recognition Across Languages: Prosodic Patterns and Self-Supervised Learning](https://arxiv.org/abs/2611.29040)
*Tianqi Geng, Zhichen Han, Hui Feng et al.* · `eess.AS` · arXiv:2611.29040v1 · relevance 0.08

- **In one sentence**: A cross-language study of prosody (pitch, intensity, timing) in emotional speech in Chinese, German and English, comparing human listeners with self-supervised speech models on emotion recognition and emotion diarization.
- **In plain words**: This paper asks how emotion shows up in the voice across three languages: Chinese, German and English. The authors measured features like loudness and pitch, and compared how well people and AI speech models could recognize the emotion being expressed. They report that humans did better than the AI models on cross-language tasks, but that the models improved considerably after a targeted adjustment (fine-tuning) and came close to native human listeners.
- **Why it matters**: Emotion recognition that works across languages matters for voice assistants, call-center analysis and health tools that listen to speech. The text suggests that certain features, such as intensity and pitch, may be shared across languages, but the abstract alone does not show how far these findings generalize, so this is best read as a preliminary result.
- **Background needed**: - Prosody: the rhythm, pitch, loudness and timing of speech, separate from the words themselves.
- ANOVA and mixed-effects models: standard statistical tests for comparing group differences while accounting for repeated measurements from the same speakers or items.
- Self-supervised learning (SSL): AI models pretrained on large amounts of unlabeled audio, which can then be adapted to specific tasks.
- Fine-tuning: a short extra round of training on labeled data to adapt a pretrained model to a new task.
- Speech emotion recognition (SER): labeling the emotion of an utterance as a whole.
- Speech emotion diarization (SED): labeling when emotions change within a longer recording, analogous to speaker diarization ("who spoke when").
- Transfer learning: using knowledge learned in one setting (here, mostly one language) in another. · level: intermediate

<details><summary>Original abstract</summary>

This study investigates the prosodic patterns of emotional speech across Chinese (CN), German (DE), and English (EN), with a focus on acoustic characteristics. Using ANOVA and mixed-effects modeling, we reveal cross-linguistic and emotion-specific prosodic patterns. A comparative analysis of Speech Emotion Recognition (SER) performance demonstrates that humans outperform Self-Supervised Learning (SSL) models in cross-lingual tasks, while SSL models show significant improvement in cross-lingual SER through an efficient fine-tuning process, achieving performance competitive with native human speakers. The study also analyzes the performance of Speech Emotion Diarization (SED) between models and humans, highlighting the effectiveness of SSL models in transfer learning scenarios. These findings emphasize the interplay between universal prosodic features (e.g., intensity, pitch) and language-specific factors. Moreover, the SSL model's outstanding performance indicates the potential value of these acoustic features in emotion processing, implying possible advancements in cross-lingual emotion recognition through refined training techniques.

</details>

## Control systems

### [Context-Aware Proactive Self-Adaptation: A Two-Layer Model Predictive Control Approach](https://arxiv.org/abs/2611.29857)
*Zhengyin Chen, Jialong Li, Nianyu Li et al.* · `cs.SE` · arXiv:2611.29857v1 · relevance 0.23

- **In one sentence**: The paper proposes a two-layer control scheme for self-adaptive software that uses a context-aware goal model to set priorities and feeds that into a model predictive controller, which plans adaptations ahead of time.
- **In plain words**: Software systems often need to change how they behave as their surroundings change, such as shifting load or conditions. This paper argues that the surrounding context should also change which goals the system treats as most important, and it builds a method that does this. The authors report that experiments in two scenarios showed better system performance, though the text gives no specific figures.
- **Why it matters**: It connects control theory with self-adaptive software engineering by treating goal priorities as part of the controller's objective, which may matter for systems that must anticipate change. The abstract does not show how large the gains were or how general the approach is, so its wider significance is uncertain.
- **Background needed**: - Self-adaptive software: systems that monitor themselves and change their behaviour at run time.
- Context: the conditions around the system, such as workload or environment.
- Goal model: a diagram of what a system is meant to achieve and how goals relate.
- Model predictive control (MPC): a control method that uses a model of the system to forecast its future and choose actions over a short horizon, repeating this at each step.
- Proactive adaptation: acting on predicted future conditions rather than only reacting to current ones.
- Two-layer control: one layer adapts the system, another adapts the controller itself, here by updating the controller's objective and constraints. · level: research-level

<details><summary>Original abstract</summary>

In self-adaptive software systems, the role of context is paramount, especially for proactive self-adaptation. Current research, however, does not fully explore context's impact, for example on priorities of the requirements. To address this gap, we introduce a novel contextual goal model to capture these factors and their influence on the system. Using this, we propose a two-layer control mechanism with a context-aware model predictive control to achieve proactive adaptation for the software system and adaptation for the controller itself. By contextual prediction and a more accurate system model, our approach utilizes model predictive control to facilitate timely and efficient system adaptations, improving both performance and adaptability. Meanwhile, we perform requirement adaptation to update the contextual goal model, which in turn updates the objective function and constraints of the controller. Our experimental evaluations across two scenarios demonstrate the significant benefits of our approach in enhancing system performance.

</details>

### [Control Barrier Functions in Motion Control](https://arxiv.org/abs/2611.28200)
*Stijn Hanegraaf (Maurice), Giannis Delimpaltadakis (Maurice), Hoang Chu (Maurice) et al.* · `eess.SY` · arXiv:2611.28200v1 · relevance 0.18

- **In one sentence**: The paper proposes control-barrier-function (CBF)-based motion controllers with continuous dynamics, specialized to integrator plants as CBF-HIGS, and compares them against projection-based controllers and the HIGS design via describing function analysis, simulations and experiments.
- **In plain words**: Precision machines such as positioning stages often use controllers that keep their response inside a chosen range, which helps them beat the limits of simple linear control. The catch is that the method used to do this makes the controller's underlying rules jump abruptly, which can stir up unwanted vibration-like behaviour in the machine. This paper borrows a safety-constraint idea from robotics and proposes a version whose rules change smoothly, and reports that in analysis, simulation and experiments it reduces this unwanted excitation while still improving disturbance rejection.
- **Why it matters**: Reducing unwanted high-frequency excitation in precision motion systems is a practical concern for manufacturing and instrumentation, and the paper claims to be the first to apply control barrier functions to this performance goal. The text does not establish how broadly the approach would transfer beyond the integrator case studied, so its wider significance is uncertain.
- **Background needed**: - Control system: a feedback rule that adjusts an input (e.g. a motor force) based on measured output, to make a machine follow a desired motion.
- Integrator: a basic dynamic element whose output accumulates its input over time; used here as a simple model of a motion plant.
- Projection-based controller: a controller that forces its response into a specified sector (a bounded range of input-output behaviour); the projection makes its rules discontinuous.
- Control barrier function (CBF): a mathematical tool, originating in safety-critical control, that keeps a system inside a safe set by enforcing a constraint on how its state evolves.
- Describing function analysis: an approximation that treats a nonlinear element as a gain depending on signal amplitude, used to estimate phase lag and harmonic (overtone) distortion.
- Harmonics: extra frequency components generated by nonlinearity; higher-order ones can excite unmodelled dynamics in hardware. · level: research-level

<details><summary>Original abstract</summary>

Projection-based controllers (PBCs) have significant engineering success in industrial high-precision motion systems by restricting their input-output behavior to performance-enhancing sector-sets thereby overcoming fundamental limitations of linear control. The projection results in continuous control signals, but their vector fields are discontinuous, potentially causing unwanted excitation of higher-order dynamics in the plant. Inspired by these projected controllers and the recent interest in control barrier functions (CBFs), we propose a new class of CBF-based motion controllers that (i) can mimic and exceed the performance benefits demonstrated by PBCs and (ii) have continuous dynamics thereby resulting in smooth control signals. We specialize our novel CBF-based control design to integrator dynamics, essentially connecting to a projected integrator, called Hybrid Integrator-Gain System (HIGS), thereby introducing CBF-HIGS. We analyze the CBF-HIGS's behavior using a describing function analysis, which reveals improved phase characteristics and a favorable trade-off in higher-order harmonic distortion compared to HIGS. Simulation and experimental results demonstrate that CBF-HIGS enhances disturbance attenuation and reduces the excitation of higher-order harmonics compared to HIGS due to its continuous vector field, without compromising robustness properties. The paper provides the first use of CBFs for performance improvement of mechatronic motion systems.

</details>

## Fetch statistics

| Topic | Fetched | New | Selected |
|---|---|---|---|
| Probability | 68 | 68 | 2 |
| Differential geometry | 78 | 78 | 2 |
| Partial differential equations | 119 | 119 | 2 |
| Harmonic analysis | 50 | 50 | 2 |
| Complex analysis | 19 | 19 | 2 |
| Operator algebras and spectral theory | 32 | 32 | 2 |
| Algebra | 67 | 67 | 2 |
| Representation theory | 26 | 26 | 2 |
| Number theory | 73 | 73 | 2 |
| Algebraic geometry | 64 | 64 | 2 |
| Topology | 38 | 38 | 2 |
| Dynamical systems | 50 | 50 | 2 |
| Combinatorics | 112 | 112 | 2 |
| Numerical analysis | 69 | 69 | 2 |
| Logic and foundations | 16 | 16 | 2 |
| Mathematical physics | 82 | 82 | 2 |
| Optimization and control | 70 | 70 | 2 |
| Statistics theory | 34 | 34 | 2 |
| Statistical methods and applications | 81 | 81 | 2 |
| AI industry news | 36 | 31 | 5 |
| Model architectures and training | 122 | 122 | 2 |
| Machine learning theory | 24 | 24 | 2 |
| Large language models | 131 | 131 | 2 |
| Computer vision | 407 | 407 | 2 |
| Reinforcement learning | 68 | 68 | 2 |
| AI safety and alignment | 67 | 67 | 2 |
| Interpretability | 9 | 9 | 2 |
| AI for mathematics | 10 | 10 | 2 |
| Robotics and embodied AI | 193 | 193 | 2 |
| Security and cryptography | 106 | 106 | 2 |
| Algorithms and complexity | 52 | 52 | 2 |
| Programming languages and formal methods | 51 | 51 | 2 |
| Systems and networking | 58 | 58 | 2 |
| Human-computer interaction | 66 | 66 | 2 |
| Information theory | 46 | 46 | 2 |
| High-energy theory and gravity | 109 | 109 | 2 |
| Statistical physics | 50 | 50 | 2 |
| Condensed matter | 84 | 84 | 2 |
| Particle physics | 90 | 90 | 2 |
| Nuclear physics | 34 | 34 | 2 |
| Quantum information and computing | 151 | 151 | 2 |
| Optics and atomic physics | 51 | 51 | 2 |
| Fluids and plasma | 55 | 55 | 2 |
| Biological physics | 10 | 10 | 2 |
| Climate, atmosphere and Earth | 22 | 22 | 2 |
| Cosmology | 35 | 35 | 2 |
| Galaxies | 40 | 40 | 2 |
| Exoplanets and planetary science | 20 | 20 | 2 |
| High-energy astrophysics | 57 | 57 | 2 |
| Stars and the Sun | 28 | 28 | 2 |
| Chemical physics | 32 | 32 | 2 |
| Materials science | 79 | 79 | 2 |
| Soft matter and polymers | 18 | 18 | 2 |
| AI for chemistry and materials | 35 | 35 | 2 |
| Biochemistry | 18 | 14 | 2 |
| Pharmacology and drug discovery | 7 | 7 | 1 |
| Computational and systems biology | 121 | 115 | 2 |
| Neuroscience | 77 | 72 | 2 |
| Genetics and genomics | 44 | 39 | 2 |
| Cell and molecular biology | 62 | 58 | 2 |
| Immunology and microbiology | 70 | 64 | 2 |
| Cancer biology | 30 | 26 | 2 |
| Ecology and evolution | 47 | 44 | 2 |
| Plant biology | 27 | 23 | 2 |
| Bioengineering and synthetic biology | 21 | 18 | 2 |
| Mathematical biology (arXiv) | 22 | 22 | 2 |
| Epidemiology | 23 | 19 | 2 |
| Infectious diseases | 4 | 2 | 1 |
| Public and global health | 17 | 13 | 2 |
| Psychiatry and neurology | 29 | 25 | 2 |
| Oncology | 9 | 6 | 2 |
| Health informatics and medical AI | 17 | 13 | 2 |
| Econometrics and applied economics | 22 | 22 | 2 |
| Economic theory | 11 | 11 | 2 |
| Game theory and algorithmic economics | 17 | 17 | 2 |
| Mathematical finance | 13 | 13 | 2 |
| Financial markets | 21 | 21 | 2 |
| Signal processing | 57 | 57 | 2 |
| Audio and speech | 30 | 30 | 2 |
| Control systems | 68 | 68 | 2 |

<!-- {% endraw %} -->
