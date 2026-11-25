# Research digest · 2026-11-25
<!-- {% raw %} -->

New papers posted from about 2026-11-24 to 2026-11-25 (UTC).

> Papers are picked by how closely their wording matches each topic's description (the "relevance" score), not by quality. Summaries are written by AI from the abstract only; open the paper before relying on them.

## Highlights

- **[(n-1)-Dimensional Hausdorff Measure Estimates for Free Boundaries of Infinity Laplace Equations](https://arxiv.org/abs/2611.31013)** (Partial differential equations): This is a mathematical study of the boundary between two regions in a certain type of equation: one where a solution is positive and one where it is zero. The authors show that the boundary is well behaved in a precise, quantified way, with a sharp constant that matches a known non-degeneracy estimate. From this they derive geometric consequences, such as the boundary being locally covered by Lipschitz graphs and having controlled surface size, which answers a question posed by Araújo, Leitão, and Teixeira in 2016.
- **[The maximum number of edges in minimal $k$-extendable bipartite graphs](https://arxiv.org/abs/2611.29504)** (Combinatorics): This paper is about graphs, which are networks of dots joined by lines, and about how many lines such a network can have while still having a robust pairing structure. A graph is "k-extendable" if any k non-overlapping pairings can always be completed to a full pairing of all dots, and "minimal" means that removing any single line destroys this property. The authors prove a conjectured maximum on the number of lines for the bipartite (two-sided) case when k is at least 3, and show the maximum is actually reached.
- **[LaTSEC: Lattice-Based Threshold Signatures with Native Non-Interactive Identifiable Abort and Compact Per-Party Storage](https://arxiv.org/abs/2611.30063)** (Security and cryptography): The paper is about a way for a group of people, each holding a secret piece of a digital signing key, to jointly sign a document while still being able to point out which member cheated or sent a bad piece. The authors propose a scheme where each member holds only one small secret share and has one public check key, so cheaters can be caught without extra back-and-forth rounds or heavy proofs. They report security proofs under standard lattice assumptions, and for 60 parties at 128-bit security they give concrete sizes: about 14.3 KiB of secret per party and a 24 KiB public key per party.

## Probability

### [Support monotonicity for quadratically regularized optimal transport](https://arxiv.org/abs/2611.30214)
*Johannes Wiesel, Xingyu Xu* · `math.OC` · arXiv:2611.30214v1 · relevance 0.17

- **In one sentence**: This paper proves that, for quadratic-cost entropic-style (quadratically regularized) optimal transport between compactly supported marginals, the support of the regularized optimizer is nested in the interior as the regularization parameter decreases, under regularity assumptions.
- **In plain words**: The paper studies a way of matching two spread-out distributions of mass, such as moving a pile of sand into a hole, where a small penalty term makes the matching smooth. The question is which locations carry any mass in the smoothed matching, and whether those locations only grow as the penalty is reduced. The authors show that, in the interior of the region and under stated regularity conditions, the set of active locations for a smaller penalty contains the set for a larger one, up to a fixed scaling factor.
- **Why it matters**: The text does not say what applications this has beyond the mathematics of optimal transport, so its wider relevance is uncertain. It concerns how an approximation behaves as a parameter goes to zero, a theme that matters for numerical methods and for the limit of the unregularized Monge problem.
- **Background needed**: - Optimal transport: finding the cheapest way to move one probability distribution onto another, here with squared-distance cost.
- Monge coupling: the exact, unregularized transport map that the regularized solution approaches as the penalty goes to zero.
- Quadratic regularization: adding a squared-density penalty to the cost so the optimal plan is smoother and spread out.
- Support of a measure: the set of points where the plan puts positive mass.
- Brenier map: the convex-gradient map that gives the optimal transport for quadratic cost.
- Marginals and densities: the two input distributions and how their mass is spread over space.
- Interior inclusion and rescaling: the claim holds away from the boundary, with a density bound of order epsilon to the power 2/(d+2).</background>
<parameter name="difficulty">research-level

<details><summary>Original abstract</summary>

We study the support of the optimizer $\pi_\varepsilon$ of the quadratically regularized optimal transport problem for quadratic cost and compactly supported marginals. As $\varepsilon$ tends to zero, this support converges to the support of the Monge coupling. We investigate whether the regularized supports are nested as $\varepsilon $ decreases. Under regularity assumptions on the marginal densities, their domains, and the Brenier map, we establish interior support inclusions in every dimension. More precisely, for each compact $K\subset\operatorname{int}X$ and fixed $\theta\in(0,1)$, we prove that $\mathrm{spt}\pi_\delta\cap(K\times Y) \subseteq\mathrm{spt}\pi_\varepsilon\cap(K\times Y)$ whenever $0<\delta\le\theta\varepsilon $ and $\varepsilon$ is sufficiently small. On these points, the rescaled density $\varepsilon d\pi_\varepsilon/d(\mu\otimes\nu)$ is bounded below by a positive multiple of $\varepsilon^{2/(d+2)}$. Our analysis combines sharp potential estimates with affine rescaling and a Liouville theorem that identifies the unique limiting density of the rescaled problem.

</details>

### [Fermat costs and path-dependent first-passage percolation](https://arxiv.org/abs/2611.28268)
*Sandro Gallo, Matthieu Jonckheere, Alejandro H. Wences* · `math.PR` · arXiv:2611.28268v1 · relevance 0.15

- **In one sentence**: The paper defines a continuum first-passage percolation model on a Riemannian manifold in which the step-cost exponent grows along the path under a control rule, and proves a shape theorem showing the costs converge to deterministic space-time integrals that define a quasi-distance.
- **In plain words**: The paper studies the cheapest way to travel between two places when you are scattered among random points, where the cost of each hop depends on its length and on how far along the route you already are. The authors show that, as the number of random points grows, the cheapest costs settle down to a fixed, predictable formula along each curve. The resulting measure is not a true distance, because going one way can cost more than going back.
- **Why it matters**: The asymmetry of the limiting cost, where moving from dense regions to sparse ones tends to be cheaper, may be relevant to machine learning settings that use random point samples and graph-like geometry. The text does not show any concrete application or experiment, so this connection is a suggestion by the authors rather than a demonstrated result.
- **Background needed**: - First-passage percolation: a random-geometry model where each hop between random points has a cost, and one studies the cheapest total cost between points.
- Shape theorem: a result saying that, at large scale, such random minimum costs converge to a deterministic limiting shape or formula.
- Riemannian manifold: a smooth curved space in which lengths and distances are defined locally.
- Density function: describes how likely points are to appear in each region; here the points are denser in some regions than others.
- Quasi-distance: like a distance but possibly not symmetric, so cost from A to B can differ from cost from B to A.
- Exponent alpha > 1: a hop of length r costs roughly r raised to alpha, so long hops are penalized more than short ones. · level: research-level

<details><summary>Original abstract</summary>

We introduce a path-dependent and space-inhomogeneous first-passage percolation (FPP) model in the continuum. Inspired by Euclidean FPP, it is defined through a sample of points drawn from a common density function on a Riemannian manifold. In Euclidean FPP, the cost of each step in a discrete path is given by its length raised to the power $\alpha>1$. In our model, the power $\alpha$ increases as the path progresses, governed by a control mechanism. Consequently, the resulting percolation cost is not a distance. However, we prove a shape theorem showing that, as the number of points goes to infinity, the percolation costs converge to deterministic space-time integrals along curves in the manifold. This limit defines a quasi-distance with the property that traversing a curve from a high-density region towards a low-density one is generally cheaper than in the reverse direction; thus highlighting its potential use in machine learning applications.

</details>

## Differential geometry

### [Gray II, K\"ahler Nullity and Ricci Flow on Generalized Flag Manifolds with Two Isotropy Summands](https://arxiv.org/abs/2611.30716)
*Lino Grama, Ailton R. Oliveira, Francisco V. Oliveira* · `math.DG` · arXiv:2611.30716v1 · relevance 0.20

- **In one sentence**: The paper studies Gray's second curvature identity, Kähler nullity, and normalized homogeneous Ricci flow on generalized flag manifolds with two isotropy summands, for both invariant almost complex structures.
- **In plain words**: The paper looks at a family of symmetric, highly structured curved spaces (generalized flag manifolds) and asks how their geometry responds to a smoothing process called Ricci flow. The authors check a curvature rule (Gray's second identity) holds for every symmetric choice of metric, and identify when a special set of directions (the Kähler nullity) collapses or lines up with a natural splitting of the space. They also reduce the flow to a single equation for one ratio of metric parameters.
- **Why it matters**: The text reports that the flow dynamics show the Kähler–Einstein direction is attracting and the other invariant Einstein direction is repelling, which describes how such spaces evolve under Ricci flow. Its relevance beyond this specific class of spaces is not stated in the text, so broader impact is uncertain.
- **Background needed**: - Manifold: a curved space that locally looks like flat space, here with extra symmetry.
- Metric: a rule for measuring distances and angles on the space; "invariant metric" means it respects the space's symmetries.
- Generalized flag manifold: a homogeneous space built from Lie group symmetry, such as spaces of nested subspaces.
- Isotropy summand: a piece of the tangent directions at a point that the symmetry group treats as a unit; "two summands" means two such pieces.
- Almost complex structure: a way of rotating tangent directions by 90 degrees, a rough analogue of multiplying by i; Kähler spaces have one compatible with the metric and integrable.
- Integrable: the structure comes from genuine complex coordinates.
- Kähler–Einstein metric: a metric that is both Kähler and has constant Ricci curvature, a special, balanced shape.
- Ricci flow: a process that deforms a metric to smooth out curvature, analogous to heat spreading out uneven temperatures.
- Totally geodesic leaves: sub-surfaces whose shortest paths stay inside them. · level: research-level

<details><summary>Original abstract</summary>

We investigate Gray's second curvature identity, K\"ahler nullity, and homogeneous Ricci flow on generalized flag manifolds with two isotropy summands. We prove that every invariant metric satisfies Gray's second identity for both invariant almost complex structures. For the non-integrable structure, the K\"ahler nullity is trivial except at a distinguished metric ratio, where it coincides with the vertical distribution of a homogeneous fibration. This distribution is integrable and has totally geodesic leaves. For the integrable structure, the K\"ahler nullity exhibits a different behavior and need not be integrable away from the K\"ahler locus. Finally, we reduce the normalized homogeneous Ricci flow to an autonomous equation for the ratio of the metric parameters. The resulting dynamics identify two invariant Einstein directions and show that the K\"ahler--Einstein direction is attracting, while the other is repelling.

</details>

### [Support functions of sections of $p$-minimal tubes](https://arxiv.org/abs/2611.29625)
*Vladimir G. Tkachev* · `math.DG` · arXiv:2611.29625v1 · relevance 0.18

- **In one sentence**: The paper studies convex hulls of horizontal sections of compact p-minimal hypersurfaces bounded by two parallel planes, showing their support function is a viscosity subsolution of a degenerate elliptic inequality and deriving mean-width, lifetime, and distance bounds, including a sharp catenoid-equality bound for minimal surfaces in R^3.
- **In plain words**: The paper looks at soap-film-like surfaces stretched between two parallel flat planes, and at the convex shape each horizontal cross-section fills in when you wrap a rubber band around it. The authors describe how a standard way of encoding such shapes (the support function) must obey a certain partial differential inequality. From this they derive bounds on how far apart the planes can be, and say the bound is sharp with equality only for a catenoid, the familiar hourglass-shaped minimal surface.
- **Why it matters**: The results give a geometric route to a known rigidity theorem of Bernstein and Breiner and extend it to non-convex and multi-component boundaries, and they link the Meeks annulus conjecture to a regularity property of these hulls. The text does not show how far the methods reach beyond these cases, so the wider impact is uncertain.
- **Background needed**: - Minimal surface: a surface that locally minimises area, like a soap film, with zero mean curvature.
- p-minimal hypersurface: a generalisation of minimal surfaces defined through a weighted area functional with exponent p; the paper's setting.
- Convex hull: the smallest convex set containing a shape, like the region enclosed by a stretched rubber band.
- Support function: a way of describing a convex body by recording, for each direction, how far its furthest point reaches.
- Viscosity subsolution: a weak notion of solving a partial differential inequality, used when functions may not be smooth.
- Monge–Ampère type equation: a nonlinear second-order PDE common in convex geometry.
- Alexandrov area functions / atoms: measures describing how surface area of a convex body is distributed by normal direction; atoms correspond to edges.
- Mean width: an average size measure of a convex body over all directions.
- Catenoid: the minimal surface formed by a soap film between two coaxial circular rings.
- Meeks annulus conjecture: a open question in minimal surface theory about embedded annuli bounded by two curves. · level: research-level

<details><summary>Original abstract</summary>

Let $M$ be a compact $p$-minimal hypersurface in ${\mathbb R}^{n+1}$ with boundary in two parallel hyperplanes. We study the convex hulls $\Omega(\tau)$ of its horizontal sections through their support function $H(\tau,\cdot)$, without any assumption on the topology of $M$. We prove that $H$ is a viscosity subsolution of a degenerate elliptic inequality. For $n=2$ it is of Monge--Amp\`ere type, and its equality case for minimal surfaces with circular sections is Riemann's system. A posteriori, $H$ is locally semiconvex and every hull is a smooth convex body; the inequality then also holds in the sense of measures, with the edges of the hulls appearing as atoms of Alexandrov's area functions. Averaging over directions gives a catenary-type inequality for the mean width of the hulls. It yields lifetime bounds for $p$-minimal tubes when $n>p$. For minimal surfaces in ${\mathbb R}^3$ it gives a sharp bound for the distance between the planes in terms of the perimeters of the hulls of the boundary curves, with equality only for a catenoid. For one convex curve in each plane this recovers, by a different method, the nonexistence and rigidity theorem of Bernstein and Breiner. The bound extends to non-convex curves and to boundaries with several components. Finally, we show that the Meeks annulus conjecture is equivalent to the absence of atoms in the area functions of the hulls of all intermediate sections.

</details>

## Partial differential equations

### [(n-1)-Dimensional Hausdorff Measure Estimates for Free Boundaries of Infinity Laplace Equations](https://arxiv.org/abs/2611.31013)
*Yantian Chen, Feida Jiang* · `math.AP` · arXiv:2611.31013v1 · relevance 0.18

- **In one sentence**: The paper proves a sharp distance-to-free-boundary estimate with an explicit optimal constant for nonnegative viscosity solutions of the infinity Laplace equation with strong absorption, yielding a tangent-ball property, a 1/2 density bound, Lipschitz covering, and local (n-1)-dimensional Hausdorff measure estimates for the free boundary.
- **In plain words**: This is a mathematical study of the boundary between two regions in a certain type of equation: one where a solution is positive and one where it is zero. The authors show that the boundary is well behaved in a precise, quantified way, with a sharp constant that matches a known non-degeneracy estimate. From this they derive geometric consequences, such as the boundary being locally covered by Lipschitz graphs and having controlled surface size, which answers a question posed by Araújo, Leitão, and Teixeira in 2016.
- **Why it matters**: The result settles an open question from a 2016 paper in the same area, so it matters to specialists in nonlinear elliptic equations and free boundary problems. The text suggests the barrier argument may extend to more general equations, but it does not show this, so that wider reach is only a possibility.
- **Background needed**: - A partial differential equation (PDE) describes how a quantity varies in space; a solution is a function satisfying it.
- The infinity Laplacian is a nonlinear, degenerate operator tied to the steepest slope of a function, used in optimal transport and game-theoretic settings.
- Viscosity solutions are a weak notion of solution suited to nonlinear equations where classical derivatives may not exist.
- A free boundary is the interface separating the region where a solution is positive from the region where it vanishes.
- Non-degeneracy estimates say a positive solution cannot decay too fast near its free boundary; the sharp constant here is the optimal value of such a bound.
- Lipschitz graphs are boundaries locally written as functions with bounded slope; the (n-1)-dimensional Hausdorff measure is the generalized surface area of an n-1 dimensional set.
- A tangent ball property means every boundary point has a ball touching it from inside, with a controlled radius. · level: research-level

<details><summary>Original abstract</summary>

We investigate the geometric properties of free boundaries associated with nonnegative viscosity solutions to the infinity Laplace equation with strong absorption $$ \Delta_\infty u=\lambda u_+^m, \qquad \lambda>0,\quad 0<m<3. $$ We first establish a sharp distance-to-free-boundary regularity estimate with an explicit optimal coefficient, which coincides with the constant in the non-degeneracy estimate. This exact matching yields a uniform interior tangent ball property at every sufficiently small scale for every free boundary point. As consequences, we obtain a sharp lower density bound of $1/2$ for the positive phase, a locally finite covering of the free boundary by Lipschitz graphs, and quantitative local estimates for its $(n-1)$-dimensional Hausdorff measure, thereby giving an affirmative answer to the question raised by Ara\'ujo, Leit\~ao, and Teixeira (J. Funct. Anal. {\textbf 270} (2016), no. 6, 2249-2267). The underlying barrier mechanism also suggests possible extensions to more general equations.

</details>

### [Global existence and decay estimates for classical solutions to 2D compressible micropolar fluid equations with vacuum](https://arxiv.org/abs/2611.28657)
*Guo Houbin, Zhu Changjiang, Zhu Qiaolong* · `math.AP` · arXiv:2611.28657v1 · relevance 0.15

- **In one sentence**: Proves global existence and uniqueness of strong and classical solutions to the 2D compressible micropolar fluid equations with far-field vacuum, for small initial energy but possibly large oscillations, via a priori decay estimates on pressure, velocity gradient and microrotation that close a bootstrap argument.
- **In plain words**: This paper studies a mathematical model of a squeezable fluid in two dimensions, where tiny particles can also spin on their own, and where the fluid thins out to nothing far away (a "vacuum"). The authors show that, when the total initial energy is small, smooth solutions exist for all time and are unique, even if the starting data fluctuate a lot. The main work is proving that the pressure, the flow's velocity gradient and the spin velocity all fade in a controlled way over time.
- **Why it matters**: Global well-posedness for compressible fluids with vacuum is a hard, active topic in PDE theory, and the paper addresses the extra coupling between flow velocity and microrotation that makes micropolar models harder than standard compressible Navier–Stokes. The text does not say how it compares with prior results or what applications it may have, so its wider significance is best judged by specialists.
- **Background needed**: - Compressible fluid: a fluid whose density can change, described by PDEs for density, velocity and pressure.
- Micropolar fluid: a richer fluid model in which small internal particles can rotate independently; the "microrotational velocity" is their spin.
- Vacuum: regions where the density is zero; "far-field vacuum" means the fluid thins to zero at infinity.
- Cauchy problem: an initial-value problem on the whole space, with data given at time zero.
- Global existence: solutions do not blow up and exist for all time.
- A priori estimates and bootstrap: bounds assumed on a solution and then improved, to show it stays regular.
- Strong/classical solutions: solutions with enough derivatives to satisfy the equations pointwise. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we consider the Cauchy problem for the two-dimensional compressible micropolar fluid equations with far field vacuum. Under the assumption that the initial energy is sufficiently small, we establish the global existence and uniqueness of strong and classical solutions, allowing for large oscillations in the initial data. The key to the proof is to derive {\it a priori} decay estimates for the pressure, the velocity gradient, and the microrotational velocity, which enable us to close the bootstrap argument. We also handle the difficulties arising from the coupling between the velocity field and the microrotational velocity.

</details>

## Harmonic analysis

### [Multipliers and integration operators on Hardy--Bloch type tent spaces](https://arxiv.org/abs/2611.28895)
*Jiale Chen* · `math.FA` · arXiv:2611.28895v1 · relevance 0.18

- **In one sentence**: The paper characterizes when integration operators J_g and I_g and pointwise multipliers M_g are bounded between Hardy–Bloch type tent spaces BT^p, with complete results for I_g and for J_g and M_g when p<q, and separate conditions when p≥q.
- **In plain words**: The paper studies a family of function spaces made of holomorphic (complex-differentiable) functions on a disc, defined by controlling a maximal average of their derivative near the boundary. It asks when certain simple operations, such as integrating a function or multiplying it by a fixed function g, keep a function inside these spaces in a controlled way. The authors give a full answer for one operator across all exponents, and for the other two operators in one range of exponents, with separate but not fully matching conditions in the other range.
- **Why it matters**: Operators of this kind are a standard way to compare function spaces in complex analysis, so the results clarify how these spaces relate to each other. The text does not claim applications beyond this area, so any wider significance is uncertain.
- **Background needed**: - Holomorphic function: a complex-valued function that is complex-differentiable on an open region, here the unit disc.
- Bloch-type space: functions whose derivative is controlled (bounded in a weighted sense) near the boundary.
- Hardy space: a space of functions whose boundary behaviour is measured by an integral power p.
- Tent space: a space built from functions on the disc through a maximal function taken over cones ("tents") reaching the boundary.
- Non-tangential maximal function: the largest value a function takes over approach regions that meet the boundary at an angle, used to measure boundary behaviour.
- Integration operator J_g, I_g and multiplier M_g: operations that respectively integrate f against g, integrate f times g, or multiply f pointwise by g.
- Boundedness: the operator maps the space into the target space with output size controlled by input size.
- Fractional maximal function: a averaging tool that measures local size with a power-law weight; used as an estimate in the proofs.
- Exponents p, q: parameters indexing the spaces; p<q and p≥q are the two regimes treated differently. · level: research-level

<details><summary>Original abstract</summary>

We investigate the boundedness of integration operators $J_g$ and $I_g$ and pointwise multipliers $M_g$ on Hardy--Bloch type tent spaces $\mathcal{BT}^p$. The main difficulty is that these spaces are defined through a non-tangential maximal function of the radial derivative, which places the problem at the interface of holomorphic function theory and harmonic analysis. We completely characterize the boundedness of $I_g:\mathcal{BT}^p\to\mathcal{BT}^q$ for all $0<p,q<\infty$, and obtain a complete characterization for $J_g$ and $M_g$ when $p<q$. For $p\geq q$, we establish separate necessary and sufficient conditions. The proofs in the case $p\leq q$ are mainly based on some fractional maximal function estimates, whereas those in the case $p>q$ are mainly based on a synthesis lemma. We also give examples showing that several converse implications in the range $p\geq q$ fail.

</details>

### [Perturbed Nevo--Thangavelu maximal functions on two-step nilpotent groups](https://arxiv.org/abs/2611.28400)
*Jaehyeon Ryu* · `math.CA` · arXiv:2611.28400v1 · relevance 0.17

- **In one sentence**: The paper studies L^p boundedness of maximal averages over parabolically dilated, curved convex hypersurfaces lying in a tilted subspace of a two-step nilpotent Lie group, in the low-rank regime, with a sharp range of p for m=1 and a Łojasiewicz-exponent criterion for m≥2.
- **In plain words**: The paper concerns a mathematical averaging tool: it looks at how averages of a function over curved surfaces, taken at many scales, can be controlled in size. The setting is a special kind of curved geometric space (a two-step nilpotent group, identified with ordinary coordinate space). The authors determine exactly which range of exponents p makes this averaging tool well behaved when the extra dimension m equals 1, and for m at least 2 they give a condition, stated through a Łojasiewicz exponent, for when a known necessary range is also enough.
- **Why it matters**: Maximal function bounds are a standard way to test how well averages behave, and sharp results of this kind shape the broader theory of averages on curved spaces. The text does not say more about applications, so the wider connections are uncertain from this excerpt alone.
- **Background needed**: - Maximal function: the supremum over many scales of averages of a function over a set; boundedness on L^p means the result stays controlled in an L^p size measure for inputs in that space.
- L^p spaces: a family of size measures indexed by p; the question is which p work.
- Nilpotent Lie group: a curved, non-commutative generalization of Euclidean space with layered (step-two) structure; exponential coordinates give it a concrete coordinate form.
- Parabolic dilates: scalings that stretch different coordinate directions by different amounts.
- Gaussian curvature: the product of principal curvatures of a surface; nonvanishing means the surface is curved everywhere in every direction.
- Tilted subspace: a flat slice of the space that is not aligned with the standard coordinate axes.
- Łojasiewicz exponent: a number measuring how flat or degenerate a real-analytic function is near its zeros, used here as a geometric quantity controlling the answer. · level: research-level

<details><summary>Original abstract</summary>

Consider a step-two nilpotent Lie group $G$ identified with $\mathbb R^d\times \mathbb R^m$ in exponential coordinates. We study maximal operators associated with parabolic dilates of smooth convex hypersurfaces with nonvanishing Gaussian curvature in a tilted $d$-dimensional subspace of $G$. We focus on the low-rank regime, where the rank is determined by the group law and the tilt. When $m=1$, we determine the optimal range of $p$ for which the maximal operator is bounded on $L^p(G)$. For $m\ge2$, we characterize, in terms of a {\L}ojasiewicz exponent, when the known necessary condition on $p$ is also sufficient.

</details>

## Complex analysis

### [An extension of Janowski functions with applications](https://arxiv.org/abs/2611.28693)
*Kunle Oladeji Babalola* · `math.CV` · arXiv:2611.28693v1 · relevance 0.08

- **In one sentence**: The paper extends Janowski functions, which are classes of analytic functions subordinate to a Möbius-type function (1+az)/(1+bz), by allowing the constants a and b to be complex numbers instead of real numbers in [-1,1] with b<a.
- **In plain words**: This paper is about a family of well-behaved mathematical functions, called Janowski functions, that are defined by comparing them to a simple fraction with two constants. The authors let those two constants take complex values (numbers with an imaginary part) rather than only real values. The text says they study this larger setting and give some applications, but the excerpt does not list the specific results.
- **Why it matters**: Generalizing a classical class of functions from real to complex parameters is a standard way to widen what a known theory covers. Whether it matters further depends on the applications, which the excerpt does not describe, so its wider significance is uncertain.
- **Background needed**: - Analytic (regular) function: a function of a complex variable that is smooth and differentiable throughout a region.
- Subordination: one function is "subordinate" to another if it behaves like the other after a suitable reparametrization of the domain.
- Janowski functions: analytic functions subordinate to (1+az)/(1+bz), with real a, b satisfying -1 ≤ b < a ≤ 1.
- Complex numbers: numbers of the form x+iy, extending the real line to a plane. · level: research-level

<details><summary>Original abstract</summary>

Janowski functions are regular functions of the form $p(z)=1+p_1z+\cdots$, which are subordinate to $L_0(a,b:z)=(1+az)/(1+bz)$ for real numbers $a,b$ such that $-1\leq b<a\leq 1$. In this paper, we expand the space of the constants, $a$ and $b$, of the superordinate function, $L_0(a,b:z)$, to a larger set of complex numbers and provide some applications.

</details>

### [Sharpness of the Brjuno Condition for Hyperbolic Bishop Surfaces](https://arxiv.org/abs/2611.30985)
*Dijia Chen* · `math.CV` · arXiv:2611.30985v1 · relevance 0.06

- **In one sentence**: The paper proves a conjecture of Gong and Stolovitch: for a unimodular, non-root-of-unity, non-Brjuno parameter μ, there is a real-analytic surface in C^2 with Moser–Webster invariant μ that is formally but not holomorphically equivalent to the Bishop quadric Q_γ with γ = 1/√(2+μ+μ⁻¹) > 1/2.
- **In plain words**: This paper is about when two smooth surfaces sitting in two-dimensional complex space can be matched by a change of coordinates. Some surfaces can be matched by a formal, power-series change of coordinates but not by a genuine convergent one. The author shows that a specific surface, built from a number μ on the unit circle that fails a certain number-theoretic condition (the Brjuno condition), is of this kind, which settles a conjecture by Gong and Stolovitch.
- **Why it matters**: The result shows that a number-theoretic condition (the Brjuno condition) is sharp in this setting: when it fails, the convergence of the transformation can break down. This marks a boundary for a known positive result, and it bears on the broader question of when local geometric normal forms converge, which links complex dynamics and the geometry of real surfaces. The text alone does not show further consequences beyond this.
- **Background needed**: - Complex plane C and complex two-dimensional space C^2; a real surface in C^2 is a 2-dimensional real object sitting in 4 real dimensions.
- Holomorphic maps: smooth maps that respect complex structure; a convergent power series gives one.
- Formal equivalence: matching two objects using power series that may not converge; holomorphic equivalence requires a convergent change of coordinates.
- Root of unity: a complex number that is a whole-number power of 1; excluded here.
- |μ|=1: μ lies on the unit circle, so it describes a rotation.
- Brjuno condition: a number-theoretic growth condition on how well μ is approximated by roots of unity; it governs convergence of linearization in holomorphic dynamics.
- Moser–Webster invariant: a number attached to a real surface's local complex structure that controls its normal form.
- Bishop quadric: a standard model quadric surface in C^2 used as a reference example. · level: research-level

<details><summary>Original abstract</summary>

Let $\mu \in \mathbb{C}$ satisfy $|\mu|=1$, and assume that $\mu$ is not a root of unity and is not Brjuno. Let $Q_\gamma$ denote the Bishop quadric with $\gamma = 1/\sqrt{2+\mu+\mu^{-1}} > 1/2$. Gong and Stolovitch conjectured that there exists a real-analytic surface in $\mathbb{C}^2$ with Moser--Webster invariant $\mu$ that is formally but not holomorphically equivalent to $Q_\gamma$. We prove this conjecture.

</details>

## Operator algebras and spectral theory

### [Trace-class perturbations of Voiculescu's free semicircular families](https://arxiv.org/abs/2611.30882)
*Minghui Ma, Rui Shi, Tianze Wang* · `math.OA` · arXiv:2611.30882v1 · relevance 0.15

- **In one sentence**: For free semicircular families on the full Fock space, trace-class perturbations give a von Neumann algebra whose type II_1 summand is the free group factor L(F_Λ), and this yields a density result for irreducible operators in the trace-class norm.
- **In plain words**: The paper studies a family of "random-like" operators that are built in a free, non-commuting way, and then nudges each of them by a small perturbation whose total size (in a trace-class sense) is finite. It shows that the part of the resulting algebra that behaves like a finite-dimensional-style "trace" piece is still the same well-known algebra as the unperturbed case. As a side consequence, operators with no nontrivial invariant subspaces cannot be packed densely near every operator in the trace-class norm.
- **Why it matters**: The result says that a small, controlled change to free operators does not destroy their basic algebraic structure, which is useful for understanding how far such structures are stable. The stated application, about irreducible operators not being trace-class dense, is a concrete claim about the geometry of operator spaces; the text alone does not show further connections.
- **Background needed**: - Operators: linear maps on a Hilbert space (infinite-dimensional generalisation of matrices).
- Self-adjoint operator: the operator analogue of a real-valued observable.
- Trace-class operator: a "small" operator whose singular values sum to a finite number; its norm is the trace norm.
- Von Neumann algebra: a closed algebra of operators, the operator-theoretic analogue of a space of measurements.
- Type II_1 and type I/II/III: classification of von Neumann algebras; type II_1 behaves like a continuous analogue of finite matrix algebras with a normalised trace.
- Free group factor L(F_Λ): a standard example of a type II_1 von Neumann algebra, generated by free unitaries indexed by the set Λ.
- Free semicircular family: a family of non-commuting random-variable-like operators with semicircle distribution, the free analogue of Gaussian variables.
- Irreducible operator: one with no nontrivial closed invariant subspace.
- Murray–von Neumann dimension: a generalised, possibly non-integer, measure of size for projections in a von Neumann algebra. · level: research-level

<details><summary>Original abstract</summary>

Let $\{s_j\}_{j\in\Lambda}$ be the standard free semicircular family on the full Fock space $\mathcal H=\mathcal F(\ell^2(\Lambda))$, where $|\Lambda|\geqslant2$. For any family $\{K_j\}_{j\in\Lambda}$ of self-adjoint trace-class operators with $\gamma=\sum_{j\in\Lambda}\|K_j\|_1<\infty$, we prove that the type $\mathrm{II}_1$ summand $\mathcal P$ of the von Neumann algebra $W^*(\{s_j+K_j\colon j\in\Lambda\})$ is isomorphic to the free group factor $\mathcal L(\mathbb F_\Lambda)$. As an application, we show that the set of irreducible operators on a separable infinite-dimensional Hilbert space is not dense in the trace-class norm. For each fixed $\gamma>0$, the possible values of the Murray--von Neumann dimension $\dim_{\mathcal P}(z_{\mathcal P}\mathcal H)$ form the interval $[1,1+\gamma)$, where $z_{\mathcal P}$ is the identity of $\mathcal P$.

</details>

### [Algebras Generated by Two Idempotent Matrices: Classification up to Isomorphism and Applications](https://arxiv.org/abs/2611.28086)
*Rounak Biswas* · `math.RA` · arXiv:2611.28086v1 · relevance 0.13

- **In one sentence**: The paper completely classifies, up to algebra isomorphism, the algebras generated by two arbitrary complex idempotent matrices P and Q, continuing earlier joint work with Falguni Roy, and applies group invertibility in these algebras to solve a particular linear system explicitly.
- **In plain words**: This paper is about a question in pure linear algebra: when you take two "idempotent" matrices (grid-of-numbers objects that, when multiplied by themselves, give back themselves) and build the smallest algebra they generate, which of these algebras are structurally the same. The author classifies these algebras with no extra restrictions on the two matrices. The text also uses a related property, called group invertibility, to write down an explicit solution to a certain system of linear equations.
- **Why it matters**: Idempotent matrices appear in projections and related structures, so a complete classification gives a clear map of all cases. The text does not state connections to specific applications beyond the linear-equation example, so wider relevance is uncertain.
- **Background needed**: - Matrix: a rectangular array of numbers that represents a linear map.
- Idempotent: a matrix P with P squared equal to P; it acts like a projection.
- Algebra generated by P and Q: the collection of all sums and products built from P and Q (and scalars).
- Algebra isomorphism: a one-to-one correspondence between two algebras that preserves addition, multiplication and scalar multiplication, so they are the same up to renaming.
- Group invertible: a matrix A has a special inverse-like partner when A, A squared and the partner interact in a specific way; this exists exactly when the matrix's rank and nullity behave nicely.
- Classification: a complete list of types, with each algebra falling into exactly one type. · level: research-level

<details><summary>Original abstract</summary>

This paper is a continuation of the earlier work by the author and Falguni Roy \cite{biswas2025comprehensive} on the algebra \(\operatorname{alg}(P,Q)\) generated by two idempotent matrices \(P,Q\in\mathbb C^{n\times n}\). A complete classification of these algebras up to algebra isomorphism is presented, without imposing any additional restrictions on the idempotents. As an application, group invertibility in \(\operatorname{alg}(P,Q)\) is employed to obtain an explicit solution to a particular system of linear equations.

</details>

## Algebra

### [Blocks with one simple module and solvable groups](https://arxiv.org/abs/2611.29140)
*Kun Zhang, Yuanyang Zhou* · `math.GR` · arXiv:2611.29140v1 · relevance 0.19

- **In one sentence**: The paper shows that a block with a single simple module of a finite group is Morita equivalent over a suitable complete discrete valuation ring to a block of a finite solvable group, and that a block Morita equivalent to a p-group algebra is nilpotent, using equivariant bimodules and a derivation-and-transfer criterion for twisted group algebras.
- **In plain words**: This paper is about the internal structure of finite groups, studied through the algebra objects (blocks) that group representations are built from. The authors show that when such a block has only one kind of simple building piece in characteristic p, it behaves, in the precise sense of being "Morita equivalent" (having the same representation theory), like a block of a simpler kind of group called a solvable group. They also show that if such a block matches the algebra of a p-group, it must have a particularly simple, nilpotent form.
- **Why it matters**: Reducing a hard family of groups to solvable ones is a recurring goal in finite group theory and modular representation theory, so the result connects two important areas. The text does not indicate further consequences, so the wider impact is uncertain from the abstract alone.
- **Background needed**: - Finite group: a group with finitely many elements.
- Modular representation theory: studying how a group acts on vector spaces over a field whose characteristic p divides the group order.
- Block: an indecomposable piece of the group algebra, a basic building unit of representation theory.
- Simple module: an irreducible representation, the smallest non-trivial building piece.
- Morita equivalence: two algebras have the same module categories, so their representation theory is essentially identical.
- Solvable group: a group built step by step from abelian groups; simpler than general finite groups.
- Nilpotent block: a block whose structure is as close as possible to that of a p-group.
- Complete discrete valuation ring: a ring used to lift results from characteristic p to characteristic zero.
- Derivation and group transfer: algebraic tools for measuring twists and relating subgroup structure. · level: research-level

<details><summary>Original abstract</summary>

Let $b$ be a block of a finite group with one isomorphism class of simple modules in characteristic $p$. We construct, over a sufficiently large complete discrete valuation ring of characteristic zero, a Morita equivalence between $b$ and a block of a finite solvable group. The proof uses equivariant Morita bimodules for the quasisimple blocks that occur in the component reduction. We also prove that a block over an algebraically closed field of characteristic $p$ is nilpotent whenever it is Morita equivalent to the group algebra of a finite $p$-group. For the latter result, we establish a criterion for twisted group algebras using derivations of the basic algebra and group transfer.

</details>

### [On a question of A.N. Skiba concerning the modularity of the lattice of $\sigma$-permutable subgroups](https://arxiv.org/abs/2611.29478)
*Chenxiao Lin* · `math.GR` · arXiv:2611.29478v1 · relevance 0.17

- **In one sentence**: The paper characterizes finite groups whose lattice of σ-permutable subgroups is modular, answering part of a question of A.N. Skiba, and shows that when all Hall σ_i-subgroups are nilpotent, modularity is equivalent to every two members of the lattice being permutable.
- **In plain words**: The paper is about finite groups, which are collections of symmetries that can be combined, and about the subgroups inside them. The authors sort out exactly which such groups have a particular tidy structure, called a modular lattice, when we look at the family of subgroups that "mix well" with a chosen partition of the prime numbers. This answers one half of a question posed by mathematician A.N. Skiba.
- **Why it matters**: The result settles a specific open question raised by Skiba, so it matters mainly to specialists in the theory of finite groups and subgroup lattices. The text gives no wider applications, and I cannot say from it how far the ideas reach beyond this area.
- **Background needed**: - Finite group: a finite set of symmetries closed under combining them.
- Subgroup: a smaller group sitting inside a group.
- Partition of primes: splitting the prime numbers into disjoint sets σ_i.
- Hall σ_i-subgroup: a subgroup whose order involves only primes from one set σ_i, and which is maximal in that sense.
- Permutable subgroup: one that commutes, as a set, with another subgroup (A·H = H·A).
- Lattice: a partially ordered family of subgroups, with ways to take intersections and joins.
- Modular lattice: a lattice obeying a particular consistency rule about how its elements order and combine.
- Nilpotent group: a group built up in a stepwise, well-behaved way. · level: research-level

<details><summary>Original abstract</summary>

Let $\sigma=\{\sigma_i\mid i\in I\}$ be some partition of the set of all primes and let $G$ be a finite group. A subgroup $A$ of $G$ is said to be $\sigma$-permutable in $G$ if $G$ has a Hall $\sigma_i$-subgroup for every $i\in I$ and $A$ permutes with every Hall $\sigma_i$-subgroup of $G$ for all $i\in I$. We describe the finite groups $G$ for which the lattice $\Lper(G)$ of all $\sigma$-permutable subgroups of $G$ is modular. This answers the first part of a question of A.N. Skiba. We also prove that if every Hall $\sigma_i$-subgroup of $G$ is nilpotent, then $\Lper(G)$ is modular if and only if every two members of $\Lper(G)$ are permutable.

</details>

## Representation theory

### [M\"obius Fusion Algebra](https://arxiv.org/abs/2611.29234)
*Ippo Orii, Yuji Tachikawa* · `math.QA` · arXiv:2611.29234v1 · relevance 0.12

- **In one sentence**: The paper defines a generally non-commutative "Möbius fusion algebra" from a pseudo-unitary modular tensor category with an anti-monoidal involution, proves it is semisimple, and gives a dimension formula for its simple modules in terms of the modular S-matrix and data from the involution.
- **In plain words**: This paper is about a mathematical structure built from rules for combining topological "particles" drawn as graphs on a Möbius band, a surface with only one side. The authors define an algebra from these rules and show it behaves well in a precise technical sense (it is semisimple). They also give a formula for the sizes of its basic building blocks, which is meant to be a counterpart of the Verlinde formula for surfaces that are not orientable.
- **Why it matters**: The Verlinde formula is a central tool linking topological quantum field theory and fusion rules, and this paper aims at an analogue for non-orientable manifolds. The text only states this as an expectation ("is expected to play the role"), so its eventual connections remain to be seen.
- **Background needed**: - Topological quantum field theory: a framework where physical quantities depend only on the shape of a space, not on measurements of distances.
- Modular tensor category: an algebraic structure of anyon-like objects and how they fuse and braid; used to build such theories.
- Fusion algebra: an algebra recording how objects combine, with multiplication given by fusion rules.
- S-matrix: a matrix describing how the basic objects transform under changes of viewpoint on a surface; it controls the Verlinde formula.
- Orientable vs non-orientable surfaces: orientable surfaces have a consistent notion of left and right; the Möbius band does not.
- Semisimple algebra: an algebra that decomposes cleanly into simple pieces, with no hidden nilpotent parts.
- Involution: a map that applied twice returns the original; here, an anti-monoidal one acting on the category. · level: research-level

<details><summary>Original abstract</summary>

Given a pseudo-unitary modular tensor category $\mathcal{C}$ with an anti-monoidal involution $\mathsf{P}$, we define a generally non-commutative algebra from this data, which we call the M\"obius fusion algebra $\mathfrak{M}$ of $(\mathcal{C},\mathsf{P})$, in terms of ribbon graphs drawn on the M\"obius band, where the orientation-reversal of the M\"obius band acts on the graphs by $\mathsf{P}$. We show that this algebra is semisimple, and give a formula for the dimensions of its simple modules, in terms of the modular $S$-matrix of $\mathcal{C}$ and a certain set of quantities extracted from the action of $\mathsf{P}$. This formula is expected to play the role of a non-orientable analogue of the Verlinde formula, in the context of Reshetikhin-Turaev-type topological quantum field theories on non-orientable manifolds.

</details>

### [Inner derivations and automorphism groups of vertex operator algebras](https://arxiv.org/abs/2611.28814)
*Jianzhi Han* · `math.QA` · arXiv:2611.28814v1 · relevance 0.11

- **In one sentence**: For a simple, rational, C_2-cofinite vertex operator algebra of CFT type, the zero-mode map from weight-one vectors to derivations is shown to be a Lie algebra isomorphism, which identifies inner automorphisms as the identity component of the full automorphism group and gives dim Aut(V) = dim V_1.
- **In plain words**: This paper is about the symmetries of a particular algebraic structure that appears in conformal field theory, a branch of physics and mathematics that studies idealized quantum systems. The author shows that a certain natural correspondence between the structure's weight-one part and its derivations (rules that behave like differentiation) is exact in both directions. From this, the symmetry group is pinned down: its size is set by the dimension of the weight-one part, and it is finite only when that part is zero.
- **Why it matters**: The result gives a precise count of the symmetries of these structures in terms of a single dimension, which is the kind of classification statement specialists look for. The text does not say how far it extends beyond the stated hypotheses, so its wider reach is unclear from this excerpt alone.
- **Background needed**: - Vertex operator algebra (VOA): an algebraic object from conformal field theory, a model of symmetry in two-dimensional quantum physics.
- Weight grading: the VOA splits into pieces V_n indexed by a "weight" (roughly an energy level); V_1 is the weight-one piece.
- Lie algebra: a vector space with a bracket operation, here built from derivations.
- Derivation: a linear map obeying a product rule, like the ordinary derivative.
- Automorphism group Aut(V): the structure-preserving symmetries of V; Inn(V) are those generated by exponentiating derivations.
- Identity component: the connected piece of a continuous group containing the identity.
- Hypotheses: simple, rational, C_2-cofinite, CFT type are technical finiteness and niceness conditions.
- Zhu's algebra and characters: tools that encode the structure through a finite-dimensional algebra and generating functions counting dimensions. · level: research-level

<details><summary>Original abstract</summary>

Let $V$ be a simple, rational, $C_2$-cofinite vertex operator algebra of CFT type. We prove that the zero mode map $V_1\to\operatorname{Der}(V)$, $h\mapsto h_0$, is an isomorphism of Lie algebras. We prove surjectivity using traces on finite sums of weight spaces and Li's module construction, and injectivity using the vacuum character of Zhu's algebra. It follows that $\operatorname{Inn}(V)$ is the identity component of $\operatorname{Aut}(V)$ and has finite index in $\operatorname{Aut}(V)$. Moreover, $\operatorname{dim}\operatorname{Aut}(V)=\dim V_1$, so $\operatorname{Aut}(V)$ is finite if and only if $V_1=0$.

</details>

## Number theory

### [On the number theory of the Greeks. I. The Fundamental Theorem of Arithmetic](https://arxiv.org/abs/2611.29380)
*Franz Lemmermeyer* · `math.NT` · arXiv:2611.29380v1 · relevance 0.21

- **In one sentence**: A historical study arguing that Euclid's version of the fundamental theorem of arithmetic (unique prime factorization) was widely known to pre-Gauss number theorists, despite being largely forgotten today.
- **In plain words**: This paper is about the history of a basic math idea: every whole number larger than one can be built from prime numbers in only one way. The author says Euclid stated this long ago, and that it was as familiar to mathematicians before Gauss as Gauss's later version is to us today. The text is a short introduction, so it does not show the detailed evidence it promises.
- **Why it matters**: It challenges the common story that this theorem entered number theory mainly through Gauss, which matters for how we credit and understand the history of mathematics. The excerpt gives only the opening claim, so the strength of the evidence cannot be judged from it alone.
- **Background needed**: - Prime number: a whole number greater than 1 with no divisors other than 1 and itself (e.g., 2, 3, 5, 7).
- Fundamental theorem of arithmetic: every whole number above 1 is a product of primes, and that product is unique apart from the order of the factors (e.g., 12 = 2×2×3 and no other way).
- Euclid: ancient Greek mathematician whose "Elements" (around 300 BCE) is a foundational geometry and number theory text.
- Gauss: Carl Friedrich Gauss, who in 1801 gave a rigorous, widely cited statement and proof of the theorem in modern form.
- Historiography: the study of how mathematical ideas were recorded, credited and forgotten over time. · level: intermediate

<details><summary>Original abstract</summary>

In this article we present Euclid's fundamental theorem of number theory and give evidence for the claim that this theorem, which is largely unknown today, was as familiar to number theorists before Gauss as the Gaussian version of the fundamental theorem is to us.

</details>

### [A Classification of Low Genus Modular Curves](https://arxiv.org/abs/2611.30908)
*Eray Karabiyik* · `math.NT` · arXiv:2611.30908v1 · relevance 0.19

- **In one sentence**: The paper classifies modular curves X_G of a fixed genus g (for open G in GL_2 of the profinite integers with full determinant and -I in G), shows they fall into finitely many families of Q^ab-twists, and gives an algorithm for computing these families and projective models, implemented for g ≤ 12.
- **In plain words**: The paper studies a family of geometric shapes, called modular curves, that encode how elliptic curves (smooth curves defined by cubic equations) can carry extra structure. The authors show that for any fixed "size" of shape, measured by genus (roughly the number of holes), all such curves belong to a finite number of families. They also describe a computer procedure for listing these families and writing down equations for them, which they have run for genus up to 12.
- **Why it matters**: Knowing which modular curves have low genus matters for questions about rational points and elliptic curves over number fields, so a complete classification is a useful reference point. The text does not say what specific consequences the authors expect, so the wider impact is uncertain from this abstract alone.
- **Background needed**: - Elliptic curve: a smooth plane cubic curve with a group law; the basic object being parametrized.
- Modular curve: a curve whose points correspond to elliptic curves together with a chosen kind of extra structure (a level structure), indexed by a subgroup G of GL_2 of the profinite integers.
- Genus: a whole-number measure of a curve's shape, roughly how many holes it has; genus 0 curves are spheres-like and are easiest to handle.
- Twist: a related curve obtained by changing the defining equations by a twisting factor; Q^ab-twists use abelian extensions of the rational numbers.
- Projective model: writing the curve as the zero set of polynomial equations in projective space.
- Determinant condition and -I in G: technical constraints on the group G that fix which curves are considered. · level: research-level

<details><summary>Original abstract</summary>

Let $G$ be an open subgroup of $\mathrm{GL}_2(\widehat{\mathbb{Z}})$ satisfying $\det(G)=\widehat{\mathbb{Z}}^{\times}$ and $-I\in G$. Associated to $G$, there is a modular curve $X_G$ defined over $\mathbb{Q}$ which parametrizes elliptic curves with $G$-level structure. We give a classification of modular curves with genus equal to a fixed nonnegative integer $g$. In particular, we show that all modular curves of genus $g$ lie in finitely many families of $\mathbb{Q}^{\mathrm{ab}}$-twists of modular curves. We also describe an algorithm for computing all families of modular curves of a fixed genus $g$ and use this to compute projective models for these modular curves. This algorithm has been fully implemented for $g \leq 12$. In an appendix with Yongyuan Huang and Rakvi, we describe two algorithms, one for computing rational functions on modular curves given as quotients of two modular forms of the same weight, and the other for computing models for the generic fibers of universal elliptic curves $\mathcal{E}_G$, where $G\subset \mathrm{GL}_2(\widehat{\mathbb{Z}})$ is an open subgroup satisfying $\det(G)=\widehat{\mathbb{Z}}^{\times}$ and $-I\notin G$.

</details>

## Algebraic geometry

### [Functionals commuting with reparametrizations](https://arxiv.org/abs/2611.30506)
*Pierre-Emmanuel Chaput, David Dos Santos Ferreira, Valentin F\'eray* · `math.AG` · arXiv:2611.30506v1 · relevance 0.13

- **In one sentence**: The paper classifies the algebraic functionals from n-tuples of polynomials vanishing at 0 to such polynomials that commute with right-composition (reparametrization), introducing a "semi-product" operation and linking the problem to polyharmonic functions on the positive discrete orthant and the type A co-invariant algebra.
- **In plain words**: The authors study rules that take several functions and combine them into one, in a way that stays consistent when you change the parameter of the curves involved. They restrict to polynomials that vanish at zero and give a complete description of the algebraic rules of this kind. The description uses a new operation they call the "semi-product".
- **Why it matters**: The problem is motivated by tangent curve bundles of algebraic varieties, so it sits at the meeting point of algebraic geometry and combinatorial algebra. The text also mentions a generalization to colored permutations and open versions for truncated polynomials and smooth functions, so the work is a starting point rather than a closed topic; the broader significance beyond these links is not stated in the text.
- **Background needed**: - Polynomials: finite sums of powers of a variable; "vanishing at 0" means the constant term is zero.
- Reparametrization: replacing a parameter t by a function of t, i.e. composing a curve with another function.
- Functional: a rule that takes functions as inputs and returns a function.
- Polyharmonic function: a discrete function on a grid whose repeated discrete Laplacian (a "smoothness" operator) vanishes.
- Co-invariant algebra of type A: a finite-dimensional algebra built from the symmetric group acting on variables, a standard object in combinatorics.
- Tangent curve bundle: a family of curves attached to each point of an algebraic variety, describing its local directions. · level: research-level

<details><summary>Original abstract</summary>

Motivated by the study of tangent curve bundles of algebraic varieties, we consider the following simple-looking problem: given a space $E$ of functions, describe functionals from $E^n$ to $E$ which commutes with reparametrizations, i.e. with the right-composition with an element of $E$. Our main result is a complete description of the algebraic solutions of this problem when $E$ is the space of polynomials vanishing in $0$, which we denote by $\mathbb C[T]_0$. This description involves a simple operation, which we call semi-product, with interesting algebraic and geometric properties. The proof involves the study of polyharmonic functions on the positive discrete orthant $\mathbb Z^n_{>0}$, and a relation with the co-invariant algebra of type $A$. We also provide a generalization connected to colored permutations, and discuss the analogue problems where $E=\mathbb C[T]_0/(T^\ell)$ for some $\ell >0$, and where $E$ consists of infinitely differentiable functions. Finding a complete description of algebraic solutions in these settings is still open.

</details>

### [The generalized Franchetta conjecture for some hyper-K\"ahler varieties, III](https://arxiv.org/abs/2611.29599)
*Lie Fu, Robert Laterveer, Carl Mazzanti et al.* · `math.AG` · arXiv:2611.29599v1 · relevance 0.12

- **In one sentence**: This paper proves the generalized Franchetta conjecture (injectivity of the cycle class map on generically defined cycles) for the families of double EPW sextics and double EPW cubes, and shows multiplicativity of the Chow-Künneth decomposition for special Gushel-Mukai fourfolds and all Gushel-Mukai sixfolds.
- **In plain words**: The paper is about families of higher-dimensional geometric shapes called hyper-Kähler varieties, which are studied through the algebraic "cycles" (sub-shapes such as points, curves and surfaces) that sit inside them. The authors check a conjecture for two specific families, asking whether these sub-shapes can be told apart by their cohomology, a coarser topological fingerprint of the shape. The method works by relating these families to Gushel-Mukai fourfolds, using a construction in which the varieties are moduli spaces of stable objects in a derived category.
- **Why it matters**: Results of this kind test how much algebraic information about a family is captured by its topological invariants, a central question in the study of algebraic cycles. The text does not state wider consequences beyond the relation between double EPW sextics and Gushel-Mukai fourfolds on the level of motives, so the broader impact is uncertain from this excerpt alone.
- **Background needed**: - Algebraic geometry studies solutions of polynomial equations as geometric objects (varieties).
- A hyper-Kähler variety is a higher-dimensional analogue of a K3 surface, with special symmetry and structure.
- A family or moduli space parametrizes many such varieties at once; the "universal family" sits over the parameter space.
- Cycles are algebraic sub-varieties (of a given dimension) inside a variety; the cycle class map sends each cycle to its cohomology class, a topological invariant.
- The generalized Franchetta conjecture says these cycle classes on a generic fiber remain distinct in cohomology, i.e. the map is injective.
- A Chow-Künneth decomposition splits the motive of a variety into pieces; "multiplicative" means it respects products of varieties.
- Gushel-Mukai fourfolds and sixfolds, double EPW sextics and cubes are specific families studied in this area; Bridgeland stability is a tool from derived categories.
- This is the third paper in a series. · level: research-level

<details><summary>Original abstract</summary>

The generalized Franchetta conjecture states that for a locally complete family of polarized hyper-K\"ahler varieties, the generically defined cycles on any fiber of the universal family over the moduli stack inject into cohomology via the cycle class map. We prove the generalized Franchetta conjecture for the family of double EPW sextics discovered by O'Grady and for the family of double EPW cubes discovered by Iliev-Kapustka-Kapustka-Ranestad. We also prove a Franchetta-type result for the relative square of the universal family of double EPW sextics, which allows to relate double EPW sextics and Gushel-Mukai fourfolds on the level of motives. The proof involves the geometry of Gushel-Mukai fourfolds, whose Kuznetsov component allows to realize double EPW sextics and cubes as moduli spaces of Bridgeland-stable objects, relatively over the parameter space of Gushel-Mukai fourfolds. A key step is that the canonical Chow-K\"unneth decomposition of special Gushel-Mukai fourfolds is multiplicative; we use this to show that generically defined cycles on the third power of a special Gushel-Mukai fourfold inject into cohomology via the cycle class map. Along the way, we also show that the canonical Chow-K\"unneth decomposition of any Gushel-Mukai sixfold is multiplicative.

</details>

## Topology

### [A complete knot invariant from grid diagrams](https://arxiv.org/abs/2611.30095)
*Agnese Barbensi, Daniele Celoria, Lavender Marshall et al.* · `math.GT` · arXiv:2611.30095v1 · relevance 0.12

- **In one sentence**: The paper builds an infinite graph from grid diagrams of a knot and proves that its isomorphism class is a complete invariant of the knot up to mirror image, with finite algorithmically determinable portions of the graph sufficing to identify the knot type.
- **In plain words**: A knot is a closed loop tangled in three-dimensional space, like a tangled shoelace with the ends joined. This paper studies a way to describe any knot by a mathematical graph built from a square grid drawing of it. The authors show that this graph captures the knot completely, up to reflection in a mirror, and that only a finite, computable piece of the graph is needed to pin down which knot it is.
- **Why it matters**: Deciding whether two knots are the same is a classic hard problem in topology, so a complete invariant that can be computed algorithmically is of interest to specialists. The text does not say how practical the method is or how it compares with existing knot invariants, so its wider significance is uncertain.
- **Background needed**: - Knot: a closed loop in space that cannot be untangled without cutting it; two knots are the same if one can be deformed into the other without cutting.
- Knot invariant: a property or number computed from a knot that is the same for equivalent knots; a complete invariant determines the knot fully.
- Grid diagram: a knot drawn on an n-by-n square grid, with vertical segments always passing over horizontal ones, which lets a knot be encoded as a finite combinatorial object.
- Graph: a set of points (vertices) joined by edges; isomorphism means two graphs have the same structure up to relabeling.
- Mirror image: the reflected version of a knot; the result identifies knots only up to mirroring, so left- and right-handed versions are not distinguished.
- Algorithmic: computable by a step-by-step procedure in finite time. · level: research-level

<details><summary>Original abstract</summary>

Using grid diagrams, we define an infinite graph associated to each knot type. We prove that the isomorphism class of this grid graph is a complete invariant of the knot, up to mirroring. Even more, we prove that algorithmically determinable finite parts of this graph are enough to determine the knot type.

</details>

### [Unknotting number is strictly subadditive for the trefoil](https://arxiv.org/abs/2611.29233)
*Anne Dranowski, Yura Kabkov, Daniel Tubbenhauer* · `math.GT` · arXiv:2611.29233v1 · relevance 0.11

- **In one sentence**: The paper shows that the unknotting number is strictly subadditive for the trefoil: a trefoil paired with a certain fourteen-crossing knot needs fewer total crossing changes to unknot together than separately, and this saving extends to infinitely many prime partners and to positive braid knots and torus knots.
- **In plain words**: This paper is about knots, the tangled loops of string studied in topology. For a knot, the unknotting number counts the fewest times you must pass one strand through another to turn it into a plain loop. The paper checks whether combining two knots can ever be cheaper to undo than handling each one separately, and finds that it can, using the trefoil (the simplest non-trivial knot) and a specific fourteen-crossing knot as the example.
- **Why it matters**: The question of whether this quantity adds up exactly when knots are joined was an open question in knot theory, so a clear counterexample family is of interest to specialists. The text does not indicate further applications, and I am not sure how far the result reaches beyond knot theory.
- **Background needed**: - A knot is a closed loop of string embedded in space, considered up to bending and stretching but not cutting.
- The unknot is the plain circle with no tangles.
- A crossing change swaps which strand passes over at one crossing.
- The unknotting number is the minimum number of crossing changes needed to reach the unknot.
- Subadditivity means the unknotting number of a combined knot is at most the sum of the parts; strict subadditivity means it is sometimes strictly less.
- The trefoil is the simplest non-trivial knot; positive braid knots and torus knots are standard families of knots.
- A prime knot cannot be split as a connected sum of two non-trivial knots. · level: research-level

<details><summary>Original abstract</summary>

A trefoil and a certain fourteen-crossing knot take four crossing changes to unknot separately and at most three together. We extend this example to infinitely many prime partners and show that the same partners give a saving for every nontrivial positive braid knot and, up to mirror, every nontrivial torus knot.

</details>

## Dynamical systems

### [KAM theory for contact Hamiltonian systems](https://arxiv.org/abs/2611.28587)
*Zhicheng Tong, Yong Li, Xuefeng Zhao* · `math.DS` · arXiv:2611.28587v1 · relevance 0.14

- **In one sentence**: The paper proves frequency-preserving KAM theorems for full-dimensional Legendrian tori in analytic contact Hamiltonian families, in both finite and infinite dimensions, and links the resulting invariant tori to analytic solutions of stationary Hamilton–Jacobi equations and weak KAM theory.
- **In plain words**: The paper studies damped or dissipative mechanical-type systems whose motion is quasi-periodic, meaning it runs on a torus with several incommensurate rhythms, and asks whether such motion survives small perturbations. The authors show that, after suitable tuning of parameters, these invariant tori persist with the same rhythms, and the motion on each torus can be written in a clean analytic form. In finite dimensions they add that, under extra convexity assumptions, the torus solution is the unique weak KAM solution in both time directions.
- **Why it matters**: Persistence of quasi-periodic motion under perturbation is a central question in dynamics, and extending KAM-type results to contact (dissipative-like) systems is a less-studied direction. The link to weak KAM theory, which connects dynamics with solutions of Hamilton–Jacobi equations, is the main conceptual bridge; the text does not establish applications beyond this.
- **Background needed**: - Hamiltonian system: a model of motion (from mechanics) described by energy-like functions and their rates of change.
- Contact Hamiltonian system: a generalization that includes a damping or dissipation term via an extra "contact" variable.
- KAM theory: results showing that quasi-periodic motion on invariant tori survives small perturbations, provided the rhythms are suitably non-resonant.
- Torus and quasi-periodic flow: motion winding around a donut-shaped surface with rhythms that never exactly repeat.
- Legendrian torus: a special half-dimensional-type geometric object compatible with the contact structure.
- Analytic: smooth in a strong sense (locally given by convergent power series).
- Hamilton–Jacobi equation and weak KAM solution: a partial differential equation whose solutions describe the long-run behavior of the dynamics.
- Tonelli assumptions: convexity and growth conditions on the energy function, standard in this field. · level: research-level

<details><summary>Original abstract</summary>

In both finite and infinite dimensions, we establish the first frequency-preserving KAM theorems for full-dimensional Legendrian tori in contact Hamiltonian families with general analytic coupling between the momenta and the contact variable. After adjustment of external parameters, the flow on each torus is analytically conjugate in the original time to the prescribed translation, with estimates uniform as the damping parameter crosses zero. This coupling can generate nonzero mean damping at first order even when the damping parameter vanishes. In finite dimensions, nonzero mean damping yields a time-preserving analytic contact linearization near the torus. In both settings the invariant graphs give global analytic solutions of stationary Hamilton--Jacobi equations whose characteristic flows are conjugate to the prescribed translation. A novel consequence in finite dimensions is that, under global Tonelli assumptions and strict increase in the contact variable, this analytic solution is both the unique forward and the unique backward weak KAM solution, and its associated Legendrian graph is an invariant torus carrying quasi-periodic dynamics.

</details>

### [One-shot identification of analytic systems](https://arxiv.org/abs/2611.30470)
*Nicolas Boull\'e, Diana Halikias, Samuel E. Otto et al.* · `math.NA` · arXiv:2611.30470v1 · relevance 0.11

- **In one sentence**: The paper gives a zero-one law for when the coefficients of a linearly parameterized analytic system can be recovered from one input-solution pair, with the failure set shown to be negligible unless it is the whole input space, and applies this to matrices, continuous-time dynamical systems, and differential operators.
- **In plain words**: The paper asks whether the unknown settings of a system, such as the numbers inside a set of equations describing how something changes over time, can be worked out from just one recorded input and the output it produces. The authors show that for almost every input the answer is yes, unless the answer is no for every input. For several classes of differential equations they also describe exactly which inputs fail and suggest specific inputs that are guaranteed to work.
- **Why it matters**: Identifying a system from a single experiment is useful when repeated experiments are costly or impossible. The text does not say how these results compare with existing identification methods or what practical applications are planned, so the wider significance is unclear from this text alone.
- **Background needed**: - A dynamical system is a rule describing how a state evolves over time, often written as an ordinary differential equation (ODE) or a partial differential equation (PDE).
- "Analytic" means the functions involved are smooth enough to be written as convergent power series.
- "Linearly parameterized" means the unknown coefficients enter the system in a linear way, so recovery reduces to solving a linear map.
- Injective means that different coefficient choices always produce different outputs, so the coefficients can be uniquely recovered.
- A set is "negligible" here if it has zero measure, meaning it takes up no volume under random Gaussian sampling of inputs.
- Gaussian measure is a standard way of randomly choosing inputs, with a bell-shaped distribution. · level: research-level

<details><summary>Original abstract</summary>

We study when the coefficients of a linearly parameterized analytic system can be identified from a single input-solution pair. Given a finite dictionary of analytic operators, each admissible input induces a finite-dimensional linear recovery map from coefficients to observed outputs. Coefficient recovery is possible exactly when this map is injective. We define the degenerate input set as the set of inputs for which injectivity fails and prove a zero-one law: either every admissible input is degenerate, or the degenerate set is negligible in the sense that it is compactly slice-null and has zero measure under every nondegenerate Gaussian measure. We then apply this framework to the recovery of matrices, analytic continuous-time dynamical systems, and differential operators. For several ODE and PDE classes, we further characterize the degenerate sets explicitly and identify deterministic choices of inputs that guarantee recovery.

</details>

## Combinatorics

### [The maximum number of edges in minimal $k$-extendable bipartite graphs](https://arxiv.org/abs/2611.29504)
*Xiaoling He* · `math.CO` · arXiv:2611.29504v1 · relevance 0.14

- **In one sentence**: The paper confirms a conjectured edge-count upper bound, (2k+1)(|V|-2k)/2, for minimal k-extendable bipartite graphs when k is at least 3, and shows the bound is sharp for even orders at least 6k.
- **In plain words**: This paper is about graphs, which are networks of dots joined by lines, and about how many lines such a network can have while still having a robust pairing structure. A graph is "k-extendable" if any k non-overlapping pairings can always be completed to a full pairing of all dots, and "minimal" means that removing any single line destroys this property. The authors prove a conjectured maximum on the number of lines for the bipartite (two-sided) case when k is at least 3, and show the maximum is actually reached.
- **Why it matters**: It settles a open conjecture from a recent paper and extends earlier results for k=1 and k=2 to all larger k from 3 onward. It is a precise, self-contained result in extremal graph theory, and its relevance beyond that field is not addressed in the text.
- **Background needed**: - Graph: dots (vertices) joined by lines (edges).
- Matching: a set of lines that share no dots; a perfect matching pairs up every dot.
- Bipartite graph: dots split into two sides, with lines only between sides.
- k-extendable: every matching of size k extends to a perfect matching; the graph must also be connected with at least 2k+2 dots.
- Minimal: removing any one line breaks k-extendability.
- Extremal bound: a formula giving the largest possible number of lines; "sharp" means some graph actually attains it.
- Known prior results: the k=1 bound (Lovász and Plummer, 1977) and the k=2 bound (Fabres, Kothari and Carvalho, 2021). · level: research-level

<details><summary>Original abstract</summary>

A connected graph of order at least $2k+2$ is {\em $k$-extendable} if it has a matching of size $k$ and every such matching extends to a perfect matching. In particular, a 1-extendable graph is also called a {\em matching covered graph}. A $k$-extendable graph $G$ is {\em minimal} if $G-e$ is not $k$-extendable for every $e\in E(G)$. Lov\'asz and Plummer [J. Combin. Theory Ser. B 23 (1977), 127--138] proved that every minimal matching covered bipartite graph $G$ with $|V(G)|\ge6$ satisfies $|E(G)|\le(3|V(G)|-6)/2$, and this bound is sharp for every even order at least 6. Fabres, Kothari and Carvalho [J. Graph Theory 96 (2021), 490--509] proved that every minimal 2-extendable bipartite graph $G$ with $|V(G)|\ge12$ satisfies $|E(G)|\le(5|V(G)|-20)/2$. Very recently, Mallik, Diwan and Kothari [J. Combin. 17 (2026), 559--606] characterized minimal matching covered bipartite graphs $G$ with $|E(G)|=(3|V(G)|-6)/2$ in terms of special trees. They also conjectured that, for every integer $k\ge1$, there exists an integer $N_k\le4k^2+2k$ such that every minimal $k$-extendable bipartite graph $G$ with $|V(G)|\ge N_k$ satisfies $|E(G)|\le(2k+1)(|V(G)|-2k)/2$. In this paper, we confirm this conjecture for $k\ge3$ and prove that the upper bound is sharp for every even order at least $6k$ ($k\ge3$).

</details>

### [Local Limits and Structures of Nearest-Predecessor Random Graphs](https://arxiv.org/abs/2611.29929)
*Xiaoyao Huang* · `math.PR` · arXiv:2611.29929v1 · relevance 0.13

- **In one sentence**: The paper constructs infinite local limits of two random "nearest-predecessor" graph models built from uniformly random insertion orders, proves Benjamini–Schramm convergence, and settles Ponomarenko's maximum-degree question for the two-sided version.
- **In plain words**: The paper studies a random network grown one vertex at a time: points arrive in a random order, and each new point links to the nearest point that arrived earlier (on each side, or among the K nearest earlier points in the second model). It shows that as the network gets large, what a typical neighborhood looks like converges to a fixed infinite random graph, and it gives results about that infinite graph's connectivity, recurrence, and degrees.
- **Why it matters**: The paper answers an open question posed by Ponomarenko, namely the growth rate of the maximum degree, with an explicit asymptotic of log n / log(3/2). Its local-limit approach is a standard way to connect finite random structures to infinite ones, but the text does not say how far the methods reach beyond these models.
- **Background needed**: - A graph is a set of vertices joined by edges; the degree of a vertex is how many edges it has.
- Benjamini–Schramm convergence: a way of saying a large random graph looks, locally around a typical vertex, like a fixed infinite graph.
- "Quenched" means the convergence holds for almost every fixed realization of the randomness, not just on average.
- One-ended: removing a finite set of vertices leaves exactly one infinite piece. Recurrent: a random walk on the graph returns to its start with probability one.
- Planar: can be drawn on a plane without crossing edges. Nonplanar is the opposite.
- Insertion times: i.i.d. continuous random values that give each vertex its arrival order.
- Probability generating function and CLT (central limit theorem): tools describing the distribution of a count and its approximate bell-curve behavior for large samples. · level: research-level

<details><summary>Original abstract</summary>

We study the two-sided nearest-predecessor graph on $[n]$, where vertices arrive in a uniformly random order and each new vertex connects to its nearest earlier vertex on each side. We construct an infinite graph on $\mathbb{Z}$ from i.i.d. continuous insertion times and prove quenched Benjamini--Schramm convergence to it almost surely. The limit is almost surely one-ended and recurrent. We resolve an open problem of Ponomarenko by proving that the maximum degree is asymptotic in probability to $\log n/\log(3/2)$ as $n\to\infty$. We obtain the probability generating function and a CLT for the number of edges crossing the boundary of $[n]$ in the infinite limit. We also study the $K$-nearest-predecessor graph, in which each new vertex attaches to its $K$ nearest earlier vertices without regard to side. For every fixed $K\geq1$, we construct the infinite limit, prove almost sure quenched Benjamini--Schramm convergence, and show that it is almost surely connected, one-ended, and recurrent, as well as nonplanar when $K\geq2$.

</details>

## Numerical analysis

### [Irreducible shallow tanh neural networks are a manifold](https://arxiv.org/abs/2611.30553)
*Ivan Bioli, Isabella Carla Gonnella, Carlo Marcati et al.* · `cs.LG` · arXiv:2611.30553v1 · relevance 0.13

- **In one sentence**: The paper proves that shallow tanh neural networks with no redundant neurons (irreducible in Sussmann's sense) form a smooth embedded submanifold of Sobolev spaces on bounded sets, and counts its connected components (n+1 for scalar input and output, connected otherwise).
- **In plain words**: The paper studies the collection of all functions that a small neural network with a particular kind of smooth "switch" function (tanh) can produce. It looks only at networks where no neuron is wasted or duplicated, and shows that this collection forms a smooth, curved surface-like shape inside a larger space of functions. It also counts how many separate pieces that shape falls into.
- **Why it matters**: Knowing the geometry of the set of functions a network can represent helps explain how training and approximation behave, since optimization runs over this shape. The text does not say what practical consequences follow, so the broader impact is uncertain.
- **Background needed**: - A neural network here is a function built from n hidden neurons, each applying tanh to a weighted sum of inputs, then combined linearly.
- Tanh is a smooth S-shaped function; "shallow" means one hidden layer.
- Sussmann's "irreducible" networks are those with no redundant neurons, e.g. no two neurons that cancel or merge.
- A smooth embedded submanifold is a curved shape without self-intersections that locally looks like flat space.
- Sobolev spaces W^{l,p} are function spaces measuring a function's size together with the sizes of its derivatives up to order l, in an L^p sense.
- Connected components are separate pieces; a shape with n+1 components cannot be reached from one piece to another by continuous paths. · level: research-level

<details><summary>Original abstract</summary>

Neural networks (NNs) have been increasingly used as function approximators, motivating the study of the geometry of their function spaces. We study the set of functions represented by shallow neural networks with hyperbolic tangent activation, fixed input and output dimensions, and $n$ hidden neurons. In particular, we prove that the subset represented by irreducible networks in the sense of Sussmann (Neural Networks, 1992), i.e., networks with no redundant neurons, is a smooth embedded submanifold of the Sobolev spaces $\mathrm{W}^{\ell,p}$ on bounded sets for any $\ell\in\mathbb{N}$ and $p\in[1,+\infty]$. The key step is to show that if a sequence of networks converges in $\mathrm{W}^{\ell,p}$ to an irreducible network with the same number of hidden neurons, then the parameters of the approximating networks remain bounded. Finally, we show that this manifold has exactly $n+1$ connected components when both the input and output are scalar, and is connected otherwise.

</details>

### [Hierarchical randomized neural networks for efficiently and accurately finding multiple solutions of semilinear elliptic equations](https://arxiv.org/abs/2611.30010)
*Jingying Hu, Jiao Li, Yufeng Xu et al.* · `math.NA` · arXiv:2611.30010v1 · relevance 0.13

- **In one sentence**: A randomized-neural-network method, with SVD-based initialization, exponential-deflation Gauss-Newton optimization, and a hierarchical multilevel acceleration, for finding multiple solutions of semilinear elliptic PDEs.
- **In plain words**: This paper addresses a common problem in scientific computing: a certain class of equations describing physical systems can have several different solutions, and it is hard to find all of them. The authors propose a computational method that uses a neural network with randomly fixed internal parts, plus a search procedure that steers away from solutions already found. According to the text, the method finds multiple solutions without prior knowledge of them, reaches relative errors around 10^-16 in numerical tests, and does so at under one-tenth of the computational cost in the best case.
- **Why it matters**: Finding all solutions of nonlinear equations matters for modeling pattern formation and similar physical problems, where different solutions can correspond to different states. The text reports numerical tests only, so its practical reach beyond the tested problems is not established here.
- **Background needed**: - Semilinear elliptic equation: a type of partial differential equation describing steady-state physical behavior, such as heat or diffusion with a nonlinear term.
- Multiple solutions: one equation can have several distinct valid answers, and finding all of them is the goal.
- Randomized neural network: a network whose hidden-layer weights are set randomly and only the output layer is fitted, which makes training cheaper.
- Gauss-Newton method: an iterative numerical method for solving nonlinear equations.
- Deflation: a technique that modifies the equation so already-found solutions are avoided, letting the search find new ones.
- Singular value decomposition (SVD): a matrix factorization used here to pick search directions.
- Multilevel method: solving the problem on coarse and fine versions in sequence to speed up computation and improve accuracy.
- Relative error: the size of the error compared with the size of the true answer. · level: research-level

<details><summary>Original abstract</summary>

Being able to find multiple solutions of a semilinear elliptic equation is a fundamental problem in scientific computing. In this paper, fully taking the advantages of randomized neural networks, we propose a new efficient and accurate method for identifying potentially as many solutions as possible. The new method is constructed from three aspects--initialization, optimization, a technique for acceleration and improving accuracy, two of which are innovative developments. Firstly, based on the basis functions of a randomized network and the sampling points, a characteristic matrix is introduced so that its singular value decomposition can be used to determine weakly variant search directions, followed by a newly developed algorithm to generate effective initial candidates. Then the good deflated Gauss-Newton method [see {\em A. Riley, et al., SIAM Journal on Scientific Computing 47~(5) (2025) A2963-A2987}] using an exponential deflation operator is adapted as the optimization to search for all multiple solutions. Local error estimate of a particular solution under some proper condition is given in terms of the neurons in the hidden layer and the sampling points for this newly designed method. Furthermore, to accelerate the computation and improve the solution accuracy, a new multilevel method based on hierarchical networks is designed. Without using any {\em a priori} information, several numerical tests show together with the multilevel method, the new method can not only accurately find multiple solutions with relative errors reaching $10^{-16}$ only in less than one-tenth computational cost for the best case, but also preserve the inherent symmetries of multiple solutions.

</details>

## Logic and foundations

### [Equivalence of Cohen generics is hyperfinite](https://arxiv.org/abs/2611.30679)
*Iian B. Smythe* · `math.LO` · arXiv:2611.30679v1 · relevance 0.15

- **In one sentence**: The paper shows that the equivalence relation "two Cohen generic reals yield the same generic extension" over a countable model of set theory is hyperfinite, answering a question posed by the author, via asymptotic separation.
- **In plain words**: This is a result in mathematical logic about "random-like" real numbers that are generic over a countable model of set theory, a kind of carefully chosen random object used to build new mathematical universes. The question is when two such numbers generate the same new universe. The paper shows that this sameness relation is "hyperfinite," meaning it can be approximated by a sequence of finite-level pieces, which answers a question the author had asked.
- **Why it matters**: The result settles an open question in the classification theory of equivalence relations, a area that studies how hard it is to decide when two objects count as the same. The text does not say how far the method reaches beyond this specific case, so wider connections are uncertain.
- **Background needed**: - Real numbers and countable models: a countable model of set theory is a countable collection of sets obeying the usual axioms, used as a base for building bigger universes.
- Cohen generic real: a real number that avoids all the sets that could be named inside the model; it is the standard way to add new objects to a universe ("forcing").
- Generic extension: the larger universe obtained by adding a generic real to the model.
- Equivalence relation: a rule saying when two objects are "the same" for a given purpose, splitting objects into classes.
- Hyperfiniteness: a measure of simplicity for equivalence relations; such a relation can be approximated by finite pieces arbitrarily well.
- Asymptotic separation: a technique for showing that certain sequences of sets or events become distinguishable in the limit; the text names it as the main tool without detailing it. · level: research-level

<details><summary>Original abstract</summary>

It is shown that the equivalence relation on Cohen generic reals over a countable model of set theory, where two are equivalent if they produce the same generic extension, is hyperfinite, answering a question of the author. The proof uses asymptotic separation and is a digestion of an argument originally produced by GPT-6.

</details>

### [Dense ideals in forcing extensions of Nairian models](https://arxiv.org/abs/2611.28226)
*Rahman Mohammadpour, Grigor Sargsyan* · `math.LO` · arXiv:2611.28226v1 · relevance 0.11

- **In one sentence**: The paper builds forcing extensions of minimal Nairian models (ZF-style models with the Axiom of Determinacy for sets of reals) in which AC and GCH hold and every uncountable regular cardinal carries a precipitous, uniform, kappa-dense ideal whose quotient algebra is the regular open algebra of Col(omega, kappa).
- **In plain words**: This is set theory: mathematicians study which infinite sizes exist and which "ideals" (collections of small sets that can be ignored) can exist on them. The paper shows that, in certain forcing extensions of a family of models where choice fails in a controlled way, every uncountable regular infinite size has a particularly well-behaved ideal of this kind. The authors also place the consistency strength of the relevant theory relative to large-cardinal hypotheses.
- **Why it matters**: It extends a theorem of Woodin, which gave such ideals only on omega_1, to every uncountable regular cardinal, and it adds to related work by Eskew and Hayut. The text itself does not say more about wider applications, so the broader significance is uncertain from this excerpt alone.
- **Background needed**: - Axiom of Choice (AC): the principle that one can pick an element from every set in a collection; it is independent of the other standard axioms.
- Axiom of Determinacy (AD) and AD_R: a strong alternative to choice stating that certain infinite two-player games are determined, applied to sets of real numbers.
- Forcing: a technique for extending a model of set theory by adding new sets, used to show what is and is not consistent.
- Cardinals, regular cardinals, and the Generalized Continuum Hypothesis (GCH): measures of infinite size and a conjecture about how sizes of power sets grow.
- Ideals and dense ideals: collections of "negligible" sets closed under certain operations; density and precipitousness are strong regularity properties of such ideals.
- Woodin cardinal: a large-cardinal assumption, a strong form of infinity used to measure consistency strength. · level: research-level

<details><summary>Original abstract</summary>

Complementing the work of Blue, Larson, and Sargsyan~\cite{NM,NM2}, we obtain forcing extensions of minimal Nairian models in which the Axiom of Choice and the Generalized Continuum Hypothesis hold. In these extensions, every uncountable regular cardinal $\kappa$ carries a precipitous, uniform, $\kappa$-dense ideal $\mathcal{I}_\kappa$. In fact, $\mathcal P(\kappa)/\mathcal{I}_\kappa$ is isomorphic to the regular open algebra of $\textrm{Col}(\omega,\kappa)$. This extends Woodin's theorem on the existence of $\omega_1$-dense ideals on $\omega_1$ in forcing extensions of models of $\Theta_{\rm reg}$ \cite[Section~2.3]{ASTWZ24}, where $\Theta_{\rm reg}$ denotes the theory $\textrm{ZF}+\textrm{AD}_{\mathbb R}+\text{``$\Theta$ is regular''}$. Moreover, our work places the consistency strength of the aforementioned theory on generic embeddings below a Woodin cardinal that is a limit of Woodin cardinals, and also complements the seminal work of Eskew and Hayut~\cite{EH24}.

</details>

## Mathematical physics

### [Tensionless M5-brane in light-cone gauge. The spinor moving frame method is wanted](https://arxiv.org/abs/2611.31189)
*Igor Bandos* · `hep-th` · arXiv:2611.31189v1 · relevance 0.11

- **In one sentence**: The paper performs complete light-cone gauge fixing of the recently proposed tensionless limit of the M5-brane action, handling the local fermionic kappa-symmetry via an adapted spinor moving frame method, and also treats the simpler tensionless p-branes (null p-branes) for comparison.
- **In plain words**: The paper studies a idealized limit of a higher-dimensional membrane-like object (an M5-brane, a five-dimensional surface in M-theory) in which its tension, or energy per unit size, goes to zero. The authors remove redundant descriptive freedom from the equations by choosing a "light-cone" gauge, which is a standard simplifying choice of coordinates, and they do this for the fermionic (spinor-valued) symmetry, which is the hardest part. They report that a modified version of a known method for handling this symmetry works, and they also apply it to simpler tensionless branes that carry no internal gauge fields.
- **Why it matters**: Tensionless branes are of interest as possible models of high-energy or strongly constrained regimes of string and M-theory, but the text itself does not establish such connections. The work is mainly a technical step toward a consistent gauge-fixed description, so its significance depends on whether that description proves useful later.
- **Background needed**: - M-theory: a proposed eleven-dimensional framework that unifies string theories.
- Brane: a extended object; a p-brane has p spatial dimensions, and the M5-brane is five-dimensional.
- Tension: energy per unit volume of a brane; the tensionless limit sets this to zero.
- Gauge symmetry and gauge fixing: redundancies in a description that can be removed by choosing a convenient set of coordinates or conditions.
- Light-cone gauge: a gauge choice using combinations of time and one space direction, which simplifies equations.
- Kappa-symmetry: a local fermionic (spinor) redundancy special to supersymmetric branes.
- PST scalar: a auxiliary field from the Pasti-Sorokin-Tonin formulation of the M5-brane action.
- Spinor moving frame: a method using spinor-built vectors to set up a local coordinate frame for fixing kappa-symmetry. · level: research-level

<details><summary>Original abstract</summary>

We perform the complete light-cone gauge fixing for the tensionless limit of the M-theory 5-brane the action for which was recently obtained in [1]. The problem of gauge fixing of local fermionic $\kappa$-symmetry becomes quite nontrivial because the projector of that is constructed from the gauge field strength which in its turn is required to be nonvanaishing and nontrivial in this limit. To resolve this problem the spinor moving frame method has been adapted. The corresponding moving frame is constructed on a vector quadratic in the gauge field strength, which is required to be nonvanishing and nondegenerate in the tensionless limit, and the derivative of the PST (Pasti-Sorokin-Tonin) scalar. The symmetries of the gauge fixed action and equations of motion are briefly discussed. To make a comparison with the case of usual tensionless p-branes (null-p-branes), those which do not carry worldvolume gauge fields, we also elaborate their spinor moving frame formulation.

</details>

### [Infrared finite scattering theory: Non-relativistic Coulomb scattering](https://arxiv.org/abs/2611.29691)
*Kartik Prabhu, Shivam Upadhyay* · `hep-th` · arXiv:2611.29691v1 · relevance 0.10

- **In one sentence**: The paper builds a perturbative, infrared-finite Dollard scattering operator for non-relativistic Coulomb scattering, checks it through second Born order, and sets up an LSZ-type reduction adapted to the modified asymptotic dynamics with a view to relativistic quantum field theory.
- **In plain words**: When two charged particles fly past each other, their electric pull never fully switches off, so the standard textbook way of calculating how they scatter produces integrals that blow up. This paper revisits that problem for the simple non-relativistic Coulomb case, using a modified reference dynamics (Dollard's approach) so that the blow-ups cancel term by term in the calculation. The authors also rewrite the problem in a different mathematical viewpoint and build a version of the standard particle-collision recipe that could, in principle, be extended to quantum field theory.
- **Why it matters**: Long-range forces such as electromagnetism cause infrared divergences, which are a known obstacle in particle physics calculations, so a clean, checkable treatment of the simplest case may help. The text says the framework is intended to extend to relativistic field theories with massless fields, but it does not show that extension, so its usefulness there remains open.
- **Background needed**: - Scattering: how particles deflect after colliding, summarized by an S-matrix that maps incoming to outgoing states.
- Coulomb potential: the 1/distance force between charges; it decays slowly, so its effects reach far away.
- Born series: computing scattering as a sum of successive approximations; the integrals diverge for Coulomb forces.
- Dollard's approach: replacing the free reference motion with a modified one that includes the slow logarithmic phase drift, making the operator well defined.
- Heisenberg picture and LSZ reduction: formal tools for relating field-theory correlation functions to measurable scattering amplitudes.
- Infrared divergence: a blow-up caused by very long-wavelength or long-range effects. · level: research-level

<details><summary>Original abstract</summary>

We revisit non-relativistic quantum-mechanical scattering in a Coulomb potential. The long-range nature of the interaction leads to divergent integrals in conventional S-matrix calculations using the Born series. Dollard showed that a well-defined scattering operator can be constructed by replacing the free Hamiltonian $ H_0 $ with an appropriate asymptotic Hamiltonian $ H_{\rm D} $. However, explicit perturbative calculations within Dollard's framework have remained scarce. We develop a perturbative formulation of the Dollard scattering operator in which the Coulomb divergences cancel to all orders. Perturbatively, we demonstrate this cancellation explicitly through second Born order and show that the resulting amplitude reproduces the known exact distributional Coulomb amplitude, including its forward-scattering contribution. With the aim of generalizing our analysis to quantum field theory, we reformulate the problem in the Heisenberg picture. We construct a new set of canonical variables through a time-dependent canonical transformation that removes the logarithmic Coulomb correction from the asymptotic phase-space coordinates. Using these variables, we construct the corresponding Heisenberg S-matrix through several complementary approaches. This leads to a formulation of the Lehmann--Symanzik--Zimmermann (LSZ) reduction formalism adapted to the modified asymptotic dynamics, which we relate to the Dollard scattering operator. This construction provides a framework for extending the LSZ formalism to infrared divergences in relativistic quantum field theories with long-range interactions and massless fields.

</details>

## Optimization and control

### [The dimension of optimal plans in multi-marginal optimal transport](https://arxiv.org/abs/2611.29080)
*Camilla Brizzi, Gero Friesecke* · `math.OC` · arXiv:2611.29080v1 · relevance 0.22

- **In one sentence**: The paper determines the maximal dimension on which optimal solutions of multi-marginal optimal transport with absolutely continuous marginals are concentrated, using a new characteristic integer tied to the Hessian of the cost function, with applications to Wasserstein barycenters, Wasserstein cubic splines and Brenier's generalized Euler equations.</one_liner>
<parameter name="plain">The paper studies the problem of matching several probability distributions together at the lowest possible total cost, where each way of matching has a cost. It asks how "spread out" the best matchings can be, that is, on how many dimensions the optimal solutions live. The authors give a general answer for a broad class of cost functions, using a newly defined integer computed from second derivatives of the cost.
- **Why it matters**: Knowing the dimension of optimal solutions tells you whether they can be described by a simpler map rather than a general spread-out plan, which matters for both theory and computation. The text links the result to several named problems (barycenters, splines, Euler-type equations), but it does not show further practical impact, so its wider significance is unclear from the abstract alone.
- **Background needed**: - Optimal transport: finding the cheapest way to move one probability distribution onto another, the classic "moving piles of earth" problem.
- Multi-marginal version: more than two distributions are matched at once, with a joint plan whose cost depends on all of them together.
- Marginals: the given probability distributions that the plan must respect.
- Absolutely continuous: the distributions have smooth densities, not concentrated on isolated points.
- Concentrated on a dimension: optimal plans live on a lower-dimensional set (for example a surface or curve) rather than filling the whole space.
- Hessian: the matrix of second derivatives of the cost function, which measures how it curves.
- Wasserstein barycenter: an "average" of several distributions defined through optimal transport.
- Brenier's generalized Euler equations: a geometric reformulation of fluid-flow equations via optimal transport. · level: research-level

<details><summary>Original abstract</summary>

For general cost functions, we determine the maximal dimension on which solutions to the multi-marginal optimal transport problem with absolutely continuous marginals are concentrated. The dimension is obtained via a novel characteristic integer associated with the Hessian of the cost function. Applications are given to important examples of multi-marginal problems like Wasserstein barycenters, Wasserstein cubic splines and Brenier's generalized Euler equations.

</details>

### [Convergence of potential-preserving annealed Sinkhorn algorithm](https://arxiv.org/abs/2611.30984)
*Dawid Lipinski, Maciej Buze* · `math.OC` · arXiv:2611.30984v1 · relevance 0.17

- **In one sentence**: The paper proves convergence results for a potential-preserving annealed Sinkhorn algorithm for entropic optimal transport, under non-increasing regularisation schedules tending to zero, including sharpness of a non-summability condition and convergence rates for polynomial inverse-temperature schedules.
- **In plain words**: The paper studies a step-by-step numerical method for finding the cheapest way to move one distribution of material onto another, a problem called optimal transport. The method gradually lowers a smoothing "temperature" parameter while keeping one set of internal variables (dual potentials) fixed in form. The authors show that if the temperature drops slowly enough in a specific sense, the method reaches a correct solution along some subsequence, and they give an example showing the condition cannot be weakened.
- **Why it matters**: Optimal transport underlies many tools in machine learning and statistics, and the choice of how to anneal the smoothing parameter affects whether the algorithm gives the right answer. The text reports that linear schedules, where recent work found the alternative scaling-preserving variant fails, do satisfy the new conditions, but it does not say how this bears on practical applications.
- **Background needed**: - Optimal transport: finding a lowest-cost way to map one probability distribution onto another, subject to fixed marginals (the amounts at each source and target).
- Entropic regularisation: adding a penalty that smooths the problem; a parameter (inverse temperature) controls how strongly it applies.
- Sinkhorn algorithm: an iterative method alternating rescalings of rows and columns of a matrix until the marginal constraints are approximately met.
- Annealing: gradually changing the smoothing parameter over iterations, akin to slowly cooling a system.
- Dual potentials: auxiliary functions tied to the constraints, used alongside the transport plan.
- Summable vs non-summable sequences: whether the total of the step sizes over all iterations is finite; non-summable means the total grows without bound.
- Convergence rate: how quickly the error shrinks as iterations proceed. · level: research-level

<details><summary>Original abstract</summary>

The annealed Sinkhorn algorithm is an iterative method for approximating solutions of optimal transport problems, in which the entropic regularisation parameter is progressively decreased. As this parameter decreases, one may preserve either the multiplicative scaling factors or the corresponding dual potentials. We study the potential-preserving iterates under positive, non-increasing regularisation schedules tending to zero. We prove that, if the schedule is non-summable, the iterates admit a subsequence converging to a solution of the corresponding optimal transport problem. The non-summability condition is sharp, as for every summable schedule in this class we construct an example in which the iterates converge to a plan violating the prescribed source marginal. We further establish convergence of the entire sequence if the relative inverse-temperature increments are also square-summable, and show by example that non-summability alone does not guarantee full convergence. Our convergence conditions are satisfied by linear inverse-temperature schedules, under which recent work has shown that the scaling-preserving iterates fail to converge to a solution of the optimal transport problem. We also derive convergence rates for polynomial inverse-temperature schedules up to and including linear growth, extending the marginal KL bound obtained by mirror-descent analysis at fixed temperature. Our best rate for the transport cost gap after rounding improves on that established for scaling-preserving annealing. Simple numerical illustrations accompany these convergence results.

</details>

## Statistics theory

### [Identification multiplicity across study designs](https://arxiv.org/abs/2611.29908)
*Carlos Garc\'ia Meixide, David R\'ios Insua* · `stat.ME` · arXiv:2611.29908v1 · relevance 0.09

- **In one sentence**: A conceptual framework for collections of causal analyses that answer one question through different observed-data translations, separating identification discrepancies from differences in causal targets and examining when averaging retains a causal meaning.
- **In plain words**: Researchers often can answer a cause-and-effect question in several legitimate ways, depending on which variables they adjust for, which comparison groups they use, or which data they draw on. This paper offers a way to organize that set of analyses, asking what each one actually estimates, which assumptions they share, and how their estimates are linked by sampling. It illustrates the ideas with fourteen examples across many study designs.
- **Why it matters**: The paper argues that agreement among several analyses is evidence only about the assumptions that differ between them, not about assumptions they all share, which is a useful caution for anyone relying on consistent results. It connects to established ideas such as instrumental variables, triangulation, transportability, and model-uncertainty inference, though the text alone does not show how widely these ideas will be adopted in practice.
- **Background needed**: - Causal question: asking what would happen to an outcome if a factor were changed, as opposed to what is merely associated with it.
- Identification: whether a causal quantity can be recovered from observed data given stated assumptions.
- Adjustment set: the variables one controls for to make groups comparable.
- Instrument: a variable that influences the treatment but affects the outcome only through it.
- Mediator: a variable on the causal path between treatment and outcome.
- Regression discontinuity and staggered adoption: designs that exploit cutoffs or timing of treatment rollout.
- Transportability: moving a causal finding from one population to another.
- Sampling dependence: how estimates computed from the same data are correlated with each other.
- Multiple testing is a different issue: it concerns the risk of false positives from many hypothesis tests, not the choice among valid-looking causal translations. · level: research-level

<details><summary>Original abstract</summary>

The answer to a causal question often admits several translations in terms of observed data. These may differ in adjustment sets, comparison groups, instruments, mediators, cutoffs, eligibility occasions, or data sources. We describe the resulting collection of analyses by three structures: the causal target that each analysis identifies under its assumptions, the assumptions that the analyses share, and the sampling dependence among their estimates. A single decomposition separates identification discrepancies from differences in causal targets, and we make both terms explicit in fourteen examples spanning adjustment, comparative panels, proxies, mediators, instruments, discontinuities, staggered adoption, sequential trials, and source combination. Comparisons within a collection can reveal differential violations of assumptions but not a bias common to all analyses; agreement is therefore evidence about the assumptions that differ, not about those that are shared. Averaging retains a causal interpretation in three ways: efficient combination of analyses that identify one target, a projection of a causal curve with a declared approximating family and weighting measure, and inference under weaker premises such as validity of at least one analysis or a known sign of its bias. Precision weights, regression-implied weights, and hierarchical models do not supply these interpretations by themselves. We relate this account to triangulation, overidentification, marginal treatment effects, transportability, and recent methods for inference under model uncertainty, and distinguish identification multiplicity from multiple testing.

</details>

### [Limit theorems for almost conditionally identically distributed random variables](https://arxiv.org/abs/2611.28967)
*Marco Battiston, Lorenzo Cappello* · `math.ST` · arXiv:2611.28967v1 · relevance 0.08

- **In one sentence**: Extends strong law of large numbers, absolute-continuity conditions for the asymptotic directing measure, and three central limit theorems from exchangeable and conditionally identically distributed sequences to the more general ξ-almost conditionally identically distributed (ξ-a.c.i.d.) setting.
- **In plain words**: The paper studies sequences of random quantities that are almost, but not exactly, "identically distributed given the past," a relaxed version of the exchangeable setting where the order of observations does not matter. A parameter sequence ξ measures how far the sequence departs from that ideal. The authors prove a law-of-large-numbers result and give conditions on when the limiting distribution has a density relative to a given reference measure, then derive three central limit theorems (describing fluctuations around the limit) for the predictive, empirical and asymptotic directing distributions.
- **Why it matters**: The results are aimed at Bayesian predictive inference, where they are said to support constructing asymptotic credible intervals, and they cover settings such as recursive algorithms and heteroskedastic data. The text does not report numerical examples or comparisons, so the practical reach beyond the stated applications is not something I can judge from it.
- **Background needed**: - Exchangeable sequence: a sequence whose joint distribution is unchanged by reordering its terms.
- Conditionally identically distributed (c.i.d.): each new term has the same conditional distribution given the past, a generalization of exchangeability.
- Directing measure: the random distribution that, conditional on it, the sequence behaves like independent draws; its limit is the "asymptotic directing measure."
- Law of large numbers: sample averages converge to a limit as the sample grows.
- Central limit theorem: after centering and scaling, fluctuations around the limit approach a normal (bell-shaped) distribution.
- Absolute continuity with respect to a σ-finite measure: the limit has a density relative to a reference measure.
- Predictive distribution: the distribution of the next observation given those seen so far. · level: research-level

<details><summary>Original abstract</summary>

$\xi$-Almost Conditional Identically Distributed ($\xi$-a.c.i.d.) random variables are generalizations of conditional identically distributed (c.i.d.) and exchangeable ones. $\xi$-a.c.i.d. random variables arise naturally in applications in statistics, such as in recursive algorithms and heteroskedastic observations, and are parametrized by a sequence $\xi=(\xi_{n})_{n\geq 0}$ that quantifies departure from the c.i.d. property. In this work, we extend limit theorems for exchangeable and c.i.d. random variables to the more general setting of $\xi$-a.c.i.d. random variables. After proving a Strong Law of Large Numbers, we provide necessary and sufficient conditions for the asymptotic directing measure of the sequence to be absolutely continuous with respect to a given $\sigma$-finite measure. Then, under regularity assumptions on the parameter $\xi$, three different Central Limit Theorems for $\xi$-a.c.i.d. sequences are derived, involving the predictive, empirical and asymptotic directing distributions. These theorems have several statistical applications, including the construction of asymptotic credible intervals in Bayesian predictive inference.

</details>

## Statistical methods and applications

### [When AI Performance Is Not Enough: Statistical Guardrails for Clinical Development](https://arxiv.org/abs/2611.28497)
*Siddhesh Kulkarni, Gina D'Angelo, Swarna Reddy et al.* · `stat.ME` · arXiv:2611.28497v1 · relevance 0.13

- **In one sentence**: A commentary arguing that AI and machine learning tools used in clinical drug development need explicit statistical safeguards, reviewed across four domains (anomaly detection, adaptive trial monitoring, biomarker enrichment, and digital twins) and framed around the ICH E9(R1) estimand approach.
- **In plain words**: This paper is a position piece about using artificial intelligence in the testing of new medicines. It says that AI tools can look good on their own terms but can still fail the statistical standards needed for trustworthy decisions about patients and regulators. The authors walk through four areas where this matters and list typical risks, such as false alarms, weakened error control in adaptive trials, and mistaking a marker that predicts a general outcome for one that predicts who benefits from a treatment.
- **Why it matters**: Regulators and sponsors are adopting AI faster than the statistical checks are being written, so a framework for judging these tools by their intended use is timely. The text is a commentary without new data or tested results, so it sets out a way of thinking rather than showing that any specific method works or fails.
- **Background needed**: - Clinical trials: controlled studies testing whether a treatment works in people, run in phases before approval.
- Type I error: the chance of wrongly concluding a treatment works when it does not; adaptive trials that change midway must keep this under control.
- Prognostic vs. predictive biomarker: a prognostic marker signals how a patient is likely to do regardless of treatment; a predictive marker signals who responds to a specific treatment.
- Estimand: a precise definition of the treatment effect being measured, including how events like dropping out are handled (ICH E9(R1) guidance).
- Digital twin: a computer model of an individual patient or trial population used to simulate outcomes, often as a stand-in for a control group.
- Context of use: the specific decision a tool is meant to support, which sets how much evidence it needs. · level: intermediate

<details><summary>Original abstract</summary>

Artificial intelligence (AI) and machine learning (ML) are reshaping the operational and inferential landscape of clinical development, yet their adoption frequently outpaces the statistical scrutiny these methods demand. This commentary offers first-principles perspectives across four application domains: anomaly detection in clinical trial data, real-time monitoring and adaptive trial designs, biomarker-based enrichment, and virtual and digital twins. For each domain, we articulate the underlying inferential problem, the contribution of AI and ML relative to established statistical methods, and the risks that statisticians, data scientists, and clinical developers must actively manage. Across these domains, a unifying theme emerges: AI and ML methods may succeed locally while failing to satisfy the broader statistical assumptions required for valid clinical and regulatory decisions. These risks include false-positive signals, compromised Type I error control in adaptive designs, conflation of prognostic with predictive biomarkers, and causal claims not supported by data and assumptions. We argue that a clearly defined context of use, relevant statistical assumptions, and consequences of the intended decision should guide the evaluation. For treatment-effect questions, the ICH E9(R1) estimand framework provides a useful organizing principle. Responsible use of AI in clinical development requires not restraint, but rigor: the inferential discipline necessary to make these technologies reproducible, interpretable, and defensible in the service of patients.

</details>

### [Quantifying and calibrating precision gain from covariate adjustment in clinical trials with binary endpoints](https://arxiv.org/abs/2611.30845)
*Jannik Hammerschmied, Christian Stock, Martin Schnuerch* · `stat.ME` · arXiv:2611.30845v1 · relevance 0.12

- **In one sentence**: The paper develops a theory for the maximum first-order precision gain from covariate adjustment when estimating marginal treatment effects on binary endpoints, introduces marginal prognostic strength, and proposes a calibration algorithm for simulation studies.
- **In plain words**: In randomized clinical trials, researchers often adjust for patient characteristics measured at baseline to get more precise estimates of a treatment effect. The paper studies this for yes/no outcomes (such as whether a patient responds), where adjustment is less straightforward than for continuous measurements. The authors derive a formula for how much precision adjustment can add, and they show that useful prognostic information does not always translate into a precision gain.
- **Why it matters**: Choosing whether and how to adjust for covariates affects how large a trial must be and how reliable its conclusions are, so the framework matters for trial design and analysis. The text does not indicate any specific trial or application beyond methodological simulation studies, and its practical impact is not assessed here.
- **Background needed**: - Randomized clinical trial: patients are randomly assigned to treatment or control, so groups are comparable on average.
- Covariate adjustment: using baseline patient information in the analysis to reduce noise in the estimated treatment effect.
- Precision: how tightly an estimate is pinned down; more precision means smaller uncertainty (narrower confidence intervals).
- Binary endpoint: an outcome with two possible values, such as response versus no response.
- Marginal versus conditional effect: a marginal effect is the average effect across the whole population; a conditional effect applies to patients with a given profile. In nonlinear models like logistic regression these can differ.
- Prognostic information: how well baseline characteristics predict the outcome.
- Simulation study: a computer experiment with artificially generated data used to test statistical methods. · level: research-level

<details><summary>Original abstract</summary>

Covariate adjustment is widely used in randomized clinical trials to improve estimation and inference of treatment effects. For continuous endpoints, the reasoning is straightforward: prognostic baseline covariates explain outcome variability and thereby increase precision. For binary endpoints, however, the situation is more complex because conditional and marginal effects generally differ in nonlinear outcome models such as logistic regression. We develop a theoretical framework for quantifying the maximum attainable first-order precision gain from covariate adjustment when estimating marginal treatment effects for binary endpoints. We derive a closed-form identity showing that precision-gain potential is governed by an estimand- and allocation-specific combination of the treatment-specific risk functions. Building on this identity, we introduce marginal prognostic strength as a population-level measure of prognostic information and characterize when it determines precision-gain potential and when the two quantities decouple. Specifically, substantial prognostic information within both treatment arms need not translate into improved precision for the marginal treatment effect when covariates are predictive on the target effect scale. We further develop a calibration algorithm for methodological simulation studies that preserves prespecified conditional outcome structures and marginal risks while allowing data-generating mechanisms to be calibrated by marginal prognostic strength and evaluated in terms of estimand-specific precision-gain potential. Together, these results provide a theoretical and practical framework for understanding, quantifying, and calibrating potential precision gains from covariate adjustment for binary endpoints.

</details>

## AI industry news

### [How iFood scales coding agents across 15,000 repositories](https://openai.com/business/customer-stories/ifood)
** · `openai.com` · OpenAI News · relevance 0.08

- **In one sentence**: A news piece titled "How iFood scales coding agents across 15,000 repositories," but the body text is missing, so only the headline's claim about iFood (a Brazilian food-delivery company) applying AI coding agents to about 15,000 code repositories can be noted.
- **In plain words**: This item is about how the food-delivery company iFood uses AI "coding agents," which are programs that can write and change software on their own, across a very large set of software projects, about 15,000 repositories. The article text is not available, so I cannot say what approach was taken or what results were reported. The headline alone does not tell us how well it worked.
- **Why it matters**: Large companies using AI tools to change code across thousands of projects is a practical question for software teams, since it touches on speed, reliability and oversight. Without the body text, I cannot say what was actually learned, so treat this as a pointer to a topic rather than a finding.
- **Background needed**: - Code repository: a stored collection of a software project's files and their change history, often shared by a team.
- Coding agent: an AI system that reads code, makes edits, and runs tasks with some autonomy, rather than only suggesting single lines.
- Scaling across repositories: applying the same tool or process to many separate projects at once, which raises questions about consistency, testing and review.
- iFood: a Brazilian food-delivery platform; the headline names it as the organization involved.
- Note: the source text is empty, so no methods, results or figures are verified here. · level: intermediate

<details><summary>Original abstract</summary>



</details>

### [Anthropic launches Claude Ship, letting AI agents review, fix, and approve code changes](https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/)
*Sarah Perez* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.07

- **In one sentence**: Anthropic has announced "Claude Ship," developer tools that let AI agents review, fix, and approve code changes, aimed at easing the approval backlog created by growing volumes of AI-generated code.
- **In plain words**: Software teams are producing more code than ever with AI help, and the human step of checking and approving each change is becoming a slow point. This article reports that Anthropic has launched new developer tools that let AI agents handle some of that routine checking, fixing, and approving. The text is brief and does not describe how the tools work in detail or how well they perform.
- **Why it matters**: If AI systems can safely take over routine sign-off on code, it could change how fast software gets released and who checks it. The article gives no performance data or safety details, so how much this matters in practice is unclear.
- **Background needed**: - "Code changes" are edits to a software project, usually reviewed by a colleague before being merged into the main version.
- "AI agents" are AI systems that carry out multi-step tasks on their own, rather than only answering one prompt at a time.
- "Bottleneck" means a stage that slows down everything after it; here, human review of code.
- Anthropic is an AI company that makes the Claude family of AI models.
- The article is a short news item; it does not include technical specifics, benchmarks, or independent evaluation. · level: intermediate

<details><summary>Original abstract</summary>

As AI-generated code piles up, Anthropic's new developer tools aim to eliminate another bottleneck by letting agents handle routine approvals.

</details>

### [Tidal to ban and remove millions of AI-generated tracks as AI slop inundates music streaming](https://techcrunch.com/2026/11/24/tidal-to-ban-and-remove-millions-of-ai-generated-tracks-as-ai-slop-inundates-music-streaming/)
*Ivan Mehta* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.07

- **In one sentence**: Music streaming service Tidal says it will ban and remove millions of fully AI-generated tracks while still allowing songs that used AI only as an assistant.
- **In plain words**: Streaming services are being flooded with low-quality music made entirely by AI, often called "AI slop." Tidal, a music streaming app, says it will remove millions of these fully AI-generated tracks. Songs where AI only helped a human artist are still allowed.
- **Why it matters**: This is a concrete platform policy on how streaming services will handle AI-made content, which affects artists, listeners and royalties. The source text is very short, so it does not say how Tidal will detect these tracks or how the policy will be enforced; those details are unknown from this text alone.
- **Background needed**: - "AI slop" is a slang term for low-effort, mass-produced content generated by AI, often with little human involvement.
- Streaming services like Tidal host catalogs of songs and pay rights holders based on plays.
- "Fully generated" music means the AI produced the song itself, while "AI-assisted" means a human made the work and used AI for some part of it.
- The article gives only the headline claim and one sentence on the policy; the full article may contain more detail. · level: introductory

<details><summary>Original abstract</summary>

The company said it will still accept songs that were made with AI assistance, but not fully generated.

</details>

### [Meta brings its Muse AI assistant directly into Instagram DMs](https://techcrunch.com/2026/11/24/meta-brings-its-muse-ai-assistant-directly-into-instagram-dms/)
*Aisha Malik* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.07

- **In one sentence**: Meta has integrated its Muse AI assistant directly into Instagram direct messages, so users no longer need to switch to the separate Muse app to use the agent.
- **In plain words**: Meta, the company that owns Instagram, is letting people use its Muse AI assistant from inside Instagram's private messaging feature. Before this change, people who wanted to use the assistant had to leave Instagram and open a separate Muse app. The article is short and mainly describes this convenience change.
- **Why it matters**: It shows how AI assistants are being built into everyday apps rather than kept as standalone products, which may affect how many people use them. The article gives no usage figures or details on how well it works, so its wider significance is unclear.
- **Background needed**: - Meta owns Instagram and develops the Muse AI assistant, described here as an "AI agent".
- An AI agent is a program that can carry out tasks for a user, such as answering questions or taking actions, rather than only chatting.
- Direct messages (DMs) are private one-to-one or group messages between Instagram users.
- "Integration" here means building one product into another so users do not have to switch apps.
- The article does not describe what Muse can do, its capabilities, or any privacy or safety details. · level: introductory

<details><summary>Original abstract</summary>

The new integration gets rid of the need for users to toggle between Instagram and the Muse app when they want to interact with the AI agent.

</details>

### [How Intentful uses dots to make more time for growth](https://openai.com/business/customer-stories/intentful-dots)
** · `openai.com` · OpenAI News · relevance 0.06

- **In one sentence**: A short company feature describing how Intentful uses an AI assistant called "dot" (named Aria in this case, used by Marina Petrova) for research, proposal drafting, proactive message flagging, and issue resolution.
- **In plain words**: This is a brief feature about a person at a company, Marina Petrova, who uses an AI assistant named Aria, built on a product called dot, to speed up her work. According to the text, Aria helps look up information on websites, drafts proposals, points out messages that may need attention, and helps resolve problems. The text gives no measured results or detailed explanation of how it works.
- **Why it matters**: It offers a small, concrete example of an AI tool being used for everyday office tasks, which is a common trend in workplace AI. The text is too thin to show how well it works or whether the claims hold beyond this one user.
- **Background needed**: - "Dot" appears to be the name of an AI assistant product; Aria is one assistant instance named in the text.
- An AI assistant is software that carries out tasks such as searching, drafting text, and sorting messages, often after being given instructions.
- "Proactively flagging" means the tool raises issues on its own rather than waiting to be asked.
- This is a company-style feature, so it likely presents the tool favorably and offers no independent evaluation. · level: introductory

<details><summary>Original abstract</summary>

Marina Petrova’s dot Aria helps research websites and build proposals, while proactively flagging messages and resolving issues.

</details>

## Model architectures and training

### [Rewirable Circuits in Transformers with Loom Attention](https://arxiv.org/abs/2611.30634)
*Da Xiao, Qingye Meng, Shengping Li et al.* · `cs.LG` · arXiv:2611.30634v1 · relevance 0.30

- **In one sentence**: Proposes "loom attention," in which each Transformer attention head is built from earlier heads' outputs via a per-token matrix memory (LoomFormer), and reports gains over compute-matched baselines in language modeling.
- **In plain words**: Large language models process text through stacked layers, and each layer has many small "heads" that decide which earlier words matter. This paper proposes letting each head first look at what earlier heads produced, so the network can reroute its internal computation for every word. The authors report that their resulting architecture, LoomFormer, reaches the quality of standard models trained with more compute.
- **Why it matters**: The claim is that a model can match or beat baselines trained with 1.7 to 3 times more compute by changing how information flows between layers, which would matter for training cost if it holds up. The abstract reports results only for specific setups (for example, LoomPythia-2.8B trained on 300B tokens), so how far the gains generalize is not yet clear from this text alone.
- **Background needed**: - Transformer: the neural network design behind modern language models, built from stacked layers of "attention" heads.
- Attention head: a unit that, for each word, weighs how much to draw from other words in the text.
- Residual stream: the running vector that each layer adds its output to; a shared information highway through the network.
- Matrix memory and linear attention: a compressed, fixed-size store of past information, used here as a cheaper alternative to full attention over all tokens.
- Baselines named: Pythia (a family of open models), and recent residual-stream variants (HC/mHC, MUDDFormer, AttnRes).
- FLOPs: a count of arithmetic operations, used as a proxy for training compute.
- Downstream tasks, 0-shot and 5-shot: benchmark tests where a model answers without or with five worked examples. · level: research-level
- Matched keywords: transformer, attention, linear attention, architecture

<details><summary>Original abstract</summary>

We propose loom attention, which allows a Transformer to dynamically rewire its circuits at every token by interweaving a head's vertical attention over the outputs of earlier heads (to obtain its query, key and value) with its horizontal attention over tokens. We instantiate vertical attention efficiently with normalized and gated linear attention over a per-token matrix memory, which stores the compressed head outputs and serves as a second residual stream. This yields LoomFormer, a dual-stream architecture that splits control and content between the vector and matrix streams. Across model sizes and training token budgets in language modeling and downstream tasks, LoomFormer matches Transformers trained with over 3x compute and recent residual-stream baselines (HC/mHC, MUDDFormer, AttnRes) trained with ~1.7-2.8x. For example, trained on the same 300B tokens with only 2% extra FLOPs, LoomPythia-2.8B achieves ~1.6x the average downstream gain of mHC-Pythia-2.8B over Pythia-2.8B, and matches (0-shot) or surpasses (5-shot) Pythia-12B. Code is available at https://github.com/Caiyun-AI/LoomFormer

</details>

### [Yggdrasil: Tree-Routed Recurrent Experts for State Tracking and Fast CPU Inference](https://arxiv.org/abs/2611.29954)
*Cosmo Santoni* · `cs.LG` · arXiv:2611.29954v1 · relevance 0.30

- **In one sentence**: Yggdrasil is a parallel-trainable recurrent architecture that routes each layer's transition through a tree-indexed bank of experts, conditioned on the current token and the layer below, to decouple model capacity from per-step CPU latency and improve discrete state tracking.
- **In plain words**: Many fast sequence models read all of their parameters at every step, so making them bigger also makes them slower on a regular computer processor. This paper proposes Yggdrasil, a model that keeps a large library of small components and, at each step, uses a routing tree to pick just one of them per layer. The authors report that it solves all five state-tracking tests among the parallel-trainable models they compared, reaches the lowest test error on two text and DNA datasets at matched active size, and runs faster on a single CPU core than the fastest streaming baseline they tested.
- **Why it matters**: The idea of keeping total capacity large while the work done per step stays small, so it fits in fast CPU cache, may matter for running language and sequence models on ordinary hardware. The text reports benchmark results and a proof, but it does not show how the approach scales to larger models or real deployments, so its broader significance is uncertain.
- **Background needed**: - Recurrent model: processes a sequence one token at a time, carrying a hidden state forward.
- Parallel-trainable recurrence (e.g., Mamba, linear attention, DeltaNet): can be trained efficiently on many tokens at once, yet still runs cheaply step by step.
- State tracking: keeping track of discrete information (such as a sequence of symbol operations) over long inputs; some models do this poorly.
- Mixture of experts / routing: a learned selector sends each input to one of several sub-networks, so only part of the model runs.
- CPU cache (L2): small, fast memory close to the processor; the paper's speed claim depends on the active weights fitting there.
- Bits per byte/character (bpb): compression-style measure of prediction error on text or DNA; lower is better.
- Parallel scan: a technique for computing a recurrence across a sequence in parallel during training. · level: research-level
- Matched keywords: attention, linear attention, architecture

<details><summary>Original abstract</summary>

Parallel-trainable recurrences such as Mamba, linear attention, and DeltaNet offer constant-cost streaming inference, but they suffer from two limitations: 1) they struggle to track discrete state, and 2) they read every parameter at every step, tying model capacity directly to CPU latency. We introduce Yggdrasil, a recurrent architecture that decouples capacity from per-step compute by looking up each layer's transition in a large, tree-routed bank of recurrent experts. Each router addresses its bank using the current token and the state of the layer below. We prove that this cross-layer context is necessary---a single token-indexed layer of non-expanding transitions with finitely many reachable states cannot perform conditional resets---while avoiding feedback from the layer's own past preserves parallel-scan training. Because each step traverses one tree path and reads a single expert per layer, active weights stay within a few hundred kilobytes in CPU L2 cache while the full bank resides in RAM. Among the parallel-trainable models we evaluate, Yggdrasil is the only one to solve all five state-tracking tasks. At matched active parameter counts, it achieves the lowest test bits on enwik8 (1.540 bpb) and the human genome hg38 (1.567 bpb), while stepping $3.0\times$ and $3.3\times$ faster on a single CPU core ($6.7\,\mu\mathrm{s}$ and $5.8\,\mu\mathrm{s}$) than the fastest streaming baseline, and delivering the highest GPU throughput of all models at batch 1024. On the Genomic Benchmarks, it is the strongest causal model at matched active parameters (86.0% mean accuracy).

</details>

## Machine learning theory

### [Statistically Optimal and Near Linear Time Hypothesis Selection](https://arxiv.org/abs/2611.30003)
*Satyen Kale, Amirreza Shaeiri, Kunal Talwar* · `stat.ML` · arXiv:2611.30003v1 · relevance 0.21

- **In one sentence**: The paper gives a hypothesis selection learner that reaches the optimal factor-2 guarantee with O(log(n/δ)/ε²) samples, removing the log factors of an earlier factor-2 result, and runs in near-linear oracle complexity.
- **In plain words**: Suppose you have a list of n candidate probability distributions and some samples from an unknown one. The task is to pick a distribution (possibly one not on the list) that is nearly as close to the unknown one as the best candidate, within a factor of 2 plus a small error. The paper shows how to do this with a number of samples that grows only logarithmically in the number of candidates, and it counts cost by how many times the algorithm queries the candidates.
- **Why it matters**: The factor of 2 is the best possible for methods whose sample count does not depend on the size of the domain, and the paper matches the sample cost of a classic factor-3 estimator while removing extra logarithmic factors from the earlier factor-2 result. It is a theory result about the best achievable guarantees; the text does not describe practical applications, so its wider relevance is uncertain.
- **Background needed**: - Probability distribution: a rule assigning probabilities to possible outcomes.
- Total variation (TV) distance: a standard measure of how far apart two distributions are, from 0 (identical) to 1 (completely different).
- Hypothesis selection: choosing a good candidate from a list of candidate models using samples from the true one.
- Approximation factor α: a multiplier on the best candidate's error; α = 2 is the target here.
- Sample complexity: how many samples are needed as a function of accuracy and failure probability.
- Proper vs. improper learner: a proper learner outputs one of the candidates; an improper one may output something new.
- Multiplicative weights: an iterative method that reweights constraints over rounds. · level: research-level
- Matched keywords: sample complexity

<details><summary>Original abstract</summary>

In hypothesis selection we are given $n$ distributions $q_1,\dots,q_n$ on a countable domain $\mathcal{X}$ and samples from an unknown distribution $p$. The goal is a distribution $q$ with $\mathrm{TV}(p,q)\le\alpha\min_i\mathrm{TV}(p,q_i)+\epsilon$. The factor $\alpha=2$ is optimal for algorithms using a number of samples from $p$ that is independent of $|\mathcal{X}|$, and in general only improper learners achieve it. We give a learner that achieves $\alpha=2$ with $O(\log(n/\delta)/\epsilon^2)$ samples of $p$, with probability at least $1-\delta$. This matches the sample complexity of Yatracos's factor-$3$ estimator, and it removes the logarithmic factors in the factor-$2$ bound of Bousquet et al. (FOCS 2021). The learner accesses the $q_i$ only through sampling and pointwise comparisons. We measure its running time by its oracle complexity, the number of oracle calls. In expectation it makes $O((n\epsilon^{-2}+\epsilon^{-4}\log(1/\epsilon))\log(n/\delta))$ oracle calls, independent of $\mathcal{X}$. It runs multiplicative weights over the constraints $\mathrm{TV}(q,q_i)\le\mathrm{TV}(p,q_i)$ and uses at most one sample of $p$ per round.

</details>

### [Data-Dependent Probability Estimation via Sample Amplification](https://arxiv.org/abs/2611.28399)
*Vitaly Feldman, Satyen Kale, Mahbod Majid et al.* · `cs.LG` · arXiv:2611.28399v1 · relevance 0.18

- **In one sentence**: The paper gives a sample-efficient estimator for the probability of an event chosen after seeing the data, combining sample amplification with online-optimization-based distribution learning, and proves matching-up-to-logs bounds for discrete domains.
- **In plain words**: The question is how to estimate how likely some event is when the event itself was picked after looking at the data, so the usual count of how often it happened in the sample can be badly misleading. The authors show that roughly the square root of the domain size many samples is enough for a constant-accuracy estimate, when the rule that picks the event is known, instead of the roughly domain-size many needed to learn the whole distribution. The text also gives a matching lower bound up to logarithmic factors, and separate results for Gaussian distributions and a smoothed sample-size setting.
- **Why it matters**: The result answers an open question posed in a related paper and shows the sample cost is essentially tight up to logarithms, which makes it a clean theoretical answer. Its relevance to practical adaptive data analysis or statistics after data-driven selection is plausible but not established by the text.
- **Background needed**: - Empirical probability: the fraction of sample points where an event occurred.
- Distribution learning: estimating the full probability distribution over a domain of size d; needs about d samples to do so to constant accuracy.
- Data-dependent queries: the event or quantity is chosen after seeing the sample, which can bias naive estimates.
- Mean squared error: the average squared gap between estimate and truth; lower is better.
- Sample amplification: techniques that produce more effective samples from fewer ones, used here as a tool.
- Online optimization: a framework for sequentially updating a estimate; used to learn the distribution.
- Big-O notation with tilde: ignores logarithmic factors. · level: research-level
- Matched keywords: sample complexity

<details><summary>Original abstract</summary>

Can we estimate the probability of an event chosen after seeing the data, without using any fresh samples? Its empirical probability can be arbitrarily misleading, while learning the entire distribution to constant accuracy requires $\Theta(d)$ samples on a domain of size $d$. We show that $\widetilde{O}(\sqrt{d})$ samples suffice for constant mean squared error, provided the rule choosing the event is known. More generally, our estimator handles arbitrary $[0,1]$-valued queries and runs in polynomial time given evaluation access to the rule. This sample complexity matches the known lower bound up to logarithmic factors and resolves the open question posed by Feldman, Kale, Raman, Talwar, and Tewari (arXiv:2610.41244). Our estimation framework relies on a new combination of sample amplification (arXiv:1904.12053 and arXiv:2201.04315) with distribution learning via online optimization. Our estimator achieves mean squared error $O(d^{3/4}/n)$ when $d\leq n$ and $\widetilde{O}(d^{1/4}/\sqrt{n})$ when $d>n$. We complement this with a lower bound of $\Omega(\min\{1,\sqrt{d}/n\})$ on the mean squared error. Using our framework, we also design an efficient estimator for data-dependent queries on Gaussian distributions with unknown mean and identity covariance. Finally, we show that a smoothed variant of the problem is much (exponentially) easier. For discrete distributions, if the sample size is chosen uniformly from $\{n,\ldots,2n-1\}$, then $n=O(\log d)$ suffices for constant mean squared error.

</details>

## Large language models

### [From Reward Engineering to Data-Centric Reinforcement Learning for Effective Agentic Visual Tool Use](https://arxiv.org/abs/2611.28558)
*Jin Cui, Xinyue Long, Jiepeng Zhou et al.* · `cs.CL` · arXiv:2611.28558v1 · relevance 0.15

- **In one sentence**: AOVO proposes a data-centric reinforcement learning framework (perception attribution plus policy-adaptive data sampling, PADS) that teaches multimodal LLMs when to call visual tools using only final-answer correctness rather than tool-specific rewards.
- **In plain words**: Some AI models can call outside tools, such as image-inspecting helpers, while they reason about a picture. Teaching them when a tool call actually helps is hard, and past methods often added extra reward bonuses for calling tools, which can warp the model's behavior. This paper instead tries to find which questions a tool would actually fix, and shifts the training questions toward those, rewarding only correct final answers.
- **Why it matters**: It offers an alternative to hand-designed reward bonuses for tool use, a design choice that can cause odd behaviors, and the authors report consistent gains over competing tool-using models on visual benchmarks. The text does not give enough detail to judge how broadly the approach generalizes beyond the tested benchmarks.
- **Background needed**: - Multimodal large language model (MLLM): an AI system that handles both text and images.
- Tool use: the model pauses mid-reasoning to call an external helper, such as a zoom or crop function, to get more visual evidence.
- Reinforcement learning (RL): training by trial and error, where good outcomes are rewarded and the model adjusts its behavior.
- Reward engineering: adding extra, hand-designed bonuses to the reward signal to steer behavior; these can distort the actual goal.
- Counterfactual probing: testing how the model's answer changes when its inputs or tool observations are altered, to see whether the tool made a difference.
- Data-centric approach: improving learning mainly by choosing which training examples to use, rather than changing the reward or model design. · level: research-level

<details><summary>Original abstract</summary>

Multimodal large language models (MLLMs) increasingly use external visual tools to acquire evidence during reasoning, yet learning when to invoke these tools remains challenging. Existing tool-use reinforcement learning (RL) methods often rely on call-contingent rewards to encourage beneficial tool use, but such reward engineering can distort the task objective and lead to degenerate calling behaviors. We argue that effective tool-use learning requires identifying not merely which questions are difficult, but which failures are attributable to missing visual evidence and can therefore be corrected through tool observations. We propose AOVO, a data-centric framework that enables MLLMs to learn effective tool use through perception attribution and policy-adaptive data sampling (PADS), without introducing tool-specific rewards. It counterfactually probes the model's reasoning states to identify observation-sensitive questions, distinguishing them from reasoning-dominated ones. PADS then periodically estimates category-level observation effects from recent policy rollouts and dynamically reallocates the training distribution toward questions where visual observations provide informative learning signals, while optimizing solely for final-answer correctness. Experiments across diverse visual perception and multimodal reasoning benchmarks demonstrate consistent improvements over competitive tool-use MLLMs, with causal analysis further validating the data-centric perspective for learning effective visual tool use.

</details>

### [Definition-Guided In-Context Learning for Zero-Shot Spoken Language Understanding](https://arxiv.org/abs/2611.28929)
*Neeraj Agrawala, Sriram Ganapathy* · `cs.CL` · arXiv:2611.28929v1 · relevance 0.14

- **In one sentence**: The paper proposes Definition-Guided In-Context Learning (DG-ICL), a fine-tuning method that trains speech-text models to classify spoken input using natural-language label definitions instead of fixed label names, with randomized labels to block shortcuts, and reports zero-shot gains on held-out tasks with novel symbols across three audio-language models.
- **In plain words**: Voice systems that sort spoken words into categories, such as intents or topics, usually need new labeled examples and retraining whenever the category list changes. This paper tests whether a plain-language description of each category, given in the instructions, is enough for an audio-capable language model to handle new categories without any examples. The authors train models with labels replaced by random made-up tokens or shuffled words, and report higher scores than standard instruction tuning on new label sets across three models.
- **Why it matters**: If a model can take a new category from a written definition alone, spoken-language tools could be adapted without collecting and labeling fresh data, which is a practical bottleneck. The text reports gains on three models and a counterfactual test, but the evaluation covers only the tasks described, so how far the approach generalizes beyond them is unclear.
- **Background needed**: - Spoken language understanding (SLU): turning speech into structured meaning, such as the intent behind a request.
- Macro-F1: an accuracy-style score that averages performance across categories, so rare categories count equally.
- In-context learning: a model learns a task from instructions or examples placed in its input, without changing its weights.
- Instruction tuning: further training a language model on instruction-and-answer pairs so it follows directions.
- Zero-shot: handling a task or category never seen during training, with no examples given.
- Audio-language models: language models extended to accept sound as input (here Audio Flamingo 3, Qwen2-Audio, SALMONN).
- Lexical shortcut: a model relying on the familiar meaning of a label name rather than the definition it was given. · level: research-level

<details><summary>Original abstract</summary>

Adapting spoken language understanding (SLU) systems to novel or revised label taxonomies conventionally requires additional labeled data and retraining, creating a bottleneck for real world deployment. While in-context learning with few-shot demonstrations offers an alternative, multi-modal generalization and scaling has been challenging. In this work, we investigate whether natural-language definitions alone can guide zero-shot SLU without demonstration exemplars, finding that symbolic definitions serve as the primary supervisory driver for adapting speech-text models. We operationalize this principle as Definition-Guided In-Context Learning (DG-ICL), a fine-tuning framework that decouples semantic categories from fixed lexical names. By replacing labels with dynamically randomized definitions (arbitrary synthetic tokens in DG-ICL-Sym or permuted vocabulary words in DG-ICL-Flip), DG-ICL avoids lexical shortcuts and encourages the model to ground acoustic representations in contextual definitions. Novel categories can thus be introduced at inference simply by defining them through the instructions. Across three speech-text models (AUDIO FLAMINGO 3, QWEN2-AUDIO, and SALMONN), DG-ICL outperforms standard instruction tuning on held-out tasks under novel symbols (0.663 vs. 0.449 macro-F1 on Audio Flamingo 3; 0.703 vs. 0.620 on Qwen2-Audio; 0.582 vs. 0.399 on SALMONN), while remaining competitive on original labels. Furthermore, counterfactual evaluations demonstrate instruction following abilities, where it is shown that DG-ICL-Sym retains 68% of its performance when definitions contradict pre-trained lexical priors, whereas standard instruction tuning elicits significantly reduced retention of 21%. Finally, we show that DG-ICL enables zero-shot speech clustering into user-defined categories specified on the fly

</details>

## Computer vision

### [Let Vision-Language Models Generate Images through Their Representations](https://arxiv.org/abs/2611.31237)
*JB Kim, Byungwoo Jeon, Kyungmin Lee et al.* · `cs.CV` · arXiv:2611.31237v1 · relevance 0.14

- **In one sentence**: Proposes Integral, a method that turns a pretrained vision-language model into a unified model for both image understanding and image generation by sharing one visual representation space between the two tasks.
- **In plain words**: Many AI systems can either understand pictures (answer questions about them) or create pictures, but rarely both well in one model. This paper starts from an existing model that already understands images and adds the ability to generate them, reusing what it has already learned. The authors report that using the same visual representations for understanding and generation helps generation learn better than using a separate visual representation, even though reconstruction quality was similar.
- **Why it matters**: It suggests that the internal representations learned for understanding images can also serve as a foundation for generating them, which bears on how future single models might be built. The text does not show how broadly this holds beyond the controlled comparisons described.
- **Background needed**: - Vision-language model: an AI model trained to connect images and text, used here to understand pictures.
- Visual generation: producing new images, for example from a text prompt.
- Unified multimodal model: a single model that handles both understanding and generation.
- Visual representation / encoder: the internal numerical description an AI builds of an image; the encoder that produces it is here kept frozen (not retrained).
- Hierarchical representations: descriptions taken from several layers of the network, from low-level detail to high-level meaning.
- Mixture-of-Transformers (MoT): a design where separate processing streams share some layers; the "block-wise" variant connects them only at block boundaries.
- Reconstruction fidelity: how faithfully an image can be recreated from its representation. · level: research-level

<details><summary>Original abstract</summary>

Recent unified multimodal models aim to combine visual understanding and generation within a single model, yet effectively integrating the two capabilities remains challenging. Leveraging pretrained vision-language models offers a way to build on already learned multimodal knowledge, but making this knowledge effectively accessible to visual generation remains nontrivial. We find that a central challenge lies in the heterogeneous visual representations used for understanding and generation. To address this challenge, we introduce Integral, which converts a pretrained vision-language model into a unified multimodal model by constructing a shared visual representation space across the two capabilities. Integral implements this design through two complementary components. Abstraction Fusion constructs shared visual tokens by aggregating hierarchical representations from the frozen vision encoder, while Block-wise MoT introduces a lightweight generative stream that interacts with the vision-language model only at block boundaries. Our approach effectively preserves the pretrained understanding capability while extending it to strong visual generation. Controlled comparisons further demonstrate that sharing visual representations between understanding and generation substantially improves generative learning compared with using a separate visual representation space, despite comparable reconstruction fidelity. These results suggest that representations learned by pretrained vision-language models already provide an effective foundation for visual generation.

</details>

### [VUOD: A Versatile Unsupervised Outlier Detection Framework for Natural, Industrial, Medical Images and Beyond](https://arxiv.org/abs/2611.28608)
*Zhonghang Liu, Siyuan Chen, Jingwen Yu et al.* · `cs.CV` · arXiv:2611.28608v1 · relevance 0.12

- **In one sentence**: VUOD proposes an unsupervised outlier detection framework that improves feature discriminativeness using intrinsic distribution priors, aiming to work beyond natural images on industrial and medical images, and reports state-of-the-art results across 14 benchmarks in 3 domains.
- **In plain words**: The paper is about spotting images that look unusual, such as a defective part on a factory line or an abnormal scan, without being given labeled examples of what is faulty. Many existing tools work well on everyday photos but lose accuracy on factory and medical images. The authors describe a general method that improves how the system represents images so it can separate normal from unusual ones, and report that it performs best on the 14 test datasets they used.
- **Why it matters**: Reliable detection of unusual images without labeled defects matters for industrial inspection and medical screening, where faulty or abnormal examples are rare. The text also says the method can be added to other vision tasks such as image classification and 3D reconstruction to improve robustness, though the text gives no details on those experiments.
- **Background needed**: - Unsupervised outlier detection: flagging inputs that differ from a set of normal examples, with no labels marking which are abnormal.
- Feature extractor: a model that turns an image into a list of numbers (features) summarizing it; "frozen and pre-trained" means a model trained on other data whose weights are not updated.
- Feature discriminativeness: how well the features separate normal from unusual images.
- Distribution priors: assumptions about how normal data is statistically shaped, used to guide learning.
- Benchmark datasets: standard public test collections used to compare methods.
- Plug-and-play: a component that can be added to an existing system without redesigning it.
- The text is a short abstract; it does not give the method's details, the specific scores, or the exact datasets. · level: research-level

<details><summary>Original abstract</summary>

Unsupervised outlier detection that automatically identifies whether visual systems involve anomalous images is a significant research topic. However, most approaches are limited to natural images because they rely on frozen and pre-trained feature extractors. So that their performance cannot be maintained in practical scenarios, especially for industrial inspection and medical imaging. In this work, we first revisit this task and then introduce a versatile unsupervised outlier detection framework to enrich the application domains. The core idea of this framework is to improve feature discriminativess via exploiting intrinsic distribution priors. Evaluated on 3 domains and 14 benchmark datasets, our proposed solution achieves state-of-the-art performance and significantly outperforms existing methods. More importantly, we show its plug-and-play property that can be integrated into diverse visual applications to improve their robustness, such as image classification and 3D reconstruction.

</details>

## Reinforcement learning

### [Reinforcing Diffusion Models by Instantaneous Trajectory Distribution Matching](https://arxiv.org/abs/2611.30986)
*Yihong Luo* · `cs.LG` · arXiv:2611.30986v1 · relevance 0.25

- **In one sentence**: The paper proposes iTDM, an infinitesimal-step variant of Trajectory Distribution Matching that uses an online auxiliary denoiser to fix baseline-induced gradient drift when reinforcement-learning-tuning diffusion models with deterministic ODE sampling.
- **In plain words**: Image-generating diffusion models can be tuned to better match reward signals, such as preference scores or text accuracy. The authors argue that a popular family of tuning methods quietly assumes the model being trained behaves like the model that generated the training samples, and this assumption breaks in common situations, making training unstable. Their proposed method, iTDM, is designed to keep the training signal anchored to the generating behavior and reports better results on several generation benchmarks.
- **Why it matters**: Stable fine-tuning of generative models with rewards matters for making them follow instructions and preferences reliably. The text reports faster convergence on the GenEval2 benchmark and training that does not collapse at a high score, but these are the authors' own experimental claims and the wider significance is not established from the text alone.
- **Background needed**: - Diffusion models generate images by starting from noise and removing it step by step.
- Reinforcement learning (RL) here means adjusting a model using a reward score on its outputs.
- ODE sampling is a deterministic generation path, so no random noise is injected at each step.
- Reward-weighted regression is a method that nudges the model toward samples, weighted by how good they scored.
- Baseline subtraction is a standard variance-reduction trick in RL that should not change the expected gradient.
- Classifier-free guidance (CFG) is a technique that strengthens prompt adherence during sampling.
- Off-policy or offline updates reuse samples produced by an older or different model. · level: research-level
- Matched keywords: reinforcement learning, offline RL

<details><summary>Original abstract</summary>

Forward diffusion reinforcement learning (RL)---enabling deterministic ODE sampling without trajectory backpropagation---has grown increasingly popular for efficiently aligning diffusion models. However, we reveal that existing methods essentially rely on signed reward-weighted regression (RWR), regressing the \emph{trainable policy} velocity onto rollouts from a \emph{behavior distribution}. Unbiased baseline subtraction implicitly assumes that the policy velocity equals the behavior marginal velocity---an idealized assumption violated under classifier-free guidance (CFG) rollouts, offline/off-policy updates, and imperfect online self-consistency. This \emph{behavior--policy mismatch} breaks baseline invariance and injects \emph{baseline-induced gradient drift}, destabilizing training. To resolve this issue, we propose \textbf{I}nstantaneous \textbf{T}rajectory \textbf{D}istribution \textbf{M}atching (\textbf{iTDM}), taking the infinitesimal limit of Trajectory Distribution Matching toward a time-local reward-guided target via the posterior-score identity to yield a sample-level gradient anchored at the behavior velocity without learning an additional reward-tilted target score. Tracking this velocity with an online auxiliary denoiser guarantees exact baseline invariance at the auxiliary optimum, effectively suppressing baseline drift across both online and offline RL. Extensive experiments across compositional generation, text rendering, and preference alignment show that iTDM achieves state-of-the-art in-domain and out-of-domain performance. Notably, on the challenging GenEval2 benchmark, iTDM converges nearly $3\times$ faster than competing methods while scaling smoothly to $0.87$ without collapse. Code is available at https://github.com/Luo-Yihong/iTDM

</details>

### [Direct Feedback Policy Optimization for AI Coding Agents](https://arxiv.org/abs/2611.29193)
*Fei Ding* · `cs.LG` · arXiv:2611.29193v1 · relevance 0.23

- **In one sentence**: DFPO is a single-trajectory reinforcement learning method for training AI coding agents that learns from one rollout at a time, reporting higher task resolution rates than GSPO under matched base models and harnesses.
- **In plain words**: This paper looks at training AI systems that write, edit, and test code over many steps. Current training methods often give only a single pass/fail score at the very end, which makes it hard to tell which earlier steps helped. The authors propose a method, Direct Feedback Policy Optimization (DFPO), that learns from a single attempt at a task, and report that it solves more tasks than the GSPO comparison method when the underlying model and test setup are held the same.
- **Why it matters**: Training agents that need many steps is expensive, and methods that avoid repeating each task many times could cut that cost. The text gives only the headline comparison, so it is unclear how large the gain is or how well it holds beyond the reported setup.
- **Background needed**: - Reinforcement learning: training a model by rewarding good outcomes and penalizing bad ones.
- Coding agent: an AI model that works through a sequence of actions such as editing files and running tests.
- Sparse terminal reward: a single score given only when the whole task finishes, with no feedback on intermediate steps.
- Group-relative methods: approaches that compare several attempts at the same task to estimate which did better, requiring repeated sampling.
- GSPO: an existing group-based policy optimization method used here as the baseline.
- Task resolution rate: the share of tasks the agent completes correctly.
- Execution harness: the surrounding software that runs the agent and its tools. · level: research-level
- Matched keywords: reinforcement learning

<details><summary>Original abstract</summary>

AI coding agents generate, modify, and validate code through multi-turn interactions. Existing reinforcement learning methods often rely on sparse terminal rewards, making it difficult to assess how intermediate decisions affect task outcomes, and group-relative methods also require repeated sampling for each task. We propose Direct Feedback Policy Optimization (DFPO), a single-trajectory reinforcement learning algorithm that trains directly from a single trajectory. DFPO achieves higher task resolution rates than GSPO under matched base models and execution harnesses.

</details>

## AI safety and alignment

### [What Counts as Attack Success? Evaluating Harmfulness in Red Teaming LLMs](https://arxiv.org/abs/2611.28038)
*Ruyuan Wan, Adriana Alvarado Garcia, Md Toufikuzzaman et al.* · `cs.CL` · arXiv:2611.28038v1 · relevance 0.19

- **In one sentence**: A review of 76 red-teaming papers finds that studies often inherit their definition of harmful AI output from prior datasets, classifiers, or judge prompts, and that different automated evaluators applied to identical outputs can disagree enough to change model comparisons.
- **In plain words**: Researchers often test AI chatbots by trying to make them produce harmful content, then use automated graders to decide whether each attempt succeeded. This paper looks at how those studies define "harmful," and finds that many borrow a definition from earlier work instead of stating their own. When the authors ran the graders from different papers on the same responses, the graders often disagreed, which could change which model looks safer.
- **Why it matters**: Safety results from AI red-teaming are often used to rank models and guide deployment, so unstated grading rules could quietly change those rankings. The paper's main contribution is a call for clearer reporting and validation of evaluators; the text does not show how widely this affects published conclusions beyond the cases examined.
- **Background needed**: - Red teaming: deliberately trying to get an AI system to misbehave, to find its weaknesses.
- Automated evaluator or "judge": another program (often a language model) that labels a response as harmful or not, in place of human reviewers.
- Harmfulness criteria: the rules that decide what counts as harmful, such as whether any non-refusal counts or only output that could plausibly cause harm.
- Attack success rate: the share of attempts that get a model to produce disallowed output, as scored by the evaluator.
- Classifier and judge prompt: the trained model or written instructions an evaluator uses to make its decision. · level: intermediate
- Matched keywords: red teaming

<details><summary>Original abstract</summary>

Judging whether a model response is harmful requires contextual and normative choices, yet red-teaming studies often delegate this judgment to automated evaluators. We examine how harmfulness criteria are specified in red-teaming research and how they carry through to reported results. Reviewing 76 papers, we find that many adopt their criteria from prior datasets, classifiers, or judge prompts rather than defining harmfulness themselves. Applying evaluators from these papers to identical outputs, we find that they can reach different judgments on the same response, which can change conclusions when comparing models. These differences arise partly because evaluators draw the boundary of harm in different places: some count any response that does not refuse, while others count only output that could plausibly cause harm. We argue that red-teaming studies should state their harmfulness criteria and report how they chose and validated their evaluators to support more reliable measurement and interpretation.

</details>

### [Which Loopholes Get Found? Predicting Reward Hacking of LLM Judges Before RL Training](https://arxiv.org/abs/2611.29651)
*Xuanyi Lyu, Yuezhou Zhao, Qing Qin* · `cs.CL` · arXiv:2611.29651v1 · relevance 0.18

- **In one sentence**: The paper proposes "exposure" (a policy's propensity to produce a given degenerate pattern times the LLM judge's false-positive rate) as a pre-training predictor of which reward-hacking loophole GRPO reinforcement learning will exploit first, and tests it causally by seeding patterns into fine-tuning data.
- **In plain words**: When an AI model is trained to satisfy another AI that acts as a grader, it can learn to exploit the grader's weak spots, such as giving a trivial answer the grader wrongly accepts. This paper asks whether we can predict which weak spot will be exploited first before training starts. The authors score each pattern by how often the starting model produces it and how often the grader wrongly accepts it, then check this by deliberately mixing patterns into training data.
- **Why it matters**: Reward hacking, where a trained system games its scoring rule instead of doing the intended task, is a central concern in AI safety, so a way to audit likely exploits before expensive training runs could be useful. The text reports 36 runs across seven judges, but its evidence comes from a specific setup (GRPO, one family of judges, hand-chosen patterns), so how far the prediction generalizes is not established by the text.
- **Background needed**: - Reward hacking: a trained model finds a way to get high scores from its grader without doing what was really wanted.
- LLM judge: a language model used to grade another model's outputs, standing in for a human rater.
- Reinforcement learning (RL): training by trying outputs and reinforcing those that score well.
- GRPO (group relative policy optimization): an RL method that compares several sampled answers to the same prompt and scores each relative to the group average.
- False-positive rate (FPR): how often the judge wrongly accepts a bad answer.
- Latin square: a balanced experimental design that varies several factors together so each is tested under each condition.
- Degenerate answers: trivial outputs, such as a lone bracket, that a flawed judge may still accept. · level: research-level
- Matched keywords: reward hacking

<details><summary>Original abstract</summary>

A policy trained against an LLM judge can learn to exploit its loopholes. Static probes show that such judges accept degenerate answers like a lone "{" or "Thought process:", but not which flaw a policy will find. In GRPO the first loophole to be exploited can be predicted before training from each pattern's exposure, the product of the starting policy's propensity to produce it and the judge's false-positive rate (FPR). To test exposure causally, we seed the patterns into fine-tuning at three doses in a Latin square. Across 36 GRPO runs with seven judges, the first exploited pattern had the highest exposure in all 12 runs with exploitation and the highest FPR in only 6. Predictions recorded before training held in three of four runs with one pattern masked by rule. When only two patterns were seeded, at 3% to 3.8% of the fine-tuning data and chosen so that exposure disagreed with FPR alone or propensity alone, exposure named the first exploited pattern and its onset window in all six runs. Exploitation occurred only on hard prompts, where an accepted exploit gets a large group-normalized advantage. Auditing exposure before RL therefore identifies the loophole a policy will likely exploit first.

</details>

## Interpretability

### [SAE-Audit: Clinical-Trial Prediction via Inference-Time Optimization of Black-Box LLMs Audited by Sparse Autoencoder Evidence](https://arxiv.org/abs/2611.29368)
*Junbo Shen* · `cs.AI` · arXiv:2611.29368v1 · relevance 0.20

- **In one sentence**: SAE-Audit uses concept features from a frozen sparse autoencoder on an open Llama-3.1-8B model, filtered by sparse probes trained on past trials, to write concept-level evidence into prompts that steer black-box LLMs toward better clinical-trial outcome predictions.
- **In plain words**: Clinical trials take years and often fail or stop early, so predicting how a trial will turn out is useful for planning. This paper tests whether giving large AI models a structured list of clinical concepts, drawn from a smaller open model's internal features and linked to past trial outcomes, helps them make better predictions. The authors report that this raised the balanced accuracy of the audited models by roughly 8 to 12 points on the tasks they tried.
- **Why it matters**: Predicting trial outcomes is a costly planning problem, and the approach aims to make AI predictions more checkable by tying them to specific concepts rather than unexplained answers. The text reports gains only on the authors' own tasks and models, so its wider value is unclear until other groups test it.
- **Background needed**: - Clinical trial: a structured study testing a medical treatment; "completes" versus "terminates early" is the outcome being predicted.
- Large language model (LLM): an AI system that generates text; "black-box" means its internals cannot be inspected, only its inputs and outputs.
- Sparse autoencoder (SAE): a tool that decomposes a model's internal activity into many separate, more interpretable features, here treated as clinical concepts.
- Sparse probe: a simple, selective classifier that checks which features predict an outcome.
- Balanced accuracy: an accuracy score that averages performance across outcome classes, so a model cannot score well by always guessing the majority class.
- Inference-time optimization: improving answers by changing the prompt or procedure at use time, without retraining the model.
- Biomni: a biomedical AI agent system named in the paper as a possible host for the method. · level: research-level
- Matched keywords: sparse autoencoder

<details><summary>Original abstract</summary>

Clinical trials are costly and often take years to complete, making early outcome prediction valuable for trial planning. Large language models (LLMs) are increasingly used to forecast clinical-trial outcomes, yet their predictions remain unreliable and their rationales may not faithfully reflect the evidence underlying their answers. On tasks such as predicting whether a registered clinical trial will complete or terminate early, frontier LLMs perform only modestly above chance in our experiments. We introduce SAE-Audit, which optimizes a black-box LLM at inference time with evidence obtained from a deployable open model. A frozen sparse autoencoder (SAE) on Llama-3.1-8B-Instruct is converted into a vocabulary of clinical concepts. Sparse probes fitted on past trials determine which concepts are associated with the outcome. For a new protocol, the concepts detected by the probe are written as evidence, each with the direction and strength of its association with the outcome, and the LLM being audited optimizes its answer in the light of this evidence. Without additional training, SAE-Audit raises balanced accuracy of deepseek-v4-flash by 9.6--12.0 points on five clinical-trial prediction tasks and raises GPT-5.6-terra by 8.0 points on trial completion, exceeding other agentic inference-time optimization methods by a large margin. As an auxiliary, SAE probes module within SAE-Audit is itself accurate and auditable, providing natural-language explanations directly derived from verified concept contributions and protocol evidence, without requiring additional LLMs at inference time. SAE-Audit provides verifiable, concept-level evidence for more accurate and auditable clinical-trial prediction. It can also be embedded into biomedical AI agents such as Biomni to optimize their performance.

</details>

### [SAEPO: Sparse-Autoencoder-Guided Credit Assignment for Policy Optimization](https://arxiv.org/abs/2611.29936)
*Yusong Zhao, Zihao Zhao, Zirui Zhang et al.* · `cs.AI` · arXiv:2611.29936v1 · relevance 0.17

- **In one sentence**: SAEPO uses concepts from a pretrained sparse autoencoder to assign token-level credit in outcome-supervised policy optimization (GRPO and GSPO) for LLM reasoning, reporting gains on math and code benchmarks.
- **In plain words**: Language models are often trained to reason using only a final right-or-wrong score for the whole answer, which does not show which individual steps helped or hurt. This paper proposes SAEPO, which uses a tool that finds recurring concepts inside a model's internal activations to score each word-piece of a reasoning attempt, so that good reasoning steps get more credit and wrong final-answer pieces get penalized. The authors report that this improves average scores on six math and two code benchmarks across three model backbones, with gains of up to 6.63% (math) and 5.57% (code).
- **Why it matters**: Better credit assignment could make reinforcement-learning training of reasoning models more efficient, which matters because such training is costly. The text does not establish how broadly the gains hold beyond the reported benchmarks and models, so its significance is still uncertain.
- **Background needed**: - Reinforcement learning with verifiable rewards (RLVR): training a model by giving it a score only when its final answer can be checked as correct.
- Credit assignment: deciding which steps in a long attempt deserve credit or blame for the result.
- Policy optimization (e.g., GRPO, GSPO): families of algorithms that adjust a model's output probabilities based on rewards.
- Sparse autoencoder (SAE): a tool trained without labels to break a model's internal activations into a set of recurring, interpretable features or "concepts."
- Advantage shaping: modifying the reward signal per token so training pushes harder on some tokens than others.
- Base model: a pretrained model before instruction tuning. · level: research-level
- Matched keywords: sparse autoencoder

<details><summary>Original abstract</summary>

Reinforcement Learning with Verifiable Rewards (RLVR) has demonstrated strong performance in improving large language model (LLM) reasoning, yet its credit-assignment signal remains coarse. Outcome verifiers provide scalable supervision by judging whether a completed response is correct, but they do not directly indicate which intermediate reasoning tokens contribute to success or failure. As a result, policy optimization can be inefficient, especially when training base models directly from sparse outcome feedback. In this paper, we introduce SAEPO, a Sparse AutoEncoder-guided token-level credit assignment method for outcome-supervised Policy Optimization. Rather than treating correctness only as a rollout-level (sequence-level) signal, SAEPO uses a pretrained sparse autoencoder (SAE) to build token-level semantic representations within reasoning trajectories; it scores each token based on the SAE concepts (e.g., penalizing wrong "final-answer" tokens but rewarding correct "reasoning-process" tokens), learned in an unsupervised manner, to achieve fine-grained credit assignment. SAEPO is a plug-in advantage-shaping module compatible with various policy optimization algorithms. We instantiate SAEPO with both GRPO and GSPO, covering token-ratio and sequence-ratio policy-gradient objectives, and evaluate SAEPO across three LLM backbones on six math and two code benchmarks. Empirical results show that SAEPO improves both the math and code benchmark averages over the matched baselines, with gains of up to 6.63% and 5.57%, respectively. On Qwen3-1.7B-Base, training curves also show faster early accuracy growth. Feature and token-level analyses suggest that the SAE-derived signal favors question-relevant concepts and reasoning tokens.

</details>

## AI for mathematics

### [Improving semantic equivalence in research-level math formalization](https://arxiv.org/abs/2611.28819)
*Ayush Khaitan, Liam Fowl, Tom\`as Ortega et al.* · `cs.AI` · arXiv:2611.28819v1 · relevance 0.21

- **In one sentence**: The paper builds a dataset of 4,076 audited differences between research-level natural-language math and its Lean formalizations, and tests whether training on those differences improves a model's ability to write Lean inside large real projects.
- **In plain words**: Mathematicians often write proofs in ordinary language, and computer proof assistants need them restated in a strict formal code called Lean. This paper collects examples of how the formal versions quietly differ from the originals, and checks whether teaching an AI model from those differences helps it write better formal math. The reported results: complete proofs rose from 11% to 20%, and statements matching the project's own formalization rose from 30% to 39%.
- **Why it matters**: Writing formal proofs for research-level mathematics is slow and hard, so a more reliable AI assistant for it would matter. The paper also reports that the gain came from the difference examples themselves, not from simply telling the model the differences in advance, which is a useful finding about what training signal helps; its broader significance beyond these benchmarks is not established by the text.
- **Background needed**: - Autoformalization: translating informal math text into a formal language a computer can check.
- Lean: a programming language and proof assistant in which proofs are checked by the computer.
- Semantic equivalence: whether a formal statement means the same thing as the intended informal one, not just whether it compiles.
- Lean projects/repositories: large collections of formalized math code, here tens of thousands of lines.
- Train/test split here is by repository, so test projects are unseen during training.
- Complete proof rate and gold agreement are the two reported measures; the text does not detail how they are scored. · level: research-level
- Matched keywords: Lean, autoformalization

<details><summary>Original abstract</summary>

Formalizing mathematics in Lean is never a word-for-word translation of a paper: a Lean formalization changes definitions, strengthens hypotheses, splits arguments, and adds lemmas the paper never mentions. It stands to reason that a model that is good at autoformalization must be a good predictor of how a natural language source must differ from its faithful Lean formalization. With that in mind, we collect 4{,}076 audited examples of such changes from 832 Lean projects that formalize research-level mathematics, and use them to ask a practical question: how well can a model \emph{write} Lean inside a real research-level project that may contain tens of thousands of lines of code, and does training on discrepancies between natural language sources and their faithful Lean formalizations help? Our training set consists of 3{,}431 tasks from 141 repositories, and the test set consists of 645 tasks from the remaining 27 repositories. Training on in-project Lean nearly doubles complete proofs ($11\% \to 20\%$) and raises the share of statements in gold agreement with the project's own formalization by nearly a third ($30\%$ to $39\%$). The gain comes from the pairs themselves: an adapter trained only to predict how the Lean will differ, or a model told the difference in advance, barely helps. Training on where formalizations depart from their sources is thus an effective way of improving semantic equivalence in research-level formalization.

</details>

### [AI-Assisted Auto-formalization for Trustworthy Scientific Computing: Case Studies and Lessons Learned](https://arxiv.org/abs/2611.31033)
*Mohit Tekriwal, Het Mankad, Naifeng Zhang et al.* · `cs.AI` · arXiv:2611.31033v1 · relevance 0.16

- **In one sentence**: A systematic study of AI agents auto-formalizing (translating into machine-checkable proofs) numerical and scientific computing results, yielding a cross-layer taxonomy of failure modes and a workflow for recurring proof patterns.
- **In plain words**: This paper asks whether AI coding and math agents can turn applied-science computing methods into formal proofs that a computer can check, not just the abstract theorems that mathematicians usually formalize. The authors ran case studies across several layers of scientific computing software and recorded where and why the agents went wrong. They report a taxonomy of failure types, the kind of expert guidance each layer needed, and practical advice for using such agents while keeping the math sound.
- **Why it matters**: Most recent reports of AI formalizing mathematics concern pure math, so this work tests the harder applied case, which matters for U.S. Department of Energy scientific software. The text does not show how large or general the findings are, so their broader reach is uncertain.
- **Background needed**: - Formalization: writing a mathematical argument in a formal language (such as Lean or Coq) so a computer can verify every step.
- Auto-formalization: using AI to do this translation automatically or semi-automatically.
- Scientific computing: numerical methods that approximate solutions to equations arising in physics, engineering and modeling, where results depend on algorithms and software layers.
- Pure vs. applied math: pure math proves abstract theorems; applied math often describes procedures or modeling choices, which are harder to state as clean theorems.
- Failure modes: the recurring ways an AI's attempted proof or translation goes wrong. · level: research-level
- Matched keywords: mathematical reasoning

<details><summary>Original abstract</summary>

Agentic AI tools have recently had success in mathematical reasoning. Both general purpose coding agents such as Claude Code and Codex, and specialized mathematics agents such as Aristotle, have been used for formalizing mathematical problems such as Fermat's last theorem, Erd\H{o}s problems and several IMO level math problems. However, much of these efforts are concentrated in the pure mathematics domain, which benefits from relatively self-contained theorem statements, fixed mathematical representation and extensive support in existing formal libraries. Applied mathematics, on the other hand, presents additional challenges because the source may describe a computational procedure or modeling transformation rather than a declarative theorem. In this work, we present a systematic study of AI-assisted auto-formalization for scientific computing (SC), a domain in applied mathematics central to U.S. Department of Energy applications. Through case studies spanning hierarchical abstraction layers in SC software stack, we evaluate not only whether AI agents can complete numerical proofs, but also where and why they fail across the stack. Our primary contribution is a cross-layer taxonomy of failure modes and an analysis of the form of expert feedback required at each layer to recover mathematical soundness. From these observations, we derive a workflow for recurring proof patterns and practical guidance for using AI agents while preserving mathematical soundness. Our results characterize both the practical value and the current limitations of AI-assisted formalization for trustworthy scientific computing.

</details>

## Robotics and embodied AI

### [SAGE-Drive: Benefit-Aware Adaptive Reasoning for Autonomous Driving Planning](https://arxiv.org/abs/2611.29947)
*Donglei Rong, Wenbin Yao, Congcong Bai et al.* · `cs.RO` · arXiv:2611.29947v1 · relevance 0.14

- **In one sentence**: SAGE-Drive learns to predict, from an initial trajectory plan and multimodal scene inputs, when explicit reasoning will reduce planning error for autonomous vehicles, and invokes it only in the top-predicted scenarios under a fixed compute budget.
- **In plain words**: Self-driving cars can think through tricky traffic step by step, but that thinking costs extra computing time and does not always help. This paper asks when that extra reasoning is worth doing. The authors compared planned routes with and without reasoning on 1,497 driving scenes, found that reasoning helped in about 53.5% of cases and hurt in 46.5%, and built a predictor that decides which scenes deserve the extra thinking.
- **Why it matters**: Reasoning that is applied selectively could cut the computing cost of smarter driving planners without giving up much accuracy. The reported results are close to the always-reason baseline at a 35% budget, but this is a single paper's test on one dataset, so its wider value is not yet established.
- **Background needed**: - Trajectory planning: deciding the path a vehicle should follow over the next few seconds.
- Explicit reasoning: a step-by-step processing stage in an AI model that works through the scene before outputting a plan; it is more expensive to run.
- Average displacement error (ADE): the average distance in meters between the planned path and the true path; lower is better.
- Reasoning budget: the fraction of scenarios allowed to use the costly reasoning step (here 20% or 35%).
- Benefit label: for each scene, the error reduction from reasoning, computed by comparing paired plans with and without it.
- Random selection: a baseline that picks which scenes get reasoning at random, used for comparison. · level: research-level

<details><summary>Original abstract</summary>

Explicit reasoning enables autonomous vehicles (AVs) to interpret complex traffic interactions and support trajectory planning, but introduces additional computational demands. Determining when explicit reasoning can improve planning accuracy remains a key challenge, as its benefits vary across driving scenarios. To address this challenge, this study proposes Scene-Adaptive Gating of Explicit Reasoning for Driving (SAGE-Drive), a benefit-aware adaptive reasoning framework for autonomous driving planning. First, paired planning outcomes with and without explicit reasoning are analyzed to measure the reasoning benefit, i.e., the reduction in planning error achieved by explicit reasoning, which serves as the supervision label. SAGE-Drive then learns to predict these benefits using geometric features of the initial trajectory planned without reasoning and multimodal scene information, and invokes explicit reasoning only for the scenarios with the highest predicted benefits under a predefined reasoning budget. Experiments on 1,497 paired driving scenarios reveal that explicit reasoning improves planning accuracy in 53.5% of cases while degrading it in 46.5%, yielding a near-zero average benefit. On the test set, with a 20% reasoning budget, SAGE-Drive achieves an average displacement error (ADE) of 1.5191 m, compared with 1.5252 m for random selection. At a 35% budget, it achieves an ADE of 1.5148 m, close to the 1.5141 m obtained when reasoning is applied to every scenario. These findings establish the predicted reasoning benefit as an effective criterion for reasoning selection, allowing explicit reasoning to be invoked where it improves planning accuracy at a fraction of its computational cost.

</details>

### [Your Diffusion-Based Driving Planner Only Needs a Nudge](https://arxiv.org/abs/2611.29123)
*Zilin Wang, Guozheng Ma, Saeed Rahmani et al.* · `cs.RO` · arXiv:2611.29123v1 · relevance 0.14

- **In one sentence**: PlanNudge freezes a pretrained diffusion-based driving planner and trains a small MLP policy with off-policy RL to output a two-dimensional speed and curvature adjustment at each step, evaluated on nuPlan.
- **In plain words**: Self-driving planners trained on human driving data can drift into unsafe situations, such as collisions or leaving the road, when their own small errors compound during closed-loop driving. This paper proposes keeping the trained planner fixed and training a small add-on component that makes small corrections to its planned speed and turning curvature. The authors report that this approach matches or exceeds the previous best reinforcement-learning fine-tuning method on six nuPlan settings while using about a sixth of the environment steps.
- **Why it matters**: It offers a cheaper way to post-train generative driving planners without retraining the whole model, which matters for safety and data efficiency in autonomous driving. The text does not show how well the results transfer beyond nuPlan's simulated benchmark, so real-world impact is unclear.
- **Background needed**: - Diffusion model: a generative model that produces outputs by gradually removing noise; here it generates candidate driving trajectories.
- Covariate shift: when a model meets situations it was not trained on, often because its own earlier mistakes lead it there.
- Closed-loop simulation: testing where the planner's actions change the world it sees next, rather than replaying recorded data.
- Reinforcement learning (RL) fine-tuning: adjusting a trained model using reward signals from its actions.
- Off-policy RL: learning from past experience stored in a buffer, not only from the current policy's actions.
- Receding horizon: planning a full path but executing only the first part before replanning.
- nuPlan: a public autonomous-driving benchmark built on real-world driving logs.
- MLP (multilayer perceptron): a basic feedforward neural network. · level: research-level

<details><summary>Original abstract</summary>

Diffusion-based planners capture the multimodality of human driving behavior well, yet covariate shift in closed-loop driving can lead them to generate trajectories that result in collisions or road departures. Reinforcement learning (RL) finetuning offers a promising way to tackle this issue, but applying it to diffusion-based planners is complicated by their iterative denoising process and receding-horizon execution. We find that small adjustments to the planned trajectories can prevent many of these unsafe outcomes. Motivated by this observation, we propose PlanNudge, which preserves the learned planning capabilities of a pretrained diffusion-based planner by freezing it and trains a lightweight policy that we call the nudge policy. At each planning step, the nudge policy outputs a nudge, a two-dimensional adjustment of the speed and curvature of the plan from the frozen planner. The nudge policy is a multilayer perceptron that predicts the nudge in a single forward pass, and both dimensions directly change the motion of the vehicle, so standard off-policy RL can train it in closed-loop simulation. We evaluate PlanNudge on nuPlan, a large-scale autonomous driving benchmark based on real-world driving data. In all six settings, PlanNudge matches or exceeds the final scores of the previous state-of-the-art RL finetuning method while using about one sixth as many environment steps and less than one fifth as much model compute. We also provide guidelines for reward shaping, value learning, and exploration when using off-policy RL to post-train autonomous driving planners. Our results are reported with means and standard deviations over six training runs. Project page: https://zerlinwang.github.io/plannudge/

</details>

## Security and cryptography

### [LaTSEC: Lattice-Based Threshold Signatures with Native Non-Interactive Identifiable Abort and Compact Per-Party Storage](https://arxiv.org/abs/2611.30063)
*Muhammad Arzaki, Muhammed F. Esgin, Markku-Juhani O. Saarinen et al.* · `cs.CR` · arXiv:2611.30063v1 · relevance 0.13

- **In one sentence**: LaTSEC is a three-round lattice-based threshold signature scheme that identifies misbehaving signers non-interactively by checking each partial signature against a single per-party public abort key, using the SEC ramp everywhere-short secret sharing scheme and a new Repeated-A Matrix Hint-MLWE assumption that the authors reduce from standard MLWE.
- **In plain words**: The paper is about a way for a group of people, each holding a secret piece of a digital signing key, to jointly sign a document while still being able to point out which member cheated or sent a bad piece. The authors propose a scheme where each member holds only one small secret share and has one public check key, so cheaters can be caught without extra back-and-forth rounds or heavy proofs. They report security proofs under standard lattice assumptions, and for 60 parties at 128-bit security they give concrete sizes: about 14.3 KiB of secret per party and a 24 KiB public key per party.
- **Why it matters**: Threshold signatures that resist quantum attacks are a live topic for protecting shared keys, and reducing per-party storage while keeping cheater identification is a practical goal. The text only gives its own benchmarks and proofs; its real-world performance and whether the new assumption holds up under further scrutiny are not established by this description alone.
- **Background needed**: - Threshold signature: a signature produced jointly by t-of-n parties, so no single party holds the whole key.
- Identifiable abort: if signing fails, the protocol can name which party misbehaved.
- Lattice-based cryptography: security rests on hard problems about geometric lattices, believed to resist quantum computers.
- MLWE / MSIS: standard lattice hardness assumptions (module learning-with-errors and module short integer solution) that the security proofs rely on.
- Secret sharing: splitting a secret into pieces so only enough pieces together can reconstruct it; "everywhere-short" means each piece has small coefficients.
- Zero-knowledge proof: a way to prove a statement is true without revealing the secret behind it.
- Hint-MLWE: a variant of MLWE where the adversary also receives some extra correlated information (hints). · level: research-level

<details><summary>Original abstract</summary>

We present $\mathsf{LaTSEC}$, a three-round lattice-based threshold signature scheme with native non-interactive identifiable abort. Each party holds one small-norm signing share and is associated with one public abort key, against which its partial signature is verified directly, without zero-knowledge proofs or an additional interactive protocol. Prior lattice-based threshold signatures that identify misbehaving parties rely on one of three mechanisms: zero-knowledge proofs, an additional interactive protocol, or an everywhere-short secret sharing scheme in which each party holds multiple signing shares, each with its own public abort key. Compared with schemes that use the third mechanism, $\mathsf{LaTSEC}$ substantially reduces per-party storage. The construction uses $\mathsf{SEC}$, a recent ramp everywhere-short secret sharing scheme based on lossless expanders that gives each party a single short share. We prove correctness, identifiable-abort security, and threshold unforgeability under the standard $\mathsf{MLWE}$ and $\mathsf{MSIS}$ assumptions. The unforgeability proof introduces the Repeated-$\boldsymbol{A}$ Matrix Hint-MLWE problem, a new variant of $\mathsf{MLWE}$ with hints that captures the complete tuple of correlated public abort keys. We rigorously prove that this new variant admits a reduction from the standard $\mathsf{MLWE}$ problem. For 60 parties at 128-bit security, $\mathsf{LaTSEC}$ tolerates up to 6 corrupted parties, and, empirically, a randomly chosen set of at least 46 parties can sign with probability at least 0.99. Each party holds one signing share of about 14.3 KiB and is associated with one 24-KiB public abort key.

</details>

### [Optimal Private Gaussian Multi-sampling](https://arxiv.org/abs/2611.30146)
*Raoof Zare Moayedi, Mohammad Hossein Yassaee, Javad B. Ebrahimi* · `cs.DS` · arXiv:2611.30146v1 · relevance 0.13

- **In one sentence**: The paper gives polynomial-time algorithms for multi-sampling from a Gaussian distribution under approximate (ε,δ)-differential privacy, using about m + d√m/ε input samples to produce m exactly independent outputs, with matching lower bounds that hold even for dependent outputs.
- **In plain words**: The paper studies how to produce many fake-but-realistic data points drawn from a bell-shaped (Gaussian) pattern without revealing too much about the private real data used to learn that pattern. The authors show how to make m new samples that are truly independent of each other while needing far fewer real input samples than running a single-sample method separately for each output. The text says the sample cost grows with the square root of the number of outputs rather than linearly, and that this is close to optimal.
- **Why it matters**: Privacy-preserving data release is a practical concern in statistics and machine learning, and reducing the data cost of generating many private samples is a useful improvement. Based only on the abstract, the result is a theoretical sample-complexity bound; its practical impact depends on details not given here.
- **Background needed**: - Differential privacy: a guarantee that the output of an algorithm reveals little about any single individual's record in the input data; (ε,δ) is the standard formal measure, with smaller values meaning stronger privacy.
- Gaussian (normal) distribution: the familiar bell-shaped distribution, described by a mean and covariance (how the dimensions spread and relate).
- Sampling: producing new data points that look like draws from a given distribution.
- Sample complexity: how many input data points an algorithm needs.
- Total variation distance: a measure of how different two probability distributions are; "α-close" means they differ by at most α in this sense.
- Independence: outputs whose values do not influence each other; the paper's concern is that privacy and robustness steps can accidentally make outputs depend on each other.
- Dimension d and number of outputs m: d is the number of features per data point; m is how many new samples are generated. · level: research-level

<details><summary>Original abstract</summary>

We give polynomial-time algorithms for Gaussian multi-sampling under approximate $(\varepsilon,\delta)$-differential privacy, with optimal sample complexity up to logarithmic factors. Our main construction uses $\widetilde{O}(m+d\sqrt{m}/\varepsilon)$ independent input samples from a $d$-dimensional Gaussian $P$ with unknown mean and covariance to generate $m$ exactly independent outputs. Their joint distribution is $\alpha$-close in total variation to $P^{\otimes m}$. Our lower bounds hold even for dependent outputs under the same joint accuracy guarantee, showing that exact independence incurs no additional sample cost beyond logarithmic factors. The single-sampler of Iverson, Kamath, and Mouzakis [COLT 2025] uses $\widetilde{O}(d/\varepsilon)$ input samples. Running it on a separate input dataset for each of $m$ outputs therefore costs $\widetilde{O}(md/\varepsilon)$ in total. Our construction reduces this dimension-dependent sample cost from linear to square-root dependence on the number of outputs. Our approach builds on the stable weighted statistics of Brown, Hopkins, and Smith [COLT 2023], also used for Gaussian single-sampling by Iverson, Kamath, and Mouzakis. To control privacy loss when the entire batch shares these statistics, we compare the joint output densities and obtain a privacy bound that scales with the square root of the batch size. The stability step downweights influential records and can reject the entire batch. Both actions can make the outputs dependent. Our correction restores exact independence while preserving differential privacy and joint accuracy.

</details>

## Algorithms and complexity

### [Weighted Flow Time Does Not Admit Constant-Competitive Randomized Algorithms](https://arxiv.org/abs/2611.30319)
*Alexander Lindermayr* · `cs.DS` · arXiv:2611.30319v1 · relevance 0.13

- **In one sentence**: The paper proves that no randomized online algorithm can be O(1)-competitive against an oblivious adversary for preemptive single-machine scheduling minimizing total weighted flow time, closing the randomized case of a long-open question, with lower bounds of order min{log log W, log log log min{P, D, n}}.
- **In plain words**: The paper studies how to schedule jobs on one machine as they arrive over time, where jobs can be paused and resumed, and the goal is to keep the total weighted waiting time low without knowing future jobs. Earlier work showed that no deterministic method can stay within a constant factor of the best possible schedule; this paper shows the same holds even when the method is allowed to make random choices. The authors also give explicit lower bounds on how badly any randomized method must perform as the job sizes, weights, and counts grow.
- **Why it matters**: It settles the remaining case of a question that has been open for a long time in online scheduling, so it fixes what is achievable for this problem. The text does not discuss applications beyond scheduling theory, so any wider relevance is unclear from the text alone.
- **Background needed**: - Online algorithm: makes decisions as inputs arrive, without knowing the future.
- Competitive ratio: the worst-case factor by which an online method's cost exceeds the best offline (all-knowing) cost; O(1) means a fixed constant factor.
- Flow time: how long a job waits from arrival until it finishes; weighted flow time multiplies each job's wait by an importance weight.
- Preemptive scheduling: a running job may be paused and resumed later.
- Randomized algorithm vs. deterministic: randomized methods make random choices; an oblivious adversary fixes the input in advance without seeing those random choices.
- Density: weight divided by size; W, P, D, n are ranges of weights, sizes, densities and the number of jobs.
- High probability: the lower bound holds with probability close to 1. · level: research-level

<details><summary>Original abstract</summary>

We study online preemptive scheduling on a single machine with the objective of minimizing the total weighted flow time. Bansal and Chan (SODA 2009) showed that no deterministic online algorithm is $O(1)$-competitive for this problem. We show that no randomized online algorithm is $O(1)$-competitive against an oblivious adversary either. This settles the remaining case of the long-standing question whether the problem admits an $O(1)$-competitive online algorithm. Quantitatively, every randomized online algorithm has a competitive ratio in $\Omega(\min\{\log\log W,\log\log\log\min\{P,D,n\}\})$, where $n$ is the number of jobs and $W$, $P$, and $D$ are the ratios of the largest to the smallest job weight, size, and density (weight divided by size), respectively. The lower bound also holds with high probability, with the same asymptotic dependence on the instance parameters. For every $\rho\ge1$ and every randomized online algorithm, there is an instance on which the cost of the algorithm is at least $\rho$ times the optimal cost with probability at least $1-2^{-2^\rho}$. Both lower bounds hold even if the algorithm knows in advance the size and weight of every job in release order and, for any fixed $\varepsilon>0$, every interarrival time up to a factor of $1+\varepsilon$.

</details>

### [A Local-to-Global Approximation Framework for Covering Disjointness-Compliable Set Families](https://arxiv.org/abs/2611.29237)
*Jingyang Zhao, Mingyu Xiao* · `cs.DS` · arXiv:2611.29237v1 · relevance 0.13

- **In one sentence**: The paper gives a local-to-global framework that turns a polynomial-time approximation for a local tree problem into a constant-factor approximation for covering disjointness-compliable vertex-set families by edges, with applications to generalized point-to-point connection, multiroot quota tree (including multiroot k-MST), and a randomized result for multiroot covering Steiner.
- **In plain words**: Many network design tasks ask for the cheapest set of links that makes a required collection of groups of points connected in an acceptable way. The paper studies a general version of this task and shows that if you can solve a small, local version of it well, you can solve the full problem to within a guaranteed factor of the best possible cost. The authors apply this to several specific network problems that previously lacked any polynomial-time constant-factor guarantee, according to the text.
- **Why it matters**: The framework is a general recipe rather than a single problem fix, so it may apply to other network design problems that share its structure. Its practical reach beyond these named problems is not established in the text.
- **Background needed**: - Approximation algorithm: a method that runs in polynomial time and returns a solution whose cost is within a known factor of the optimum.
- Polynomial-time: running time grows at most as a fixed power of the input size, so the method is efficient in principle.
- Spanning tree / Steiner tree: a set of edges connecting chosen vertices at minimum total cost, possibly using extra intermediate vertices.
- Disjointness-compliable family: a collection of vertex sets where the union of disjoint feasible sets stays feasible; the paper's precise definition is not given in the abstract.
- Membership test: a fast check of whether a given set belongs to the family.
- Multiroot: the problem allows several root vertices instead of one.
- The ratio (1+ε)(√2+√α)² means the guarantee degrades slightly with a tunable parameter ε and with the local approximation factor α. · level: research-level

<details><summary>Original abstract</summary>

Many network design problems can be formulated as covering a family of vertex sets by edges. We develop a local-to-global approximation framework for disjointness-compliable families with polynomial-time membership tests. A class of vertices is deficient if it belongs to the family and feasible otherwise. Our local problem seeks a minimum-cost tree that connects one deficient class to feasible classes so that their union is feasible. If this local problem admits a polynomial-time $\alpha$-approximation, then the covering problem admits a polynomial-time $(1+\varepsilon)(\sqrt{2}+\sqrt{\alpha})^2$-approximation for every fixed $\varepsilon>0$. Our algorithm first connects deficient vertices that are difficult to separate and then handles regions containing one deficient class at a time. To bound the total local cost, we compare the local trees with a feasible forest. We delete edges of this forest after using them in the bound, so each is counted at most once even when regions overlap. As applications, we obtain polynomial-time $(8+\varepsilon)$-approximation algorithms for generalized point-to-point connection and multiroot quota tree, including multiroot $k$-minimum spanning tree. To the best of our knowledge, these are the first polynomial-time constant-factor approximations for both problems. We also obtain a randomized approximation for multiroot covering Steiner that has the same asymptotic ratio as the known approximation for its single-root version.

</details>

## Programming languages and formal methods

### [Landscape and Taxonomy of Prompt Engineering Patterns in Software Engineering](https://arxiv.org/abs/2611.29853)
*Yuya Sasaki, Hironori Washizaki, Jialong Li et al.* · `cs.SE` · arXiv:2611.29853v1 · relevance 0.13

- **In one sentence**: A systematic literature review, conducted in early 2023, that builds a taxonomy of prompt engineering patterns for software engineering tasks involving large language models.
- **In plain words**: Large language models are AI systems that respond to written instructions, called prompts. This paper looks at published research on the reusable ways people word those prompts to get better results for software development work. It sorts these techniques into a organized catalogue, or taxonomy, based on a literature review done in early 2023.
- **Why it matters**: The text argues that good prompt design still matters for usability and reliability, even as models improve. The text does not say how much the patterns help in practice, and because the review reflects early-2023 models, some findings may be dated.
- **Background needed**: - Large language model (LLM): an AI system trained on large amounts of text that generates responses to instructions.
- Prompt: the written instruction or input given to an LLM.
- Prompt pattern: a reusable template or strategy for structuring prompts.
- Software engineering: the work of designing, building, and maintaining software.
- Systematic literature review: a structured method for finding and summarizing existing published studies.
- Taxonomy: a classification scheme that groups items into categories.
- Context length: how much text a model can consider at once. · level: intermediate

<details><summary>Original abstract</summary>

Advancements in large language models (LLMs) have enhanced their ability to handle ambiguous user instructions. However, effective prompt patterns remain crucial for usability and comprehension. This article presents a taxonomy of prompt engineering patterns for software engineering. It is based on a systematic literature review that was conducted in early 2023, when LLMs still faced significant limitations in context length and inference capabilities. Our study explores techniques that enhance the usability and reliability of LLMs, emphasizing the ongoing importance of well-designed prompts in optimizing task performance. Our findings highlight the critical role of prompt patterns in maximizing LLM's potential, even as their capabilities continue to evolve.

</details>

### [Sheaf Semantics of Probabilistic Programs](https://arxiv.org/abs/2611.30692)
*Shing Hin Ho, Nicolas Wu, Azalea Raad* · `cs.LO` · arXiv:2611.30692v1 · relevance 0.13

- **In one sentence**: The paper gives a monadic denotational semantics, built on Simpson's probability sheaves and the internal logic of atomic sheaves, for higher-order probabilistic programs with continuous distributions, proves it models the ν-calculus, and derives a higher-order probabilistic Hoare logic that handles continuous random variables, higher-order functions, and independence.
- **In plain words**: Probabilistic programs are software that makes random choices, such as drawing numbers from a bell curve. This paper gives a rigorous mathematical meaning to such programs, including programs that pass functions around and sample from continuous ranges of values. It then uses that meaning to build a logical system for proving claims about the programs, such as what their outputs look like and whether outputs are independent of each other.
- **Why it matters**: Reasoning about randomness in programs is hard once values are continuous and functions are first-class, and the text claims this is the first Hoare-style logic that handles all of these together with rigorous treatment. Its relevance beyond this formal setting is not established by the text, which does not discuss applications.
- **Background needed**: - Denotational semantics: assigning each program a precise mathematical object representing what it computes.
- Hoare logic: a method of proving that a program satisfies a stated condition before and after it runs.
- Monads: a standard way in functional programming to structure computations that have side effects, here randomness.
- Measure theory: the branch of mathematics that makes probabilities over continuous values rigorous.
- Sheaves and toposes: structures from category theory that organise local information consistently; the "internal logic" is the logic a topos supports.
- Probabilistic independence: two random outputs do not influence each other's distribution. · level: research-level

<details><summary>Original abstract</summary>

Finding denotational models of probabilistic languages that support sampling from continuous distributions is difficult: the existence of continuous distributions means that measure-theoretic objects are needed to define the semantics. A challenging task on top of this is logical reasoning with respect to the semantic model: in the case of probabilistic programs, the desired properties to reason about include the distributions, expected value and the probabilistic (in)dependence of outputs. This paper introduces a monadic semantics for higher-order probabilistic programs with continuous distributions based on Simpson's theory of probability sheaves and the internal logic of atomic sheaves. We prove that our semantics forms a model of the $\nu$-calculus. Furthermore, using the well-behavedness of the semantic domain and the internal logic of the topos, we derive the first higher-order probabilistic Hoare logic with rigorous treatment of continuous random variables, higher-order functions, and independence.

</details>

## Systems and networking

### [Zarc: Exact Nearest Neighbors over a Billion Vectors in Seconds](https://arxiv.org/abs/2611.29252)
*Dongfang Zhao* · `cs.DC` · arXiv:2611.29252v1 · relevance 0.06

- **In one sentence**: Zarc is a GPU-plus-host-memory system that performs exact k-nearest-neighbor vector search over a billion vectors by keeping only compact half-precision lower-bound rows on the GPU and fetching the few surviving full vectors from host memory.
- **In plain words**: Computers often need to find the stored items most similar to a query, such as the closest matching pieces of text represented as lists of numbers. Doing this exactly over a billion items normally means scanning everything, which is slow. This paper describes Zarc, a system that skips most items using cheap rough checks and only looks at the few remaining candidates in full, reporting that it does this exactly and in seconds.
- **Why it matters**: Exact search speed matters for large language model attention and for data deduplication, where approximate results may miss true matches. The reported speedups come from the paper's own benchmarks on four H100 GPUs and eleven open LLMs, so they should be checked against the full evaluation before being relied on.
- **Background needed**: - k-nearest-neighbor search: finding the k stored vectors closest to a query vector.
- Vector: a list of numbers representing an item, such as a piece of text or an image.
- Exact vs. approximate search: exact search guarantees the true closest items; approximate methods may return near misses for speed.
- GPU and host memory: a GPU is a fast parallel chip with limited memory; host memory is the larger but slower main memory of the computer.
- Half precision (bf16): storing numbers with fewer bits to save memory and time, at some cost in accuracy.
- Lower-bound proof: a cheap calculation guaranteeing an item is too far away to be a top match, so it can be skipped.
- Attention and sparse attention: the mechanism in language models that weighs past tokens; sparse attention uses only a few selected keys. · level: research-level

<details><summary>Original abstract</summary>

Exact k-nearest-neighbor vector search lies on the critical path of machine learning systems, from sparse attention in the latest large language models (LLMs) to long-context memories and training-data deduplication. Exhaustive GPU search scans the whole dataset for every query, while approximate indexes return inexact neighbors. Recent methods skip almost every vector with a cheap half-precision proof that it lies too far away, but only on one GPU that holds the whole dataset. Our insight is to keep only the short rows of these proofs in GPU memory and to fetch the few remaining full vectors from host memory. Our system, Zarc, answers Euclidean, cosine, inner-product, and filtered queries exactly under updates. On four H100 GPUs, it answers 10,000 exact queries over one billion vectors in 1.1 seconds instead of five minutes. On eleven open LLMs, it retrieves the exact top-10 attention keys 2.2x to 13.1x faster than exhaustive search. In sparse attention over one million tokens, it runs 3.1x faster than bf16 selection with FlashInfer, which misses the exact top-64 for most queries.

</details>

### [Torcalia.jl: An MPI-based Runtime System for Asynchronous Task Parallelism in Julia](https://arxiv.org/abs/2611.30776)
*Argiris Sofotasios, Dimitris Metaxakis, Chrysostomos Stylios et al.* · `cs.DC` · arXiv:2611.30776v1 · relevance 0.06

- **In one sentence**: Torcalia.jl is a Julia package that runs dependency-aware asynchronous tasks across shared-memory threads and distributed nodes, built on MPI.jl, with work-sharing and work-stealing scheduling, nested tasks, application-level distributed shared memory, and skeleton abstractions, evaluated on the ARIS supercomputer against Dagger.
- **In plain words**: Scientific programs often split work into fixed chunks that run in lockstep, which wastes computer time when the work is uneven or changes as it runs. This paper presents Torcalia, a software library for the Julia programming language that instead breaks work into many small tasks and schedules them dynamically across the cores and machines of a supercomputer. On four test workloads run on the ARIS supercomputer, the authors report wall-clock time reductions of up to 18.1% compared with Dagger, another Julia task system.
- **Why it matters**: Getting large machines to stay busy on irregular workloads is a practical problem in high-performance computing, and Julia is increasingly used for it. The result is a comparison against one existing Julia tool on a single supercomputer with four workloads, so it is a measured improvement in a specific setting rather than a general claim about task-based computing.
- **Background needed**: - Parallel computing: running several pieces of work at once on multiple processors.
- Bulk-synchronous parallel (BSP): a style where all workers compute a step, then wait for each other before the next step.
- Asynchronous many-task (AMT) runtime: software that splits work into many small tasks and schedules them as resources free up.
- Work-stealing: idle workers take queued tasks from busy ones to balance load; work-sharing distributes tasks up front.
- MPI: the standard message-passing library that lets processes on different machines communicate.
- Distributed shared memory (DSM): presenting memory spread across several machines as if it were one shared pool.
- Multithreading: several threads inside one process sharing memory.
- Julia: a programming language aimed at fast scientific computing. · level: research-level

<details><summary>Original abstract</summary>

Designed to address the two-language problem, the Julia programming language provides a powerful platform for developing high-performance scientific computing and machine learning applications. Such applications increasingly exhibit irregular, adaptive, or data-driven workloads for which traditional bulk-synchronous parallel (BSP) models often struggle to efficiently exploit the available parallelism. Asynchronous many-task (AMT) runtime systems offer a compelling alternative, decomposing computations into fine-grained tasks that are dynamically scheduled across the hierarchical architecture of modern HPC systems. This paper introduces Torcalia$.$jl, a Julia package designed to orchestrate the asynchronous execution of tasks across both shared and distributed memory environments. Built on top of MPI$.$jl and Julia's native multithreading, Torcalia employs a dependency-aware task scheduling scheme that combines the work-sharing and work-stealing paradigms to achieve adaptive load balancing. Tasks can be nested arbitrarily, enabling applications to exploit multiple levels of parallelism, while application-level distributed shared memory (DSM) extends task-based shared-memory programming to multi-node clusters. Beyond task-based programming, the proposed library supports skeletal programming, providing high-level abstractions that facilitate the implementation of parallel applications at scale. Evaluated on the ARIS supercomputer using four diverse workloads, Torcalia demonstrates strong scalability, reducing wall-clock time by up to 18.1% compared with Dagger, a state-of-the-art task-based engine in Julia. The source code of Torcalia$.$jl is publicly available at https://github.com/CEID-HPCLAB/Torcalia.jl.

</details>

## Human-computer interaction

### [The Agent Is Not Your Driver: Clarifying the Implied Capabilities of In-Vehicle Anthropomorphic Agents](https://arxiv.org/abs/2611.28007)
*Benjamin Hardin* · `cs.HC` · arXiv:2611.28007v1 · relevance 0.11

- **In one sentence**: A position paper arguing that anthropomorphic in-vehicle agents can overstate their knowledge of the car's automated driving system, creating risks of user dependence and betrayal, and proposing a research agenda to study and narrow that gap safely.
- **In plain words**: The paper looks at talking, human-like assistants inside self-driving cars. The concern is that such an assistant may seem to be part of the car's driving system when it is not, so riders may trust it too much or feel misled when it gets something wrong. The authors do not report new experiments; they lay out the problem and propose questions and a research plan for future work.
- **Why it matters**: As cars add conversational assistants, what the assistant appears to know about driving could shape how much people rely on it, which bears on safety. The text does not give evidence of harm, so the concern is a proposed research direction rather than a established finding.
- **Background needed**: - Anthropomorphic agent: a voice or on-screen character designed to seem human-like, with a name, personality, or social cues.
- Automated driving system (ADS): the car's underlying software that actually steers, brakes, and monitors the road.
- Gap: the difference between what the friendly assistant can really do or know and what it appears to do or know.
- Dependence and betrayal: over-reliance on a trusted helper, and the sense of being let down when that trust proves unwarranted.
- Position paper: an argument and agenda for future work, not a report of new experimental results.
- Safety assurance: methods for showing a system is safe enough to use. · level: intermediate

<details><summary>Original abstract</summary>

This position paper considers how the gap between an anthropomorphic agent in an autonomous vehicle and the automated driving system of the vehicle can create psychological risks if the agent inaccurately presents itself as integrated into the driving system. This gap is under-explored both because of the evolving nature of these agents and because of study limitations in Human-Computer Interaction (HCI) research. Nevertheless, this gap may cause the agent to misrepresent itself as more knowledgeable about the car than it is, creating a risk of dependence and, in the worst case, betrayal if the occupant feels that the agent has misled them. This paper proposes a research agenda for future work to understand the psychological risk that exists in the gap between agents and driving systems and to narrow this gap in a manner aligned with safety assurance. As these agents evolve to hold greater capabilities and increased anthropomorphism, future research must investigate risks which may emerge from richer interaction with them. The impact of how an agent presents itself and its knowledge becomes greater.

</details>

### [Typing Behavior in Human-LLM Interaction: Keystroke Dynamics Reveal Cognitive Effort During Prompting](https://arxiv.org/abs/2606.28090)
*Laura Sch\"utz, Yousri Cherif, Clara Sayffaerth et al.* · `cs.HC` · arXiv:2606.28090v1 · relevance 0.11

- **In one sentence**: A 36-person user study finds that keystroke timing and volume track self-reported mental workload when people write prompts for an LLM, but do not predict how useful users rate the output.
- **In plain words**: When people type requests to an AI chatbot, how they type may reveal how hard they are thinking. The researchers had 36 participants write prompts for easy and hard tasks on desktop and mobile devices, then recorded their keystrokes and asked them to rate their workload. Harder tasks produced more typing, slower typing, and longer pauses, but the typing patterns did not tell whether people found the AI's answers useful.
- **Why it matters**: Typing signals could offer a cheap, real-time way to notice when a user is struggling during an AI interaction, without interrupting them with questionnaires. The text also shows a clear limit: typing reflected effort but not perceived success, so it is not a complete measure of how well the collaboration is going.
- **Background needed**: - LLM (large language model): an AI system that generates text in response to written prompts, such as chatbots.
- Keystroke dynamics: the measurable details of typing, such as how many keys are pressed, how fast, and how long the pauses between them are.
- NASA-TLX: a standard questionnaire that asks people to rate mental workload (effort, frustration, time pressure and similar factors).
- Human-computer interaction (HCI): the field that studies how people use and experience computers and software.
- The study is a small lab experiment (N = 36); the text does not describe the specific tasks, sample details, or statistical methods, so findings should be read as preliminary. · level: introductory

<details><summary>Original abstract</summary>

As Large Language Models (LLMs) become increasingly integrated into daily routines, understanding how users interact with these systems is crucial for effective human-AI collaboration. This work investigates keystroke dynamics as a behavioral measure of user mental effort and perceived output usefulness in human-LLM interaction. We conducted a user study (N = 36) to examine how task difficulty (easy vs. hard) and device type (desktop vs. mobile) influence typing behavior and workload (NASA-TLX) during interactions. Our results indicate that hard tasks led to significantly more keystrokes, slower typing, increased pauses, and higher self-reported workload. Device type had weaker effects, with mobile use slightly reducing input length and typing speed. While keystrokes captured differences in cognitive effort, they did not predict perceived LLM output usefulness. These findings highlight the potential of keystroke dynamics as real-time indicators of cognitive effort during LLM prompting, while also showing their limitations in capturing perceived collaboration success.

</details>

## Information theory

### [An Alphabet-Size Bound for the Information Bottleneck Function](https://arxiv.org/abs/2611.30697)
*Christoph Hirche, Andreas Winter* · `cs.IT` · arXiv:2611.30697v1 · relevance 0.09

- **In one sentence**: The paper proves that the information bottleneck function can be approximated, within a stated error, using a compressed variable W whose size is bounded in terms of the approximation error and the size of the label set Y rather than the size of X, and extends such cardinality bounds to settings with quantum variables.
- **In plain words**: The information bottleneck is a way of squeezing a large piece of data X into a smaller summary W while keeping as much information as possible about a related quantity Y, such as a label. Known results say the summary can be limited to at most |X|+1 possible values, which is unhelpful when X is huge, as in machine learning. The authors show that, up to a chosen small error, the summary can instead be limited to a number of values that depends only on the error and the number of labels.
- **Why it matters**: Many practical uses, such as machine learning and compression, involve very large inputs with small label sets, so a size limit tied to the labels could make calculations feasible. The text does not show how tight the new bounds are or report any experiments, so their practical impact is unclear from this summary alone.
- **Background needed**: - Random variable: a quantity whose value is uncertain, described by a probability distribution.
- Mutual information: a measure of how much knowing one variable tells you about another, in bits.
- Information bottleneck: finding a compressed representation W of X that keeps as much information about Y as possible, subject to a limit on how much it retains about X.
- Cardinality: the number of distinct values a variable can take.
- Approximation error (epsilon): the allowed gap between the approximate and exact answer.
- Quantum information: information carried by quantum systems, which behaves differently from classical probability; the paper treats this as a generalization. · level: research-level

<details><summary>Original abstract</summary>

The information bottleneck function gives a measure of optimal preservation of correlation between some random variable $X$ and some side information $Y$ while compressing $X$ into a new random variable $W$ with bounded remaining correlation to $X$. As such, the information bottleneck has found many natural applications in machine learning, coding and video compression. The main objective in order to calculate the information bottleneck is to find the optimal representation on $W$. This could in principle be arbitrarily complicated, but fortunately it is known that the cardinality of $W$ can be restricted as $|{\cal W}|\leq|{\cal X}|+1$ which makes the calculation possible for finite $|{\cal X}|$. Now, for many practical applications, e.g. in machine learning, $X$ represents a potentially very large data space, while $Y$ is from a comparably small set of labels. This raises the question whether the known cardinality bound can be improved in such situations. We show that the information bottleneck function can always be approximated up to an error $\delta(\epsilon,|{\cal Y}|)$ with a cardinality $|{\cal W}| \leq f(\epsilon,|{\cal Y}|)$, for explicitly given functions $\delta$ and $f$ of an approximation parameter $\epsilon>0$ and the cardinality of ${\cal Y}$. Finally, we generalize the known cardinality bounds to the case were some of the random variables represent quantum information.

</details>

### [Following the Error Through a Compressed Network:An Angular Measure for FFN Weight Compression in ViT-L/16](https://arxiv.org/abs/2611.28067)
*Paolo D'Alberto* · `cs.CV` · arXiv:2611.28067v1 · relevance 0.08

- **In one sentence**: The paper compares four ways of quantizing the feed-forward weight matrices of ViT-L/16 to 2–8 bits and proposes angular error measures, tracked through the residual stream and through a block's output spectrum, that rank the schemes as final classification does.
- **In plain words**: Large neural networks store their learned settings as many decimal numbers, and this paper studies how to round those numbers to a small number of bits so the model takes less storage. It tests four rounding schemes on one image-recognition model, checking both its final accuracy on 50,000 images and how far its internal signals drift from the original. The authors found that a rotation-based scheme keeps errors from building up as they pass through the layers, and they propose a way to judge schemes by looking at a single layer that matches the ranking of the full network.
- **Why it matters**: Knowing how rounding errors build up inside a network is useful for deciding how far a model can be compressed without losing its behaviour. The angle-based measure may be portable to other models and precisions, but the text only covers one model, weights in the feed-forward parts only, and simulated (float) evaluation with no speed gains, so its wider value is not yet shown.
- **Background needed**: - Quantization: replacing precise numbers with a small set of allowed values, measured in bits (2 bits gives 4 levels, 8 bits gives 256).
- Feed-forward network (FFN): the per-layer block of weight matrices in a transformer that follows attention.
- Vision Transformer (ViT-L/16): a large image-classification model made of stacked blocks; "48 FFN matrices" means one per FFN sublayer across its blocks.
- Residual stream: the running signal that each block adds to; the paper tracks how its direction (angle) departs from the original.
- Lloyd–Max table: a fixed set of optimal rounding levels for a bell-shaped (Gaussian) distribution.
- Hadamard rotation: a mixing transform that spreads out large values before rounding, which the paper pairs with random signs.
- Float32: the standard full-precision number format used as the reference. · level: research-level

<details><summary>Original abstract</summary>

We study the compression of the 48 feed-forward network (FFN) matrices of the Vision Transformer ViT-L/16 to 2--8 bits with four schemes: a per-token grid, a fixed Gaussian Lloyd--Max table, a table fitted to the matrix, and a random-sign Hadamard rotation followed by the fixed table. We evaluate on 50,000 images. At 4 bits the top-1 accuracy of the four schemes lies within 0.8 points of the float32 model, while the agreement with its predictions ranges from 98.4\% to 94.4\%. We use the angular error between the compressed and the float32 residual stream, followed through the blocks, as a portable measure that ranks the schemes as the final classification does and shows where the ranking is built: with rotation the angle grows close to the square root of the number of blocks, the signature of independently accumulating errors, while the other schemes are amplified in the later blocks. The same measure shows that a scheme that is better on one block in isolation can be worse in the whole network. To address this inconsistency we introduce an angular measure of the spectrum of the output of a block, which in isolation orders the schemes as the whole network does where they diverge most. We support these observations with real samples and with statistically generated ones. The scope is one model, the FFN weights only, and float evaluation of compressed weights; no speed-up is claimed. The error measures and the sample generation, however, can be applied to other models and precisions.

</details>

## High-energy theory and gravity

### [Scattering amplitudes in AdS$_5\times$ S$^5$ from the pure spinor superstring](https://arxiv.org/abs/2611.29622)
*Luis F. Alday, Thiago Fleury, Tobias Hansen et al.* · `hep-th` · arXiv:2611.29622v1 · relevance 0.16

- **In one sentence**: The paper gives a BRST-invariant rule for integrating over zero modes in the pure spinor superstring on AdS5×S5, valid for genus-zero amplitudes, and uses it to compute two- and three-point supergravity amplitudes directly on the worldsheet.
- **In plain words**: The paper tackles a technical obstacle in string theory: calculating how strings scatter in a curved background, AdS5×S5, which is the setting of a well-known duality with a gauge theory. The authors propose a consistent way to handle certain "zero modes" (directions in which the string's position does not change) so that the calculation can be carried out. Using this, they compute simple scattering quantities for supergravity particles directly from the string's worldsheet, and report that the properly normalised three-point results match those of planar N=4 super Yang-Mills theory.
- **Why it matters**: The text says this removes a central obstacle to amplitude computations in this background, which matters for testing the AdS/CFT correspondence from the string side. The text does not say how far the method extends beyond the low-point cases shown, so its wider impact is uncertain.
- **Background needed**: - Scattering amplitude: a quantity giving the probability-like weight for particles to interact in a given way.
- String worldsheet: the two-dimensional surface swept out by a string as it moves through spacetime.
- AdS5×S5: a curved spacetime (anti-de Sitter times a sphere) that is the background of the AdS/CFT duality.
- Pure spinor superstring: a formulation of superstring theory that keeps supersymmetry manifest.
- Zero modes: parts of the string's motion that do not change its shape, which must be integrated over with care.
- BRST invariance: a symmetry used to ensure that unphysical gauge-related degrees of freedom do not affect results.
- Genus zero: the simplest topology of the worldsheet (a sphere), corresponding to tree-level interactions.
- Half-BPS supergravity states: special, highly symmetric particle states that are protected from quantum corrections.
- N=4 super Yang-Mills: a supersymmetric gauge theory that is dual to string theory on AdS5×S5. · level: research-level

<details><summary>Original abstract</summary>

We formulate a BRST-invariant prescription for the integration of zero modes in the pure spinor superstring on $AdS_5\times S^5$. The measure includes contributions absent in flat space and admits a description in terms of picture changing operators or a non-minimal regulator. The prescription is valid for genus-zero amplitudes with arbitrary multiplicity and external states and removes a central obstacle to amplitude computations in this background. We use it to perform the first direct worldsheet computation of two and three-point amplitudes of half-BPS supergravity states. The properly normalised three-point amplitudes exactly reproduce the results of planar ${\mathcal N}=4$ super Yang-Mills theory.

</details>

### [Primordial black holes production in Einstein-Gauss-Bonnet gravity](https://arxiv.org/abs/2611.28150)
*Ekaterina O. Pozdeeva, Sergey Yu. Vernov* · `gr-qc` · arXiv:2611.28150v1 · relevance 0.15

- **In one sentence**: Proposes an inflation model in Einstein-Gauss-Bonnet gravity, with the Gauss-Bonnet term coupled to a scalar field, that the authors argue can produce primordial black holes and agree with ACT data for some parameter values.
- **In plain words**: This paper looks at the very early universe, when space expanded rapidly in a period called inflation. The authors modify the gravity equations with an extra term that depends on a scalar field, and they propose a version of this early expansion that could form primordial black holes. They report that, for certain parameter choices, the predictions match observations from the Atacama Cosmology Telescope, and they suggest these black holes could account for all or part of dark matter.
- **Why it matters**: If primordial black holes formed in the early universe, they could be a candidate for some or all of dark matter, which is a major open question. The link to ACT data gives the model a testable check, but the text gives few details, so the strength of the claim is unclear from the abstract alone.
- **Background needed**: - Inflation: a brief, rapid expansion of the universe just after the Big Bang, which is thought to seed later structure.
- Primordial black holes: black holes that could have formed in the early universe, not from collapsed stars.
- Gauss-Bonnet term: an extra term in the equations of gravity, beyond Einstein's standard version, that comes from higher-dimensional or quantum-motivated theories.
- Scalar field: a field that takes a single value at each point in space, often used to drive inflation.
- ACT (Atacama Cosmology Telescope): a telescope that measures the cosmic microwave background, the faint afterglow of the Big Bang, and constrains inflation models.
- Dark matter: unseen matter that makes up most of the matter in the universe and is inferred from its gravitational effects. · level: research-level

<details><summary>Original abstract</summary>

We consider models with the Gauss-Bonnet term multiplied to a function of the scalar field and propose a new inflationary model which provides a mechanism for the formation of primordial black holes (PBHs). For certain values of the model parameters, the predictions of this model agree with observational data from the Atacama Cosmology Telescope (ACT). Due to estimation of possiable PBHs masses, we demonstrate that they can be considered as a possible source for all or part of dark matter.

</details>

## Statistical physics

### [Statistical mechanics of linear classification on hierarchical tree data](https://arxiv.org/abs/2611.28824)
*Jerome Garnier-Brun, Federica Kulka, Carlo Lucibello* · `cond-mat.dis-nn` · arXiv:2611.28824v1 · relevance 0.15

- **In one sentence**: A replica-theory analysis of a linear classifier trained to recover the root of a tree-structured broadcast process from its leaves, showing a two-stage double descent with well-separated sample-size scales below the reconstruction threshold.
- **In plain words**: The paper studies a simple learning problem where a hidden root value spreads down a branching tree and the learner only sees the values at the leaves, then must guess the root. The authors find that the data is not well described by the usual Gaussian (bell-curve) assumptions along the label-carrying direction, so they keep that direction's exact statistics and approximate the rest as Gaussian. This gives a theory that matches measured learning curves and reveals a two-step pattern of error going down, then up, then down as more samples arrive.
- **Why it matters**: Many theoretical tools for learning from structured data assume Gaussian statistics, and this work shows a controlled case where that assumption breaks and a more careful theory still works. It may serve as a starting point for studying deeper networks and generative models on hierarchical data, though the text itself does not establish that connection.
- **Background needed**: - Broadcast process on a tree: a value at the root is randomly copied and noisily passed down branches, so leaves carry noisy information about the root.
- Reconstruction threshold: the noise level above which the root can no longer be inferred from the leaves at all.
- Linear classifier: a weighted sum of the inputs followed by a threshold, trained on labeled examples.
- Learning curve: how test error changes as the number of training samples grows.
- Double descent: test error first falls, rises to a peak (often near the point where samples match parameters), then falls again.
- Replica method: a statistical-physics technique for computing average-case error of learning rules in high dimensions.
- Gaussian equivalence: the assumption that complicated data can be replaced by Gaussian data with the same mean and covariance for analysis.
- Regularization: a penalty that discourages overly large weights. · level: research-level

<details><summary>Original abstract</summary>

Deep networks owe much of their success to their ability to exploit the structure in data, from the grammar of language to the multi-scale organization of images. Yet, many statistical mechanics approaches to structured data rely on Gaussian equivalence, whose assumptions can fail when a few latent variables influence all input coordinates. In this work, we take a step beyond this setting with a simple setup, in which a linear classifier is trained to infer the root of the classical broadcast process on a tree from its $N$ leaves. Despite this simplicity, the data already display non-Gaussian statistics along the direction carrying the label, as well as strong finite-size effects. By retaining the exact law along this direction and approximating the transverse fluctuations as Gaussian, we obtain a finite-depth replica theory that accurately describes the measured learning curves. At large depth and sufficiently weak regularization, we uncover a double descent whose two stages are separated in scale. In a range of broadcast noise below the reconstruction threshold, the first descent occurs at a number of samples scaling as $N^\omega$, with $0<\omega<1$ set by the data statistics, whereas the overfitting peak occurs at order $N$ samples. Beyond linear classifiers, this setup could serve as a controlled starting point to study deeper architectures and generative models on hierarchical data.

</details>

### [A Novel Algebraic Approach to Medium-Range Solvable Models](https://arxiv.org/abs/2611.29351)
*Yuan Miao, Kohei Fukai* · `math-ph` · arXiv:2611.29351v1 · relevance 0.13

- **In one sentence**: The paper extends Jones' algebraic Baxterisation to quantum spin chains with medium-range interactions, using an extended Yang-Baxter equation solved by the chromatic algebra of 3-colouring, yielding four representations that reproduce the folded XXZ and hard-rod deformed XXZ models and give new medium-range models.
- **In plain words**: The paper studies chains of interacting quantum spins, the simplified models physicists use to understand magnets and similar materials. Most solvable models only let each spin interact with its immediate neighbours, and this work builds solvable models where interactions reach further along the chain. The authors use an algebraic recipe, starting from the rules of a specific mathematical structure (the chromatic algebra of 3-colouring), to produce four such models, two of which reproduce known models and two of which are new.
- **Why it matters**: Exactly solvable models give rare exact answers about how many-body quantum systems behave, so a systematic way to generate new ones is useful to the field. The paper also reports that two of the four models have non-invertible symmetries, a less common kind of symmetry; the text does not show what physical consequences follow from this.
- **Background needed**: - Quantum spin chain: a line of quantum spins (tiny magnetic moments) where each interacts with nearby ones; a simple model of magnetism.
- Yang-Baxter equation: an algebraic consistency condition that makes a model exactly solvable, i.e. its behaviour can be worked out exactly.
- R matrix and Lax operator: the building blocks used to construct transfer matrices, which generate conserved quantities of the model.
- Medium-range interaction: spins interact with others beyond their immediate neighbours.
- XXZ model: a standard solvable spin-chain model; folded XXZ and hard-rod deformed XXZ are variants of it.
- Chromatic algebra / Rep(S_3): mathematical structures tied to counting colourings of graphs and to the symmetry group of three objects; the link to the physics is only sketched in the text.
- Non-invertible symmetry: a generalised symmetry whose operations cannot be undone, as the fusion-category framework describes. · level: research-level

<details><summary>Original abstract</summary>

We extend Jones' Baxterisation, which produces solutions to the Yang-Baxter equation directly from the generators of an algebra, to quantum spin chains with medium-range interactions. The key ingredient is an extended Yang-Baxter equation for R matrices that are built from the generators attached to two neighbouring sites. Together with the accompanying Lax operator, it gives rise to transfer matrices that are in involution up to boundary terms, exactly as in Jones' construction. We find a solution to the extended Yang-Baxter equation, of non-difference form, in terms of the generators of the chromatic algebra of 3-colouring, and obtain from it two families of medium-range lattice Hamiltonians. Thus, each representation of the algebra provides a medium-range solvable model. Using the relation between the chromatic algebra of 3-colouring and the fusion category $\mathrm{Rep}(S_3)$, we construct four such representations. They reproduce the folded XXZ model and the hard-rod deformed XXZ model, and give new medium-range models of a three-state antiferromagnet and of a Rydberg-blockade ladder. Two of the four models possess non-invertible symmetries.

</details>

## Condensed matter

### [Anomalous Field-induced Coherence beyond Single-ion Kondo Physics](https://arxiv.org/abs/2611.31137)
*Arushi, Konstantin Semeniuk, Manuel Brando et al.* · `cond-mat.str-el` · arXiv:2611.31137v1 · relevance 0.14

- **In one sentence**: In the heavy fermion compound Ce2Rh3Ga5, a magnetic field suppresses the residual resistivity and restores T^2 coherent metallic transport that is absent at zero field, a behavior the authors argue cannot be explained by single-ion Kondo physics alone and which resembles the anomalous magnetotransport of UBe13.</one_liner>
<parameter name="plain">Some metals conduct electricity poorly even at very low temperature, and the reason is not well understood. This paper studies one such metal, Ce2Rh3Ga5, and finds that applying a magnetic field lowers its electrical resistance a lot and makes it behave like a well-ordered metal again. The authors report that the field's effect on heat storage can be described with a standard model, but its effect on resistance cannot.
- **Why it matters**: The result points to an extra source of electron scattering beyond the usual textbook picture for these materials, which matters for understanding why some strongly correlated metals behave oddly. The comparison with UBe13, a long-studied material, suggests the mechanism may be shared, though the text itself does not establish the microscopic cause.
- **Background needed**: - Heavy fermion metals: materials containing rare-earth atoms (here cerium) whose electrons behave as if they have very large effective mass.
- Kondo effect: local magnetic atoms get screened by conduction electrons, which can form heavy quasiparticles at low temperature.
- Coherence: when scattering weakens at low temperature, electrical resistivity drops and follows a simple T^2 law.
- Specific heat coefficient C/T: a measure of how strongly electrons store heat; large values signal heavy electrons.
- Magnetoresistance: change in electrical resistance caused by a magnetic field; negative means resistance falls as field rises.
- Residual resistivity: the resistance remaining as temperature approaches zero, set by impurities and other defects.
- UBe13: a uranium heavy fermion compound known for unusual transport and superconductivity. · level: research-level

<details><summary>Original abstract</summary>

The emergence of coherent heavy quasiparticles in Kondo lattices is generally accompanied by a reduction in electrical resistivity at low temperatures. However, certain strongly correlated metals exhibit anomalously large resistivities that persist to very low temperatures, raising fundamental questions about the mechanisms governing charge transport. Here, we report an unusual magnetic field-induced evolution of electronic transport and thermodynamic properties in a Ce-based heavy fermion compound, Ce$_{2}$Rh$_{3}$Ga$_{5}$. At zero field, Ce$_{2}$Rh$_{3}$Ga$_{5}$ undergoes a magnetic transition at $T$$_{0}$ = 0.45 K and exhibits a strongly enhanced low temperature specific heat coefficient, reaching $C$/$T$ = 2.2 J/mol$_{Ce}$-K$^{2}$, but no discernible coherence in its electrical resistivity. Remarkably, applying a magnetic field produces a large negative magnetoresistance and restores coherent metallic behavior, characterized by low-temperature $T$$^2$ resistivity. Although the field dependence of the electronic specific heat coefficient can be described phenomenologically within a single-ion Kondo framework, the same description fails to account for the strong suppression of the residual resistivity and the overall magnetoresistance. These results point to an additional field-sensitive scattering contribution beyond conventional single-ion Kondo physics. The striking resemblance to the long-standing anomalous magnetotransport behavior of UBe$_{13}$, without the complications introduced by superconductivity, establishes Ce$_{2}$Rh$_{3}$Ga$_{5}$ as a platform for investigating the microscopic origin of anomalous scattering and field-induced coherent transport in strongly correlated electron systems.

</details>

### [Perfect Spin-to-Charge Signal Conversion via Inverse Spin Hall Effect in a Superconductor](https://arxiv.org/abs/2611.30781)
*Rodrigo de las Heras, Ilya V. Tokatly, F. Sebastian Bergeret* · `cond-mat.supr-con` · arXiv:2611.30781v1 · relevance 0.13

- **In one sentence**: A theoretical proposal that, in a superconductor below its gap, the inverse spin Hall effect could convert injected spin accumulation into a charge voltage with near-unity efficiency despite a small spin Hall angle, testable via temperature- and spin-bias-dependent nonlocal measurements.
- **In plain words**: Spintronics uses the spin of electrons, a tiny magnetic property, to carry information, and it usually needs to turn that spin into an electrical voltage. Normally this conversion is weak. This paper proposes that a superconductor, a material that carries current with no resistance, can make the conversion far more efficient, because below its energy gap very few unpaired electrons can carry current, so the spin-driven charge imbalance shows up as a comparable voltage.
- **Why it matters**: If the effect holds, it could offer a much stronger electrical readout of spin signals than conventional heavy-metal spin Hall detectors. The text is a theory paper with predictions only; it does not report experiments, so the claim of near-unity conversion depends on the model and its assumptions.
- **Background needed**: - Spin: a quantum property of electrons that acts like a tiny magnet; spintronics uses it alongside or instead of charge.
- Spin Hall effect: a spin current flowing through a material deflects sideways and produces a transverse charge voltage. The inverse effect goes the other way, turning spin into charge.
- Spin Hall angle: a number measuring how efficiently a material makes this conversion; typical values are small.
- Nonlocal spin valve: a device where spin is injected at one point and detected at a separate point, so the signal is not mixed with ordinary charge current.
- Superconductor and energy gap: below a critical temperature, electrons pair up and there is an energy gap; quasiparticles (unpaired excitations) are suppressed below the gap.
- Charge imbalance: a mismatch between electron-like and hole-like excitations in a superconductor, which can produce a voltage.
- Spectral broadening: a finite smearing of the energy levels, a realistic correction to the idealized model. · level: research-level

<details><summary>Original abstract</summary>

Spin-to-charge conversion is central to spintronics, but conventional spin Hall mechanisms are intrinsically limited by the small spin Hall angle. Here we show that superconductivity can overcome this limitation and enable near-unity spin-to-charge signal conversion. We consider a nonlocal spin-valve geometry in which a spin accumulation is injected into a superconductor and converted into a transverse charge signal through the inverse spin Hall effect. In the superconducting state, the strongly suppressed quasiparticle conductance below the gap allows the resulting charge imbalance to generate a voltage comparable to the injected spin bias, despite a small spin Hall angle. We derive the full nonequilibrium response including finite spectral broadening and finite temperature, and propose temperature and spin-bias-dependent measurements of the detector voltage to test our predictions.

</details>

## Particle physics

### [Superheavy gravitational dark matter from runaway bubble collisions](https://arxiv.org/abs/2611.30113)
*Cheng-Wei Chiang, Van Que Tran* · `hep-ph` · arXiv:2611.30113v1 · relevance 0.16

- **In one sentence**: The paper proposes that a very heavy, stable particle coupling only gravitationally could be pair-produced by graviton exchange in collisions of runaway bubble walls during a first-order vacuum transition, yielding a flat production rate up to masses near (H/β)M_P/ν² and dark matter up to about 10^17 GeV.
- **In plain words**: The paper asks how a dark matter particle could be made in the early universe if it interacts with ordinary matter only through gravity. It proposes that particles can be created when the walls of expanding bubbles of a new vacuum state collide at high speed, with gravity acting as the link. The text reports a yield formula for Dirac fermions and says gravity alone could account for dark matter up to very large masses, in cases where the usual freeze-in mechanism would not work.
- **Why it matters**: It offers a production route for extremely heavy dark matter that depends only on gravity, which is relevant because such particles would be hard to detect directly. The connection to specific observations is not addressed in the text, so its relevance beyond this scenario is uncertain.
- **Background needed**: - Dark matter: unseen matter that makes up most of the matter in the universe, inferred from its gravitational effects.
- Gravitational coupling: the particle interacts with other things only through gravity, not through the electromagnetic or other forces.
- Pair production: creating a particle and its antiparticle from energy in a collision.
- Graviton: the hypothetical quantum carrier of gravity, analogous to a photon for electromagnetism.
- Vacuum bubble walls: in some models the universe's vacuum can decay, forming expanding bubbles whose boundaries (walls) can collide and release energy.
- Runaway walls: bubble walls that keep accelerating rather than settling to a steady speed.
- Freeze-in: a production mechanism where a dark matter particle is slowly created by collisions of other particles in the hot early universe; it fails for very heavy particles at low reheating temperatures.
- Reheating temperature: the temperature the universe reached after inflation ended and its energy was converted into hot particles.
- Hubble rate: the rate at which the universe is expanding; H/β compares it to the speed of the wall transition.
- Reduced Planck mass: the natural mass scale of gravity, about 2.4×10^18 GeV. · level: research-level

<details><summary>Original abstract</summary>

A stable particle that couples only through gravity is pair-produced in collisions of runaway bubble walls by graviton exchange. For a transition of duration $1/\beta$, a Dirac fermion reaches the yield $Y_X\simeq6.8\times10^{-3}(H/\beta)(T_{\rm reh}/M_{\rm P})^3$, where $H$ is the Hubble rate of the vacuum energy, $T_{\rm reh}$ the reheating temperature and $M_{\rm P}$ the reduced Planck mass. The yield is flat up to masses near $(H/\beta)M_{\rm P}/\nu^2$, where $\nu$ of order one sets the wall-field excursion. Gravity alone then gives dark matter up to about $10^{17}$~GeV at reheating temperatures far below its mass, where freeze-in fails.

</details>

### [WIMPs as FIMPs: the Inert Doublet Model and low-temperature reheating](https://arxiv.org/abs/2611.28217)
*Genevi\`eve B\'elanger, Nicol\'as Bernal, Andreas Goudelis et al.* · `hep-ph` · arXiv:2611.28217v1 · relevance 0.16

- **In one sentence**: The paper revisits the Inert Doublet Model and shows that, with low reheating temperatures, a WIMP dark matter candidate can reach its observed relic abundance via freeze-in instead of the usual freeze-out, including finite-duration reheating and annihilation backreaction effects.
- **In plain words**: The paper asks how dark matter, the invisible material that makes up most of the universe's matter, gets its present-day amount. The usual textbook story assumes the particles were once in thermal balance with everything else and then "froze out" as the universe cooled. The authors show that if the universe was reheated to only a fairly low temperature after inflation, a heavy particle of this type may never reach that balance and can instead build up slowly, a process called freeze-in.
- **Why it matters**: Most searches for WIMP dark matter assume freeze-out, so a viable WIMP model that is ruled out under that assumption may survive under a different early-universe history. The text does not claim any experimental test or detection; its link to observations is only through the idea that the relic abundance constraint can be relaxed.
- **Background needed**: - Dark matter: unseen matter inferred from gravity; its total amount is measured.
- WIMP (weakly interacting massive particle): a heavy dark matter candidate that interacts through weak-force-like couplings.
- Freeze-out: particles are in thermal equilibrium early on, then annihilation stops as the universe expands and cools, leaving a fixed leftover amount.
- Freeze-in: particles are produced very weakly and slowly, never reaching equilibrium; the leftover builds up over time. FIMPs are the feebly interacting analogue.
- Reheating: the period after inflation when the universe's hot plasma of particles is re-established; its final temperature is the reheating temperature.
- Inert Doublet Model: an extension of the Standard Model with an extra Higgs-like doublet whose lightest neutral component can be dark matter.
- Relic abundance: the density of dark matter left over today. · level: research-level

<details><summary>Original abstract</summary>

Weakly Interacting Massive Particles (WIMPs) are conventionally assumed to acquire their dark matter relic abundance through thermal freeze-out. However, this association relies on assumptions concerning the thermal history of the early Universe. We revisit the Inert Doublet Model (IDM), a representative WIMP framework in which dark matter interacts with the Standard Model through electroweak gauge interactions, even when its Higgs-portal coupling vanishes. We demonstrate that sufficiently low reheating temperatures can prevent chemical equilibrium, allowing a genuine WIMP to acquire its relic abundance through freeze-in rather than freeze-out. Considering both instantaneous and finite-duration reheating, we identify different production histories, including freeze-out during radiation domination, freeze-out during reheating, and freeze-in with potentially significant annihilation backreactions. These scenarios open regions of the IDM parameter space that would otherwise be excluded by dark matter overabundance. Our results demonstrate that WIMPs can behave as FIMPs, depending on the thermal history of the Universe.

</details>

## Nuclear physics

### [Effect of dark matter and scalar-cut potential on the macroscopic properties of neutron stars: A chiral quark mean field approach](https://arxiv.org/abs/2611.30434)
*Hrishika P, Arvind Kumar* · `hep-ph` · arXiv:2611.30434v1 · relevance 0.13

- **In one sentence**: A chiral SU(3) quark mean-field study of neutron stars that adds fermionic dark matter (two-fluid TOV) and a scalar-cut potential, examining how these change the equation of state, mass-radius relation, tidal deformability and gravitational redshift.
- **In plain words**: This paper asks how a hypothetical invisible component, dark matter, might change the inside of a neutron star, the extremely dense collapsed remnant of a massive star. The authors build a computer model of the star's ordinary matter and a separate dark matter fluid that interacts with it only through gravity. They report that adding a particular potential stiffens the matter's pressure response, while more dark matter generally softens it and alters the star's size, mass and related observable properties.
- **Why it matters**: Neutron star mass, size and how easily they are tidally squeezed are measurable, so models like this can in principle be checked against observations, which is why dark matter inside stars is studied. The text does not show how strongly these effects compare with current observational limits, so their real-world significance remains uncertain.
- **Background needed**: - Neutron star: a city-sized, extremely dense star left after a massive star's core collapses.
- Equation of state (EOS): the rule linking pressure to density in a material; a "stiffer" EOS resists compression more and supports more mass.
- Mass-radius relation: how a star's radius changes with its mass; it is a key test against observations.
- Tidal deformability: how much a star is stretched out of shape by a companion's gravity, which affects gravitational-wave signals from merging stars.
- Gravitational redshift: the shift of light to longer wavelengths as it escapes a strong gravitational field.
- Chiral quark mean-field model: a theoretical framework describing nuclear matter in terms of quarks bound in particles and exchanged force-carrying fields.
- Two-fluid TOV: the standard stellar-structure equations extended to two fluids that share only gravity.
- Dark matter halo vs. core: dark matter may sit in a dense central core or in a diffuse outer cloud, depending on its mass and interactions. · level: research-level

<details><summary>Original abstract</summary>

We investigate the effects of fermionic dark matter (DM) and scalar-cut potential ($U_{\text{cut}}(\phi)$) on the equation of state (EOS) and macroscopic properties of neutron stars. The baryonic matter consists of neutrons, protons, electrons, and muons under the $\beta$-equilibrium and is described within the chiral SU(3) quark mean-field (CQMF) model. In this framework, quarks are confined within baryons, whose properties are modified through the exchange of scalar fields $\sigma$, $\zeta$, and $\delta$, and vector fields $\omega$ and $\rho$. The DM is modelled as a self-interacting fermionic fluid with scalar $\varphi_D$ and vector $V_D^\mu$ mediators. The baryonic and DM fluids interact only through gravity and are treated within a two-fluid Tolman-Oppenheimer-Volkoff formalism. We examine the resulting mass-radius relation and tidal deformability, along with the gravitational redshift, to investigate the effects of DM on neutron star structure and observable properties. The inclusion of $U_{\text{cut}}(\phi)$ stiffens the EOS, whereas increasing the DM fraction generally softens the EOS and modifies the mass-radius relation, tidal deformability, and gravitational redshift. The magnitude and nature of these modifications depend on the DM particle mass and mediator interactions, which determine whether the resulting configurations exhibit compact DM cores or extended DM halos.

</details>

### [Bypassing the Nanoampere Limit: A Thick-Target Methodology for Ultra-Low-Energy Resonances in the $^{11}$B(p,$\alpha$)2$\alpha$ Reaction](https://arxiv.org/abs/2611.30439)
*Xu-Yang Luo, Wen-Qing Wei, Shi-zheng Zhang et al.* · `nucl-ex` · arXiv:2611.30439v1 · relevance 0.09

- **In one sentence**: The paper introduces a thick-target method, using beam currents of 20–60 µA with Monte Carlo yield calculations, to measure the very small cross section of the 11B(p,α)2α reaction and search for low-energy resonances below 100 keV.
- **In plain words**: Scientists want to know how often protons and boron-11 nuclei react at very low energies, because this reaction matters for stars and for possible clean fusion power. The reaction is so unlikely at these energies that older experiments could only use very weak proton beams, which gave too few events to measure well. This paper describes a way to use beams about a thousand times stronger, with computer simulations to convert the counts into an absolute reaction yield.
- **Why it matters**: Better measurements of this reaction at low energy would help nuclear astrophysics and fusion research, which depend on how often it occurs. The authors say the method may be a practical tool for searching for unknown resonances, though the text reports only preliminary checks at 75 and 100 keV, so its wider usefulness is not yet shown.
- **Background needed**: - Cross section: a measure of how likely a nuclear reaction is for a given collision energy; tiny values mean rare events.
- Resonance: an energy at which a reaction is strongly enhanced, like a pitch at which a system responds most strongly.
- Center-of-mass (c.m.) energy: the collision energy measured in the frame moving with the two colliding particles.
- Thin vs. thick target: a thin target lets the beam pass through with little slowing, while a thick target slows the beam inside the material, so the reaction happens across a range of energies.
- Beam current (nanoampere, microampere): the flow of charged particles; a microampere is a thousand times larger than a nanoampere.
- Monte Carlo simulation: random-sampling computer modeling used here to predict the reaction yield from the full kinematics.
- Astrophysical and fusion relevance: p-11B fusion produces helium nuclei without neutrons, which is why it is studied for energy and why stellar reaction rates are of interest. · level: research-level

<details><summary>Original abstract</summary>

Precise measurements of the low-energy cross section for the $^{11}$B(p,$\alpha$)2$\alpha$ reaction is critical for nuclear astrophysics and fusion energy research, yet such measurements are experimentally demanding due to the reaction's extremely small cross section. Conventional thin-target experiments are fundamentally limited to nanoampere beam currents, which restrict count rates to impractical levels at ultra-low proton energies. To overcome this limitation, we report a correction-free thick-target methodology capable of operating at beam currents of 20-60 microamperes, corresponding to a gain of over three orders of magnitude. Monte Carlo simulations of the full reaction kinematics are employed to determine the absolute reaction yield, eliminating the requirement for empirical normalization factors. At the well-known 148~keV (c.m.) resonance peak, our extracted resonance energy ($E_{\mathrm{r}} = 148.0$~keV) and level width ($\Gamma_{\mathrm{cm}} = 5.3$~keV) are demonstrated in good agreement with published data. A scheme via comparing the measured reaction probability with a theoretical extrapolation result is furtherly presented to probe low-energy resonances below 100~keV region. Preliminary measurements at proton energies of 75~keV and 100~keV reveal no evidence for additional low-energy resonances. This work provides a robust new methodology to measure cross section and resonance parameters for the p$^{11}$B reaction and offers a highly efficient tool for systematic resonance searches in the ultra-low-energy regime.

</details>

## Quantum information and computing

### [Quantum simulation of low-temperature impurity models](https://arxiv.org/abs/2611.30187)
*Jiaqing Jiang, Nathan Ju* · `quant-ph` · arXiv:2611.30187v1 · relevance 0.16

- **In one sentence**: The paper gives quantum algorithms for preparing thermal and ground states of fermionic quantum impurity models, using global jump operators in quantum Gibbs samplers to avoid exponential-in-inverse-temperature overhead.
- **In plain words**: The paper looks at a standard model in materials physics: a small, strongly interacting piece of a system attached to a large, simpler surrounding bath. It describes quantum computer procedures for preparing this system's state at a chosen low temperature, and for estimating its properties, with the running time growing polynomially in system size and inverse temperature.
- **Why it matters**: Impurity models are the core computation inside dynamical mean field theory, a common tool for simulating strongly correlated materials, so faster low-temperature methods could matter there. The text does not show any hardware demonstration, so practical impact is unclear.
- **Background needed**: - Quantum impurity model: a small strongly interacting subsystem coupled to a large non-interacting bath.
- Dynamical mean field theory: a method for approximating strongly correlated materials by solving impurity models.
- Thermal state at inverse temperature β: the quantum state of a system in equilibrium; larger β means colder.
- Fermionic modes: the basic units of storage for fermions (particles such as electrons) in a quantum computer.
- Quantum Gibbs sampler: a quantum analogue of Markov chain Monte Carlo, a method for sampling from a target distribution by a random walk.
- Spectral gap: the energy difference between the ground state and the first excited state; a larger gap makes the ground state easier to prepare.
- Purification: an enlarged quantum state whose reduced state is the thermal state, allowing properties to be estimated.
- Heisenberg scaling: error decreasing as 1/δ in runtime, a quadratic improvement over the usual 1/δ² scaling. · level: research-level

<details><summary>Original abstract</summary>

Quantum impurity models, which describe a small but strongly-interacting subsystem coupled to a large noninteracting bath, are the computational core of dynamical mean field theory and play an important role in simulating strongly correlated materials. We develop quantum algorithms for efficiently simulating these models at low temperatures and with high precision. For any impurity model on $n$ fermionic modes with fixed impurity size: (1) We give a quantum algorithm that prepares the thermal state at inverse temperature $\beta$ to precision $\delta$ in time $\mathrm{poly}(n,\beta,\log(1/\delta))$. This algorithm is the first to achieve both polynomial scaling in the inverse temperature and polylogarithmic scaling in the precision. When the Hamiltonian has an inverse-polynomial spectral gap, our quantum algorithm prepares its ground state to precision $\delta$ in time $\mathrm{poly}(n,\log(1/\delta))$. (2) We further give a quantum algorithm that prepares a purification of the thermal state in time $\mathrm{poly}(n,\beta,\log(1/\delta))$. Using this purification, we estimate static and dynamical properties with error $\delta$ in time polynomial in $n$ and $\beta$ and linear in $1/\delta$ up to polylogarithmic factors, achieving the Heisenberg scaling. Our algorithms build on quantum Gibbs samplers, which are quantum analogues of Markov chain Monte Carlo methods. By using global jump operators instead of local ones, we avoid the $\exp(\beta)$ overhead commonly associated with quantum Gibbs samplers, making them efficient for impurity models even at low temperatures.

</details>

### [Incompressible quantum information](https://arxiv.org/abs/2611.28361)
*Lasse H. Wolff, Matthias Christandl, Bergfinnur Durhuus et al.* · `quant-ph` · arXiv:2611.28361v1 · relevance 0.14

- **In one sentence**: The paper shows that, unlike the classical case, a small classical system correlated with a large quantum system cannot always be matched by compressing the quantum system without losing a significant amount of mutual information.
- **In plain words**: The paper asks whether a large data set can always be shrunk while keeping the links between it and a small summary of it. For classical data the answer is yes, but the authors show that for some quantum systems it is not: any sizeable compression destroys a significant share of the correlation. The result is stated in terms of mutual information, a standard measure of how much two systems tell you about each other.
- **Why it matters**: The result points to a limit on information-bottleneck methods used in quantum machine learning: a small summary of the relevant features does not guarantee a compact encoding of the quantum data that keeps those features. The text itself does not discuss practical consequences beyond this, so the wider impact is unclear from the abstract alone.
- **Background needed**: - Mutual information: a measure of how much knowing one system reduces uncertainty about another.
- Correlation between two systems: how strongly their states are linked.
- Compression (in this context): replacing a large system with a smaller one that still preserves its relevant links to a third system.
- Information bottleneck: a machine learning method that seeks a compact representation keeping only information relevant to a target.
- Quantum versus classical: quantum systems can be entangled and cannot always be described by classical probabilities, which is why classical compression results may fail.
- Bipartite state: a joint quantum state of two subsystems. · level: research-level

<details><summary>Original abstract</summary>

For a small classical system correlated with a large one, it is always possible to compress the large system down to a size only dependent on the size of the smaller one, while preserving all correlations up to a given controllable error. Here, we show that such a statement does not hold at all when the large system is quantum mechanical. More precisely, we show that there are bipartite states such that any compression of the large system, by a non-trivial relative factor, will necessarily lead to the destruction of a significant amount of correlation, measured in mutual information. Our results therefore identify a limitation of information-bottleneck approaches to quantum machine learning, showing that a small system specifying the relevant features contained in a large quantum data set does not guarantee a compact encoding of the latter that preserves the relevant correlations.

</details>

## Optics and atomic physics

### [Reconfigurable Microwave Photonic All-Pass Filters based on Optical Kerr Microcombs](https://arxiv.org/abs/2611.29115)
*David J. Moss* · `physics.optics` · arXiv:2611.29115v1 · relevance 0.08

- **In one sentence**: The paper demonstrates microwave photonic all-pass filters (1st and 2nd order) built from an optical Kerr microcomb driven transversal filter, with reconfiguration done by changing tap coefficients in software rather than hardware.
- **In plain words**: The paper is about filters that change the timing (phase) of radio-frequency signals without making them louder or quieter. The authors build such filters using light from a special optical comb, and they report measured results for first- and second-order versions. They also show the filter's behavior can be adjusted by changing settings in software, without rebuilding the hardware.
- **Why it matters**: Phase control of high-bandwidth microwave signals matters for radar and communications signal processing, so a reconfigurable way to build these filters could be useful. The text reports measured figures, but it does not compare them with other systems, so its standing relative to existing approaches cannot be judged from this text alone.
- **Background needed**: - All-pass filter: a filter that leaves signal strength unchanged and only shifts its phase (timing of the wave).
- Group delay: how much a signal's envelope is delayed by the filter; larger values mean stronger timing shifts.
- Microwave photonics: processing radio-frequency signals using light, then converting back to electronics.
- Optical Kerr microcomb: a set of evenly spaced optical frequencies (colors) generated in a micro-resonator through a nonlinear optical effect.
- Transversal filter: a filter that sums delayed, weighted copies of a signal; the weights are the "tap coefficients."
- Order of a filter: roughly how many independent phase-shifting stages it has; higher order gives more phase shift.
- Reported metrics: maximum amplitude variation (MAV, ripple in signal strength in dB) and maximum group delay (MGD, in picoseconds). · level: research-level

<details><summary>Original abstract</summary>

Microwave photonic (MWP) all pass filters (APFs), which enable phase manipulation without altering signal amplitudes, are essential for phase engineering in high bandwidth microwave signal processing. However, achieving a high degree of reconfigurability in the filter order and characteristic parameters of APFs remains challenging for conventional methods. Here, we propose and experimentally demonstrate a new strategy for realizing MWP APFs based on a microcomb driven transversal filter system, enabling high reconfigurability, sharp phase transitions with high group delays, and low loss. We experimentally demonstrate both 1st and 2nd order APFs, achieving a maximum amplitude variation (MAV) of 1.95 dB and a maximum group delay (MGD) of 580 ps for the former, and a MAV of 2.01 dB and an MGD of 1740 ps for the latter. In addition, both independent and joint tuning of APF characteristic parameters are demonstrated by simply programming the tap coefficients without changing any hardware, enabling highly reconfigurable filter response for diverse phase engineering functionalities. These results highlight the potential of our approach for implementing MWP APFs with both high performance and reconfigurability for practical applications requiring dynamic and versatile phase control.

</details>

### [Anisoplanatic Blind Deconvolution using Phase Diversity](https://arxiv.org/abs/2611.28458)
*Shubhankar Jape, Seungman Choi, Peter Menart et al.* · `physics.optics` · arXiv:2611.28458v1 · relevance 0.07

- **In one sentence**: A simulation study proposing coded anisoplanatic blind deconvolution (CA-BD), which uses a pupil-plane spatial light modulator to apply known phase codes across short measurement bursts to jointly recover a scene and spatially varying atmospheric phase, compared against tuned multiframe blind deconvolution.
- **In plain words**: Air turbulence bends light from distant objects, so images of stars or ground targets come out blurry, and the blur differs from one part of the view to another and changes over time. This paper proposes a way to undo that blur during fast imaging by placing a programmable light-modifying device in the optical path that applies a known pattern to each frame. In simulations, the method estimated the phase distortion more accurately than a tuned existing approach, with the authors reporting about 3.5 times lower phase error for steady turbulence and 2 to 3 times lower for changing turbulence.
- **Why it matters**: Turbulence blur limits telescopes and long-range cameras, and the paper targets the case where a wide field and fast imaging make standard computational deblurring fall short. The results are from simulation only, and the text notes the benefit depends on faster modulators, so practical impact is uncertain until hardware tests are reported.
- **Background needed**: - Atmospheric turbulence: random variations in air density that distort light wavefronts, blurring images.
- Isoplanatic angle: the angular range over which the distortion can be treated as the same; wider fields see different distortions.
- Phase / wavefront: the shape of the light wave's peaks; distortions here are phase errors.
- Blind deconvolution: recovering a sharp image when the blurring function is unknown, using multiple frames.
- Phase diversity: taking measurements with known, different phase patterns so the unknowns can be separated.
- Spatial light modulator (SLM): a programmable device that changes the phase of light pixel by pixel.
- Cramér-Rao bound: a theoretical lower limit on how precisely a quantity can be estimated.
- Coherence time: how long the turbulence stays roughly unchanged. · level: research-level

<details><summary>Original abstract</summary>

Atmospheric turbulence distorts the wavefront of light from a distant scene and blurs its image. Over a field of view wider than the isoplanatic angle, the distortion varies with direction and evolves in time, so no single wavefront describes the blur. Multiframe blind deconvolution (MFBD) can recover the scene from measurements spread over a long acquisition, but falls short during fast imaging because of limited diversity across measurements. We present coded anisoplanatic blind deconvolution (CA-BD), in which a pupil-plane spatial light modulator (SLM) applies a different known phase code to every measurement, with no wavefront sensor or deformable mirror, so that the measurements carry diversity even within a short acquisition. A per-pixel single-layer estimator recovers the object and spatially varying phases from the coded measurements. In simulation, a Cram\'er-Rao bound analysis shows that under anisoplanatism direct imaging needs about 41 times the photons of coded imaging for equal phase precision in strong turbulence. At the stronger of two turbulence strengths, CA-BD outperforms tuned MFBD on average at every burst length. It reduces the phase mean squared error 3.5x for stationary turbulence and 2-3x for time-varying turbulence. Measurements taken within a few coherence times benefit most from the known coded SLM patterns, making faster SLMs the key to its full advantage in time-varying turbulence.

</details>

## Fluids and plasma

### [Formation of Multiple BGK-like Structures in the Time-asymptotic State of Collisionless Vlasov-Poisson Plasmas](https://arxiv.org/abs/2611.28898)
*Hugo A. Carril, Jorge A. Gidi, Roberto E. Navarro et al.* · `physics.plasm-ph` · arXiv:2611.28898v1 · relevance 0.09

- **In one sentence**: High-resolution Vlasov-Poisson simulations of a collisionless Maxwellian plasma show the time-asymptotic state consisting of multiple vortex-like BGK-like structures filling phase space, rather than the usual two counter-propagating BGK modes, with power-law spectra suggesting an energy cascade.
- **In plain words**: This paper studies what a hot, nearly collisionless electrified gas (a plasma) settles into after a strong disturbance. The usual textbook picture is that it ends up as two opposing wave-like patterns in particle velocity and position. Using very detailed computer simulations, the authors report instead that many swirl-like patterns form and gradually fill the available space, and the electric field and averaged particle distribution show a broad range of scales.
- **Why it matters**: It challenges the standard two-wave picture of how plasma relaxes after a perturbation, and the reported power-law spectra hint at an energy cascade similar to turbulence in fluids. The text does not say how far these results apply to real space or laboratory plasmas, so the connection is uncertain.
- **Background needed**: - Plasma: an ionized gas whose charged particles respond collectively to electric fields.
- Collisionless: particles interact mainly through the shared field, not by frequent direct collisions.
- Vlasov-Poisson equations: the kinetic model that tracks the particle distribution in position and velocity space together with the self-consistent electric field.
- Phase space: a map of each particle's position and velocity; filamentation means the distribution becomes increasingly fine-grained in this map.
- BGK mode: a known steady, wave-like solution (Bernstein-Greene-Kruskal) in which particles are trapped in the wave's potential, forming vortex-like swirls in phase space.
- Power-law spectrum: energy spread across scales following a simple power law, a common signature of turbulence-like cascades. · level: research-level

<details><summary>Original abstract</summary>

The time-asymptotic state of a finite-amplitude perturbation in a collisionless and Maxwellian plasma is typically represented as a steady state of two non-linearly superposed, counter-propagating Bernstein-Greene-Kruskal (BGK) modes. Using high-resolution Vlasov-Poisson simulations, we show that the plasma evolves self-consistently into a time-asymptotic state of multiple vortex-like structures that gradually fill the phase-space and reduce filamentation. This occurs without the need for external forcing or the presence of an energetic plasma population. This finding suggests that the time-asymptotic regime of the plasma is rather akin to a non-linear superposition of multiple BGK-like modes associated with nearly constant phase-speed waves. The electric field and the space-averaged particle distribution function exhibit a power-law broad spectrum, which is consistent with an energy cascade towards smaller scales in both position and velocity spaces.

</details>

### [Numerical Study of Flow and Cavitation in Single-Liquid Injectors with Sharp-Edged and Chamfered Orifice Inlets](https://arxiv.org/abs/2611.28527)
*Shreyash Gulati, Sven R. Walsberg, Timothy W. Nearhood et al.* · `physics.flu-dyn` · arXiv:2611.28527v1 · relevance 0.08

- **In one sentence**: A CFD study (k-omega SST turbulence model, ZGB cavitation model, VOF interface tracking) of water flow and cavitation in single-liquid injector orifices with sharp-edged versus chamfered inlets, validated against existing flow-rate data across pressure drops of 0.07 to 0.59 MPa and L/D ratios of 2, 5 and 10.</one_liner>
<parameter name="plain">This paper uses computer simulations to study how water squeezes through the tiny holes of a fuel-style injector nozzle. It looks at whether bubbles form inside the hole (cavitation), and how the shape of the hole's entrance (sharp corner or a beveled edge) and the hole's length change that. The simulated flow rates were checked against earlier lab measurements.</plain>
<why>Cavitation in nozzle orifices affects how a spray forms, which matters for engines and other injection systems. The text reports that the simulations matched earlier experiments, including a known "hydraulic flip" case, but it does not state applications or broader implications, so the wider significance is unclear from this text alone.</why>
<background>
- Orifice: a small hole that a liquid flows through; its length-to-diameter (L/D) ratio describes how long the hole is relative to its width.
- Cavitation: when pressure in a flowing liquid drops low enough, vapor bubbles form and collapse.
- Hydraulic flip: a flow pattern in which the liquid detaches from the hole walls and fills the hole, a known effect seen in earlier experiments.
- Chamfered inlet: an inlet edge that is beveled rather than a sharp corner.
- CFD (computational fluid dynamics): numerical simulation of fluid flow on a computer.
- Turbulence and VOF models: standard computational tools for modeling swirling flow and tracking the liquid-gas boundary.
- MPa (megapascal): a unit of pressure; 0.1 MPa is roughly atmospheric pressure.
</background>
<difficulty>research-level</difficulty>
</invoke>

<details><summary>Original abstract</summary>

In the current work, the investigators used Computational Fluid Dynamics (CFD) to investigate water flow and cavitation in single-liquid injectors with sharp-edged and chamfered orifice inlets. The k-{\omega} Shear Stress Transport (SST) turbulence model was used along with the Zwart-Gerber-Belamri (ZGB) cavitation model and the Volume of Fluid (VOF) method. The CFD predictions for the volumetric flow rate were validated against existing experimental data for the sharp-edged and chamfered orifice inlets. Pressure drops ranging between 0.07 MPa and 0.59 MPa were considered along with orifice length-to-diameter ratios of 2, 5, and 10. Strong cavitation was observed for the sharp-edged orifice inlet cases with a length-to-diameter ratio of 5 and a pressure drop larger than 0.2 MPa. A hydraulic flip was observed for the sharp-edged orifice inlet with a length-to-diameter ratio of 5 and a pressure drop of 0.59 MPa, which was consistent with the findings from the previous experimental study. Cavitation inception was observed for the chamfered orifice inlet cases with a length-to-diameter ratio of 5 and pressure drops larger than 0.2 MPa. For the sharp-edged orifice inlet with orifice length-to-diameter ratios of 2 and 10, a strong cavitation was observed inside the orifice.

</details>

## Biological physics

### [Estimating Extrapolation Factors in Time-Resolved Crystallography](https://arxiv.org/abs/2611.28961)
*Sebastian Bielfeldt, Henry N. Chapman, Thomas J. Lane* · `physics.bio-ph` · arXiv:2611.28961v1 · relevance 0.07

- **In one sentence**: The paper reviews and benchmarks methods for estimating the extrapolation factor (the hidden fraction of triggered molecules) in two-state time-resolved crystallography, and introduces a voxel-by-voxel "Vacuum Level Matching" method with quality-control metrics and a Python package.
- **In plain words**: Time-resolved crystallography takes snapshots of proteins as they change shape after a trigger such as a light pulse, but only some molecules in the crystal actually respond, so the measured signal is a mix that has to be untangled. This paper compares the existing ways of doing that untangling on simulated data, finds that they are not always accurate, especially when the noise is high or few molecules have been triggered. It then proposes a new method that uses the physical rule that electron density cannot go below zero, and reports that it does better on simulated data and gives reasonable results on two real datasets while flagging where the data are too weak.
- **Why it matters**: Accurate separation of triggered and untriggered molecules determines whether the structural changes read from these experiments can be trusted. The paper's explicit quality-control flags and reusable software may help other groups judge their own datasets, though the text does not show how widely the method will be adopted.
- **Background needed**: - Crystallography: X-ray diffraction from a protein crystal yields an electron density map showing where atoms are.
- Time-resolved crystallography: a crystal is triggered (e.g., by light) and imaged at set time points to watch structural change.
- Mixed population: only a fraction of molecules respond to the trigger, so each map is a blend of "changed" and "unchanged" protein.
- Extrapolation factor: a fitted scaling parameter that the paper argues is related to, but not the same as, the true fraction of triggered molecules (called occupancy).
- Voxel: one small 3D cell of the density map; the method works on each cell separately.
- Nonnegativity: electron density cannot be less than zero, which sets a floor ("vacuum level") used as the constraint. · level: research-level

<details><summary>Original abstract</summary>

Time-resolved crystallography (TRX) captures macromolecules in action, but a triggered crystal contains a mixture of triggered proteins in an unknown state and untriggered proteins in the reference state. Separating these is necessary to isolate the dynamics of interest and is an underdetermined data-analysis task. For the simplest case, with one triggered state and one reference state, a range of methods exists, but their assumptions, accuracy, and domains of applicability have not been systematically investigated. Here, we deconstruct and review the methods in current use, employing a unified notation. We make their assumptions explicit and benchmark each on a simulated dataset. A key point is that many of these methods do not estimate the fraction of all triggered molecules in the crystal, but instead estimate a latent parameter we call the extrapolation factor, which is related to but distinct from the so-called "occupancy". As our simulations make apparent, current methods do not always yield accurate results, in particular with noisy data and when the fraction of triggered protein is low. Inspired by previous work, we introduce Vacuum Level Matching, a method that grounds the estimate in the physical constraint that electron density is a nonnegative quantity: it cannot fall below a vacuum level. Operating voxel by voxel, Vacuum Level Matching replaces the manual choices of previous methods with a data-driven procedure and reports quality-control metrics that flag data unable to support a confident prediction. On the same simulated data, it outperforms state-of-the-art methods, and on two experimental datasets, rsEGFP2 and a multi-time-point photolyase series, it recovers known structural changes while flagging issues where the data are weak. Finally, we report an implementation of Vacuum Level Matching in the form of a small, reusable Python package.

</details>

### [Nonequilibrium fluctuations could explain the hot mitochondria paradox](https://arxiv.org/abs/2611.28225)
*Matthew P. Leighton, Benjamin B. Machta* · `cond-mat.stat-mech` · arXiv:2611.28225v1 · relevance 0.04

- **In one sentence**: A proposed explanation for reported ~10 K temperature excesses inside mitochondria, arguing that nonequilibrium fluctuations combined with frequency-selective molecular thermometers could produce apparent temperature differences without a true steady-state gradient.
- **In plain words**: Several experiments have reported that the inside of mitochondria, the energy-producing parts of cells, appears up to about 10 degrees warmer than the surrounding cell. Heat conduction physics seems to rule out such a steady difference unless the cell spends far more energy than it can. This paper proposes that rapid, random fluctuations in the cell, read by molecular probes that respond only to certain frequency ranges, could make the measurements show a 10 K difference while staying within a biologically plausible energy budget.
- **Why it matters**: The reported temperature gap has gone unexplained for nearly a decade, and it matters for how we interpret temperature-sensitive measurements in cells. The text only sketches the idea; it does not show that the proposed mechanism matches the actual experiments, so the claim should be treated as a hypothesis.
- **Background needed**: - Mitochondria: small structures inside cells that produce most of the cell's usable chemical energy.
- Temperature in a cell: normally a uniform value; a real steady temperature difference would need a constant heat source and a way to keep it from leaking away.
- Heat conduction: heat flows from hot to cold and spreads out quickly in small, watery spaces, so large steady gradients are hard to sustain.
- Steady state vs. fluctuations: a steady state is a settled condition; fluctuations are random short-lived changes. Nonequilibrium means the system is continuously driven by energy flow, so its fluctuations need not behave like those in equilibrium.
- Molecular temperature probes: fluorescent or similar molecules whose signal changes with temperature; their readout can depend on the timescale over which they respond.
- Power budget: the rate of energy use the cell can afford. · level: research-level

<details><summary>Original abstract</summary>

Several different experiments have found apparent temperature differences of up to 10 K between the interior of mitochondria and the rest of the cellular environment. The physics of heat conduction, however, precludes the steady-state existence of a temperature difference greater than the microkelvin scale within the cell, absent a far greater energy budget. Nearly a decade after the first reported measurement, this apparent paradox remains unexplained. Here, we propose an explanation which allows the elevated temperature measurements to coexist with the theoretical impossibility of a true 10 K steady-state temperature difference. We suggest that nonequilibrium fluctuations within the cellular environment, combined with molecular temperature probes sensitive to specific ranges of frequencies, can lead to apparent 10 K temperature differences with a biologically attainable power budget.

</details>

## Climate, atmosphere and Earth

### [Tipping cascades may lock the Earth system on a pathway towards a melthouse](https://arxiv.org/abs/2611.29086)
*Victor Couplet, Wim Thiery, Michel Crucifix* · `physics.ao-ph` · arXiv:2611.29086v1 · relevance 0.08

- **In one sentence**: A reduced-complexity Earth system model with a dynamic carbon cycle and interacting tipping elements finds no single threshold for a hothouse state, but suggests tipping cascades could lead to an irreversible melthouse with over 10 m of sea-level rise, possibly even under low-emission scenarios.
- **In plain words**: This paper asks whether the planet could slide past a point of no return into a much hotter, "hothouse" state, and what happens to sea level if it does. Using a simplified computer model of the climate, carbon cycle and large natural systems such as ice sheets, the authors report that they found no single planetary threshold for a hothouse. Instead, one tipping event can set off others in a chain, which they say could push the system toward a melthouse with more than 10 metres of sea-level rise.
- **Why it matters**: Sea-level rise of this size would threaten coastal cities and communities, and the paper argues that the risk comes from chains of tipping events rather than from one tipping point, which affects how emission targets should be judged. The text does not show how sensitive the result is to the model's simplifications, so its size should be treated as model-based rather than a firm projection.
- **Background needed**: - Tipping elements: parts of the Earth system (such as ice sheets, permafrost, or forest systems) that can shift abruptly and often irreversibly once a threshold is crossed.
- Tipping cascade: one tipping element changing and pushing other elements past their own thresholds, so the chain continues even if warming is later reduced.
- Hothouse Earth: a proposed very warm, stable state of the planet that is hard to reverse, often discussed in climate research.
- Melthouse: the paper's term for a state where large-scale ice loss has driven sea level up by over 10 metres and remains there.
- Reduced-complexity model: a simplified climate model that runs quickly and captures key processes but with less detail than the large models used for official projections.
- Dynamic carbon cycle: the model includes how land and ocean absorb or release carbon as the climate changes, rather than fixing carbon levels in advance. · level: research-level

<details><summary>Original abstract</summary>

The potential for the Earth system to transition irreversibly into a hothouse Earth has attracted considerable scientific and media attention but remains insufficiently explored in modeling studies. Using a reduced-complexity Earth system model that includes a dynamic carbon cycle and interacting tipping elements, we find no planetary threshold beyond which the Earth system irreversibly shifts into a hothouse state. Instead, tipping cascades can drive the system towards an irreversible melthouse state with over 10 m of sea-level rise. Such cascades may occur even under low-emission scenarios, preventing long-term stabilization of sea level at intermediate values. Our results overall highlight the substantial risk of a melthouse rather than a hothouse Earth, and call for drastic emission reductions to avert dramatic impacts on coastal cities and communities.

</details>

### [An exact and differentiable rewrite of a coupled weather and fire model](https://arxiv.org/abs/2611.30866)
*John S. Schreck, John Dennis, Iris Linck et al.* · `physics.ao-ph` · arXiv:2611.30866v1 · relevance 0.08

- **In one sentence**: AI coding agents rebuilt selected configurations of the WRF atmospheric model and its coupled fire-spread physics in PyTorch, matching the corrected Fortran code bit for bit over a 12-hour Marshall Fire simulation, with a GPU speed route and a backward pass giving fire sensitivity to wind.
- **In plain words**: This paper looks at whether an established weather-and-fire simulation can be rewritten in a modern machine-learning framework without changing its results. The authors used AI coding agents to rebuild parts of the Weather Research and Forecasting model, including how fire spreads, and checked it against the original Fortran code over 12 hours of the Marshall Fire. The rebuilt version matched the original exactly at all 365 checkpoints, and ran about five times faster on one GPU than the original on a 128-core CPU node.
- **Why it matters**: Being able to compute how a fire forecast changes with wind and moisture, and to swap in learned components while keeping the tested physics, could matter for fire and weather prediction. The text reports these capabilities in synthetic tests and short forecasts, so their value for real operational use is not yet shown.
- **Background needed**: - WRF: a widely used open-source weather model that simulates the atmosphere on a grid.
- Coupled fire model: a component that simulates a wildfire's spread and its heat and smoke feeding back into the air, including firebrands (burning particles carried by wind).
- Fortran: an older programming language common in scientific simulation code.
- PyTorch: a machine-learning software library that can run on GPUs and compute derivatives automatically.
- Bit-for-bit agreement: the two codes produce numerically identical outputs, not just similar ones.
- Differentiable model: one where you can calculate how much the output changes when an input is nudged, via a backward pass.
- Double precision: a high-accuracy number format used in the Fortran reference.
- Marshall Fire: a 2021 wildfire near Boulder, Colorado, used here as a test case. · level: research-level

<details><summary>Original abstract</summary>

AI is changing weather and climate prediction by replacing physical models with learned ones. Here we show a different path, in which AI coding agents rebuild the physical model itself in a machine-learning framework and reproduce its forecast bit for bit. We reconstruct selected configurations of the Weather Research and Forecasting model and its coupled fire physics in PyTorch, treating every difference from the corrected Fortran code as a bug. Across twelve hours of a Marshall Fire simulation, the two independently advancing codes agree bit for bit at all 365 checkpoints, in the atmosphere, fire and firebrand particles. This agreement holds when the code runs one operation at a time, with the Fortran code's mathematical library. On a separate fast route, the reconstructed model runs about five times faster on one GPU than the double-precision Fortran code on a 128-core CPU node. One backward pass maps the fire's sensitivity to the wind at every grid point. In synthetic tests, its derivatives show how to change wind and fuel moisture to correct a misplaced fire front. Neural networks replace the radiation and fire-spread calculations in 24-hour coupled forecasts, and we measure their effect against the physical calculation. An established model thus becomes fast, differentiable and open to learned components, with its tested calculation intact.

</details>

## Cosmology

### [Scale-dependent Dark Matter in a Multi-component Cosmological Framework: Distinct Components Governing Galactic and Cosmological Dynamics](https://arxiv.org/abs/2611.29007)
*V. K. Oikonomou* · `astro-ph.CO` · arXiv:2611.29007v1 · relevance 0.18

- **In one sentence**: The paper generalizes a scale-dependent, nearly isothermal equation of state for dark matter from galactic to cosmological scales, argues it cannot be all of the dark matter, and proposes that several distinct dark matter components cluster differently and govern dynamics at different scales.
- **In plain words**: The paper is about what dark matter, the unseen mass that holds galaxies together, is like in terms of pressure and density. The authors previously found a model where dark matter's pressure-to-density ratio varies slowly with distance from a galaxy's centre, and here they extend that idea to whole-universe scales. They conclude that this kind of dark matter cannot be the only dark matter present, and suggest that different dark matter components may control dynamics at different sizes.
- **Why it matters**: If dark matter comes in several parts that behave differently at different sizes, that would bear on how galaxies and the large-scale universe are modelled. The text gives only the theoretical framing and conclusions, so how strongly the claims hold cannot be judged from this excerpt alone.
- **Background needed**: - Dark matter: invisible matter inferred from its gravitational effects on galaxies and the universe's large-scale structure.
- Equation of state: a relation linking a material's pressure (P) to its density (rho); here P = K·rho, where K is a "entropy-like" factor.
- Isothermal: a state where temperature (or velocity spread) is roughly uniform.
- Velocity dispersion (sigma): the typical spread of speeds of particles; a measure of how "hot" a gas of particles is.
- Scale-dependent: the property changes depending on the size of the region studied.
- Cosmological scales: the size of the whole universe, as opposed to individual galaxies. · level: research-level

<details><summary>Original abstract</summary>

In this work we generalize the concept of scale-dependent equation of state dark matter from galactic to cosmological scales. At galactic scales, the scale-dependent equation of state which successfully describes dark matter dominated galaxies has a nearly isothermal equation of state of the form $P(r)=K(r)\rho(r)$, where the entropy function $K(r)$ is radius dependent and slowly varying with the galactic radius. Using appropriate theoretical arguments, the successful galactic scale dark matter model is generalized to have a universal equation of state of the form $\langle P(\chi)\rangle =\langle \rho(\chi)\rangle \langle \sigma_{DM}^2\rangle$, where $\chi$ is the scale of the system under study and it can describe cosmological or galactic scales and $\sigma_{DM}$ is the characteristic velocity dispersion of dark matter at the relevant scales. This results to the entropy function behaving universally as $K(\chi)=\langle \sigma_{DM}^2\rangle$. We investigate the cosmological implications of scale-dependent equation of state dark matter, and we conclude that this scale-dependent equation of state dark matter cannot be the sole component of dark matter in the Universe. Also the second aim of this work is to provide a sufficient explanation for the question why $K_0$ changes for each galaxy, where $K_0$ is the value of $K(r)$ at intermediate and large radii from the core of the galaxy. Furthermore, we introduce the concept of having distinct dark matter components which cluster differently, and thus controlling differently the dynamics of the Universe at various scales. Scale-dependent equation of state dark matter can control the galactic scales, while another component can dominate at cosmological scales and thus control the Universe at cosmological scales.

</details>

### [Closure of averaged Einstein equations by DESI data](https://arxiv.org/abs/2611.31041)
*Thomas Buchert* · `astro-ph.CO` · arXiv:2611.31041v1 · relevance 0.15

- **In one sentence**: The paper tests whether the dark energy behaviour measured by DESI (as a function of cosmic time) could instead arise from inhomogeneous structure in general relativity, using an effective scalar "morphon" field and a single closure condition fitted to DESI 3-year data parametrizations.
- **In plain words**: The paper asks whether the odd-looking changes in dark energy that the DESI survey reports over cosmic history could instead come from the lumpy, uneven distribution of matter in the universe, rather than from a separate dark energy ingredient. The authors describe an averaged, effective description of that lumpiness, which they call a "morphon," and find that it can shift from ordinary to "phantom" behaviour without breaking basic energy rules. They then fit one required closure condition to parametrizations of DESI's 3-year data and show how the resulting effective quantities vary with redshift.
- **Why it matters**: If lumpiness of matter can mimic the measured dark energy trend, that would bear on how we interpret one of the leading cosmology observations. The text does not show that the hypothesis holds; it frames the paper as setting a benchmark that any structure-formation model in this framework would need to meet.
- **Background needed**: - Dark energy: the unexplained component thought to drive the accelerating expansion of the universe; standard models describe it by an "equation of state" (the ratio of its pressure to its energy density).
- Redshift: a measure of how far back in time we are looking; higher redshift means an earlier epoch.
- DESI: the Dark Energy Spectroscopic Instrument survey, which has reported evidence that dark energy may evolve with time.
- Phantom behaviour: a hypothetical dark energy whose equation of state is below -1, meaning its density grows over time.
- Averaged/backreaction cosmology: the idea that averaging Einstein's equations over lumpy matter can produce extra effective terms that look like dark energy.
- Energy conditions: basic physical requirements that energy densities stay non-negative in a suitable sense.
- Flow-orthogonal foliation: a way of slicing spacetime into time-slices that follow the matter flow. · level: research-level

<details><summary>Original abstract</summary>

We benchmark the hypothesis that the redshift dependence of postulated dark energy in the standard model, measured by the DESI collaboration, is a natural outcome of dark energy-free models of structure formation in general relativity. We recall fundamental results and the properties of averaged dust cosmologies that suggest to replace the dark energy equation of state through the nonperturbative impact of the inhomogeneous geometry. The relevant mechanism can be phrased in terms of an effective mean field description of inhomogeneities using the fluid analogy of a scalar field (the `morphon'). Without violating energy conditions this effective field exhibits a cross-over to phantom behaviour, compatible with observations. The exact dark energy-free framework needs a single closure condition that we implement in terms of parametrizations of the 3-years data of the DESI team. The resulting redshift dependence of effective cosmological characteristics is then illustrated and subject to physical interpretation. The aim of this paper is to set a benchmark that has to be met by any structure formation model or simulation investigated within general relativity in a flow-orthogonal foliation of spacetime, given the hypothesis.

</details>

## Galaxies

### [On the effect of a redshift- and metallicity-dependent top-heavy IMF on high-redshift UV luminosity functions](https://arxiv.org/abs/2611.31148)
*Keita Fukushima, Shuya Kitagawa, Akio K. Inoue et al.* · `astro-ph.GA` · arXiv:2611.31148v1 · relevance 0.14

- **In one sentence**: A semi-analytic galaxy model tests whether a top-heavy, redshift- and metallicity-dependent stellar initial mass function, combined with self-consistent dust attenuation, can reproduce the JWST-observed UV luminosity function at z ~ 10-13.
- **In plain words**: Telescopes such as JWST have found more bright galaxies in the very early universe than many models predicted. This paper asks whether the stars in those galaxies may have formed with a larger share of massive stars than usual, which would make them shine more brightly in ultraviolet light. The authors built model galaxies with this assumption and found that the extra brightness is partly cancelled out by the dust that the extra stars produce, so the model matches observations at z ~ 10 but not clearly at z ≳ 12.
- **Why it matters**: The number of bright early galaxies is a live question in galaxy evolution, and this work shows that the stellar mass distribution and the dust it creates have to be treated together rather than separately. The authors report that the highest-redshift comparison does not give a robust constraint, so the conclusions are tentative.
- **Background needed**: - Initial mass function (IMF): the distribution of stellar masses at birth; a "top-heavy" IMF means more massive, short-lived, very bright stars.
- Redshift (z): a measure of look-back in time; higher z means an earlier universe. z ~ 10 is roughly 500 million years after the Big Bang.
- UV luminosity function (UVLF): the number of galaxies per volume at each ultraviolet brightness; the main observable being compared.
- Metallicity: the fraction of elements heavier than helium in a star or gas; early galaxies are low in metallicity.
- Dust attenuation: dimming of starlight by dust grains, which absorb ultraviolet light.
- Semi-analytic model: a simplified, rule-based way of growing galaxies inside a simulated dark-matter structure.
- SED template: a model spectrum of light emitted by a stellar population. · level: research-level

<details><summary>Original abstract</summary>

JWST observations have revealed a higher-than-expected abundance of bright galaxies at $z \gtrsim 10$. Several scenarios have been proposed to explain this excess, one of which invokes a top-heavy stellar initial mass function (IMF) in the early Universe. In this work, we construct spectral energy distribution (SED) templates based on a redshift- and metallicity-dependent IMF ($z$-$Z$ dependent IMF) motivated by the star-cluster simulations of Chon et al. (2022) and the redshift-dependent IMF model of Steinhardt et al. (2020). We implement these templates in a semi-analytic galaxy model built on a large-box $N$-body simulation to investigate the impact of a top-heavy IMF on the ultraviolet luminosity function (UVLF) of high-redshift galaxies. The adopted $z$-$Z$ dependent IMF enhances the UV luminosity of young stellar populations, particularly at low metallicity, and increases the scatter in the UV luminosity-to-star formation rate conversion factor relative to the Kroupa IMF. Without dust attenuation, both top-heavy IMF models predict a substantially enhanced bright end of the UVLF. However, when dust attenuation is included and calibrated at $z=7$, IMF-dependent metal enrichment and the resulting dust attenuation partly offset the intrinsic UV enhancement. The self-consistent model broadly reproduces the observed UVLF at $z\sim10$, although discrepancies remain at $z\gtrsim12$. For the selected high-redshift UVLF constraints, the best-fitting dust optical depths are 51% and 21% of the fiducial values at $z=9.7$ and $13.04$, respectively, indicating a preference for weaker effective dust attenuation. The highest-redshift comparison does not provide a robust constraint. Our results highlight the importance of accounting for both enhanced stellar UV emission and IMF-dependent metal enrichment and dust attenuation when assessing the impact of a top-heavy IMF on high-redshift galaxies.

</details>

### [Outflows and Young Stars in the Auriga-California Giant Molecular Cloud](https://arxiv.org/abs/2611.29408)
*T. A. Movsessian, T. Yu. Magakian* · `astro-ph.GA` · arXiv:2611.29408v1 · relevance 0.12

- **In one sentence**: A survey with Byurakan 1-m Schmidt narrowband Hα and [SII] imaging, slitless spectroscopy, and Spitzer/WISE infrared data that finds seven new Herbig-Haro objects, molecular hydrogen outflows, Hα emission-line stars and reflection-nebula stars in the Auriga-California Molecular Cloud, concentrated along its northern filament.
- **In plain words**: This paper looks for signs of new star birth in a nearby cloud of gas and dust called the Auriga-California Molecular Cloud. The authors used special filtered photographs and infrared images to find glowing shock fronts (Herbig-Haro objects) and streams of hot gas shot out by young stars. They report seven new such objects, along with many young stars, and find that most of this activity lies along the cloud's northern dark filament.
- **Why it matters**: The work maps where stars are currently forming in a moderately active nearby cloud, which helps show how star formation is spread across a region. The text does not go further than this regional census, so its wider significance is unclear from the excerpt alone.
- **Background needed**: - Molecular cloud: a cold, dense cloud of gas and dust where stars form.
- Young stellar object (YSO): a newborn star still gathering material; Class 0/I means very young and deeply embedded in dust.
- Herbig-Haro (HH) object: a small glowing patch of gas where a fast jet from a young star hits surrounding material.
- Outflow: a jet or wind of gas blown out from a young star; molecular outflows are traced by cold molecular gas, and H2 (molecular hydrogen) emission marks them in infrared.
- Hα and [SII]: specific wavelengths of light emitted by hot hydrogen and sulfur in shocks; narrowband imaging isolates them.
- Reflection nebula: dust near a star that scatters its light.
- Spitzer and WISE: infrared space telescopes; unWISE is a reprocessed archive of WISE data. · level: intermediate

<details><summary>Original abstract</summary>

The Auriga-California Molecular Cloud (AMC) is a nearby star-forming region with a moderate level of star formation activity. Previous infrared surveys have shown that its young stellar population is concentrated along a dense filament extending north of NGC 1579. We searched for new manifestations of ongoing star formation in the AMC by identifying optical and molecular outflows, H{\alpha} emission-line stars, and young stars associated with reflection nebulae. Narrowband H{\alpha} and [SII] imaging, together with slitless spectroscopy, were obtained with the 1-m Schmidt telescope of the Byurakan Observatory. The optical data were complemented by near-infrared images from the Spitzer Enhanced Imaging Products (SEIP) and by WISE/unWISE archival data. We discovered seven new Herbig-Haro (HH) objects and outflows associated with several young stellar objects, including deeply embedded infrared sources and stars surrounded by compact reflection nebulae. Nearly all of the optical HH objects have molecular hydrogen counterparts, and several additional candidate H2 outflows without optical counterparts were identified. Particularly noteworthy is a compact region around V347 Per that appears to host at least three molecular outflows. We also present a list of newly identified H{\alpha} emission-line stars and a catalogue of stars associated with optical reflection nebulae. Both populations are concentrated primarily along the northern dark filament of the cloud. The spatial distribution of the newly identified HH objects, molecular outflows, emission-line stars, and nebulous young stars confirms that the northern filament is the principal site of ongoing star formation in the AMC. The close correspondence between the optical and molecular outflowsfurther suggests that most of their driving sources are deeply embedded Class 0/I young stellar objects.

</details>

## Exoplanets and planetary science

### [Updated View on Titan's Habitability: Interior and Surface Aqueous Environments](https://arxiv.org/abs/2611.28186)
*Diogo Gon\c{c}alves, L\'igia F. Coelho, Catarina Miranda et al.* · `astro-ph.EP` · arXiv:2611.28186v1 · relevance 0.10

- **In one sentence**: A review of the prebiotic chemistry potential of three aqueous settings on Saturn's moon Titan (its interior ocean, cryovolcanic flows, and impact-melt pools), framed around the upcoming Dragonfly mission.
- **In plain words**: This paper looks at whether Titan, Saturn's large moon, could have conditions where the chemistry leading toward life's building blocks might happen. The authors review three kinds of places where liquid water might meet carbon-based molecules: a hidden underground ocean, icy lava-like flows erupting from the surface, and pools of melted rock left by meteorite impacts. For each, they list what helps this chemistry along and what holds it back.
- **Why it matters**: NASA's Dragonfly mission is planned to visit Titan and study its organic chemistry directly, so a current map of the open questions helps decide what to measure. The text also notes that the longevity of Titan's interior water has recently been questioned, which is a live uncertainty rather than a settled result.
- **Background needed**: - Titan: Saturn's largest moon, with a thick nitrogen atmosphere and surface lakes of hydrocarbons, and likely an ice shell over a salty or ammonia-rich water layer.
- Prebiotic chemistry: chemistry that produces molecules (such as amino acids or sugars) that were precursors to life, not life itself.
- Organic molecules: carbon-containing compounds.
- Ammonia: a nitrogen-hydrogen compound that lowers water's freezing point, keeping liquid water longer.
- Cryovolcanism: eruption of icy, water-based material instead of molten rock.
- Impact-melt pool: a pocket of rock melted by a meteorite strike, which can stay warm for a long time.
- Dragonfly: a NASA rotorcraft lander planned to fly across Titan's surface.
- This is a review synthesis; the text given does not include new measurements or specific numbers. · level: intermediate

<details><summary>Original abstract</summary>

Saturn's moon Titan is the only world beyond Earth where abundant organic molecules and liquid water are expected to interact. Crucially, these interactions yield prebiotic molecules central to terrestrial biochemistry. Characterizing this prebiotic chemistry is one of the main science goals of NASA's upcoming Dragonfly mission. Here we synthesize the current state of knowledge on the habitability and prebiotic potential of Titan's three aqueous settings: its interior hydrosphere, its putative cryovolcanic flows, and its impact-melt pools. For each setting, we identify the enabling factors and the principal bottlenecks that limit prebiotic complexification. Titan's interior is likely pervaded by liquid water in contact with organic material delivered from the surface and released from the core, though the longevity of its liquid water has recently been called into question. Cryovolcanic regions transiently expose surface organics to ammonia-bearing aqueous melts but are constrained by short freezing timescales. Impact-melt pools, by contrast, are warm and long-lived environments whose prebiotic chemistry is limited by the scarcity of ammonia. Dragonfly will return ground-truth data not only for Titan's habitability, but also for organic-rich aqueous environments across the Solar System and beyond. The years before its arrival are the last in which predictive work can still shape Dragonfly's investigations.

</details>

### [Probabilistic, facility-specific prioritisation of temperate exoplanets for atmospheric characterisation with JWST and the ELT](https://arxiv.org/abs/2611.31181)
*Effy Viridis* · `astro-ph.EP` · arXiv:2611.31181v1 · relevance 0.08

- **In one sentence**: A public Monte Carlo framework (UHI v6.1) builds facility-specific, probabilistic priority lists of 6,112 NASA-archived planets for JWST transit spectroscopy and ELT reflected-light observations, with Sobol sensitivity analysis showing the XUV shoreline dominates rocky-planet rankings and Hycean results are only indicative.
- **In plain words**: The paper asks which temperate planets outside our solar system should be looked at first with the James Webb Space Telescope and the planned Extremely Large Telescope, which can only spend limited time on each target. Instead of producing one ranking, the authors run 10,000 simulated draws that account for uncertain measurements, and they report how often each planet lands near the top. They find that whether a planet survives basic habitability checks matters most for whether it makes the lists, and that one assumption about how much stellar radiation a planet's atmosphere can withstand drives much of the rocky-planet results.
- **Why it matters**: Observing time on the largest telescopes is scarce, so a transparent, rerunnable way to rank targets could guide which atmospheres get studied first. The text does not show that these lists have been tested against actual observations, so their practical value remains to be seen.
- **Background needed**: - Transit spectroscopy: measuring starlight filtered through a planet's atmosphere as it passes in front of its star; works for planets that transit.
- Reflected-light observations: measuring starlight bounced off a non-transiting planet, the approach planned for the ELT's planet-finding instrument (PCS).
- Temperate planet: a planet whose surface temperature could allow liquid water.
- Hycean planet: a hypothetical world with a deep water layer under a hydrogen-rich atmosphere.
- XUV shoreline: the boundary in stellar X-ray and extreme-UV flux below which a planet's atmosphere is likely to be kept.
- Monte Carlo: repeating a calculation many times with randomly drawn inputs to see the spread of outcomes.
- Sobol sensitivity indices: numbers showing how much each input assumption contributes to the variation in results; a higher total-order index means more influence.
- Sigma (5σ, 3σ): confidence thresholds for detection; 5σ is a stricter detection standard. · level: research-level

<details><summary>Original abstract</summary>

Deciding which temperate exoplanets to observe first matters for JWST transit spectroscopy and for planned ELT reflected-light instruments, yet signal-to-noise metrics ignore habitability and similarity indices ignore observability. We present an open Monte Carlo framework (UHI v6.1) that builds probabilistic priority lists separately for each facility and composition class, never as a single ranking. For each of 6,112 planets in the NASA Exoplanet Archive, 10,000 draws carry catalogue uncertainties through climate, cumulative stellar-XUV atmospheric retention, per-draw rocky, Hycean or gas-rich classes, and a JWST (transiting) or ELT/PCS (non-transiting) detection model, giving each planet a survival probability, a conditional score and a top-N probability. At $5\sigma$, 255 rocky and 71 Hycean candidates remain viable. A Saltelli--Sobol analysis of 32 assumptions ($N = 512$) shows that the location and width of the XUV shoreline dominate the rocky lists, with total-order indices of 0.22 and 0.12 at $5\sigma$ (0.25 and 0.14 at $3\sigma$), and all ten leading indices have 95% bootstrap half-widths below 0.05. For Hycean planets most outputs are degenerate and the analysis does not converge, so that branch is reported as indicative. Membership of these lists is limited mainly by whether a planet survives the habitability vetoes: at $5\sigma$, 3 of the nominal JWST and 4 of the nominal ELT rocky top-10 targets enter the top 10 in at least half of all draws, yet every one of them stays in the top 10 in more than half of the draws in which it survives. Code, per-planet posterior summaries, sensitivity tables and maps are public, so observers can rerun the lists under their own instrument assumptions and see which inputs would most change a target's priority.

</details>

## High-energy astrophysics

### [Tidal effects of bulk viscosity in neutron stars](https://arxiv.org/abs/2611.30454)
*A. Kanakis-Pegios, P. S. Koliogiannis, Ch. C. Moustakidis* · `astro-ph.HE` · arXiv:2611.30454v1 · relevance 0.18

- **In one sentence**: This paper computes how bulk viscosity from direct Urca neutron decays dissipates tidal energy in neutron stars, expressed through lag time and dissipative deformability, as a function of temperature and compactness, with causality-based upper bounds for 1.4 solar-mass and maximum-mass stars.
- **In plain words**: Neutron stars in close pairs raise tides on each other, and the way the star's dense matter resists being squeezed can drain some of that energy as heat. This paper studies one such drain, called bulk viscosity, which comes from neutrons and protons being converted into one another and back as the star is squeezed and stretched. The authors estimate how strong this effect is at temperatures up to a few MeV, and find it peaks at a particular temperature and is stronger in medium-mass stars than in the heaviest ones.
- **Why it matters**: Tidal effects shape the gravitational-wave signal from merging neutron stars, so any extra energy loss could in principle be looked for in those signals. The paper's bounds are theoretical benchmarks; the text does not show whether such effects are actually detectable with current or planned instruments.
- **Background needed**: - Neutron star: the collapsed core of a massive star, about 1.4 times the Sun's mass packed into a city-sized ball.
- Tidal deformability: how much a star gets stretched by a companion's gravity; it affects the gravitational-wave signal from a binary merger.
- Bulk viscosity: a form of internal friction, here arising when compression changes the balance between particle types, which turns motion into heat.
- Direct Urca process: a fast reaction in which neutrons and protons convert to each other, emitting neutrinos; it restores chemical balance after compression.
- Equation of state: the rule relating a star's pressure to its density, which sets its size and internal structure.
- Compactness: how massive a star is relative to its radius.
- MeV: a unit of energy used for particles; a few MeV corresponds to temperatures of roughly tens of billions of kelvin.
- Causality bound: an upper limit imposed because nothing in the star can carry signals faster than light. · level: research-level

<details><summary>Original abstract</summary>

Bulk viscosity in neutron-star matter provides a temperature-dependent mechanism for tidal dissipation. In this study, we investigate the impact of bulk viscosity on the dissipative tidal response of neutron stars composed of neutrons, protons, and electrons. Employing cold equations of state derived through the momentum-dependent interaction model, we examine the bulk viscosity arising from the direct Urca process, which acts to restore chemical equilibrium. The temperature dependence is incorporated through the weak-interaction rate, allowing us to explore the behavior of bulk viscosity in the neutrino-transparent regime at temperatures up to a few MeV. To account for the spatial distribution of bulk viscosity within neutron stars, we introduce the effective bulk viscosity, a volume-averaged quantity over the region where direct Urca process operates, and establish a connection with the bulk viscosity. Specifically, we investigate its implications for tidal quantities, including the lag time and dissipative deformability, highlighting their dependence on temperature and stellar compactness. We find that the dissipative tidal effects become maximal at a temperature approximately coinciding with the one of maximum bulk viscosity on the onset of direct Urca. Additionally, these effects are more pronounced in intermediate neutron star masses compared to maximum ones. Finally, for both canonical $1.4\;M_\odot$ and maximum-mass neutron star configurations, we derive causality-based upper bounds on these quantities, providing theoretical benchmarks for assessing the potential observability of bulk-viscous effects in gravitational-wave signals from binary neutron star inspirals.

</details>

### [Fast Radio Bursts Co-detected by CHIME/FRB and DSA-110 from 400 to 1530 MHz](https://arxiv.org/abs/2611.28250)
*S. K. Ocker, K. Nimmo, J. Faber et al.* · `astro-ph.HE` · arXiv:2611.28250v1 · relevance 0.18

- **In one sentence**: A sample of 15 fast radio bursts detected by both the CHIME/FRB and DSA-110 telescopes (12 with channelized voltage data from both, 9 with secure redshifts) is used to study spectral shape, scattering, and selection effects across 400 to 1530 MHz.
- **In plain words**: Fast radio bursts are millisecond flashes of radio waves from distant galaxies, and their origin is still debated. This paper looks at 15 such flashes that were caught by two different radio telescopes, CHIME and DSA-110, which together cover a very wide range of radio frequencies. The authors report how the bursts' brightness changes across that range, how their signals are smeared out as they travel, and why the two telescopes seem to pick up different kinds of bursts.
- **Why it matters**: Most bursts have been studied over a narrower slice of the radio spectrum, so measuring them across more than a gigahertz of bandwidth tests how the emission and the material between us and the source change the signal. The text suggests the findings may guide future surveys that cover very wide frequency ranges, though the broader physical implications are not spelled out in the summary.
- **Background needed**: - Fast radio bursts (FRBs): brief, bright radio flashes of extragalactic origin, lasting milliseconds.
- CHIME/FRB and DSA-110: two radio telescope systems that detect FRBs at different frequencies (about 400–800 MHz and 1280–1530 MHz).
- Spectral index: a number describing how a burst's brightness scales with frequency.
- Spectral turnover: a frequency above or below which the emission drops off, similar to some pulsar and magnetar radio spectra.
- Pulse broadening (scattering): the smearing of a burst's signal in time as radio waves pass through plasma in galaxies or between galaxies.
- Scintillation: rapid flickering of brightness caused by interference as radio waves cross turbulent plasma, akin to twinkling starlight.
- Redshift: a measure of how far away a source is, inferred from how much its light is stretched to longer wavelengths.
- Repeater vs. non-repeater: repeating FRBs emit more than one burst; the study's sample is all non-repeaters except one.
- Selection effect: a bias in what a survey is able to detect, which can distort measured averages. · level: research-level

<details><summary>Original abstract</summary>

We present a sample of $15$ fast radio bursts (FRBs) that were co-detected by the Deep Synoptic Array (DSA-110) and the Canadian Hydrogen Intensity Mapping Experiment (CHIME) between 2022 and 2024, of which $12$ have channelized voltage data from both instruments and 9 have secure redshifts. All but one are as-yet-non-repeating. Most bursts span the entire bandwidth of each instrument (400-800 MHz for CHIME, 1280-1530 MHz for DSA-110), significantly expanding the number of FRBs known to emit across $>1$ GHz of spectral bandwidth and constraining the spectral evolution of energy and propagation effects. On average, the FRBs exhibit higher spectral energies (up to a factor of $\sim10$) in the CHIME band but are lower in peak flux density due to substantial pulse broadening. The sample mean (median) spectral index $-0.4\pm0.4$ ($-0.3\pm0.4$) is shallower than previously reported spectral indices, likely a selection effect. A third of the sample shows evidence for a spectral turnover, comparable to that seen in GHz-peaked pulsar and magnetar spectra. Joint scintillation and pulse broadening constraints indicate that nearly all bursts encounter multiple scattering screens, with pulse broadening originating within their host galaxies. The co-detected bursts are among the most scattered in the CHIME/FRB sample, while being the narrowest in the DSA-110 sample, indicating that CHIME/FRB and DSA-110 select different subsets of the FRB population; the interplay between intrinsic burst width, scattering, and the FRB search time resolution creates a narrow window of sensitivity to co-detected FRBs, providing a blueprint for future ultra-wideband FRB surveys.

</details>

## Stars and the Sun

### [Asteroseismic investigation of intermediate age open star cluster NGC 2126](https://arxiv.org/abs/2611.29291)
*Athul Dileep, Santosh Joshi, Patricia Lampens et al.* · `astro-ph.SR` · arXiv:2611.29291v1 · relevance 0.11

- **In one sentence**: A preliminary asteroseismic study of delta Scuti pulsators and the binary V551 Aur in the intermediate-age open cluster NGC 2126, using TESS full-frame images and earlier ground-based photometry.
- **In plain words**: Astronomers studied the rhythmic brightness wobbles of a group of pulsating stars in NGC 2126, a cluster of stars several hundred million years old. By comparing the pulsation patterns with models of how stars vibrate, they tentatively identified the vibration modes of three stars and firmly identified a second overtone in one. They also found that a pulsating star in a close binary pair seems to be affected by its companion's gravity, and that one star shows chemical features resembling an Am star.</plain>
<parameter name="why">Stars that pulse in a cluster share an age and origin, so their vibrations can test stellar models more tightly than single stars alone. The finding that the main pulsator in the binary V551 Aur does not match a fundamental radial mode is an open puzzle the text does not resolve, and the authors describe the work as preliminary.
- **Background needed**: - Open star cluster: a loose group of stars born together from the same cloud; NGC 2126 is intermediate in age.
- Delta Scuti star: a type of pulsating star whose brightness rises and falls over minutes to hours as its outer layers swell and shrink.
- Asteroseismology: inferring a star's interior structure from the frequencies of its vibrations, much as seismology reads Earth's interior from earthquake waves.
- Radial mode / overtone: a vibration in which the star expands and contracts uniformly; the fundamental is the simplest, and overtones are higher-order versions with more nodes.
- Period-luminosity relation: an empirical link between how fast a pulsator oscillates and how bright it is, used to estimate which mode is present.
- TESS: NASA's space telescope that surveys large areas of sky for changes in starlight.
- Binary star (eclipsing): two stars orbiting each other, dimming periodically when one passes in front of the other.
- Am star: a type of star with unusual surface chemistry, such as enhanced metals and depleted calcium-group elements. · level: research-level

<details><summary>Original abstract</summary>

We present a preliminary asteroseismic investigation of the pulsating stars in the intermediate-age open cluster NGC 2126. The TESS Full Frame Images and ground-based photometry from the previous study, Dileep et al. (2025), were used to identify the pulsation modes of {\delta} Scuti member stars using period-luminosity relations and pulsation modelling. Our analysis resulted in a tentative identification up to the first radial overtone in stars N1, N2 and ZV1. Additionally, the second radial overtone was secured in N1. The disentangled pulsation and eclipse light curves of the binary star V551 Aur (V6) from our previous research were employed to study pulsation amplitude and phase modulations across the orbital period. The primary component of V6 exhibits pulsations showing amplitude and phase modulations, indicating tidal influence on the oscillations. Modelling the pulsation as the fundamental radial mode reveals that in order for the mode to be radial, the star must be significantly brighter than observed. Hence, the mode is not the fundamental radial mode or the overtones. Low-resolution spectroscopy was used to search for chemical peculiarities in the pulsating members, and we found that star ID 143 has features similar to an Am star.

</details>

### [Empirical Mass and Radius Relations for Main-sequence Stars from Detached Eclipsing Binaries](https://arxiv.org/abs/2611.28229)
*D. M. Rowan, C. S. Kochanek* · `astro-ph.SR` · arXiv:2611.28229v1 · relevance 0.06

- **In one sentence**: Empirical polynomial relations, calibrated on 605 main-sequence stars in detached eclipsing binaries, that predict stellar mass and radius from spectroscopic temperature, surface gravity/density and metallicity, with a comparison against MIST and PARSEC stellar models.
- **In plain words**: Stars in pairs that pass in front of each other, seen as eclipses, let astronomers measure their masses and sizes very precisely. This paper uses 605 such stars to build formulas that estimate a star's mass and radius from quickly measured properties like temperature and composition. The formulas predict the Sun's mass and radius to within a few tenths of a percent and fit the calibrator stars to within about 4% in radius and 8% in mass.
- **Why it matters**: Mass and radius estimates feed into work on planets orbiting other stars, where a star's size and mass set the size of any planet found, so better formulas matter for that work. The text also reports that two widely used stellar model sets differ systematically from the formulas, with hot stars' radii overestimated and cool stars' underestimated by several percent; the text does not say how this affects specific planet results.
- **Background needed**: - Main-sequence star: a star in the stable, long-lived phase of hydrogen burning, like the Sun.
- Detached eclipsing binary: two stars orbiting each other without touching, whose light dims periodically as one passes in front of the other; this allows direct measurement of mass and radius.
- Spectroscopic parameters: properties inferred from a star's light spectrum, such as effective temperature, surface gravity, and metal content (metallicity).
- Surface gravity and mean density: related ways of describing how tightly a star's mass is packed into its size.
- Empirical relation: a formula fitted to observed data rather than derived from physical theory.
- RMS scatter and dex: the typical size of prediction errors; a dex is a logarithmic unit, where 0.01 dex is roughly 2.3%.
- Stellar model grids (MIST, PARSEC): theoretical computer models of how stars evolve, used as a reference for comparison. · level: research-level

<details><summary>Original abstract</summary>

Detached eclipsing binaries have long served as fundamental calibrators for stellar models because they provide precise measurements of stellar masses and radii. Given a sample of detached eclipsing binaries, we can derive empirical relations between spectroscopic parameters (effective temperatures, surface gravities and abundances) and stellar masses and radii. We use a sample of 605 stars (330 with metallicities) in detached eclipsing binaries to update and refine these empirical models for main-sequence stars. An eight-term polynomial model reproduces the radii and masses of the eclipsing binary calibrators with an RMS scatter of $\sigma_{\log R} = 0.0161$ dex (3.8%) and $\sigma_{\log M} = 0.0322$ dex (7.7%), respectively. Most of this scatter is explained by the parameter uncertainties - the estimated intrinsic scatters in the radius and mass are only $\sigma_{\rm int}=0.0085$ and $0.017$ dex (2.0% and 4.0%). The predicted mass and radius of the Sun are $(1.028\pm0.004)\ M_\odot$ and $(1.014\pm0.002)\ R_\odot$. A 14-term model, while formally preferred, explains little more of the intrinsic scatter. We additionally provide the equivalent relations in terms of the mean stellar density instead of the surface gravity for use with exoplanet host stars. If we compare the 8-term model to MIST and PARSEC model stars with closely matched spectroscopic parameters, we find systematic differences. For example, the radii of hot (cool) stars are systematically over- (under-)estimated in both models by several percent.

</details>

## Chemical physics

### [An equivariant classical density functional for ionic fluids at complex interfaces](https://arxiv.org/abs/2611.28501)
*Bingqing Cheng* · `physics.chem-ph` · arXiv:2611.28501v1 · relevance 0.13

- **In one sentence**: A machine-learned classical density functional for ionic fluids, combining a symmetry-adapted neural free energy for short-range correlations with explicit long-range electrostatics, is trained on the restricted primitive model and tested on charged solutes and atomically structured metal electrodes.
- **In plain words**: The paper concerns how salt ions crowd and arrange themselves next to charged, irregularly shaped surfaces such as electrodes in batteries or supercapacitors. The authors built a learned mathematical model that predicts these ion distributions without running full atomistic simulations for every case. According to the text, it matches molecular dynamics results around charged solutes, including cases where the force reverses direction, and it captures how charge spreads over metal electrodes with steps and bumps and how charging behaves over time.
- **Why it matters**: Predicting ion behaviour at complex interfaces matters for electrochemical devices, and a model that avoids costly atomistic simulation could make exploring composition and geometry faster. The text claims transferability to new particle and electrode types, but the scope beyond the tested systems is not established here, and the authors only say the framework "can be extended" to more complex fluids.
- **Background needed**: - Classical density functional theory: a way to get the equilibrium distribution of a fluid from a free-energy functional, instead of tracking every particle.
- Restricted primitive model: a simplified model of salt where ions are charged hard spheres in a uniform background solvent.
- Long-range electrostatics (Coulomb forces): forces that decay slowly with distance, so they must be treated explicitly.
- Molecular dynamics (MD): computer simulation that moves every atom over time; used here as the reference.
- Machine learning / neural free energy: a learned function standing in for the hard-to-compute part of the free energy from short-range ion packing.
- Symmetry-adapted: the learned model respects rotations and reflections of the geometry.
- Capacitance: how much charge a surface stores per unit voltage; the text reports it rises with surface steps and bumps.
- Mobility: how fast ions move under a force, here taken from separate bulk simulations. · level: research-level

<details><summary>Original abstract</summary>

Predicting the combined effects of ionic packing and long-range electrostatics at complex interfaces is technologically important, but remains challenging without atomistic simulations. Here we present a machine-learned classical density functional for ionic fluids that combines a symmetry-adapted neural free energy for short-range correlations with explicit long-range electrostatics. Trained on three-dimensional equilibrium densities and bulk correlations of the full-Coulomb restricted primitive model, a single functional transfers to charge-patterned particles and atomically structured electrodes. Around anisotropic charged solutes, it reproduces the ionic structure and mean forces from molecular dynamics, including reversals of the bare electrostatic force. At metal electrodes, self-consistent coupling to metal atoms captures the redistribution of ionic and electrode charge and the loading-dependent capacitance enhancement produced by steps and bumps. Combined with mobilities determined independently from bulk molecular dynamics, the same functional describes the main features of charging dynamics and resolves geometry-dependent spatial relaxation. This framework can be extended to more complex ionic fluids, enabling efficient exploration of how composition and geometry control structure and response.

</details>

### [An informational interpretation of the reverse nonequilibrium molecular dynamics](https://arxiv.org/abs/2611.29174)
*Yuxing Jiao, Mingcheng Yang* · `cond-mat.stat-mech` · arXiv:2611.29174v1 · relevance 0.12

- **In one sentence**: The paper gives an information-thermodynamic (information-reservoir) interpretation of reverse nonequilibrium molecular dynamics, a simulation method for measuring self-diffusivity, and derives an entropy production fluctuation theorem and thermodynamic uncertainty relation for it.
- **In plain words**: Scientists often measure how fast particles spread through a liquid or gas by running computer simulations. One such shortcut, reverse nonequilibrium molecular dynamics, swaps particles between regions in a way that looks artificial and makes a flow appear. This paper explains that trick in terms of information, like a sorting demon that uses knowledge about particles to drive a flow. The authors then check their theory against computer simulations.
- **Why it matters**: The method is already used as an efficient way to compute transport coefficients, so a clear physical explanation of why it works could support its design and use. The link to information thermodynamics and fluctuation theorems is a connection to broader theory, though the text does not show how far that link extends beyond this one scheme.
- **Background needed**: - Transport coefficient: a number describing how quickly something (particles, heat, momentum) moves in response to a gradient, such as self-diffusivity for particle spreading.
- Molecular dynamics: computer simulation that tracks the motion of many atoms or molecules under physical forces.
- Force-flux causality: the usual idea that a gradient (a difference in concentration or temperature) drives a flux (a flow).
- Maxwell demon: a thought experiment in which a sorting agent uses information about particles to move them against their natural direction, linking information and thermodynamics.
- Entropy production: a measure of irreversibility, how much disorder is generated in a process that runs in one direction.
- Fluctuation theorem and thermodynamic uncertainty relation: results saying how likely backward versus forward fluctuations are, and that precision of a flow costs entropy.
- Large deviation functional: a mathematical tool for the probability of rare averages over long times. · level: research-level

<details><summary>Original abstract</summary>

Reverse nonequilibrium molecular dynamics (RNEMD) is an efficient simulation method for determining transport coefficients. In this method, a flux is imposed by a seemingly artificial nonlocal exchange operation and the corresponding thermodynamic gradient is induced as a result, apparently reversing the usual force-flux causality. Although this method is well studied as a simulation technique, developing an information-thermodynamic interpretation of its Maxwell-demon-type operation and the associated apparent reversal of force-flux causality would provide a solid physical foundation for algorithms of this type. Here, we develop an information-reservoir interpretation for a representative RNEMD scheme for determining self-diffusivity. We show that the statistical bias of the information reservoir defines an information affinity that sustains a concentration gradient and a diffusive flux in the steady state. We further derive the linear transport coefficient corresponding to the information affinity in the linear response regime. Using the large deviation functional for the steady-state densities and currents, we also establish a fluctuation theorem for entropy production and the thermodynamic uncertainty relation linking entropy production to the fluctuations of the particle current. Computer simulations are performed to corroborate our theoretical results.

</details>

## Materials science

### [DeepDOSReasoner: Physics-Grounded Reasoning for Density-of-States Prediction and Materials Discovery](https://arxiv.org/abs/2611.29132)
*Yingheng Wang, Francesco Ricci, Zhilong Wang et al.* · `cond-mat.mtrl-sci` · arXiv:2611.29132v1 · relevance 0.12

- **In one sentence**: DeepDOSReasoner is a machine-learning model that predicts electronic and phonon density-of-states spectra directly from crystal structure, using source attention and a continuity-equation transport step that enforces nonnegativity and total-state conservation, and is evaluated on a prospective DFT-validated screen of new materials.
- **In plain words**: Researchers want to know how a material's energy levels are spread out, but computing this with a standard quantum simulation is slow, and many materials in a public database lack it. This paper describes a computer model that predicts these energy-level spectra from a material's atomic arrangement in a fraction of a second. The authors report it was more accurate than the methods they compared against, and that 25 of its top 50 picks for a particular band-gap property were confirmed by new simulations.
- **Why it matters**: Filling in missing spectra for tens of thousands of database entries could speed up searches for materials with useful electronic or thermal properties, such as for solar cells or electronics. The text reports the released predictions but does not show how they perform in real laboratory use, so practical impact remains to be tested.
- **Background needed**: - Density of states (DOS): a count of how many allowed energy levels exist at each energy; it governs how a material conducts electricity, absorbs light, and stores heat.
- Electronic DOS (eDOS) concerns electrons; phonon DOS (phDOS) concerns atomic vibrations.
- Density functional theory (DFT): a standard, costly quantum-mechanical calculation used to compute these spectra.
- Materials Project: a public database of computed material properties, many entries missing these spectra.
- Valence-band (VB) gap: an energy range with no allowed electron states in the valence band, relevant to electronic behavior.
- Conservation and nonnegativity: physical constraints that the predicted spectrum must add up to the correct total number of states and never go below zero.
- Ablation: a test where parts of a model are removed to see whether each part matters. · level: research-level

<details><summary>Original abstract</summary>

Predicting a material's behavior from its atomic structure is a longstanding goal of the physical sciences. The electronic and phonon densities of states (eDOS and phDOS) govern key electronic, optical, vibrational, and thermodynamic properties, yet their calculation using density functional theory (DFT) is costly: about 60% of Materials Project entries lack eDOS and over 80% lack phDOS. Existing crystal-to-spectrum models rely on pooled structural representations and pointwise regression, which blur spectral features and violate total-state conservation. Here we introduce DeepDOSReasoner, a physics-grounded framework that decodes spectra through atom-to-energy source attention and refines the normalized DOS through learned continuity-equation transport, enforcing nonnegativity and total-state conservation by construction. DeepDOSReasoner achieves the highest prediction accuracy across all evaluated metrics for both eDOS and phDOS, recovers element-resolved contributions without supervision, and most reliably identifies rare valence-band (VB) gaps. In a prospective screen of 8,106 uncharted materials validated by new DFT calculations, its predictions remain the most accurate among the methods evaluated, with 25 of its top 50 candidates confirmed as VB-gap materials. Three case studies spanning substituted compounds, photovoltaic chalcogenides, and a high-entropy alloy demonstrate transfer across materials classes. Ablations confirm that both stages are necessary, while the model retains comparable accuracy when trained on only 25% of the data. Predicting spectra in milliseconds enables exhaustive screening; we release predictions filling the missing eDOS for 91,405 and phDOS for 127,768 Materials Project entries. DeepDOSReasoner provides a blueprint for integrating machine learning with physical reasoning toward high-throughput spectral screening and autonomous materials discovery.

</details>

### [Diagnostic Accuracy Is Not Deployment Value: Decision-Aligned Reliability Evaluation for Foundation MLIPs in Materials Discovery](https://arxiv.org/abs/2611.30066)
*Harry Sevi, Joonatan E. M. Laulainen* · `cs.LG` · arXiv:2611.30066v1 · relevance 0.12

- **In one sentence**: The paper argues that standard reliability metrics for foundation machine-learned interatomic potentials (MACE-MP, CHGNet, Orb V3) do not predict whether a reliability intervention improves DFT-based screening of crystal structures, and proposes decision-aligned evaluation instead.
- **In plain words**: Scientists use machine-learning models to quickly estimate which candidate materials are promising, so that only a few need costly quantum-mechanical checks. This paper asks whether making those models more "reliable" by standard measures actually leads to better choices about which candidates to check. The authors found that several common fixes can look successful on their own metric while leaving the final screening decision unchanged or worse.
- **Why it matters**: Materials discovery pipelines spend heavily on expensive simulations, so whether a model fix actually saves that cost matters in practice. The paper's central point, that accuracy or uncertainty scores are not the same as decision value, may also apply to other AI-guided screening tasks, though the text itself only covers materials.
- **Background needed**: - Interatomic potential: a fast machine-learned model that estimates the energy of an atomic arrangement, standing in for slower quantum calculations.
- DFT (density functional theory): the expensive quantum-mechanical calculation used to verify candidates.
- Convex hull / near-hull candidates: a crystal is stable if its energy lies on or near the lower envelope of energies for competing compositions; "near-hull" means close to stable.
- Recall: the fraction of truly promising candidates that the screening procedure correctly keeps.
- Calibration: whether a model's stated uncertainty matches how often it is actually wrong.
- Novelty detection: flagging inputs that differ from the training data, suggesting the model may be unreliable there.
- Foundation model: a large model pretrained broadly, then applied to many tasks. · level: research-level

<details><summary>Original abstract</summary>

In AI-guided materials discovery, machine-learning models increasingly decide which candidate materials should receive expensive first-principles or experimental evaluation. Standard reliability metrics such as uncertainty, calibration, novelty, and ranking accuracy evaluate properties of the predictions, but success on these metrics does not necessarily imply a better downstream screening decision. We study this mismatch for foundation machine-learned interatomic potentials (MACE-MP, CHGNet, Orb V3) used to rank candidate crystal structures before DFT verification. We evaluate three representative reliability interventions (novelty detection, sparse DFT calibration, and chemistry-level ranking audits) using a deployment objective that measures how much DFT can be avoided while maintaining a required recall of near-hull candidates. Across all three, a reliability signal can succeed on its immediate target without improving the final screening decision: novelty detects distribution shift but weakly ranks failure severity; calibration can improve pooled ranking metrics while leaving screening unchanged or degrading it; and sparse audits identify MLIP-chemistry combinations with poor ranking reliability without yielding a robustly beneficial routing policy. A two-oracle analysis further shows that the source of failure depends on the screening decision itself: under formation-energy screening, even perfect knowledge of average ranking reliability can select the wrong model, whereas in the evaluated hull-aligned variant the oracle target becomes decision-aligned but finite-budget audits still fail to realize the value. Reliability should be evaluated relative to the decision it supports: the relevant question is not whether a model is uncertain or inaccurate, but whether acquiring and acting on additional information will improve the final discovery decision enough to justify its cost.

</details>

## Soft matter and polymers

### [Intrinsic volume fraction can decouple from hydrodynamic size in p(NIPAm-co-AA) microgels](https://arxiv.org/abs/2611.28284)
*Peter Edimeh, Howard Chen, Jacinta C. Conrad* · `cond-mat.soft` · arXiv:2611.28284v1 · relevance 0.08

- **In one sentence**: Using capillary viscometry and static and dynamic light scattering, this study tests whether intrinsic volume fraction and hydrodynamic size of p(NIPAm-co-AA) microgels track each other across the acrylic acid pKa and the polymer's volume phase transition, and finds they decouple at high temperature in acidic conditions.
- **In plain words**: Microgels are tiny soft gel particles made of a polymer network that swells or shrinks with temperature and acidity. Researchers often estimate how tightly these particles pack together by assuming their overall size and the amount of polymer inside change in step. This paper checks that assumption for two versions of a temperature- and pH-sensitive microgel, and finds that at low pH and high temperature the size and the viscosity-based volume measures no longer match.
- **Why it matters**: Packing fraction controls how thick suspensions flow, so a wrong estimate could mislead rheology and transport predictions for these materials. The paper suggests that copolymer composition and crosslink density could be used to tune flow through internal structure, though the text does not show this in applied settings.
- **Background needed**: - Microgels: micron-scale cross-linked polymer network particles that swell in water and shrink under certain conditions.
- Hydrodynamic radius (R_h): the effective size a particle appears to have when moving through liquid, measured here by dynamic light scattering.
- Radius of gyration (R_g): a measure of how mass is spread out from the particle's center, from static light scattering; the ratio R_g/R_h hints at internal density distribution (uniform spheres have a known theoretical ratio).
- Intrinsic viscosity and intrinsic volume fraction: how much a dilute suspension thickens, reflecting the effective volume the polymer occupies.
- Crosslinker (methylenebisacrylamide): the chemical that ties the polymer chains together; more crosslinker gives a tighter network.
- pKa of acrylic acid: the pH at which the acid groups become charged; above it (pH 8) they are charged and repel each other, below it (pH 4) they are mostly neutral.
- Volume phase transition: an abrupt shrinking of a gel near a critical temperature (here near the lower critical solution temperature of pNIPAm, about 32 °C for the pure polymer). · level: research-level

<details><summary>Original abstract</summary>

Quantifying the packing fraction of microgels is key to understanding their rheology and transport properties. Often, packing fractions are extrapolated from the hydrodynamic size and intrinsic volume fraction under the assumption that particle size and polymer volume change are proportional. Here, we test this assumption for p(N-isopropylacrylamide-co-acrylic acid) [p(NIPAm-co-AA)] microgels of two crosslinker concentrations (1 wt\% and 7 wt\% methylenebisacrylamide) using capillary viscometry and light scattering (static and dynamic) above and below the pKa of acrylic acid (AA). At pH 8, where AA is fully ionized, the microgels do not undergo a pronounced volume phase transition because electrostatic repulsion hinders thermal collapse, and both measures of hydrodynamic volume are equal. At pH 4, however, p(NIPAm-co-AA) microgels are weakly charged and exhibit a volume phase transition near the lower critical solution temperature of pNIPAm; the magnitude of the size change is greater for the less-crosslinked microgel. Above the volume phase transition temperature, the volume change from hydrodynamic radius decouples from that from viscosity. The ratio of the radius of gyration and hydrodynamic radius R_g/R_h of p(NIPAm-co-AA) microgels at high temperature exceeds the value theoretically predicted for homogeneous spheres and the deviation increases with the extent of crosslinking, suggesting that a non-uniform internal distribution of polymer gives rise to the anomalous decoupling at high temperatures. Our results indicate that care must be taken in extrapolating packing fractions for multi-responsive copolymer microgels, and suggest that copolymer composition and crosslink density may be used to tune bulk properties such as rheology through the internal microstructure.

</details>

### [Dynamical evolution and rheological behavior of a sheared compound vesicle with a highly viscous core: a mesoscale particle-based study](https://arxiv.org/abs/2611.30232)
*A. Lamura* · `cond-mat.soft` · arXiv:2611.30232v1 · relevance 0.05

- **In one sentence**: A two-dimensional mesoscale particle simulation of a compound vesicle (an outer membrane enclosing a fluid annulus and a more viscous inner core) in wall-bounded shear flow, examining how core viscosity and filling fraction change membrane dynamics, inclination, intrinsic viscosity and internal-vesicle motion.
- **In plain words**: This study uses a computer simulation to look at a flexible bubble-like capsule with a second, thicker fluid inside, placed in a flow between walls, as a simple stand-in for a cell that has a nucleus. The authors vary how viscous the inner core is and how much of the space is filled by the inner body. They report that a more viscous core pushes the outer membrane out of a steady rolling-like motion ("tank-treading") at high filling fractions, and that the inner body tends to tumble and move away from the center.
- **Why it matters**: Cells often contain dense internal structures, and this model suggests the inner body can change how the outer membrane deforms and moves under flow. The work is a minimal, two-dimensional model, so its link to real three-dimensional cells is something the text does not establish and should be treated as tentative.
- **Background needed**: - Vesicle: a closed membrane enclosing fluid, used as a model of a cell.
- Compound vesicle: a vesicle with a second vesicle or body inside, leaving a fluid layer (the annulus) between them.
- Shear flow: fluid moving at different speeds in layers, like flow between two plates.
- Tank-treading: a steady state where the membrane circulates around its shape without the shape tumbling.
- Tumbling: the whole body rotating end over end in the flow.
- Filling fraction (φ): how much of the available space the inner body occupies.
- Intrinsic viscosity: a measure of how much a suspension of such bodies thickens the fluid.
- Mesoscale particle-based simulation: a computer method that models fluid and membranes as groups of particles at an intermediate scale. · level: research-level

<details><summary>Original abstract</summary>

We study numerically the dynamics and the rheology of a two-dimensional compound vesicle in wall-bounded shear flow, as a minimal model of a nucleated cell. We consider the configuration in which the annular fluid is iso-viscous with the external one, while the inner core is more viscous. Increasing the core viscosity drives the external vesicle away from steady tank-treading at values $\phi \geq 0.6$. When an internal body is present, the annular fluid partially shields the outer membrane from the viscous core, so that at small filling fractions the external vesicle retains tank-treading with a higher inclination angle and the intrinsic viscosity stays comparatively low. The internal vesicle, by contrast, tumbles and migrates away from the center, and at high $\phi$ this motion couples back to the host, producing intermittent shape excursions of the external membrane. The inner viscous body thus acts as an internal governor of the dynamical state.

</details>

## AI for chemistry and materials

### [RumiFold: Teaching an LLM to Natively Fold Proteins and Reason About Their Function](https://arxiv.org/abs/2611.29444)
*Kevin Lu, David Bau, Wengong Jin* · `cs.LG` · arXiv:2611.29444v1 · relevance 0.19

- **In one sentence**: RumiFold is a pretrained chat-style language model that learns to predict protein 3D structures from its own hidden states and then uses those folded representations to answer natural-language questions about protein function.
- **In plain words**: Researchers asked whether a general-purpose language model, the kind that chats in text, can also learn to predict how a protein folds into its 3D shape. Their model, RumiFold, does this inside its own internal computations and then answers questions about what the protein does. The abstract reports that its folding accuracy is comparable to a dedicated folding model, and that it performs best on certain protein function tasks.
- **Why it matters**: It suggests that protein structure and language-based reasoning could be combined in a single model rather than handled by separate tools. The abstract's claims rest on its own benchmarks, so how well this holds up on wider tasks is not yet clear from the text.
- **Background needed**: - Proteins are chains of amino acids that fold into 3D shapes, and the shape largely determines what they do.
- Protein structure prediction: computationally guessing that 3D shape from the sequence.
- Language models: AI systems trained on text that generate and answer in natural language.
- Hidden states: the internal numerical values a model computes at each step, here tied to individual amino acid positions ("per-residue").
- Gene Ontology: a standard vocabulary of labels describing protein functions, used to score function prediction.
- Causal interventions: experiments that alter internal parts of a model to test whether they actually drive its output. · level: research-level
- Matched keywords: protein

<details><summary>Original abstract</summary>

Can we teach a general-purpose language model to fold proteins? And if so, what does learning to fold enable beyond structure prediction itself? We introduce RumiFold, a pretrained chat model that learns to predict protein structures directly from its own hidden states. RumiFold processes proteins through repeated folding passes, then uses these folded representations to answer questions in natural language. It achieves folding accuracy comparable to dedicated single-representation models such as SimpleFold, alongside state-of-the-art performance on Gene Ontology protein function prediction and free-text function description. We find that folding pretraining organizes the model's hidden states around protein function, creating an internal per-residue workspace that is biologically grounded. Causal interventions show that this folded workspace links structure and language when RumiFold predicts function, providing rich representations for biomolecular reasoning. We see RumiFold as a step toward native biomolecular intelligence: where protein-based computations and language-based reasoning become integrated capabilities of general-purpose language models. Code, data, and models are available at: https://rumifold.baulab.info

</details>

### [Auditing two-stage MS/MS molecular retrieval on MassSpecGym v1.5: Reranking gains, candidate priors and spectrum dependence](https://arxiv.org/abs/2611.28096)
*Jiaqi Xue, Yutong Wu, Qiang Zhang* · `physics.chem-ph` · arXiv:2611.28096v1 · relevance 0.19

- **In one sentence**: An audit of a two-stage deep-learning retrieval system that ranks candidate molecules for tandem mass spectra on the MassSpecGym v1.5 benchmark, separating genuine spectrum-based signal from candidate priors, replicate spectra, precursor-mass effects and training-set overlap.
- **In plain words**: The paper looks at how computers try to identify an unknown chemical from its mass spectrum, a fingerprint made by breaking molecules into fragments and weighing them. The authors build a two-step system: first a shortlist of likely candidate molecules, then a reranker that reorders them using mass-consistency checks. They then test how much of the reported accuracy really comes from the spectrum itself versus shortcuts, such as the candidate list or the molecules' mass.
- **Why it matters**: Identifying molecules from mass spectra is a bottleneck in chemistry and metabolomics, so benchmark claims about it matter for how much trust to place in such tools. The paper's main value is its caution: it shows that a sizable share of the score can come without reading the spectrum at all, which is useful for anyone designing fair evaluations in this area.
- **Background needed**: - Tandem mass spectrometry (MS/MS): an instrument technique that breaks molecules into fragments and records their masses, producing a "spectrum."
- Molecular retrieval: picking the correct molecule from a database of candidate structures that matches a spectrum.
- Recall@k: the fraction of test spectra where the correct molecule appears in the top k ranked candidates.
- Two-stage retrieval: a fast first pass that shortlists candidates, followed by a slower reranker that reorders them.
- Fingerprints: numerical codes describing which structural features a molecule contains.
- Adduct and precursor mass: how the measured ion was formed and its total mass, both used to filter feasible candidates.
- Candidate priors: biases where some molecules are easier to guess regardless of the spectrum, e.g. because they appear often in training data.
- Benchmark audit: a check of whether reported gains hold up under control experiments. · level: research-level
- Matched keywords: molecule, molecular

<details><summary>Original abstract</summary>

Two-stage retrieval of molecular structures from tandem mass spectra (MS/MS) can benefit from candidate reranking, but benchmark gains may also reflect candidate priors, replicate spectra, precursor mass, and training-set coverage. We audit a two-stage retrieval system on the official MassSpecGym v1.5 split (17,556 test spectra). A data-safe DreaMS encoder and composite molecular fingerprints provide an initial shortlist; a support-gated reranker combines pair scores, candidate-relative peak coverage, and mass-feasibility features. The final system achieves 31.05% Recall@1, a 10.05-point gain over its Stage 1 ensemble, while preserving its 72.62% Recall@20. Replacing the query spectrum with one from a different molecule matched on adduct and precursor mass reduces Recall@1 by 9.0 points (15.3 points under molecule-balanced weighting); nevertheless, a training-mean spectrum retains 13.75% Recall@1, indicating substantial spectrum-independent signal. Mass-feasibility features improve Recall@1 beyond score and coverage controls, while learned peak-fragment similarities do not outperform constant coverage. Errors cluster by molecule, and removing close training neighbours causes a large decline in Stage 1 shortlist recall among initially well-covered molecules. We conclude that candidate-relative mass-feasibility evidence improves front-rank retrieval and spectrum dependence, but does not establish learned structural discrimination or eliminate candidate priors. Evaluation should separately assess shortlist reachability, spectrum dependence, and molecule-level generalization.

</details>

## Biochemistry

### [Albumin alleviates pressure overload-induced heart failure by improving mitochondrial homeostasis via PKA-LKB1-AMPK axis](https://www.biorxiv.org/content/10.64898/2026.11.21.768247v1)
*AN, Q.; Ma, B.; Fu, Y. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.21.768247 v1 · relevance 0.06

- **In one sentence**: In a mouse model of pressure-overload heart failure, recombinant mouse serum albumin improved cardiac function and mitochondrial energy metabolism, reportedly via a PKA-LKB1-AMPK signalling axis, and albumin-knockout mice fared worse.
- **In plain words**: Heart failure is a condition where the heart cannot pump blood well, and patients with low levels of the blood protein albumin tend to do worse. This study tested in mice whether albumin actually helps the heart, by giving them a purified form of mouse albumin after a surgery that squeezes the aorta and strains the heart. Treated mice had better heart pumping, less enlargement and scarring, and less inflammation, and the authors link this to improved energy production inside heart cells.
- **Why it matters**: Low albumin is a known warning sign in heart failure, but it was unclear whether albumin itself is protective; this work suggests it may be a treatment target, though the evidence is from mice and a single model. It may connect to how energy supply in heart muscle cells is maintained, but the text alone does not show how well the findings transfer to people.
- **Background needed**: - Heart failure: the heart pumps too weakly to meet the body's needs; often follows long-term strain such as high blood pressure.
- Pressure overload / transverse aortic constriction (TAC): a surgery that narrows the aorta in mice to mimic this strain.
- Serum albumin: the most abundant protein in blood, which carries molecules and helps maintain fluid balance.
- Knockout (Alb-/-) mice: animals genetically engineered to lack a gene, here the albumin gene, to test its role.
- Mitochondria: the cell's power plants that produce energy, partly by burning fats and sugars.
- Fatty acid oxidation: breaking down fats to release energy; a key fuel for the heart.
- AMPK, LKB1, PKA: cellular signalling proteins that sense energy status and regulate metabolism.
- Phenylephrine (PE): a drug used in the lab to make heart muscle cells enlarge, mimicking hypertrophy. · level: research-level

<details><summary>Original abstract</summary>

Aims Heart failure (HF) is a global health challenge due to its high incidence, mortality, and socioeconomic burden. Despite medical advancements, HF prognosis remains poor, highlighting the need for enhanced understanding and treatment strategies. Serum albumin, a key circulatory protein, has gained attention as a biomarker in cardiovascular diseases. Low serum albumin levels are linked to HF incidence, progression, and prognosis, suggesting its regulatory role, though mechanisms remain unclear. This study aimed to elucidate the role of serum albumin in HF pathogenesis and investigate its potential therapeutic effects. Methods and results A mouse model of pressure overload-induced HF was established via transverse aortic constriction (TAC). Serum albumin levels were significantly decreased in HF mice. Administration of recombinant mouse serum albumin (rMSA) effectively restored serum albumin concentrations, improved cardiac systolic function, alleviated cardiac hypertrophy and fibrosis, and reduced inflammatory responses, collectively attenuating disease progression. In contrast, albumin-knockout (Alb-/-, AKO) HF mice displayed aggravated pathological manifestations compared with wild-type (WT) controls, whereas rMSA supplementation markedly ameliorated these impairments. In vitro experiments demonstrated that rMSA protected against phenylephrine (PE)-induced hypertrophy in cardiomyocytes. To elucidate the underlying mechanism, transcriptomic analyses of cardiac tissues revealed that albumin played a critical role in improving mitochondrial homeostasis. Experimental validation further demonstrated that albumin activated the PKA-LKB1-AMPK signaling axis, leading to improved mitochondrial respiratory function and oxidative phosphorylation, as well as enhanced mitochondrial quality control. These changes promoted fatty acid oxidation and optimized energy metabolism, thereby reversing the energy imbalance underlying cardiac dysfunction. Conclusion Our study suggests that serum albumin exerts a protective effect in HF by improving mitochondrial dysfunction and energy metabolism disorders, thus reversing energy imbalance and mitigating disease progression. These results support recombinant serum albumin as a promising therapeutic for HF, with its mechanism involving the critical improvement of mitochondrial homeostasis.

</details>

### [A Shifting Landscape: Deconvoluting the Effect of Mg2+ and pH on Base Triple Formation in 7SK SL-1](https://www.biorxiv.org/content/10.64898/2026.11.19.767663v1)
*Fallon, L.; Venkatesh, H.; Jones, A.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.19.767663 v1 · relevance 0.04

- **In one sentence**: A combined simulation, NMR and SAXS study of how Mg2+ ions and pH reshape the base-triple network in the 7SK SL-1 RNA hairpin, which helps it bind the HEXIM protein.
- **In plain words**: This paper looks at a small RNA molecule, 7SK, that helps control how a cell's main gene-copying enzyme works. The authors ask how the acidity of the surroundings and the presence of magnesium ions change the way one part of this RNA folds and holds together. They combine computer simulations, magnetic-resonance measurements and X-ray scattering, and report that pH and magnesium each shift the molecule's shape in different ways, favoring the formation of stabilizing base triples.
- **Why it matters**: Base triples are small three-way contacts between RNA building blocks that help set the shape the RNA presents to its partner protein, HEXIM. The authors suggest that this shape-shifting could be a way for the cell to tune the RNA's grip on HEXIM and thereby the output of RNA polymerase II, though the text presents this as a possibility rather than a demonstrated mechanism.
- **Background needed**: - RNA is a chain of four chemical letters that can fold into 3D shapes, much like a protein.
- 7SK is a non-coding RNA that regulates transcription, the copying of genes into messenger RNA, by RNA polymerase II.
- HEXIM and P-TEFb are proteins that 7SK interacts with to control transcription elongation.
- A stem-loop is a hairpin-shaped RNA fold; SL-1 is the first such hairpin in 7SK.
- Base triples are three-way hydrogen-bonded contacts among RNA bases that stabilize particular folds.
- Mg2+ (magnesium ions) and pH (acidity) affect how charged RNA folds and holds together.
- Methods: molecular dynamics (computer simulation of atomic motion), free energy calculations, NMR (nuclear magnetic resonance spectroscopy) and SAXS (small-angle X-ray scattering, which measures overall molecular shape in solution). · level: research-level

<details><summary>Original abstract</summary>

The small-nuclear RNA (snRNA) 7SK is essential for regulating the transcription of genes by RNA polymerase II through its interactions with Hexamethylene Bisacetamide Inducible Protein (HEXIM) and positive transcription elongation factor b (P-TEFb). High-resolution structures of 7SK stem-loop 1 (SL-1) reveal the presence of several base triples that coordinate the interaction with HEXIM. However, different high-resolution structures of 7SK SL-1 exhibit different conformations, each with unique base triple configurations. Previous NMR studies show that the conformation of 7SK SL-1 is sensitive to changes in pH and Mg2+ concentration. However, the exact mechanism by which Mg2+ and pH influence the formation and stability of base triples in 7SK SL-1 at an atomic level remains unclear. We combine molecular dynamics (MD) simulations, free energy calculations, nuclear magnetic resonance (NMR), and small angle X-ray scattering (SAXS) to conduct a detailed investigation into the mechanism and dynamics of base triple formation in 7SK SL-1, and deconvolute the effects of pH and Mg2+. We find that the conformational landscape of 7SK SL-1 dramatically changes depending on the pH and presence of Mg2+, and that pH and Mg2+ act orthogonally to favor the formation of base triples. We discuss how the dynamic behavior of the base triples may provide a means for 7SK to regulate its interactions with HEXIM, modulating the transcriptional output of RNA polymerase II.

</details>

## Pharmacology and drug discovery

Nothing notable this time.

## Computational and systems biology

### [Microbiome complexity shapes host transcriptional networks across the ileum-liver axis](https://www.biorxiv.org/content/10.64898/2026.11.16.767119v1)
*Halkhoree, A. C.; Grannell, A.; Pearson, C. et al.* · `systems biology` · bioRxiv doi:10.64898/2026.11.16.767119 v1 · relevance 0.08

- **In one sentence**: Transcriptomic survey of ileal (terminal small intestine) gene expression in germ-free, gnotobiotic 12-strain (MM12) and specific-pathogen-free mice, asking how microbiome complexity reshapes co-expression networks across the ileum-liver axis.
- **In plain words**: The gut is home to trillions of microbes, and they are known to influence the gut and the liver. This paper looks at the last part of the small intestine, the terminal ileum, and asks how much the microbial community changes which genes the gut tissue switches on and off. The authors compared mice with no microbes, mice with a simple community of 12 defined bacterial strains, and mice with a normal full microbiota, with 15 mice in each group.
- **Why it matters**: Understanding how microbes tune host gene activity in the gut could help explain links between the intestine, bile acid handling, immunity and liver function. The text provided is only the introduction and study design, so it does not show what the authors actually found; the significance of any results cannot be judged from it.
- **Background needed**: - Transcriptome: the set of gene activity levels measured in a tissue sample, read out as RNA.
- Co-expression network: a map of genes whose activity rises and falls together, often suggesting shared regulation.
- Germ-free (GF) mice: raised with no microbes at all, used as a baseline.
- Oligo-Mouse-Microbiota-12 (MM12): a defined community of 12 bacterial strains, a simplified stand-in for a microbiome.
- Specific pathogen free (SPF): conventional lab mice with a normal, diverse microbiota but no known pathogens.
- Ileum-liver axis: the two-way communication between the lower small intestine and the liver, via immune cells and molecules such as bile acids.
- Bile acids: digestive molecules made by the liver, modified by gut bacteria. · level: research-level

<details><summary>Original abstract</summary>

The microbiome plays an increasingly recognised role in development, metabolism and immunity across all segments of the small and large intestine, as well as more distant organs such as the liver. In the terminal ileum - a key site of nutrient absorption - the presence of microbes dictates the development of secondary lymphoid structures (Peyers patches), mediates bile acid metabolism, and impacts absorption. In part, coordinated regulatory networks in the gut impact liver function and immunity through gut-liver connectivity and the movement of immune cells and bioactive small molecules that includes bile acids and other bacterial metabolites. We aimed to examine the extent of microbiome involvement in ileal transcription, where subtle changes in co-expression networks can be tuned by microbiome diversity, composition and function. We surveyed ileal transcriptomes across mouse models which vary in microbiome complexity ranging from germ-free (GF, n = 15), the Oligo-Mouse-Microbiota-12 (MM12, n = 15), and specific pathogen free (SPF, n = 15).

</details>

### [A2Holo: Dual-Stream Flow Matching of 3D Structure and a Protein Language Model for Conformational Transition Prediction](https://www.biorxiv.org/content/10.64898/2026.11.20.768033v1)
*Kim, D.; Kim, H.; Sim, J. et al.* · `bioinformatics` · bioRxiv doi:10.64898/2026.11.20.768033 v1 · relevance 0.08

- **In one sentence**: A2Holo uses deterministic flow matching between apo and holo protein structures, with a dual-stream joint attention design that borrows from in-context image generation and fuses residue-aligned protein language model embeddings with 3D structure.
- **In plain words**: Proteins often change shape when a drug-like molecule binds them, and drug designers would like to predict the bound shape from the unbound one. This paper proposes a model, A2Holo, that learns to move directly from the unbound structure to the bound structure instead of generating shapes from random noise. The authors report that it reaches the lowest median structural error among the methods they compared on a standard benchmark, without needing the ligand as input.
- **Why it matters**: Predicting the bound shape of a protein from its unbound form matters for structure-based drug discovery, so a deterministic method that does not rely on ligand input could be useful if the results hold up. The paper also inspects the internal attention of the model to see which residues it attends to, which may offer an interpretable view of how sequence and structure information are combined; the text alone does not show how far that interpretation generalises.
- **Background needed**: - Apo vs holo: the unbound (apo) and ligand-bound (holo) forms of a protein.
- Conformational change: a protein shifting its 3D shape, often at a few flexible regions.
- Flow matching: a way to train a model to transform one structure smoothly into another along a path.
- Protein language model: a neural network trained on protein sequences whose embeddings capture chemical and evolutionary patterns.
- Joint attention: a mechanism letting two data streams (here sequence and structure) exchange information.
- RMSD and TM-score: measures of how far a predicted 3D structure is from the true one (lower RMSD and higher TM-score are better).
- Stochastic sampling: generating several outputs with randomness; the paper compares its single deterministic output against the best of 10 samples from baselines. · level: research-level

<details><summary>Original abstract</summary>

Modelling a ligand-bound holo conformation from a ligand-free apo conformation is essential in structure-based drug discovery. We present A2Holo, which casts apo-to-holo prediction as flow matching between two experimental structures rather than generation from noise. It transplants the dual-stream joint attention of in-context image generation to residue-aligned protein language model embeddings and structure. Without ligand conditioning or stochastic sampling, A2Holo's single deterministic trajectory reaches a median C RMSD of 0.809 [A] on the D3PM benchmark, the lowest among existing methods. Its TM-score exceeds even the best of 10 samples from every stochastic baseline on at least 144 of 150 pairs. Beyond performance, we directly measure the transplanted multimodal mechanism itself. Because sequence and structure are residue-aligned, its joint attention can be measured at residue resolution and tested for reproducibility across independently trained model variants. Within the structure stream, the attention a residue receives recovers moving residues better than the attention it emits, and this asymmetry is learned. A2Holo demonstrates a successful multimodal transplant from in-context image generation to protein conformational change, with strong deterministic apo-to-holo prediction. It also provides a quantitative account of how that mechanism organises residue-aligned sequence and structure around the residues that move.

</details>

## Neuroscience

### [Investigating Motor Skill Acquisition in Mice and Humans: Towards A Cross-Species Paradigm](https://www.biorxiv.org/content/10.64898/2026.11.20.768070v1)
*Hille, M.; Justus, L. C.; Zocher, S. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.20.768070 v1 · relevance 0.06

- **In one sentence**: A cross-species study that uses a matched chopstick grasping task in mice and humans, with structural and quantitative MRI before, during and after training, to compare early motor-learning brain changes.
- **In plain words**: Researchers wanted a way to link brain scans of people learning a skill to the cell-level changes seen in animal studies. They built a chopstick-grasping task for humans that mirrors a reaching task used with mice, then scanned trained and untrained mice and men over time. Mice showed shrinking volume in the motor area of the brain on the side opposite the trained hand, while humans showed no reliable volume change but did show signs of changed tissue properties in a similar region.
- **Why it matters**: It offers a possible bridge for translating non-invasive human brain imaging into findings that can be tested in animals at the cellular level. The text itself says it is unclear whether the changes in the two species share a common biological mechanism, so the link is a starting point rather than a established result.
- **Background needed**: - MRI (magnetic resonance imaging) is a non-invasive scan that measures brain structure and tissue properties.
- Gray matter volume is the amount of brain tissue made of nerve cell bodies, measured as size of a region.
- Motor cortex is the brain area that plans and controls movement; the contralateral side controls the opposite hand.
- Myelin is the fatty insulation around nerve fibers; quantitative MRI measures such as MTsat and R1 are sensitive to it, though they do not measure it directly.
- Single-pellet reaching task: a standard test in which rodents reach for and grasp a small food pellet.
- Cross-species research compares the same kind of process in different animals, here mice and people. · level: research-level

<details><summary>Original abstract</summary>

Relating non-invasive observations of human brain plasticity to cellular processes identified in animal models remains a major challenge in neuroscience. We address this challenge by introducing a paradigm for studying motor skill acquisition across species. We designed a human chopstick grasping task modeled after the rodent single-pellet reaching task, resulting in a comparable sequence of reach-to-grasp movements across species. We studied 48 young adult male C57BL/6N mice and 71 young men, comparing trained groups with untrained controls. In both mice and humans, structural magnetic resonance imaging (MRI) was performed before, during, and after motor training. The functional form of behavioral performance gains on the trained task was highly similar across species. In trained compared to control mice, analysis of the early learning interval revealed decreases in regional volume in contralateral primary motor and forelimb somatosensory cortices, with greater volume reductions in primary motor cortex associated with better reaching performance. In humans, performance gains transferred to other chopstick tasks but not to general dexterity, and no reliable changes in gray matter volume were observed. Quantitative MRI, however, revealed early training-related changes in tissue-sensitive measures, including increases in magnetization transfer saturation (MTsat) and longitudinal relaxation rate (R1) in contralateral motor and frontal regions, potentially reflecting an increase in intracortical myelin. Thus, early structural changes in the contralateral motor cortex were detected in both species, but the degree to which these changes reflect a common biological mechanism is unclear. We conclude that the present cross-species paradigm provides a viable starting point for studying brain plasticity across species. Future work needs to relate macroscopic structural changes more directly to cellular processes by applying longitudinal microscopic imaging and MRI in the same animals.

</details>

### [Sex differences in the effects of enhanced adult hippocampal neurogenesis on pattern discrimination and Intellicage spatial learning in Bax-knockout mice](https://www.biorxiv.org/content/10.64898/2026.11.23.768231v1)
*Tunc-Ozcan, E.; Rodriguez, A. M.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.23.768231 v1 · relevance 0.05

- **In one sentence**: In mice with Bax genetically deleted to boost survival of newborn hippocampal granule cells, enhanced adult neurogenesis produced sex- and task-dependent changes in Intellicage place/reversal learning and an A/B context discrimination task, only partly matching the hypothesis that males would benefit more.
- **In plain words**: Scientists asked whether making more new brain cells survive in the memory region of the brain (the hippocampus) helps learning equally in male and female mice. They used a genetic change that stops newborn cells from self-destructing, then tested the mice on several learning tasks. The benefits were uneven: they depended on sex, the task, and the day of testing.
- **Why it matters**: It matters because it suggests that a single brain manipulation may not help males and females in the same way, which is relevant to how sex is handled in neuroscience studies of memory. The text does not establish how these mouse findings would translate to people, so that link remains uncertain.
- **Background needed**: - Adult hippocampal neurogenesis: the birth of new nerve cells (dentate granule cells) in the hippocampus, a region involved in memory and navigation in adult brains.
- Bax: a pro-apoptotic gene that drives programmed cell death; knocking it out in newborn cells lets more of them survive.
- Conditional knockout: a genetic change switched on only in certain cells or at certain times, so the effect is targeted.
- tdTomato: a fluorescent marker used to label and count the newborn cells.
- IntelliCage: an automated home-cage system where mice perform learning tasks by visiting corners and licking sensors, without handling by researchers.
- Place learning and reversal learning: learning a rewarded location, then learning a new one after the rule changes.
- A/B context discrimination: telling apart two similar environments or patterns.
- Results are mixed and described only briefly in the source; no effect sizes or statistics are given here. · level: research-level

<details><summary>Original abstract</summary>

Adult hippocampal neurogenesis has been implicated in learning and memory. Although increasing neurogenesis has been associated with improved spatial learning and pattern discrimination, whether these benefits differ between male and female mice remains unclear. The goal of this study was to see if increasing adult hippocampal neurogenesis improves learning in male and female mice, and whether the benefit is the same in both sexes. We used conditional deletion of the pro-apoptotic gene Bax to increase the survival of newborn dentate granule cells. Male and female BAX knockout (KO) and wild-type (WT) mice were tested in Intellicage place learning and reversal learning tasks, and an A/B context discrimination task. BAX KO mice had more tdTomato-positive newborn dentate granule cells than BAX WT mice, with no significant effect of sex. During Intellicage adaptation, there were no differences between genotypes or sexes in total visits and licks. During place learning, male mice had a higher percent correct response than female mice, while female mice showed increases in licks and correct visits from day 1 to day 4. BAX KO mice made more visits overall but had a lower percent correct response than BAX WT mice on day 4. During reversal learning, male BAX KO mice showed a decrease in visits and had fewer visits with a lick than male BAX WT mice on day 4. In the A/B task, male BAX KO mice had higher discrimination scores than male BAX WT mice on day 5, while female BAX KO mice showed an initial advantage over female BAX WT mice. These results partially support our hypothesis that increasing neurogenesis would benefit male mice more. Overall, increasing the survival of newborn dentate granule cells does not improve learning in the same way across sexes and tasks.

</details>

## Genetics and genomics

### [The 'near T2T' Canton-S assembly is inconsistent with other Canton-S genomes](https://www.biorxiv.org/content/10.64898/2026.11.19.767897v1)
*Emerson, J. J.* · `genomics` · bioRxiv doi:10.64898/2026.11.19.767897 v1 · relevance 0.08

- **In one sentence**: A commentary argues that the recently published "near T2T" genome assembly of the Drosophila Canton-S strain differs from three other independently sequenced Canton-S assemblies by an amount comparable to differences between distinct strains, raising doubts about its genetic identity.
- **In plain words**: Canton-S is a fruit fly lineage that scientists have used for decades as a standard reference animal. A newly published, very high-quality map of its genetic code (the "near T2T" assembly) is meant to give the research community a better reference, but this short comment says that map does not match three other independent maps of the same strain. The author concludes that the mismatch is about as large as the differences seen between genuinely different fly strains, so the new map's identity is in question.
- **Why it matters**: Many fly studies, including behavior and trait-mapping work, rely on Canton-S as the baseline, so whether a reference genome really represents that strain affects how results are interpreted and reused. The text does not show how the comparison was done in detail, so the strength of the claim rests on the author's analysis, which readers should check against the full paper.
- **Background needed**: - Drosophila melanogaster is the common fruit fly, a major model organism in genetics.
- A "strain" is a line of flies kept inbred so members are genetically very similar; "wild-type" means a standard reference line.
- A genome assembly is a reconstructed, letter-by-letter sequence of an organism's DNA.
- "T2T" (telomere-to-telomere) means an assembly covering complete chromosomes end to end, including hard-to-sequence repeats; "near T2T" means nearly complete.
- Comparing independent assemblies of the same strain is a way to check whether a reference is accurate and represents the intended line. · level: intermediate

<details><summary>Original abstract</summary>

Canton-S is among the most widely used Drosophila melanogaster strains, underlying substantial community infrastructure, including serving as a wild-type strain for: genetics studies; studying phenotypes, especially in behavioral studies; and complex trait mapping studies among many others. The recent 'near T2T' assembly of Canton-S (LIU et al.) is presented as delivering modern sequencing and assembly quality to the Drosophila community via this important strain. I find that this assembly is inconsistent with three other independently sequenced Canton-S genome assemblies on a magnitude comparable to differences between distinct strains, raising concerns about its genetic identity that the community should consider when choosing whether to adopt it as a resource.

</details>

### [Genomics of the diversification of Heliconius cydno (Lepidoptera: Nymphalidae) in northern South America: geographic and phenotypic patterns](https://www.biorxiv.org/content/10.64898/2026.11.20.768178v1)
*Arias Cardenas, A.; Rueda-M, N.; Arias, C. F. et al.* · `genomics` · bioRxiv doi:10.64898/2026.11.20.768178 v1 · relevance 0.08

- **In one sentence**: Whole-genome analysis of 133 Heliconius cydno butterflies across Central and northern South America, testing how Andean mountain uplift, geography and introgression shaped its wing-pattern diversification and identifying ivory:mir-193 as the locus behind the hindwing white band.
- **In plain words**: This study looks at a group of colourful, toxic-tasting butterflies that have split into many local forms across Central and northern South America. The researchers sequenced the complete genomes of 133 butterflies to trace how these forms are related and how mountains and geography shaped their spread. They also pinpointed a specific genetic region that controls a white band on the back wings and found signs that this trait passed into a related species.
- **Why it matters**: The work shows how geography, gene flow between species and a few key genes can together drive fast evolutionary change in visible traits. It may matter for understanding how warning-colour mimicry rings form, though the text does not establish broader implications beyond these butterflies.
- **Background needed**: - Heliconius are tropical butterflies known for warning colours (aposematism) that signal toxicity to predators.
- Mimicry: unrelated or related species evolve similar patterns so predators learn to avoid them as a group.
- Subspecies are local geographic forms of one species; monophyletic lineages are groups that all descend from a single common ancestor.
- Andean orogeny: the uplift of the Andes mountains, which can split populations and shape where species live.
- Introgression: transfer of genes between species through occasional interbreeding.
- Cis-regulatory elements: DNA stretches that switch genes on or off, rather than encoding proteins; mir-193 is a small RNA molecule that regulates gene activity.
- Whole-genome sequencing reads the full genetic code of each individual, allowing comparisons across populations. · level: research-level

<details><summary>Original abstract</summary>

The interplay between natural selection, gene flow, and geography is a key driver of population differentiation. This study investigates their influence on the recent adaptive radiation of Heliconius cydno, a mimetic and aposematic butterfly with striking variation in wing color pattern across its distribution in Central and northern South America. The genetic basis of this phenotypic diversity has a modular architecture, whereby a few key genes and cis-regulatory elements control differences among morphotypes. Using whole-genome sequences from 133 individuals representing all subspecies of H. cydno, we investigated (1) the role of Andean orogeny in its diversification and (2) the genetic basis of the variation in the hindwing white submarginal band, which to date, had remained unknown. First, we found that five of the fourteen described subspecies correspond to distinct monophyletic lineages and well-defined genetic clusters that originated in northwestern South America and later expanded into Central America and the Colombian inter-Andean valleys. Second, we observed signatures of genetic structure that were consistent with geographic patterns, particularly those associated with the inter-Andean region and Gorgona Island. Third, we identified ivory:mir-193 as the locus underlying variation in the white submarginal band on the hindwing. We also detected evidence of introgression suggesting that this trait was likely transferred from H. cydno to H. melpomene, contributing to the establishment of a novel mimicry ring with H. erato. Altogether, these findings highlight the roles of geography, genomic architecture, and introgression in the diversification of H. cydno.

</details>

## Cell and molecular biology

### [Smyd1 regulates H3K4me3 to support adaptive fatty acid oxidation in the adult heart during lipid overload](https://www.biorxiv.org/content/10.64898/2026.11.18.763125v1)
*Mukai, R.; Oka, S.; Sung, E.-A. et al.* · `cell biology` · bioRxiv doi:10.64898/2026.11.18.763125 v1 · relevance 0.10

- **In one sentence**: In mice fed a high-fat diet, the muscle-specific histone methyltransferase Smyd1 shows a transient rise in cardiomyocytes that supports fatty acid oxidation genes via an interaction with PPARα, and cardiac-specific Smyd1 heterozygous loss worsens heart dysfunction and survival.
- **In plain words**: Obesity and metabolic syndrome raise the risk of heart failure, partly because heart muscle cells stop burning fat efficiently. This study looked at how the heart normally adapts to a high-fat diet in mice, focusing on a protein called Smyd1 that helps control which genes are switched on. The authors found that Smyd1 and a related chemical mark on DNA packaging rise early on a high-fat diet, then return to normal, and that mice with less Smyd1 in the heart developed worse heart damage and died sooner.
- **Why it matters**: It points to a possible way the heart keeps its fuel-burning flexibility under fat overload, which is relevant to obesity-related heart disease. The link between Smyd1 and PPARα is described only as a potential mechanism based on co-immunoprecipitation, so the proposed pathway still needs confirmation and it is not yet clear it would translate into treatment.
- **Background needed**: - Fatty acid oxidation (FAO): the process by which cells break down fats to produce energy; the heart relies on it heavily.
- Lipid overload: having more fat in the blood and tissues than the body can comfortably handle, as in a high-fat diet.
- Histone methyltransferase: an enzyme that adds small chemical tags (methyl groups) to histones, the protein spools DNA wraps around, altering which genes are active. H3K4me3 is one such tag, generally linked to active genes.
- PPARα: a nuclear receptor (a protein that switches genes on or off in response to fats) that drives many fat-burning genes.
- Co-immunoprecipitation: a lab method that pulls a protein out with its binding partners to test whether two proteins physically interact.
- Heterozygous knockout: mice carrying one working and one disabled copy of a gene, so the protein level is reduced but not absent.
- Single-cell RNA sequencing: a method that measures gene activity in individual cells, here used to find which heart cell types changed. · level: research-level

<details><summary>Original abstract</summary>

Obesity and metabolic syndrome are major risk factors for heart failure, and impaired fatty acid oxidation (FAO) is a key contributor to metabolic dysfunction in obesity-related cardiomyopathy. However, how the heart maintains FAO and adapts to chronic lipid overload remains poorly understood. Here, we identify SET and MYND domain-containing protein 1 (Smyd1), a muscle-specific histone methyltransferase, as an early compensatory regulator of cardiac metabolism in response to lipid overload. In wild-type mouse hearts, high-fat diet (HFD) feeding induced transient increases in Smyd1 expression and H3K4me3 levels during the early-to-mid phase of metabolic stress, both of which returned to baseline levels during prolonged HFD exposure. Single-cell RNA sequencing further revealed that this adaptive increase in Smyd1 expression occurred predominantly in cardiomyocytes. In contrast, cardiac-specific Smyd1 heterozygous knockout mice exhibited accelerated cardiac dysfunction, left ventricular dilation, increased myocardial fibrosis, and reduced survival following HFD feeding. Mechanistically, Smyd1 deficiency impaired the adaptive upregulation of key FAO-related genes and reduced cardiac FAO activity. Furthermore, co-immunoprecipitation analysis revealed an interaction between Smyd1 and peroxisome proliferator-activated receptor alpha (PPAR), suggesting a potential mechanism by which Smyd1 supports FAO gene expression. Taken together, these findings identify Smyd1 as an early compensatory regulator that supports FAO-dependent metabolic adaptation and protects the heart against lipid overload-induced cardiac dysfunction. This adaptive mechanism, involving H3K4me3 regulation and the Smyd1-PPAR interaction, may provide potential therapeutic targets for therapeutic strategies aimed at preserving cardiac metabolic flexibility in obesity-related cardiomyopathy.

</details>

### [Targeted protein depletion in quiescent fission yeast cells using an auxin-degron system](https://www.biorxiv.org/content/10.64898/2026.11.20.767346v1)
*Le Collen, D.; Vazquez-Bolado, A.; Wu, P.-Y. J.* · `cell biology` · bioRxiv doi:10.64898/2026.11.20.767346 v1 · relevance 0.09

- **In one sentence**: In nitrogen-starved fission yeast, a quiescent (dormant, non-dividing) state, the authors find that analog-sensitive kinase inhibition with ATP analogs is unsuitable because the analog acts as a nitrogen source and triggers cell cycle re-entry, whereas an auxin-inducible degron allows rapid, reversible protein depletion in quiescent cells.
- **In plain words**: Cells can enter a dormant, non-dividing state and wake up again later, but it is hard to study the proteins needed for this state because switching them off often also kills the cell. This paper tests two common switch-off methods in yeast that have been starved of nitrogen, a standard model of dormancy. One method, which blocks engineered enzymes with a modified fuel-like molecule, turned out to feed the cells and pushed them to start dividing again, so it does not work here. The second method, which tags a protein so that a plant hormone (auxin) marks it for destruction, did remove proteins quickly and reversibly in dormant cells.
- **Why it matters**: Researchers need reliable ways to switch off essential proteins in dormant cells, since many processes from stress survival to development depend on this state. The text presents the auxin-degron approach as a practical tool for this, and the finding that one common method fails in quiescent cells is a useful warning for others; broader applicability beyond this yeast model is not shown in the text.
- **Background needed**: - Quiescence: a reversible resting state in which cells stop dividing but can resume growth when conditions improve.
- Fission yeast (Schizosaccharomyces pombe): a single-celled organism widely used to study the cell cycle; nitrogen starvation induces quiescence.
- Conditional inactivation: switching off a gene or protein on demand, useful for proteins essential to survival.
- Analog-sensitive kinase: an engineered enzyme (kinase) that can be blocked by a synthetic ATP-like molecule that normally would not affect it.
- Auxin-inducible degron: a short protein tag that, in the presence of the plant hormone auxin, causes the tagged protein to be broken down by the cell's own machinery.
- Cell cycle re-entry: a quiescent cell beginning to divide again. · level: intermediate

<details><summary>Original abstract</summary>

Quiescence is a reversible, non-proliferative cellular state in which cells can remain for extended periods of time while retaining the ability to re-enter the cell cycle upon exposure to favorable conditions. This physiological state is critical for a broad range of biological processes, from stress response in unicellular systems to differentiation and development in multicellular organisms. Surprisingly, despite its recognized roles in cell biology in diverse species, key aspects of the regulation of quiescence remain poorly understood. To investigate protein function specifically in quiescence, a conditional activation approach is critical, in particular for factors that are essential for cell viability. However, the efficacy of a number of such inactivation strategies in quiescent cells remained unknown. Using nitrogen-depleted fission yeast cells as a well-established model for quiescence, we probed two types of commonly-used approaches: a targeted method for the reversible inhibition of engineered kinases using non-hydrolyzable ATP analogs, and a more general system targeting protein depletion using an auxin-inducible degron. Here we show that the use of analog-sensitive kinases is unsuitable for quiescent fission yeast cells, as the ATP analog serves as a nitrogen source and induces cell cycle re-entry. We then demonstrate how coupling a degron tag with a specific auxin ligand allows for rapid, lasting and reversible protein depletion in quiescent cells, providing a powerful tool for investigating the regulation of this crucial and widespread cellular state.

</details>

## Immunology and microbiology

### [Oral microbiome and DNA virome profiling in pigs reveals age-associated dynamics and extracellular recovery of Streptococcus suis-associated phage lineages](https://www.biorxiv.org/content/10.64898/2026.11.21.768310v1)
*Osei, E. K.; Ornelas, M. A. S.; Garcia Manzanilla, E. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.21.768310 v1 · relevance 0.10

- **In one sentence**: Shotgun metagenomic profiling of oral fluids from pigs on 15 Irish farms, using paired bulk and virus-like-particle enrichment, maps age-linked succession of oral bacteria and DNA phages and identifies 26 predicted phages targeting Streptococcus suis.
- **In plain words**: Researchers sampled the saliva-like oral fluid of pigs at different ages on commercial farms and sequenced all the genetic material in it, both the bacteria and the viruses that infect them. The microbial and viral communities shifted in a fairly predictable way as the pigs aged, especially after weaning. Among tens of thousands of viral groups found, 26 were predicted to infect Streptococcus suis, a pig pathogen.
- **Why it matters**: Pig oral microbes and viruses are relevant to herd health and to transmission of disease, and the paper offers a first catalogue of phages that may infect S. suis, which could inform phage-based or microbiome-targeted approaches. Whether these phages are useful as treatments is not shown here; the text only describes predicted targets from sequence data.
- **Background needed**: - Metagenomics: sequencing all DNA in a sample at once, then matching fragments to known organisms.
- Virome: the set of viruses in a sample; here, DNA viruses only.
- Bacteriophage (phage): a virus that infects bacteria.
- VLP (virus-like particle) enrichment: a lab step that concentrates viral particles so viral DNA is better represented.
- vOTU (viral operational taxonomic unit): a cluster of similar viral sequences treated as one viral "species".
- Streptococcus suis: a bacterium that causes disease in pigs and can occasionally infect people.
- Weaning: the point when piglets stop nursing and switch to solid feed, a major dietary change.
- Resistome: the collection of antibiotic resistance genes in a sample. · level: research-level

<details><summary>Original abstract</summary>

The pig oral cavity is a critical interface for microbial transmission and herd health monitoring, yet its microbiome and virome remains poorly characterised. We performed shotgun metagenomic sequencing of oral fluids from pigs across 15 commercial farms in Ireland, using paired bulk and virus-like particles (VLP) enrichment to capture comprehensive microbial and DNA virome diversity. Microbial communities shifted progressively with age, with early post-weaning animals enriched in environmental genera such as Pseudomonas and Staphylococcus and later stages dominated by lactic acid bacteria and anaerobes. Only 20.6% of vOTUs could be assigned to a known genus, with the most abundant being Astrithrvirus, which increased with age. Both microbiome and DNA virome exhibited predictable, coordinated age-associated succession with strong cross-domain coupling supported by virus-host networks. Functional profiling of the microbiome revealed that predicted carbohydrate substrates tracked the dietary transitions, while accessory viral functions partitioned by lifestyle and host. The early post-weaning stage was characterised by high abundance of viral integration and excision functions, as well as elevated resistome diversity that was almost exclusively of prokaryotic origin rather than viral. Importantly, 26 of the 25,223 vOTUs identified were predicted to target Streptococcus suis, providing the first metagenomic catalogue of such phages from pig oral environments. These findings expand our understanding of oral microbiome-virome dynamics and establish a framework for integrated microbiome and viromics approaches that could enable therapeutic phage discovery and inform microbiome-targeted interventions in pig production systems.

</details>

### [Infant formula composition is linked to distinct patterns of early gut colonization](https://www.biorxiv.org/content/10.64898/2026.11.20.768025v1)
*Fountouli, I.; Jayaprakash, Y.; Keizer, T. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.20.768025 v1 · relevance 0.08

- **In one sentence**: In 240 exclusively formula-fed infants in the Lifelines-NEXT cohort, reconstructed nutrient profiles of 17 formulas (62 components) were linked to species richness and to species-level gut colonization, with higher iron tied to lower Bifidobacterium breve and B. bifidum and higher Clostridium paraputrificum, supported by in vitro iron-limitation growth assays on stool isolates.
- **In plain words**: Babies who are fed infant formula receive different formulas, and the amounts of nutrients in them vary. This study asked whether those differences change which bacteria settle in the baby's gut during the first three months. The researchers reconstructed the nutrient content of the 17 formulas used by 240 infants and compared it with the gut bacteria found in each infant.
- **Why it matters**: Formula is a common early diet, so knowing that its nutrient levels relate to gut bacteria could eventually inform how formulas are designed or chosen. The text shows associations and lab growth tests only; it does not show that changing formula iron or other nutrients would change infant health, so the practical link is still unproven.
- **Background needed**: - Gut microbiota: the community of bacteria living in the intestine; early colonization is when these communities first establish.
- Infant formula: manufactured milk substitute whose nutrient content (vitamins, minerals, iron, etc.) can differ between brands.
- Birth cohort: a study that follows a group of people from birth to track exposures and outcomes.
- Species richness: how many different bacterial species are present.
- Bifidobacterium and Clostridium: genera of gut bacteria; Bifidobacterium species are commonly associated with infant guts.
- Association vs. causation: the study finds statistical links between formula components and bacteria, which do not by themselves prove cause.
- In vitro growth assay: testing how bacteria grow in a lab dish under set conditions, here limited iron. · level: intermediate

<details><summary>Original abstract</summary>

Early-life nutrition shapes the gut microbiota and can have long-term health implications. While infant formula feeding is widespread, it remains unclear how variations in its nutritional components shape microbiome colonization. Here, we reconstructed 62 components across the 17 infant formulas consumed during the first three months of life in 240 exclusively formula-fed infants in the Lifelines-NEXT birth cohort. Formula composition varied widely and several micronutrients, including vitamin E and iodine, were associated with species richness. Components were also associated with species-level colonization patterns. Higher iron content was associated with reduced Bifidobacterium breve and Bifidobacterium bifidum and increased Clostridium paraputrificum. Follow-up in vitro growth assays on infant-derived stool isolates showed that Bifidobacterium breve and Bifidobacterium bifidum tolerated iron limitation, while C. paraputrificum did not, consistent with the association signals. These findings show that infant formulas are not all alike and differences in component concentration affect microbiome colonization in early-life.

</details>

## Cancer biology

### [A hidden mitotic vulnerability emerges from BCAT1 redox-motif disruption in Ewing sarcoma](https://www.biorxiv.org/content/10.64898/2026.11.20.768122v1)
*Li, J.; Geyer, F. H.; Yershova, A. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.20.768122 v1 · relevance 0.05

- **In one sentence**: In Ewing sarcoma, disrupting the redox-active CXXC motif of BCAT1 (rather than its catalytic activity or its protein level) causes oxidative-stress sensitivity, chromosome-segregation defects, and reduced tumor growth, and it sensitizes cells to combined CK2 and AURKB inhibition in preclinical models.
- **In plain words**: This study looks at a protein called BCAT1 in Ewing sarcoma, a rare bone and soft-tissue cancer in young people. The researchers found that changing one specific chemically reactive site on the protein, while leaving its main enzyme activity intact, made cancer cells more fragile: they handled oxidative stress worse, made more errors when dividing, and grew less in the lab and in animals. Combining two existing drugs that target related cell-division enzymes made the cells easier to stop.
- **Why it matters**: It suggests a possible drug strategy that targets a cancer's redox and cell-division machinery rather than the usual enzyme activity, and it uses clinically evaluated inhibitors. The text reports only preclinical cell and animal work, so whether this helps patients is unknown.
- **Background needed**: - Cancer cells divide rapidly and produce high levels of reactive oxygen species (chemically reactive molecules that can damage cells); they need redox balance to cope.
- Chromosomal instability (CIN): frequent errors in splitting chromosomes when a cell divides, which can be fatal to cells beyond a tolerable limit.
- BCAT1 is an enzyme that breaks down branched-chain amino acids; the paper's focus is a CXXC motif (a pair of cysteines, a redox-sensitive site) separate from its catalytic activity.
- EWSR1::FLI1 is the fusion protein that drives Ewing sarcoma.
- CK2 and Aurora kinase B (AURKB) are enzymes that regulate cell division; silmitasertib (CK2 inhibitor) and barasertib (AURKB inhibitor) are drugs tested in clinical settings.
- Prime editing: a gene-editing method used to make precise changes in the cell's own DNA.
- Preclinical: results come from cell lines and animal models, not patients. · level: research-level

<details><summary>Original abstract</summary>

Cancer cells must keep oxidative stress and chromosome-segregation errors within tolerable limits to sustain rapid proliferation. Because redox homeostasis supports faithful chromosome segregation, disrupting redox-dependent mitotic safeguards could drive chromosomal instability (CIN) beyond cell tolerance and suppress tumor growth. Here, we investigated whether selectively disrupting redox-dependent safeguards could uncouple oxidative-stress adaptation from faithful chromosome segregation, exposing a therapeutic vulnerability at the interface of metabolic regulation and genome maintenance. We used Ewing sarcoma (EwS) as a model because it combines low genomic complexity with elevated oxidative stress and limited redox-buffering capacity. A survival analysis of cell-cycle-associated genes prioritized branched-chain amino acid transaminase 1 (BCAT1), whose high expression was associated with adverse outcomes in both primary and relapsed EwS. Functional genomics analyses revealed that BCAT1 is transcriptionally regulated by the EwS-specific EWSR1::FLI1 fusion oncoprotein through a distal enhancer-like GGAA microsatellite. Using prime-edited endogenous alleles and isogenic cell models, we found that disrupting BCAT1 redox-active CXXC motif increased sensitivity to oxidative stress and impaired recovery from it. Motif disruption also caused chromosome-segregation defects and DNA damage, reduced three-dimensional growth, and suppressed tumor formation and metastasis in vivo. By contrast, catalytic inactivation had limited effects. Although acute BCAT1 protein depletion reduced proliferation and tumor formation, constitutive BCAT1 knockout cells remained viable in culture and reduced tumor formation less than motif disruption. Mechanistically, CXXC motif disruption reduced casein kinase 2 (CK2) activity and increased Aurora kinase B (AURKB) activity, whereas BCAT1 degradation left CK2 activity unchanged and reduced AURKB activity. The enhanced sensitivity of CXXC-mutant cells to AURKB inhibition suggests a therapeutic vulnerability that could be exploited in BCAT1-wild-type EwS cells through combined CK2 and AURKB inhibition with silmitasertib and barasertib, increasing maximal growth inhibition and lowering the barasertib concentration required to suppress proliferation. Collectively, these findings reveal a mitotic vulnerability associated with BCAT1 redox-motif disruption that is not fully reproduced by protein loss and can be therapeutically exploited using clinically evaluated CK2 and AURKB inhibitors.

</details>

### [CIP2A is a biomarker for progression and poor prognosis in cutaneous squamous cell carcinoma](https://www.biorxiv.org/content/10.64898/2026.11.19.767767v1)
*Nissinen, L.; Tran, P.; Heiskanen, L. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.19.767767 v1 · relevance 0.04

- **In one sentence**: CIP2A, an inhibitor of the tumor-suppressor phosphatase PP2A, is elevated in cutaneous squamous cell carcinoma, promotes cancer cell growth via the MEK1/ERK1/2 pathway in vitro, and is associated with worse disease-specific survival in patients.
- **In plain words**: Cutaneous squamous cell carcinoma is a common skin cancer whose rising numbers call for better treatments, especially when it spreads. This study looked at a protein called CIP2A, which switches off a cell's natural brake on tumor growth. The researchers found more CIP2A in skin cancer cells and in tumor samples than in normal skin, reduced cancer cell growth when they silenced the gene, and found that patients whose tumors had high CIP2A did worse.
- **Why it matters**: The findings suggest CIP2A could help flag which skin tumors are likely to progress and could be a future drug target for advanced disease. The text reports associations and cell-level experiments, so it does not show that targeting CIP2A would treat patients; that would need further testing.
- **Background needed**: - Cutaneous squamous cell carcinoma (cSCC): a common skin cancer that can recur or spread (metastasize).
- Actinic keratoses and in situ cSCC: early or precancerous skin lesions, usually less invasive than full tumors.
- PP2A (protein phosphatase 2A): an enzyme that normally acts as a tumor suppressor by removing chemical 'on' tags from proteins.
- CIP2A: a protein that inhibits PP2A; when it is high, the tumor-suppressing brake is weakened.
- MEK1 and ERK1/2: proteins in a signaling chain that tells cells to grow and divide; phosphorylation is the tagging step that activates them.
- siRNA silencing: a lab technique that switches off a specific gene to see what happens to the cells.
- Kaplan-Meier analysis: a standard way to compare survival curves between patient groups.
- Immunostaining and single-cell RNA sequencing: methods for seeing where a protein or gene is active in tissue and in individual cells. · level: intermediate

<details><summary>Original abstract</summary>

The incidence of cutaneous squamous cell carcinoma (cSCC) is rising worldwide, highlighting the need for novel therapeutic options for recurrent and metastatic disease. Protein phosphatase 2A (PP2A) is a keyt tumor suppressor, and its inhibition promotes malignant progression. Here, we investigated the role of the cancerous inhibitor of PP2A (CIP2A) in cSCC progression. RNA-sequencing, oligonucleotide array-based expression, and qRT-PCR analysis demonstrated elevated CIP2A mRNA levels in cSCC cells compared with normal human epidermal keratinocytes (NHEKs). Western blotting confirmed higher CIP2A protein production in cSCC cells than in NHEKs. Analysis of single-cell RNA-sequencing data from cSCC showed CIP2A expression in epithelial cells and fibroblasts. Silencing CIP2A with specific siRNAs reduced cSCC cell growth and viability by inhibiting MEK1 and ERK1/2 phosphorylation. In vivo, strong CIP2A immunostaining was observed in tumor cells of primary cSCCs and cSCC metastases, whereas staining was absent or weak in all actinic keratoses and most cSCC in situ samples. Kaplan-Meier analysis revealed that patients with high CIP2A expression had significantly worse disease-specific survival than those with low expression. These findings identify CIP2A as a clinically relevant oncogene in cSCC progression, with elevated expression in invasive primary tumors and metastases. CIP2A may serve as a biomarker of cSCC progression and metastasis, as well as a potential therapeutic target in advanced and metastatic cSCC.

</details>

## Ecology and evolution

### [Social information use promotes breeding synchrony but constrains adaptation to rapid environmental changes](https://www.biorxiv.org/content/10.64898/2026.11.20.767538v1)
*Zheng, J.; Kuijper, B.; Aplin, L. M. et al.* · `animal behavior and cognition` · bioRxiv doi:10.64898/2026.11.20.767538 v1 · relevance 0.09

- **In one sentence**: An evolutionary individual-based model shows that breeding animals copying their neighbours' timing synchronises populations, speeding adaptation in stable or abrupt-change settings but lagging behind steady directional climate change.
- **In plain words**: The paper asks whether birds or other animals that time their breeding by watching their neighbours do better or worse than those that rely only on their own senses, especially as climate shifts. Using a computer simulation of populations living in territories with fluctuating, peaked resources, the authors found that copying neighbours makes individuals' timing converge, which helps populations adapt quickly in stable conditions. But when the climate changes steadily in one direction, the same convergence makes the population lag behind the shifting best timing and reduces its reproduction.
- **Background needed**: - Breeding phenology: the timing of reproduction within the year (e.g., when a bird lays eggs).
- Social information: cues gained by observing others' behaviour, as opposed to private information from one's own senses.
- Individual-based model: a computer simulation where each animal is tracked separately and its traits can evolve over generations.
- Synchrony: individuals acting at roughly the same time, which can emerge from copying each other.
- Positive feedback: when early copying makes others copy more, reinforcing the pattern.
- Environmental optimum: the best timing for a given environment, which can shift under climate change.
- Trade-off: gaining one benefit (coordination) at the cost of another (flexibility). · level: research-level

<details><summary>Original abstract</summary>

Animals use social information to make decisions, yet how such processes influence predictions in reproductive timing and population adaptation under environmental change remains unclear. While social information can improve decision accuracy through information pooling, spatiotemporal heterogeneity in conditions and patterns of environmental changes creates noise that potentially limits the value of social information use among breeding individuals. Here, we established an evolutionary individual-based model to examine how social and private sensing interact to shape breeding phenology in species distributed across territories with peaked resources and facing annual fluctuations and rapid climate change. We show that when individuals incorporate social information from neighbours, behavioural responses become increasingly synchronised through positive feedback in decision-making. This emergent synchrony helps populations to adapt faster and can increase reproductive output under stable environmental conditions relative to relying only on private information. However, under directional climate change, the same mechanism reduces population responsiveness by constraining variation in individual responses, leading to systematic lag in tracking shifting environmental optima and reduced population reproductive output. Our results demonstrate that social information use can produce a general trade-off at the population level between synchronisation and adaptive flexibility across environmental contexts. Social interaction enhances population performance when environments are either consistent or changing drastically across both spatial and temporal scales. Rather than uniformly improving performance, social interaction may create conditions under which collective behaviour becomes maladaptive when environments change rapidly.

</details>

### [No evidence of evolution of male fitness components in response to yeast deprivation: Putative female specific nutrient dependent reproductive adaptation](https://www.biorxiv.org/content/10.64898/2026.11.23.768529v1)
*Adhikary, S.; Pal, R. S.; Halder, S. et al.* · `evolutionary biology` · bioRxiv doi:10.64898/2026.11.23.768529 v1 · relevance 0.08

- **In one sentence**: Experimental evolution of Drosophila melanogaster under adult live-yeast deprivation for over 140 generations found no change in measured male pre- and post-copulatory fitness traits, suggesting the nutrient-driven adaptation is female-specific and genetically decoupled between sexes.
- **In plain words**: Researchers asked whether fruit flies that were bred for many generations on a diet without live yeast changed in ways that affect males, not just females. Female flies had previously evolved to lay more eggs early in life under this diet, so the question was whether males would also change, either directly or because the sexes share genes. The team measured a range of male competitive traits and found none had changed.
- **Why it matters**: It bears on a long-standing question in evolutionary biology: whether genes shared between the sexes limit how each sex can adapt separately. The text reports a null result in four populations, so it supports the idea of decoupled sex-specific genetics for this particular diet stress, but it does not establish this more broadly.
- **Background needed**: - Experimental evolution: populations are kept under a fixed challenge for many generations and then compared with controls.
- Intersexual genetic correlation: when genes that affect one sex also affect the other, so changes in one can drag the other along.
- Sexual antagonism: a trait that helps one sex but harms the other.
- Pre- and post-copulatory fitness: success in attracting or competing for mates before mating, and success in sperm competition or fertilization after mating.
- Drosophila melanogaster: the common fruit fly, widely used in genetics.
- Live yeast is a protein source that female flies need to produce eggs. · level: intermediate

<details><summary>Original abstract</summary>

Intersexual genetic correlation (IGC) is pervasive in sexually reproducing organisms and can constrain sex-specific adaptive evolution. Nevertheless, sexes frequently undergo adaptive divergence in response to novel ecological challenges. Here, we investigated whether adaptation to nutritional stress is sex-limited or constrained by shared genetic architecture. We utilized four laboratory-adapted populations of Drosophila melanogaster subjected to experimental evolution under adult-stage live-yeast deprivation for over 140 generations - a regime that previously drove adaptive female reproductive evolution, particularly enhancing early-life fecundity and ovarian function. Because female D. melanogaster rely heavily on dietary yeast for protein-dependent egg production, this evolutionary response may be female-limited. Alternatively, male fitness traits could respond either through direct selection or via correlated response driven by IGC. To distinguish between these hypotheses, we evaluated a comprehensive suite of pre- and post-copulatory male competitive fitness components. We found that all measured male fitness traits remained unchanged following experimental evolution, demonstrating that nutrient-dependent adaptation in these populations is strictly female-specific, with no evidence of correlated responses or sexually antagonistic trade-offs. Our results indicate that the genetic architecture underlying nutrient-dependent reproductive adaptation is largely decoupled between the sexes, allowing each sex to independently approach its sex-specific fitness optimum.

</details>

## Plant biology

### [Arabidopsis histone demethylase RSI1/FLD self-regulates its pathogen-induced expression](https://www.biorxiv.org/content/10.64898/2026.11.19.767995v1)
*Singh, U.; Patil, V.; Kumar, R. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.19.767995 v1 · relevance 0.05

- **In one sentence**: In Arabidopsis, the histone demethylase RSI1/FLD appears to repress its own pathogen-induced expression by removing H3K4me2/me3 marks at its transcription start site, with GSTT2 needed for that induction.
- **In plain words**: Plants fight infections in one leaf and then prepare the rest of the plant for future attacks, a state called systemic acquired resistance. This paper studies a plant gene, RSI1/FLD, that is needed for this whole-plant defense and is switched on when a pathogen arrives. The authors found that the gene limits its own activity: it sticks to its own DNA near the start of the gene and removes chemical marks that help genes stay active, which may keep the defense response at a moderate level.
- **Why it matters**: Defense responses that are too weak leave plants exposed, while responses that are too strong can be costly, so a built-in brake on a key regulator is a sensible design to study. The text does not show how broadly this self-limiting loop applies beyond this gene and these experiments, so its wider significance is uncertain.
- **Background needed**: - Histones are proteins that DNA wraps around; chemical tags on them (methyl groups) help switch genes on or off.
- H3K4me2 and H3K4me3 are methyl tags on the histone H3 protein that are generally linked to active genes.
- A histone demethylase removes these methyl tags, which usually quiets a gene.
- Systemic acquired resistance (SAR) is a long-lasting, plant-wide immune state triggered by a local infection.
- Transcription start site (TSS) is the point where a gene's copying into RNA begins.
- ChIP (chromatin immunoprecipitation) is a lab method for finding which DNA regions a protein binds or which tags are present there.
- GUS reporter assays use a marker enzyme to measure how active a gene's promoter is.
- GSTT2 is a protein with a SANT domain, a structural motif that often binds DNA or chromatin; the text describes it only as essential for SAR.</background>
<parameter name="difficulty">research-level

<details><summary>Original abstract</summary>

REDUCED SYSTEMIC IMMUNITY 1(RSI1)/FLOWERING LOCUS D (FLD) is essential for the activation of systemic acquired resistance (SAR). RSI1 functions as a repressor of gene expression by demethylating H3K4me2 and H3K4me3. RSI1 expression is induced both in local and systemic tissues upon pathogen inoculation. However, the mechanism of its induction or its expression regulation upon pathogenesis is not known. Here we show that RSI1 expression in SAR-induced rsi1 mutant plants is higher than WT plants, suggesting self-regulation. Pathogen-induced expression of RSI1 requires the function of GSTT2, a SANT domain-containing protein essential for SAR activation. Co-expression of RSI1 suppresses pRSI1:GUS activity in a transient assay system. Chromatin-immunoprecipitation (ChIP) experiments reveal that RSI1 physically associates near the transcription start site (TSS) of the RSI1 locus and facilitates demethylation of H3K4me2 and H3K4me3 at RSI1 locus. Our data altogether demonstrate that RSI1 negatively regulates its own expression as a possible mechanism of keep the SAR expression at an optimal level.

</details>

### [Zeaxanthin-dependent rapid energy quenching uncovers complexity of PsbS protonation](https://www.biorxiv.org/content/10.64898/2026.11.21.768332v1)
*Ponce, R.; Liu, E.; Niyogi, K. K. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.21.768332 v1 · relevance 0.04

- **In one sentence**: In Arabidopsis plants expressing PsbS with mutations at two lumen-facing protonatable glutamate residues (E122 and E226), the authors show a residual energy-dependent quenching (qE) that tracks zeaxanthin and lumenal acidification and is halved without the CP29 antenna protein.
- **In plain words**: Plants protect their light-capturing machinery from too much sunlight by releasing extra energy as harmless heat, a process called energy-dependent quenching. This study looked at a protein called PsbS, which senses acidity inside the photosynthetic membrane and helps trigger that heat release. By changing the two parts of PsbS that take up acid, the researchers found that a small amount of heat release still happened, and it depended on a pigment called zeaxanthin and on a nearby light-harvesting protein, CP29.
- **Why it matters**: Understanding exactly how PsbS switches on heat dissipation matters for efforts to tune crop photosynthesis under fluctuating light. The text suggests PsbS's physical presence, not just its acid-sensing residues, is needed, which refines the current picture; the full implications beyond this study are not established in the text.
- **Background needed**: - Photosynthesis captures light energy in membranes (thylakoids) inside chloroplasts.
- Too much light acidifies the inside of these membranes (the lumen).
- Energy-dependent quenching (qE) is a protective process that converts excess light energy into heat.
- PsbS is a protein in photosystem II that senses this acidity; its key acid-binding sites are glutamate residues E122 and E226.
- Zeaxanthin is a yellow plant pigment (xanthophyll) that helps drive quenching.
- CP29 is a small light-harvesting antenna protein attached to photosystem II.
- Arabidopsis is a model plant commonly used in lab studies; a "null mutant" lacks the gene entirely. · level: research-level

<details><summary>Original abstract</summary>

Rapid responses to changes in light intensity are crucial for photosynthetic organisms to regulate their light-harvesting capacity and optimize growth. PsbS, the S subunit of photosystem II (PSII) located in the thylakoid membrane, senses lumenal pH changes that reflect the balance between the light and carbon reactions of photosynthesis. Upon lumenal acidification caused by absorption of excess light energy, PsbS undergoes protonation of its lumen-exposed domain, triggering energy-dependent quenching (qE), which dissipates excess energy as heat. Despite extensive research, the precise molecular mechanism by which PsbS induces qE remains poorly understood. In this study, rather than relying solely on a PsbS null mutant, we used Arabidopsis lines expressing PsbS variants with mutations at the two essential protonatable residues (E122 and E226) in the lumenal domains to investigate the molecular interplay among PsbS, lumenal acidification, and zeaxanthin during qE induction. Our results indicate that this mutant PsbS protein can induce a small qE, the magnitude of which is strongly linked to both zeaxanthin accumulation and lumenal acidification. Furthermore, we found that the loss of the monomeric light-harvesting antenna complex CP29 in this mutant PsbS line reduced the small qE induction by nearly half. Together, our observations suggest that the physical presence of PsbS is essential for qE induction, which is driven by direct or indirect interactions between PsbS and zeaxanthin, potentially mediated by light-harvesting antenna complexes.

</details>

## Bioengineering and synthetic biology

### [Correlative mapping links extracellular matrix architecture to local mechanics in cardiac aging](https://www.biorxiv.org/content/10.64898/2026.11.21.768346v1)
*Ramli, M. F. H.; Ghosh, A.; Hengst, R. M. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.21.768346 v1 · relevance 0.06

- **In one sentence**: Correlative imaging and nanoindentation study that links an image-based index of extracellular matrix architecture (ArchI) to local stiffness in young versus aged murine heart tissue.
- **In plain words**: As the heart ages, the scaffolding around its cells, called the extracellular matrix, gets reorganized, and it is unclear how that change in structure relates to how stiff the tissue feels locally. The authors measured six image-based features of several matrix proteins in young and old mouse hearts, combined them into a single score, and tested it against stiffness measured by pressing a small probe onto thin slices of fresh heart tissue. They report that older hearts scored higher on this index and were stiffer, and that the two were positively linked, more strongly in the aged tissue.
- **Why it matters**: Stiffening of the heart wall is part of age-related heart decline, so tying a measurable structural pattern to local mechanics may help future work on how matrix structure drives tissue stiffness. The text does not establish a causal link or a clinical use, so the practical significance remains unclear.
- **Background needed**: - Extracellular matrix (ECM): the protein mesh outside cells that gives tissue its structure, including collagen fibers, fibronectin and laminin.
- Collagen remodeling: changes in how much collagen is present and how it is arranged; often linked to tissue stiffening with age.
- Immunofluorescence: staining proteins with fluorescent tags so they show up under a microscope.
- Nanoindentation: pressing a tiny probe into a sample to measure local stiffness, expressed as Young's modulus (higher means stiffer).
- Architectural index (ArchI): the authors' combined score from six image measurements; the text gives no further detail on its construction.
- Stochastic network model: a computer model that generates random fiber networks to test how structural changes affect the measurements.
- Age-adjusted regression: a statistical method that checks the link between two measures while accounting for age. · level: research-level

<details><summary>Original abstract</summary>

Cardiac aging is accompanied by extracellular matrix (ECM) remodeling, but how changes in matrix architecture relate to local tissue mechanics remains poorly understood. Here, we quantified six image-derived architectural descriptors across selected ECM components in young and aged murine myocardium and integrated them into an architectural index that we term 'ArchI'. Age-associated architectural changes differed among ECM components, with higher ArchI values observed for fibrillar collagen, fibronectin, and laminin-associated networks. To examine how defined structural changes affect the component descriptors, we developed controlled synthetic geometries and a stochastic network model. These analyses revealed index sensitivity to matrix occupancy, fiber width, and network continuity. We then combined nanoindentation of fresh cardiac tissue slices with subsequent immunofluorescence staining and imaging of collagen to correlate local tissue stiffness with ECM architecture in corresponding regions. Aged myocardium exhibited higher ArchI and Young's modulus, with local heterogeneity in their spatial correspondence. Age-adjusted regression revealed a positive association between ArchI and Young's modulus, with a steeper association in aged myocardium. Together, these findings reveal component-specific ECM remodeling during aging and provide a means to examine spatial structure-mechanics relationships in the aging heart.

</details>

### [Enhancing the Efficacy of Oncolytic Viruses by Engineering Virus Host Interactions Using CRISPR Cas13d](https://www.biorxiv.org/content/10.64898/2026.11.20.768134v1)
*Ameil, Z.; Kooshki Zamani, N.; Khalid, Z. et al.* · `synthetic biology` · bioRxiv doi:10.64898/2026.11.20.768134 v1 · relevance 0.05

- **In one sentence**: The paper builds a doxycycline-inducible CRISPR Cas13d system inside an oncolytic herpes simplex virus type 1 (oHSV1) to knock down host antiviral genes in tumor cells during infection, and tests a 15-gene guide RNA library across three mouse and human tumor cell lines.
- **In plain words**: Oncolytic viruses are viruses engineered to infect and kill cancer cells, but tumor cells can fight back with their own antiviral defenses. This work adds a switchable gene-silencing tool to a herpes virus so that researchers can turn down specific tumor defense genes on demand, using a drug (doxycycline) as the switch. The authors report that the approach works in principle and shows guide-dependent differences in fluorescence across three tumor cell lines.
- **Why it matters**: Limited viral spread inside tumors is one reason these therapies can fall short, so a way to temporarily lower tumor antiviral defenses could in principle help improve them. The text is a platform-development report, however; it does not show improved tumor killing or any therapeutic benefit in animals, so its practical value remains to be tested.
- **Background needed**: - Oncolytic virus: a virus designed to replicate in and destroy cancer cells.
- Herpes simplex virus type 1 (HSV1): a common virus that is being engineered as a cancer treatment.
- Antiviral response: the cell's built-in defenses that slow or stop viral replication.
- CRISPR: a gene-editing toolkit originally from bacteria; Cas13d is a variant that targets RNA rather than DNA, reducing the amount of a protein made from a gene without changing the DNA.
- Guide RNA: a short RNA sequence that directs the Cas enzyme to a specific target.
- Tet On/Tet Off: genetic switches that turn a gene on or off in the presence of doxycycline, an antibiotic.
- Pharmacological inhibitors: drugs that block specific cell pathways, used here to find which pathways limit infection.
- Cell lines used: EMT6 and CT26 (mouse tumor cells) and 786-O (human kidney tumor cells). · level: research-level

<details><summary>Original abstract</summary>

Oncolytic herpes simplex virus type 1 (oHSV1) is a promising cancer therapy, but tumor cell antiviral responses can restrict viral replication. Strategies for temporally controlled targeting of antiviral factors remain limited. Here, we developed an inducible CRISPR Cas13d platform to modulate host responses during HSV1 infection. We screened 13 pharmacological inhibitors across tumor models to identify pathways associated with restricted infection. Reporter assays identified Cas13d as the preferred effector over Cas13b, while endogenous-target experiments demonstrated Cas13d mediated reductions in target protein abundance. We optimized guide RNA expression using RNA polymerase III promoters, selected p7SK, and established doxycycline-responsive Tet On and Tet Off systems. The platform was incorporated into HSV1 to generate a gRNA library targeting 15 host antiviral genes, together with two non-targeting controls. Doxycycline-dependent reporter readouts demonstrated inducible activity. Evaluation in EMT6, CT26, and 786 O cells revealed guide-dependent differences in fluorescence. These findings establish a programmable framework for investigating virus host interactions during oncolytic HSV infection.

</details>

## Mathematical biology (arXiv)

### [Beyond the Blueprint: The Continuing Evolution of Turing's Theory of Morphogenesis](https://arxiv.org/abs/2611.30543)
*Andrew L. Krause, Kevin J. Painter, Denis J. Headon* · `q-bio.CB` · arXiv:2611.30543v1 · relevance 0.06

- **In one sentence**: A historical and critical review of Alan Turing's reaction-diffusion theory of biological pattern formation, assessing the overlapping concepts derived from it and proposing challenges for future interdisciplinary work.
- **In plain words**: This paper looks back at Alan Turing's 1952 idea that chemicals reacting and spreading through tissue could spontaneously create patterns such as stripes or spots in living things. The authors trace how the idea developed over time and how it has been used in modern experiments. They argue that some uses are valuable, but that overly simple claims of confirmation should be treated with caution.
- **Why it matters**: Turing's model is one of the most cited explanations for how animal coats, fingers, and organ layouts take shape, so a careful check of what it does and does not explain is useful for developmental biology. The text itself is a review and does not report new experimental results, so its value lies in clarifying concepts rather than in a new finding.
- **Background needed**: - Morphogenesis: the process by which an organism develops its shape and form.
- Turing pattern: a pattern that arises from two or more chemicals that react with each other and diffuse (spread) at different rates, starting from near-uniform conditions.
- Reaction-diffusion: the mathematical framework describing such chemical reactions combined with spreading.
- Morphogen: a signaling molecule whose concentration gradient guides cell fate.
- Model validation: checking whether a theory's predictions match real observations; the paper cautions that simple matches can be misleading. · level: intermediate

<details><summary>Original abstract</summary>

Turing's article ``The Chemical Basis of Morphogenesis'' has profoundly influenced conceptual views on the emergence of biological form across scales and species. It has also served as a foundational framework to guide experimental investigations into the mechanisms that underlie pattern formation. In this article, we trace the historical development of Turing's ideas and examine their integration into contemporary research programs. We critically assess the broad and often overlapping concepts that have derived from Turing's work, both highlighting value in productive applications of the theory and suggesting that skepticism should remain in overly simplistic validations. By clarifying these concepts and their intrinsic limitations, we rethink contemporary approaches aimed at understanding the essential principles that govern biological pattern formation. We pose some important challenges that will require interdisciplinary expertise to overcome, and which will necessitate fundamentally new paradigms to understand the physical origin of Darwin's ``endless forms most beautiful''.

</details>

### [General-purpose language models are neurosymbolic reasoners able to annotate proteins from sequence](https://arxiv.org/abs/2611.28529)
*Christopher J. Mungall, Marcin P. Joachimiak* · `q-bio.GN` · arXiv:2611.28529v1 · relevance 0.04

- **In one sentence**: Frontier general-purpose language models were prompted with raw protein sequences and performed above chance on several annotation tasks (Pfam domain location, loss of catalytic residues, structure and activity), though they were not compared against specialised tools.
- **In plain words**: Scientists want to work out what jobs genes and proteins do, across all living things. This paper asks whether large general-purpose AI chatbots, which are trained mostly on text, can read a protein's chain of amino-acid letters and label it, much as specialised biology programs do. The authors found the models did clearly better than guessing on these labelling tasks, but they also made confident-sounding mistakes.
- **Why it matters**: It challenges the common assumption that text-trained models cannot handle biological sequences, and suggests they might eventually be combined with sequence data and literature knowledge. The text does not show how these models compare with dedicated tools, so their practical value remains unclear.
- **Background needed**: - Protein: a chain of amino acids, written as a string of letters, that folds into a 3D shape and carries out a function.
- Protein annotation: labelling a protein with what it does, its structural parts, or its domains.
- Pfam domain: a recognised, reusable building block of a protein with a known function, catalogued in a standard database.
- Catalytic residue: a specific amino acid that directly takes part in a protein's chemical reaction; losing it usually means the protein no longer works.
- Language model: an AI system trained to predict text (or here, sequence letters); "frontier" means among the most capable current models.
- Hallucination: when an AI produces plausible but false output, here stated with the same confidence as correct answers.
- Neurosymbolic: combining pattern-learning AI with explicit rule-based reasoning and symbols.
- Chance baseline: the score a random guess would achieve; "above chance" means better than this only. · level: intermediate

<details><summary>Original abstract</summary>

Determining the function of genes across the tree of life is one of the major challenges in biology. Generative AI approaches to this problem generally fall into two categories: language models trained on biological sequences that are able to predict structure and function from signals in those sequences; and generalist language models trained on text, that are able to reason about biological function symbolically. A default operating assumption is that protein language models do not perform well on symbolic tasks, and that generalist language models do not perform well on sequence tasks. However, a recent report showed that frontier generalist models perform surprisingly well on next-residue prediction tasks. We set out to explore whether these capabilities extended to protein annotation. We assigned different frontier generalist models a variety of protein annotation tasks, including predicting the presence and coordinates of Pfam domains, loss of functional catalytic residues, and predicting structure and activity. On all annotation tasks, the frontier models performed well above chance; we did not benchmark them against specialised tools. The models also make characteristic hallucination errors, and they state them as confidently as their correct calls. Though untested against specialised methods, the nascent ability of frontier models to perform protein annotation from sequence alone is intriguing. The ability to reason over sequence, structure, and symbols in a single model allows for a neurosymbolic approach where a combination of sequence, experimental data and knowledge from the literature can be holistically combined to improve on de novo functional annotation of the protein universe. Prompts, test sets, model outputs and code: https://github.com/ai4curation/fable-sequence-to-function. Summary of results: https://ai4curation.io/fable-sequence-to-function/

</details>

## Epidemiology

### [Disease-anchored organ aging clocks enable multi-organ risk profiling from routine labs](https://www.medrxiv.org/content/10.64898/2026.11.22.26368688v1)
*Shi, C.; Sun, Y.; Ruan, X. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.22.26368688 v1 · relevance 0.05

- **In one sentence**: Organ-specific aging clocks trained on first onset of each organ's disease from routine blood tests (rather than chronological age from proteomics) are shown to flag own-organ disease in UK Biobank, and to retain organ correspondence and add information over clinical risk scores in NHANES and JMDC cohorts.
- **In plain words**: Researchers wanted a way to estimate how "old" each organ in the body is, using simple blood tests rather than expensive protein measurements. They trained organ-specific scores on when people in a large UK study first developed diseases of each organ, then fixed those scores so they could be applied elsewhere. The paper reports that the scores picked out disease in the matching organ, and that they carried useful information in two other cohorts, one in the US and one in Japan.
- **Why it matters**: Organ-level risk from routine lab tests could help flag which organ is at risk before disease appears, if it holds up beyond these cohorts. The text does not report clinical outcomes of acting on these flags, so its practical value is still untested.
- **Background needed**: - Biological age: an estimate of how worn-down the body is, which can differ from calendar age.
- Organ clock: a score that estimates the biological age of one organ, often from blood markers.
- Proteomics: measuring thousands of proteins in blood; costly and not routinely done.
- UK Biobank, NHANES (US), JMDC (Japan): large health cohorts with lab data and long follow-up.
- "First onset": the first time a disease is diagnosed in a person.
- Frozen coefficients: the scoring formula is fixed after training and applied unchanged to new data.
- Random protein panels: size-matched sets of random proteins used as a control to check that results are not just chance.
- Clinical risk scores: standard tools that estimate patient risk from common factors. · level: research-level

<details><summary>Original abstract</summary>

Organ clocks estimate the biological age of organs from blood, but current clocks assign tissue-enriched proteins to organs and train on chronological age, which requires proteomics and does not yield organ-specific disease risk. In the UK Biobank, we trained organ clocks on first onset of disease of each organ using routine laboratory tests and froze the coefficients. Under an age label, organ-clock readouts arose equally in size-matched random protein panels; with a disease label, clocks selected their own organ's proteins and predicted their own organ's diseases. Defining extreme aging by multiples of disease risk concentrated flags on own-organ disease. Frozen clocks kept organ correspondence in the US NHANES cohort, predicted first onset of own-organ disease in the Japanese JMDC cohort and added more information to clinical risk scores than current organ clocks. Trained once where disease follow-up exists, organ clocks can be used wherever routine laboratory tests are measured.

</details>

### [Sources of protein in UK adults following contemporary plant-based diets: findings from the Feeding the Future (FEED) Study](https://www.medrxiv.org/content/10.64898/2026.11.23.26368579v1)
*Lawson, I.; Bell, W.; Key, T. J. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.23.26368579 v1 · relevance 0.05

- **In one sentence**: Cross-sectional analysis of the UK FEED cohort (n=6,113) quantifying food-group sources of protein across omnivore, flexitarian, pescatarian, vegetarian and vegan diets, and the share of each group below the estimated average protein requirement, with and without under-reporters excluded.
- **In plain words**: This study looks at where protein comes from in the diets of about 6,000 UK adults who eat meat, fish, or no animal products in different combinations. The researchers worked out how much each food group adds to daily protein and how many people in each diet group fall short of a standard protein target. Few people fell short overall, and the gap seen among vegetarians and vegans mostly disappeared once people who likely under-reported their eating were removed.
- **Why it matters**: Plant-based diets are common, and people often ask whether they supply enough protein, so this gives a large, recent UK picture of protein sources. The reported shortfalls shrink sharply after excluding under-reporters, which suggests the conclusion depends heavily on how reliable self-reported diet records are; the text does not show how well that exclusion was done.
- **Background needed**: - Protein is needed for building and repairing body tissue; the "estimated average requirement" (EAR) is the amount that meets the needs of half a population.
- A food frequency questionnaire is an online survey asking how often people eat listed foods; it relies on memory and self-report.
- Under-reporters are people whose recorded energy intake seems implausibly low compared with their likely needs; excluding them is a common sensitivity check.
- Diet groups compared: omnivores (eat everything), flexitarians (mostly plant-based, sometimes meat), pescatarians (fish but no meat), vegetarians (no meat or fish), vegans (no animal products).
- Cross-sectional means a single snapshot in time, so it cannot show cause and effect.
- "Plant-based meat alternatives" are processed products designed to resemble meat, such as meat-substitute burgers. · level: intermediate

<details><summary>Original abstract</summary>

Objective To identify and quantify sources of protein intake in United Kingdom (UK) adults following different diets, and assess how these sources contribute to meeting protein requirements. Design Cross-sectional analysis of the Feeding the Future Study (FEED), a UK cohort recruited in 2022-2023. Dietary intake was assessed using an online food frequency questionnaire. We calculated the percentage contribution of food groups to daily protein intake, and the proportion of participants meeting the estimated average requirement (EAR) for protein, with and without exclusion of under-reporters. Setting A contemporary cohort of UK adults. Participants 6,113 adults: 1,540 omnivores, 1,322 flexitarians, 547 pescatarians, 1,212 vegetarians, and 1,492 vegans. Results Grains contributed 10-30% of total protein intake across all groups. Dairy contributed 12.9-14.2% in non-vegan groups, while plant-based dairy alternatives contributed less in vegans (7%), mainly from soy milk (4.3%). Other major contributors (>10%) were meat for omnivores (33.0%) and flexitarians (13.5%); fish for pescatarians (14.9%); plant-based meat alternatives for vegetarians (12.0%); and plant-based meat alternatives (15.0%), legumes and pulses (10.5%), and nuts and seeds (10.5%) for vegans. The proportion below the protein EAR ranged from 1.9% in omnivores to 14.0% in vegans, falling to 0.01% and 3.6% respectively, after excluding under-reporters. Conclusions Grains were a major contributor to protein intake across all diet groups, as was dairy in all non-vegan groups. Protein sources were more varied in non-omnivorous groups, particularly vegans. Few participants fell below the protein EAR and the higher proportions among vegetarians and vegans were largely attenuated after excluding under-reporters.

</details>

## Infectious diseases

### [Impact of expanded influenza vaccination programs in children and adults in Australia: a mathematical modelling study](https://www.medrxiv.org/content/10.64898/2026.11.23.26368629v1)
*Leung, T.; Stopard, I. J.; Wood, J. G. et al.* · `infectious diseases` · medRxiv doi:10.64898/2026.11.23.26368629 v1 · relevance 0.08

- **In one sentence**: A mathematical transmission model, calibrated to Australian surveillance data, compares the population-level impact of a live-attenuated influenza vaccine (LAIV) program for school-aged children against strategies that raise inactivated vaccine (IIV) uptake in adults.
- **In plain words**: This study asks whether giving a nasal-spray flu vaccine to children could reduce flu illness across Australia, beyond the injected vaccine that mainly protects older adults. The researchers built a computer model of how flu spreads and is vaccinated, checked it against surveillance data, and compared scenarios. They found that a children's nasal-spray program aimed at ages 5 to 17 was estimated to cut flu hospitalisations by 16% and deaths by 13% at 55% coverage.
- **Why it matters**: Children are a major source of flu spread, so protecting them may also help adults and older people who are not vaccinated. The result supports the idea that the nasal-spray vaccine could be an additional tool for flu prevention in Australia, though the findings depend on the model's assumptions and are not a trial result.
- **Background needed**: - Influenza (flu) is a common virus that causes severe illness, especially in young children and older adults.
- Inactivated influenza vaccine (IIV) is the standard injected flu shot; Australian programs focus mainly on protecting older adults directly.
- Live-attenuated influenza vaccine (LAIV) is a weakened live virus given as a nasal spray; it is now approved in Australia for ages 2 to 17.
- Mathematical (transmission) modelling simulates how an infection spreads through a population under different vaccination scenarios, calibrated here to surveillance data (routine case and hospital records).
- "Coverage" means the share of the target group vaccinated; "dose efficiency" compares how much benefit is gained per vaccine dose given.
- "Number needed to vaccinate" (NNV) is the number of people who must be vaccinated to prevent one hospitalisation. · level: intermediate

<details><summary>Original abstract</summary>

Background: Seasonal influenza is a common cause of severe illness, particularly in young children and older adults. In Australia, influenza vaccination programs using the inactivated influenza vaccine (IIV) largely focus on direct protection of older adults. Live-attenuated influenza vaccine (LAIV) is now available for children aged 2-17 years, offering an opportunity to complement existing IIV programs. Methods: We developed a mathematical model of seasonal influenza transmission and vaccination in Australia, calibrated to surveillance data. We evaluated the health impact of LAIV programs on influenza burden relative to a baseline IIV-only scenario that assumed current coverage levels. We compared the dose efficiency of LAIV programs targeting school-aged children with strategies that increased IIV uptake in adults. Findings: An LAIV program targeting children aged 5-17 years was estimated to have the largest population-level impact, reducing influenza hospitalisations by 16% and deaths by 13%, assuming 55% coverage. An IIV program achieving 55% coverage in adults aged 50 years and older was predicted to have a similar population-level reduction in hospitalisations to a primary school-aged LAIV program (around 9.5%). Based only on doses administered, LAIV programs were more efficient at averting cases, hospitalisations, and deaths than strategies that expanded IIV uptake in adults. However, for outcomes in adults [&ge;]65 years old, increasing IIV uptake in this age group was estimated to be the most efficient strategy, with a number needed to vaccinate of 1811 to avert one hospitalisation. Interpretation: Our results support the potential use of LAIV as an additional tool in the prevention of seasonal influenza in Australia.

</details>

### [Distinct pulmonary transcriptomic and proteomic host signatures enable accurate diagnosis of severe lower respiratory tract infection](https://www.medrxiv.org/content/10.64898/2026.11.23.26368772v1)
*Lydon, E.; Sax, P. K.; Van Phan, H. et al.* · `infectious diseases` · medRxiv doi:10.64898/2026.11.23.26368772 v1 · relevance 0.08

- **In one sentence**: Paired transcriptomic (RNA) and proteomic (protein) profiling of tracheal aspirates from critically ill children distinguishes microbiologically confirmed lower respiratory tract infection from noninfectious causes, with similar global pathways but poor gene-protein agreement and different top biomarkers.
- **In plain words**: Doctors often struggle to tell whether a severely ill child's breathing failure is caused by a lung infection or by something non-infectious. This study looked at fluid sucked from the windpipe of 105 critically ill children, measuring both the genetic messages (RNA) and the proteins the body's cells made. Both approaches showed a similar overall picture of infection, though the individual genes and their matching proteins often did not agree.
- **Why it matters**: It suggests that measuring the body's own immune response, rather than only searching for germs, can work for diagnosis, and that RNA and protein tests may point to different biomarkers while reaching similar conclusions. The text does not show whether either approach improves clinical care, so its practical impact remains to be tested.
- **Background needed**: - Lower respiratory tract infection: infection of the lungs and airways below the throat.
- Tracheal aspirate: a sample of fluid suctioned from the windpipe of a patient on a breathing tube.
- Transcriptomics: measuring RNA, the short-lived copies of genes that signal which genes are active.
- Proteomics: measuring proteins, the molecules that do most of the work in cells.
- Gene-protein agreement: whether a gene's RNA level tracks the amount of its protein; here it was largely poor.
- Classifier and AUC: a statistical model that sorts patients into groups; AUC near 1.0 means near-perfect separation, and >0.90 here means high accuracy.
- Biomarker: a measurable signal used to indicate a condition.
- Interferon signaling and complement activation: parts of the immune system's alarm and defense responses. · level: research-level

<details><summary>Original abstract</summary>

Lower respiratory tract infection (LRTI) is a leading cause of acute respiratory illness, yet distinguishing it from noninfectious conditions remains a clinical challenge. Measuring the host immune response in the blood or lower airways, rather than exclusively detecting pathogens, has emerged as an alternative diagnostic strategy. However, it remains unclear whether RNA or protein measurements yield greater diagnostic information, or whether the two capture the same underlying biology. To address this, we performed paired transcriptomics and proteomics on tracheal aspirate specimens from 105 critically ill children with respiratory failure, 72 with microbiologically confirmed LRTI and 33 with noninfectious causes. Both approaches detected a clear host signature of LRTI which converged on similar core immune pathways including interferon signaling, inflammation, and complement activation. Despite this, agreement between individual genes and their corresponding proteins was largely poor. Diagnostic classifiers built from either RNA or protein data identified LRTI with similarly high accuracy (AUC>0.90), but selected different top biomarkers, and yielded discordant classifications for 12% of patients. Taken together, we find that lower airway transcriptomics and proteomics capture similar global biological features of LRTI despite poor correlation between gene and protein expression, providing fresh insight into approaches for biomarker discovery and clinical translation.

</details>

## Public and global health

### [Procedure composition, age and race/color in gender-affirming surgical authorizations of the Brazilian public health system, 2014-2025](https://www.medrxiv.org/content/10.64898/2026.11.23.26368723v1)
*dos Santos, J.; Amorim Costa, C. M.* · `public and global health` · medRxiv doi:10.64898/2026.11.23.26368723 v1 · relevance 0.08

- **In one sentence**: A nationwide descriptive study of 1,375 Brazilian Unified Health System hospital admission authorizations for gender-affirming surgery (2014–2025), classifying procedures by code with a versioned classification and reporting procedure mix, age, race/color and facility counts, with results reproduced by an independent pipeline.
- **In plain words**: This paper looks at records of surgeries that Brazil's public health system paid for to help people change their body to match their gender, from 2014 to 2025. The records only show billed procedures and rough details like age and recorded race/color, not who the people are, how they identify, or whether they needed the surgery. The authors found that the balance shifted from mostly feminizing procedures toward an equal split by 2024–2025, but that the two sides of that split involved very different types of surgery.
- **Why it matters**: Public health systems are a growing source of data on gender-affirming care, so how these records are counted and interpreted matters for monitoring. The paper's main caution is that equal totals can hide very different procedure mixes, and that questions of access and equity need person-level or patient-reported data that these records lack.
- **Background needed**: - Gender-affirming surgery: operations that change a person's body to better match their gender identity; here, "feminizing" or "masculinizing" is inferred from the billing code.
- Hospital Information System (SIH): Brazil's administrative database of hospital admission billing, released as monthly state files.
- Unified Health System (SUS): Brazil's publicly financed health system.
- Authorization (AIH): a billing record for a hospital admission, not a clinical chart.
- Versioned classification: procedure code definitions that change over time, so the same code may mean different things in different years.
- Descriptive study: reports patterns and counts without testing causes.
- Habilitated hospitals: hospitals officially approved by the health ministry to perform a given service.
- Parda: a Brazilian census category for mixed-race or brown people, used here as recorded. · level: intermediate

<details><summary>Original abstract</summary>

Hospital admission authorizations from publicly financed health systems are increasingly used to describe gender-affirming surgery, although they record billed procedures whose feminizing or masculinizing direction can be inferred from the code, without identifying people, self-reported gender identity or clinical need. This nationwide descriptive study examined the authorizations for gender-affirming surgery processed by the Brazilian Unified Health System from 2014 to 2025, which were selected from 3,888 public monthly state files of the Hospital Information System with a historically versioned classification of procedure codes. Of the 1,375 selected authorizations, 711 corresponded to directly feminizing procedures, 428 to directly masculinizing procedures and 236 to a complementary procedure that was analyzed separately. The feminizing share of the directly classified authorizations decreased from 81.7% (196/240) in 2014-2018 to 72.2% (213/295) in 2019-2023 and to 50.0% (302/604) in 2024-2025, proportions that describe composition within periods of unequal length and cannot be read as population rates. In 2024-2025, bilateral mastectomy accounted for 264 of the 302 masculinizing authorizations (87.4%), whereas bilateral breast reconstruction with silicone implants accounted for 118 of the 302 feminizing authorizations (39.1%). The median recorded age was 35 years in feminizing and 30 years in masculinizing authorizations over the whole period, and 34 and 29 years when the comparison was restricted to 2024-2025. The brown (parda) race/color category was recorded in 42.6% (303/711) of feminizing and 61.0% (261/428) of masculinizing authorizations, in a comparison pooled over the whole period and not adjusted for period or procedure. The number of hospitals habilitated for these surgeries remained at five from 2014 to 2022 and doubled in 2023. All aggregate results were reproduced by an independent pipeline that re-read every original public file. It was observed that the equal numbers of feminizing and masculinizing authorizations in the most recent period resulted from markedly different procedure portfolios, which suggests that the monitoring of publicly funded gender-affirming surgery may benefit from procedure-specific indicators and versioned code definitions, while questions of access and equity would require person-level and patient-reported data.

</details>

### [Developing a Stakeholder-Driven One Health Collaboration Framework for Bovine Tuberculosis Control at the Human-Animal Interface in Lundazi and Monze Districts, Zambia](https://www.medrxiv.org/content/10.64898/2026.11.23.26368721v1)
*Phiri, A.; Zulu, M.; Phiri, M. et al.* · `public and global health` · medRxiv doi:10.64898/2026.11.23.26368721 v1 · relevance 0.07

- **In one sentence**: A qualitative study from Lundazi and Monze districts in Zambia, based on 10 focus groups (104 participants) and 10 key informant interviews, that identifies barriers to veterinary-medical collaboration on bovine tuberculosis and proposes a five-pillar One Health collaboration framework.
- **In plain words**: Bovine tuberculosis is a cattle disease that can also infect people, spreading through raw milk, undercooked meat, and handling infected carcasses. The researchers held group discussions and interviews in two Zambian districts with farmers, abattoir workers, vets, doctors and government officials to find out why the human and animal health sectors do not work together well. They found poor awareness among farmers and abattoir workers, weak lab capacity to tell the cattle strain from the human strain, and no formal coordination, and they propose a framework for district-level teamwork.
- **Why it matters**: The paper addresses a neglected zoonotic disease in a setting where human and animal health services often operate separately, so its practical framework may be of interest to public health planners. The text does not report any measured outcome from applying the framework, so its real-world effect is untested.
- **Background needed**: - Zoonosis: a disease that passes between animals and people.
- Mycobacterium bovis: the bacterium that causes bovine tuberculosis in cattle; it is distinct from the M. tuberculosis that causes human TB, though the two are hard to tell apart in basic labs.
- One Health: an approach that treats human, animal and environmental health as linked and calls for joint work across sectors.
- Focus group discussion: a moderated group conversation used to collect people's views.
- Key informant interview: an in-depth interview with a person holding a specific role or expertise.
- Qualitative thematic analysis: a method of finding recurring themes in transcribed interviews rather than counting outcomes.
- Carcass condemnation: when meat from an animal is rejected as unfit for sale after inspection. · level: intermediate

<details><summary>Original abstract</summary>

Background: Bovine tuberculosis, caused by Mycobacterium bovis, is a neglected zoonosis at the human-animal interface in Zambia, particularly affecting cattle-dependent rural communities in Eastern and Southern Provinces, where cattle are central to livelihoods, nutrition, and cultural identity. While Zambia has a One Health Strategic Plan 2022-2026 and a One Health Secretariat under Zambia National Public Health Institute, operational collaboration between veterinary and medical sectors at district level remains fragmented, contributing to diagnostic gaps, under-reporting, and continued transmission through consumption of raw milk, undercooked meat, and occupational exposure during slaughter and handling of infected carcasses. The disconnect between national policy and district implementation has created a vacuum where frontline workers operate in isolation despite sharing the same disease burden. Methods: This qualitative exploratory study was conducted in Lundazi District (Eastern Province) and Monze District (Southern Province), Zambia, from February to June 2022. Ten Focus Group Discussions were conducted with 104 participants, including cattle farmers, cattle businessmen, abattoir workers, veterinary and para-veterinary professionals, and medical doctors, and ten Key Informant Interviews were conducted with District Veterinary Officers, District Medical Officers, Ministry of Health officials, and Ministry of Fisheries and Livestock officials. Participants were purposively selected based on their role, experience, and knowledge of bovine tuberculosis and One Health collaboration. Discussions were held in local languages (Tumbuka, Tonga, Chewa), audio-recorded with consent, transcribed verbatim, translated into English, and imported into NVivo 12 (QSR International, Melbourne, Australia) for thematic analysis following Braun and Clarke's six-step approach, with framework matrices for triangulation and trustworthiness. This methodological rigor ensured that diverse voices from community to policy level were systematically captured and compared. Results: Five themes emerged: (1) awareness of bovine tuberculosis, (2) socio-economic impacts, (3) public health impacts, (4) cultural practices and transmission, and (5) collaboration gaps and proposed framework. Medical and veterinary professionals demonstrated excellent awareness, while cattle farmers and abattoir workers showed poor awareness. Socio-economic impacts included reduced milk yield and carcass condemnation. Key barriers to collaboration included lack of diagnostic capacity at district hospitals to differentiate Mycobacterium bovis from Mycobacterium tuberculosis, siloed training curricula, absence of formal round-table coordination mechanisms, and limited funding. An existing enabler was informal collaboration in meat inspection between veterinary assistants and environmental health officers. Based on these findings, a five-pillar One Health Collaboration Framework is proposed. This framework was co-constructed from participant recommendations, making it contextually grounded and acceptable to end-users. Conclusion: Effective control of bovine tuberculosis in Zambia requires institutionalized One Health collaboration, moving from informal ad hoc interactions to formal governance structures. The proposed framework provides a practical, low-cost and contextually grounded roadmap for district-level implementation and is applicable to other zoonoses such as brucellosis, anthrax and rabies. Its implementation can help break the cycle of under-reporting and under-funding that currently sustains zoonotic transmission in rural Zambia

</details>

## Psychiatry and neurology

### [Plasma proteomic markers of cognitive and brain aging in a multi-ethnic cohort](https://www.medrxiv.org/content/10.64898/2026.11.22.26368682v1)
*Wood, B.; Wood Alexander, M.; Clappison, A. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.22.26368682 v1 · relevance 0.09

- **In one sentence**: A plasma proteomics study measuring 220 blood proteins in 250 older adults from three ethnic groups, linking protein levels to cognition, brain MRI measures, and cognitive decline, with partial replication in 1,381 ADNI participants.
- **In plain words**: Researchers checked about 220 proteins in blood samples from 250 older adults of Chinese, South Asian, and non-Hispanic White background, and compared them with thinking test scores and brain scans. Blood levels of proteins tied to brain disease, nerve-cell connections, oxidative stress, and inflammation were linked to poorer cognition, and some inflammatory proteins were linked to signs of small blood-vessel damage in the brain. Several findings were then checked in a separate, much larger US dataset, the Alzheimer's Disease Neuroimaging Initiative.
- **Why it matters**: Most Alzheimer's and brain-aging biomarker research has been done in mostly White populations, so testing these blood markers in more ethnically diverse groups is a useful check on whether they hold up more broadly. The findings point to candidate blood markers for brain aging, but the text does not show that they can be used clinically, and the associations described are not proof of cause.
- **Background needed**: - Proteomics: measuring large numbers of proteins at once in a blood sample.
- Plasma: the liquid part of blood, used here as the sample.
- Tau (pTau): a protein that forms tangles in Alzheimer's disease; phosphorylated forms are used as disease markers, and BDpTau is a brain-derived form measured in blood.
- Entorhinal cortex: a memory-related brain region that thins in early Alzheimer's.
- Small vessel disease: damage to the tiny blood vessels deep in the brain, often seen on MRI.
- Cardiometabolic risk: conditions such as diabetes, high blood pressure, and obesity.
- Replication: testing earlier findings in a separate group to see if they hold.
- ADNI: a large, long-running US study of people with and without Alzheimer's disease. · level: research-level

<details><summary>Original abstract</summary>

Advances in ultrasensitive proteomics offer opportunities to characterize molecular pathways underlying brain aging. We measured 220 plasma proteins using NULISAseq Neuro220 in 250 Chinese, South Asian, and non-Hispanic White older adults (mean age=68.2 years, 70.4% female). Proteins implicated in neurodegenerative diseases (including brain-derived phosphorylated Tau, BDpTau), synaptic function, oxidative stress, and inflammation were associated with poorer cognition. Phosphorylated Tau205 was associated with reduced entorhinal thickness, whereas inflammatory proteins were associated with imaging markers of cerebral small vessel disease. Several findings were replicated in 1,381 participants in the Alzheimer's Disease Neuroimaging Initiative, including associations of BDpTau species, NPTX2, BACE1, TREM1, CCL17, PRDX6, and IGF1R with cognitive decline and clinical progression. Cardiometabolic risk factors were associated with widespread proteomic alterations, many of which were also linked to poorer brain health. These results identify promising molecular markers of brain aging and extend proteomic research to ethnically diverse populations historically underrepresented in Alzheimer's disease research.

</details>

### [Nigral volume as a marker for Lewy body copathology in Alzheimer's disease](https://www.medrxiv.org/content/10.64898/2026.11.23.26368759v1)
*langley, j.; Hwang, K. S.; Hu, X. P.* · `neurology` · medRxiv doi:10.64898/2026.11.23.26368759 v1 · relevance 0.08

- **In one sentence**: In 73 ADNI participants with clinical Alzheimer's disease or mild cognitive impairment, lower antemortem neuromelanin-MRI substantia nigra volume tracked with autopsy-confirmed Lewy body copathology and with greater nigral hypopigmentation at autopsy, in a single-cohort study.
- **In plain words**: Some people diagnosed with Alzheimer's disease also have Lewy body deposits, abnormal protein clumps in the brain that are more typical of Parkinson's disease and dementia with Lewy bodies. This study asked whether a special brain scan, which measures the size of a small midbrain region called the substantia nigra, can help spot those cases while people are still alive. Among 73 people who had both scans and autopsies, those with Lewy body deposits had a smaller nigral volume, and adding this measure improved a simple prediction model.
- **Why it matters**: Lewy body copathology is linked to earlier symptoms and faster cognitive decline, so a non-invasive way to flag it before death could matter for diagnosis and trial selection. The authors themselves note this is one cohort, with several years between scan and autopsy, so the result needs replication before it is relied on.
- **Background needed**: - Alzheimer's disease (AD): the most common dementia, marked by amyloid plaques and tau tangles.
- Lewy bodies: clumps of the protein alpha-synuclein found in Parkinson's disease and dementia with Lewy bodies; they can co-occur with AD.
- Mild cognitive impairment (MCI): noticeable memory or thinking problems that do not yet meet the threshold for dementia.
- Substantia nigra: a midbrain area that produces dopamine and loses cells in Parkinson's disease; its dark color comes from neuromelanin.
- Neuromelanin-sensitive MRI: a scan sequence that makes the pigmented substantia nigra visible, so its size can be measured.
- Autopsy confirmation: the diagnosis of Lewy body pathology was made after death, which is the reference standard here.
- ADNI: the Alzheimer's Disease Neuroimaging Initiative, a large public research cohort. · level: research-level

<details><summary>Original abstract</summary>

Background: Lewy body (LB) copathology in Alzheimer's disease (AD) is associated with earlier symptom onset and faster cognitive decline. Depigmentation of substantia nigra pars compacta (SNc) volume is seen in both Parkinson's disease and dementia with Lewy bodies. We examined whether lower antemortem SNc volume was associated with autopsy confirmed LB pathology in patients with AD or mild cognitive impairment (MCI). Methods: Seventy-three participants with a clinical diagnosis of AD or MCI, neuromelanin-sensitive MRI, and subsequent neuropathologic assessment from the Alzheimer's Disease Neuroimaging Initiative were studied. At autopsy, 33 participants had LB pathology (LB+) and 40 had no LB pathology (LB-). We compared SNc volume between groups using analysis of covariance adjusted for age and sex. Within the LB+ group, we assessed the association between SNc volume and nigral hypopigmentation using Spearman correlation. In a secondary analysis, we tested whether adding SNc volume to a logistic regression mode containing age, sex, and executive function improved model fit for autopsy-defined LB status. Results: LB+ participants had greater nigral hypopigmentation at autopsy and lower antemortem SNc volume than LB- participants. The adjusted mean difference in SNc volume (LB+ minus LB-) was -66 mm3 (95% confidence interval -115.9 to -16.2, P=0.010). Within the LB+ group, lower SNc volume was associated with greater hypopigmentation (Spearman rho;=-0.373, P=0.032). Among 71 participants with complete model data, adding SNc volume improved model fit (likelihood ratio=8.67, P=0.003). The combined model had an in sample area under the receiver operating characteristic curve of 0.770 (95% confidence interval: 0.661-0.879). Conclusion: The correspondence between lower antemortem SNc volume and greater hypopigmentation at autopsy supports the use of neuromelanin-sensitive MRI to characterize nigral involvement in AD or MCI with LB copathology. These findings are based on a single cohort, and the interval of several years between imaging and autopsy limits how closely the pigmentation ratings reflect nigral integrity at imaging.

</details>

## Oncology

### [Integrated real-world and translational studies nominate CREB binding protein/EP3001 inhibition to overcome androgen receptor pathway modulator resistance in men with prostate cancer](https://www.medrxiv.org/content/10.64898/2026.11.24.26368506v1)
*Somarelli, J. A.; Dougherty, B. V.; Beckmann, A. G. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.24.26368506 v1 · relevance 0.06

- **In one sentence**: Regulatory network models built from multi-omic data of over 10,000 prostate cancer patients nominate EP300/CBP as a target in androgen pathway modulator-resistant disease, supported by preclinical work with the inhibitor pocenbrodib and one clinical case.
- **In plain words**: Prostate cancer often stops responding to hormone-blocking drugs over time, and doctors need new targets for these resistant tumors. The authors used computer models of gene and protein activity from thousands of patients to look for weak points, and the models pointed to a pair of related proteins, CBP and EP300. A new drug that blocks them, pocenbrodib, worked in lab and animal tests, and the authors report that it also helped one patient.
- **Why it matters**: Resistance to androgen-targeting therapy is nearly universal, so a new, actionable target is clinically relevant. The work connects patient-data modeling with lab and clinical testing, though the clinical evidence described here is a single patient, so the finding is early.
- **Background needed**: - Androgen pathway modulators (APMs): drugs that block male sex hormone (androgen) signaling, used in advanced prostate cancer.
- Resistance: the tumor keeps growing despite these drugs.
- Androgen receptor: a protein in cells that responds to androgens and drives prostate cancer growth.
- EP300 / CBP: two closely related proteins that switch genes on or off by adding chemical tags (acetylation) to other proteins.
- Regulatory network model: a map of which genes and proteins influence which others, built from large datasets.
- Multi-omic data: measurements across several layers of biology, such as genes, RNA, proteins and modifications.
- Acetylomics: measuring acetylation changes across many proteins.
- Oxidative phosphorylation and fatty acid metabolism: cell energy-producing pathways.
- Preclinical: tested in cells and animals, not yet proven in people. · level: research-level

<details><summary>Original abstract</summary>

Androgen pathway modulators (APMs) have significantly improved outcomes for men with metastatic prostate cancer, but the evolution of therapy resistance is nearly universal, and there remains a major clinical need to identify actionable vulnerabilities for therapy-resistant disease. To address this need, we employed regulatory network models that leverage multi-omic data from over 10,000 prostate cancer patients with longitudinal clinical data. Analysis of the architecture of the network models identified EP300 as the top actionable target associated with androgen receptor-mediated therapy resistance. These observations were validated using a novel inhibitor of CBP/EP300, pocenbrodib, which showed preclinical activity in vitro and in vivo. Acetylomics analysis and functional studies pinpointed inhibition of oxidative phosphorylation and fatty acid metabolism as key mechanisms of action for pocenbrodib. Clinical benefit for this agent was demonstrated in a patient with metastatic APM-resistant prostate cancer (NCT04575766), highlighting CBP/EP300 as a key target for further translation.

</details>

### [Direct tumour-adipocyte contact / Stroma AReactive Invasion Front Areas (TAC/SARIFA) in advanced oropharyngeal cancer](https://www.medrxiv.org/content/10.64898/2026.11.22.26368676v1)
*Haas, S.; Maerkl, B.; Peiper, A. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.22.26368676 v1 · relevance 0.03

- **In one sentence**: A monocentric retrospective study of 78 advanced (pT3–pT4) oropharyngeal squamous cell carcinomas assessing whether tumour-adipocyte contact (TAC/SARIFA) on routine H&E slides relates to overall survival, recurrence-free survival, p16 status, and nodal findings.
- **In plain words**: This paper looks at a pattern seen under the microscope where cancer cells touch fat cells at the edge of a tumour, in throat cancers (oropharyngeal cancer). The researchers reviewed 78 patients treated between 2005 and 2023 and checked whether this pattern was present in the tumour and its lymph nodes. They then compared it with how long patients survived and how long they stayed free of recurrence.
- **Why it matters**: Among these 78 patients, the pattern was linked to shorter overall survival and was almost always found with extranodal extension (cancer breaking out of a lymph node), which may make it a cheap extra signal from slides already prepared. The recurrence result was not statistically significant, and the single-centre, retrospective design means the finding is a possible risk factor that needs confirmation in larger studies.
- **Background needed**: - Oropharyngeal cancer: cancer of the throat behind the mouth, often linked to HPV infection; p16 is a protein marker used as a stand-in for HPV.
- H&E staining: the standard pink-and-purple stain pathologists use to read tissue slides.
- SARIFA / TAC: a pattern at the invasive edge of a tumour where cancer cells directly contact fat cells (adipocytes), thought to reflect how tumours invade surrounding tissue.
- Retrospective study: looks back at existing patient records rather than following patients forward in a controlled trial.
- Overall survival vs. recurrence-free survival: time until death from any cause vs. time until the cancer returns.
- Extranodal extension (ENE): cancer spreading beyond the capsule of a lymph node into surrounding tissue, a marker of more aggressive disease.
- p-value: a measure of how likely a result is to arise by chance; below about 0.05 is usually called statistically significant. · level: intermediate

<details><summary>Original abstract</summary>

Introduction: Stroma areactive invasion front areas (SARIFA) are a histopathological phenomenon at the tumour invasion front characterised by direct tumour-adipocyte contact (TAC). It can be detected on histological Haematoxylin-Eosin (H&E) stained tumour slides. TAC/SARIFA has emerged as a strong negative prognostic factor in several tumour entities. In this monocentric retrospective study, we aim to elucidate the impact of TAC/SARIFA in oropharyngeal cancer. Materials and methods: 78 cases of pT3 to pT4 oropharyngeal squamous cell cancer from 2005 to 2023 and their corresponding lymph nodes were analysed for the occurrence of TAC/SARIFA. Besides, we compared overall survival rates, recurrence-free survival (RFS) and association with biological and pathological tumour characteristics. Results: In total, overall survival was significantly reduced in TAC/SARIFA-positive tumours (p=0.014). Moreover, TAC/SARIFA positive primary tumours are associated with TAC/SARIFA positive lymph nodes (p<0.001) and extranodal extension (ENE) (p=0.032). Finally, RFS in TAC/SARIFA-positive tumours was reduced, but not significantly (p=0.072). No significant difference was found between p16 positive and p16 negative tumours and prevalence of TAC/SARIFA. Conclusion: TAC/SARIFA is a possible prognostically relevant risk factor in oropharyngeal cancer. When detected in the primary tumour or lymph nodes, it is associated with reduced overall survival rates and tendency towards shorter RFS. TAC/SARIFA-positive lymph nodes almost always show ENE.

</details>

## Health informatics and medical AI

### [Effect of a feedback loop on clinical prediction model performance](https://www.medrxiv.org/content/10.64898/2026.11.23.26368745v1)
*Pacynko, S.; Sperrin, M.; Jenkins, D.* · `health informatics` · medRxiv doi:10.64898/2026.11.23.26368745 v1 · relevance 0.17

- **In one sentence**: A simulation study of how updating a clinical prediction model with data from patients whose treatment was guided by that same model affects calibration, discrimination and treatment-threshold risk assignment, with and without unmeasured confounding.
- **In plain words**: Doctors increasingly use computer models that estimate a patient's risk of a bad outcome and then guide whether to start treatment. When such a model is later retrained on data collected after its own advice changed who got treated, its predictions can drift and become less accurate. This paper uses computer simulations, with settings loosely based on heart disease prediction and treatment, to measure how much this happens and whether recording the treatment itself helps.
- **Why it matters**: Models that steer treatment can undermine their own future accuracy, which matters for any AI tool deployed in care and updated over time. The authors say the findings agree with earlier work, and the abstract highlights that unrecorded confounding (hidden factors that affect both treatment and outcome) still degrades performance even when treatment is included, so monitoring after deployment is needed.
- **Background needed**: - Clinical prediction model: a formula or algorithm that turns patient data into a estimated probability of an outcome, such as a heart attack within a set time.
- Calibration: whether predicted risks match observed frequencies (calibration-in-the-large checks overall level; calibration slope checks whether predictions are too spread out or too compressed).
- C-statistic: how well a model ranks patients who will and will not have the outcome; 0.5 is chance, 1 is perfect.
- Treatment threshold: the risk level above which treatment is recommended.
- Feedback loop: the model's decisions change the data it later learns from.
- Unmeasured confounding: a hidden factor that influences both who gets treated and the outcome, so it is not in the data.
- Simulation study: the researchers generate synthetic patient data under chosen rules rather than using real patients. · level: research-level

<details><summary>Original abstract</summary>

Clinical prediction models (CPMs) that guide treatment-initiation, and therefore affect patient outcomes, may create feedback loops when updated using data from patients whose care they influenced. Treatment can alter predictor-outcome relationships and outcome prevalence, potentially reducing model performance. This simulation study aims to quantify this effect using setting parameters based on cardiovascular disease prediction and intervention and assess if including a treatment variable in the model mitigates any performance degradation. In the simulation, models were developed to predict the probability of a binary adverse outcome, guide treatment allocation, and then updated using data containing patients in whom the model was applied. Scenarios varied treatment inclusion as a predictor in the model and the presence of unmeasured confounding. Performance was assessed with calibration-in-the-large, calibration slope, c-statistic, and correct risk assignment relative to treatment threshold. Without unmeasured confounding, excluding treatment as a predictor resulted in miscalibration, but including treatment solves this problem completely. With unmeasured confounding, performance deteriorated even when treatment was included. These results agree with previous findings and illustrate the likelihood that models that guide interventions may experience performance deterioration due to the difficulty of recording treatment and avoiding unmeasured confounders. Causal inference methods combined with risk prediction may help address this problem. Further research is needed on monitoring techniques to allow detection of this issue post-model implementation.

</details>

### [STREAM: Sequential Transformer for Risk Estimation from Asynchronous Medical Events for Dynamic Postoperative AKI Prediction](https://www.medrxiv.org/content/10.64898/2026.11.21.26368665v1)
*Lu, S.; Ruan, X.; Wang, L. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.21.26368665 v1 · relevance 0.11

- **In one sentence**: STREAM is a Transformer model that treats irregular electronic health record data as a time-ordered stream of clinical events to dynamically predict postoperative acute kidney injury, with event-level interpretability analyses.
- **In plain words**: Doctors need to know how likely a patient is to develop kidney injury after surgery, and that risk changes as new test results and notes come in. This study built a model that reads a patient's hospital records as a sequence of timestamped events and updates its risk estimate each time a new event arrives. In a retrospective set of about 167,000 non-cardiac surgeries, it scored somewhat higher than two comparison models on the measures reported.
- **Why it matters**: Risk estimates that update as information accumulates could fit real-time clinical decision support, and the authors suggest it could be one component of a future perioperative "digital twin" (a computer model of a patient). The text does not show clinical use or prospective testing, and the gains over the comparison models are modest, so its practical value is still unclear.
- **Background needed**: - Acute kidney injury (AKI): a sudden drop in kidney function, which is a common complication after surgery.
- Electronic health record (EHR): the digital hospital chart, with labs, medications, and notes recorded at irregular times.
- Transformer: a neural network architecture that weighs the relationships between items in a sequence; widely used in language models.
- GRU-D: a recurrent network designed to handle gaps in irregularly timed clinical data.
- AUROC / AUPRC: measures of how well a model ranks patients by risk; AUPRC is more sensitive to rare outcomes.
- Calibration: whether predicted probabilities match observed event rates.
- Retrospective cohort: a study using existing records rather than a new trial.
- Digital twin: a continuously updated computer model of an individual patient. · level: research-level

<details><summary>Original abstract</summary>

Postoperative acute kidney injury (PO-AKI) risk estimates evolve as clinical information accumulates, yet many electronic health record (EHR) models use static or fixed-window representations. We developed STREAM, a perioperative event-stream Transformer that represents irregular EHR data as chronological clinical events and supports surgery-index prediction at surgery completion and event-by-event postoperative AKI prediction. In a retrospective cohort of 167,078 noncardiac surgical episodes, STREAM achieved surgery-index AUROC/AUPRC of 0.942/0.771, the Time-series Transformer 0.933/0.729, and GRU-D 0.926/0.695. Postoperative macro-AUPRC across 6-hour evaluation intervals was 0.589, 0.525, and 0.547, respectively. STREAM showed more consistent calibration across postoperative time points than the comparators. Event-arrival attribution and within-window permutation analysis enabled event-level interpretation of how newly arrived information and fine-grained event ordering shaped evolving risk estimates. These findings support event-stream modeling as an interpretable framework for dynamic, temporally resolved prediction from longitudinal EHR data as well as a potential risk-estimation component for future perioperative digital twins.

</details>

## Econometrics and applied economics

### [Adaptive experiments with observational data: Efficient experimental design and asymptotic time-uniform inference for long-term treatment effects](https://arxiv.org/abs/2611.30595)
*Kentaro Kawato* · `econ.EM` · arXiv:2611.30595v1 · relevance 0.08

- **In one sentence**: The paper proposes using pre-experiment observational data to design adaptive experiments that estimate long-term treatment effects more precisely, with a sequential procedure and time-uniform confidence sequences for early stopping.
- **In plain words**: Some experiments need years before the results that matter most, such as long-term income or health, are visible. This paper uses data gathered before an experiment starts to help decide who to enroll and how to assign treatment, so that the long-term effect can be measured more precisely. The authors also build a way to keep checking the results as participants arrive while still keeping valid error bounds.
- **Why it matters**: Long waits for outcomes delay both research findings and policy decisions, so designs that get more information per participant could matter for many program evaluations. The text reports simulations and one illustration using the Pakistan Graduation experiment, but it does not show how large the gains are in practice, so the practical payoff is still to be tested.
- **Background needed**: - Average treatment effect: the average difference in outcomes between people who receive an intervention and those who do not.
- Long-term outcome: a result measured well after the intervention, which may take years to observe.
- Observational data: records collected without random assignment, here used to predict long-term outcomes from short-term information.
- Semiparametric efficiency bound: the lowest variance any reasonable estimator can achieve without fully specifying the model.
- Adaptive experiment: one where later assignment and sampling decisions depend on data already collected.
- Confidence sequence: a running interval that stays valid when checked after every new participant, allowing early stopping.
- Conditional variance: how spread out outcomes are for people with given characteristics, which the design uses to decide where to focus sampling. · level: research-level

<details><summary>Original abstract</summary>

Estimating long-term treatment effects in experiments requires waiting for outcomes to become observable, which can delay both the evaluation of an intervention and subsequent decisions. Recent econometric work has developed identification methods that combine experimental data with observational data containing long-term outcomes. This paper proposes using observational data available before the experiment begins not only for identification but also for designing adaptive experiments, in which experimental data are collected sequentially. To estimate the long-term average treatment effect as precisely as possible, we express its semiparametric efficiency bound as a function of the covariate sampling and treatment assignment rules and minimize the bound over these rules to characterize an optimal fixed experimental design. This experimental design depends on the treatment-specific conditional variances of the observational prediction of the long-term outcome, which can be learned only from experimental participants. We therefore construct a sequential procedure that learns the experimental design as experimental data accumulate and show that its estimator attains the same limiting variance as an oracle estimator implemented under the optimal fixed experimental design. We further construct an asymptotic confidence sequence whose coverage holds simultaneously over all rounds after a prespecified start, so that the experimenter can inspect the interval after each participant and stop once it excludes zero. Monte Carlo simulations show that the learned experimental design can improve precision and shorten the time to detection relative to baseline sampling and equal-probability assignment. An illustration using the Pakistan Graduation experiment shows how estimated conditional variance heterogeneity informs sampling and treatment assignment.

</details>

### [Place-Based Policy from Space: Evidence from Italy's Inner Areas](https://arxiv.org/abs/2611.31100)
*Nicola Caravaggio, Giuseppe Di Renzo, Giuliano Resce et al.* · `econ.GN` · arXiv:2611.31100v1 · relevance 0.06

- **In one sentence**: A staggered difference-in-differences study of Italy's National Strategy for Inner Areas (SNAI) uses satellite nighttime lights to find that funded municipalities saw their lit area expand, with no detectable change in brightness per lit cell, over 2011–2022.
- **In plain words**: Italy's National Strategy for Inner Areas is a government programme that sends money to remote, struggling towns to fund services and local businesses. This paper asks whether the programme shows up from space, using satellite images of night-time light as a rough gauge of economic activity. Comparing 941 funded towns with 3,112 similar eligible towns, it finds that funded areas lit up over a larger area, but not much brighter where they already had light.
- **Why it matters**: It offers a way to track place-based development policy with yearly satellite data, which can be more frequent than official statistics that are slower and coarser. The text suggests the activity spreads outward rather than intensifying in existing centres, and that the effect is descriptively largest at intermediate funding levels; the paper does not settle how far these findings generalise beyond Italy.
- **Background needed**: - Place-based policy: government programmes targeting specific geographic areas, here peripheral "inner areas" of Italy.
- Difference-in-differences: compares changes over time in treated places against changes in comparable untreated places, with staggered timing of funding.
- Nighttime lights: satellite measurements of artificial light, used as a proxy for economic and human activity.
- Lit area vs. radiance: lit area is how much of a region shows any light; radiance is how bright each lit cell is.
- Comparison groups: the paper tests whether results hold across different sets of control municipalities. · level: intermediate

<details><summary>Original abstract</summary>

This paper evaluates a place-based policy, Italy's National Strategy for Inner Areas (SNAI), using satellite nighttime lights. Targeting structurally fragile and peripheral municipalities, SNAI invests in essential services and economic activities. Staggered difference-in-differences compares 941 funded municipalities with 3,112 eligible controls over 2011--2022. Funding is associated with an expansion of lit area and no detectable change in radiance per lit cell, suggesting that activity extends its footprint rather than intensifying in existing centres. The expansion holds across comparison groups and, descriptively, concentrates at intermediate funding per resident. Annual satellite data can complement slower and coarser statistics.

</details>

## Economic theory

### [Shadow economy as a null set. Measure-theoretic approach to shadow economy](https://arxiv.org/abs/2611.29797)
*Rados\l{}aw A. Kycia, Andrzej Buszko* · `econ.EM` · arXiv:2611.29797v1 · relevance 0.08

- **In one sentence**: The paper proposes modeling the shadow economy as a null set relative to institutional measurement devices, and combines Banach lattices, Lebesgue decomposition, copula theory, Kullback-Leibler divergence and compressed sensing into three regimes for underreporting, hidden flows and audit sampling.
- **In plain words**: The paper asks whether the informal, unreported part of an economy can be defined as something that official measuring systems simply fail to see. It proposes a mathematical framework built around that idea and describes three methods: combining incomplete tax or registry records, estimating hidden money flows from indirect signals such as physical or technological indicators, and sampling audits efficiently to catch large evasion networks. The provided text describes the framework and methods but does not report numerical results or validation.
- **Why it matters**: Measuring the shadow economy is a long-standing problem for tax authorities and economists, and the paper argues that conventional definitions mix up the real activity with the limits of what institutions can observe. Its relevance depends on whether the framework can be tested against real data, which the text only describes as a goal ("testable framework") without showing results.
- **Background needed**: - Shadow (informal or hidden) economy: economic activity that is not recorded by official bodies, such as unreported cash work or untaxed sales.
- Null set: in measure theory, a set that is so small it has zero measure; here, a metaphor for activity that instruments cannot register.
- Measure and measurement instrument: a way of assigning sizes to sets of transactions; "institutional measures" are the counts that tax or registry systems produce.
- Banach lattice / supremum operator: an ordered space of functions; the supremum operator takes the largest value across several partial records to combine them.
- Lebesgue decomposition: splitting a measure into a part that is smooth with respect to a reference and a part that is not.
- Copula: a function that describes how variables are linked, separately from their individual distributions.
- Kullback-Leibler divergence: a measure of how far one probability distribution is from another.
- Compressed sensing: a technique for recovering a sparse signal (one with few nonzero entries) from a small number of random measurements. · level: research-level

<details><summary>Original abstract</summary>

In this paper we asked if the shadow economy can be defined as a system of null sets for institutional measures or sensors that measure economic transactions. As an answer a measure-theoretic testable framework to redefine and quantify the shadow economy was designed. Traditional economic definitions frequently conflate the actual shadow economy with the observational limitations of state institutions. To resolve this, we model the shadow economy as a null set relative to institutional measures and analyze three complementary economic regimes. We explore in this context how standard mathematical tools can be given economic meaning. First, in the low-resolution regime, we apply Banach Lattices and Lebesgue decomposition of a measure to address transaction underreporting by aggregating incomplete institutional registries using a supremum fusion operator. Second, for hidden economic dimensions, we utilize Copula theory and Kullback-Leibler divergence optimization to reconstruct unobserved financial flows from technological and physical indicators. Third, we address audit scalability by modeling the shadow economy as a sparse vector, applying Compressed Sensing to detect high-volume sparse evasion networks through random, incoherent, and privacy-preserving sampling.

</details>

### [Principal Revelations of the Revelation Principle](https://arxiv.org/abs/2611.30612)
*Mark Whitmeyer* · `econ.TH` · arXiv:2611.30612v1 · relevance 0.07

- **In one sentence**: The paper proves a converse to the revelation principle, showing it implicitly requires the designer to assume agents coordinate on her most-preferred equilibrium, and that with private values, independent types and quasilinear payoffs, unrestricted transfers let a principal approximate any mechanism's equilibrium payoff using a direct mechanism with a unique truthful equilibrium.
- **In plain words**: This paper is about how an organizer (the "principal") who designs a game or set of rules for private participants can predict how those participants will behave. The author shows that the standard shortcut for this, the revelation principle, only works if the organizer assumes participants settle on the outcome that is best for the organizer. The paper also finds that when money transfers are unrestricted, the organizer can get close to any achievable result using a simple truthful-reporting scheme.
- **Why it matters**: The revelation principle is a standard tool in mechanism design, used in auctions, contracts and regulation, so a result about what it quietly assumes bears on how those models should be read. The text does not indicate its wider applications, so the reach beyond theory is uncertain.
- **Background needed**: - Mechanism design: building the rules of a game so that self-interested players produce a desired outcome (for example, an auction).
- Principal and agents: the principal is the designer; the agents are the participants whose private information matters.
- Equilibrium: a set of strategies where no participant gains by changing alone; a game can have several equilibria.
- Revelation principle: the claim that one may restrict attention to mechanisms where participants simply report their private information truthfully.
- Private values and independent types: each participant's valuation depends only on their own information, and participants' information is statistically unrelated.
- Quasilinear payoffs: utility is value minus money paid, so money transfers can be traded one-for-one against outcomes.
- Prior: the designer's probability beliefs about participants' private information. · level: research-level

<details><summary>Original abstract</summary>

I prove a converse to the revelation principle, arguing that it is a principle of optimism: if it must hold for all environments (in fact, even just those with private values and independent types) the principal must assume her favorite equilibrium is played by the agents. When the principal knows only that the prior lies in some set, she must additionally assume it is her favorite one. With private values, independent types, and quasilinear payoffs, however, unrestricted transfers allow the principal to approximate any mechanism's equilibrium payoff via a direct mechanism whose unique equilibrium is truthful.

</details>

## Game theory and algorithmic economics

### [Optimal Regret Lower Bounds in Matrix Games](https://arxiv.org/abs/2611.31149)
*Taira Tsuchiya* · `cs.GT` · arXiv:2611.31149v1 · relevance 0.11

- **In one sentence**: The paper proves that deterministic learning dynamics in two-player zero-sum matrix games must incur regret of order sqrt(log m · log n) on some payoff matrix (matching known upper bounds), plus an Ω(min{T, log min{m,n}}) bound for all m, n, T, via an adaptive rank-one construction of the payoff matrix.
- **In plain words**: This paper studies two players who repeatedly play a fixed zero-sum game, each adjusting their randomized choices based on what they have seen so far. The authors show that no deterministic way of adjusting can avoid a certain minimum amount of regret (how much worse off a player ends up than they would have been with the best fixed choice) on some game. They build the hard game step by step, adding a new piece in each round that keeps past feedback the same while pushing up the total regret of both players.
- **Why it matters**: The result pins down the best achievable regret for deterministic methods in this setting, so the known upper bound is now tight up to constants in the stated range. It also gives by-products on how fast averaged strategies approach a Nash equilibrium (a stable outcome where no one gains by switching) and on how many matrix-vector products an algorithm needs to find one; the text does not go further on practical impact.
- **Background needed**: - Zero-sum game: one player's gain is the other's loss; represented by a payoff matrix with m and n actions.
- Mixed strategy: choosing actions with certain probabilities rather than always the same one.
- Regret: the gap between a player's total payoff and the payoff of the best single fixed action in hindsight.
- Hedge / optimistic Hedge: standard online learning rules that shift probability toward actions that have done well.
- Minimax regret: the best worst-case regret any method can guarantee; Θ and Ω denote matching upper and lower growth rates.
- Nash equilibrium: a pair of strategies where neither player can improve by unilaterally changing.
- Deterministic learning dynamic: a fixed rule with no internal randomness.
- Rank-one matrix: a matrix formed by multiplying one column vector by one row vector; used here as the building block of the hard payoff matrix. · level: research-level

<details><summary>Original abstract</summary>

We study learning in two-player zero-sum games, also known as matrix games, in which two players with $m$ and $n$ actions repeatedly select mixed strategies for $T$ rounds. The learning dynamics based on optimistic Hedge guarantee regrets of $O(\log(mn))$, which improve to $O(\sqrt{\log m\log n})$ if each player knows the number of actions of the opponent, whereas matching regret lower bounds have been known only for specific learning dynamics. We prove that, for every deterministic learning dynamic, there exists a payoff matrix for which the maximum individual regret is $\Omega(\sqrt{\log m\log n})$ for a wide range of $m$ and $n$. Together with the upper bound $O(\sqrt{\log m\log n})$, this lower bound shows that the minimax regret of deterministic learning dynamics in matrix games is $\Theta(\sqrt{\log m\log n})$ in this regime. For all $m$, $n$, and $T$, we also prove the lower bound $\Omega(\min\{T,\log\min\{m,n\}\})$. These lower bounds hold even if each player also observes the strategies and the feedback of the opponent. Our main technical contribution is an adaptive construction of the payoff matrix. While running the algorithms of the two players, we add in each round a rank-one matrix that keeps the feedback of the previous rounds unchanged and increases a lower bound on the sum of the regrets of the two players. As by-products, we obtain lower bounds on the rate at which the average strategies converge to a Nash equilibrium and on the query complexity of matrix-vector products that deterministic algorithms need to compute an approximate Nash equilibrium.

</details>

### [A Characterized Softmax for Distributing Standing Across Multiple Affiliations](https://arxiv.org/abs/2611.28391)
*Md Mahedi Hasan Riday, Md Shajalal, Gunnar Stevens* · `cs.GT` · arXiv:2611.28391v1 · relevance 0.10

- **In one sentence**: The paper defines "membership attribution," the problem of splitting a player's standing across overlapping pre-given group tags in a cooperative game, shows the naive ratio-based split fails when group signals have mixed sign, and characterizes a restricted-domain softmax solution unique up to a temperature parameter under five requirements, with a sixth fixing the temperature's sign and a seventh (shown independent via counterexample) forcing one shared temperature.
- **In plain words**: The paper asks how a participant's standing should be divided among the groups it already belongs to, when those group memberships are fixed in advance and separate from the game being played. The author shows that the obvious proportional split breaks down when a player's evidence points in opposite directions for different groups, which the author describes as common. The proposed alternative, a softmax-style weighting, is shown to be the only rule meeting five stated requirements (up to a tuning constant), and a worked example on a small exact game is said to confirm the requirements numerically.</plain>
<parameter name="why">The text frames this as a fourth question alongside classic cooperative-game problems such as payoff allocation and interaction attribution, which gives it a clear place in that literature. Beyond the stated results, the text does not say what applications it might have, so any wider relevance is unclear from this text alone.</plain>
<parameter name="background">- Cooperative game theory: a setting where players form coalitions and the question is how to divide a shared payoff (e.g., Shapley value).
- Overlapping groups: a player can belong to several groups at once, and these tags are given independently of the game.
- Softmax: a function that turns a list of scores into positive weights that sum to one, with a temperature parameter controlling how sharp the weights are.
- Axiomatic characterization: showing a formula is the only one satisfying a list of stated requirements.
- Mixed sign: some group-level signals are positive and others negative, which breaks ratio-based shares.
- **Background needed**:  · level: research-level

<details><summary>Original abstract</summary>

Cooperative game theory answers canonical questions on payoff allocation (Shapley, Owen), interaction attribution (Grabisch-Roubens, Faith-Shap), and coalition formation and stability. None answers a fourth question that arises whenever players carry known, overlapping group tags fixed independently of the game: how should a player's standing be distributed across the groups it already belongs to? We call this membership attribution, formalize it, and give a complete characterization of its solution. The direct, ratio-based answer is provably invalid whenever a player's group-level signals have mixed sign --- a common, structurally unavoidable case. We propose a restricted-domain softmax construction instead, and prove that, for any player satisfying a precisely defined richness condition on the group structure, it is the unique such map, up to a temperature parameter, satisfying five requirements. A sixth requirement fixes the sign of this temperature; a seventh, shown independent of the rest via an explicit counterexample, forces one shared temperature across all eligible players. A worked example on an exact cooperative game confirms the applicable requirements numerically and shows the construction degrades gracefully, valid but uninformative, when a player's evidence fails to distinguish between its groups.

</details>

## Mathematical finance

### [Model Doubt, Risk Aversion, and the Threshold for Trading: A Geometry of Pricing Measures](https://arxiv.org/abs/2611.28288)
*Amine Mohamed Aboussalah* · `q-fin.MF` · arXiv:2611.28288v1 · relevance 0.06

- **In one sentence**: In a one-period market, an investor who trusts a reference model only up to a Kullback-Leibler divergence radius stops holding risky assets exactly when that radius reaches the smallest divergence of a pricing measure, with doubt for log utility acting like higher risk aversion and a geometric (Pythagorean) identity linking real-world, pricing, and share measures.
- **In plain words**: The paper asks how much doubt about a statistical model an investor can have before they stop buying risky assets altogether. The investor treats any model that is "close enough" to their best guess, measured by a standard distance between probability models, as possible. The authors find a precise threshold for when this investor holds no risky asset, and they illustrate it with about a century of U.S. market data and with the VIX volatility index.
- **Why it matters**: It links a concrete question about investor caution to measurable market quantities such as the VIX and the equity risk premium, which may matter for robust decision-making under model uncertainty. The text reports the empirical figures as the authors' own estimates; how much weight they deserve depends on the reference model chosen, which the text itself notes.
- **Background needed**: - Reference model: the investor's best-guess probability model for future prices.
- Kullback-Leibler divergence: a non-symmetric measure of how different two probability models are; larger means more different.
- Utility function: a way of describing how an investor values wealth; log utility is a common benchmark.
- Relative risk aversion: how strongly an investor dislikes proportional risk; log utility corresponds to 1.
- Pricing (risk-neutral) measure: an adjusted probability model under which asset prices equal discounted expected payoffs.
- Share (stock-numeraire) measure: probabilities re-weighted by using the stock as the unit of account.
- VIX: a market index of expected stock-market volatility over the next month, derived from option prices.
- Entropy premium: an extra return term tied to the Kullback-Leibler-type measure of distance between models.
- One-period market: a model with a single trading date before payoffs are realized. · level: research-level

<details><summary>Original abstract</summary>

How much model doubt can an investor bear before they stop trading? Our investor treats every model within a given Kullback-Leibler divergence of their reference model as plausible. In a finite one-period market, they hold no risky asset exactly when this doubt reaches the smallest divergence of a pricing measure from their model, for every smooth, strictly increasing, strictly concave utility; non-traded claims then have intervals of no-trade prices. Below this threshold, for log utility and in a given market, doubt acts exactly like higher constant relative risk aversion; their robust pricing measure moves from the log-utility measure toward the pricing measure at that smallest divergence. With a century of U.S. data, a log investor who doubts the Black-Scholes mean return over its 95% confidence interval acts like a fully trusting investor with relative risk aversion of about 1.8 instead of 1. Implied doubt turns a quote into a radius; the mean VIX implies doubt beyond the threshold, but whether significantly so depends on the reference model. By a known identity, real-world, pricing, and share (stock-numeraire) measures form a triangle whose Pythagorean defect is a log risk premium; one side is half the squared (ideal) VIX times the horizon. Since 1990, the U.S. defect averages about 10% per year, about 1 point of it entropy premium.

</details>

### [Gated Payoff-Weighted Net Profit Maximization For Online Portfolio Selection With Transaction Costs](https://arxiv.org/abs/2611.29552)
*Grace Chengrong Xie, Alvey Qianli Lin, Wai Ki Ching* · `q-fin.PM` · arXiv:2611.29552v1 · relevance 0.06

- **In one sentence**: The paper proposes a gated, payoff-weighted combination of net-profit-maximization portfolio experts driven by calibrated AOLMA price-relative forecasts, evaluated for online portfolio selection under a 0.1% transaction cost on nine datasets.
- **In plain words**: This paper is about how to automatically reallocate money across several investments one day at a time, while paying a small fee each time you trade. The authors found that a forecasting method they build on tends to overstate how much prices will move, so they added a "gate" that learns, for each asset, how much of the forecast to trust. Their combined strategy reportedly earned about 5.9 times the geometric-mean wealth of the base strategy on nine datasets at a 0.1% fee, and beat it on every dataset.
- **Why it matters**: The work is a targeted refinement of an existing online trading rule, with a concrete claim about calibration and trading costs. Its broader relevance beyond these datasets is not established by the text, which gives no information on out-of-sample periods, risk, or comparisons with other strategies.
- **Background needed**: - Online portfolio selection: repeatedly splitting wealth among assets (e.g., stocks) over time, deciding each period using only past data.
- Relative return: today's price divided by yesterday's price for an asset.
- Transaction cost: the fee or spread paid when buying or selling; here set at 0.1% of traded value.
- Net profit maximization (NPM): a rule that trades only when the expected gain from rebalancing exceeds the trading cost.
- Moving-average forecast: predicting the next price move from a weighted average of recent moves; "adaptive" means the weights change over time.
- Calibration: whether a forecast's stated size matches how large the moves actually turn out to be.
- Geometric mean wealth: the compounded growth rate of wealth across periods, a standard performance measure here.
- Experts and fund combination: several strategies run in parallel, with capital shifted toward those that have performed best. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we study online portfolio selection (OLPS) problems. The net profit maximization (NPM) acting upon Adaptive Online Moving Average (AOLMA), namely the AOLNPM strategy in portfolio selection, trades when forecast gain exceeds the transaction cost. In essence, this method relies heavily on calibrated forecasts. Indeed, we show that AOLMA forecasts overstate the realized relative returns. We therefore design a gate that adjusts how strongly an AOLMA forecast is used; for each asset, it learns the recent mixture proportion assigned to AOLMA from predictive likelihoods against a neutral forecast (no change). The proportion therefore estimates the extent to which the forecast is realized. We then feed the resulting forecast into the NPM portfolio rule, where the gate acts as an asset-specific cost threshold. A payoff-weighted fund combines gated NPM experts with fixed decay factors in proportion to their wealth and needs no learning rate. On nine datasets with a transaction cost rate of 0.1%, our method produces 5.9 times the wealth of AOLNPM in geometric mean and sits above AOLNPM on every dataset, with its preponderance growing with the cost rate.

</details>

## Financial markets

### [Political Orientation and Participation in Prediction Markets: Large Stakes Converge, Small Stakes Diverge](https://arxiv.org/abs/2611.29576)
*Ali Hosseinzadeh, Ali Hosseiny, Reza Jafari* · `physics.soc-ph` · arXiv:2611.29576v1 · relevance 0.06

- **In one sentence**: A complex-network analysis of about 1.14 billion Polymarket transactions that compares how large-scale and small-scale wallets allocate money across topics, split by Trump-only versus Harris-only investors in the 2024 U.S. presidential election.
- **In plain words**: Prediction markets are online platforms where people buy and sell shares on whether future events will happen, so money is put behind their beliefs. This paper studies over a billion trades on Polymarket to see how investment is spread out and how people who bet only on a Trump win or only on a Harris win differ in where they put their money. The main finding is that big investors on the two sides look more alike in how they spread their money across topics, while small investors diverge more and vary more from one another.
- **Why it matters**: It offers a large-scale look at how political views relate to money-backed behavior, which matters for understanding public expectations and how markets reflect beliefs. The text does not say how far these patterns generalize beyond this platform and this election, so the wider significance is uncertain.
- **Background needed**: - Prediction market: a platform where people trade shares that pay out depending on whether an event occurs; prices are read as a crowd's estimate of likelihood.
- Wallet: an account address on a blockchain-based platform; one person may control several wallets, so a wallet is not the same as a person.
- Bipartite network: a graph with two kinds of nodes (here users and events) where links only join one kind to the other.
- Community structure: groups of nodes that are more densely connected to each other than to the rest of the network.
- Concentration / skewed distribution: a small share of participants or events accounts for most of the activity.
- Statistical support: the reported differences passed a formal test that they are unlikely to be due to chance alone. · level: intermediate

<details><summary>Original abstract</summary>

Prediction markets offer a way to study collective expectations and beliefs: people express their views on various events and, by putting money behind their predictions, take on the risks of their judgments. As a result, the scale of investment can reveal additional dimensions of individual behavior and beliefs. In this study, we use a complex network approach to examine the structure of user participation, drawing on roughly 1.14 billion transaction records from the Polymarket platform, covering more than 3.1 million wallet addresses and 764,000 prediction events. To do this, we build a bipartite network of users and events and analyze patterns of investment concentration, connections between topics, and the network's community structure. Our findings show a highly skewed distribution of financial participation: 1\% of events account for 64\% of total transaction volume, while 1\% of wallets account for 79.2\% of total financial participation. We also examine how investment scale and political orientation shape user participation patterns. Focusing on the 2024 U.S. presidential election, we compare users who invested exclusively in a Trump victory or exclusively in a Harris victory, grouping wallets by purchase size rather than by retail or institutional status. The results show that among large-scale investors, capital allocation patterns across topics are more similar between the two political groups; in contrast, these patterns diverge more and vary more among small-scale investors. This result holds across six different ways of representing and comparing the networks, and four of these differences are also statistically supported.

</details>

### [Cleaning correlation matrices with external information: the Maximum Variance estimat](https://arxiv.org/abs/2611.30843)
*S\'ebastien Valeyre* · `q-fin.PM` · arXiv:2611.30843v1 · relevance 0.06

- **In one sentence**: The paper proposes a Maximum Variance (MaxVar) estimator that cleans an empirical correlation matrix by using a grouping of assets (asset classes) to fix its noisy leading eigenvectors, and tests it on 47 futures contracts.
- **In plain words**: Investors and risk managers estimate how assets move together using a table of correlations, but when the history is short that table is very noisy and portfolios built on it perform poorly. This paper proposes a way to tidy up the table by using outside knowledge about which assets belong to the same group, such as stock indices, bonds, or currencies. The authors report that, in a simulated test and on real futures data from 1993 to 2018, the cleaned table gave a somewhat better risk parity portfolio than both the raw table and an existing cleaning method.
- **Why it matters**: Portfolio construction depends heavily on the quality of correlation estimates, so a method that needs fewer parameters and still yields a valid matrix when observations are fewer than assets is practically relevant. The real-data gains are modest (Sharpe ratio 1.28 versus 1.24 and 1.17), and the text does not show how robust they are across other markets or periods.
- **Background needed**: - Correlation matrix: a table giving how strongly each pair of assets moves together.
- Eigenvalues and eigenvectors: the main directions of co-movement in the table and how strong each is; noisy estimates distort both.
- Rotationally invariant estimator: an existing method that adjusts only the strengths (eigenvalues) of the table and keeps its directions.
- Factor model: describing many assets with a small number of common drivers, here fewer parameters (about n) than the full table (about n²/2).
- Positive definite: a mathematical requirement that the matrix be usable for calculations such as inversion.
- Risk parity portfolio: a portfolio that spreads risk evenly across holdings; it requires inverting the correlation matrix.
- Sharpe ratio: return per unit of risk, used to compare strategies.
- Monte Carlo test: a simulation with artificial data where the true answer is known. · level: research-level

<details><summary>Original abstract</summary>

Rotationally invariant estimators clean the eigenvalues of an empirical correlation matrix but keep its noisy eigenvectors. We study an estimator that corrects the eigenvectors by using external information, namely a partition of the assets into groups such as asset classes or regions. The Maximum Variance (MaxVar) estimator restricts the leading eigenvectors to linear combinations of the maximum-variance portfolios of the groups and replaces the rest of the spectrum by a single eigenvalue. It is a factor model with about n parameters instead of n2/2, and it is positive de nite even when the number of observations is smaller than the number of assets n. We apply it to the correlation matrix of 47 futures on stock indices, bonds and currencies, with the three asset classes as groups. In an illustrative Monte Carlo test, in which the reference matrix has the structure assumed by the estimator, the distance to the reference is reduced by one third with respect to the empirical matrix, against less than 10% for the rotationally invariant estimator. The decisive test is the performance of a portfolio on real data: over 1993-2018, the Sharpe ratio of the risk parity portfolio, which involves the inverse of the matrix, is 1.28 with the MaxVar estimator, 1.24 with the rotationally invariant estimator and 1.17 with the empirical matrix, and the advantage increases when the estimation window is shortened.

</details>

## Signal processing

### [Deep-Learning-Based Classiffcation of Relay-Surface Scattering Regimes for NLOS Millimeter-Wave Sensing](https://arxiv.org/abs/2611.30279)
*Haoran Yuan, Guanghua Liu, You Xu et al.* · `eess.SP` · arXiv:2611.30279v1 · relevance 0.08

- **In one sentence**: DEKL, a deep-learning framework with a lightweight KLNet classifier, identifies which scattering regime (specular, structured multipath, diffuse, or no target) dominates relay-surface echoes in NLOS millimeter-wave radar, using Kullback-Leibler-based model selection and confidence-gated iterative decoding.</one_liner>
<parameter name="plain">When radar signals bounce off a relay surface before hitting a hidden target, the surface's roughness changes the echo and can make localization wrong, creating false "ghost" targets. This paper proposes a deep-learning method that reads the radar echo and decides which kind of scattering is dominant, without directly measuring the surface's roughness. The authors report that it discriminates better than the information-criterion-based rules they compared against, in analytical, electromagnetic and radar-measurement tests.
- **Why it matters**: Choosing the right propagation model matters for hidden-object sensing and for digital-twin maps of wireless environments, since a wrong model produces wrong positions. The text does not say how far the gains extend beyond the evaluated cases, so the practical impact is still to be judged.
- **Background needed**: - Millimeter-wave radar: short-wavelength radio used for sensing; its echoes carry information about distance and direction.
- Non-line-of-sight (NLOS): the target is hidden from direct view, so signals reach it only by bouncing off other surfaces such as walls.
- Specular vs. diffuse reflection: a smooth surface reflects like a mirror; a rough one scatters energy in many directions.
- Ghost target: a false detection caused by reflected paths being mistaken for a real object.
- Model selection with Kullback-Leibler information criterion: a statistical way to pick which candidate model best fits the data, penalizing unnecessary complexity.
- Covariance features: summary statistics of how signal channels vary together, used here as network input.
- Digital twin: a computer model of a real environment kept in sync with measurements. · level: research-level

<details><summary>Original abstract</summary>

In non-line-of-sight (NLOS) millimeter-wave sensing, relay-surface scattering alters target echoes and can cause propagation-model mismatch, angle-estimation errors, and ghost targets. DEKL, a deep-learning framework, identifies the dominant scattering regime from radar echoes without measuring surface roughness. Multipath echo models describe specular reflection, structured multipath reflection, and diffuse scattering. These models and a no-target hypothesis define a model-selection problem with unknown parameters. The Kullback-Leibler information criterion yields an adaptive decision rule for selecting among these hypotheses. A lightweight network, KLNet, learns covariance-domain features and combines attention with confidence-gated iterative decoding to avoid repeated likelihood evaluation. Analytical simulations, independent electromagnetic simulations, and radar measurements show that DEKL improves discrimination over the evaluated information-criterion-based rules. Ablations show how attention, confidence supervision, and gated decoding contribute to selective prediction and robustness under controlled covariance perturbations. The predicted regime guides propagation-model selection for radio-environment repre-sentations in wireless-network digital twins and informs NLOS localization and imaging.

</details>

### [From Surface Lakes to Subsurface Signatures in Antarctica with BIOMASS P-Band TomoSAR](https://arxiv.org/abs/2611.28189)
*Francesco Banda* · `astro-ph.IM` · arXiv:2611.28189v1 · relevance 0.08

- **In one sentence**: Uses P-band tomographic SAR from ESA's BIOMASS satellite to probe subsurface scattering in the firn of the Riiser-Larsen Ice Shelf, East Antarctica, where supraglacial lakes have historically formed.
- **In plain words**: Meltwater lakes sometimes form on the surface of Antarctic ice shelves, and their water can seep down into the snow and firn (old, compacted snow) below. This paper uses radar from the new BIOMASS satellite, which sees with longer wavelengths than usual, to look beneath a area where such lakes have formed in the past. The authors report that the radar signal below the surface appears linked to where lakes recurred, with changes in its structure and depth over time.</plain>
<parameter name="why">Standard satellite optical and radar sensors mostly see only the top layer of ice, so a way to look deeper could help track melt and refreeze that affect ice mass estimates. The link between past lakes and lasting traces in the firn is suggestive, but the text is a short summary and does not give the strength of the evidence, so the finding should be read as preliminary.</plain>
<parameter name="background">- Supraglacial lake: a pool of meltwater sitting on top of an ice sheet or ice shelf.
- Firn: partly compacted snow that sits between fresh snow and solid glacier ice; meltwater can percolate through it.
- Ice shelf: a floating extension of land ice at the edge of Antarctica.
- SAR (synthetic aperture radar): a satellite radar that builds images by moving along an orbit.
- P-band: a long radio wavelength (about 70 cm here) that penetrates ice and snow more deeply than shorter wavelengths.
- Tomography (TomoSAR): combining several radar passes to separate signals by depth, like slicing an image into layers.
- Subsurface scattering: radar energy bouncing back from inside the snow or ice rather than from the surface.
- Mass balance: whether an ice body is gaining or losing mass over time.
- **Background needed**:  · level: research-level

<details><summary>Original abstract</summary>

Spaceborne remote sensing of the cryosphere is fundamental to map ice structure and dynamics. Accurate mass balance estimation requires a better understanding of melt/refreeze processes and firn hydrology, whereas spaceborne optical and Radar sensors are mostly limited to near-surface observations. The BIOMASS P-band Synthetic Aperture Radar, launched by European Space Agency in 2025, provides an unprecedented opportunity to gain a more direct access to englacial processes, thanks to the 70 cm wavelength paired with polarimetry, interferometry and tomography. This paper investigates subsurface beneath a region of historical supraglacial lake activity with BIOMASS tomography, at the Riiser-Larsen Ice Shelf in East Antarctica. The main result is that subsurface scattering appears to be related to historical supraglacial lake recurrence, with structural and depth variations over time. This suggests that recurrent supraglacial lake activity may leave persistent hydrological signatures within the firn. Overall, this study highlights the potential of gaining valuable insights into ice sheet hydrology with P-band.

</details>

## Audio and speech

### [Tenlai-TTS 2.0: Continuous-Representation LLM-Based TTS System with End-to-End Training](https://arxiv.org/abs/2611.29226)
*Changfeng Gao, Yong Ren, Jun Yuan et al.* · `cs.SD` · arXiv:2611.29226v1 · relevance 0.08

- **In one sentence**: Tenlai-TTS 2.0 trains a continuous speech-latent encoder, an LLM with an autoregressive diffusion head, a flow-matching mel decoder and a recognition model jointly end to end, then refines predictions with reconstruction and recognition feedback and reinforcement learning, evaluated on Seed-TTS-eval.
- **In plain words**: This paper is about making computer-generated speech from text using a language model that works on smooth, continuous "speech codes" rather than discrete tokens. The usual approach learns these codes separately and then freezes them, which can make them a poor fit for the language model. The authors instead train the whole pipeline together and report lower error rates on the Seed-TTS-eval benchmark, such as character error rate falling from 8.32% to 7.08% on the hard Chinese test set.
- **Why it matters**: It addresses a real design trade-off in modern speech synthesis: codes must keep enough acoustic detail for good audio yet stay predictable for a language model. The reported gains are modest, and the text does not compare against other systems, so its wider significance is unclear.
- **Background needed**: - Text-to-speech (TTS): software that turns written text into spoken audio.
- Large language model (LLM): a neural network that predicts the next item in a sequence; here it predicts speech pieces in order.
- Continuous latents vs. discrete tokens: continuous latents are smooth numeric vectors that avoid rounding information away; discrete tokens are picked from a fixed list.
- Autoregressive: generating one step at a time, each based on the previous ones.
- Diffusion / flow matching: methods that generate data by gradually refining noise into a clean signal; a mel-spectrogram is a standard picture of sound frequencies over time.
- Gaussian bottleneck: a narrow layer that adds noise and limits how much information passes through.
- Character / word error rate (CER/WER): share of words or characters a speech recognizer gets wrong on the synthesized audio; lower is better.
- Speaker similarity: how closely the synthesized voice matches a reference speaker.
- Reinforcement learning: tuning a model using reward signals rather than fixed correct answers. · level: research-level

<details><summary>Original abstract</summary>

Autoregressive text-to-speech (TTS) with continuous speech latents avoids quantization-induced information loss, but typically relies on a latent space that is learned separately and then frozen before language-model training. Such a space must satisfy two competing requirements: it must retain enough acoustic detail for high-fidelity reconstruction, yet be sufficiently structured and regularized to support autoregressive prediction by a language model. We present Tenlai-TTS 2.0, which learns continuous speech representations through end-to-end training to balance acoustic detail with autoregressive predictability. The model comprises a speech encoder with a capacity-controlled Gaussian bottleneck, a large language model (LLM) with an autoregressive diffusion transformer (AR-DiT) head, a flow-matching (FM) mel-spectrogram decoder, and a multi-task recognition model (RM). With energy normalization and fixed-variance Gaussian noise, the bottleneck has a closed-form upper bound on its information rate. Through joint optimization with reconstruction, recognition, and next-patch prediction objectives, we learn continuous speech representations that suit all three tasks and train the LLM and AR-DiT for autoregressive generation. The LLM and AR-DiT are further optimized using differentiable reconstruction and recognition feedback on their predicted latents through the FM decoder and RM. On Seed-TTS-eval, this feedback-based optimization reduces character error rate (CER) from 0.82% to 0.74% on test-zh and from 8.32% to 7.08% on test-hard-zh, and word error rate (WER) from 1.32% to 1.27% on test-en, compared with joint training alone. Subsequent reinforcement learning further reduces CER to 6.29% on test-hard-zh and WER to 1.08% on test-en, with speaker similarity scores of 0.811, 0.766, and 0.784 on test-zh, test-en, and test-hard-zh, respectively.

</details>

### [CAST: A Deployed Speech-to-Text Cascade for Closed Captioning of Entertainment Television](https://arxiv.org/abs/2611.31055)
*Aditya Mishra, Thanish Bolla, Bidisha Sharma et al.* · `cs.SD` · arXiv:2611.31055v1 · relevance 0.07

- **In one sentence**: CAST is a deployed speech-to-text pipeline for closed captioning of long-form entertainment TV that wraps a frozen Whisper large-v3 model with a hierarchical voice activity detector, language identification, lyrics routing, and hallucination detection and repair, evaluated against a WhisperX baseline on in-house and public data.
- **In plain words**: Automatic speech recognition, the software that turns spoken audio into text, struggles with TV shows full of music, sound effects, accents, and overlapping voices. This paper describes a captioning system built around an existing speech model that adds extra steps to find quiet speech, skip silent stretches that cause the model to invent or repeat words, and fix those errors. On 100 internal assets totaling about 60 hours, the authors report lower word error rate and fewer subtitle edits per hour than the WhisperX baseline.
- **Why it matters**: Captioning long entertainment video is a practical, high-volume problem, and the paper argues that segmentation and surrounding steps matter as much as the core model. Its reported production deployment gives it some real-world weight, though the evidence comes from the authors' own in-house data and the public-dataset result is described only briefly.
- **Background needed**: - Word error rate (WER): share of words the system gets wrong; lower is better.
- Voice activity detection (VAD): a step that decides which parts of audio contain speech and which are silence or noise.
- Whisper: an open speech recognition model from OpenAI; "frozen" means its internal weights are not retrained here.
- Hallucination in speech models: when a model outputs plausible-sounding text that was never spoken, often repeating phrases over silence.
- Subtitle edit rate: the human effort, in minutes, needed to correct captions per hour of video.
- Deletion rate: share of spoken words the system drops entirely.
- Closed captioning (CC): on-screen text transcripts for viewers who are deaf or hard of hearing, or who need subtitles. · level: intermediate

<details><summary>Original abstract</summary>

Despite rapid progress in automatic speech recognition (ASR), caption generation for long-form entertainment video remains challenging for content dense in music and effects, rich in accents, crosstalk, and noise. The transcript quality depends on segmentation and surrounding modules as much as the acoustic model. A single pass voice activity detection (VAD) can miss faint, low-energy voice while forwarding near-silent segments that induce hallucination and repetition in an autoregressive decoder. These competing errors motivate a hierarchical VAD that revisits rejected segments under semantic and acoustic retention checks. We present Captioning ASR Stack for Television (CAST), an integrated speech-to-text pipeline for closed captioning (CC) combining frozen Whisper large-v3 with segmentation, language identification, lyrics routing, and targeted hallucination detection and repair on a single NVIDIA L4 GPU. On 100 in-house assets spanning 60.46 hours, CAST reduces normalized WER from 6.99% to 5.36% and subtitle edit rate from 254.2 to 221.9 min/hour against the WhisperX pipeline, and improves deletion rate by 11% on public datasets. We also present the behavior of each stage in the pipeline. CAST entered the production speech-to-text (STT) stage of our CC pipeline in late August 2026; we report the evaluation evidence and path to full-scale operation.

</details>

## Control systems

### [Autonomous UAV Navigation in an Unknown Environment via Multi-Trajectory Model Predictive Control](https://arxiv.org/abs/2611.30463)
*Danilo Saccani, Lorenzo Fagiano* · `eess.SY` · arXiv:2611.30463v1 · relevance 0.17

- **In one sentence**: The paper proposes multi-trajectory MPC (mt-MPC), which optimizes several candidate future state trajectories within one finite-horizon optimal control problem to separate obstacle-avoidance constraints from goal-reaching cost, and applies it to a LiDAR-equipped UAV navigating unknown terrain with recursive feasibility guarantees under a time-invariant environment.
- **In plain words**: This paper looks at how a small drone can plan its flight path while it only partly sees its surroundings through a laser scanner (LiDAR). The authors propose a planning method, called multi-trajectory model predictive control, that considers several possible future paths at once so that avoiding obstacles and reaching the target are handled more separately. In simulation, it performed better than a standard version of the same kind of controller.
- **Why it matters**: Safe navigation with incomplete sensing is a central problem for drones and other autonomous vehicles, so the approach is relevant to that area. The text reports simulation results and theoretical guarantees under a fixed-environment assumption, but says nothing about flight tests or real-world conditions, so its practical reach is uncertain.
- **Background needed**: - Model predictive control (MPC): at each time step, the controller solves a short-horizon optimization over predicted future states and applies only the first control action, then repeats.
- Finite Horizon Optimal Control Problem (FHOCP): the optimization problem MPC solves over a limited look-ahead window.
- Recursive feasibility: the guarantee that if a plan is feasible now, the controller will still find a feasible plan at the next step, so it never gets stuck without a safe option.
- Hierarchical control: low-level loops keep the vehicle stable and follow setpoints, while the high-level controller chooses where to go.
- LiDAR: a laser sensor that measures distances to nearby surfaces, giving only a partial map of the surroundings.
- Time-invariant environment: an assumption that obstacles do not move during the analysis. · level: research-level

<details><summary>Original abstract</summary>

A novel model predictive control (MPC) formulation, named multi-trajectory MPC (mt-MPC), is presented and applied to the problem of autonomous navigation of an unmanned aerial vehicle (UAV) in an unknown environment. The UAV is equipped with a LiDAR sensor, providing only a partial description of the surroundings and resulting in time-varying constraints as the vehicle navigates among the obstacles. The control system layout is hierarchical: the low-level loops stabilize the vehicle's trajectories and track the set-points commanded by the high-level, mt-MPC controller. The latter is required to plan the UAV trajectory trading off safety, i.e. to avoid collisions with the uncertain obstacles, and exploitation, i.e. to reach an assigned target location. To achieve this goal, mt-MPC considers different future state trajectories in the same Finite Horizon Optimal Control Problem (FHOCP), enabling a partial decoupling between constraint satisfaction (safety) and cost function minimization (exploitation). Recursive feasibility and, consequently, persistent obstacle avoidance guarantees are derived under the assumption of a time invariant environment. The performance of the approach is studied in simulation and compared with that of a standard MPC, showing good improvement.

</details>

### [Performance Evaluation of Nonlinear Model Predictive and Sliding Mode Controllers on a 4-Cable Spatial CSPR in Simscape](https://arxiv.org/abs/2611.29748)
*Erfun Bayat Sarmadi, Ali Asadi, Moosa Ayati* · `cs.RO` · arXiv:2611.29748v1 · relevance 0.15

- **In one sentence**: A simulation comparison of nonlinear model predictive control (NMPC) and sliding mode control (SMC) for a four-cable spatial cable-suspended parallel robot, using both an analytical dynamic model with cable elasticity and friction and a MATLAB Simscape Multibody model.
- **In plain words**: This paper looks at how to steer a robot whose arm-like platform is held up and moved by four cables, so it can follow a path precisely. The authors tested two control strategies on the same paths and limits, using both a mathematical model and a physics-based computer simulation. They report that the predictive method tracked the path more accurately and resisted disturbances better, but needed more computing power.
- **Why it matters**: Cable-driven robots are used where large workspaces and high precision are needed, so the trade-off between tracking accuracy and computing cost is practically relevant. The text also suggests that a physics-based simulation can check that an analytical model is consistent, though the text alone does not show how broadly this generalises beyond the studied robot.
- **Background needed**: - Cable-suspended parallel robot: a platform positioned by several cables pulled from fixed anchor points, rather than by rigid links.
- Control system: a method that computes motor commands to make a system follow a desired reference.
- Sliding mode control: a robust feedback method that forces the system onto a chosen surface and keeps it there despite uncertainty.
- Nonlinear model predictive control: at each step, the controller predicts future behaviour with a nonlinear model and optimises its commands over a short horizon, respecting limits.
- Simscape Multibody: a MATLAB tool for simulating the physical motion of mechanical systems.
- Cable elasticity and friction: real-world effects that stretch cables and dissipate energy, which simple models often ignore. · level: intermediate

<details><summary>Original abstract</summary>

This paper offers a comprehensive comparative study between Nonlinear Model Predictive Control (NMPC) and Sliding Mode Control (SMC) applied to a spatial Cable-Suspended Parallel Robot (CSPR) actuated by four cables. The robot is modeled in two parallel ways: (i) via an analytical dynamic model with included cable elasticity and frictional losses, and (ii) in MATLAB Simscape Multibody, capturing realistic physical effects. Both controllers are implemented under identical reference trajectories, system constraints, and tuning strategies. Our results show that NMPC achieves superior tracking accuracy and stronger disturbance rejection compared to SMC, but at the cost of higher computational demand. Moreover, both controllers were tested on an analytical model of the robot and a Simscape model. The close agreement between the two, for both control schemes, confirms the accuracy of the analytical formulation and its consistency with the physics-based simulation. The study highlights the value of physics-based simulation as a complementary tool for validating advanced controllers under realistic conditions, and demonstrates that NMPC offers superior performance for the studied high-precision, constrained CSPR.

</details>

## Fetch statistics

| Topic | Fetched | New | Selected |
|---|---|---|---|
| Probability | 68 | 64 | 2 |
| Differential geometry | 78 | 76 | 2 |
| Partial differential equations | 119 | 116 | 2 |
| Harmonic analysis | 50 | 47 | 2 |
| Complex analysis | 19 | 17 | 2 |
| Operator algebras and spectral theory | 32 | 30 | 2 |
| Algebra | 67 | 64 | 2 |
| Representation theory | 26 | 24 | 2 |
| Number theory | 73 | 71 | 2 |
| Algebraic geometry | 64 | 60 | 2 |
| Topology | 38 | 36 | 2 |
| Dynamical systems | 50 | 45 | 2 |
| Combinatorics | 112 | 106 | 2 |
| Numerical analysis | 69 | 66 | 2 |
| Logic and foundations | 16 | 14 | 2 |
| Mathematical physics | 82 | 78 | 2 |
| Optimization and control | 70 | 66 | 2 |
| Statistics theory | 34 | 31 | 2 |
| Statistical methods and applications | 81 | 77 | 2 |
| AI industry news | 36 | 27 | 5 |
| Model architectures and training | 122 | 118 | 2 |
| Machine learning theory | 24 | 19 | 2 |
| Large language models | 131 | 127 | 2 |
| Computer vision | 407 | 404 | 2 |
| Reinforcement learning | 68 | 62 | 2 |
| AI safety and alignment | 67 | 64 | 2 |
| Interpretability | 9 | 7 | 2 |
| AI for mathematics | 10 | 8 | 2 |
| Robotics and embodied AI | 193 | 191 | 2 |
| Security and cryptography | 106 | 101 | 2 |
| Algorithms and complexity | 52 | 50 | 2 |
| Programming languages and formal methods | 51 | 47 | 2 |
| Systems and networking | 58 | 55 | 2 |
| Human-computer interaction | 66 | 64 | 2 |
| Information theory | 46 | 43 | 2 |
| High-energy theory and gravity | 109 | 102 | 2 |
| Statistical physics | 50 | 45 | 2 |
| Condensed matter | 84 | 80 | 2 |
| Particle physics | 90 | 85 | 2 |
| Nuclear physics | 34 | 32 | 2 |
| Quantum information and computing | 151 | 144 | 2 |
| Optics and atomic physics | 51 | 49 | 2 |
| Fluids and plasma | 55 | 53 | 2 |
| Biological physics | 10 | 7 | 2 |
| Climate, atmosphere and Earth | 22 | 20 | 2 |
| Cosmology | 35 | 31 | 2 |
| Galaxies | 40 | 36 | 2 |
| Exoplanets and planetary science | 20 | 18 | 2 |
| High-energy astrophysics | 57 | 52 | 2 |
| Stars and the Sun | 28 | 25 | 2 |
| Chemical physics | 32 | 29 | 2 |
| Materials science | 79 | 75 | 2 |
| Soft matter and polymers | 18 | 14 | 2 |
| AI for chemistry and materials | 35 | 31 | 2 |
| Biochemistry | 14 | 11 | 2 |
| Pharmacology and drug discovery | 8 | 7 | 0 |
| Computational and systems biology | 87 | 82 | 2 |
| Neuroscience | 46 | 41 | 2 |
| Genetics and genomics | 33 | 30 | 2 |
| Cell and molecular biology | 42 | 40 | 2 |
| Immunology and microbiology | 43 | 37 | 2 |
| Cancer biology | 19 | 15 | 2 |
| Ecology and evolution | 36 | 33 | 2 |
| Plant biology | 18 | 14 | 2 |
| Bioengineering and synthetic biology | 13 | 10 | 2 |
| Mathematical biology (arXiv) | 22 | 20 | 2 |
| Epidemiology | 15 | 14 | 2 |
| Infectious diseases | 6 | 5 | 2 |
| Public and global health | 22 | 18 | 2 |
| Psychiatry and neurology | 27 | 24 | 2 |
| Oncology | 7 | 4 | 2 |
| Health informatics and medical AI | 16 | 12 | 2 |
| Econometrics and applied economics | 22 | 18 | 2 |
| Economic theory | 11 | 8 | 2 |
| Game theory and algorithmic economics | 17 | 15 | 2 |
| Mathematical finance | 13 | 11 | 2 |
| Financial markets | 21 | 16 | 2 |
| Signal processing | 57 | 55 | 2 |
| Audio and speech | 30 | 28 | 2 |
| Control systems | 68 | 66 | 2 |

<!-- {% endraw %} -->
