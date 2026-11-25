# Research digest · 2026-11-25
<!-- {% raw %} -->

New papers posted from about 2026-11-24 to 2026-11-25 (UTC).

> Papers are picked by how closely their wording matches each topic's description (the "relevance" score), not by quality. Summaries are written by AI from the abstract only; open the paper before relying on them.

## Highlights

- **[(n-1)-Dimensional Hausdorff Measure Estimates for Free Boundaries of Infinity Laplace Equations](https://arxiv.org/abs/2611.31013)** (Partial differential equations): The paper studies the boundary between a region where a certain mathematical function is positive and where it is zero, for a nonlinear equation that describes things like optimal extremal behavior and "absorption" of a quantity. The authors show that this boundary is never too irregular: at every sufficiently small scale, a ball of fixed size can be fitted inside the positive region touching the boundary. From this they derive measured bounds on how the boundary can be covered by simple pieces and how much area it can have.
- **[The maximum number of edges in minimal $k$-extendable bipartite graphs](https://arxiv.org/abs/2611.29504)** (Combinatorics): This paper is about graphs, meaning dots joined by lines, and a property called k-extendability: any set of k non-touching pairings between dots can always be completed to pair up every dot. The question is how many lines a "minimal" graph with this property can have, where removing any single line destroys the property. The authors prove a conjectured upper limit on the number of lines for k at least 3 and show that the limit can actually be reached.
- **[LaTSEC: Lattice-Based Threshold Signatures with Native Non-Interactive Identifiable Abort and Compact Per-Party Storage](https://arxiv.org/abs/2611.30063)** (Security and cryptography): This paper is about a way for a group of people to jointly produce a digital signature so that no single person holds the whole signing key, and if someone cheats or sends a bad piece, the group can tell who it was. The authors propose a scheme where each member keeps only one small secret piece and has one public check value, so bad pieces can be traced to their sender without extra back-and-forth rounds of messages. For 60 parties at 128-bit security, they report it tolerates up to 6 corrupted parties, and a random group of at least 46 can sign with probability at least 0.99.

## Probability

### [Support monotonicity for quadratically regularized optimal transport](https://arxiv.org/abs/2611.30214)
*Johannes Wiesel, Xingyu Xu* · `math.OC` · arXiv:2611.30214v1 · relevance 0.17

- **In one sentence**: For quadratically regularized optimal transport with quadratic cost and compactly supported marginals, the paper proves interior nesting of the optimizer's supports as the regularization parameter decreases, under regularity assumptions, in every dimension.
- **In plain words**: This paper studies a way of moving one pile of material onto another as cheaply as possible, where a small penalty term is added to make the solution smoother. The authors ask whether the region where the best plan places material only grows as the penalty gets weaker, and they show that this holds in the interior of the domain, under regularity assumptions, for small enough penalty values. The argument relies on detailed estimates of an auxiliary function and a rescaling trick.
- **Why it matters**: The text gives a concrete nesting result that tracks how the regularized solution approaches the classical (unregularized) optimal map as the penalty goes to zero, which is a basic question in the theory of regularized transport. Its broader connections are not spelled out in the text, so beyond this specialist setting I am not sure how far it reaches.
- **Background needed**: - Optimal transport: finding the cheapest way to rearrange one probability distribution into another, with a cost for moving each unit.
- Coupling: a joint distribution (plan) whose two sides match the given source and target distributions.
- Monge coupling: the classical solution given by a single map from source to target points.
- Quadratic regularization: adding a squared-size penalty to the cost, so the optimal plan is spread out rather than concentrated on one map; the penalty strength is the small parameter epsilon.
- Support: the set of points where the plan puts positive weight.
- Brenier map: the special optimal map for quadratic cost, given by the gradient of a convex function.
- Compact support and interior: the marginal distributions live on bounded sets, and results are proved away from the boundary.
- Density and rescaling: the plan is compared with the product of the two marginals; the paper rescales it by epsilon and studies the limit. · level: research-level

<details><summary>Original abstract</summary>

We study the support of the optimizer $\pi_\varepsilon$ of the quadratically regularized optimal transport problem for quadratic cost and compactly supported marginals. As $\varepsilon$ tends to zero, this support converges to the support of the Monge coupling. We investigate whether the regularized supports are nested as $\varepsilon $ decreases. Under regularity assumptions on the marginal densities, their domains, and the Brenier map, we establish interior support inclusions in every dimension. More precisely, for each compact $K\subset\operatorname{int}X$ and fixed $\theta\in(0,1)$, we prove that $\mathrm{spt}\pi_\delta\cap(K\times Y) \subseteq\mathrm{spt}\pi_\varepsilon\cap(K\times Y)$ whenever $0<\delta\le\theta\varepsilon $ and $\varepsilon$ is sufficiently small. On these points, the rescaled density $\varepsilon d\pi_\varepsilon/d(\mu\otimes\nu)$ is bounded below by a positive multiple of $\varepsilon^{2/(d+2)}$. Our analysis combines sharp potential estimates with affine rescaling and a Liouville theorem that identifies the unique limiting density of the rescaled problem.

</details>

### [Fermat costs and path-dependent first-passage percolation](https://arxiv.org/abs/2611.28268)
*Sandro Gallo, Matthieu Jonckheere, Alejandro H. Wences* · `math.PR` · arXiv:2611.28268v1 · relevance 0.15

- **In one sentence**: The paper introduces a continuum first-passage percolation model on a Riemannian manifold in which the step-cost exponent grows along the path under a control rule, and proves a shape theorem showing the costs converge to deterministic space-time integrals that define a quasi-distance.
- **In plain words**: The paper studies how cheaply one can travel between two points when you are dropped randomly among many scattered points and must hop between them, with the cost of each hop depending on its length and on how far along the route you already are. As the number of points grows, the cheapest travel costs settle into a fixed, predictable pattern. The authors show this limit is not a true distance, because going from a crowded region to a sparse one can be cheaper than the reverse.
- **Why it matters**: The asymmetry of the limiting cost is the stated reason for interest, and the text suggests possible use in machine learning, though it does not show a concrete application. Its relevance beyond probability theory is therefore a suggestion rather than a demonstrated result.
- **Background needed**: - First-passage percolation: a random model where the cost of paths is the sum of random or position-dependent step costs, and one studies the minimal cost between points.
- Shape theorem: a result that the random minimal cost, rescaled, converges to a deterministic limiting shape or cost function.
- Riemannian manifold: a smooth curved space in which distances and volumes are defined locally, generalizing flat Euclidean space.
- Quasi-distance: like a distance but possibly not symmetric (cost from A to B may differ from B to A), and may fail the triangle inequality.
- Step cost exponent alpha > 1: each hop costs its length raised to a power greater than one, so long hops are penalized more than short ones.
- Point density: the points are sampled with a varying density, so some regions are crowded and others sparse. · level: research-level

<details><summary>Original abstract</summary>

We introduce a path-dependent and space-inhomogeneous first-passage percolation (FPP) model in the continuum. Inspired by Euclidean FPP, it is defined through a sample of points drawn from a common density function on a Riemannian manifold. In Euclidean FPP, the cost of each step in a discrete path is given by its length raised to the power $\alpha>1$. In our model, the power $\alpha$ increases as the path progresses, governed by a control mechanism. Consequently, the resulting percolation cost is not a distance. However, we prove a shape theorem showing that, as the number of points goes to infinity, the percolation costs converge to deterministic space-time integrals along curves in the manifold. This limit defines a quasi-distance with the property that traversing a curve from a high-density region towards a low-density one is generally cheaper than in the reverse direction; thus highlighting its potential use in machine learning applications.

</details>

## Differential geometry

### [Gray II, K\"ahler Nullity and Ricci Flow on Generalized Flag Manifolds with Two Isotropy Summands](https://arxiv.org/abs/2611.30716)
*Lino Grama, Ailton R. Oliveira, Francisco V. Oliveira* · `math.DG` · arXiv:2611.30716v1 · relevance 0.20

- **In one sentence**: The paper studies Gray's second curvature identity, Kähler nullity, and normalized homogeneous Ricci flow on generalized flag manifolds with two isotropy summands, for both invariant almost complex structures.
- **In plain words**: The paper looks at a family of smooth curved spaces with a high degree of symmetry (generalized flag manifolds) and asks how their geometry behaves under a few specific rules for measuring and smoothing curvature. The authors show that every symmetric way of measuring distance on these spaces satisfies one known curvature identity, and they track how the special "Kähler" directions of the space change. They also reduce a geometric smoothing process (Ricci flow) to a single equation for one ratio of parameters, and study where that ratio goes over time.
- **Why it matters**: The result gives a fairly complete, explicit picture on a concrete class of spaces, which is useful for testing general conjectures about curvature and geometric flows. The stated finding that the Kähler–Einstein direction attracts while the other Einstein direction repels is a specific dynamical statement; its wider significance beyond these spaces is not established in the text.
- **Background needed**: - Generalized flag manifolds: symmetric curved spaces built from Lie groups, a standard object in homogeneous geometry.
- Isotropy summands: pieces of the space's symmetry data at a point; "two summands" means the simplest nontrivial case.
- Invariant metric: a way of measuring distance that respects the space's symmetries; it is described by a few parameters.
- Almost complex structure: a rotation-like structure on tangent directions; "Kähler" means it is compatible with the metric and closed in a suitable sense.
- Gray's identity: a constraint relating curvature and its derivatives on almost Hermitian manifolds.
- Kähler nullity: the space of directions where the curvature behaves like a Kähler manifold's; "trivial" means it is zero.
- Ricci flow: an evolution of the metric that tends to smooth out curvature, here normalized and reduced to an ODE for one ratio.
- Attracting/repelling: whether nearby starting ratios are drawn toward or pushed away from a fixed value under the flow. · level: research-level

<details><summary>Original abstract</summary>

We investigate Gray's second curvature identity, K\"ahler nullity, and homogeneous Ricci flow on generalized flag manifolds with two isotropy summands. We prove that every invariant metric satisfies Gray's second identity for both invariant almost complex structures. For the non-integrable structure, the K\"ahler nullity is trivial except at a distinguished metric ratio, where it coincides with the vertical distribution of a homogeneous fibration. This distribution is integrable and has totally geodesic leaves. For the integrable structure, the K\"ahler nullity exhibits a different behavior and need not be integrable away from the K\"ahler locus. Finally, we reduce the normalized homogeneous Ricci flow to an autonomous equation for the ratio of the metric parameters. The resulting dynamics identify two invariant Einstein directions and show that the K\"ahler--Einstein direction is attracting, while the other is repelling.

</details>

### [Support functions of sections of $p$-minimal tubes](https://arxiv.org/abs/2611.29625)
*Vladimir G. Tkachev* · `math.DG` · arXiv:2611.29625v1 · relevance 0.18

- **In one sentence**: The paper studies convex hulls of horizontal sections of compact p-minimal hypersurfaces bounded by two parallel planes, proves a viscosity subsolution inequality for their support functions, and derives distance and lifetime bounds for minimal surfaces, including a sharp catenoid-equality bound in R^3.
- **In plain words**: The paper looks at soap-film-like surfaces stretched between two parallel flat planes and at the convex shapes enclosed by their cross-sections at each height. It describes how a standard "support function" measuring those shapes must behave, and uses this to bound how far apart the two planes can be. For ordinary minimal surfaces in three-dimensional space, the bound is sharp and holds with equality only for the catenoid, the classic soap-film shape.
- **Why it matters**: It gives a new analytic route to known rigidity results (Bernstein and Breiner) and extends them to non-convex and multi-component boundaries. The link to the Meeks annulus conjecture, which the authors reduce to a statement about atoms in area functions, may make it relevant to specialists in minimal surface theory, though the text alone does not show how far that reduction goes.
- **Background needed**: - Minimal surface: a surface that locally has the least area for its boundary, like a soap film; p-minimal is a generalization of this notion from a variational/PDE viewpoint.
- Hypersurface: a surface of one dimension less than the ambient space (e.g. a surface in ordinary 3D space).
- Convex hull and support function: the smallest convex set containing a shape, and a function recording how far its flat supporting planes lie from the origin in each direction.
- Viscosity subsolution: a weak notion of solution for second-order partial differential equations, used when solutions may not be smooth.
- Degenerate elliptic inequality: a class of second-order PDE inequalities that may lose strictness in some directions.
- Monge–Ampère type: a nonlinear second-order PDE family common in convex geometry.
- Alexandrov area functions and atoms: measures describing how surface area of a convex body is distributed by normal direction; atoms correspond to edges.
- Catenoid: the surface of revolution formed by a soap film between two coaxial rings.
- Meeks annulus conjecture: a open conjecture about minimal annuli in space. · level: research-level

<details><summary>Original abstract</summary>

Let $M$ be a compact $p$-minimal hypersurface in ${\mathbb R}^{n+1}$ with boundary in two parallel hyperplanes. We study the convex hulls $\Omega(\tau)$ of its horizontal sections through their support function $H(\tau,\cdot)$, without any assumption on the topology of $M$. We prove that $H$ is a viscosity subsolution of a degenerate elliptic inequality. For $n=2$ it is of Monge--Amp\`ere type, and its equality case for minimal surfaces with circular sections is Riemann's system. A posteriori, $H$ is locally semiconvex and every hull is a smooth convex body; the inequality then also holds in the sense of measures, with the edges of the hulls appearing as atoms of Alexandrov's area functions. Averaging over directions gives a catenary-type inequality for the mean width of the hulls. It yields lifetime bounds for $p$-minimal tubes when $n>p$. For minimal surfaces in ${\mathbb R}^3$ it gives a sharp bound for the distance between the planes in terms of the perimeters of the hulls of the boundary curves, with equality only for a catenoid. For one convex curve in each plane this recovers, by a different method, the nonexistence and rigidity theorem of Bernstein and Breiner. The bound extends to non-convex curves and to boundaries with several components. Finally, we show that the Meeks annulus conjecture is equivalent to the absence of atoms in the area functions of the hulls of all intermediate sections.

</details>

## Partial differential equations

### [(n-1)-Dimensional Hausdorff Measure Estimates for Free Boundaries of Infinity Laplace Equations](https://arxiv.org/abs/2611.31013)
*Yantian Chen, Feida Jiang* · `math.AP` · arXiv:2611.31013v1 · relevance 0.18

- **In one sentence**: The paper proves a sharp distance-to-boundary estimate with an explicit optimal constant for free boundaries of nonnegative viscosity solutions to the infinity Laplace equation with strong absorption (Δ∞u = λu₊^m, 0<m<3), yielding density, Lipschitz covering, and (n-1)-dimensional Hausdorff measure bounds that answer a question of Araújo, Leitão, and Teixeira.
- **In plain words**: The paper studies the boundary between a region where a certain mathematical function is positive and where it is zero, for a nonlinear equation that describes things like optimal extremal behavior and "absorption" of a quantity. The authors show that this boundary is never too irregular: at every sufficiently small scale, a ball of fixed size can be fitted inside the positive region touching the boundary. From this they derive measured bounds on how the boundary can be covered by simple pieces and how much area it can have.
- **Why it matters**: It settles an open question posed in a 2016 paper by Araújo, Leitão, and Teixeira, so it is a targeted advance in a specialized area rather than a broad change. The method, a barrier argument whose constant matches a non-degeneracy estimate, is said by the authors to suggest extensions to more general equations, but the text does not show that.
- **Background needed**: - Partial differential equations: equations relating a function to its rates of change in space.
- Viscosity solutions: a weak notion of solution used for nonlinear equations where classical derivatives may fail to exist.
- Infinity Laplacian: a highly nonlinear, degenerate version of the Laplace operator, tied to optimal-control and "steepest slope" ideas.
- Free boundary: the interface separating the region where the solution is positive from where it vanishes, which is not fixed in advance.
- Non-degeneracy estimate: a lower bound saying the solution cannot be too flat near points where it is positive.
- Tangent ball property: the boundary can be touched from inside by a ball of a given radius.
- Hausdorff measure: a generalized way of measuring size of sets; (n-1)-dimensional measure is the surface-area analogue for a boundary in n dimensions. · level: research-level

<details><summary>Original abstract</summary>

We investigate the geometric properties of free boundaries associated with nonnegative viscosity solutions to the infinity Laplace equation with strong absorption $$ \Delta_\infty u=\lambda u_+^m, \qquad \lambda>0,\quad 0<m<3. $$ We first establish a sharp distance-to-free-boundary regularity estimate with an explicit optimal coefficient, which coincides with the constant in the non-degeneracy estimate. This exact matching yields a uniform interior tangent ball property at every sufficiently small scale for every free boundary point. As consequences, we obtain a sharp lower density bound of $1/2$ for the positive phase, a locally finite covering of the free boundary by Lipschitz graphs, and quantitative local estimates for its $(n-1)$-dimensional Hausdorff measure, thereby giving an affirmative answer to the question raised by Ara\'ujo, Leit\~ao, and Teixeira (J. Funct. Anal. {\textbf 270} (2016), no. 6, 2249-2267). The underlying barrier mechanism also suggests possible extensions to more general equations.

</details>

### [Global existence and decay estimates for classical solutions to 2D compressible micropolar fluid equations with vacuum](https://arxiv.org/abs/2611.28657)
*Guo Houbin, Zhu Changjiang, Zhu Qiaolong* · `math.AP` · arXiv:2611.28657v1 · relevance 0.15

- **In one sentence**: Proves global existence and uniqueness of strong and classical solutions for the 2D compressible micropolar fluid equations with far-field vacuum, under a small initial energy assumption but allowing large oscillations, via a priori decay estimates for pressure, velocity gradient and microrotation.
- **In plain words**: This paper studies a mathematical model of a fluid made of tiny particles that can also spin, such as some suspensions or liquid crystals, in a two-dimensional setting where the fluid thins out to empty space (vacuum) far away. The authors show that, if the starting energy of the fluid is small, smooth solutions exist for all time and are unique, even when the starting state varies a lot. Their main tool is to prove that pressure, the rate of flow deformation, and the spin velocity all fade in a controlled way over time.
- **Why it matters**: Questions of whether fluid equations keep smooth solutions forever are basic to understanding them, and vacuum regions make the analysis much harder. The paper is a theoretical result, so its relevance lies in the mathematical method rather than any direct application mentioned in the text; the text does not discuss specific physical uses.
- **Background needed**: - Compressible fluid: a fluid whose density can change, as with gases.
- Micropolar fluid: a fluid model in which each small volume element can also rotate independently, adding a "microrotational velocity" alongside the usual velocity.
- Vacuum: regions where density is zero; "far field vacuum" means the density vanishes at infinity.
- Global existence: a solution exists for all future times, not just for a short while.
- Classical/strong solutions: smooth enough that the derivatives in the equations make sense.
- A priori estimates and bootstrap: bounds derived assuming a solution exists, used to show it cannot blow up and so persists.
- Partial differential equations (PDEs): equations relating a function to its rates of change in space and time. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we consider the Cauchy problem for the two-dimensional compressible micropolar fluid equations with far field vacuum. Under the assumption that the initial energy is sufficiently small, we establish the global existence and uniqueness of strong and classical solutions, allowing for large oscillations in the initial data. The key to the proof is to derive {\it a priori} decay estimates for the pressure, the velocity gradient, and the microrotational velocity, which enable us to close the bootstrap argument. We also handle the difficulties arising from the coupling between the velocity field and the microrotational velocity.

</details>

## Harmonic analysis

### [Multipliers and integration operators on Hardy--Bloch type tent spaces](https://arxiv.org/abs/2611.28895)
*Jiale Chen* · `math.FA` · arXiv:2611.28895v1 · relevance 0.18

- **In one sentence**: The paper characterizes when integration operators J_g and I_g and pointwise multipliers M_g are bounded between Hardy–Bloch type tent spaces BT^p, with complete results for I_g and for J_g and M_g when p<q, and separate conditions when p≥q.
- **In plain words**: The paper studies a family of function spaces on the unit disc in the complex plane, defined using a maximal average of a function's radial derivative taken near the boundary. It asks when three standard operations (integrating a function, and two ways of multiplying by a fixed function g) keep functions inside these spaces in a controlled way. The authors give a full answer for one operator across all exponents, a full answer for the other two when the input exponent is smaller than the output exponent, and separate, not fully matching conditions otherwise.
- **Why it matters**: Questions of when multiplication and integration operators are bounded are basic tools for understanding function spaces, and this work sits where complex analysis meets harmonic analysis. The text does not indicate applications beyond this theory, so its wider significance is uncertain.
- **Background needed**: - Unit disc: the set of complex numbers with modulus less than 1, where holomorphic (complex-differentiable) functions live.
- Bloch-type space: a space of holomorphic functions whose derivative is controlled in a weighted sense.
- Hardy-type space: spaces measuring a function's size near the boundary circle, indexed by an exponent p.
- Tent spaces: spaces of functions on the disc defined via maximal functions taken over cone-shaped regions reaching the boundary.
- Non-tangential maximal function: the largest value of a function over approach regions that meet the boundary at an angle, used to measure boundary behaviour.
- Bounded operator: one that maps the space into itself (or another space) while keeping size controlled by a constant.
- Fractional maximal function: an averaging tool that measures local concentration with a power-law weight; used here in the proofs.
- Synthesis lemma: a technical decomposition tool for rebuilding a function from pieces. · level: research-level

<details><summary>Original abstract</summary>

We investigate the boundedness of integration operators $J_g$ and $I_g$ and pointwise multipliers $M_g$ on Hardy--Bloch type tent spaces $\mathcal{BT}^p$. The main difficulty is that these spaces are defined through a non-tangential maximal function of the radial derivative, which places the problem at the interface of holomorphic function theory and harmonic analysis. We completely characterize the boundedness of $I_g:\mathcal{BT}^p\to\mathcal{BT}^q$ for all $0<p,q<\infty$, and obtain a complete characterization for $J_g$ and $M_g$ when $p<q$. For $p\geq q$, we establish separate necessary and sufficient conditions. The proofs in the case $p\leq q$ are mainly based on some fractional maximal function estimates, whereas those in the case $p>q$ are mainly based on a synthesis lemma. We also give examples showing that several converse implications in the range $p\geq q$ fail.

</details>

### [Perturbed Nevo--Thangavelu maximal functions on two-step nilpotent groups](https://arxiv.org/abs/2611.28400)
*Jaehyeon Ryu* · `math.CA` · arXiv:2611.28400v1 · relevance 0.17

- **In one sentence**: The paper studies L^p boundedness of maximal averages over parabolically dilated, curved convex hypersurfaces lying in a tilted subspace of a two-step nilpotent Lie group, in the low-rank regime, giving a sharp p-range when m=1 and a Łojasiewicz-exponent criterion for m≥2.
- **In plain words**: The paper looks at a way of averaging a function over curved surfaces inside a particular kind of geometric space, and asks for which sizes of function the largest such average stays well behaved. For the simplest case (one extra direction, m=1) the authors pin down exactly which range of sizes works. For higher-dimensional extra directions, they show that a known necessary condition is also sufficient precisely when a certain algebraic measure of how flat the surface can get, the Łojasiewicz exponent, meets a condition.
- **Why it matters**: Maximal operators of this kind are standard tools for controlling averages in harmonic analysis, and the result gives a sharp answer in one case and a clean criterion in the other. The text does not state wider applications, so any connection beyond this area is uncertain.
- **Background needed**: - Maximal operator: takes the largest average of a function over dilated copies of a surface; asking if it is bounded on L^p means asking whether it keeps the function's overall size under control for a range of p.
- L^p spaces: measure of function size; p is an exponent, and boundedness typically holds only for some range of p.
- Nilpotent Lie group: a curved, non-commutative space whose structure is built in layers; here a two-step version, identified with R^d × R^m.
- Exponential coordinates: a way of labeling points of the group by ordinary vectors.
- Parabolic dilates: rescalings that stretch the space by different amounts in different directions.
- Nonvanishing Gaussian curvature: the surface bends in every direction at every point (like a sphere or paraboloid, not flat anywhere).
- Tilted subspace and low-rank regime: the surface sits in a slanted slice of the space, with the tilt setting how degenerate the geometry is.
- Łojasiewicz exponent: a number measuring how flat a smooth function can be near its zeros; used here as the criterion. · level: research-level

<details><summary>Original abstract</summary>

Consider a step-two nilpotent Lie group $G$ identified with $\mathbb R^d\times \mathbb R^m$ in exponential coordinates. We study maximal operators associated with parabolic dilates of smooth convex hypersurfaces with nonvanishing Gaussian curvature in a tilted $d$-dimensional subspace of $G$. We focus on the low-rank regime, where the rank is determined by the group law and the tilt. When $m=1$, we determine the optimal range of $p$ for which the maximal operator is bounded on $L^p(G)$. For $m\ge2$, we characterize, in terms of a {\L}ojasiewicz exponent, when the known necessary condition on $p$ is also sufficient.

</details>

## Complex analysis

### [An extension of Janowski functions with applications](https://arxiv.org/abs/2611.28693)
*Kunle Oladeji Babalola* · `math.CV` · arXiv:2611.28693v1 · relevance 0.08

- **In one sentence**: The paper extends Janowski functions, which are classes of analytic functions subordinate to a Möbius-type function (1+az)/(1+bz), by allowing the parameters a and b to be complex numbers rather than real ones with -1 ≤ b < a ≤ 1, and gives some applications.
- **In plain words**: The paper studies a family of smooth, well-behaved functions of a complex variable that are controlled by two constants. Until now those constants were restricted to real numbers in a certain range. The authors allow the constants to be complex numbers instead and explore what follows from this wider setting, with some applications.
- **Why it matters**: The text gives only the setup and does not state specific results, so its significance is hard to judge from this excerpt. It belongs to geometric function theory, a field that studies how analytic functions map regions of the complex plane, and the applications may be relevant to that field.
- **Background needed**: - Analytic (regular) function: a function of a complex variable z that is differentiable throughout a region, with a power series expansion.
- Subordination: f is subordinate to g if f(z) = g(w(z)) for some analytic self-map w of the unit disk with w(0)=0; roughly, f takes values in the image region of g.
- Janowski functions: analytic functions p with p(0)=1 that are subordinate to the Möbius map (1+az)/(1+bz).
- Möbius map: a ratio of linear expressions in z, which maps circles and lines to circles and lines.
- The paper's change: the constants a and b are moved from real numbers to complex numbers. · level: research-level

<details><summary>Original abstract</summary>

Janowski functions are regular functions of the form $p(z)=1+p_1z+\cdots$, which are subordinate to $L_0(a,b:z)=(1+az)/(1+bz)$ for real numbers $a,b$ such that $-1\leq b<a\leq 1$. In this paper, we expand the space of the constants, $a$ and $b$, of the superordinate function, $L_0(a,b:z)$, to a larger set of complex numbers and provide some applications.

</details>

### [Sharpness of the Brjuno Condition for Hyperbolic Bishop Surfaces](https://arxiv.org/abs/2611.30985)
*Dijia Chen* · `math.CV` · arXiv:2611.30985v1 · relevance 0.06

- **In one sentence**: The paper proves a conjecture of Gong and Stolovitch: for a unimodular, non-root-of-unity, non-Brjuno parameter μ, there is a real-analytic surface in C^2 with Moser–Webster invariant μ that is formally but not holomorphically equivalent to the Bishop quadric Q_γ.
- **In plain words**: This is about the local shape of smooth surfaces in two-dimensional complex space, specifically how they can be matched to a simple reference surface (a "Bishop quadric") by changing coordinates. The question is whether a surface can be matched on the level of infinite power series but not by any genuinely smooth, convergent change of coordinates. The paper shows that such a surface exists for a certain class of rotation-type parameters, confirming a guess made by Gong and Stolovitch.
- **Why it matters**: It sharpens our understanding of when local geometric normal forms can be realized convergently, and it shows that an arithmetic condition (the Brjuno condition on μ) is exactly the right dividing line in this setting. The text does not say more about wider applications, so the broader connections are unclear from this excerpt alone.
- **Background needed**: - Complex plane C and complex two-dimensional space C^2 (pairs of complex numbers).
- A real-analytic surface: a real-dimension-based surface that locally has convergent power series description.
- Bishop quadric: a standard model quadratic surface in C^2 with a parameter γ.
- Formal vs. holomorphic equivalence: two surfaces match via an infinite power series (formal) versus a convergent, genuine change of coordinates (holomorphic).
- Moser–Webster invariant: a number μ on the unit circle that measures the local rotation behaviour of the surface at a special point.
- Root of unity: a number whose power equals 1; these are excluded here.
- Brjuno condition: a number-theoretic condition on how well μ can be approximated by rationals; it governs convergence of certain iterative procedures. · level: research-level

<details><summary>Original abstract</summary>

Let $\mu \in \mathbb{C}$ satisfy $|\mu|=1$, and assume that $\mu$ is not a root of unity and is not Brjuno. Let $Q_\gamma$ denote the Bishop quadric with $\gamma = 1/\sqrt{2+\mu+\mu^{-1}} > 1/2$. Gong and Stolovitch conjectured that there exists a real-analytic surface in $\mathbb{C}^2$ with Moser--Webster invariant $\mu$ that is formally but not holomorphically equivalent to $Q_\gamma$. We prove this conjecture.

</details>

## Operator algebras and spectral theory

### [Trace-class perturbations of Voiculescu's free semicircular families](https://arxiv.org/abs/2611.30882)
*Minghui Ma, Rui Shi, Tianze Wang* · `math.OA` · arXiv:2611.30882v1 · relevance 0.15

- **In one sentence**: For free semicircular families perturbed by small trace-class self-adjoint operators, the type II_1 summand of the generated von Neumann algebra is shown to be the free group factor L(F_Λ), and this is used to show irreducible operators are not trace-norm dense.
- **In plain words**: The paper studies a family of abstract "random-like" operators (free semicircular elements) that are each nudged by a small perturbation of controlled size. It proves that a specific piece of the algebra generated by the nudged operators has the same structure as a known standard object, the free group factor. As a side consequence, it shows that irreducible operators (those with no nontrivial invariant subspaces) do not form a dense set under the trace-class norm.
- **Why it matters**: The result gives a precise structural answer about how far small trace-class changes can alter the algebra generated by free operators, and it bears on the density question for irreducible operators. The text does not say more about wider applications, so its broader significance beyond operator theory is unclear.
- **Background needed**: - Operators: linear maps on a Hilbert space (an infinite-dimensional generalisation of vectors and matrices).
- Trace-class operators: "small" operators whose singular values sum to a finite number; the trace norm measures their size.
- Von Neumann algebra: a self-contained algebra of operators closed under limits; its type (I, II, III) classifies its structure, with type II_1 behaving like a continuous analogue of matrix algebras with a trace.
- Free semicircular family: a collection of non-commuting, free "random" self-adjoint operators whose distribution is the semicircle law.
- Free group factor L(F_Λ): a standard type II_1 von Neumann algebra built from the free group on the index set Λ.
- Murray–von Neumann dimension: a normalised measure of the size of a projection within a II_1 algebra.
- Irreducible operator: one with no nontrivial closed invariant subspace. · level: research-level

<details><summary>Original abstract</summary>

Let $\{s_j\}_{j\in\Lambda}$ be the standard free semicircular family on the full Fock space $\mathcal H=\mathcal F(\ell^2(\Lambda))$, where $|\Lambda|\geqslant2$. For any family $\{K_j\}_{j\in\Lambda}$ of self-adjoint trace-class operators with $\gamma=\sum_{j\in\Lambda}\|K_j\|_1<\infty$, we prove that the type $\mathrm{II}_1$ summand $\mathcal P$ of the von Neumann algebra $W^*(\{s_j+K_j\colon j\in\Lambda\})$ is isomorphic to the free group factor $\mathcal L(\mathbb F_\Lambda)$. As an application, we show that the set of irreducible operators on a separable infinite-dimensional Hilbert space is not dense in the trace-class norm. For each fixed $\gamma>0$, the possible values of the Murray--von Neumann dimension $\dim_{\mathcal P}(z_{\mathcal P}\mathcal H)$ form the interval $[1,1+\gamma)$, where $z_{\mathcal P}$ is the identity of $\mathcal P$.

</details>

### [Algebras Generated by Two Idempotent Matrices: Classification up to Isomorphism and Applications](https://arxiv.org/abs/2611.28086)
*Rounak Biswas* · `math.RA` · arXiv:2611.28086v1 · relevance 0.13

- **In one sentence**: The paper completes a classification, up to algebra isomorphism and with no extra restrictions, of the algebra generated by two complex idempotent matrices P and Q, continuing earlier joint work with Falguni Roy, and applies group invertibility in that algebra to solve a particular linear system explicitly.
- **In plain words**: The paper studies a mathematical object built from two "idempotent" matrices, which are grids of numbers that stay unchanged when squared. It sorts all such algebras (collections of numbers closed under addition, multiplication and scaling) into classes that count as the same structure after relabeling. It then uses a related idea, group invertibility, to write down an explicit answer to a certain system of linear equations.
- **Why it matters**: The result is a full classification, so it settles the question of which such algebras are structurally distinct rather than only special cases. The text does not say what wider problems it connects to, so its reach beyond this area is unclear from the text alone.
- **Background needed**: - Matrix: a rectangular grid of numbers that can be added and multiplied.
- Idempotent: a matrix P with P squared equal to P; it acts like a projection.
- Algebra generated by P and Q: the smallest set closed under sums, products and scalar multiples that contains P and Q.
- Isomorphism: a relabeling that preserves addition and multiplication, so two algebras with the same structure count as equal.
- Group invertibility: a matrix A has a group inverse if there is a matrix X with AXA = A, XAX = X and AX = XA.
- Linear system: a set of equations of the form Ax = b, solved with matrix methods. · level: research-level

<details><summary>Original abstract</summary>

This paper is a continuation of the earlier work by the author and Falguni Roy \cite{biswas2025comprehensive} on the algebra \(\operatorname{alg}(P,Q)\) generated by two idempotent matrices \(P,Q\in\mathbb C^{n\times n}\). A complete classification of these algebras up to algebra isomorphism is presented, without imposing any additional restrictions on the idempotents. As an application, group invertibility in \(\operatorname{alg}(P,Q)\) is employed to obtain an explicit solution to a particular system of linear equations.

</details>

## Algebra

### [Blocks with one simple module and solvable groups](https://arxiv.org/abs/2611.29140)
*Kun Zhang, Yuanyang Zhou* · `math.GR` · arXiv:2611.29140v1 · relevance 0.19

- **In one sentence**: The paper shows that a block with a single simple module of a finite group is Morita equivalent over a suitable complete discrete valuation ring to a block of a finite solvable group, and that a block Morita equivalent to a p-group algebra is nilpotent.
- **In plain words**: The paper is about the representation theory of finite groups, which studies how symmetry groups act on vector spaces. The authors consider a specific building block of such a group, called a block, that has only one kind of irreducible (indivisible) piece when working mod p. They show that this block can be matched, in a precise sense called Morita equivalence, with a block coming from a simpler kind of group, a solvable one.
- **Why it matters**: The text gives the main claims but not their wider impact, so the significance beyond this specialist area is unclear. Results of this kind relate blocks of general finite groups to solvable ones, which is a recognised theme in modular representation theory, but the text does not say how far the result extends.
- **Background needed**: - Finite group: a group with finitely many elements, such as the symmetries of a finite object.
- Representation / module: a way of letting a group act on a vector space; a simple module is one with no smaller nontrivial pieces.
- Block: an indecomposable piece of the group algebra, a standard building block of representation theory.
- Characteristic p: arithmetic mod a prime p, which changes how representations behave.
- Morita equivalence: a notion saying two algebras have the same module categories, so they share the same representation-theoretic structure.
- Complete discrete valuation ring: a local number-like ring used to lift results from characteristic p to characteristic zero.
- Solvable group: a group built in layers from abelian pieces; nilpotent and p-group are special, more restrictive cases.
- Twisted group algebra and derivation: algebraic constructions used in the paper's criterion. · level: research-level

<details><summary>Original abstract</summary>

Let $b$ be a block of a finite group with one isomorphism class of simple modules in characteristic $p$. We construct, over a sufficiently large complete discrete valuation ring of characteristic zero, a Morita equivalence between $b$ and a block of a finite solvable group. The proof uses equivariant Morita bimodules for the quasisimple blocks that occur in the component reduction. We also prove that a block over an algebraically closed field of characteristic $p$ is nilpotent whenever it is Morita equivalent to the group algebra of a finite $p$-group. For the latter result, we establish a criterion for twisted group algebras using derivations of the basic algebra and group transfer.

</details>

### [On a question of A.N. Skiba concerning the modularity of the lattice of $\sigma$-permutable subgroups](https://arxiv.org/abs/2611.29478)
*Chenxiao Lin* · `math.GR` · arXiv:2611.29478v1 · relevance 0.17

- **In one sentence**: The paper characterises finite groups whose lattice of σ-permutable subgroups is modular, answering the first part of a question posed by A.N. Skiba, and shows that when all Hall σ_i-subgroups are nilpotent, modularity is equivalent to every two members permuting.
- **In plain words**: This is a paper in group theory, the study of symmetry operations in mathematics. It looks at a family of subgroups of a finite group, called σ-permutable subgroups, where a partition of the primes sorts the group's structure into classes. The authors identify exactly which finite groups have a well-behaved (modular) pattern of these subgroups, which answers part of a question raised by Skiba.
- **Why it matters**: The work settles a specific open question from the literature on subgroup lattices, so it matters mainly to specialists in finite group theory. The text gives no wider applications, and I have not checked how it relates to other work beyond the question it answers.
- **Background needed**: - Finite group: a group with finitely many elements, a set with a rule for combining elements (like rotations of a shape).
- Subgroup: a subset of a group that is itself a group under the same rule.
- Lattice of subgroups: all subgroups arranged by inclusion, with a way to combine any two.
- Modular lattice: a lattice obeying a specific compatibility rule for how its elements combine; a structural regularity.
- Permutable subgroups: two subgroups A and B are permutable if AB = BA, meaning combining them in either order gives the same set.
- Partition of primes: splitting the set of prime numbers into disjoint classes σ_i.
- Hall σ_i-subgroup: a subgroup whose order involves only primes from class σ_i, in the sense of a generalised Sylow subgroup.
- Nilpotent: a group whose structure is built up in layers that commute nicely; a mild form of regularity. · level: research-level

<details><summary>Original abstract</summary>

Let $\sigma=\{\sigma_i\mid i\in I\}$ be some partition of the set of all primes and let $G$ be a finite group. A subgroup $A$ of $G$ is said to be $\sigma$-permutable in $G$ if $G$ has a Hall $\sigma_i$-subgroup for every $i\in I$ and $A$ permutes with every Hall $\sigma_i$-subgroup of $G$ for all $i\in I$. We describe the finite groups $G$ for which the lattice $\Lper(G)$ of all $\sigma$-permutable subgroups of $G$ is modular. This answers the first part of a question of A.N. Skiba. We also prove that if every Hall $\sigma_i$-subgroup of $G$ is nilpotent, then $\Lper(G)$ is modular if and only if every two members of $\Lper(G)$ are permutable.

</details>

## Representation theory

### [M\"obius Fusion Algebra](https://arxiv.org/abs/2611.29234)
*Ippo Orii, Yuji Tachikawa* · `math.QA` · arXiv:2611.29234v1 · relevance 0.12

- **In one sentence**: The paper defines a generally non-commutative "Möbius fusion algebra" from a pseudo-unitary modular tensor category with an anti-monoidal involution, shows it is semisimple, and gives a dimension formula for its simple modules in terms of the modular S-matrix and data from the involution.
- **In plain words**: This is a piece of abstract algebra arising from topological quantum field theory: it builds a new algebraic structure out of ribbon-graph diagrams drawn on a Möbius band, a one-sided surface. The authors prove that this structure is well behaved (semisimple), and they give a formula for the sizes of its basic building blocks, the simple modules. The formula is meant as a counterpart, for non-orientable surfaces, of the Verlinde formula known for orientable ones.
- **Why it matters**: The Verlinde formula links algebra to the counting of quantum states on surfaces, so a version for non-orientable surfaces would extend that link to a wider class of spaces. The text only states this as an expectation; it does not show the full connection, so that remains a hope rather than a demonstrated result.
- **Background needed**: - Modular tensor category: an abstract algebraic framework of anyons or quantum particles and how they fuse and braid.
- Ribbon graphs: diagrams of lines (with framing) drawn inside a surface, used to compute in topological quantum field theory.
- Möbius band: a surface with only one side and one edge, the simplest non-orientable surface.
- Orientation reversal and involution: a map that undoes itself when applied twice; here it flips the orientation of the band.
- Semisimple algebra: one whose modules decompose cleanly into simple pieces, making it easier to analyse.
- Simple module and dimension: the smallest building block of a representation, and its size (dimension).
- Modular S-matrix: a matrix encoding how the basic objects of the category relate to one another; it is the key input to the Verlinde formula.
- Verlinde formula: a classical result expressing fusion-rule counts for orientable surfaces via the S-matrix. · level: research-level

<details><summary>Original abstract</summary>

Given a pseudo-unitary modular tensor category $\mathcal{C}$ with an anti-monoidal involution $\mathsf{P}$, we define a generally non-commutative algebra from this data, which we call the M\"obius fusion algebra $\mathfrak{M}$ of $(\mathcal{C},\mathsf{P})$, in terms of ribbon graphs drawn on the M\"obius band, where the orientation-reversal of the M\"obius band acts on the graphs by $\mathsf{P}$. We show that this algebra is semisimple, and give a formula for the dimensions of its simple modules, in terms of the modular $S$-matrix of $\mathcal{C}$ and a certain set of quantities extracted from the action of $\mathsf{P}$. This formula is expected to play the role of a non-orientable analogue of the Verlinde formula, in the context of Reshetikhin-Turaev-type topological quantum field theories on non-orientable manifolds.

</details>

### [Inner derivations and automorphism groups of vertex operator algebras](https://arxiv.org/abs/2611.28814)
*Jianzhi Han* · `math.QA` · arXiv:2611.28814v1 · relevance 0.11

- **In one sentence**: For a simple, rational, C_2-cofinite vertex operator algebra of CFT type, the zero-mode map from the weight-one space V_1 to the derivations of V is shown to be a Lie algebra isomorphism, which identifies the inner automorphism group as the identity component of Aut(V) with finite index and gives dim Aut(V) = dim V_1.
- **In plain words**: This paper studies a symmetric algebraic structure, called a vertex operator algebra, that appears in the mathematics behind two-dimensional conformal field theory in physics. The author(s) show that a certain natural correspondence between the weight-one part of the structure and its rules of change (derivations) is exact, meaning it pairs the two up perfectly. From this, they conclude how the group of symmetries relates to the simpler "inner" symmetries, and that the symmetry group is finite exactly when the weight-one part is zero.
- **Why it matters**: It gives a precise, checkable link between the size of the weight-one space and the size of the symmetry group, which is a structural result for a central class of algebras. The text does not say how far it extends beyond these algebras, so its wider reach is unclear from this excerpt alone.
- **Background needed**: - Vertex operator algebra: an algebraic object graded by "weight", modelling chiral symmetry in 2D conformal field theory.
- Weight-one space V_1: the part of the algebra with weight exactly 1; it carries a Lie algebra structure.
- Derivation: a rule for differentiating products inside the algebra, forming a Lie algebra.
- Inner automorphism: a symmetry that comes from exponentiating a derivation coming from V_1.
- Identity component and finite index: a connected core of a group of symmetries, and how many pieces the whole group splits into.
- Lie algebra and Lie group dimension: the continuous "size" of a symmetry group.
- Simple, rational, C_2-cofinite, CFT type: technical finiteness and nondegeneracy hypotheses on the algebra.
- Zhu's algebra and vacuum character: a finite-dimensional algebra attached to V and a generating function counting its lowest-weight states, used in the injectivity proof. · level: research-level

<details><summary>Original abstract</summary>

Let $V$ be a simple, rational, $C_2$-cofinite vertex operator algebra of CFT type. We prove that the zero mode map $V_1\to\operatorname{Der}(V)$, $h\mapsto h_0$, is an isomorphism of Lie algebras. We prove surjectivity using traces on finite sums of weight spaces and Li's module construction, and injectivity using the vacuum character of Zhu's algebra. It follows that $\operatorname{Inn}(V)$ is the identity component of $\operatorname{Aut}(V)$ and has finite index in $\operatorname{Aut}(V)$. Moreover, $\operatorname{dim}\operatorname{Aut}(V)=\dim V_1$, so $\operatorname{Aut}(V)$ is finite if and only if $V_1=0$.

</details>

## Number theory

### [On the number theory of the Greeks. I. The Fundamental Theorem of Arithmetic](https://arxiv.org/abs/2611.29380)
*Franz Lemmermeyer* · `math.NT` · arXiv:2611.29380v1 · relevance 0.21

- **In one sentence**: A historical study arguing that Euclid's version of the fundamental theorem of arithmetic (unique factorization into primes) was widely known to pre-Gaussian number theorists, much as Gauss's later formulation is known today.
- **In plain words**: This paper looks at a basic rule of arithmetic: every whole number larger than 1 can be built from prime numbers in only one way. The author says Euclid stated this rule long ago, and that it was once as familiar to mathematicians as the later version given by Gauss is now. The text given here is only a short summary, so the detailed evidence is not shown.
- **Why it matters**: It is a historical claim about how a central idea of number theory was understood and passed on, which matters for how we credit mathematical results. The excerpt does not show the evidence in detail, so the strength of the claim cannot be judged from it alone.
- **Background needed**: - Prime number: a whole number greater than 1 with no divisors other than 1 and itself (2, 3, 5, 7, ...).
- Fundamental Theorem of Arithmetic: every whole number above 1 factors into primes in exactly one way, ignoring order.
- Euclid: ancient Greek mathematician, author of the Elements, around 300 BCE.
- Gauss: Carl Friedrich Gauss, 18th–19th century mathematician, whose 1801 Disquisitiones Arithmeticae is often credited with the modern statement of the theorem.
- The paper is the first part of a series on Greek number theory. · level: intermediate

<details><summary>Original abstract</summary>

In this article we present Euclid's fundamental theorem of number theory and give evidence for the claim that this theorem, which is largely unknown today, was as familiar to number theorists before Gauss as the Gaussian version of the fundamental theorem is to us.

</details>

### [A Classification of Low Genus Modular Curves](https://arxiv.org/abs/2611.30908)
*Eray Karabiyik* · `math.NT` · arXiv:2611.30908v1 · relevance 0.19

- **In one sentence**: The paper classifies modular curves of a fixed genus g attached to open subgroups G of GL_2(Z-hat) with full determinant and -I in G, shows they fall into finitely many families of Q^ab-twists, and gives an algorithm (implemented for g ≤ 12) to compute their projective models.
- **In plain words**: The paper studies a family of geometric curves that classify elliptic curves (a standard kind of smooth curve defined by cubic equations) with extra structure. For each fixed "genus" (roughly, the number of holes in the curve's surface), the authors sort all such curves into a finite number of families. They also describe a computer procedure for finding explicit equations for these curves, which they carried out for genus up to 12.
- **Why it matters**: Modular curves are central to modern number theory, and their rational points connect to questions such as which elliptic curves can have particular torsion behaviour. A finite classification by genus gives a systematic way to organise these curves, though the text alone does not show how far the results will be used in later work.
- **Background needed**: - Elliptic curves: smooth cubic curves with a group law, widely used in number theory and cryptography.
- Modular curve X_G: a curve over the rationals whose points parametrise elliptic curves with a given level structure (extra symmetry data on their torsion points).
- GL_2(Z-hat): the group of invertible 2x2 integer matrices, completed over all primes; open subgroups encode level structures.
- Genus: a whole-number measure of a curve's topology (number of "handles"); genus 0 curves are rational-like, higher genus curves are harder.
- Q^ab-twist: a twist of a curve by an extension of the rationals with abelian Galois group.
- Projective model: explicit polynomial equations describing the curve in projective space. · level: research-level

<details><summary>Original abstract</summary>

Let $G$ be an open subgroup of $\mathrm{GL}_2(\widehat{\mathbb{Z}})$ satisfying $\det(G)=\widehat{\mathbb{Z}}^{\times}$ and $-I\in G$. Associated to $G$, there is a modular curve $X_G$ defined over $\mathbb{Q}$ which parametrizes elliptic curves with $G$-level structure. We give a classification of modular curves with genus equal to a fixed nonnegative integer $g$. In particular, we show that all modular curves of genus $g$ lie in finitely many families of $\mathbb{Q}^{\mathrm{ab}}$-twists of modular curves. We also describe an algorithm for computing all families of modular curves of a fixed genus $g$ and use this to compute projective models for these modular curves. This algorithm has been fully implemented for $g \leq 12$. In an appendix with Yongyuan Huang and Rakvi, we describe two algorithms, one for computing rational functions on modular curves given as quotients of two modular forms of the same weight, and the other for computing models for the generic fibers of universal elliptic curves $\mathcal{E}_G$, where $G\subset \mathrm{GL}_2(\widehat{\mathbb{Z}})$ is an open subgroup satisfying $\det(G)=\widehat{\mathbb{Z}}^{\times}$ and $-I\notin G$.

</details>

## Algebraic geometry

### [Functionals commuting with reparametrizations](https://arxiv.org/abs/2611.30506)
*Pierre-Emmanuel Chaput, David Dos Santos Ferreira, Valentin F\'eray* · `math.AG` · arXiv:2611.30506v1 · relevance 0.13

- **In one sentence**: The paper classifies the algebraic functionals from n-tuples of polynomials vanishing at 0 to such polynomials that commute with right-composition (reparametrization), introducing a "semi-product" operation, with links to polyharmonic functions on the positive discrete orthant and the type A co-invariant algebra.
- **In plain words**: The paper studies rules that take several functions and combine them into one function in a way that respects changing the parameter of the curve (reparametrization). The authors motivate this by the geometry of tangent curves to algebraic varieties. For the case of polynomials that vanish at zero, they give a complete description of all such algebraic rules, built from a new operation they call the semi-product.
- **Why it matters**: The result is a complete classification in a specific setting, and the proof uses tools from discrete analysis and algebra that are not obviously related to the original geometric question. The text says the semi-product has interesting algebraic and geometric properties, but does not spell these out, and the setting is narrow, so its wider significance is unclear from this abstract alone.
- **Background needed**: - Functional: a rule that takes functions as inputs and returns a function as output.
- Reparametrization: changing the variable of a curve, for example replacing t by a function of t; here, right-composition of a function with another function from the space.
- Polynomials vanishing at 0: polynomials with zero constant term, written C[T]_0.
- Polyharmonic function: a function on a grid of integer points whose discrete Laplacian-type operators repeatedly vanish, a discrete analogue of harmonic functions.
- Positive discrete orthant: the set of integer points with all coordinates positive.
- Co-invariant algebra of type A: a finite-dimensional quotient algebra associated with the symmetric group, arising in combinatorics and representation theory.
- Colored permutations: permutations in which each entry also carries a color or label from a finite group. · level: research-level

<details><summary>Original abstract</summary>

Motivated by the study of tangent curve bundles of algebraic varieties, we consider the following simple-looking problem: given a space $E$ of functions, describe functionals from $E^n$ to $E$ which commutes with reparametrizations, i.e. with the right-composition with an element of $E$. Our main result is a complete description of the algebraic solutions of this problem when $E$ is the space of polynomials vanishing in $0$, which we denote by $\mathbb C[T]_0$. This description involves a simple operation, which we call semi-product, with interesting algebraic and geometric properties. The proof involves the study of polyharmonic functions on the positive discrete orthant $\mathbb Z^n_{>0}$, and a relation with the co-invariant algebra of type $A$. We also provide a generalization connected to colored permutations, and discuss the analogue problems where $E=\mathbb C[T]_0/(T^\ell)$ for some $\ell >0$, and where $E$ consists of infinitely differentiable functions. Finding a complete description of algebraic solutions in these settings is still open.

</details>

### [The generalized Franchetta conjecture for some hyper-K\"ahler varieties, III](https://arxiv.org/abs/2611.29599)
*Lie Fu, Robert Laterveer, Carl Mazzanti et al.* · `math.AG` · arXiv:2611.29599v1 · relevance 0.12

- **In one sentence**: This paper proves the generalized Franchetta conjecture (cycles on the generic fiber of a family of hyper-Kähler varieties inject into cohomology) for double EPW sextics and double EPW cubes, and studies Chow-Künneth decompositions of Gushel-Mukai varieties to do so.
- **In plain words**: The paper studies a family of geometric shapes, called hyper-Kähler varieties, that vary smoothly as parameters change. It asks whether certain algebraic sub-objects defined over the general member of the family can be told apart by their topological fingerprint (cohomology), and it answers yes for two specific families, the double EPW sextics and double EPW cubes. The main tool is a link to Gushel-Mukai fourfolds, whose structure is used to realize these shapes as spaces of stable objects.
- **Why it matters**: This is the third paper in a series on one conjecture, so it extends a line of established work rather than starting a new field. The connection it draws between double EPW sextics and Gushel-Mukai fourfolds at the level of motives is the kind of link that specialists in algebraic cycles and moduli may find useful; the text does not say how far it reaches beyond this area.
- **Background needed**: - Algebraic geometry studies shapes defined by polynomial equations, and families of such shapes indexed by parameters.
- Hyper-Kähler varieties are a special class of higher-dimensional complex shapes with particularly rigid geometry; they are the higher-dimensional analogues of K3 surfaces.
- Cohomology is an algebraic fingerprint of a shape's holes and structure; the cycle class map sends algebraic sub-shapes (cycles) to this fingerprint.
- "Generically defined" cycles are those that make sense over a general member of a family, rather than only special members.
- The Franchetta conjecture concerns whether such cycles are determined by their cohomology class; "injects" means distinct cycles have distinct fingerprints.
- Chow-Künneth decomposition splits the cohomology-like structure of a shape into pieces; multiplicativity means this splitting behaves well under products.
- Bridgeland-stable objects come from derived categories, a homological-algebra framework for organizing geometric objects; Kuznetsov components are pieces of such categories attached to Fano varieties.
- Motives are a universal framework relating different algebraic varieties. · level: research-level

<details><summary>Original abstract</summary>

The generalized Franchetta conjecture states that for a locally complete family of polarized hyper-K\"ahler varieties, the generically defined cycles on any fiber of the universal family over the moduli stack inject into cohomology via the cycle class map. We prove the generalized Franchetta conjecture for the family of double EPW sextics discovered by O'Grady and for the family of double EPW cubes discovered by Iliev-Kapustka-Kapustka-Ranestad. We also prove a Franchetta-type result for the relative square of the universal family of double EPW sextics, which allows to relate double EPW sextics and Gushel-Mukai fourfolds on the level of motives. The proof involves the geometry of Gushel-Mukai fourfolds, whose Kuznetsov component allows to realize double EPW sextics and cubes as moduli spaces of Bridgeland-stable objects, relatively over the parameter space of Gushel-Mukai fourfolds. A key step is that the canonical Chow-K\"unneth decomposition of special Gushel-Mukai fourfolds is multiplicative; we use this to show that generically defined cycles on the third power of a special Gushel-Mukai fourfold inject into cohomology via the cycle class map. Along the way, we also show that the canonical Chow-K\"unneth decomposition of any Gushel-Mukai sixfold is multiplicative.

</details>

## Topology

### [A complete knot invariant from grid diagrams](https://arxiv.org/abs/2611.30095)
*Agnese Barbensi, Daniele Celoria, Lavender Marshall et al.* · `math.GT` · arXiv:2611.30095v1 · relevance 0.12

- **In one sentence**: The paper builds an infinite graph from grid diagrams of a knot and proves that this graph, up to isomorphism and mirror image, completely determines the knot type, with finite algorithmically computable portions sufficing.
- **In plain words**: The paper is about knots, the tangled loops studied in mathematics, and how to tell two knots apart. The authors turn each knot into a grid of marks and from that build a large network-like object, called a graph. They show that this object captures the knot completely, so two knots are the same type exactly when their graphs match, apart from a mirror reflection. They also show that a finite, computable piece of the graph is already enough.
- **Why it matters**: A complete invariant is a rare and valuable tool, because many standard knot invariants cannot distinguish all knots. The text does not say how practical the method is or how it compares with existing invariants, so its broader usefulness is uncertain from this summary alone.
- **Background needed**: - A knot is a closed loop embedded in three-dimensional space, considered the same as another if one can be deformed into the other without cutting.
- A knot invariant is a property that is the same for equivalent knots; a complete invariant determines the knot fully.
- A grid diagram is a square grid with markers placed in cells that encode a knot's crossings.
- A graph is a set of points (vertices) joined by lines (edges); isomorphism means two graphs have the same structure.
- Mirroring reverses a knot like a reflection in a mirror; the result is only claimed to be determined up to this. · level: research-level

<details><summary>Original abstract</summary>

Using grid diagrams, we define an infinite graph associated to each knot type. We prove that the isomorphism class of this grid graph is a complete invariant of the knot, up to mirroring. Even more, we prove that algorithmically determinable finite parts of this graph are enough to determine the knot type.

</details>

### [Unknotting number is strictly subadditive for the trefoil](https://arxiv.org/abs/2611.29233)
*Anne Dranowski, Yura Kabkov, Daniel Tubbenhauer* · `math.GT` · arXiv:2611.29233v1 · relevance 0.11

- **In one sentence**: The paper shows that the unknotting number is strictly subadditive for the trefoil: there is a knot K such that u(T#K) < u(T)+u(K), with the saving extended to infinitely many prime partners and to positive braid knots and torus knots.
- **In plain words**: The paper studies knots, which are closed loops of string tangled in space. For a knot, the "unknotting number" is the fewest times you must swap one crossing for the other to make the loop plain, untangled. The question is whether joining two knots together can ever be cheaper to untangle than doing each separately, and the text reports that for the trefoil it can be: a trefoil plus a particular fourteen-crossing knot needs at most three changes together, while the two separately need four each.
- **Why it matters**: Whether this unknotting cost adds up exactly when knots are joined was an open-style question in knot theory, so a concrete saving is a notable, checkable example. The text does not say what broader consequences follow beyond the stated families of knots.
- **Background needed**: - Knot: a closed loop embedded in three-dimensional space, considered the same if it can be deformed without cutting.
- Crossing change: switching which strand passes over at one crossing in a diagram.
- Unknotting number: the minimum number of crossing changes needed to turn a knot into the unknot (the simplest, untangled loop).
- Trefoil: the simplest nontrivial knot, with three crossings.
- Connected sum: joining two knots into one, like tying their ends together; the unknotting number is subadditive if the cost of the joined knot is at most the sum of the costs.
- Strict subadditivity: the joined knot is strictly cheaper than the sum, which is what this paper exhibits.
- Positive braid knot and torus knot: special families of knots with regular, structured descriptions. · level: research-level

<details><summary>Original abstract</summary>

A trefoil and a certain fourteen-crossing knot take four crossing changes to unknot separately and at most three together. We extend this example to infinitely many prime partners and show that the same partners give a saving for every nontrivial positive braid knot and, up to mirror, every nontrivial torus knot.

</details>

## Dynamical systems

### [KAM theory for contact Hamiltonian systems](https://arxiv.org/abs/2611.28587)
*Zhicheng Tong, Yong Li, Xuefeng Zhao* · `math.DS` · arXiv:2611.28587v1 · relevance 0.14

- **In one sentence**: The paper proves frequency-preserving KAM theorems for full-dimensional Legendrian tori in contact Hamiltonian families (finite and infinite dimensional), with analytic coupling between momenta and the contact variable, and links the resulting invariant graphs to analytic stationary Hamilton–Jacobi solutions and weak KAM solutions.
- **In plain words**: The paper studies dynamical systems that have friction-like damping built into their rules of motion, and asks when their motion stays on a predictable, quasi-periodic pattern (like a set of nested, repeating loops) even under small disturbances. The authors show that, after suitable parameter adjustments, such motion on special invariant surfaces can be smoothly re-timed and kept at its prescribed rhythm, including in cases where the damping averages to a nonzero value. In finite dimensions they also show the resulting smooth solution is the only one of its type in both time directions, under extra assumptions.
- **Why it matters**: KAM theory is a standard tool for showing that quasi-periodic motion survives small perturbations, and extending it to dissipative (contact) systems is a natural but technically hard step. The text does not show applications beyond the mathematical connections it names, so its wider significance is uncertain.
- **Background needed**: - Hamiltonian systems: energy-conserving motion described by position and momentum.
- Contact systems: a generalization that includes energy loss or gain through an extra "contact" variable.
- KAM theory: results showing that quasi-periodic (non-repeating but regular) motion survives small perturbations.
- Invariant tori: smooth surfaces that the motion stays on, winding around at fixed rates.
- Legendrian tori: a special, geometrically constrained kind of invariant torus in contact systems.
- Hamilton–Jacobi equations and weak KAM solutions: partial differential equations whose solutions encode the long-term behavior of the motion.
- Analytic: infinitely smooth in a strong, power-series sense. · level: research-level

<details><summary>Original abstract</summary>

In both finite and infinite dimensions, we establish the first frequency-preserving KAM theorems for full-dimensional Legendrian tori in contact Hamiltonian families with general analytic coupling between the momenta and the contact variable. After adjustment of external parameters, the flow on each torus is analytically conjugate in the original time to the prescribed translation, with estimates uniform as the damping parameter crosses zero. This coupling can generate nonzero mean damping at first order even when the damping parameter vanishes. In finite dimensions, nonzero mean damping yields a time-preserving analytic contact linearization near the torus. In both settings the invariant graphs give global analytic solutions of stationary Hamilton--Jacobi equations whose characteristic flows are conjugate to the prescribed translation. A novel consequence in finite dimensions is that, under global Tonelli assumptions and strict increase in the contact variable, this analytic solution is both the unique forward and the unique backward weak KAM solution, and its associated Legendrian graph is an invariant torus carrying quasi-periodic dynamics.

</details>

### [One-shot identification of analytic systems](https://arxiv.org/abs/2611.30470)
*Nicolas Boull\'e, Diana Halikias, Samuel E. Otto et al.* · `math.NA` · arXiv:2611.30470v1 · relevance 0.11

- **In one sentence**: The paper gives a zero-one law for when the coefficients of a linearly parameterized analytic system can be recovered from one input-solution pair, characterizing the degenerate inputs where injectivity of the recovery map fails, and applies this to matrices, continuous-time dynamical systems and differential operators.
- **In plain words**: The paper asks whether you can work out the unknown settings of a system (such as the rates in a set of differential equations) by watching it respond to just one input and recording one resulting trajectory. It shows that for a given input, either every input fails to reveal the settings, or the failing inputs form a very small set that is negligible under random Gaussian choices. The authors then work out explicit failing sets for several classes of ODEs and PDEs and name some deterministic inputs that do guarantee recovery.
- **Why it matters**: Identifying a system from a single experiment is practically useful when repeated experiments are costly or impossible. The result may connect to system identification and control, though the text alone does not show how far the framework extends beyond the classes it covers.
- **Background needed**: - Analytic function: a smooth function that can be locally written as a convergent power series.
- Dynamical system: a rule describing how a state evolves over time, often given by differential equations.
- Linearly parameterized system: the unknown coefficients enter the equations linearly, multiplying fixed known operators.
- Injective map: a map where different inputs give different outputs, so the output determines the input uniquely; here it means the coefficients are uniquely determined by the observed output.
- Degenerate set: the inputs for which this uniqueness fails.
- Gaussian measure: a standard way of randomly choosing inputs; a set of zero measure is one that random choices almost never hit.
- Differential operator: a rule combining derivatives of a function, as in ODEs (one variable) and PDEs (several variables). · level: research-level

<details><summary>Original abstract</summary>

We study when the coefficients of a linearly parameterized analytic system can be identified from a single input-solution pair. Given a finite dictionary of analytic operators, each admissible input induces a finite-dimensional linear recovery map from coefficients to observed outputs. Coefficient recovery is possible exactly when this map is injective. We define the degenerate input set as the set of inputs for which injectivity fails and prove a zero-one law: either every admissible input is degenerate, or the degenerate set is negligible in the sense that it is compactly slice-null and has zero measure under every nondegenerate Gaussian measure. We then apply this framework to the recovery of matrices, analytic continuous-time dynamical systems, and differential operators. For several ODE and PDE classes, we further characterize the degenerate sets explicitly and identify deterministic choices of inputs that guarantee recovery.

</details>

## Combinatorics

### [The maximum number of edges in minimal $k$-extendable bipartite graphs](https://arxiv.org/abs/2611.29504)
*Xiaoling He* · `math.CO` · arXiv:2611.29504v1 · relevance 0.14

- **In one sentence**: The paper confirms a conjectured edge-count upper bound, (2k+1)(|V|-2k)/2, for minimal k-extendable bipartite graphs when k is at least 3, and shows the bound is sharp for even orders at least 6k.
- **In plain words**: This paper is about graphs, meaning dots joined by lines, and a property called k-extendability: any set of k non-touching pairings between dots can always be completed to pair up every dot. The question is how many lines a "minimal" graph with this property can have, where removing any single line destroys the property. The authors prove a conjectured upper limit on the number of lines for k at least 3 and show that the limit can actually be reached.
- **Why it matters**: It settles, for larger k, a conjecture posed in a very recent paper, extending earlier results for k=1 and k=2. The link to wider applications is not stated in the text, so I cannot say more about its reach.
- **Background needed**: - Graph: dots (vertices) joined by lines (edges).
- Bipartite graph: dots split into two groups, with lines only between the groups.
- Matching: a set of lines with no two sharing a dot; a perfect matching pairs up every dot.
- k-extendable: connected, with at least 2k+2 dots, has a matching of size k, and every such matching extends to a perfect matching.
- Minimal: removing any one line makes the graph lose k-extendability.
- Known prior results: Lovász and Plummer (1977) for k=1 bound; Fabres, Kothari and Carvalho (2021) for k=2; Mallik, Diwan and Kothari (2026) characterized the k=1 extremal case and made the conjecture.
- Sharpness: the bound is attained by some graphs at the stated orders. · level: research-level

<details><summary>Original abstract</summary>

A connected graph of order at least $2k+2$ is {\em $k$-extendable} if it has a matching of size $k$ and every such matching extends to a perfect matching. In particular, a 1-extendable graph is also called a {\em matching covered graph}. A $k$-extendable graph $G$ is {\em minimal} if $G-e$ is not $k$-extendable for every $e\in E(G)$. Lov\'asz and Plummer [J. Combin. Theory Ser. B 23 (1977), 127--138] proved that every minimal matching covered bipartite graph $G$ with $|V(G)|\ge6$ satisfies $|E(G)|\le(3|V(G)|-6)/2$, and this bound is sharp for every even order at least 6. Fabres, Kothari and Carvalho [J. Graph Theory 96 (2021), 490--509] proved that every minimal 2-extendable bipartite graph $G$ with $|V(G)|\ge12$ satisfies $|E(G)|\le(5|V(G)|-20)/2$. Very recently, Mallik, Diwan and Kothari [J. Combin. 17 (2026), 559--606] characterized minimal matching covered bipartite graphs $G$ with $|E(G)|=(3|V(G)|-6)/2$ in terms of special trees. They also conjectured that, for every integer $k\ge1$, there exists an integer $N_k\le4k^2+2k$ such that every minimal $k$-extendable bipartite graph $G$ with $|V(G)|\ge N_k$ satisfies $|E(G)|\le(2k+1)(|V(G)|-2k)/2$. In this paper, we confirm this conjecture for $k\ge3$ and prove that the upper bound is sharp for every even order at least $6k$ ($k\ge3$).

</details>

### [Local Limits and Structures of Nearest-Predecessor Random Graphs](https://arxiv.org/abs/2611.29929)
*Xiaoyao Huang* · `math.PR` · arXiv:2611.29929v1 · relevance 0.13

- **In one sentence**: The paper studies random "nearest-predecessor" graphs built by inserting vertices in random order, proving local (Benjamini–Schramm) limits, degree asymptotics, boundary-edge CLT and connectivity/planarity properties for the two-sided and K-nearest variants.
- **In plain words**: The paper looks at a random network built by adding points one at a time in a random order, where each new point links to the closest point already placed on each side (or to its K closest earlier points). It shows that, as the network grows, its view from a typical vertex settles into a fixed infinite network, and it pins down how many connections a single vertex can have at most. It also gives results about the number of links crossing a boundary and about basic shape properties of the infinite version.
- **Why it matters**: The paper answers an open question posed by Ponomarenko about the maximum degree, which is a concrete point of interest for people studying random graph growth models. The text does not say how far the methods reach beyond this specific model, so any wider connections should be treated as unclear.
- **Background needed**: - A graph is a set of vertices joined by edges; the degree of a vertex is how many edges it has.
- Random insertion order: vertices arrive in a uniformly random order, so each new vertex's neighbours depend on chance.
- Benjamini–Schramm convergence: a way of saying a growing random graph looks, locally around a typical vertex, more and more like a fixed infinite graph.
- "Quenched" means the result holds for almost every fixed realisation of the random inputs, not just on average over them.
- One-ended / recurrent / planar: infinite graphs can be described by how they can be split apart, whether a random walk returns to its start, and whether it can be drawn in a plane without crossing edges.
- Probability generating function and CLT (central limit theorem): tools for describing the distribution of a count and saying it is approximately bell-shaped for large sizes. · level: research-level

<details><summary>Original abstract</summary>

We study the two-sided nearest-predecessor graph on $[n]$, where vertices arrive in a uniformly random order and each new vertex connects to its nearest earlier vertex on each side. We construct an infinite graph on $\mathbb{Z}$ from i.i.d. continuous insertion times and prove quenched Benjamini--Schramm convergence to it almost surely. The limit is almost surely one-ended and recurrent. We resolve an open problem of Ponomarenko by proving that the maximum degree is asymptotic in probability to $\log n/\log(3/2)$ as $n\to\infty$. We obtain the probability generating function and a CLT for the number of edges crossing the boundary of $[n]$ in the infinite limit. We also study the $K$-nearest-predecessor graph, in which each new vertex attaches to its $K$ nearest earlier vertices without regard to side. For every fixed $K\geq1$, we construct the infinite limit, prove almost sure quenched Benjamini--Schramm convergence, and show that it is almost surely connected, one-ended, and recurrent, as well as nonplanar when $K\geq2$.

</details>

## Numerical analysis

### [Irreducible shallow tanh neural networks are a manifold](https://arxiv.org/abs/2611.30553)
*Ivan Bioli, Isabella Carla Gonnella, Carlo Marcati et al.* · `cs.LG` · arXiv:2611.30553v1 · relevance 0.13

- **In one sentence**: The paper proves that shallow tanh neural networks with no redundant neurons (irreducible in Sussmann's sense) form a smooth embedded submanifold of Sobolev spaces on bounded sets, and counts its connected components (n+1 for scalar input and output, connected otherwise).
- **In plain words**: The paper studies the collection of all functions that a small neural network with a fixed number of neurons can produce. It looks only at networks where no neuron is redundant, and shows that this collection forms a smooth, curved surface-like shape inside a larger space of functions. It also counts how many separate pieces that shape has.
- **Why it matters**: Knowing the geometry of the set of functions a network can represent helps explain how training and approximation behave, though the text itself does not spell out applications. The main technical step is showing that when approximating networks converge to an irreducible one, their parameters stay bounded.
- **Background needed**: - Neural network: a function built from simple units ("neurons") with adjustable weights.
- Shallow network with n hidden neurons: one layer of n such units feeding the output.
- Hyperbolic tangent (tanh): a smooth S-shaped activation function.
- Irreducible network (Sussmann, 1992): a network with no redundant neurons, so it cannot be simplified.
- Sobolev space W^{l,p}: a space of functions measured by both their values and their derivatives up to order l, in L^p norm.
- Smooth embedded submanifold: a set that locally looks like a smooth curved space of fixed dimension inside a bigger space.
- Connected components: separate pieces of a set that cannot be joined by a continuous path. · level: research-level

<details><summary>Original abstract</summary>

Neural networks (NNs) have been increasingly used as function approximators, motivating the study of the geometry of their function spaces. We study the set of functions represented by shallow neural networks with hyperbolic tangent activation, fixed input and output dimensions, and $n$ hidden neurons. In particular, we prove that the subset represented by irreducible networks in the sense of Sussmann (Neural Networks, 1992), i.e., networks with no redundant neurons, is a smooth embedded submanifold of the Sobolev spaces $\mathrm{W}^{\ell,p}$ on bounded sets for any $\ell\in\mathbb{N}$ and $p\in[1,+\infty]$. The key step is to show that if a sequence of networks converges in $\mathrm{W}^{\ell,p}$ to an irreducible network with the same number of hidden neurons, then the parameters of the approximating networks remain bounded. Finally, we show that this manifold has exactly $n+1$ connected components when both the input and output are scalar, and is connected otherwise.

</details>

### [Hierarchical randomized neural networks for efficiently and accurately finding multiple solutions of semilinear elliptic equations](https://arxiv.org/abs/2611.30010)
*Jingying Hu, Jiao Li, Yufeng Xu et al.* · `math.NA` · arXiv:2611.30010v1 · relevance 0.13

- **In one sentence**: A randomized-neural-network method, combining an SVD-based initialization, a deflated Gauss-Newton optimizer with an exponential deflation operator, and a hierarchical multilevel scheme, is proposed to find multiple solutions of semilinear elliptic PDEs.
- **In plain words**: This paper is about finding several different solutions to a type of equation that describes steady physical states, such as temperature or pressure patterns in a region. The authors use a neural network whose inner weights are set randomly and only the output layer is solved for, and they combine this with a search procedure designed to avoid already-found solutions. According to the text, the method finds multiple solutions without prior knowledge of them, with relative errors reaching 10^-16 in the best case and at under one-tenth of the computational cost, and it keeps the symmetries the solutions have.
- **Why it matters**: Semilinear elliptic equations often have several valid solutions, and missing some can matter in applications, so a reliable way to find them is useful. The text reports accuracy and cost results only from numerical tests, and it gives a local error estimate under stated conditions; whether the approach generalizes to harder problems is not shown in the text.
- **Background needed**: - Elliptic equation: a equation describing steady states (no time change), e.g. equilibrium temperature or membrane shape.
- Semilinear: the nonlinearity is simple enough that the equation is still tractable, but it can admit several solutions.
- Randomized neural network: a network whose hidden-layer weights are drawn at random and fixed; only the output weights are fitted, which is fast.
- Singular value decomposition (SVD): a matrix factorization that reveals the dominant directions in data.
- Gauss-Newton method: an iterative method for solving nonlinear equations by linearizing at each step.
- Deflation: a technique that modifies an equation so that already-found solutions are no longer attractive, pushing the search to find new ones.
- Multilevel method: solving on coarse versions first and refining, to speed up and improve accuracy.
- Relative error: the error divided by the size of the true answer.</background>
<parameter name="difficulty">research-level

<details><summary>Original abstract</summary>

Being able to find multiple solutions of a semilinear elliptic equation is a fundamental problem in scientific computing. In this paper, fully taking the advantages of randomized neural networks, we propose a new efficient and accurate method for identifying potentially as many solutions as possible. The new method is constructed from three aspects--initialization, optimization, a technique for acceleration and improving accuracy, two of which are innovative developments. Firstly, based on the basis functions of a randomized network and the sampling points, a characteristic matrix is introduced so that its singular value decomposition can be used to determine weakly variant search directions, followed by a newly developed algorithm to generate effective initial candidates. Then the good deflated Gauss-Newton method [see {\em A. Riley, et al., SIAM Journal on Scientific Computing 47~(5) (2025) A2963-A2987}] using an exponential deflation operator is adapted as the optimization to search for all multiple solutions. Local error estimate of a particular solution under some proper condition is given in terms of the neurons in the hidden layer and the sampling points for this newly designed method. Furthermore, to accelerate the computation and improve the solution accuracy, a new multilevel method based on hierarchical networks is designed. Without using any {\em a priori} information, several numerical tests show together with the multilevel method, the new method can not only accurately find multiple solutions with relative errors reaching $10^{-16}$ only in less than one-tenth computational cost for the best case, but also preserve the inherent symmetries of multiple solutions.

</details>

## Logic and foundations

### [Equivalence of Cohen generics is hyperfinite](https://arxiv.org/abs/2611.30679)
*Iian B. Smythe* · `math.LO` · arXiv:2611.30679v1 · relevance 0.15

- **In one sentence**: The paper shows that the equivalence relation "two Cohen generic reals yield the same generic extension" over a countable model of set theory is hyperfinite, answering a question posed by the author, via asymptotic separation.
- **In plain words**: This is a set-theory paper about "random-like" infinite objects called Cohen generic reals, and about when two of them count as giving the same new mathematical universe. The author shows that this sameness relation is "hyperfinite," meaning its classes can be approximated by finite pieces in a controlled way. The text says the proof is a reworked version of an argument first produced by GPT-6, an AI model.
- **Why it matters**: It settles an open question the author had raised, so it is a concrete result rather than a survey. Its link to AI is notable mainly because the text says the original argument came from GPT-6; the text does not say how much of the final write-up depends on that, so the significance of that claim is hard to judge from this brief alone.
- **Background needed**: - Countable model of set theory: a countable collection of sets satisfying the axioms of set theory, used as a stand-in for the universe of sets.
- Cohen generic real: a real number that avoids all the "exceptional" sets one could name in the model, so it is random-like relative to that model.
- Generic extension: a larger model of set theory obtained by adding a generic real to the original.
- Equivalence relation: a rule saying two objects are "the same" in some respect, splitting objects into classes.
- Hyperfinite: an equivalence relation whose classes can be handled by a limit of finite approximations, a notion from descriptive set theory.
- Asymptotic separation: a technique for showing that certain objects can be told apart in the limit, used here as the core proof tool. · level: research-level

<details><summary>Original abstract</summary>

It is shown that the equivalence relation on Cohen generic reals over a countable model of set theory, where two are equivalent if they produce the same generic extension, is hyperfinite, answering a question of the author. The proof uses asymptotic separation and is a digestion of an argument originally produced by GPT-6.

</details>

### [Dense ideals in forcing extensions of Nairian models](https://arxiv.org/abs/2611.28226)
*Rahman Mohammadpour, Grigor Sargsyan* · `math.LO` · arXiv:2611.28226v1 · relevance 0.11

- **In one sentence**: The paper builds forcing extensions of minimal Nairian models (ZF-style models of the Axiom of Determinacy for real-number sets) in which AC and GCH hold and every uncountable regular cardinal carries a precipitous, uniform, κ-dense ideal whose quotient is the regular open algebra of Col(ω,κ).
- **In plain words**: Set theory studies which infinite collections exist and how big they are, and this paper works in a framework where the axiom of choice is dropped and a different axiom, determinacy, is assumed instead. The authors show that, after a further controlled extension of such a model, every uncountable regular infinite size has a particular kind of "dense ideal" (a way of sorting subsets of that size into negligible and non-negligible ones). The text presents this as extending a known result of Woodin and placing the consistency strength of the setting relative to a large-cardinal assumption.
- **Why it matters**: It strengthens and generalizes an existing theorem of Woodin about dense ideals on ω1, and it addresses how strong a large-cardinal assumption is needed for this combination of determinacy and choice-free theory. The text itself does not claim wider consequences, so its reach beyond set theory is unclear from this excerpt.
- **Background needed**: - Axiom of Choice (AC): the principle that one can pick an element from every set in a family; Zermelo–Fraenkel set theory (ZF) omits it.
- Axiom of Determinacy (AD): a principle that every two-player game on natural numbers has a winner determined by a strategy; it conflicts with AC, so models of AD are choice-free.
- Nairian models: models studied by Blue, Larson, and Sargsyan, built from AD for real numbers; "minimal" refers to the smallest such models.
- Generalized Continuum Hypothesis (GCH): each infinite size is the next-larger size of infinite collection after the one below it, with no sizes in between.
- Cardinals, uncountable regular cardinal: infinite "sizes" that cannot be reached as a countable union of smaller ones.
- Ideal and dense ideal: a family of "small" sets closed under taking subsets and finite unions; density means the non-small sets can be split finely; precipitous and uniform are technical strength conditions.
- Forcing extension: enlarging a model of set theory by adding new objects in a controlled way.
- Woodin cardinal: a large-cardinal assumption, an infinite size stronger than ordinary ones; "consistency strength" measures how much such an assumption a theory needs. · level: research-level

<details><summary>Original abstract</summary>

Complementing the work of Blue, Larson, and Sargsyan~\cite{NM,NM2}, we obtain forcing extensions of minimal Nairian models in which the Axiom of Choice and the Generalized Continuum Hypothesis hold. In these extensions, every uncountable regular cardinal $\kappa$ carries a precipitous, uniform, $\kappa$-dense ideal $\mathcal{I}_\kappa$. In fact, $\mathcal P(\kappa)/\mathcal{I}_\kappa$ is isomorphic to the regular open algebra of $\textrm{Col}(\omega,\kappa)$. This extends Woodin's theorem on the existence of $\omega_1$-dense ideals on $\omega_1$ in forcing extensions of models of $\Theta_{\rm reg}$ \cite[Section~2.3]{ASTWZ24}, where $\Theta_{\rm reg}$ denotes the theory $\textrm{ZF}+\textrm{AD}_{\mathbb R}+\text{``$\Theta$ is regular''}$. Moreover, our work places the consistency strength of the aforementioned theory on generic embeddings below a Woodin cardinal that is a limit of Woodin cardinals, and also complements the seminal work of Eskew and Hayut~\cite{EH24}.

</details>

## Mathematical physics

### [Tensionless M5-brane in light-cone gauge. The spinor moving frame method is wanted](https://arxiv.org/abs/2611.31189)
*Igor Bandos* · `hep-th` · arXiv:2611.31189v1 · relevance 0.11

- **In one sentence**: The paper performs complete light-cone gauge fixing of the tensionless limit of the M5-brane action, using a spinor moving frame method adapted to handle the fermionic kappa-symmetry, and also builds the analogous formulation for tensionless p-branes without worldvolume gauge fields.
- **In plain words**: The paper studies a idealized version of a membrane-like object from string/M-theory, the 5-dimensional "M5-brane," in the limit where its tension (the energy cost per unit size that gives it stiffness) goes to zero. The main difficulty is that the usual way of removing redundant descriptions of the object does not work cleanly here, so the authors adapt a technique called the spinor moving frame method to do it. The text describes this as a method that works, and it also checks the symmetries of the resulting equations.
- **Why it matters**: Tensionless branes are a niche but active topic in theoretical physics, and this work shows how to put the M5-brane's tensionless action into a fixed, simpler gauge. It may matter for understanding high-tension-to-zero limits of M-theory, but the text does not state broader consequences, so the wider significance is unclear from the abstract alone.
- **Background needed**: - M-theory: the proposed 11-dimensional theory unifying string theories.
- Branes: extended objects; a p-brane has p spatial dimensions, and an M5-brane is 5+1 dimensional.
- Tension: the energy per unit volume of a brane; a tensionless brane is a limiting case.
- Gauge fixing: choosing a convenient description by removing redundant mathematical freedom.
- Light-cone gauge: a specific choice of coordinates that simplifies equations.
- Kappa-symmetry: a local fermionic (spinor-valued) symmetry of brane actions that must be handled when fixing the gauge.
- Spinor moving frame: a technique that builds a local coordinate frame from spinor quantities to fix that symmetry.
- PST scalar: a scalar field from the Pasti-Sorokin-Tonin formulation of the M5-brane action. · level: research-level

<details><summary>Original abstract</summary>

We perform the complete light-cone gauge fixing for the tensionless limit of the M-theory 5-brane the action for which was recently obtained in [1]. The problem of gauge fixing of local fermionic $\kappa$-symmetry becomes quite nontrivial because the projector of that is constructed from the gauge field strength which in its turn is required to be nonvanaishing and nontrivial in this limit. To resolve this problem the spinor moving frame method has been adapted. The corresponding moving frame is constructed on a vector quadratic in the gauge field strength, which is required to be nonvanishing and nondegenerate in the tensionless limit, and the derivative of the PST (Pasti-Sorokin-Tonin) scalar. The symmetries of the gauge fixed action and equations of motion are briefly discussed. To make a comparison with the case of usual tensionless p-branes (null-p-branes), those which do not carry worldvolume gauge fields, we also elaborate their spinor moving frame formulation.

</details>

### [Infrared finite scattering theory: Non-relativistic Coulomb scattering](https://arxiv.org/abs/2611.29691)
*Kartik Prabhu, Shivam Upadhyay* · `hep-th` · arXiv:2611.29691v1 · relevance 0.10

- **In one sentence**: The paper builds a perturbative, infrared-finite Dollard scattering operator for non-relativistic Coulomb scattering, checks it through second Born order, and sets up an LSZ-type reduction in the Heisenberg picture adapted to the modified asymptotic dynamics.
- **In plain words**: When two charged particles fly past each other, their electric pull never fully switches off, so the standard textbook way of calculating how they scatter produces infinite terms. This paper revisits that problem for the simple non-relativistic Coulomb case and uses a modified reference dynamics (Dollard's approach) that makes the infinities cancel order by order in the calculation. The authors check that the result matches the known exact Coulomb scattering amplitude, including its forward-scattering part, and then rewrite the setup in a different mathematical viewpoint meant as a stepping stone toward quantum field theory.
- **Why it matters**: Long-range forces and massless particles, such as photons, create the same kind of infrared divergence in quantum field theory, so a clean, checkable version of the method in a simple case may help with that harder setting. The text only describes the framework and its consistency checks through second order; it does not show that the relativistic extension works, so that link remains a goal rather than a result.
- **Background needed**: - Scattering amplitude: a quantity giving the probability-like outcome when particles collide or pass each other.
- Coulomb potential: the 1/r electric attraction or repulsion between charges, which decays slowly with distance.
- Born series: calculating scattering as a sum of successively refined approximations; each term here is a perturbation.
- Infrared divergence: infinite results caused by long-range effects or very low-energy (soft) quanta.
- Dollard scattering operator: a modified reference dynamics that absorbs the slow-decay problem so the scattering quantity is well defined.
- Heisenberg picture and S-matrix: a way of tracking operators over time, and the matrix connecting incoming to outgoing states.
- LSZ reduction: the standard recipe in quantum field theory for extracting scattering amplitudes from correlation functions.
- Canonical transformation: a change of position and momentum variables that preserves the underlying physics. · level: research-level

<details><summary>Original abstract</summary>

We revisit non-relativistic quantum-mechanical scattering in a Coulomb potential. The long-range nature of the interaction leads to divergent integrals in conventional S-matrix calculations using the Born series. Dollard showed that a well-defined scattering operator can be constructed by replacing the free Hamiltonian $ H_0 $ with an appropriate asymptotic Hamiltonian $ H_{\rm D} $. However, explicit perturbative calculations within Dollard's framework have remained scarce. We develop a perturbative formulation of the Dollard scattering operator in which the Coulomb divergences cancel to all orders. Perturbatively, we demonstrate this cancellation explicitly through second Born order and show that the resulting amplitude reproduces the known exact distributional Coulomb amplitude, including its forward-scattering contribution. With the aim of generalizing our analysis to quantum field theory, we reformulate the problem in the Heisenberg picture. We construct a new set of canonical variables through a time-dependent canonical transformation that removes the logarithmic Coulomb correction from the asymptotic phase-space coordinates. Using these variables, we construct the corresponding Heisenberg S-matrix through several complementary approaches. This leads to a formulation of the Lehmann--Symanzik--Zimmermann (LSZ) reduction formalism adapted to the modified asymptotic dynamics, which we relate to the Dollard scattering operator. This construction provides a framework for extending the LSZ formalism to infrared divergences in relativistic quantum field theories with long-range interactions and massless fields.

</details>

## Optimization and control

### [The dimension of optimal plans in multi-marginal optimal transport](https://arxiv.org/abs/2611.29080)
*Camilla Brizzi, Gero Friesecke* · `math.OC` · arXiv:2611.29080v1 · relevance 0.22

- **In one sentence**: The paper determines the maximal dimension on which optimal solutions of multi-marginal optimal transport problems with absolutely continuous marginals concentrate, using a new integer invariant derived from the Hessian of the cost function, with applications to Wasserstein barycenters, Wasserstein cubic splines and Brenier's generalized Euler equations.
- **In plain words**: The paper studies a problem about the best way to match up several smooth probability distributions at once, where a cost is paid for each combined arrangement. It asks how "spread out" the best matchings can be: whether they fill a full-dimensional region or sit on a smaller, lower-dimensional set. The authors give a general answer for the maximal dimension of that set, computed from a new integer tied to the curvature (Hessian) of the cost function.
- **Why it matters**: Optimal transport is a central tool for comparing and averaging distributions, and knowing where optimal solutions live tells you how they can be computed and described. The text notes applications to Wasserstein barycenters, cubic splines and Brenier's generalized Euler equations, but the abstract alone does not show how far these results reach beyond those examples.
- **Background needed**: - Optimal transport: finding the cheapest way to move one probability distribution of mass onto another, given a cost for each move.
- Multi-marginal version: the same idea with three or more distributions that must be coupled jointly.
- Marginals: the individual distributions being matched; "absolutely continuous" means they have a density, so they do not sit on thin sets.
- Concentration dimension: whether the optimal arrangement spreads over a full-dimensional region or lies on a lower-dimensional surface.
- Hessian: the matrix of second derivatives of the cost, describing its local curvature.
- Wasserstein barycenter: an "average" of several distributions defined through transport distance. · level: research-level

<details><summary>Original abstract</summary>

For general cost functions, we determine the maximal dimension on which solutions to the multi-marginal optimal transport problem with absolutely continuous marginals are concentrated. The dimension is obtained via a novel characteristic integer associated with the Hessian of the cost function. Applications are given to important examples of multi-marginal problems like Wasserstein barycenters, Wasserstein cubic splines and Brenier's generalized Euler equations.

</details>

### [Convergence of potential-preserving annealed Sinkhorn algorithm](https://arxiv.org/abs/2611.30984)
*Dawid Lipinski, Maciej Buze* · `math.OC` · arXiv:2611.30984v1 · relevance 0.17

- **In one sentence**: The paper proves convergence results for a potential-preserving annealed Sinkhorn algorithm for entropic optimal transport, including a sharp non-summability condition on the regularisation schedule, full-sequence convergence under an additional square-summability condition, and convergence rates for polynomial inverse-temperature schedules up to linear growth.
- **In plain words**: The paper studies a computer method for finding the cheapest way to move one spread of material (a probability distribution) onto another, a problem known as optimal transport. The method works by gradually lowering a smoothing "temperature" parameter while it iterates, and the authors examine the version that keeps track of dual potentials (internal weight values) rather than scaling factors. They show that if the temperature drops slowly enough that its total sum diverges, some subsequence of the iterates reaches a correct solution, and that this condition cannot be weakened in general.
- **Why it matters**: Annealing schedules control whether a fast iterative method lands on the right answer, so precise conditions on them are useful for anyone relying on these solvers. The text reports that the conditions cover linear schedules, for which recent work found the alternative scaling-preserving version fails, and that it gives rate bounds; its relevance beyond this specific algorithm is not established in the text.
- **Background needed**: - Optimal transport: finding a minimum-cost way to rearrange one probability distribution into another, given a cost for each move.
- Entropic regularisation: adding a smoothing term controlled by a parameter (here, the inverse temperature); larger smoothing makes the problem easier to solve but less exact.
- Sinkhorn algorithm: a simple iterative method that alternately rescales rows and columns of a plan until it matches the target distributions.
- Annealing: gradually changing the smoothing parameter during iteration, similar to slowly cooling a material.
- Dual potentials: auxiliary weight functions attached to each distribution whose values drive the transport plan.
- Convergence and summability: whether a sequence settles to a limit; a series is summable if its total sum is finite, and non-summable if it diverges.
- Mirror descent and KL divergence: standard optimisation tools and a measure of mismatch between distributions, used here for rate bounds. · level: research-level

<details><summary>Original abstract</summary>

The annealed Sinkhorn algorithm is an iterative method for approximating solutions of optimal transport problems, in which the entropic regularisation parameter is progressively decreased. As this parameter decreases, one may preserve either the multiplicative scaling factors or the corresponding dual potentials. We study the potential-preserving iterates under positive, non-increasing regularisation schedules tending to zero. We prove that, if the schedule is non-summable, the iterates admit a subsequence converging to a solution of the corresponding optimal transport problem. The non-summability condition is sharp, as for every summable schedule in this class we construct an example in which the iterates converge to a plan violating the prescribed source marginal. We further establish convergence of the entire sequence if the relative inverse-temperature increments are also square-summable, and show by example that non-summability alone does not guarantee full convergence. Our convergence conditions are satisfied by linear inverse-temperature schedules, under which recent work has shown that the scaling-preserving iterates fail to converge to a solution of the optimal transport problem. We also derive convergence rates for polynomial inverse-temperature schedules up to and including linear growth, extending the marginal KL bound obtained by mirror-descent analysis at fixed temperature. Our best rate for the transport cost gap after rounding improves on that established for scaling-preserving annealing. Simple numerical illustrations accompany these convergence results.

</details>

## Statistics theory

### [Identification multiplicity across study designs](https://arxiv.org/abs/2611.29908)
*Carlos Garc\'ia Meixide, David R\'ios Insua* · `stat.ME` · arXiv:2611.29908v1 · relevance 0.09

- **In one sentence**: A framework for collections of causal analyses that identify the same question through different observed-data translations, separating identification discrepancies from differences in causal target, and examining when agreement among them is informative and when averaging retains a causal meaning.
- **In plain words**: Many causal questions, such as whether a policy or treatment works, can be answered by several different statistical analyses, each built on different choices of comparison groups, control variables, or data sources. This paper describes how to organize such a set of analyses, looking at what causal target each one estimates, which assumptions they share, and how their estimates vary together across samples. It works through fourteen example designs and argues that agreement among the analyses mainly tells us about the assumptions that differ between them, not those they all share.
- **Why it matters**: Researchers often report several analyses of one question and treat their agreement as reassurance, so a clear account of what that agreement can and cannot show matters for how evidence is judged. The paper links these ideas to triangulation, instrumental-variable overidentification, marginal treatment effects, transportability, and model-uncertainty inference, though the text alone does not show how far these links carry in practice.
- **Background needed**: - Causal target: the specific effect a study aims to measure, such as the average effect of a treatment in a defined group.
- Identification: whether, under stated assumptions, a causal target can be computed from observed data.
- Adjustment set: the variables controlled for to make groups comparable.
- Instrument: a variable that nudges people toward a treatment without directly affecting the outcome, used when confounding is present.
- Mediator: a variable on the causal path between treatment and outcome.
- Regression discontinuity and staggered adoption: designs that exploit a cutoff or timing of rollout to form comparisons.
- Transportability: moving a result from one population to another.
- Overidentification: having more valid-looking restrictions than strictly needed, which can be tested in part.
- Multiple testing: correcting for many hypothesis tests run on the same data, a different issue from choosing among analyses of one question. · level: research-level

<details><summary>Original abstract</summary>

The answer to a causal question often admits several translations in terms of observed data. These may differ in adjustment sets, comparison groups, instruments, mediators, cutoffs, eligibility occasions, or data sources. We describe the resulting collection of analyses by three structures: the causal target that each analysis identifies under its assumptions, the assumptions that the analyses share, and the sampling dependence among their estimates. A single decomposition separates identification discrepancies from differences in causal targets, and we make both terms explicit in fourteen examples spanning adjustment, comparative panels, proxies, mediators, instruments, discontinuities, staggered adoption, sequential trials, and source combination. Comparisons within a collection can reveal differential violations of assumptions but not a bias common to all analyses; agreement is therefore evidence about the assumptions that differ, not about those that are shared. Averaging retains a causal interpretation in three ways: efficient combination of analyses that identify one target, a projection of a causal curve with a declared approximating family and weighting measure, and inference under weaker premises such as validity of at least one analysis or a known sign of its bias. Precision weights, regression-implied weights, and hierarchical models do not supply these interpretations by themselves. We relate this account to triangulation, overidentification, marginal treatment effects, transportability, and recent methods for inference under model uncertainty, and distinguish identification multiplicity from multiple testing.

</details>

### [Limit theorems for almost conditionally identically distributed random variables](https://arxiv.org/abs/2611.28967)
*Marco Battiston, Lorenzo Cappello* · `math.ST` · arXiv:2611.28967v1 · relevance 0.08

- **In one sentence**: Extends strong law of large numbers, absolute-continuity conditions for the asymptotic directing measure, and three central limit theorems from exchangeable and conditionally identically distributed (c.i.d.) sequences to the broader class of ξ-almost c.i.d. sequences.
- **In plain words**: The paper studies sequences of random quantities that are almost, but not exactly, "identically distributed given the past," a looser version of the exchangeable setting. It proves a law saying that averages settle down to a limit, gives conditions under which that limit has a density relative to a reference measure, and derives three central limit theorems describing how fluctuations around the limit behave. The departure from the exact property is controlled by a parameter sequence ξ.
- **Why it matters**: These results are aimed at justifying large-sample methods for predictive inference, and the text says they support constructing asymptotic credible intervals in Bayesian prediction. The text does not give numerical examples or comparisons, so its practical reach beyond the stated applications is unclear to me.
- **Background needed**: - Exchangeable sequence: the joint distribution does not change when the order of the variables is permuted.
- Conditionally identically distributed (c.i.d.): each new variable has the same distribution conditional on the past, a generalization of exchangeability.
- Strong law of large numbers: sample averages converge almost surely to a limit.
- Directing measure: the random distribution that the empirical frequencies of an exchangeable sequence converge to.
- Central limit theorem: suitably scaled fluctuations around a limit become approximately normal.
- Absolute continuity: the limit distribution has a density with respect to a reference measure.
- Bayesian predictive inference: forecasting new observations from past data, with credible intervals as the Bayesian analogue of confidence intervals. · level: research-level

<details><summary>Original abstract</summary>

$\xi$-Almost Conditional Identically Distributed ($\xi$-a.c.i.d.) random variables are generalizations of conditional identically distributed (c.i.d.) and exchangeable ones. $\xi$-a.c.i.d. random variables arise naturally in applications in statistics, such as in recursive algorithms and heteroskedastic observations, and are parametrized by a sequence $\xi=(\xi_{n})_{n\geq 0}$ that quantifies departure from the c.i.d. property. In this work, we extend limit theorems for exchangeable and c.i.d. random variables to the more general setting of $\xi$-a.c.i.d. random variables. After proving a Strong Law of Large Numbers, we provide necessary and sufficient conditions for the asymptotic directing measure of the sequence to be absolutely continuous with respect to a given $\sigma$-finite measure. Then, under regularity assumptions on the parameter $\xi$, three different Central Limit Theorems for $\xi$-a.c.i.d. sequences are derived, involving the predictive, empirical and asymptotic directing distributions. These theorems have several statistical applications, including the construction of asymptotic credible intervals in Bayesian predictive inference.

</details>

## Statistical methods and applications

### [When AI Performance Is Not Enough: Statistical Guardrails for Clinical Development](https://arxiv.org/abs/2611.28497)
*Siddhesh Kulkarni, Gina D'Angelo, Swarna Reddy et al.* · `stat.ME` · arXiv:2611.28497v1 · relevance 0.13

- **In one sentence**: A commentary arguing that AI and machine learning tools used in clinical drug development need explicit statistical safeguards, reviewing four domains (trial anomaly detection, adaptive monitoring, biomarker enrichment, and digital twins) and proposing context-of-use and estimand thinking as an organizing frame.
- **In plain words**: This commentary looks at how artificial intelligence is being used to help run medical studies that test new treatments, such as spotting odd data, monitoring trials as they go, choosing which patients to enroll, and simulating virtual patients. The authors argue that these tools can work well on their own terms but still produce conclusions that are not statistically valid for approving a treatment. They suggest judging each use by what decision it supports and what assumptions it needs, rather than by performance alone.</plain>
<parameter name="why">Regulators and drug developers are adopting AI faster than statistical standards for it are settling, so the question of when a good-looking model is good enough for a decision about patients is practically important. The text is a perspective piece rather than a study with new data, so it sets out principles and risks rather than measured outcomes.
- **Background needed**: - Clinical trial: a structured experiment testing whether a treatment is safe and effective in people.
- Type I error: a false alarm, concluding a treatment works when it does not; controlling it is central to trial validity.
- Adaptive trial design: a trial that can change its rules partway through based on interim data, which makes error control harder.
- Prognostic vs. predictive biomarker: a prognostic marker predicts how a patient will do overall; a predictive marker predicts who will benefit from a specific treatment.
- Digital twin: a computer model of an individual patient used to predict outcomes or stand in for a control group.
- Estimand (ICH E9(R1)): a precise definition of the treatment effect being estimated, including how events like dropout are handled.
- Context of use: the specific decision a tool is meant to inform, which sets how much evidence it needs. · level: intermediate

<details><summary>Original abstract</summary>

Artificial intelligence (AI) and machine learning (ML) are reshaping the operational and inferential landscape of clinical development, yet their adoption frequently outpaces the statistical scrutiny these methods demand. This commentary offers first-principles perspectives across four application domains: anomaly detection in clinical trial data, real-time monitoring and adaptive trial designs, biomarker-based enrichment, and virtual and digital twins. For each domain, we articulate the underlying inferential problem, the contribution of AI and ML relative to established statistical methods, and the risks that statisticians, data scientists, and clinical developers must actively manage. Across these domains, a unifying theme emerges: AI and ML methods may succeed locally while failing to satisfy the broader statistical assumptions required for valid clinical and regulatory decisions. These risks include false-positive signals, compromised Type I error control in adaptive designs, conflation of prognostic with predictive biomarkers, and causal claims not supported by data and assumptions. We argue that a clearly defined context of use, relevant statistical assumptions, and consequences of the intended decision should guide the evaluation. For treatment-effect questions, the ICH E9(R1) estimand framework provides a useful organizing principle. Responsible use of AI in clinical development requires not restraint, but rigor: the inferential discipline necessary to make these technologies reproducible, interpretable, and defensible in the service of patients.

</details>

### [Quantifying and calibrating precision gain from covariate adjustment in clinical trials with binary endpoints](https://arxiv.org/abs/2611.30845)
*Jannik Hammerschmied, Christian Stock, Martin Schnuerch* · `stat.ME` · arXiv:2611.30845v1 · relevance 0.12

- **In one sentence**: A theoretical framework that quantifies the maximum first-order precision gain from covariate adjustment for marginal treatment effects with binary endpoints, introduces marginal prognostic strength, and proposes a calibration algorithm for simulation studies.
- **In plain words**: Clinical trials often record extra patient details (like age or health markers) and use them to sharpen estimates of whether a treatment works. This paper studies that idea for yes-or-no outcomes, such as whether a patient recovered, where adding such details is less straightforward than for measured outcomes like blood pressure. The authors derive a formula for how much precision can be gained and show that strong prognostic information does not always translate into a more precise treatment estimate.
- **Why it matters**: Choosing whether to adjust for covariates affects how many patients a trial needs, so the question matters for trial design. The text does not say how the results perform in real trials, so their practical impact is best judged from the full paper.
- **Background needed**: - Randomized clinical trial: patients are randomly assigned to treatment or control, so groups are comparable on average.
- Covariate adjustment: using baseline patient characteristics in the analysis to get more precise estimates.
- Precision: how tightly an estimate clusters around the true value; more precision means smaller uncertainty.
- Binary endpoint: an outcome with two possible results (e.g., event or no event).
- Conditional vs. marginal effect: a conditional effect compares treatment within patients sharing the same covariates; a marginal effect compares treatment across the whole population. In nonlinear models like logistic regression these differ.
- Prognostic information: how well covariates predict the outcome.
- Simulation study: computer experiments that generate artificial data to test statistical methods. · level: research-level

<details><summary>Original abstract</summary>

Covariate adjustment is widely used in randomized clinical trials to improve estimation and inference of treatment effects. For continuous endpoints, the reasoning is straightforward: prognostic baseline covariates explain outcome variability and thereby increase precision. For binary endpoints, however, the situation is more complex because conditional and marginal effects generally differ in nonlinear outcome models such as logistic regression. We develop a theoretical framework for quantifying the maximum attainable first-order precision gain from covariate adjustment when estimating marginal treatment effects for binary endpoints. We derive a closed-form identity showing that precision-gain potential is governed by an estimand- and allocation-specific combination of the treatment-specific risk functions. Building on this identity, we introduce marginal prognostic strength as a population-level measure of prognostic information and characterize when it determines precision-gain potential and when the two quantities decouple. Specifically, substantial prognostic information within both treatment arms need not translate into improved precision for the marginal treatment effect when covariates are predictive on the target effect scale. We further develop a calibration algorithm for methodological simulation studies that preserves prespecified conditional outcome structures and marginal risks while allowing data-generating mechanisms to be calibrated by marginal prognostic strength and evaluated in terms of estimand-specific precision-gain potential. Together, these results provide a theoretical and practical framework for understanding, quantifying, and calibrating potential precision gains from covariate adjustment for binary endpoints.

</details>

## AI industry news

### [How iFood scales coding agents across 15,000 repositories](https://openai.com/business/customer-stories/ifood)
** · `openai.com` · OpenAI News · relevance 0.08

- **In one sentence**: A news piece titled "How iFood scales coding agents across 15,000 repositories," though the body text is missing, so only the headline's topic can be reported.
- **In plain words**: The article appears to be about how iFood, a food delivery company, uses AI coding agents (software that writes or changes code on its own) across about 15,000 code repositories (storage areas holding a project's source code). The text itself is not available, so I cannot say what approach was used or what results were reported.
- **Why it matters**: Large companies using AI tools to change code at scale is a live topic in software engineering, so the piece may connect to that trend. However, the body is empty, so I cannot confirm the details or how significant the work is.
- **Background needed**: - Coding agent: an AI system that reads, edits, and tests software with limited human input.
- Repository (repo): a project's stored source code, often tracked with version-control tools such as Git.
- Scaling across many repos: applying the same tool or change to thousands of separate code projects, which raises questions about reliability, review, and cost.
- iFood: a Brazilian food-delivery company, so the work likely reflects its internal engineering practices. · level: intermediate

<details><summary>Original abstract</summary>



</details>

### [Anthropic launches Claude Ship, letting AI agents review, fix, and approve code changes](https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/)
*Sarah Perez* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.07

- **In one sentence**: Anthropic has announced "Claude Ship," developer tools that let AI agents review, fix, and approve code changes, aiming to reduce the approval backlog created by growing volumes of AI-generated code.
- **In plain words**: As AI tools write more software, the step where people check and sign off on each change has become a slowdown. The article reports that Anthropic, an AI company, has launched new developer tools, called Claude Ship, that let AI agents handle some of these routine checks and approvals. The text is brief and does not give details on how the approvals work or how well they perform.
- **Why it matters**: It matters because it reflects a shift toward letting AI systems oversee other AI-written work, which raises practical questions about quality and accountability. The article is short, so its claims about real-world effect are unverified and should be read as a product announcement.
- **Background needed**: - AI agent: a program that carries out multi-step tasks with limited human input, rather than only answering one prompt.
- Code review: the standard practice where another person checks a software change before it is merged into a project.
- Approval bottleneck: when a queue of changes waits on human sign-off, slowing the whole process.
- Anthropic: an AI company that makes the Claude family of AI models.
- Note: the article gives no technical specifics, so details of what "approve" means here are unknown. · level: introductory

<details><summary>Original abstract</summary>

As AI-generated code piles up, Anthropic's new developer tools aim to eliminate another bottleneck by letting agents handle routine approvals.

</details>

### [Tidal to ban and remove millions of AI-generated tracks as AI slop inundates music streaming](https://techcrunch.com/2026/11/24/tidal-to-ban-and-remove-millions-of-ai-generated-tracks-as-ai-slop-inundates-music-streaming/)
*Ivan Mehta* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.07

- **In one sentence**: Streaming service Tidal says it will ban and remove millions of fully AI-generated tracks while still accepting songs made with AI assistance.
- **In plain words**: Tidal, a music streaming service, is moving to remove millions of songs that were created entirely by artificial intelligence, which the headline calls "AI slop" as they flood the platform. The company says it will still allow songs where AI helped in the making but did not generate the whole piece.
- **Why it matters**: Streaming platforms pay royalties per play, so a flood of machine-made tracks can affect how money and listener attention are shared among artists. The source text is very short, so it does not show how Tidal will identify fully generated tracks or what the policy's enforcement looks like.
- **Background needed**: - Music streaming services host catalogs of tracks and pay rights holders based on plays.
- "AI-generated" music is created by software from prompts or models, with little or no human composition.
- "AI-assisted" music means a person used AI tools for parts of the work, such as editing or mixing, while still making the core creative choices.
- "AI slop" is a informal term for low-quality, mass-produced AI content.
- The article is a brief news item; details of the policy are not given in the text provided. · level: introductory

<details><summary>Original abstract</summary>

The company said it will still accept songs that were made with AI assistance, but not fully generated.

</details>

### [Meta brings its Muse AI assistant directly into Instagram DMs](https://techcrunch.com/2026/11/24/meta-brings-its-muse-ai-assistant-directly-into-instagram-dms/)
*Aisha Malik* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.07

- **In one sentence**: Meta has integrated its Muse AI assistant directly into Instagram direct messages, so users no longer need to switch to the separate Muse app to use it.
- **In plain words**: Meta, the company that owns Instagram, has added its Muse AI assistant inside Instagram's private messaging. Until now, people who wanted to use the assistant had to leave Instagram and open a separate Muse app. The article says the change removes that extra step, but it gives little other detail.
- **Why it matters**: It shows a common industry move: putting AI helpers inside apps people already use, rather than asking them to download a new one. The text does not say how many people will use it or how well it works, so its wider significance is unclear.
- **Background needed**: - Meta owns Instagram and Facebook.
- Muse is Meta's AI assistant, which the text describes as an "AI agent" that users talk to.
- "DMs" means direct messages, the private chat feature inside Instagram.
- "Integration" here means building one product into another so they work together.
- The article is short and gives no technical details, pricing, or user numbers. · level: introductory

<details><summary>Original abstract</summary>

The new integration gets rid of the need for users to toggle between Instagram and the Muse app when they want to interact with the AI agent.

</details>

### [How Intentful uses dots to make more time for growth](https://openai.com/business/customer-stories/intentful-dots)
** · `openai.com` · OpenAI News · relevance 0.06

- **In one sentence**: A short company feature describing how Intentful uses a tool called "dot," an AI assistant named Aria, which Marina Petrova uses to research websites, draft proposals, flag messages, and resolve issues.
- **In plain words**: This short article profiles a company called Intentful and how one of its staff, Marina Petrova, uses an AI assistant named Aria, which runs on a product called dot. According to the text, Aria helps with researching websites and writing proposals, and it points out important messages and helps sort out problems before she asks.
- **Why it matters**: It is a small example of how AI assistants are being used for everyday office work, which is a widely discussed trend. The text is a brief user story, so it does not show measured results or how well the tool performs.
- **Background needed**: - "dot" is the name of the AI product in the text; Aria is the assistant Marina Petrova uses.
- An AI assistant is software that carries out routine tasks such as research, drafting, and message triage.
- "Proactively flagging" means the tool raises items on its own rather than waiting to be asked.
- The text is a promotional-style user story with no figures, methods, or independent evaluation. · level: introductory

<details><summary>Original abstract</summary>

Marina Petrova’s dot Aria helps research websites and build proposals, while proactively flagging messages and resolving issues.

</details>

## Model architectures and training

### [Rewirable Circuits in Transformers with Loom Attention](https://arxiv.org/abs/2611.30634)
*Da Xiao, Qingye Meng, Shengping Li et al.* · `cs.LG` · arXiv:2611.30634v1 · relevance 0.30

- **In one sentence**: Proposes "loom attention," in which each attention head's query, key and value are built by a vertical attention over earlier heads' outputs, implemented with normalized, gated linear attention over a per-token matrix memory that acts as a second residual stream, yielding the dual-stream LoomFormer architecture.
- **In plain words**: Transformers are the neural networks behind most modern language AI, and their internal "wiring" (which parts of the model read from which other parts) is normally fixed. This paper proposes a way for the model to rewire those connections for every word it processes, by letting each internal component look at the outputs of earlier components before deciding what to focus on. The authors report that their resulting model, LoomFormer, matches standard Transformers trained with over 3x the compute, and some recent alternative designs trained with about 1.7 to 2.8x, on language modeling and downstream tasks.
- **Why it matters**: If the reported gains hold up, they suggest a cheap way to get more capability per unit of training compute, which matters because training large models is expensive. The text is a single abstract with headline comparisons, so the size and robustness of the gains beyond these settings are not yet clear.
- **Background needed**: - Transformer: a neural network design that processes text by letting each token attend to other tokens.
- Attention head: one of several parallel sub-units inside a layer that each compute a weighted focus over tokens.
- Query, key, value: the three vectors each head computes to decide what to look for, what to offer, and what to pass on.
- Residual stream: the running internal signal that each layer adds its output to; the paper adds a second such stream.
- Linear attention: a cheaper approximation of attention whose cost grows linearly rather than quadratically with text length.
- Pythia: a family of openly released language models of various sizes, used here as baselines.
- FLOPs: a count of arithmetic operations, used as a rough measure of compute cost.
- Few-shot (0-shot, 5-shot): evaluation where the model sees zero or five worked examples in the prompt before answering. · level: research-level
- Matched keywords: transformer, attention, linear attention, architecture

<details><summary>Original abstract</summary>

We propose loom attention, which allows a Transformer to dynamically rewire its circuits at every token by interweaving a head's vertical attention over the outputs of earlier heads (to obtain its query, key and value) with its horizontal attention over tokens. We instantiate vertical attention efficiently with normalized and gated linear attention over a per-token matrix memory, which stores the compressed head outputs and serves as a second residual stream. This yields LoomFormer, a dual-stream architecture that splits control and content between the vector and matrix streams. Across model sizes and training token budgets in language modeling and downstream tasks, LoomFormer matches Transformers trained with over 3x compute and recent residual-stream baselines (HC/mHC, MUDDFormer, AttnRes) trained with ~1.7-2.8x. For example, trained on the same 300B tokens with only 2% extra FLOPs, LoomPythia-2.8B achieves ~1.6x the average downstream gain of mHC-Pythia-2.8B over Pythia-2.8B, and matches (0-shot) or surpasses (5-shot) Pythia-12B. Code is available at https://github.com/Caiyun-AI/LoomFormer

</details>

### [Yggdrasil: Tree-Routed Recurrent Experts for State Tracking and Fast CPU Inference](https://arxiv.org/abs/2611.29954)
*Cosmo Santoni* · `cs.LG` · arXiv:2611.29954v1 · relevance 0.30

- **In one sentence**: Yggdrasil is a parallel-trainable recurrent architecture that routes each layer's transition through a tree-indexed bank of experts, conditioned on the current token and the layer below, to decouple model capacity from per-step CPU latency while aiming to track discrete state.
- **In plain words**: Many fast sequence models, such as Mamba and DeltaNet, process text one step at a time and must read all their weights at every step, so bigger models run slower on a CPU. This paper proposes Yggdrasil, which stores many small recurrent "expert" modules in a large bank and uses a tree of routers to pick just one expert per layer at each step. The authors report that it solves all five state-tracking tasks among the parallel-trainable models they tested, gets the lowest test error on enwik8 and human genome data at matched active size, and runs a single CPU step several times faster than the fastest streaming baseline.
- **Why it matters**: It targets a real tradeoff between model size and speed on ordinary hardware, which matters for on-device and streaming use. The reported gains are from the paper's own comparisons, and the text gives no independent replication, so how far they hold up in wider settings is unclear.
- **Background needed**: - Recurrent model: a model that updates a hidden state one token at a time, like a running summary.
- Parallel-trainable: can be trained across all positions at once on GPUs, even though inference is step by step.
- State tracking: keeping track of a discrete condition (for example, a switch's on/off state) through a sequence; a known weak point of many efficient models.
- Mixture of experts with routing: a learned gate sends each input to a chosen sub-network, so total parameters can grow while per-step compute stays small.
- Active parameters: the subset of weights actually used for one step.
- bpb (bits per byte/base): compression-style score where lower is better; enwik8 is Wikipedia text, hg38 is human genome sequence.
- CPU L2 cache: a small, fast memory close to the processor. · level: research-level
- Matched keywords: attention, linear attention, architecture

<details><summary>Original abstract</summary>

Parallel-trainable recurrences such as Mamba, linear attention, and DeltaNet offer constant-cost streaming inference, but they suffer from two limitations: 1) they struggle to track discrete state, and 2) they read every parameter at every step, tying model capacity directly to CPU latency. We introduce Yggdrasil, a recurrent architecture that decouples capacity from per-step compute by looking up each layer's transition in a large, tree-routed bank of recurrent experts. Each router addresses its bank using the current token and the state of the layer below. We prove that this cross-layer context is necessary---a single token-indexed layer of non-expanding transitions with finitely many reachable states cannot perform conditional resets---while avoiding feedback from the layer's own past preserves parallel-scan training. Because each step traverses one tree path and reads a single expert per layer, active weights stay within a few hundred kilobytes in CPU L2 cache while the full bank resides in RAM. Among the parallel-trainable models we evaluate, Yggdrasil is the only one to solve all five state-tracking tasks. At matched active parameter counts, it achieves the lowest test bits on enwik8 (1.540 bpb) and the human genome hg38 (1.567 bpb), while stepping $3.0\times$ and $3.3\times$ faster on a single CPU core ($6.7\,\mu\mathrm{s}$ and $5.8\,\mu\mathrm{s}$) than the fastest streaming baseline, and delivering the highest GPU throughput of all models at batch 1024. On the Genomic Benchmarks, it is the strongest causal model at matched active parameters (86.0% mean accuracy).

</details>

## Machine learning theory

### [Statistically Optimal and Near Linear Time Hypothesis Selection](https://arxiv.org/abs/2611.30003)
*Satyen Kale, Amirreza Shaeiri, Kunal Talwar* · `stat.ML` · arXiv:2611.30003v1 · relevance 0.21

- **In one sentence**: The paper gives a hypothesis selection learner that achieves the optimal approximation factor of 2 with sample complexity matching Yatracos's factor-3 estimator, removing log factors from prior factor-2 results, and runs in near-linear oracle complexity.
- **In plain words**: Suppose you have a list of candidate probability models for some unknown source of data, and you can draw samples from that source. This paper describes a procedure that picks a candidate, or builds a new distribution, that is nearly as close to the source as the best candidate on the list. It does this with a sample count that depends only on the list size and accuracy, not on the size of the outcome space, and the authors claim it is optimal in its approximation factor.
- **Why it matters**: The approximation factor of 2 is stated in the text as optimal for sample-efficient methods, and the paper claims to reach it without the extra logarithmic factors of earlier work. Its use of multiplicative weights and a cost measured by oracle calls may matter for statistical learning theory, though the text alone does not show wider impact.
- **Background needed**: - Total variation (TV) distance: a measure of how different two probability distributions are, between 0 and 1.
- Distribution over a countable domain: a rule assigning probabilities to discrete outcomes.
- Hypothesis selection: choosing among candidate models using samples from an unknown distribution.
- Approximation factor alpha: the learned output's error may be up to alpha times the best candidate's error, plus a small additive slack epsilon.
- Proper vs. improper learners: a proper learner outputs one of the candidates; an improper one may output a new distribution.
- Sample complexity: how many samples are needed; here O(log(n/delta)/epsilon^2).
- Multiplicative weights: an iterative method that reweights constraints based on how badly they are violated.
- Oracle complexity: counting calls to sampling or comparison routines rather than total computer operations. · level: research-level
- Matched keywords: sample complexity

<details><summary>Original abstract</summary>

In hypothesis selection we are given $n$ distributions $q_1,\dots,q_n$ on a countable domain $\mathcal{X}$ and samples from an unknown distribution $p$. The goal is a distribution $q$ with $\mathrm{TV}(p,q)\le\alpha\min_i\mathrm{TV}(p,q_i)+\epsilon$. The factor $\alpha=2$ is optimal for algorithms using a number of samples from $p$ that is independent of $|\mathcal{X}|$, and in general only improper learners achieve it. We give a learner that achieves $\alpha=2$ with $O(\log(n/\delta)/\epsilon^2)$ samples of $p$, with probability at least $1-\delta$. This matches the sample complexity of Yatracos's factor-$3$ estimator, and it removes the logarithmic factors in the factor-$2$ bound of Bousquet et al. (FOCS 2021). The learner accesses the $q_i$ only through sampling and pointwise comparisons. We measure its running time by its oracle complexity, the number of oracle calls. In expectation it makes $O((n\epsilon^{-2}+\epsilon^{-4}\log(1/\epsilon))\log(n/\delta))$ oracle calls, independent of $\mathcal{X}$. It runs multiplicative weights over the constraints $\mathrm{TV}(q,q_i)\le\mathrm{TV}(p,q_i)$ and uses at most one sample of $p$ per round.

</details>

### [Data-Dependent Probability Estimation via Sample Amplification](https://arxiv.org/abs/2611.28399)
*Vitaly Feldman, Satyen Kale, Mahbod Majid et al.* · `cs.LG` · arXiv:2611.28399v1 · relevance 0.18

- **In one sentence**: The paper gives a sample-efficient estimator for the probability of an event chosen after seeing the data, combining sample amplification with online-optimization-based distribution learning, with matching-up-to-logs upper and lower bounds on squared error.
- **In plain words**: The question is how to estimate the chance of an event that was picked by looking at the same data used to estimate it, when the event could be chosen to mislead a naive count. The authors show that roughly the square root of the domain size many samples is enough for a constant-accuracy estimate, when the rule for choosing the event is known, which is far fewer than the number needed to learn the whole distribution. They also give matching-up-to-logarithmic-factors lower bounds, extensions to other bounded queries and Gaussians, and a smoothed setting where far fewer samples suffice.
- **Why it matters**: It answers an open question posed in a related prior work and shows a clear gap between naive counting and learning the full distribution, which is relevant to adaptive data analysis and the reuse of data. The text does not indicate practical deployments, so its broader impact is uncertain.
- **Background needed**: - Probability distribution over a finite domain of size d, and empirical probability (the fraction of samples in an event).
- Sample complexity: how many i.i.d. samples are needed to reach a target accuracy.
- Mean squared error as the accuracy measure for an estimator.
- Adaptivity: the event is chosen after seeing the data, so naive empirical estimates can be biased.
- Sample amplification: producing more useful samples from fewer, a tool from prior work.
- Online optimization and minimax lower bounds at a conceptual level. · level: research-level
- Matched keywords: sample complexity

<details><summary>Original abstract</summary>

Can we estimate the probability of an event chosen after seeing the data, without using any fresh samples? Its empirical probability can be arbitrarily misleading, while learning the entire distribution to constant accuracy requires $\Theta(d)$ samples on a domain of size $d$. We show that $\widetilde{O}(\sqrt{d})$ samples suffice for constant mean squared error, provided the rule choosing the event is known. More generally, our estimator handles arbitrary $[0,1]$-valued queries and runs in polynomial time given evaluation access to the rule. This sample complexity matches the known lower bound up to logarithmic factors and resolves the open question posed by Feldman, Kale, Raman, Talwar, and Tewari (arXiv:2610.41244). Our estimation framework relies on a new combination of sample amplification (arXiv:1904.12053 and arXiv:2201.04315) with distribution learning via online optimization. Our estimator achieves mean squared error $O(d^{3/4}/n)$ when $d\leq n$ and $\widetilde{O}(d^{1/4}/\sqrt{n})$ when $d>n$. We complement this with a lower bound of $\Omega(\min\{1,\sqrt{d}/n\})$ on the mean squared error. Using our framework, we also design an efficient estimator for data-dependent queries on Gaussian distributions with unknown mean and identity covariance. Finally, we show that a smoothed variant of the problem is much (exponentially) easier. For discrete distributions, if the sample size is chosen uniformly from $\{n,\ldots,2n-1\}$, then $n=O(\log d)$ suffices for constant mean squared error.

</details>

## Large language models

### [From Reward Engineering to Data-Centric Reinforcement Learning for Effective Agentic Visual Tool Use](https://arxiv.org/abs/2611.28558)
*Jin Cui, Xinyue Long, Jiepeng Zhou et al.* · `cs.CL` · arXiv:2611.28558v1 · relevance 0.15

- **In one sentence**: AOVO proposes a data-centric reinforcement learning method, using counterfactual probing and policy-adaptive data sampling (PADS), to teach multimodal LLMs when to call visual tools without adding tool-specific rewards.
- **In plain words**: This paper is about teaching AI models that can read images and text when it is worth using a visual tool, such as one that looks closer at part of a picture. The authors argue that rewarding tool use directly can warp what the model is trying to do, so instead they change which training questions the model practices on, picking those where seeing more of the image would actually help. They report consistent gains over other tool-using models on visual perception and reasoning benchmarks, with some causal analysis supporting the approach.
- **Why it matters**: It offers an alternative to reward design for tool use: changing the training data rather than the scoring rules. Its broader relevance to making AI agents use tools more sensibly is plausible, but the text alone does not establish how far the approach generalizes beyond the benchmarks tested.
- **Background needed**: - Multimodal large language model (MLLM): a language model that takes images as well as text input.
- Tool use: the model calls an external function (e.g., zooming into an image region) to gather more information mid-reasoning.
- Reinforcement learning (RL): training by trial and reward; the model is nudged toward answers that score well.
- Reward engineering: adding extra scoring rules to steer behavior, which can unintentionally change the goal.
- Counterfactual probing: checking how the model's answer changes when its inputs or observations are altered, to see whether the visual information mattered.
- Data sampling: deciding which training questions to show the model and how often. · level: research-level

<details><summary>Original abstract</summary>

Multimodal large language models (MLLMs) increasingly use external visual tools to acquire evidence during reasoning, yet learning when to invoke these tools remains challenging. Existing tool-use reinforcement learning (RL) methods often rely on call-contingent rewards to encourage beneficial tool use, but such reward engineering can distort the task objective and lead to degenerate calling behaviors. We argue that effective tool-use learning requires identifying not merely which questions are difficult, but which failures are attributable to missing visual evidence and can therefore be corrected through tool observations. We propose AOVO, a data-centric framework that enables MLLMs to learn effective tool use through perception attribution and policy-adaptive data sampling (PADS), without introducing tool-specific rewards. It counterfactually probes the model's reasoning states to identify observation-sensitive questions, distinguishing them from reasoning-dominated ones. PADS then periodically estimates category-level observation effects from recent policy rollouts and dynamically reallocates the training distribution toward questions where visual observations provide informative learning signals, while optimizing solely for final-answer correctness. Experiments across diverse visual perception and multimodal reasoning benchmarks demonstrate consistent improvements over competitive tool-use MLLMs, with causal analysis further validating the data-centric perspective for learning effective visual tool use.

</details>

### [Definition-Guided In-Context Learning for Zero-Shot Spoken Language Understanding](https://arxiv.org/abs/2611.28929)
*Neeraj Agrawala, Sriram Ganapathy* · `cs.CL` · arXiv:2611.28929v1 · relevance 0.14

- **In one sentence**: The paper proposes Definition-Guided In-Context Learning (DG-ICL), a fine-tuning method that trains speech-text models to classify spoken input using natural-language definitions of labels, with labels randomized to synthetic tokens or permuted words, so new categories can be added at inference without demonstrations or retraining.
- **In plain words**: Voice systems that sort spoken requests into categories usually need new labeled recordings and retraining whenever the category list changes. This paper tests whether a plain-language description of each category, given in the instructions, is enough for a speech-AI model to handle categories it never saw during training. The authors report that their training method, which hides the usual label names behind random symbols or swapped words, beats standard instruction tuning on held-out tasks with novel labels.
- **Why it matters**: If definitions alone can steer a speech model, category lists could be updated by editing text rather than collecting data and retraining, which matters for real deployments. The text reports gains on three models, but it is a single preprint and the evaluation is limited to the settings described, so the practical reach is still unclear.
- **Background needed**: - Spoken language understanding (SLU): turning speech into structured meaning, such as an intent or slot label.
- Zero-shot / few-shot: handling new categories with no examples, or only a few shown in the prompt.
- In-context learning: a model learns a task from instructions or examples written in its input, without changing its weights.
- Instruction tuning: fine-tuning a model on instruction-and-answer pairs so it follows directions.
- Macro-F1: an accuracy-style score that averages performance across categories, giving rare categories equal weight.
- Audio-language models: models such as Qwen2-Audio, SALMONN and Audio Flamingo 3 that take audio and text as input.
- Counterfactual evaluation: testing whether a model follows a definition even when it contradicts what it learned before. · level: research-level

<details><summary>Original abstract</summary>

Adapting spoken language understanding (SLU) systems to novel or revised label taxonomies conventionally requires additional labeled data and retraining, creating a bottleneck for real world deployment. While in-context learning with few-shot demonstrations offers an alternative, multi-modal generalization and scaling has been challenging. In this work, we investigate whether natural-language definitions alone can guide zero-shot SLU without demonstration exemplars, finding that symbolic definitions serve as the primary supervisory driver for adapting speech-text models. We operationalize this principle as Definition-Guided In-Context Learning (DG-ICL), a fine-tuning framework that decouples semantic categories from fixed lexical names. By replacing labels with dynamically randomized definitions (arbitrary synthetic tokens in DG-ICL-Sym or permuted vocabulary words in DG-ICL-Flip), DG-ICL avoids lexical shortcuts and encourages the model to ground acoustic representations in contextual definitions. Novel categories can thus be introduced at inference simply by defining them through the instructions. Across three speech-text models (AUDIO FLAMINGO 3, QWEN2-AUDIO, and SALMONN), DG-ICL outperforms standard instruction tuning on held-out tasks under novel symbols (0.663 vs. 0.449 macro-F1 on Audio Flamingo 3; 0.703 vs. 0.620 on Qwen2-Audio; 0.582 vs. 0.399 on SALMONN), while remaining competitive on original labels. Furthermore, counterfactual evaluations demonstrate instruction following abilities, where it is shown that DG-ICL-Sym retains 68% of its performance when definitions contradict pre-trained lexical priors, whereas standard instruction tuning elicits significantly reduced retention of 21%. Finally, we show that DG-ICL enables zero-shot speech clustering into user-defined categories specified on the fly

</details>

## Computer vision

### [Let Vision-Language Models Generate Images through Their Representations](https://arxiv.org/abs/2611.31237)
*JB Kim, Byungwoo Jeon, Kyungmin Lee et al.* · `cs.CV` · arXiv:2611.31237v1 · relevance 0.14

- **In one sentence**: Proposes Integral, a method that turns a pretrained vision-language model into a unified model for both image understanding and image generation by building a shared visual representation space, with a lightweight generative branch attached block by block.
- **In plain words**: Researchers want one AI model that can both understand pictures and create new ones, rather than two separate systems. This paper takes an existing model that already understands images and text and adapts it so the same internal visual representations can also be used to generate images. The authors report that sharing these representations between understanding and generation helped image generation learn better than using a separate representation, even though reconstruction quality was comparable.
- **Why it matters**: Combining understanding and generation in one model is an active goal in the field, and the paper's controlled comparison offers a specific reason, shared representations, that may help generative learning. The text does not establish how it compares with other unified models on standard benchmarks, so its wider significance is not yet clear.
- **Background needed**: - Vision-language model: an AI system trained on images paired with text, able to describe or answer questions about pictures.
- Unified multimodal model: a single model that both reads images and produces them.
- Visual representation: the internal numerical description a model builds of an image, used as its working "language" for pictures.
- Frozen encoder: a part of the model whose learned weights are kept fixed during further training.
- Generative learning: training a model to produce new content, such as images, rather than only analyze it.
- Mixture-of-Transformers (MoT): an architecture where separate transformer streams handle different tasks and share information at certain points; here the generative stream exchanges information with the main model only at block boundaries.
- Reconstruction fidelity: how accurately an image can be rebuilt from its representation. · level: research-level

<details><summary>Original abstract</summary>

Recent unified multimodal models aim to combine visual understanding and generation within a single model, yet effectively integrating the two capabilities remains challenging. Leveraging pretrained vision-language models offers a way to build on already learned multimodal knowledge, but making this knowledge effectively accessible to visual generation remains nontrivial. We find that a central challenge lies in the heterogeneous visual representations used for understanding and generation. To address this challenge, we introduce Integral, which converts a pretrained vision-language model into a unified multimodal model by constructing a shared visual representation space across the two capabilities. Integral implements this design through two complementary components. Abstraction Fusion constructs shared visual tokens by aggregating hierarchical representations from the frozen vision encoder, while Block-wise MoT introduces a lightweight generative stream that interacts with the vision-language model only at block boundaries. Our approach effectively preserves the pretrained understanding capability while extending it to strong visual generation. Controlled comparisons further demonstrate that sharing visual representations between understanding and generation substantially improves generative learning compared with using a separate visual representation space, despite comparable reconstruction fidelity. These results suggest that representations learned by pretrained vision-language models already provide an effective foundation for visual generation.

</details>

### [VUOD: A Versatile Unsupervised Outlier Detection Framework for Natural, Industrial, Medical Images and Beyond](https://arxiv.org/abs/2611.28608)
*Zhonghang Liu, Siyuan Chen, Jingwen Yu et al.* · `cs.CV` · arXiv:2611.28608v1 · relevance 0.12

- **In one sentence**: VUOD is an unsupervised outlier detection framework that improves feature discriminativeness using intrinsic distribution priors, aiming to work beyond natural images in industrial and medical settings, and is reported to be plug-and-play in tasks such as image classification and 3D reconstruction.
- **In plain words**: This paper is about spotting images that look unusual without being shown examples of what "unusual" means. Most existing tools were built for ordinary photos and work poorly on factory inspection or medical scans. The authors propose a general framework that sharpens the image features the detector uses, and report that it performs best across 14 benchmark datasets in three domains.
- **Why it matters**: Spotting defective parts or abnormal scans without labeled faults is useful in quality control and healthcare, so a method that transfers beyond natural photos could matter there. The text also claims it can be added to other vision systems to make them more robust, but the abstract gives no details on how much that helps, so the practical value is still unclear.
- **Background needed**: - Outlier (anomaly) detection: flagging inputs that differ from the normal data the system learned from, without labeled anomalies.
- Unsupervised: learning from normal examples only, with no labels marking which items are faulty.
- Feature extractor: a model, often pre-trained on large photo collections, that converts an image into a list of numbers describing it.
- Frozen pre-trained features: reusing such a model without changing its weights; the paper argues this limits performance on non-photo images.
- Feature discriminativeness: how well the features separate normal from unusual images.
- Distribution priors: assumptions about the statistical shape of the data, used here to guide learning.
- Plug-and-play: a component that can be added to an existing system without redesigning it.
- Benchmark datasets: standard public collections used to compare methods fairly. · level: research-level

<details><summary>Original abstract</summary>

Unsupervised outlier detection that automatically identifies whether visual systems involve anomalous images is a significant research topic. However, most approaches are limited to natural images because they rely on frozen and pre-trained feature extractors. So that their performance cannot be maintained in practical scenarios, especially for industrial inspection and medical imaging. In this work, we first revisit this task and then introduce a versatile unsupervised outlier detection framework to enrich the application domains. The core idea of this framework is to improve feature discriminativess via exploiting intrinsic distribution priors. Evaluated on 3 domains and 14 benchmark datasets, our proposed solution achieves state-of-the-art performance and significantly outperforms existing methods. More importantly, we show its plug-and-play property that can be integrated into diverse visual applications to improve their robustness, such as image classification and 3D reconstruction.

</details>

## Reinforcement learning

### [Reinforcing Diffusion Models by Instantaneous Trajectory Distribution Matching](https://arxiv.org/abs/2611.30986)
*Yihong Luo* · `cs.LG` · arXiv:2611.30986v1 · relevance 0.25

- **In one sentence**: The paper proposes iTDM, an infinitesimal-limit variant of Trajectory Distribution Matching for reinforcement learning of diffusion models with deterministic ODE sampling, which uses an online auxiliary denoiser to track the behavior velocity and suppress baseline-induced gradient drift.
- **In plain words**: Image-generating diffusion models can be tuned with reward signals so their outputs better match goals such as correct text rendering or following a prompt's composition. The authors argue that a common tuning approach quietly assumes the model being trained behaves like the model that produced the samples, and that this assumption fails in practice, which can make training unstable. They propose a new update rule, iTDM, that anchors each gradient step to the sampling behavior and reports better results on several benchmarks.
- **Why it matters**: The paper points to a specific stability problem in a widely used fine-tuning family and offers a fix with reported gains in convergence speed and in-domain and out-of-domain performance. The evidence is the authors' own experiments as described in the abstract; the work has not been independently checked, so its practical impact is not yet established.
- **Background needed**: - Diffusion models: generative models that create images by gradually removing noise, here sampled along a deterministic path (an ODE).
- Reinforcement learning (RL) for generators: adjusting a model using a reward score on its outputs, rather than only imitating training data.
- Reward-weighted regression: a method that nudges the model toward its sampled outputs, weighted up or down by reward.
- Baseline subtraction: subtracting an average reward to reduce noise in the training signal; it is only unbiased under certain assumptions.
- Behavior vs. policy: the behavior distribution is the one that generated the samples; the policy is the model being trained. They differ under guidance, offline data, or lagging updates.
- Classifier-free guidance (CFG): a sampling technique that strengthens prompt adherence and changes the sampling distribution.
- Benchmarks: GenEval2 tests compositional image generation; text rendering and preference alignment are other evaluation targets. · level: research-level
- Matched keywords: reinforcement learning, offline RL

<details><summary>Original abstract</summary>

Forward diffusion reinforcement learning (RL)---enabling deterministic ODE sampling without trajectory backpropagation---has grown increasingly popular for efficiently aligning diffusion models. However, we reveal that existing methods essentially rely on signed reward-weighted regression (RWR), regressing the \emph{trainable policy} velocity onto rollouts from a \emph{behavior distribution}. Unbiased baseline subtraction implicitly assumes that the policy velocity equals the behavior marginal velocity---an idealized assumption violated under classifier-free guidance (CFG) rollouts, offline/off-policy updates, and imperfect online self-consistency. This \emph{behavior--policy mismatch} breaks baseline invariance and injects \emph{baseline-induced gradient drift}, destabilizing training. To resolve this issue, we propose \textbf{I}nstantaneous \textbf{T}rajectory \textbf{D}istribution \textbf{M}atching (\textbf{iTDM}), taking the infinitesimal limit of Trajectory Distribution Matching toward a time-local reward-guided target via the posterior-score identity to yield a sample-level gradient anchored at the behavior velocity without learning an additional reward-tilted target score. Tracking this velocity with an online auxiliary denoiser guarantees exact baseline invariance at the auxiliary optimum, effectively suppressing baseline drift across both online and offline RL. Extensive experiments across compositional generation, text rendering, and preference alignment show that iTDM achieves state-of-the-art in-domain and out-of-domain performance. Notably, on the challenging GenEval2 benchmark, iTDM converges nearly $3\times$ faster than competing methods while scaling smoothly to $0.87$ without collapse. Code is available at https://github.com/Luo-Yihong/iTDM

</details>

### [Direct Feedback Policy Optimization for AI Coding Agents](https://arxiv.org/abs/2611.29193)
*Fei Ding* · `cs.LG` · arXiv:2611.29193v1 · relevance 0.23

- **In one sentence**: DFPO is a single-trajectory reinforcement learning method for training AI coding agents that learns from one run of a multi-turn task rather than from groups of repeated samples, and reports higher task resolution than GSPO under matched base models and harnesses.
- **In plain words**: This paper looks at how to train AI systems that write, edit, and test code over many steps. Current training methods often give a single pass/fail score only at the very end, which makes it hard to tell which intermediate steps helped. The authors propose a training method, DFPO, that learns from a single attempt at a task, and they report that it resolves more tasks than a comparison method, GSPO, when both use the same base model and test setup.
- **Why it matters**: Training coding agents is costly, and needing many repeated attempts per task adds to that cost, so a method that works from one attempt could matter if the reported gains hold up. The text does not give the size of the gain, the benchmarks used, or how robust the result is, so its significance is uncertain from this summary alone.
- **Background needed**: - Reinforcement learning: training by trial and reward, where a system is scored on outcomes and adjusts its behavior.
- Coding agent: a language model that takes actions over several turns, such as editing files and running tests.
- Sparse terminal reward: a score given only at the end of a task, with little feedback on earlier steps.
- Group-relative methods: approaches that compare several sampled attempts at the same task to judge which was better; they need repeated sampling per task.
- GSPO: an existing group-based policy optimization method used here as the baseline.
- Task resolution rate: the share of tasks the agent completes correctly.
- Matched base models and harnesses: the comparison holds the underlying model and the surrounding execution setup constant. · level: research-level
- Matched keywords: reinforcement learning

<details><summary>Original abstract</summary>

AI coding agents generate, modify, and validate code through multi-turn interactions. Existing reinforcement learning methods often rely on sparse terminal rewards, making it difficult to assess how intermediate decisions affect task outcomes, and group-relative methods also require repeated sampling for each task. We propose Direct Feedback Policy Optimization (DFPO), a single-trajectory reinforcement learning algorithm that trains directly from a single trajectory. DFPO achieves higher task resolution rates than GSPO under matched base models and execution harnesses.

</details>

## AI safety and alignment

### [What Counts as Attack Success? Evaluating Harmfulness in Red Teaming LLMs](https://arxiv.org/abs/2611.28038)
*Ruyuan Wan, Adriana Alvarado Garcia, Md Toufikuzzaman et al.* · `cs.CL` · arXiv:2611.28038v1 · relevance 0.19

- **In one sentence**: A review of 76 red-teaming papers finds that studies often borrow their definition of "harmful" from prior work, and that different automated evaluators applied to identical outputs can disagree enough to change model comparisons.
- **In plain words**: Researchers often test AI chatbots by trying to get them to produce harmful answers, then use automatic graders to decide whether each attempt "succeeded." This paper checks how those studies define harm and finds they often copy someone else's definition instead of stating their own. When the same answers were graded by evaluators from different papers, the verdicts often differed, which could change which model looks safer.
- **Why it matters**: Safety claims about AI models often rest on these attack success rates, so a grader's hidden definition of harm can quietly decide the headline result. The paper's call for stated criteria and validated graders is a practical point for anyone reading or comparing safety benchmarks.
- **Background needed**: - Red teaming: deliberately trying to make an AI system misbehave, to find its weaknesses.
- Attack success rate: the share of such attempts that the study counts as having produced a harmful response.
- Automated evaluator or "judge": another model or classifier, guided by a prompt, that labels a response as harmful or not, standing in for human reviewers.
- Refusal versus harm: some evaluators count any non-refusal as a failure, while others count only answers that could plausibly cause real harm.
- Benchmark and dataset: a fixed set of test prompts and labeling rules that many studies reuse. · level: intermediate
- Matched keywords: red teaming

<details><summary>Original abstract</summary>

Judging whether a model response is harmful requires contextual and normative choices, yet red-teaming studies often delegate this judgment to automated evaluators. We examine how harmfulness criteria are specified in red-teaming research and how they carry through to reported results. Reviewing 76 papers, we find that many adopt their criteria from prior datasets, classifiers, or judge prompts rather than defining harmfulness themselves. Applying evaluators from these papers to identical outputs, we find that they can reach different judgments on the same response, which can change conclusions when comparing models. These differences arise partly because evaluators draw the boundary of harm in different places: some count any response that does not refuse, while others count only output that could plausibly cause harm. We argue that red-teaming studies should state their harmfulness criteria and report how they chose and validated their evaluators to support more reliable measurement and interpretation.

</details>

### [Which Loopholes Get Found? Predicting Reward Hacking of LLM Judges Before RL Training](https://arxiv.org/abs/2611.29651)
*Xuanyi Lyu, Yuezhou Zhao, Qing Qin* · `cs.CL` · arXiv:2611.29651v1 · relevance 0.18

- **In one sentence**: The paper proposes "exposure" (a policy's propensity to produce a given degenerate pattern times the judge's false-positive rate) as a pre-training predictor of which loophole a GRPO-trained policy will exploit first, and tests it causally with seeded patterns across 36 runs and seven judges.
- **In plain words**: When an AI model is trained to please another AI model that acts as a grader, it can learn to game the grader with junk answers the grader wrongly accepts. This paper asks whether we can predict, before training starts, which junk answer the model will discover first. The authors score each pattern by how often the starting model produces it times how often the grader wrongly accepts it, then test that score by deliberately planting patterns in fine-tuning data.
- **Why it matters**: Reward hacking is a central worry in AI safety, because a model optimised against a flawed grader can look successful while not doing the intended task. A pre-training audit that flags the likely first exploit could help developers check graders before spending compute on reinforcement learning, though the text reports results only for the specific setup tested.
- **Background needed**: - LLM judge: a language model used to score another model's answers, standing in for human graders.
- Reward hacking: a trained system finding a way to get high scores without meeting the real goal.
- GRPO (group relative policy optimisation): a reinforcement learning method that compares several sampled answers to the same prompt and reinforces the better ones.
- Group-normalised advantage: how much better an answer is than its group's average; a large value means a strong training signal.
- False-positive rate (FPR): how often the judge wrongly accepts a bad answer.
- Propensity: how likely the starting model is to produce a given pattern on its own.
- Latin square: an experimental design that balances conditions so each dose and pattern appears in controlled combinations.
- Seeding: deliberately inserting examples of a pattern into training data to test its effect. · level: research-level
- Matched keywords: reward hacking

<details><summary>Original abstract</summary>

A policy trained against an LLM judge can learn to exploit its loopholes. Static probes show that such judges accept degenerate answers like a lone "{" or "Thought process:", but not which flaw a policy will find. In GRPO the first loophole to be exploited can be predicted before training from each pattern's exposure, the product of the starting policy's propensity to produce it and the judge's false-positive rate (FPR). To test exposure causally, we seed the patterns into fine-tuning at three doses in a Latin square. Across 36 GRPO runs with seven judges, the first exploited pattern had the highest exposure in all 12 runs with exploitation and the highest FPR in only 6. Predictions recorded before training held in three of four runs with one pattern masked by rule. When only two patterns were seeded, at 3% to 3.8% of the fine-tuning data and chosen so that exposure disagreed with FPR alone or propensity alone, exposure named the first exploited pattern and its onset window in all six runs. Exploitation occurred only on hard prompts, where an accepted exploit gets a large group-normalized advantage. Auditing exposure before RL therefore identifies the loophole a policy will likely exploit first.

</details>

## Interpretability

### [SAE-Audit: Clinical-Trial Prediction via Inference-Time Optimization of Black-Box LLMs Audited by Sparse Autoencoder Evidence](https://arxiv.org/abs/2611.29368)
*Junbo Shen* · `cs.AI` · arXiv:2611.29368v1 · relevance 0.20

- **In one sentence**: SAE-Audit uses concepts extracted from a frozen sparse autoencoder on an open Llama-3.1-8B model, weighted by sparse probes fitted on past trials, to feed evidence into inference-time optimization of black-box LLMs for clinical-trial outcome prediction.
- **In plain words**: The paper looks at predicting whether a registered clinical trial will finish or stop early, a task where large language models have been only slightly better than guessing. The authors attach evidence to each new trial protocol: clinical concepts found inside an open model, each marked as pointing toward or away from the outcome based on past trials. The audited model then revises its answer in light of that evidence, and the authors report accuracy gains without any retraining.
- **Why it matters**: Trial outcome forecasting could help plan costly, slow studies, and the method tries to make the model's reasoning traceable to specific concepts rather than opaque. The text reports gains on several tasks, but the evaluation details and comparisons are not shown here, so the strength of the result is not yet clear.
- **Background needed**: - Clinical trial: a structured study testing a medical treatment; "completes" versus "terminates early" is the outcome being predicted.
- Large language model (LLM): an AI text model; "black-box" means its internals are not accessible, so it can only be prompted.
- Balanced accuracy: a score that averages accuracy across outcome classes, so a model cannot look good by always guessing the common class.
- Sparse autoencoder (SAE): a tool that splits a model's internal activity into many separate, more human-readable features, here treated as clinical concepts.
- Sparse probe: a simple, selective classifier that checks which features predict an outcome.
- Inference-time optimization: improving an answer while the model is running, by adjusting prompts or evidence, without retraining it.
- Interpretability: methods for explaining why a model produces its outputs. · level: research-level
- Matched keywords: sparse autoencoder

<details><summary>Original abstract</summary>

Clinical trials are costly and often take years to complete, making early outcome prediction valuable for trial planning. Large language models (LLMs) are increasingly used to forecast clinical-trial outcomes, yet their predictions remain unreliable and their rationales may not faithfully reflect the evidence underlying their answers. On tasks such as predicting whether a registered clinical trial will complete or terminate early, frontier LLMs perform only modestly above chance in our experiments. We introduce SAE-Audit, which optimizes a black-box LLM at inference time with evidence obtained from a deployable open model. A frozen sparse autoencoder (SAE) on Llama-3.1-8B-Instruct is converted into a vocabulary of clinical concepts. Sparse probes fitted on past trials determine which concepts are associated with the outcome. For a new protocol, the concepts detected by the probe are written as evidence, each with the direction and strength of its association with the outcome, and the LLM being audited optimizes its answer in the light of this evidence. Without additional training, SAE-Audit raises balanced accuracy of deepseek-v4-flash by 9.6--12.0 points on five clinical-trial prediction tasks and raises GPT-5.6-terra by 8.0 points on trial completion, exceeding other agentic inference-time optimization methods by a large margin. As an auxiliary, SAE probes module within SAE-Audit is itself accurate and auditable, providing natural-language explanations directly derived from verified concept contributions and protocol evidence, without requiring additional LLMs at inference time. SAE-Audit provides verifiable, concept-level evidence for more accurate and auditable clinical-trial prediction. It can also be embedded into biomedical AI agents such as Biomni to optimize their performance.

</details>

### [SAEPO: Sparse-Autoencoder-Guided Credit Assignment for Policy Optimization](https://arxiv.org/abs/2611.29936)
*Yusong Zhao, Zihao Zhao, Zirui Zhang et al.* · `cs.AI` · arXiv:2611.29936v1 · relevance 0.17

- **In one sentence**: SAEPO uses concepts from a pretrained sparse autoencoder to assign token-level credit inside reasoning trajectories, as a plug-in advantage-shaping module for GRPO and GSPO policy optimization under outcome-only (RLVR) rewards.
- **In plain words**: Training language models to reason often gives only one score for a whole answer: right or wrong. This paper proposes a way to spread that score across individual words in the reasoning, so the model can tell which parts helped or hurt. It uses a tool that finds recurring patterns, called concepts, inside the model's own internal activity, and rewards or penalizes tokens based on those concepts.
- **Why it matters**: Finer-grained feedback could make reinforcement learning for reasoning models more efficient, which matters for training base models from sparse outcome signals. The text reports gains of up to 6.63% on math and 5.57% on code averages across three backbones, but these are the authors' own benchmark results and I have not checked how robust they are.
- **Background needed**: - Reinforcement learning with verifiable rewards (RLVR): a model is trained by checking whether its final answer is correct, with no feedback on intermediate steps.
- Credit assignment: deciding which specific steps or words deserve credit or blame for an outcome.
- Policy optimization (GRPO, GSPO): families of algorithms that adjust a model's outputs toward higher-reward responses.
- Advantage shaping: modifying the learning signal (the "advantage," how much better than expected an action was) before it updates the model.
- Sparse autoencoder (SAE): a method that learns a set of human-inspectable features from a model's internal activations, without labels.
- Base model: a language model before instruction tuning or alignment. · level: research-level
- Matched keywords: sparse autoencoder

<details><summary>Original abstract</summary>

Reinforcement Learning with Verifiable Rewards (RLVR) has demonstrated strong performance in improving large language model (LLM) reasoning, yet its credit-assignment signal remains coarse. Outcome verifiers provide scalable supervision by judging whether a completed response is correct, but they do not directly indicate which intermediate reasoning tokens contribute to success or failure. As a result, policy optimization can be inefficient, especially when training base models directly from sparse outcome feedback. In this paper, we introduce SAEPO, a Sparse AutoEncoder-guided token-level credit assignment method for outcome-supervised Policy Optimization. Rather than treating correctness only as a rollout-level (sequence-level) signal, SAEPO uses a pretrained sparse autoencoder (SAE) to build token-level semantic representations within reasoning trajectories; it scores each token based on the SAE concepts (e.g., penalizing wrong "final-answer" tokens but rewarding correct "reasoning-process" tokens), learned in an unsupervised manner, to achieve fine-grained credit assignment. SAEPO is a plug-in advantage-shaping module compatible with various policy optimization algorithms. We instantiate SAEPO with both GRPO and GSPO, covering token-ratio and sequence-ratio policy-gradient objectives, and evaluate SAEPO across three LLM backbones on six math and two code benchmarks. Empirical results show that SAEPO improves both the math and code benchmark averages over the matched baselines, with gains of up to 6.63% and 5.57%, respectively. On Qwen3-1.7B-Base, training curves also show faster early accuracy growth. Feature and token-level analyses suggest that the SAE-derived signal favors question-relevant concepts and reasoning tokens.

</details>

## AI for mathematics

### [Improving semantic equivalence in research-level math formalization](https://arxiv.org/abs/2611.28819)
*Ayush Khaitan, Liam Fowl, Tom\`as Ortega et al.* · `cs.AI` · arXiv:2611.28819v1 · relevance 0.21

- **In one sentence**: The paper studies whether training language models on the differences between research-level natural-language math and its faithful Lean formalization improves in-project Lean writing, reporting higher proof completion and statement agreement on held-out repositories.
- **In plain words**: Mathematicians increasingly write proofs in Lean, a computer language that checks math automatically, but a Lean version of a paper is never a word-for-word copy: it changes definitions, adds helper results, and splits arguments. The authors collected about 4,000 audited examples of these changes from 832 Lean projects and used them to train AI models to write Lean inside large real projects. Training on these differences roughly doubled the share of complete proofs on unseen projects (from 11% to 20%) and raised the share of statements matching the project's own formalization (from 30% to 39%).
- **Why it matters**: It offers a concrete, measured way to make AI help with formal mathematics more faithful to the source text, which matters if such tools are to assist real research projects. The text does not show how well the gains hold beyond these test repositories or for other formal systems.
- **Background needed**: - Lean: a programming language and proof assistant in which mathematical statements and proofs are written and machine-checked.
- Autoformalization: using AI to translate informal mathematical text into formal Lean code.
- Formalization project / repository: a large body of Lean code, here tens of thousands of lines, built around one research area.
- Semantic equivalence: whether the formal statement means the same thing as the intended mathematics, not just whether it compiles.
- Complete proof rate: the share of tasks where the model produces a proof that the Lean checker accepts.
- Adapter: a small add-on module trained on top of a larger model, used here as a comparison condition.
- Train/test split by repository: the test projects were unseen during training, which makes the results a fairer check of generalization. · level: research-level
- Matched keywords: Lean, autoformalization

<details><summary>Original abstract</summary>

Formalizing mathematics in Lean is never a word-for-word translation of a paper: a Lean formalization changes definitions, strengthens hypotheses, splits arguments, and adds lemmas the paper never mentions. It stands to reason that a model that is good at autoformalization must be a good predictor of how a natural language source must differ from its faithful Lean formalization. With that in mind, we collect 4{,}076 audited examples of such changes from 832 Lean projects that formalize research-level mathematics, and use them to ask a practical question: how well can a model \emph{write} Lean inside a real research-level project that may contain tens of thousands of lines of code, and does training on discrepancies between natural language sources and their faithful Lean formalizations help? Our training set consists of 3{,}431 tasks from 141 repositories, and the test set consists of 645 tasks from the remaining 27 repositories. Training on in-project Lean nearly doubles complete proofs ($11\% \to 20\%$) and raises the share of statements in gold agreement with the project's own formalization by nearly a third ($30\%$ to $39\%$). The gain comes from the pairs themselves: an adapter trained only to predict how the Lean will differ, or a model told the difference in advance, barely helps. Training on where formalizations depart from their sources is thus an effective way of improving semantic equivalence in research-level formalization.

</details>

### [AI-Assisted Auto-formalization for Trustworthy Scientific Computing: Case Studies and Lessons Learned](https://arxiv.org/abs/2611.31033)
*Mohit Tekriwal, Het Mankad, Naifeng Zhang et al.* · `cs.AI` · arXiv:2611.31033v1 · relevance 0.16

- **In one sentence**: A systematic study of AI-agent-assisted formalization (machine-checked proofs) of numerical and scientific computing results, yielding a cross-layer taxonomy of failure modes and the kinds of expert feedback needed to restore mathematical soundness.
- **In plain words**: Researchers tested whether modern AI coding and math agents can turn applied-math and scientific-computing material into formal, computer-checked proofs. Unlike pure math, these sources often describe a computational procedure or a modeling step rather than a clean theorem, so the AI has more trouble. The paper catalogs where and why the agents failed across several layers of scientific software and proposes a workflow for recurring proof patterns.
- **Why it matters**: Scientific computing underpins U.S. Department of Energy work, so proofs that software is mathematically sound matter for trust in simulations. The paper is a careful account of limits and failure modes rather than a claim of a general solution, and its practical value is described in the text only in broad terms.
- **Background needed**: - Auto-formalization: translating informal math or code descriptions into a formal language a proof checker can verify.
- Proof assistant / formal library: software (e.g., Lean-style systems) that checks each logical step and provides reusable verified results.
- Scientific computing: using algorithms and software to simulate physical systems, such as solving equations numerically.
- Numerical soundness: whether an algorithm's computed output is guaranteed to be accurate within stated assumptions, not just whether it runs.
- AI agents: coding or math assistants (e.g., Claude Code, Codex, Aristotle) that act through multi-step tool use.
- Background context: the abstract cites prior successes on Fermat's Last Theorem, Erdős problems, and IMO-level problems, mostly in pure math. · level: research-level
- Matched keywords: mathematical reasoning

<details><summary>Original abstract</summary>

Agentic AI tools have recently had success in mathematical reasoning. Both general purpose coding agents such as Claude Code and Codex, and specialized mathematics agents such as Aristotle, have been used for formalizing mathematical problems such as Fermat's last theorem, Erd\H{o}s problems and several IMO level math problems. However, much of these efforts are concentrated in the pure mathematics domain, which benefits from relatively self-contained theorem statements, fixed mathematical representation and extensive support in existing formal libraries. Applied mathematics, on the other hand, presents additional challenges because the source may describe a computational procedure or modeling transformation rather than a declarative theorem. In this work, we present a systematic study of AI-assisted auto-formalization for scientific computing (SC), a domain in applied mathematics central to U.S. Department of Energy applications. Through case studies spanning hierarchical abstraction layers in SC software stack, we evaluate not only whether AI agents can complete numerical proofs, but also where and why they fail across the stack. Our primary contribution is a cross-layer taxonomy of failure modes and an analysis of the form of expert feedback required at each layer to recover mathematical soundness. From these observations, we derive a workflow for recurring proof patterns and practical guidance for using AI agents while preserving mathematical soundness. Our results characterize both the practical value and the current limitations of AI-assisted formalization for trustworthy scientific computing.

</details>

## Robotics and embodied AI

### [SAGE-Drive: Benefit-Aware Adaptive Reasoning for Autonomous Driving Planning](https://arxiv.org/abs/2611.29947)
*Donglei Rong, Wenbin Yao, Congcong Bai et al.* · `cs.RO` · arXiv:2611.29947v1 · relevance 0.14

- **In one sentence**: SAGE-Drive learns to predict, from an initial non-reasoning trajectory plan and multimodal scene features, when explicit reasoning will reduce planning error in autonomous driving, and invokes reasoning only on the top-predicted scenarios under a fixed compute budget.
- **In plain words**: Self-driving cars can think through tricky traffic before choosing a path, but that thinking costs computing time. This paper asks when the extra thinking actually helps, and builds a gate that predicts which situations benefit most and only spends that effort there. On 1,497 paired driving scenarios, the extra reasoning helped in about 53.5% of cases and hurt in 46.5%, so on average it made almost no difference.
- **Why it matters**: Reasoning is expensive, and the paper suggests a way to spend it selectively while keeping accuracy close to always reasoning. The reported gains are small in absolute terms (for example, an error of 1.5191 m at a 20% budget versus 1.5252 m for random selection), so the practical value depends on how the method holds up beyond this dataset; the text does not show deployment or real-road tests.
- **Background needed**: - Trajectory planning: choosing the path a vehicle should follow over the next few seconds.
- Average displacement error (ADE): the average distance between the planned path and the actual path, in metres; lower is better.
- Explicit reasoning: the model generating intermediate step-by-step analysis of the scene before outputting a plan, which costs extra computation.
- Reasoning benefit: the reduction in planning error gained by reasoning, measured by comparing paired plans with and without it.
- Reasoning budget: the fixed share of scenarios allowed to use the costly reasoning step (e.g., 20% or 35%).
- Multimodal scene information: inputs combining different sensor or data types describing the road scene. · level: research-level

<details><summary>Original abstract</summary>

Explicit reasoning enables autonomous vehicles (AVs) to interpret complex traffic interactions and support trajectory planning, but introduces additional computational demands. Determining when explicit reasoning can improve planning accuracy remains a key challenge, as its benefits vary across driving scenarios. To address this challenge, this study proposes Scene-Adaptive Gating of Explicit Reasoning for Driving (SAGE-Drive), a benefit-aware adaptive reasoning framework for autonomous driving planning. First, paired planning outcomes with and without explicit reasoning are analyzed to measure the reasoning benefit, i.e., the reduction in planning error achieved by explicit reasoning, which serves as the supervision label. SAGE-Drive then learns to predict these benefits using geometric features of the initial trajectory planned without reasoning and multimodal scene information, and invokes explicit reasoning only for the scenarios with the highest predicted benefits under a predefined reasoning budget. Experiments on 1,497 paired driving scenarios reveal that explicit reasoning improves planning accuracy in 53.5% of cases while degrading it in 46.5%, yielding a near-zero average benefit. On the test set, with a 20% reasoning budget, SAGE-Drive achieves an average displacement error (ADE) of 1.5191 m, compared with 1.5252 m for random selection. At a 35% budget, it achieves an ADE of 1.5148 m, close to the 1.5141 m obtained when reasoning is applied to every scenario. These findings establish the predicted reasoning benefit as an effective criterion for reasoning selection, allowing explicit reasoning to be invoked where it improves planning accuracy at a fraction of its computational cost.

</details>

### [Your Diffusion-Based Driving Planner Only Needs a Nudge](https://arxiv.org/abs/2611.29123)
*Zilin Wang, Guozheng Ma, Saeed Rahmani et al.* · `cs.RO` · arXiv:2611.29123v1 · relevance 0.14

- **In one sentence**: PlanNudge freezes a pretrained diffusion-based driving planner and trains a small MLP "nudge policy" with off-policy RL to adjust the plan's speed and curvature, reporting matched or better scores than the prior RL finetuning method on nuPlan with about one sixth the environment steps.
- **In plain words**: Self-driving planners trained on human driving data can drift into collisions or off the road when they encounter situations unlike their training data. This paper proposes a small add-on that makes slight corrections to the planner's chosen path, adjusting its speed and steering curvature, while the original planner stays unchanged. On the nuPlan driving benchmark, the authors report that this matches or beats the previous best reinforcement-learning fine-tuning method while using far less simulated experience.
- **Why it matters**: Fine-tuning a capable planner without destroying what it already learned is a practical problem for autonomous driving, and the claim that small corrections prevent many unsafe outcomes is a concrete, testable idea. The text does not say how it would transfer to real vehicles or other domains, so its wider significance is uncertain.
- **Background needed**: - Diffusion model: a generative method that produces outputs by gradually removing noise; here it generates candidate driving trajectories.
- Covariate shift: when a model meets inputs unlike its training data, so its errors compound over time.
- Closed-loop simulation: testing where the planner's actions change what it sees next, rather than replaying recorded data.
- Receding-horizon execution: the planner computes a long plan but only executes the first part before replanning.
- Reinforcement learning (RL) finetuning: improving a trained model by rewarding good behavior in simulation.
- Off-policy RL: learning from experience gathered by any policy, which tends to be more sample-efficient.
- nuPlan: a public autonomous driving benchmark built on real-world driving logs.
- Multilayer perceptron (MLP): a simple feedforward neural network. · level: research-level

<details><summary>Original abstract</summary>

Diffusion-based planners capture the multimodality of human driving behavior well, yet covariate shift in closed-loop driving can lead them to generate trajectories that result in collisions or road departures. Reinforcement learning (RL) finetuning offers a promising way to tackle this issue, but applying it to diffusion-based planners is complicated by their iterative denoising process and receding-horizon execution. We find that small adjustments to the planned trajectories can prevent many of these unsafe outcomes. Motivated by this observation, we propose PlanNudge, which preserves the learned planning capabilities of a pretrained diffusion-based planner by freezing it and trains a lightweight policy that we call the nudge policy. At each planning step, the nudge policy outputs a nudge, a two-dimensional adjustment of the speed and curvature of the plan from the frozen planner. The nudge policy is a multilayer perceptron that predicts the nudge in a single forward pass, and both dimensions directly change the motion of the vehicle, so standard off-policy RL can train it in closed-loop simulation. We evaluate PlanNudge on nuPlan, a large-scale autonomous driving benchmark based on real-world driving data. In all six settings, PlanNudge matches or exceeds the final scores of the previous state-of-the-art RL finetuning method while using about one sixth as many environment steps and less than one fifth as much model compute. We also provide guidelines for reward shaping, value learning, and exploration when using off-policy RL to post-train autonomous driving planners. Our results are reported with means and standard deviations over six training runs. Project page: https://zerlinwang.github.io/plannudge/

</details>

## Security and cryptography

### [LaTSEC: Lattice-Based Threshold Signatures with Native Non-Interactive Identifiable Abort and Compact Per-Party Storage](https://arxiv.org/abs/2611.30063)
*Muhammad Arzaki, Muhammed F. Esgin, Markku-Juhani O. Saarinen et al.* · `cs.CR` · arXiv:2611.30063v1 · relevance 0.13

- **In one sentence**: LaTSEC is a three-round lattice-based threshold signature scheme that identifies misbehaving signers non-interactively by checking each partial signature against a per-party public abort key, built on the SEC ramp everywhere-short secret sharing scheme and proven secure under standard MLWE and MSIS assumptions.
- **In plain words**: This paper is about a way for a group of people to jointly produce a digital signature so that no single person holds the whole signing key, and if someone cheats or sends a bad piece, the group can tell who it was. The authors propose a scheme where each member keeps only one small secret piece and has one public check value, so bad pieces can be traced to their sender without extra back-and-forth rounds of messages. For 60 parties at 128-bit security, they report it tolerates up to 6 corrupted parties, and a random group of at least 46 can sign with probability at least 0.99.
- **Why it matters**: Threshold signatures are used to protect high-value keys, and post-quantum (lattice-based) versions are an active area as classical schemes face future quantum attacks. Reducing per-party storage and removing extra interaction for finding cheaters may make such schemes more practical, though the text does not establish deployment readiness or how it compares in real systems.
- **Background needed**: - Threshold signature: a signature that t-of-n parties can produce together, with no one party holding the full key.
- Identifiable abort: when signing fails, the protocol can name the party that caused the failure.
- Lattice-based cryptography: security based on hard problems about high-dimensional grids, believed to resist quantum computers.
- MLWE / MSIS: standard lattice hardness assumptions the security proofs rely on.
- Zero-knowledge proof: a way to prove a statement is true without revealing why; prior schemes used these heavily, which is costly.
- Secret sharing: splitting a secret into pieces so only enough pieces together can reconstruct it; "ramp" and "everywhere-short" refer to specific variants where shares stay small.
- Abort key / Hint-MLWE: the paper's public per-party check values and a new variant of a hard problem used in its proof. · level: research-level

<details><summary>Original abstract</summary>

We present $\mathsf{LaTSEC}$, a three-round lattice-based threshold signature scheme with native non-interactive identifiable abort. Each party holds one small-norm signing share and is associated with one public abort key, against which its partial signature is verified directly, without zero-knowledge proofs or an additional interactive protocol. Prior lattice-based threshold signatures that identify misbehaving parties rely on one of three mechanisms: zero-knowledge proofs, an additional interactive protocol, or an everywhere-short secret sharing scheme in which each party holds multiple signing shares, each with its own public abort key. Compared with schemes that use the third mechanism, $\mathsf{LaTSEC}$ substantially reduces per-party storage. The construction uses $\mathsf{SEC}$, a recent ramp everywhere-short secret sharing scheme based on lossless expanders that gives each party a single short share. We prove correctness, identifiable-abort security, and threshold unforgeability under the standard $\mathsf{MLWE}$ and $\mathsf{MSIS}$ assumptions. The unforgeability proof introduces the Repeated-$\boldsymbol{A}$ Matrix Hint-MLWE problem, a new variant of $\mathsf{MLWE}$ with hints that captures the complete tuple of correlated public abort keys. We rigorously prove that this new variant admits a reduction from the standard $\mathsf{MLWE}$ problem. For 60 parties at 128-bit security, $\mathsf{LaTSEC}$ tolerates up to 6 corrupted parties, and, empirically, a randomly chosen set of at least 46 parties can sign with probability at least 0.99. Each party holds one signing share of about 14.3 KiB and is associated with one 24-KiB public abort key.

</details>

### [Optimal Private Gaussian Multi-sampling](https://arxiv.org/abs/2611.30146)
*Raoof Zare Moayedi, Mohammad Hossein Yassaee, Javad B. Ebrahimi* · `cs.DS` · arXiv:2611.30146v1 · relevance 0.13

- **In one sentence**: The paper gives polynomial-time algorithms for multi-sampling from a d-dimensional Gaussian with unknown mean and covariance under approximate (ε,δ)-differential privacy, needing about m + d√m/ε input samples (up to log factors) to produce m exactly independent outputs.
- **In plain words**: The paper studies how to produce many new random data points that look like they came from an unknown bell-shaped (Gaussian) distribution, while revealing only a limited amount about the private input data used to make them. Compared with running a single-output method separately for each output, the authors' approach needs far fewer input samples as the number of outputs grows: the cost scales with the square root of the number of outputs rather than linearly with the dimension times that number. The authors also argue, with lower bounds, that requiring the outputs to be exactly independent costs nothing extra beyond logarithmic factors.
- **Why it matters**: Differentially private statistics and synthetic data are used where sensitive records must be shared, so lowering the data cost of generating many private samples matters for that practice. The text only shows the sample-complexity claims and their comparison with prior single-sampler work; it does not report experiments or practical deployment, so real-world impact is unclear from this text alone.
- **Background needed**: - Differential privacy: a guarantee that an algorithm's output changes only slightly whether or not any one person's record is included; (ε,δ) is the standard strength parameter, with δ a small allowed failure probability.
- Gaussian (normal) distribution: the familiar bell-shaped distribution, described by a mean (center) and covariance (spread and correlation across dimensions).
- Dimension d: the number of numerical features per data point.
- Sample complexity: how many input data points an algorithm needs.
- Total variation distance: a measure of how different two probability distributions are; α-closeness means they are within α in this sense.
- Independence: the m outputs do not influence each other, as if each were drawn fresh from the distribution.
- Prior work: Brown, Hopkins and Smith (COLT 2023) introduced stable weighted statistics; Iverson, Kamath and Mouzakis (COLT 2025) gave a single-output Gaussian sampler. · level: research-level

<details><summary>Original abstract</summary>

We give polynomial-time algorithms for Gaussian multi-sampling under approximate $(\varepsilon,\delta)$-differential privacy, with optimal sample complexity up to logarithmic factors. Our main construction uses $\widetilde{O}(m+d\sqrt{m}/\varepsilon)$ independent input samples from a $d$-dimensional Gaussian $P$ with unknown mean and covariance to generate $m$ exactly independent outputs. Their joint distribution is $\alpha$-close in total variation to $P^{\otimes m}$. Our lower bounds hold even for dependent outputs under the same joint accuracy guarantee, showing that exact independence incurs no additional sample cost beyond logarithmic factors. The single-sampler of Iverson, Kamath, and Mouzakis [COLT 2025] uses $\widetilde{O}(d/\varepsilon)$ input samples. Running it on a separate input dataset for each of $m$ outputs therefore costs $\widetilde{O}(md/\varepsilon)$ in total. Our construction reduces this dimension-dependent sample cost from linear to square-root dependence on the number of outputs. Our approach builds on the stable weighted statistics of Brown, Hopkins, and Smith [COLT 2023], also used for Gaussian single-sampling by Iverson, Kamath, and Mouzakis. To control privacy loss when the entire batch shares these statistics, we compare the joint output densities and obtain a privacy bound that scales with the square root of the batch size. The stability step downweights influential records and can reject the entire batch. Both actions can make the outputs dependent. Our correction restores exact independence while preserving differential privacy and joint accuracy.

</details>

## Algorithms and complexity

### [Weighted Flow Time Does Not Admit Constant-Competitive Randomized Algorithms](https://arxiv.org/abs/2611.30319)
*Alexander Lindermayr* · `cs.DS` · arXiv:2611.30319v1 · relevance 0.13

- **In one sentence**: The paper proves that no randomized online algorithm for preemptive single-machine scheduling minimizing total weighted flow time is O(1)-competitive against an oblivious adversary, giving a lower bound of Ω(min{log log W, log log log min{P,D,n}}) on the competitive ratio.
- **In plain words**: This paper is about deciding how to run jobs on one machine when jobs arrive over time without warning, and the goal is to keep the total weighted waiting time low. The authors show that even randomized strategies, which make random choices, cannot stay within a fixed constant factor of the best possible schedule in the worst case. This closes the remaining open case of whether such a constant-factor guarantee exists.
- **Why it matters**: It settles a long-standing open question in online scheduling: earlier work had ruled out constant-factor guarantees only for deterministic algorithms, and this extends the negative answer to randomized ones. The result is a theoretical limit on what any online method can guarantee, so its relevance is mainly to algorithm design theory rather than to a specific application named in the text.
- **Background needed**: - Online algorithm: makes decisions without knowing future job arrivals.
- Competitive ratio: worst-case ratio between an online algorithm's cost and the best offline cost knowing everything in advance.
- Preemptive scheduling: a running job may be paused and resumed later.
- Flow time: time a job spends in the system from arrival to completion; weighted flow time multiplies each job's time by its importance weight.
- Job size, weight, and density (weight divided by size); W, P, D are ratios of largest to smallest of these quantities.
- Randomized algorithm vs. deterministic; oblivious adversary means the adversary fixes the input without seeing the algorithm's random coin flips.
- High probability: the bound holds except with very small chance.
- Big-O and Omega notation: asymptotic upper and lower bounds. · level: research-level

<details><summary>Original abstract</summary>

We study online preemptive scheduling on a single machine with the objective of minimizing the total weighted flow time. Bansal and Chan (SODA 2009) showed that no deterministic online algorithm is $O(1)$-competitive for this problem. We show that no randomized online algorithm is $O(1)$-competitive against an oblivious adversary either. This settles the remaining case of the long-standing question whether the problem admits an $O(1)$-competitive online algorithm. Quantitatively, every randomized online algorithm has a competitive ratio in $\Omega(\min\{\log\log W,\log\log\log\min\{P,D,n\}\})$, where $n$ is the number of jobs and $W$, $P$, and $D$ are the ratios of the largest to the smallest job weight, size, and density (weight divided by size), respectively. The lower bound also holds with high probability, with the same asymptotic dependence on the instance parameters. For every $\rho\ge1$ and every randomized online algorithm, there is an instance on which the cost of the algorithm is at least $\rho$ times the optimal cost with probability at least $1-2^{-2^\rho}$. Both lower bounds hold even if the algorithm knows in advance the size and weight of every job in release order and, for any fixed $\varepsilon>0$, every interarrival time up to a factor of $1+\varepsilon$.

</details>

### [A Local-to-Global Approximation Framework for Covering Disjointness-Compliable Set Families](https://arxiv.org/abs/2611.29237)
*Jingyang Zhao, Mingyu Xiao* · `cs.DS` · arXiv:2611.29237v1 · relevance 0.13

- **In one sentence**: The paper gives a local-to-global approximation framework for covering disjointness-compliable set families by edges, reducing the global problem to a local minimum-cost tree problem and yielding (1+ε)(√2+√α)²-approximations, with applications to generalized point-to-point connection and multiroot quota tree problems.
- **In plain words**: The paper studies network design: choosing the cheapest set of links so that a required collection of groups of points is covered. The authors show that if a smaller "local" version of the problem can be solved within a known factor of the best possible cost, then the full problem can be solved within a guaranteed factor of the optimum, computed in polynomial time. Applied to several specific problems, this gives solutions guaranteed to cost at most about 8 times (plus a small ε) the optimum.
- **Why it matters**: Constant-factor guarantees for these network design problems are useful benchmarks, and the abstract claims the first such results for two of the applications. The text does not show how the bounds compare with prior work beyond these claims, so the practical reach is unclear from this abstract alone.
- **Background needed**: - Approximation algorithm: a fast method that guarantees a solution within a fixed multiple of the best possible cost, rather than finding the exact optimum.
- Polynomial time: running time that grows at a manageable rate with input size.
- Spanning/Steiner tree: a set of edges linking chosen vertices without cycles; minimum-cost versions are classic network design tasks.
- Set family covering: choosing edges so that each required set of vertices is linked as the constraints demand.
- Disjointness-compliable family: a family of sets where requirements behave well when the sets do not overlap; the paper's framework relies on this property.
- Membership test: a fast check of whether a given set of vertices satisfies the family's requirement.
- Randomized approximation: an algorithm that uses random choices, with the guarantee holding in expectation or with high probability. · level: research-level

<details><summary>Original abstract</summary>

Many network design problems can be formulated as covering a family of vertex sets by edges. We develop a local-to-global approximation framework for disjointness-compliable families with polynomial-time membership tests. A class of vertices is deficient if it belongs to the family and feasible otherwise. Our local problem seeks a minimum-cost tree that connects one deficient class to feasible classes so that their union is feasible. If this local problem admits a polynomial-time $\alpha$-approximation, then the covering problem admits a polynomial-time $(1+\varepsilon)(\sqrt{2}+\sqrt{\alpha})^2$-approximation for every fixed $\varepsilon>0$. Our algorithm first connects deficient vertices that are difficult to separate and then handles regions containing one deficient class at a time. To bound the total local cost, we compare the local trees with a feasible forest. We delete edges of this forest after using them in the bound, so each is counted at most once even when regions overlap. As applications, we obtain polynomial-time $(8+\varepsilon)$-approximation algorithms for generalized point-to-point connection and multiroot quota tree, including multiroot $k$-minimum spanning tree. To the best of our knowledge, these are the first polynomial-time constant-factor approximations for both problems. We also obtain a randomized approximation for multiroot covering Steiner that has the same asymptotic ratio as the known approximation for its single-root version.

</details>

## Programming languages and formal methods

### [Landscape and Taxonomy of Prompt Engineering Patterns in Software Engineering](https://arxiv.org/abs/2611.29853)
*Yuya Sasaki, Hironori Washizaki, Jialong Li et al.* · `cs.SE` · arXiv:2611.29853v1 · relevance 0.13

- **In one sentence**: A taxonomy of prompt engineering patterns for software engineering, derived from a systematic literature review conducted in early 2023.
- **In plain words**: Large language models are AI systems that write text in response to instructions, called prompts. This paper sorts the recurring ways people word those prompts to get useful results for software tasks, and builds a classification of these approaches. The classification is based on a review of existing published studies gathered in early 2023, when these models still had tight limits on how much text they could read at once.
- **Why it matters**: Prompt wording strongly affects how useful AI tools are for developers, so a shared catalogue of patterns can help practitioners and researchers. The text does not report specific results or how well each pattern performs, so its practical impact is hard to judge from this summary alone.
- **Background needed**: - Large language model (LLM): an AI system trained on large amounts of text that generates responses to written input.
- Prompt: the instruction or question given to the model.
- Prompt pattern: a reusable way of structuring a prompt to get a reliable result, similar to a recipe.
- Systematic literature review: a structured search and summary of published research on a topic.
- Context length: how much text a model can take in at once.
- Software engineering: the work of designing, building, and maintaining software. · level: intermediate

<details><summary>Original abstract</summary>

Advancements in large language models (LLMs) have enhanced their ability to handle ambiguous user instructions. However, effective prompt patterns remain crucial for usability and comprehension. This article presents a taxonomy of prompt engineering patterns for software engineering. It is based on a systematic literature review that was conducted in early 2023, when LLMs still faced significant limitations in context length and inference capabilities. Our study explores techniques that enhance the usability and reliability of LLMs, emphasizing the ongoing importance of well-designed prompts in optimizing task performance. Our findings highlight the critical role of prompt patterns in maximizing LLM's potential, even as their capabilities continue to evolve.

</details>

### [Sheaf Semantics of Probabilistic Programs](https://arxiv.org/abs/2611.30692)
*Shing Hin Ho, Nicolas Wu, Azalea Raad* · `cs.LO` · arXiv:2611.30692v1 · relevance 0.13

- **In one sentence**: The paper gives a monadic denotational semantics, built on Simpson's probability sheaves and the internal logic of atomic sheaves, for higher-order probabilistic programs with continuous distributions, proves it is a model of the ν-calculus, and derives a higher-order probabilistic Hoare logic that handles continuous random variables, higher-order functions and independence.
- **In plain words**: The paper is about how to give a precise mathematical meaning to computer programs that make random choices from continuous distributions (such as a value drawn from a bell curve), including programs whose functions can take other functions as inputs. The authors build such a meaning using a mathematical framework called sheaves and then use it to set up a logic for proving properties of these programs, such as what distribution their outputs follow and whether outputs are independent of each other. The text presents this as a set of proofs and a derived proof system rather than experiments.
- **Why it matters**: Reasoning formally about randomized programs with continuous values is hard, and most existing tools handle only discrete randomness or first-order programs, so an approach that covers higher-order functions and independence addresses a real gap. The connection is to verification of probabilistic software and to the mathematical foundations of statistics-driven code; the text does not say how practical the logic is, so its impact on real tools is uncertain.
- **Background needed**: - Probabilistic programs: programs that draw random values, here from continuous distributions (real-valued, not just coin flips).
- Denotational semantics: assigning each program a mathematical object that captures its meaning.
- Measure theory: the branch of mathematics that makes probabilities over real numbers rigorous.
- Monad: a standard way in programming theory to package effects such as randomness into a composable structure.
- Sheaf and topos: advanced category-theory structures that organize local information consistently; the paper uses their internal logic.
- Hoare logic: a proof system that reasons about programs using pre- and post-conditions.
- Probabilistic (in)dependence: whether knowing one random output tells you anything about another. · level: research-level

<details><summary>Original abstract</summary>

Finding denotational models of probabilistic languages that support sampling from continuous distributions is difficult: the existence of continuous distributions means that measure-theoretic objects are needed to define the semantics. A challenging task on top of this is logical reasoning with respect to the semantic model: in the case of probabilistic programs, the desired properties to reason about include the distributions, expected value and the probabilistic (in)dependence of outputs. This paper introduces a monadic semantics for higher-order probabilistic programs with continuous distributions based on Simpson's theory of probability sheaves and the internal logic of atomic sheaves. We prove that our semantics forms a model of the $\nu$-calculus. Furthermore, using the well-behavedness of the semantic domain and the internal logic of the topos, we derive the first higher-order probabilistic Hoare logic with rigorous treatment of continuous random variables, higher-order functions, and independence.

</details>

## Systems and networking

### [Zarc: Exact Nearest Neighbors over a Billion Vectors in Seconds](https://arxiv.org/abs/2611.29252)
*Dongfang Zhao* · `cs.DC` · arXiv:2611.29252v1 · relevance 0.06

- **In one sentence**: Zarc is a multi-GPU system that gives exact k-nearest-neighbor vector search over a billion vectors by keeping compact half-precision lower-bound rows on the GPU and fetching only the few surviving full vectors from host memory.
- **In plain words**: The paper is about finding the closest matches to a query among a huge collection of numerical "fingerprints" (vectors), such as the data behind AI models' attention mechanisms. Searching every item for every query is slow, and fast shortcut methods are often approximate or need one GPU to hold everything. The authors report a system that keeps small summary rows on the GPUs, skips nearly all items cheaply, and reads only the few remaining full items from main memory, so answers stay exact.
- **Why it matters**: Exact search at this scale matters for LLM attention and large data-cleaning jobs, where approximate answers can silently change results. The reported speedups (for example 10,000 queries over a billion vectors in 1.1 seconds on four H100 GPUs, versus about five minutes) are the authors' own measurements, and the text does not show how they hold up on other hardware or workloads.
- **Background needed**: - Vector search: finding the stored vectors most similar to a query vector, often by Euclidean distance, cosine similarity, or inner product.
- k-nearest neighbors (k-NN): returning the k closest stored items; "exact" means no true neighbor is missed.
- Approximate vs exact search: approximate indexes trade some accuracy for speed.
- Attention in LLMs: a model step that weighs past tokens by relevance; sparse attention only looks at a few top-scoring keys.
- GPU and host memory: GPU memory is fast but small; host (CPU-side) memory is larger but slower to read.
- Half precision (bf16/fp16): storing numbers with fewer bits to save memory and time.
- Lower-bound "proofs": cheap estimates guaranteeing a vector is too far away to be a top match, so it can be skipped. · level: research-level

<details><summary>Original abstract</summary>

Exact k-nearest-neighbor vector search lies on the critical path of machine learning systems, from sparse attention in the latest large language models (LLMs) to long-context memories and training-data deduplication. Exhaustive GPU search scans the whole dataset for every query, while approximate indexes return inexact neighbors. Recent methods skip almost every vector with a cheap half-precision proof that it lies too far away, but only on one GPU that holds the whole dataset. Our insight is to keep only the short rows of these proofs in GPU memory and to fetch the few remaining full vectors from host memory. Our system, Zarc, answers Euclidean, cosine, inner-product, and filtered queries exactly under updates. On four H100 GPUs, it answers 10,000 exact queries over one billion vectors in 1.1 seconds instead of five minutes. On eleven open LLMs, it retrieves the exact top-10 attention keys 2.2x to 13.1x faster than exhaustive search. In sparse attention over one million tokens, it runs 3.1x faster than bf16 selection with FlashInfer, which misses the exact top-64 for most queries.

</details>

### [Torcalia.jl: An MPI-based Runtime System for Asynchronous Task Parallelism in Julia](https://arxiv.org/abs/2611.30776)
*Argiris Sofotasios, Dimitris Metaxakis, Chrysostomos Stylios et al.* · `cs.DC` · arXiv:2611.30776v1 · relevance 0.06

- **In one sentence**: Torcalia.jl is a Julia package that runs dependency-aware asynchronous tasks across both multithreaded and multi-node MPI clusters, using work-sharing and work-stealing scheduling plus application-level distributed shared memory, and reports up to 18.1% lower wall-clock time than the Dagger engine on four workloads on the ARIS supercomputer.
- **In plain words**: Scientific programs often split work into many small pieces that finish at uneven times, which wastes computers that sit idle waiting for others. This paper presents Torcalia, a software library for the Julia programming language that schedules these small pieces of work automatically, both within one machine and across many machines in a supercomputer. On four test workloads run on the ARIS supercomputer, the authors report up to 18.1% less run time than Dagger, another Julia task system.
- **Why it matters**: Efficient scheduling of irregular workloads matters for scientific computing that must scale to large clusters, and the paper gives a concrete comparison against an existing Julia tool. The reported gain is measured on a specific set of four workloads and one machine, so it shows promise rather than a general improvement; the source code is public, which allows independent checking.
- **Background needed**: - Julia: a programming language popular for scientific and numerical computing.
- Parallel computing: running many computations at once on several processors or machines.
- Bulk-synchronous (BSP) model: a style where all workers proceed in lockstep through phases, which can waste time when work is uneven.
- Asynchronous many-task (AMT) runtime: a system that breaks a program into many small tasks and schedules them dynamically as resources free up.
- Work-stealing: idle processors take waiting tasks from busy ones to balance load.
- MPI: a standard message-passing library that lets computers in a cluster communicate.
- Distributed shared memory (DSM): a layer that makes memory spread across machines look like one shared memory to programs.
- Wall-clock time: the real elapsed time a program takes to finish. · level: research-level

<details><summary>Original abstract</summary>

Designed to address the two-language problem, the Julia programming language provides a powerful platform for developing high-performance scientific computing and machine learning applications. Such applications increasingly exhibit irregular, adaptive, or data-driven workloads for which traditional bulk-synchronous parallel (BSP) models often struggle to efficiently exploit the available parallelism. Asynchronous many-task (AMT) runtime systems offer a compelling alternative, decomposing computations into fine-grained tasks that are dynamically scheduled across the hierarchical architecture of modern HPC systems. This paper introduces Torcalia$.$jl, a Julia package designed to orchestrate the asynchronous execution of tasks across both shared and distributed memory environments. Built on top of MPI$.$jl and Julia's native multithreading, Torcalia employs a dependency-aware task scheduling scheme that combines the work-sharing and work-stealing paradigms to achieve adaptive load balancing. Tasks can be nested arbitrarily, enabling applications to exploit multiple levels of parallelism, while application-level distributed shared memory (DSM) extends task-based shared-memory programming to multi-node clusters. Beyond task-based programming, the proposed library supports skeletal programming, providing high-level abstractions that facilitate the implementation of parallel applications at scale. Evaluated on the ARIS supercomputer using four diverse workloads, Torcalia demonstrates strong scalability, reducing wall-clock time by up to 18.1% compared with Dagger, a state-of-the-art task-based engine in Julia. The source code of Torcalia$.$jl is publicly available at https://github.com/CEID-HPCLAB/Torcalia.jl.

</details>

## Human-computer interaction

### [The Agent Is Not Your Driver: Clarifying the Implied Capabilities of In-Vehicle Anthropomorphic Agents](https://arxiv.org/abs/2611.28007)
*Benjamin Hardin* · `cs.HC` · arXiv:2611.28007v1 · relevance 0.11

- **In one sentence**: A position paper arguing that anthropomorphic in-vehicle agents can imply driving knowledge and control they do not have, and proposing a research agenda on the resulting psychological risks of dependence and betrayal.
- **In plain words**: Some cars now include talking, human-like assistants that sit in the dashboard or voice system. This paper is concerned that such an assistant may suggest it is part of the car's self-driving system when it is not, which could lead passengers to trust it too much. The paper does not report experiments; it proposes questions and a research plan for studying this gap and narrowing it in a way that supports safety.
- **Why it matters**: As cars take on more automated driving and their voice assistants become more human-like, a mismatch between what an assistant appears to know and what it actually controls could affect how safely people rely on it. The text does not provide evidence of how common this problem is today, so its scale is uncertain.
- **Background needed**: - Autonomous vehicle: a car whose driving system can steer, brake, and monitor the road with varying levels of human involvement.
- Automated driving system: the software and sensors that actually control the vehicle, as distinct from other systems in the car.
- Anthropomorphic agent: a voice or on-screen assistant designed to seem human-like, with a name, personality, or conversational manner.
- Implied capability: what a user is led to believe a system can do, which may differ from what it really can do.
- Dependence and betrayal: over-reliance on a system, and the sense of being misled when it fails to deliver what it seemed to promise.
- Position paper: an argument and agenda rather than a report of new experimental results. · level: intermediate

<details><summary>Original abstract</summary>

This position paper considers how the gap between an anthropomorphic agent in an autonomous vehicle and the automated driving system of the vehicle can create psychological risks if the agent inaccurately presents itself as integrated into the driving system. This gap is under-explored both because of the evolving nature of these agents and because of study limitations in Human-Computer Interaction (HCI) research. Nevertheless, this gap may cause the agent to misrepresent itself as more knowledgeable about the car than it is, creating a risk of dependence and, in the worst case, betrayal if the occupant feels that the agent has misled them. This paper proposes a research agenda for future work to understand the psychological risk that exists in the gap between agents and driving systems and to narrow this gap in a manner aligned with safety assurance. As these agents evolve to hold greater capabilities and increased anthropomorphism, future research must investigate risks which may emerge from richer interaction with them. The impact of how an agent presents itself and its knowledge becomes greater.

</details>

### [Typing Behavior in Human-LLM Interaction: Keystroke Dynamics Reveal Cognitive Effort During Prompting](https://arxiv.org/abs/2606.28090)
*Laura Sch\"utz, Yousri Cherif, Clara Sayffaerth et al.* · `cs.HC` · arXiv:2606.28090v1 · relevance 0.11

- **In one sentence**: A 36-person user study finds that keystroke timing and volume track self-reported mental workload when prompting an LLM under easy versus hard tasks and desktop versus mobile devices, but do not predict how useful users rate the output.
- **In plain words**: People typing questions to AI chatbots may reveal how hard they are thinking through how they type: harder tasks led to more keystrokes, slower typing, and longer pauses. The study had 36 participants work on easy and hard tasks on a computer or a phone, and the typing patterns matched how much effort they reported. However, the typing patterns did not tell the researchers whether people found the AI's answers useful.
- **Why it matters**: Typing signals could offer a cheap, real-time way for software to notice when a user is struggling, without asking them questions. The limit found here, that typing does not capture perceived usefulness, suggests such signals would be a partial picture of how well human-AI collaboration is going.
- **Background needed**: - Keystroke dynamics: measuring how a person types, such as how many keys they press, how fast, and how long they pause between keys.
- Human-computer interaction (HCI): the field that studies how people use and experience computers and software.
- Large Language Model (LLM): an AI system that generates text in response to written prompts, such as a chatbot.
- Prompting: writing the input or question given to an AI system.
- NASA-TLX: a standard questionnaire where people rate their mental workload, such as mental demand, effort, and frustration.
- Cognitive effort: the amount of mental work a task requires.
- The text is a short abstract only; it gives no detail on exact measures, statistics, or task design. · level: introductory

<details><summary>Original abstract</summary>

As Large Language Models (LLMs) become increasingly integrated into daily routines, understanding how users interact with these systems is crucial for effective human-AI collaboration. This work investigates keystroke dynamics as a behavioral measure of user mental effort and perceived output usefulness in human-LLM interaction. We conducted a user study (N = 36) to examine how task difficulty (easy vs. hard) and device type (desktop vs. mobile) influence typing behavior and workload (NASA-TLX) during interactions. Our results indicate that hard tasks led to significantly more keystrokes, slower typing, increased pauses, and higher self-reported workload. Device type had weaker effects, with mobile use slightly reducing input length and typing speed. While keystrokes captured differences in cognitive effort, they did not predict perceived LLM output usefulness. These findings highlight the potential of keystroke dynamics as real-time indicators of cognitive effort during LLM prompting, while also showing their limitations in capturing perceived collaboration success.

</details>

## Information theory

### [An Alphabet-Size Bound for the Information Bottleneck Function](https://arxiv.org/abs/2611.30697)
*Christoph Hirche, Andreas Winter* · `cs.IT` · arXiv:2611.30697v1 · relevance 0.09

- **In one sentence**: The paper shows that the information bottleneck function can be approximated with a compressed variable W whose alphabet size is bounded by a function of the approximation error and |Y| alone, rather than |X|, and extends such cardinality bounds to settings with quantum variables.
- **In plain words**: The paper is about how to compress a large piece of data while keeping the parts that matter for predicting a small set of labels. The known method needs a summary variable with at most one more value than the size of the original data set, which is impractical when that data set is huge. The authors show that an approximate answer is possible with a summary size that depends only on the number of labels and the allowed error, and they also extend the result to quantum information.
- **Why it matters**: Machine learning tasks often have huge input spaces and small label sets, so a bound that depends on the label count could make these calculations feasible. The text does not report any applications or numerical tests, so its practical impact is unclear from the abstract alone.
- **Background needed**: - Random variable: a quantity whose value is uncertain, described by a probability distribution.
- Mutual information: a measure of how much knowing one variable tells you about another.
- Information bottleneck: finding a compressed summary W of X that keeps as much information about Y as possible, subject to a limit on how much of X it retains.
- Cardinality (alphabet size): the number of distinct values a variable can take.
- Approximation error: how far the approximate answer may deviate from the exact optimum.
- Quantum information: information carried by quantum systems, where variables may not behave like classical ones. · level: research-level

<details><summary>Original abstract</summary>

The information bottleneck function gives a measure of optimal preservation of correlation between some random variable $X$ and some side information $Y$ while compressing $X$ into a new random variable $W$ with bounded remaining correlation to $X$. As such, the information bottleneck has found many natural applications in machine learning, coding and video compression. The main objective in order to calculate the information bottleneck is to find the optimal representation on $W$. This could in principle be arbitrarily complicated, but fortunately it is known that the cardinality of $W$ can be restricted as $|{\cal W}|\leq|{\cal X}|+1$ which makes the calculation possible for finite $|{\cal X}|$. Now, for many practical applications, e.g. in machine learning, $X$ represents a potentially very large data space, while $Y$ is from a comparably small set of labels. This raises the question whether the known cardinality bound can be improved in such situations. We show that the information bottleneck function can always be approximated up to an error $\delta(\epsilon,|{\cal Y}|)$ with a cardinality $|{\cal W}| \leq f(\epsilon,|{\cal Y}|)$, for explicitly given functions $\delta$ and $f$ of an approximation parameter $\epsilon>0$ and the cardinality of ${\cal Y}$. Finally, we generalize the known cardinality bounds to the case were some of the random variables represent quantum information.

</details>

### [Following the Error Through a Compressed Network:An Angular Measure for FFN Weight Compression in ViT-L/16](https://arxiv.org/abs/2611.28067)
*Paolo D'Alberto* · `cs.CV` · arXiv:2611.28067v1 · relevance 0.08

- **In one sentence**: The paper compares four ways of quantizing the feed-forward weight matrices of ViT-L/16 to 2–8 bits and proposes an angular error measure, followed through the blocks, that ranks the schemes like the final classifier does.
- **In plain words**: Large image-recognition networks store their learned settings as very precise numbers, which takes a lot of memory. This paper studies how to round those numbers to much coarser levels (down to 2–8 bits) in one model, ViT-L/16, and how the rounding errors build up as they pass through the network. At 4 bits, all four rounding schemes stay within 0.8 points of the original accuracy on 50,000 images, but they differ in how often they agree with the original predictions (98.4% down to 94.4%).
- **Why it matters**: The authors show that the final accuracy alone can hide differences between compression schemes, and that tracking the angle of the error through the layers reveals where the ranking comes from. The measures are described as portable to other models and precisions, but the study covers one model, FFN weights only, and does not claim any speed-up, so the wider relevance is not yet shown.
- **Background needed**: - Quantization: storing model weights with fewer bits, trading precision for memory.
- Feed-forward network (FFN): the per-block two-layer sub-network inside a transformer.
- Vision Transformer (ViT-L/16): a large image classifier that splits images into 16x16 patches and passes them through stacked blocks.
- Residual stream: the running signal that each block adds its output to; errors here carry from block to block.
- Lloyd–Max table: a fixed set of optimal rounding levels for a bell-shaped (Gaussian) distribution of values.
- Hadamard rotation: a mixing transform that spreads out large values before rounding; here it is random-sign.
- Angular error: the angle between the compressed and original signal vectors, a scale-free way to measure how far they point apart.
- Float32 evaluation: the compressed weights are simulated in normal floating-point arithmetic, so no real speed or memory gain is measured. · level: research-level

<details><summary>Original abstract</summary>

We study the compression of the 48 feed-forward network (FFN) matrices of the Vision Transformer ViT-L/16 to 2--8 bits with four schemes: a per-token grid, a fixed Gaussian Lloyd--Max table, a table fitted to the matrix, and a random-sign Hadamard rotation followed by the fixed table. We evaluate on 50,000 images. At 4 bits the top-1 accuracy of the four schemes lies within 0.8 points of the float32 model, while the agreement with its predictions ranges from 98.4\% to 94.4\%. We use the angular error between the compressed and the float32 residual stream, followed through the blocks, as a portable measure that ranks the schemes as the final classification does and shows where the ranking is built: with rotation the angle grows close to the square root of the number of blocks, the signature of independently accumulating errors, while the other schemes are amplified in the later blocks. The same measure shows that a scheme that is better on one block in isolation can be worse in the whole network. To address this inconsistency we introduce an angular measure of the spectrum of the output of a block, which in isolation orders the schemes as the whole network does where they diverge most. We support these observations with real samples and with statistically generated ones. The scope is one model, the FFN weights only, and float evaluation of compressed weights; no speed-up is claimed. The error measures and the sample generation, however, can be applied to other models and precisions.

</details>

## High-energy theory and gravity

### [Scattering amplitudes in AdS$_5\times$ S$^5$ from the pure spinor superstring](https://arxiv.org/abs/2611.29622)
*Luis F. Alday, Thiago Fleury, Tobias Hansen et al.* · `hep-th` · arXiv:2611.29622v1 · relevance 0.16

- **In one sentence**: The paper gives a BRST-invariant rule for integrating over zero modes in the pure spinor superstring on AdS5×S5, valid for genus-zero amplitudes, and uses it to compute two- and three-point supergravity amplitudes that match planar N=4 super Yang-Mills.
- **In plain words**: The paper concerns a string-theory model of particles living on a curved, five-dimensional anti-de Sitter space times a five-sphere, the background linked to a well-known gauge-theory duality. The authors fix a long-standing technical problem: how to add up the "zero mode" directions of the string's worldsheet consistently. With that fix, they directly compute how simple particle interactions (two- and three-point amplitudes) come out of the string description.
- **Why it matters**: Scattering amplitudes are the basic predictions of a quantum theory, so having a working worldsheet method in this background is a prerequisite for computing more of them. The reported check is that the three-point results agree with planar N=4 super Yang-Mills, which is the gauge theory the duality relates to this background; the text does not go beyond that comparison.
- **Background needed**: - Scattering amplitude: a quantity giving the probability-like strength of particles colliding and producing other particles.
- Worldsheet: the two-dimensional surface a string sweeps out through spacetime; string amplitudes are integrals over it.
- Pure spinor superstring: a particular formulation of superstring theory with built-in supersymmetry, used here to handle the curved background.
- Zero modes: directions of the worldsheet integral that do not change the field configuration and must be integrated separately.
- BRST invariance: a symmetry used to remove unphysical (gauge) degrees of freedom consistently.
- Picture changing operators: bookkeeping devices needed to deal with fermionic fields in superstring calculations.
- Genus zero, planar: the simplest topology of the worldsheet and the leading-order limit of the gauge theory.
- AdS5×S5 / N=4 super Yang-Mills: the pair of theories linked by the AdS/CFT correspondence, a flagship example of a gravity–gauge theory duality. · level: research-level

<details><summary>Original abstract</summary>

We formulate a BRST-invariant prescription for the integration of zero modes in the pure spinor superstring on $AdS_5\times S^5$. The measure includes contributions absent in flat space and admits a description in terms of picture changing operators or a non-minimal regulator. The prescription is valid for genus-zero amplitudes with arbitrary multiplicity and external states and removes a central obstacle to amplitude computations in this background. We use it to perform the first direct worldsheet computation of two and three-point amplitudes of half-BPS supergravity states. The properly normalised three-point amplitudes exactly reproduce the results of planar ${\mathcal N}=4$ super Yang-Mills theory.

</details>

### [Primordial black holes production in Einstein-Gauss-Bonnet gravity](https://arxiv.org/abs/2611.28150)
*Ekaterina O. Pozdeeva, Sergey Yu. Vernov* · `gr-qc` · arXiv:2611.28150v1 · relevance 0.15

- **In one sentence**: Proposes an inflation model in Einstein-Gauss-Bonnet gravity, where the Gauss-Bonnet term is coupled to a function of the scalar field, that may generate primordial black holes and agree with ACT data for some parameter values.
- **In plain words**: The paper looks at a theory of the early universe, in the first instants after the Big Bang, when space expanded very rapidly (inflation). The authors propose a new version of that model in which a mathematical term from gravity theory is tied to a field that drives the expansion. They report that for certain parameter choices the predictions match data from the Atacama Cosmology Telescope, and they suggest the resulting small black holes could make up all or part of dark matter.
- **Why it matters**: If primordial black holes formed in the early universe, they could be a candidate for some or all of dark matter, which is still unidentified. The work connects inflation, cosmological observations and dark matter, but the text gives only a brief abstract, so the strength of the claims cannot be judged from it alone.
- **Background needed**: - Inflation: a brief period of extremely rapid expansion of the early universe, usually driven by a scalar field (a field with a single value at each point in space).
- Primordial black holes (PBHs): black holes that could have formed in the early universe from density fluctuations, not from collapsed stars.
- Gauss-Bonnet term: a specific combination of spacetime curvature terms in gravity theory that goes beyond standard General Relativity.
- Einstein-Gauss-Bonnet gravity: General Relativity extended with this term.
- ACT (Atacama Cosmology Telescope): a ground telescope whose measurements of the cosmic microwave background constrain inflation models.
- Dark matter: unseen matter inferred from its gravitational effects on galaxies and large-scale structure.
- The abstract gives no equations, specific parameter values, or PBH mass numbers, so the details must be checked in the full paper. · level: research-level

<details><summary>Original abstract</summary>

We consider models with the Gauss-Bonnet term multiplied to a function of the scalar field and propose a new inflationary model which provides a mechanism for the formation of primordial black holes (PBHs). For certain values of the model parameters, the predictions of this model agree with observational data from the Atacama Cosmology Telescope (ACT). Due to estimation of possiable PBHs masses, we demonstrate that they can be considered as a possible source for all or part of dark matter.

</details>

## Statistical physics

### [Statistical mechanics of linear classification on hierarchical tree data](https://arxiv.org/abs/2611.28824)
*Jerome Garnier-Brun, Federica Kulka, Carlo Lucibello* · `cond-mat.dis-nn` · arXiv:2611.28824v1 · relevance 0.15

- **In one sentence**: A replica-theory analysis of a linear classifier trained to recover the root of a broadcast process on a tree from its leaves, showing a two-stage double descent whose stages are separated in sample-size scale when broadcast noise is below the reconstruction threshold.
- **In plain words**: The paper studies a simple learning problem: a tree-shaped chain of noisy copying, where a hidden root value spreads down to many leaves, and a linear classifier must guess the root from the leaves. The authors find that the data are not Gaussian (bell-curve-like) along the direction that carries the label, and that finite-size effects matter. They keep the exact statistics along that label direction, treat the other fluctuations as Gaussian, and build a theory that they report matches measured learning curves.
- **Why it matters**: It offers a controlled, solvable toy model for how learning systems exploit hierarchical structure, which the abstract suggests could be a starting point for studying deeper networks and generative models. Its broader relevance is stated only as a possibility by the authors, not demonstrated here.
- **Background needed**: - Linear classifier: a rule that weighs each input feature and sums them to pick a label.
- Learning curve: how test error changes as the number of training samples grows.
- Double descent: error first falls, rises to a peak (often near the point where samples match parameters), then falls again.
- Broadcast process on a tree: a root value is copied down branches with random flips; leaves are observed.
- Reconstruction threshold: the noise level above which the root can no longer be inferred from the leaves better than chance.
- Replica method: a statistical-physics technique for averaging over random datasets to predict typical performance.
- Gaussian equivalence: approximating complex data by a Gaussian with matching mean and covariance. · level: research-level

<details><summary>Original abstract</summary>

Deep networks owe much of their success to their ability to exploit the structure in data, from the grammar of language to the multi-scale organization of images. Yet, many statistical mechanics approaches to structured data rely on Gaussian equivalence, whose assumptions can fail when a few latent variables influence all input coordinates. In this work, we take a step beyond this setting with a simple setup, in which a linear classifier is trained to infer the root of the classical broadcast process on a tree from its $N$ leaves. Despite this simplicity, the data already display non-Gaussian statistics along the direction carrying the label, as well as strong finite-size effects. By retaining the exact law along this direction and approximating the transverse fluctuations as Gaussian, we obtain a finite-depth replica theory that accurately describes the measured learning curves. At large depth and sufficiently weak regularization, we uncover a double descent whose two stages are separated in scale. In a range of broadcast noise below the reconstruction threshold, the first descent occurs at a number of samples scaling as $N^\omega$, with $0<\omega<1$ set by the data statistics, whereas the overfitting peak occurs at order $N$ samples. Beyond linear classifiers, this setup could serve as a controlled starting point to study deeper architectures and generative models on hierarchical data.

</details>

### [A Novel Algebraic Approach to Medium-Range Solvable Models](https://arxiv.org/abs/2611.29351)
*Yuan Miao, Kohei Fukai* · `math-ph` · arXiv:2611.29351v1 · relevance 0.13

- **In one sentence**: The paper extends Jones' algebraic Baxterisation to quantum spin chains with medium-range interactions, using an extended Yang-Baxter equation built from the chromatic algebra of 3-colouring, and yields four representations that reproduce known models and give new ones.
- **In plain words**: The paper studies chains of interacting quantum spins, the kind used as simple models of magnets and other many-body materials, where each spin interacts not just with its immediate neighbour but with a few more distant ones. The authors give a general algebraic recipe for building such chains that can be solved exactly, and they apply it to build four specific versions. Two of these reproduce models already known in the literature, and two are new, one describing a three-state antiferromagnet and one a Rydberg-blockade ladder.
- **Why it matters**: Exactly solvable models are rare and valuable because they give precise answers that can test approximate methods and reveal general behaviour. The text reports that two of the new models have non-invertible symmetries, a less common kind of symmetry; the text does not say more about what this implies for physical behaviour.
- **Background needed**: - Quantum spin chain: a row of tiny quantum magnets (spins) coupled to their neighbours; its Hamiltonian is the energy operator governing it.
- Medium-range interaction: spins interact beyond nearest neighbours, not just with the adjacent site.
- Yang-Baxter equation: a consistency condition on matrices that guarantees a model is exactly solvable (integrable).
- Transfer matrix and involution: a family of commuting operators generated from the model; commuting means they share eigenstates, which is the hallmark of integrability.
- Lax operator: the building block from which transfer matrices are constructed.
- Algebra generators and representations: abstract rules for operators; a representation is a concrete realisation of those rules on a space of states.
- Chromatic algebra / 3-colouring: an algebra arising from counting colourings of graphs with three colours; related to the fusion category Rep(S3).
- Non-invertible symmetry: a generalised symmetry whose operators cannot be undone by an inverse, a recent topic in condensed matter and high-energy physics.
- Folded XXZ and hard-rod deformed XXZ: known integrable spin-chain models that the construction recovers. · level: research-level

<details><summary>Original abstract</summary>

We extend Jones' Baxterisation, which produces solutions to the Yang-Baxter equation directly from the generators of an algebra, to quantum spin chains with medium-range interactions. The key ingredient is an extended Yang-Baxter equation for R matrices that are built from the generators attached to two neighbouring sites. Together with the accompanying Lax operator, it gives rise to transfer matrices that are in involution up to boundary terms, exactly as in Jones' construction. We find a solution to the extended Yang-Baxter equation, of non-difference form, in terms of the generators of the chromatic algebra of 3-colouring, and obtain from it two families of medium-range lattice Hamiltonians. Thus, each representation of the algebra provides a medium-range solvable model. Using the relation between the chromatic algebra of 3-colouring and the fusion category $\mathrm{Rep}(S_3)$, we construct four such representations. They reproduce the folded XXZ model and the hard-rod deformed XXZ model, and give new medium-range models of a three-state antiferromagnet and of a Rydberg-blockade ladder. Two of the four models possess non-invertible symmetries.

</details>

## Condensed matter

### [Anomalous Field-induced Coherence beyond Single-ion Kondo Physics](https://arxiv.org/abs/2611.31137)
*Arushi, Konstantin Semeniuk, Manuel Brando et al.* · `cond-mat.str-el` · arXiv:2611.31137v1 · relevance 0.14

- **In one sentence**: In the Ce-based heavy fermion Ce2Rh3Ga5, a magnetic field produces large negative magnetoresistance and restores T^2 coherent transport, a behavior the authors say cannot be explained by single-ion Kondo physics alone and resembles the anomalous magnetotransport of UBe13.
- **In plain words**: Some metals made of rare-earth elements carry heavy electrons that usually conduct electricity more easily as they get colder. This paper studies Ce2Rh3Ga5, a material whose electrical resistance stays high at very low temperatures, and reports that a magnetic field lowers that resistance and makes the material behave like a well-ordered metal again. The authors conclude that a simple single-atom model does not account for the drop, which points to an extra source of electron scattering.
- **Why it matters**: The result matters because it offers a new, clean material in which electron scattering and coherent transport can be studied in a heavy fermion system without superconductivity, which complicates the older UBe13 case. The text does not establish the microscopic origin of the extra scattering, so its broader significance is still to be tested.
- **Background needed**: - Heavy fermions: metals whose electrons behave as if they are many times heavier than normal, usually arising from interactions with localized magnetic atoms (here cerium).
- Kondo effect: a localized magnetic atom gets screened by conduction electrons; the single-ion version describes one such atom at a time.
- Coherence: when scattering weakens and electrons act collectively, resistivity typically drops at low temperature.
- Resistivity and magnetoresistance: resistance to electric current, and how much it changes with a magnetic field.
- Specific heat coefficient C/T: a measure of how many low-energy thermal states the electrons have; large values signal heavy quasiparticles.
- T^2 resistivity: resistance that grows with the square of temperature, a signature of coherent metallic behavior.
- UBe13: a uranium heavy fermion compound with long-standing puzzles in its transport, which the paper uses as a comparison. · level: research-level

<details><summary>Original abstract</summary>

The emergence of coherent heavy quasiparticles in Kondo lattices is generally accompanied by a reduction in electrical resistivity at low temperatures. However, certain strongly correlated metals exhibit anomalously large resistivities that persist to very low temperatures, raising fundamental questions about the mechanisms governing charge transport. Here, we report an unusual magnetic field-induced evolution of electronic transport and thermodynamic properties in a Ce-based heavy fermion compound, Ce$_{2}$Rh$_{3}$Ga$_{5}$. At zero field, Ce$_{2}$Rh$_{3}$Ga$_{5}$ undergoes a magnetic transition at $T$$_{0}$ = 0.45 K and exhibits a strongly enhanced low temperature specific heat coefficient, reaching $C$/$T$ = 2.2 J/mol$_{Ce}$-K$^{2}$, but no discernible coherence in its electrical resistivity. Remarkably, applying a magnetic field produces a large negative magnetoresistance and restores coherent metallic behavior, characterized by low-temperature $T$$^2$ resistivity. Although the field dependence of the electronic specific heat coefficient can be described phenomenologically within a single-ion Kondo framework, the same description fails to account for the strong suppression of the residual resistivity and the overall magnetoresistance. These results point to an additional field-sensitive scattering contribution beyond conventional single-ion Kondo physics. The striking resemblance to the long-standing anomalous magnetotransport behavior of UBe$_{13}$, without the complications introduced by superconductivity, establishes Ce$_{2}$Rh$_{3}$Ga$_{5}$ as a platform for investigating the microscopic origin of anomalous scattering and field-induced coherent transport in strongly correlated electron systems.

</details>

### [Perfect Spin-to-Charge Signal Conversion via Inverse Spin Hall Effect in a Superconductor](https://arxiv.org/abs/2611.30781)
*Rodrigo de las Heras, Ilya V. Tokatly, F. Sebastian Bergeret* · `cond-mat.supr-con` · arXiv:2611.30781v1 · relevance 0.13

- **In one sentence**: A theoretical proposal that, in a superconductor, the quasiparticle charge imbalance created by injected spin accumulation can convert spin into a charge voltage near unity efficiency via the inverse spin Hall effect, despite a small spin Hall angle, with finite broadening and temperature effects included.
- **In plain words**: Spintronics devices often turn spin (a quantum magnetic property of electrons) into an electrical voltage, but the usual materials convert only a small fraction of it. This paper argues that running the process through a superconductor, a material that carries current without resistance below a critical temperature, could make the voltage almost as large as the injected spin signal. The authors derive the full theory of this effect for a standard test geometry and suggest experiments that vary temperature and spin bias to check it.
- **Why it matters**: If confirmed, a near-complete spin-to-charge conversion would be a useful readout tool for spin-based electronics, which is why the claim merits attention. The text is theoretical only and reports no experimental data, so the size of the effect in real materials remains untested.
- **Background needed**: - Spin: an electron's intrinsic magnetic moment, which can be carried as a "spin accumulation" in a material.
- Spin Hall effect / inverse spin Hall effect: a spin current bends sideways and produces a transverse charge voltage; the spin Hall angle measures how efficient this is, and it is usually small.
- Nonlocal spin-valve: a device where spin is injected at one point and detected by a voltage at a separate point, so the signal is not mixed with ordinary charge current.
- Superconductor gap: below a critical temperature, electrons pair up and there is an energy gap; quasiparticles (single unpaired excitations) are suppressed below this gap, so charge current flows with little resistance.
- Charge imbalance: a surplus of one kind of quasiparticle charge that a spin bias can create in a superconductor.
- Spectral broadening: a smearing of the energy levels caused by finite lifetimes, which the paper includes in its calculation. · level: research-level

<details><summary>Original abstract</summary>

Spin-to-charge conversion is central to spintronics, but conventional spin Hall mechanisms are intrinsically limited by the small spin Hall angle. Here we show that superconductivity can overcome this limitation and enable near-unity spin-to-charge signal conversion. We consider a nonlocal spin-valve geometry in which a spin accumulation is injected into a superconductor and converted into a transverse charge signal through the inverse spin Hall effect. In the superconducting state, the strongly suppressed quasiparticle conductance below the gap allows the resulting charge imbalance to generate a voltage comparable to the injected spin bias, despite a small spin Hall angle. We derive the full nonequilibrium response including finite spectral broadening and finite temperature, and propose temperature and spin-bias-dependent measurements of the detector voltage to test our predictions.

</details>

## Particle physics

### [Superheavy gravitational dark matter from runaway bubble collisions](https://arxiv.org/abs/2611.30113)
*Cheng-Wei Chiang, Van Que Tran* · `hep-ph` · arXiv:2611.30113v1 · relevance 0.16

- **In one sentence**: The paper proposes that a particle coupling only gravitationally is pair-produced when runaway bubble walls collide during a first-order phase transition, yielding a flat relic abundance up to masses near 10^17 GeV at low reheating temperatures.
- **In plain words**: The paper asks how very heavy dark matter could be made in the early universe, when a vacuum bubble expands and its walls collide. The idea is that a hidden particle interacting only through gravity can be created in pairs when these fast-moving walls hit, with no other forces needed. The text reports an estimated yield for a Dirac fermion (a common type of particle) that stays roughly constant up to very large masses, enough to account for dark matter up to about 10^17 GeV even when the universe was reheated to temperatures far below that mass.
- **Why it matters**: It offers a route to dark matter far heavier than the usual freeze-in mechanism can reach, using gravity as the only link to the Standard Model. The text does not say how the result compares with observations or whether the bubble scenario is realised, so its relevance to real dark matter remains an open question.
- **Background needed**: - Dark matter: unseen matter that makes up most of the matter in the universe, inferred from its gravitational pull.
- Vacuum bubbles: in some models of the early universe, regions of space tunnel into a lower-energy state and expand as bubbles; their walls can run away, accelerating toward light speed.
- Graviton exchange: gravity is carried by a hypothetical particle, the graviton; here it is the only force linking the bubble walls to the dark particle.
- Yield: the number of dark particles produced per unit of entropy (a measure of the hot material's disorder), which sets how much dark matter remains.
- Reheating temperature: the temperature the universe reached after inflation ended and its energy was converted into hot particles.
- Freeze-in: a production mechanism where particles are slowly created by ordinary collisions in the hot early universe; the text says it fails for these very heavy masses.
- Planck mass: the natural mass scale of gravity (about 10^19 GeV). · level: research-level

<details><summary>Original abstract</summary>

A stable particle that couples only through gravity is pair-produced in collisions of runaway bubble walls by graviton exchange. For a transition of duration $1/\beta$, a Dirac fermion reaches the yield $Y_X\simeq6.8\times10^{-3}(H/\beta)(T_{\rm reh}/M_{\rm P})^3$, where $H$ is the Hubble rate of the vacuum energy, $T_{\rm reh}$ the reheating temperature and $M_{\rm P}$ the reduced Planck mass. The yield is flat up to masses near $(H/\beta)M_{\rm P}/\nu^2$, where $\nu$ of order one sets the wall-field excursion. Gravity alone then gives dark matter up to about $10^{17}$~GeV at reheating temperatures far below its mass, where freeze-in fails.

</details>

### [WIMPs as FIMPs: the Inert Doublet Model and low-temperature reheating](https://arxiv.org/abs/2611.28217)
*Genevi\`eve B\'elanger, Nicol\'as Bernal, Andreas Goudelis et al.* · `hep-ph` · arXiv:2611.28217v1 · relevance 0.16

- **In one sentence**: The paper revisits the Inert Doublet Model, showing that low reheating temperatures can stop a WIMP dark matter candidate from reaching chemical equilibrium, so its relic abundance comes from freeze-in rather than freeze-out, including instantaneous and finite-duration reheating scenarios.
- **In plain words**: The paper asks how dark matter particles could have been produced in the early universe, a question usually answered by assuming they were once in thermal balance and then "froze out" as the universe cooled. The authors show that if the universe was reheated to only a low temperature after inflation, a heavy dark matter candidate in the Inert Doublet Model may never reach that balance and instead gets produced gradually, a process called freeze-in. They describe several possible production histories and report that this opens parameter regions that would otherwise be ruled out because they produce too much dark matter.
- **Why it matters**: It suggests that the standard assumption linking a WIMP's abundance to its interaction strength may not hold, which matters for how dark matter searches are interpreted. The text does not show experimental consequences, so the broader significance remains to be tested.
- **Background needed**: - Dark matter: unseen matter whose gravity explains galaxy motions; its total amount is measured.
- WIMP (weakly interacting massive particle): a heavy dark matter candidate that is produced through its interactions with ordinary particles.
- Thermal freeze-out: the particle is in balance with the hot plasma, then drops out as the universe expands and cools, leaving a fixed leftover amount.
- Freeze-in: the particle is produced very weakly and gradually, never reaching balance; this is typical of FIMPs (feebly interacting particles).
- Reheating: the hot phase of the universe after inflation; its temperature sets the early thermal history.
- Inert Doublet Model: an extension of the Standard Model Higgs sector that contains a dark matter candidate.
- Relic abundance: the amount of dark matter left over today. · level: research-level

<details><summary>Original abstract</summary>

Weakly Interacting Massive Particles (WIMPs) are conventionally assumed to acquire their dark matter relic abundance through thermal freeze-out. However, this association relies on assumptions concerning the thermal history of the early Universe. We revisit the Inert Doublet Model (IDM), a representative WIMP framework in which dark matter interacts with the Standard Model through electroweak gauge interactions, even when its Higgs-portal coupling vanishes. We demonstrate that sufficiently low reheating temperatures can prevent chemical equilibrium, allowing a genuine WIMP to acquire its relic abundance through freeze-in rather than freeze-out. Considering both instantaneous and finite-duration reheating, we identify different production histories, including freeze-out during radiation domination, freeze-out during reheating, and freeze-in with potentially significant annihilation backreactions. These scenarios open regions of the IDM parameter space that would otherwise be excluded by dark matter overabundance. Our results demonstrate that WIMPs can behave as FIMPs, depending on the thermal history of the Universe.

</details>

## Nuclear physics

### [Effect of dark matter and scalar-cut potential on the macroscopic properties of neutron stars: A chiral quark mean field approach](https://arxiv.org/abs/2611.30434)
*Hrishika P, Arvind Kumar* · `hep-ph` · arXiv:2611.30434v1 · relevance 0.13

- **In one sentence**: A chiral SU(3) quark mean-field study of neutron stars that adds a scalar-cut potential to the baryonic equation of state and models fermionic dark matter as a self-interacting, gravity-coupled second fluid within a two-fluid TOV framework, examining mass-radius relations, tidal deformability and gravitational redshift.
- **In plain words**: Neutron stars are extremely dense remnants of collapsed stars, and this paper asks how a hypothetical invisible component, dark matter, might change their size, mass and other observable properties. The authors build a computer model of the star's matter, including a term that stiffens its pressure response, and add a dark-matter fluid that interacts with ordinary matter only through gravity. They report that the stiffening term makes the matter less compressible, while adding more dark matter generally softens it, with the effect depending on the dark particle's mass and how it interacts.
- **Why it matters**: Neutron star mass, radius and tidal deformability are among the few astrophysical handles on how matter behaves at extreme density, and gravitational-wave and X-ray observations can measure them. The paper is a theoretical model, so it does not show that dark matter is present in stars; it shows what signatures a dark-matter component would be expected to leave if it were.
- **Background needed**: - Neutron star: a city-sized, extremely dense stellar remnant; its mass and radius depend on its equation of state (the rule relating pressure to density).
- Mass-radius relation and tidal deformability: observable properties that constrain the equation of state; tidal deformability describes how much a star stretches under a companion's gravity.
- Gravitational redshift: how much light from the star is stretched to longer wavelengths by its gravity.
- Quark mean-field model: a theoretical framework in which quarks are confined inside baryons (protons, neutrons and similar particles) and their interactions are represented by exchanged effective fields.
- Chiral SU(3): a symmetry-based approach that includes strange quarks in the model.
- Two-fluid TOV: the standard Tolman-Oppenheimer-Volkoff equations for stellar structure, extended so that dark and ordinary matter are separate fluids coupled only by gravity.
- Dark matter core versus halo: whether dark matter concentrates in the star's centre or extends outward around it. · level: research-level

<details><summary>Original abstract</summary>

We investigate the effects of fermionic dark matter (DM) and scalar-cut potential ($U_{\text{cut}}(\phi)$) on the equation of state (EOS) and macroscopic properties of neutron stars. The baryonic matter consists of neutrons, protons, electrons, and muons under the $\beta$-equilibrium and is described within the chiral SU(3) quark mean-field (CQMF) model. In this framework, quarks are confined within baryons, whose properties are modified through the exchange of scalar fields $\sigma$, $\zeta$, and $\delta$, and vector fields $\omega$ and $\rho$. The DM is modelled as a self-interacting fermionic fluid with scalar $\varphi_D$ and vector $V_D^\mu$ mediators. The baryonic and DM fluids interact only through gravity and are treated within a two-fluid Tolman-Oppenheimer-Volkoff formalism. We examine the resulting mass-radius relation and tidal deformability, along with the gravitational redshift, to investigate the effects of DM on neutron star structure and observable properties. The inclusion of $U_{\text{cut}}(\phi)$ stiffens the EOS, whereas increasing the DM fraction generally softens the EOS and modifies the mass-radius relation, tidal deformability, and gravitational redshift. The magnitude and nature of these modifications depend on the DM particle mass and mediator interactions, which determine whether the resulting configurations exhibit compact DM cores or extended DM halos.

</details>

### [Bypassing the Nanoampere Limit: A Thick-Target Methodology for Ultra-Low-Energy Resonances in the $^{11}$B(p,$\alpha$)2$\alpha$ Reaction](https://arxiv.org/abs/2611.30439)
*Xu-Yang Luo, Wen-Qing Wei, Shi-zheng Zhang et al.* · `nucl-ex` · arXiv:2611.30439v1 · relevance 0.09

- **In one sentence**: The paper introduces a thick-target method, with Monte Carlo yield calculations and no empirical normalization, to measure the very small cross section of the 11B(p,α)2α reaction at ultra-low proton energies using 20–60 µA beams, validated on the known 148 keV resonance.
- **In plain words**: This paper is about measuring how often a proton hitting a boron-11 nucleus causes a fusion-type reaction, which is extremely rare at very low proton energies. Ordinary experiments can only use tiny beam currents, so the counts are too low to be practical. The authors describe a different setup that uses beams about a thousand times stronger, and they check it against a resonance (a sharply enhanced energy point) that was already well measured.
- **Why it matters**: Boron-11 fusion is of interest for nuclear astrophysics and for possible clean fusion energy, and the reaction's behavior at low energies is poorly pinned down. The main value claimed is a method that could make searches for weak low-energy resonances more efficient; the text reports only preliminary checks below 100 keV, so its broader impact is still uncertain.
- **Background needed**: - Cross section: a measure of how likely a nuclear reaction is for a given collision energy; tiny values mean rare events.
- Nuclear reaction 11B(p,α)2α: a proton strikes a boron-11 nucleus and it breaks into helium nuclei (alpha particles).
- Resonance: an energy at which the reaction rate sharply increases; the paper's test case is at 148 keV (center-of-mass energy), with a width of about 5.3 keV.
- Thin vs. thick target: a thin target is a very thin layer where the beam loses little energy, forcing low beam current; a thick target absorbs the beam gradually, allowing much higher current but requiring careful modeling of energy loss.
- Monte Carlo simulation: computer modeling using random sampling to predict outcomes such as reaction yield.
- Beam current is measured in microamperes (µA) and nanoamperes (nA); 1 µA is 1000 times 1 nA. · level: research-level

<details><summary>Original abstract</summary>

Precise measurements of the low-energy cross section for the $^{11}$B(p,$\alpha$)2$\alpha$ reaction is critical for nuclear astrophysics and fusion energy research, yet such measurements are experimentally demanding due to the reaction's extremely small cross section. Conventional thin-target experiments are fundamentally limited to nanoampere beam currents, which restrict count rates to impractical levels at ultra-low proton energies. To overcome this limitation, we report a correction-free thick-target methodology capable of operating at beam currents of 20-60 microamperes, corresponding to a gain of over three orders of magnitude. Monte Carlo simulations of the full reaction kinematics are employed to determine the absolute reaction yield, eliminating the requirement for empirical normalization factors. At the well-known 148~keV (c.m.) resonance peak, our extracted resonance energy ($E_{\mathrm{r}} = 148.0$~keV) and level width ($\Gamma_{\mathrm{cm}} = 5.3$~keV) are demonstrated in good agreement with published data. A scheme via comparing the measured reaction probability with a theoretical extrapolation result is furtherly presented to probe low-energy resonances below 100~keV region. Preliminary measurements at proton energies of 75~keV and 100~keV reveal no evidence for additional low-energy resonances. This work provides a robust new methodology to measure cross section and resonance parameters for the p$^{11}$B reaction and offers a highly efficient tool for systematic resonance searches in the ultra-low-energy regime.

</details>

## Quantum information and computing

### [Quantum simulation of low-temperature impurity models](https://arxiv.org/abs/2611.30187)
*Jiaqing Jiang, Nathan Ju* · `quant-ph` · arXiv:2611.30187v1 · relevance 0.16

- **In one sentence**: The paper gives quantum algorithms for preparing thermal and ground states of fermionic quantum impurity models, using global jump operators in quantum Gibbs samplers to avoid exponential-in-inverse-temperature overhead, with a claimed Heisenberg-scaling estimate of static and dynamical properties.
- **In plain words**: The paper looks at a standard model in materials physics: a small strongly interacting piece of a system attached to a large, simpler surrounding bath. It describes quantum computer procedures for preparing this system's state at low temperature and for estimating its properties. The authors state that the running time grows polynomially with system size and inverse temperature, and only logarithmically with the required accuracy.
- **Why it matters**: Impurity models are the core computational step in dynamical mean field theory, a widely used method for strongly correlated materials, so faster low-temperature simulation would matter if the scaling holds in practice. The text is a theory paper with claimed asymptotic bounds only; it does not show any numerical demonstration or hardware run, so practical impact is unclear.
- **Background needed**: - Quantum impurity model: a small interacting subsystem coupled to a large noninteracting bath.
- Dynamical mean field theory: a method that maps a material's behavior onto an impurity model solved self-consistently.
- Thermal state: the quantum state of a system in equilibrium at a given temperature; inverse temperature (beta) grows as temperature falls.
- Fermionic modes: the basic units of storage for electrons-like particles, here counted as n.
- Quantum Gibbs sampler: a quantum analogue of Markov chain Monte Carlo that prepares thermal states by simulated random jumps between states.
- Spectral gap: the energy difference between the ground state and the first excited state; a larger gap makes the ground state easier to isolate.
- Purification: an enlarged quantum state whose reduced description equals the thermal state, allowing thermal averages to be estimated on a quantum computer.
- Heisenberg scaling: error decreasing as 1/δ rather than 1/√δ, the best possible for many estimation tasks. · level: research-level

<details><summary>Original abstract</summary>

Quantum impurity models, which describe a small but strongly-interacting subsystem coupled to a large noninteracting bath, are the computational core of dynamical mean field theory and play an important role in simulating strongly correlated materials. We develop quantum algorithms for efficiently simulating these models at low temperatures and with high precision. For any impurity model on $n$ fermionic modes with fixed impurity size: (1) We give a quantum algorithm that prepares the thermal state at inverse temperature $\beta$ to precision $\delta$ in time $\mathrm{poly}(n,\beta,\log(1/\delta))$. This algorithm is the first to achieve both polynomial scaling in the inverse temperature and polylogarithmic scaling in the precision. When the Hamiltonian has an inverse-polynomial spectral gap, our quantum algorithm prepares its ground state to precision $\delta$ in time $\mathrm{poly}(n,\log(1/\delta))$. (2) We further give a quantum algorithm that prepares a purification of the thermal state in time $\mathrm{poly}(n,\beta,\log(1/\delta))$. Using this purification, we estimate static and dynamical properties with error $\delta$ in time polynomial in $n$ and $\beta$ and linear in $1/\delta$ up to polylogarithmic factors, achieving the Heisenberg scaling. Our algorithms build on quantum Gibbs samplers, which are quantum analogues of Markov chain Monte Carlo methods. By using global jump operators instead of local ones, we avoid the $\exp(\beta)$ overhead commonly associated with quantum Gibbs samplers, making them efficient for impurity models even at low temperatures.

</details>

### [Incompressible quantum information](https://arxiv.org/abs/2611.28361)
*Lasse H. Wolff, Matthias Christandl, Bergfinnur Durhuus et al.* · `quant-ph` · arXiv:2611.28361v1 · relevance 0.14

- **In one sentence**: The paper shows that, unlike the classical case, a small classical system correlated with a large quantum system cannot always be matched by a compressed encoding of the large system that keeps the correlations intact, which limits information-bottleneck approaches to quantum machine learning.
- **In plain words**: The paper asks whether a big quantum system can be squeezed into a much smaller one without losing the links it shares with a small classical system. For ordinary classical data this is always possible, but the authors show that for some quantum states any substantial compression destroys a significant amount of the shared information, measured as mutual information.
- **Why it matters**: It identifies a limit on a compression idea used in quantum machine learning: specifying the relevant features with a small system does not guarantee a compact encoding of the quantum data that keeps those features. The text does not say how far this affects practical quantum learning methods.
- **Background needed**: - Mutual information: a measure of how much knowing one system tells you about another.
- Compression: encoding a large system in fewer resources, here meaning a smaller system.
- Classical versus quantum: quantum systems can be correlated in ways with no classical counterpart, and their states cannot always be copied or split as classical data can.
- Information bottleneck: a method that keeps only the parts of data relevant to a target, used in machine learning.
- Bipartite state: a joint quantum state of two systems, one small and classical, one large and quantum. · level: research-level

<details><summary>Original abstract</summary>

For a small classical system correlated with a large one, it is always possible to compress the large system down to a size only dependent on the size of the smaller one, while preserving all correlations up to a given controllable error. Here, we show that such a statement does not hold at all when the large system is quantum mechanical. More precisely, we show that there are bipartite states such that any compression of the large system, by a non-trivial relative factor, will necessarily lead to the destruction of a significant amount of correlation, measured in mutual information. Our results therefore identify a limitation of information-bottleneck approaches to quantum machine learning, showing that a small system specifying the relevant features contained in a large quantum data set does not guarantee a compact encoding of the latter that preserves the relevant correlations.

</details>

## Optics and atomic physics

### [Reconfigurable Microwave Photonic All-Pass Filters based on Optical Kerr Microcombs](https://arxiv.org/abs/2611.29115)
*David J. Moss* · `physics.optics` · arXiv:2611.29115v1 · relevance 0.08

- **In one sentence**: The paper proposes and experimentally demonstrates microwave photonic all-pass filters (1st and 2nd order) built on a Kerr microcomb-driven transversal filter, reconfigurable by changing tap coefficients in software.
- **In plain words**: The paper describes a way to shift the timing (phase) of radio-frequency signals using light, without changing their strength. The authors built first- and second-order versions of such a filter from an optical frequency comb, a set of evenly spaced laser colors. They report that the filter's settings can be changed by reprogramming its tap coefficients (the weights applied to each comb line) rather than by rebuilding the hardware.
- **Why it matters**: Precise control of signal phase matters for high-bandwidth radar, communications and signal processing, so a filter that is both low-loss and easy to reconfigure could be useful there. The text reports measured group delays of 580 ps (1st order) and 1740 ps (2nd order) with amplitude variation around 2 dB, but it does not compare these against competing methods, so its practical standing is unclear.
- **Background needed**: - Microwave photonics: using light to process radio-frequency signals, often for bandwidth or flexibility.
- All-pass filter: a filter that changes the phase (timing) of a signal while leaving its amplitude roughly unchanged.
- Group delay: how much a signal's envelope is delayed at each frequency; larger values mean stronger phase change.
- Optical Kerr microcomb: a set of many equally spaced optical colors generated in a tiny resonator by a nonlinear optical effect.
- Transversal filter (tapped delay line): a filter that sums weighted, delayed copies of a signal; the tap coefficients are the weights.
- Order of a filter: roughly, how many poles or phase-shifting stages it has; higher order gives sharper phase transitions. · level: research-level

<details><summary>Original abstract</summary>

Microwave photonic (MWP) all pass filters (APFs), which enable phase manipulation without altering signal amplitudes, are essential for phase engineering in high bandwidth microwave signal processing. However, achieving a high degree of reconfigurability in the filter order and characteristic parameters of APFs remains challenging for conventional methods. Here, we propose and experimentally demonstrate a new strategy for realizing MWP APFs based on a microcomb driven transversal filter system, enabling high reconfigurability, sharp phase transitions with high group delays, and low loss. We experimentally demonstrate both 1st and 2nd order APFs, achieving a maximum amplitude variation (MAV) of 1.95 dB and a maximum group delay (MGD) of 580 ps for the former, and a MAV of 2.01 dB and an MGD of 1740 ps for the latter. In addition, both independent and joint tuning of APF characteristic parameters are demonstrated by simply programming the tap coefficients without changing any hardware, enabling highly reconfigurable filter response for diverse phase engineering functionalities. These results highlight the potential of our approach for implementing MWP APFs with both high performance and reconfigurability for practical applications requiring dynamic and versatile phase control.

</details>

### [Anisoplanatic Blind Deconvolution using Phase Diversity](https://arxiv.org/abs/2611.28458)
*Shubhankar Jape, Seungman Choi, Peter Menart et al.* · `physics.optics` · arXiv:2611.28458v1 · relevance 0.07

- **In one sentence**: The paper proposes coded anisoplanatic blind deconvolution (CA-BD), which uses a pupil-plane spatial light modulator to apply known phase codes across short image bursts to jointly estimate a scene and spatially varying atmospheric phase, and compares it in simulation against tuned multiframe blind deconvolution.
- **In plain words**: Turbulence in the air bends light from distant objects and blurs images, and the blur differs from one part of the view to another and changes over time. This paper describes a way to undo that blur by placing a programmable light-shaping device in the imaging path that applies a known pattern to each frame, so the frames differ in a controlled way even when taken quickly. In simulations, the authors report that this approach recovers phase errors more accurately than a standard reconstruction method, especially in stationary turbulence.
- **Why it matters**: Imaging through turbulence matters for astronomy and long-range surveillance, where fast capture is often needed. The text reports only simulation results, so how well the approach works with real hardware and real air is not shown here.
- **Background needed**: - Atmospheric turbulence: small changes in air temperature and density that distort light's wavefront and blur images.
- Isoplanatic angle: the angular region over which the blur is roughly the same; beyond it, the blur varies across the image (anisoplanatism).
- Blind deconvolution: recovering a sharp image when the blur itself is unknown, estimated jointly with the scene.
- Phase diversity: using several measurements with known, different phase distortions so the unknowns can be separated.
- Spatial light modulator (SLM): a programmable device that changes the phase of light across the aperture.
- Cramér-Rao bound: a theoretical lower limit on how precisely a parameter can be estimated from measured data.
- Coherence time: how long the turbulence stays roughly fixed; the paper's fast-capture advantage depends on measurements taken within a few of these. · level: research-level

<details><summary>Original abstract</summary>

Atmospheric turbulence distorts the wavefront of light from a distant scene and blurs its image. Over a field of view wider than the isoplanatic angle, the distortion varies with direction and evolves in time, so no single wavefront describes the blur. Multiframe blind deconvolution (MFBD) can recover the scene from measurements spread over a long acquisition, but falls short during fast imaging because of limited diversity across measurements. We present coded anisoplanatic blind deconvolution (CA-BD), in which a pupil-plane spatial light modulator (SLM) applies a different known phase code to every measurement, with no wavefront sensor or deformable mirror, so that the measurements carry diversity even within a short acquisition. A per-pixel single-layer estimator recovers the object and spatially varying phases from the coded measurements. In simulation, a Cram\'er-Rao bound analysis shows that under anisoplanatism direct imaging needs about 41 times the photons of coded imaging for equal phase precision in strong turbulence. At the stronger of two turbulence strengths, CA-BD outperforms tuned MFBD on average at every burst length. It reduces the phase mean squared error 3.5x for stationary turbulence and 2-3x for time-varying turbulence. Measurements taken within a few coherence times benefit most from the known coded SLM patterns, making faster SLMs the key to its full advantage in time-varying turbulence.

</details>

## Fluids and plasma

### [Formation of Multiple BGK-like Structures in the Time-asymptotic State of Collisionless Vlasov-Poisson Plasmas](https://arxiv.org/abs/2611.28898)
*Hugo A. Carril, Jorge A. Gidi, Roberto E. Navarro et al.* · `physics.plasm-ph` · arXiv:2611.28898v1 · relevance 0.09

- **In one sentence**: High-resolution Vlasov-Poisson simulations of a collisionless Maxwellian plasma show the time-asymptotic state evolving into multiple vortex-like phase-space structures, interpreted as a superposition of many BGK-like modes with nearly constant phase speeds, with power-law spectra suggesting a cascade to small scales.
- **In plain words**: This paper studies what a plasma (a gas of charged particles) settles into after a disturbance, when collisions between particles are negligible. The usual picture is two opposing wave-like patterns, but the simulations here show the plasma instead forms many swirling, vortex-like patterns that gradually fill the particle-position-and-speed map and reduce its folding into finer and finer filaments. The spectra of the electric field and the averaged particle distribution follow power laws, which the authors say is consistent with energy moving toward smaller scales.
- **Why it matters**: It challenges the standard description of how a collisionless plasma relaxes after a large wave is excited, which matters for plasma physics and space or fusion plasmas. The text does not establish how far the result extends beyond the simulated setup, so its wider relevance is uncertain.
- **Background needed**: - Plasma: an ionized gas whose charged particles interact through their own electric fields.
- Collisionless: particles rarely bump into each other, so their motion is governed by the collective field.
- Vlasov-Poisson equations: the standard model that tracks the particle distribution in position and velocity together with the electric field it generates.
- Phase space: a map of particle position against velocity; filamentation is the stretching of the distribution into thin folds.
- BGK mode: an exact, steady wave pattern in a collisionless plasma, named after Bernstein, Greene and Kruskal.
- Power-law spectrum: a pattern where energy at each scale falls off as a fixed power of the scale, often linked to a cascade of energy from large to small scales. · level: research-level

<details><summary>Original abstract</summary>

The time-asymptotic state of a finite-amplitude perturbation in a collisionless and Maxwellian plasma is typically represented as a steady state of two non-linearly superposed, counter-propagating Bernstein-Greene-Kruskal (BGK) modes. Using high-resolution Vlasov-Poisson simulations, we show that the plasma evolves self-consistently into a time-asymptotic state of multiple vortex-like structures that gradually fill the phase-space and reduce filamentation. This occurs without the need for external forcing or the presence of an energetic plasma population. This finding suggests that the time-asymptotic regime of the plasma is rather akin to a non-linear superposition of multiple BGK-like modes associated with nearly constant phase-speed waves. The electric field and the space-averaged particle distribution function exhibit a power-law broad spectrum, which is consistent with an energy cascade towards smaller scales in both position and velocity spaces.

</details>

### [Numerical Study of Flow and Cavitation in Single-Liquid Injectors with Sharp-Edged and Chamfered Orifice Inlets](https://arxiv.org/abs/2611.28527)
*Shreyash Gulati, Sven R. Walsberg, Timothy W. Nearhood et al.* · `physics.flu-dyn` · arXiv:2611.28527v1 · relevance 0.08

- **In one sentence**: A CFD study using the SST k-omega turbulence model, the ZGB cavitation model and the VOF method to simulate water flow and cavitation through sharp-edged and chamfered orifice inlets in single-liquid injectors, validated against existing flow-rate data.
- **In plain words**: This paper looks at how water squirts through tiny holes in fuel-injector-style nozzles, and when bubbles form inside the flow (cavitation). The authors ran computer simulations across a range of pressure drops and hole length-to-diameter ratios. They report that bubbles were strongest in sharp-edged holes with a moderate length at higher pressure, that a known "hydraulic flip" appeared in one case, and that rounding the inlet (chamfering) changed where bubbles began.
- **Why it matters**: Cavitation inside injector holes can affect spray quality and wear in engines and similar devices, so simulation results that match experiments may help design choices. The text does not say how far these findings extend beyond the cases studied, so the wider application is uncertain.
- **Background needed**: - Cavitation: vapor bubbles that form in a liquid when local pressure drops sharply, then collapse.
- Orifice: a small hole that a liquid is forced through, such as a nozzle opening.
- Sharp-edged vs. chamfered inlet: a sharp corner at the hole entrance versus a beveled, angled edge.
- Length-to-diameter ratio: how long the hole is compared with its width; here 2, 5 and 10.
- Hydraulic flip: a flow pattern in which the liquid detaches from the hole wall and fills the orifice, which changes the spray.
- CFD (computational fluid dynamics): simulating fluid flow on a computer.
- Turbulence model (SST k-omega), cavitation model (ZGB), and VOF (tracking liquid and gas volumes): the computational tools used. · level: research-level

<details><summary>Original abstract</summary>

In the current work, the investigators used Computational Fluid Dynamics (CFD) to investigate water flow and cavitation in single-liquid injectors with sharp-edged and chamfered orifice inlets. The k-{\omega} Shear Stress Transport (SST) turbulence model was used along with the Zwart-Gerber-Belamri (ZGB) cavitation model and the Volume of Fluid (VOF) method. The CFD predictions for the volumetric flow rate were validated against existing experimental data for the sharp-edged and chamfered orifice inlets. Pressure drops ranging between 0.07 MPa and 0.59 MPa were considered along with orifice length-to-diameter ratios of 2, 5, and 10. Strong cavitation was observed for the sharp-edged orifice inlet cases with a length-to-diameter ratio of 5 and a pressure drop larger than 0.2 MPa. A hydraulic flip was observed for the sharp-edged orifice inlet with a length-to-diameter ratio of 5 and a pressure drop of 0.59 MPa, which was consistent with the findings from the previous experimental study. Cavitation inception was observed for the chamfered orifice inlet cases with a length-to-diameter ratio of 5 and pressure drops larger than 0.2 MPa. For the sharp-edged orifice inlet with orifice length-to-diameter ratios of 2 and 10, a strong cavitation was observed inside the orifice.

</details>

## Biological physics

### [Estimating Extrapolation Factors in Time-Resolved Crystallography](https://arxiv.org/abs/2611.28961)
*Sebastian Bielfeldt, Henry N. Chapman, Thomas J. Lane* · `physics.bio-ph` · arXiv:2611.28961v1 · relevance 0.07

- **In one sentence**: The paper reviews and benchmarks methods for estimating the extrapolation factor (the fraction of triggered molecules in a time-resolved crystallography experiment) and introduces Vacuum Level Matching, a voxel-by-voxel method that uses the non-negativity of electron density, with a Python package.
- **In plain words**: Scientists who watch proteins change shape by triggering them with light or another signal often get a mixed signal: some molecules in the crystal have changed and some have not. This paper explains how the existing ways of separating the two were built and where they fail, especially with noisy data or when only a small fraction of molecules has changed. It then proposes a new method that uses a physical limit (the density of electrons cannot go below zero) to make the estimate and flags datasets too weak to trust.
- **Why it matters**: Time-resolved crystallography is one of the few ways to see molecular motion at atomic detail, so the reliability of how signals are separated affects what structural changes are reported. The text reports benchmarks on simulated data and two experimental datasets, but it does not establish how widely the method will be adopted or how it performs beyond these cases.
- **Background needed**: - X-ray crystallography: firing X-rays at a protein crystal and reading the diffraction pattern to build a 3D map of electron density.
- Time-resolved crystallography: triggering a reaction in the crystal (often with a light pulse) and taking snapshots at different delays to watch the protein change.
- Reference state vs. triggered state: the untouched protein shape versus the shape after the trigger.
- Extrapolation factor: a fitted scaling number that relates the observed change to the full change; the paper notes it is related to but distinct from occupancy (the true fraction of molecules triggered).
- Electron density: the map of where electrons sit in the crystal; it cannot be negative, which is the physical constraint the new method uses.
- Voxel: one small 3D cell of the density map, treated independently.
- rsEGFP2 and photolyase: two light-responsive proteins used as experimental test cases. · level: research-level

<details><summary>Original abstract</summary>

Time-resolved crystallography (TRX) captures macromolecules in action, but a triggered crystal contains a mixture of triggered proteins in an unknown state and untriggered proteins in the reference state. Separating these is necessary to isolate the dynamics of interest and is an underdetermined data-analysis task. For the simplest case, with one triggered state and one reference state, a range of methods exists, but their assumptions, accuracy, and domains of applicability have not been systematically investigated. Here, we deconstruct and review the methods in current use, employing a unified notation. We make their assumptions explicit and benchmark each on a simulated dataset. A key point is that many of these methods do not estimate the fraction of all triggered molecules in the crystal, but instead estimate a latent parameter we call the extrapolation factor, which is related to but distinct from the so-called "occupancy". As our simulations make apparent, current methods do not always yield accurate results, in particular with noisy data and when the fraction of triggered protein is low. Inspired by previous work, we introduce Vacuum Level Matching, a method that grounds the estimate in the physical constraint that electron density is a nonnegative quantity: it cannot fall below a vacuum level. Operating voxel by voxel, Vacuum Level Matching replaces the manual choices of previous methods with a data-driven procedure and reports quality-control metrics that flag data unable to support a confident prediction. On the same simulated data, it outperforms state-of-the-art methods, and on two experimental datasets, rsEGFP2 and a multi-time-point photolyase series, it recovers known structural changes while flagging issues where the data are weak. Finally, we report an implementation of Vacuum Level Matching in the form of a small, reusable Python package.

</details>

### [Nonequilibrium fluctuations could explain the hot mitochondria paradox](https://arxiv.org/abs/2611.28225)
*Matthew P. Leighton, Benjamin B. Machta* · `cond-mat.stat-mech` · arXiv:2611.28225v1 · relevance 0.04

- **In one sentence**: A theory proposing that nonequilibrium fluctuations in the cell, read by frequency-selective molecular thermometers, could produce apparent 10 K mitochondrial temperature differences without a true steady-state temperature gradient.
- **In plain words**: Experiments have reported that the inside of mitochondria, the energy-producing parts of cells, can appear up to 10 degrees warmer than the surrounding cell. Heat physics suggests a real difference that large should not be able to persist, so the reported values have stayed unexplained for about a decade. This paper proposes that random, out-of-balance jiggling inside the cell, picked up by temperature sensors tuned to particular frequencies, could make such differences appear without a true steady temperature gap.
- **Why it matters**: The proposal tries to reconcile a long-standing conflict between measurements and heat-conduction theory, which matters for how cells manage energy and how temperature is measured inside living cells. The text gives only the abstract-level argument, so whether it holds up depends on details not shown here.
- **Background needed**: - Mitochondria: small structures inside cells that produce most of the cell's usable energy, and that release heat as a by-product.
- Steady state: a condition where temperatures and flows no longer change over time; a real temperature difference would need a continuous energy supply to maintain.
- Microkelvin vs. 10 K: the physics the abstract cites says a steady difference inside a cell should be tiny (microkelvin scale), while measurements report up to 10 K.
- Nonequilibrium fluctuations: random energy changes in a system that is not in thermal balance, which can be larger than ordinary thermal noise.
- Molecular temperature probes: fluorescent or similar molecules whose signal changes with temperature; their readout can depend on the timescale they respond to. · level: research-level

<details><summary>Original abstract</summary>

Several different experiments have found apparent temperature differences of up to 10 K between the interior of mitochondria and the rest of the cellular environment. The physics of heat conduction, however, precludes the steady-state existence of a temperature difference greater than the microkelvin scale within the cell, absent a far greater energy budget. Nearly a decade after the first reported measurement, this apparent paradox remains unexplained. Here, we propose an explanation which allows the elevated temperature measurements to coexist with the theoretical impossibility of a true 10 K steady-state temperature difference. We suggest that nonequilibrium fluctuations within the cellular environment, combined with molecular temperature probes sensitive to specific ranges of frequencies, can lead to apparent 10 K temperature differences with a biologically attainable power budget.

</details>

## Climate, atmosphere and Earth

### [Tipping cascades may lock the Earth system on a pathway towards a melthouse](https://arxiv.org/abs/2611.29086)
*Victor Couplet, Wim Thiery, Michel Crucifix* · `physics.ao-ph` · arXiv:2611.29086v1 · relevance 0.08

- **In one sentence**: A reduced-complexity Earth system model with a dynamic carbon cycle and interacting tipping elements finds no single threshold for a hothouse Earth, but suggests tipping cascades can lead to an irreversible melthouse state with over 10 m of sea-level rise, possibly even under low-emission scenarios.
- **In plain words**: This study asks whether warming could push the planet past a point of no return into a very hot state, often called a "hothouse Earth." Using a simplified computer model of the climate, carbon cycle and several large natural systems that can flip into new states, the authors found no single tipping point for that. Instead, one tipping event can set off others in a chain, which they say could lock in a "melthouse" state with more than 10 metres of sea-level rise.
- **Why it matters**: Sea-level rise of this scale would threaten coastal cities, so the claim bears directly on climate policy. The text does not show how sensitive the result is to the model's simplifications, so it should be read as a model-based risk estimate rather than a firm forecast.
- **Background needed**: - Tipping element: a part of the climate system (such as ice sheets or forests) that can shift abruptly and self-reinforce once a threshold is crossed.
- Tipping cascade: one tipping element triggering others, so the combined effect is larger than each alone.
- Hothouse Earth: a proposed very hot planetary state that would be hard to reverse, discussed widely in the literature.
- Melthouse: the paper's term for a state where large-scale ice loss drives very high sea levels; the text gives over 10 m of rise.
- Reduced-complexity model: a simplified climate model that runs quickly and captures key feedbacks but omits much detail.
- Irreversibility: once reached, the state persists even if emissions later fall. · level: research-level

<details><summary>Original abstract</summary>

The potential for the Earth system to transition irreversibly into a hothouse Earth has attracted considerable scientific and media attention but remains insufficiently explored in modeling studies. Using a reduced-complexity Earth system model that includes a dynamic carbon cycle and interacting tipping elements, we find no planetary threshold beyond which the Earth system irreversibly shifts into a hothouse state. Instead, tipping cascades can drive the system towards an irreversible melthouse state with over 10 m of sea-level rise. Such cascades may occur even under low-emission scenarios, preventing long-term stabilization of sea level at intermediate values. Our results overall highlight the substantial risk of a melthouse rather than a hothouse Earth, and call for drastic emission reductions to avert dramatic impacts on coastal cities and communities.

</details>

### [An exact and differentiable rewrite of a coupled weather and fire model](https://arxiv.org/abs/2611.30866)
*John S. Schreck, John Dennis, Iris Linck et al.* · `physics.ao-ph` · arXiv:2611.30866v1 · relevance 0.08

- **In one sentence**: AI coding agents rebuilt selected configurations of the WRF atmospheric and coupled fire model in PyTorch, matching the corrected Fortran code bit for bit over a 12-hour Marshall Fire simulation, with a differentiable backward pass and neural-network replacements for radiation and fire-spread terms.
- **In plain words**: This paper looks at a model that simulates how weather and wildfire interact, using the Marshall Fire in Colorado as its test case. The authors had AI coding agents rewrite the original Fortran program in a machine-learning framework, and treated any mismatch with the original as a bug to fix. The rewrite matched the original exactly at all 365 checkpoints over twelve simulated hours, and it ran about five times faster on one GPU than the original on a 128-core CPU node.
- **Why it matters**: A rewrite that reproduces an established forecast exactly, while also being differentiable, could make physics-based fire and weather models easier to tune and combine with learned components. The text does not show how well this generalises beyond the selected configurations and one fire event, so its wider value is still to be tested.
- **Background needed**: - WRF (Weather Research and Forecasting) is a widely used open-source weather model written in Fortran, a language long used for scientific computing.
- Its coupled fire component simulates how a wildfire spreads and how it feeds heat and smoke back into the air, including firebrands (burning particles carried by the wind).
- PyTorch is a machine-learning software library; models built in it can run on GPUs and can be differentiated automatically.
- "Bit for bit" agreement means the two programs produce numerically identical outputs, not just similar ones.
- A "backward pass" computes how sensitive the output is to each input, such as wind speed at each grid point, which can guide corrections.
- Double precision is a high-accuracy number format; the CPU baseline used it.
- Neural networks here stand in for some physics calculations (radiation and fire spread), and their effect is measured against the original physics. · level: research-level

<details><summary>Original abstract</summary>

AI is changing weather and climate prediction by replacing physical models with learned ones. Here we show a different path, in which AI coding agents rebuild the physical model itself in a machine-learning framework and reproduce its forecast bit for bit. We reconstruct selected configurations of the Weather Research and Forecasting model and its coupled fire physics in PyTorch, treating every difference from the corrected Fortran code as a bug. Across twelve hours of a Marshall Fire simulation, the two independently advancing codes agree bit for bit at all 365 checkpoints, in the atmosphere, fire and firebrand particles. This agreement holds when the code runs one operation at a time, with the Fortran code's mathematical library. On a separate fast route, the reconstructed model runs about five times faster on one GPU than the double-precision Fortran code on a 128-core CPU node. One backward pass maps the fire's sensitivity to the wind at every grid point. In synthetic tests, its derivatives show how to change wind and fuel moisture to correct a misplaced fire front. Neural networks replace the radiation and fire-spread calculations in 24-hour coupled forecasts, and we measure their effect against the physical calculation. An established model thus becomes fast, differentiable and open to learned components, with its tested calculation intact.

</details>

## Cosmology

### [Scale-dependent Dark Matter in a Multi-component Cosmological Framework: Distinct Components Governing Galactic and Cosmological Dynamics](https://arxiv.org/abs/2611.29007)
*V. K. Oikonomou* · `astro-ph.CO` · arXiv:2611.29007v1 · relevance 0.18

- **In one sentence**: The paper generalizes a scale-dependent, nearly isothermal equation-of-state model of galactic dark matter to cosmological scales, argues it cannot be all of the dark matter, and proposes that multiple dark matter components with different clustering govern dynamics at different scales.
- **In plain words**: The paper looks at dark matter, the unseen material that appears to hold galaxies together and shapes the large-scale universe. The authors extend a model that describes how dark matter pressure and density relate inside galaxies so that it applies to whole-universe scales as well. They conclude that this model cannot account for all dark matter on its own, and they suggest that a second kind of dark matter may dominate at cosmological scales.
- **Why it matters**: It proposes that dark matter may not be a single uniform substance, which could matter for how galaxies and the universe's large-scale structure are modeled. The text gives only the framework and conclusions, so how strongly it bears on observations is unclear from this summary alone.
- **Background needed**: - Dark matter: invisible matter inferred from its gravitational effects on galaxies and large-scale structure.
- Equation of state: a rule linking a material's pressure to its density; here pressure is written as an entropy-like factor K times density.
- Velocity dispersion: the typical spread of particle speeds in a system; higher means "hotter" material.
- Isothermal: a state where the effective temperature (here, velocity spread) stays roughly constant across the system.
- Cosmological vs. galactic scales: the whole universe versus individual galaxies.
- Clustering: how strongly a substance gathers into lumps under gravity. · level: research-level

<details><summary>Original abstract</summary>

In this work we generalize the concept of scale-dependent equation of state dark matter from galactic to cosmological scales. At galactic scales, the scale-dependent equation of state which successfully describes dark matter dominated galaxies has a nearly isothermal equation of state of the form $P(r)=K(r)\rho(r)$, where the entropy function $K(r)$ is radius dependent and slowly varying with the galactic radius. Using appropriate theoretical arguments, the successful galactic scale dark matter model is generalized to have a universal equation of state of the form $\langle P(\chi)\rangle =\langle \rho(\chi)\rangle \langle \sigma_{DM}^2\rangle$, where $\chi$ is the scale of the system under study and it can describe cosmological or galactic scales and $\sigma_{DM}$ is the characteristic velocity dispersion of dark matter at the relevant scales. This results to the entropy function behaving universally as $K(\chi)=\langle \sigma_{DM}^2\rangle$. We investigate the cosmological implications of scale-dependent equation of state dark matter, and we conclude that this scale-dependent equation of state dark matter cannot be the sole component of dark matter in the Universe. Also the second aim of this work is to provide a sufficient explanation for the question why $K_0$ changes for each galaxy, where $K_0$ is the value of $K(r)$ at intermediate and large radii from the core of the galaxy. Furthermore, we introduce the concept of having distinct dark matter components which cluster differently, and thus controlling differently the dynamics of the Universe at various scales. Scale-dependent equation of state dark matter can control the galactic scales, while another component can dominate at cosmological scales and thus control the Universe at cosmological scales.

</details>

### [Closure of averaged Einstein equations by DESI data](https://arxiv.org/abs/2611.31041)
*Thomas Buchert* · `astro-ph.CO` · arXiv:2611.31041v1 · relevance 0.15

- **In one sentence**: The paper tests whether the time-varying dark energy signal reported by DESI can instead arise from inhomogeneous structure in general relativity, using an averaged-dust framework with an effective scalar "morphon" field and one closure condition fitted to DESI 3-year parametrizations.
- **In plain words**: Astronomers using the DESI survey have reported that the effect driving the universe's accelerating expansion seems to change over cosmic time, which standard models explain by a special "dark energy" ingredient. This paper asks whether the same pattern could instead come from the uneven, clumpy distribution of matter, with no dark energy at all. The authors describe an averaged, effective description of that clumpiness and check it against parametrized DESI data, setting out what a model would need to match.
- **Why it matters**: If clumpy structure alone can reproduce the redshift dependence DESI reports, it would bear on whether dark energy is needed at all. The text presents this as a benchmark for future structure-formation models rather than a demonstrated result, and it does not show that the hypothesis holds.
- **Background needed**: - Dark energy: the hypothesized component that makes cosmic expansion speed up; the standard model treats it as a fixed or simply parametrized quantity.
- Equation of state: the ratio of a fluid's pressure to its energy density; its value over time is what DESI measures.
- DESI: a large spectroscopic survey mapping galaxy positions and distances to trace expansion history.
- General relativity and averaging: Einstein's theory of gravity; averaging the Einstein equations over lumpy matter yields extra effective terms that can mimic dark energy.
- Morphon: an effective scalar-field analogy for inhomogeneities, used here as a mean-field description, not a known particle.
- Phantom behaviour: an effective equation of state below -1, which the text says arises without violating energy conditions.
- Closure condition: an extra relation needed to make the averaged equations solvable.
- Flow-orthogonal foliation: a way of slicing spacetime along the matter flow, used as the framework's coordinate choice. · level: research-level

<details><summary>Original abstract</summary>

We benchmark the hypothesis that the redshift dependence of postulated dark energy in the standard model, measured by the DESI collaboration, is a natural outcome of dark energy-free models of structure formation in general relativity. We recall fundamental results and the properties of averaged dust cosmologies that suggest to replace the dark energy equation of state through the nonperturbative impact of the inhomogeneous geometry. The relevant mechanism can be phrased in terms of an effective mean field description of inhomogeneities using the fluid analogy of a scalar field (the `morphon'). Without violating energy conditions this effective field exhibits a cross-over to phantom behaviour, compatible with observations. The exact dark energy-free framework needs a single closure condition that we implement in terms of parametrizations of the 3-years data of the DESI team. The resulting redshift dependence of effective cosmological characteristics is then illustrated and subject to physical interpretation. The aim of this paper is to set a benchmark that has to be met by any structure formation model or simulation investigated within general relativity in a flow-orthogonal foliation of spacetime, given the hypothesis.

</details>

## Galaxies

### [On the effect of a redshift- and metallicity-dependent top-heavy IMF on high-redshift UV luminosity functions](https://arxiv.org/abs/2611.31148)
*Keita Fukushima, Shuya Kitagawa, Akio K. Inoue et al.* · `astro-ph.GA` · arXiv:2611.31148v1 · relevance 0.14

- **In one sentence**: A semi-analytic galaxy model with redshift- and metallicity-dependent top-heavy stellar initial mass functions (IMFs) is used to test whether such IMFs can explain the excess of bright high-redshift galaxies seen by JWST, with dust attenuation included and calibrated at z=7.
- **In plain words**: Telescopes like JWST have found more very bright galaxies in the early universe, roughly 13 billion years ago, than standard models predicted. One proposed explanation is that the first stars formed with a different mix of masses, skewed toward heavier stars that shine more brightly. The authors built star-light templates for this scenario, put them into a galaxy simulation, and checked how the predicted brightness counts change once dust and metal enrichment are included.
- **Why it matters**: This tests whether a change in how stars form could account for the JWST bright-galaxy excess, a question still open in the field. The text indicates the answer depends on dust: without dust the top-heavy IMF strongly boosts bright galaxies, but with dust included the effect is partly offset, and the model fits z~10 data but not z≳12.
- **Background needed**: - Initial mass function (IMF): the distribution of stellar masses formed in a star-forming event; a "top-heavy" IMF produces more massive stars, which are much brighter in ultraviolet light.
- UV luminosity function (UVLF): the number of galaxies per volume at each ultraviolet brightness; the main observable being compared.
- Redshift (z): a measure of distance and lookback time; higher z means earlier in the universe. z~10 corresponds to roughly 470 million years after the Big Bang.
- Metallicity: the fraction of elements heavier than helium in gas and stars; low metallicity is typical of early galaxies.
- Dust attenuation: dimming of starlight by interstellar dust, which absorbs ultraviolet light.
- Semi-analytic model: a galaxy formation model using simplified physical recipes run on top of an N-body (dark matter) simulation.
- Star formation rate (SFR) conversion: the factor linking observed UV brightness to how fast a galaxy is forming stars; the paper finds this factor scatters more under the top-heavy IMF. · level: research-level

<details><summary>Original abstract</summary>

JWST observations have revealed a higher-than-expected abundance of bright galaxies at $z \gtrsim 10$. Several scenarios have been proposed to explain this excess, one of which invokes a top-heavy stellar initial mass function (IMF) in the early Universe. In this work, we construct spectral energy distribution (SED) templates based on a redshift- and metallicity-dependent IMF ($z$-$Z$ dependent IMF) motivated by the star-cluster simulations of Chon et al. (2022) and the redshift-dependent IMF model of Steinhardt et al. (2020). We implement these templates in a semi-analytic galaxy model built on a large-box $N$-body simulation to investigate the impact of a top-heavy IMF on the ultraviolet luminosity function (UVLF) of high-redshift galaxies. The adopted $z$-$Z$ dependent IMF enhances the UV luminosity of young stellar populations, particularly at low metallicity, and increases the scatter in the UV luminosity-to-star formation rate conversion factor relative to the Kroupa IMF. Without dust attenuation, both top-heavy IMF models predict a substantially enhanced bright end of the UVLF. However, when dust attenuation is included and calibrated at $z=7$, IMF-dependent metal enrichment and the resulting dust attenuation partly offset the intrinsic UV enhancement. The self-consistent model broadly reproduces the observed UVLF at $z\sim10$, although discrepancies remain at $z\gtrsim12$. For the selected high-redshift UVLF constraints, the best-fitting dust optical depths are 51% and 21% of the fiducial values at $z=9.7$ and $13.04$, respectively, indicating a preference for weaker effective dust attenuation. The highest-redshift comparison does not provide a robust constraint. Our results highlight the importance of accounting for both enhanced stellar UV emission and IMF-dependent metal enrichment and dust attenuation when assessing the impact of a top-heavy IMF on high-redshift galaxies.

</details>

### [Outflows and Young Stars in the Auriga-California Giant Molecular Cloud](https://arxiv.org/abs/2611.29408)
*T. A. Movsessian, T. Yu. Magakian* · `astro-ph.GA` · arXiv:2611.29408v1 · relevance 0.12

- **In one sentence**: A survey of the Auriga-California Molecular Cloud using narrowband H-alpha and [SII] imaging, slitless spectroscopy, and Spitzer/WISE infrared data that reports seven new Herbig-Haro objects, candidate H2 outflows, H-alpha emitting stars, and reflection-nebula stars concentrated along the cloud's northern dark filament.
- **In plain words**: This paper looks for signs of newly forming stars in a nearby cloud of gas and dust in the Auriga-California region. Young stars in such clouds throw out jets of glowing gas and streams of hot hydrogen, and the authors used telescope images and infrared archives to find these traces. They report seven new glowing gas knots (Herbig-Haro objects), several outflows, and lists of young stars, and find that most of them lie along the northern dark filament of the cloud.
- **Why it matters**: The work maps where stars are currently forming in a moderately active nearby cloud, which helps show how star formation is distributed within a single cloud. The authors suggest the outflows are mostly driven by deeply embedded very young stars, but the text does not give further tests of that idea.
- **Background needed**: - Molecular cloud: a cold, dense cloud of gas and dust where stars form.
- Young stellar object (YSO): a star still gathering material; Class 0/I means the youngest stage, still hidden in its dust cocoon.
- Outflow: jets and winds blown out from young stars, which can be seen in glowing gas.
- Herbig-Haro (HH) object: a small knot of glowing gas where such a jet hits surrounding material.
- H-alpha and [SII]: specific colors of light emitted by hot hydrogen and sulfur, used to spot shocks and jets.
- H2 (molecular hydrogen): a gas whose infrared glow traces shocked outflows.
- Reflection nebula: dust that scatters starlight, often lit around young stars.
- Narrowband imaging and slitless spectroscopy: observing only a narrow band of colors, or spreading light without a slit, to find emitting objects. · level: intermediate

<details><summary>Original abstract</summary>

The Auriga-California Molecular Cloud (AMC) is a nearby star-forming region with a moderate level of star formation activity. Previous infrared surveys have shown that its young stellar population is concentrated along a dense filament extending north of NGC 1579. We searched for new manifestations of ongoing star formation in the AMC by identifying optical and molecular outflows, H{\alpha} emission-line stars, and young stars associated with reflection nebulae. Narrowband H{\alpha} and [SII] imaging, together with slitless spectroscopy, were obtained with the 1-m Schmidt telescope of the Byurakan Observatory. The optical data were complemented by near-infrared images from the Spitzer Enhanced Imaging Products (SEIP) and by WISE/unWISE archival data. We discovered seven new Herbig-Haro (HH) objects and outflows associated with several young stellar objects, including deeply embedded infrared sources and stars surrounded by compact reflection nebulae. Nearly all of the optical HH objects have molecular hydrogen counterparts, and several additional candidate H2 outflows without optical counterparts were identified. Particularly noteworthy is a compact region around V347 Per that appears to host at least three molecular outflows. We also present a list of newly identified H{\alpha} emission-line stars and a catalogue of stars associated with optical reflection nebulae. Both populations are concentrated primarily along the northern dark filament of the cloud. The spatial distribution of the newly identified HH objects, molecular outflows, emission-line stars, and nebulous young stars confirms that the northern filament is the principal site of ongoing star formation in the AMC. The close correspondence between the optical and molecular outflowsfurther suggests that most of their driving sources are deeply embedded Class 0/I young stellar objects.

</details>

## Exoplanets and planetary science

### [Updated View on Titan's Habitability: Interior and Surface Aqueous Environments](https://arxiv.org/abs/2611.28186)
*Diogo Gon\c{c}alves, L\'igia F. Coelho, Catarina Miranda et al.* · `astro-ph.EP` · arXiv:2611.28186v1 · relevance 0.10

- **In one sentence**: A review of Titan's three possible water-bearing settings (its interior ocean, cryovolcanic flows, and impact-melt pools) that assesses their prebiotic potential and bottlenecks ahead of NASA's Dragonfly mission.
- **In plain words**: This paper looks at Saturn's moon Titan, where carbon-rich chemicals and liquid water may meet, and asks where the conditions for life's chemical building blocks could exist. The authors survey three places: the water layer beneath the surface, possible lava-like flows that erupt cold and contain water mixed with ammonia, and pools of melted rock left by meteorite impacts. For each, they list what helps the chemistry along and what limits it.
- **Why it matters**: It sets out what is known and what is still uncertain before NASA's Dragonfly rotorcraft arrives at Titan, so it may help shape which measurements are most useful. The text itself is a summary of the state of knowledge and does not report new measurements, so its weight depends on how well the cited evidence holds up.
- **Background needed**: - Titan: Saturn's largest moon, with a thick nitrogen atmosphere and lakes of liquid methane on its surface.
- Prebiotic chemistry: chemistry that produces the molecules (such as amino acids and sugars) that came before life, not life itself.
- Organic molecules: carbon-based compounds; they are common on Titan.
- Hydrosphere: the water layer of a planet or moon; on Titan it is thought to lie under an icy shell.
- Ammonia: acts like antifreeze, lowering the freezing point of water, which is why it matters for how long liquid lasts.
- Cryovolcanism: volcanic-like eruptions of icy or liquid material instead of molten rock.
- Impact-melt pool: a pool of rock melted by a meteorite strike, which can stay warm for a long time.
- Dragonfly: a NASA mission planned to fly a drone-like vehicle across Titan's surface to sample its chemistry. · level: intermediate

<details><summary>Original abstract</summary>

Saturn's moon Titan is the only world beyond Earth where abundant organic molecules and liquid water are expected to interact. Crucially, these interactions yield prebiotic molecules central to terrestrial biochemistry. Characterizing this prebiotic chemistry is one of the main science goals of NASA's upcoming Dragonfly mission. Here we synthesize the current state of knowledge on the habitability and prebiotic potential of Titan's three aqueous settings: its interior hydrosphere, its putative cryovolcanic flows, and its impact-melt pools. For each setting, we identify the enabling factors and the principal bottlenecks that limit prebiotic complexification. Titan's interior is likely pervaded by liquid water in contact with organic material delivered from the surface and released from the core, though the longevity of its liquid water has recently been called into question. Cryovolcanic regions transiently expose surface organics to ammonia-bearing aqueous melts but are constrained by short freezing timescales. Impact-melt pools, by contrast, are warm and long-lived environments whose prebiotic chemistry is limited by the scarcity of ammonia. Dragonfly will return ground-truth data not only for Titan's habitability, but also for organic-rich aqueous environments across the Solar System and beyond. The years before its arrival are the last in which predictive work can still shape Dragonfly's investigations.

</details>

### [Probabilistic, facility-specific prioritisation of temperate exoplanets for atmospheric characterisation with JWST and the ELT](https://arxiv.org/abs/2611.31181)
*Effy Viridis* · `astro-ph.EP` · arXiv:2611.31181v1 · relevance 0.08

- **In one sentence**: A public Monte Carlo framework (UHI v6.1) builds facility-specific, probabilistic priority lists of 6,112 NASA-catalogued planets for JWST transit and ELT reflected-light characterisation, with global sensitivity analysis showing the XUV shoreline dominates rocky-planet rankings and Hycean-planet results are only indicative.
- **In plain words**: The paper asks which temperate planets outside our solar system are the best first targets for the next large telescopes to study their atmospheres, given that many candidates may have lost their air to stellar radiation. The authors ran 10,000 randomized simulations per planet, varying the uncertain catalogue measurements and modelling assumptions, to estimate how likely each planet is to survive and to rank highly. They report 255 rocky and 71 Hycean (water-ocean-covered) candidates that remain detectable at 5 sigma, a statistical confidence threshold.
- **Why it matters**: Telescope time on JWST and the future Extremely Large Telescope (ELT) is scarce, so a transparent way to rank targets matters for planning observations. The sensitivity analysis is useful because it shows which assumptions most change the rankings, which helps observers judge where to focus. The text does not show how well the rankings will match what the telescopes actually find.
- **Background needed**: - Transit spectroscopy: measuring starlight filtered through a planet's atmosphere as it passes in front of its star (JWST); reflected-light imaging of non-transiting planets (ELT).
- Temperate planet: one whose surface temperature could allow liquid water.
- Hycean planet: a hypothetical water-ocean world with a hydrogen-rich atmosphere.
- XUV shoreline: the boundary in stellar X-ray and extreme-UV flux above which a planet is likely to lose its atmosphere.
- Monte Carlo: repeated random sampling of uncertain inputs to see the spread of outcomes.
- Sobol indices: a sensitivity measure giving how much each assumption contributes to output variation; total-order indices include interactions.
- Signal-to-noise / sigma: how confidently a detection stands out from noise; 5 sigma is a stricter threshold than 3 sigma. · level: research-level

<details><summary>Original abstract</summary>

Deciding which temperate exoplanets to observe first matters for JWST transit spectroscopy and for planned ELT reflected-light instruments, yet signal-to-noise metrics ignore habitability and similarity indices ignore observability. We present an open Monte Carlo framework (UHI v6.1) that builds probabilistic priority lists separately for each facility and composition class, never as a single ranking. For each of 6,112 planets in the NASA Exoplanet Archive, 10,000 draws carry catalogue uncertainties through climate, cumulative stellar-XUV atmospheric retention, per-draw rocky, Hycean or gas-rich classes, and a JWST (transiting) or ELT/PCS (non-transiting) detection model, giving each planet a survival probability, a conditional score and a top-N probability. At $5\sigma$, 255 rocky and 71 Hycean candidates remain viable. A Saltelli--Sobol analysis of 32 assumptions ($N = 512$) shows that the location and width of the XUV shoreline dominate the rocky lists, with total-order indices of 0.22 and 0.12 at $5\sigma$ (0.25 and 0.14 at $3\sigma$), and all ten leading indices have 95% bootstrap half-widths below 0.05. For Hycean planets most outputs are degenerate and the analysis does not converge, so that branch is reported as indicative. Membership of these lists is limited mainly by whether a planet survives the habitability vetoes: at $5\sigma$, 3 of the nominal JWST and 4 of the nominal ELT rocky top-10 targets enter the top 10 in at least half of all draws, yet every one of them stays in the top 10 in more than half of the draws in which it survives. Code, per-planet posterior summaries, sensitivity tables and maps are public, so observers can rerun the lists under their own instrument assumptions and see which inputs would most change a target's priority.

</details>

## High-energy astrophysics

### [Tidal effects of bulk viscosity in neutron stars](https://arxiv.org/abs/2611.30454)
*A. Kanakis-Pegios, P. S. Koliogiannis, Ch. C. Moustakidis* · `astro-ph.HE` · arXiv:2611.30454v1 · relevance 0.18

- **In one sentence**: A study of how bulk viscosity from direct Urca neutrino reactions in neutron-star matter adds tidal dissipation, using an effective volume-averaged viscosity, with lag time and dissipative deformability reported versus temperature and compactness for 1.4 solar-mass and maximum-mass stars.
- **In plain words**: Neutron stars are extremely dense stellar remnants, and when two orbit each other they stretch and squeeze one another via tides. This paper asks how the internal friction of the star's matter, called bulk viscosity, changes that tidal stretching by turning some of the motion into heat. The authors model the effect at temperatures up to a few MeV, and they report that it peaks at a temperature close to where the viscosity itself is largest.
- **Why it matters**: Tidal effects are what gravitational-wave detectors use to learn about neutron-star interiors during binary inspirals, so a dissipative signature could in principle be a probe of the matter. The text does not establish whether such effects are large enough to be detected, and it only gives causality-based upper bounds as benchmarks.
- **Background needed**: - Neutron star: a collapsed star roughly 1.4 times the Sun's mass squeezed into about 20 km across.
- Tides: the gravitational stretching one body causes on another; the stretch lags slightly when the star's matter dissipates energy.
- Bulk viscosity: resistance of dense matter to being compressed and expanded out of balance; it converts motion into heat.
- Direct Urca process: a fast neutrino-emitting reaction that restores chemical balance between neutrons, protons and electrons.
- Equation of state: the rule relating pressure, density and composition of the star's matter.
- Compactness: mass divided by radius, a measure of how strongly gravity compresses the star.
- Lag time and dissipative deformability: measures of how far and how late the tidal bulge trails the orbit, and the energy-loss-related tidal response.
- Neutrino-transparent regime: conditions where neutrinos escape the star freely. · level: research-level

<details><summary>Original abstract</summary>

Bulk viscosity in neutron-star matter provides a temperature-dependent mechanism for tidal dissipation. In this study, we investigate the impact of bulk viscosity on the dissipative tidal response of neutron stars composed of neutrons, protons, and electrons. Employing cold equations of state derived through the momentum-dependent interaction model, we examine the bulk viscosity arising from the direct Urca process, which acts to restore chemical equilibrium. The temperature dependence is incorporated through the weak-interaction rate, allowing us to explore the behavior of bulk viscosity in the neutrino-transparent regime at temperatures up to a few MeV. To account for the spatial distribution of bulk viscosity within neutron stars, we introduce the effective bulk viscosity, a volume-averaged quantity over the region where direct Urca process operates, and establish a connection with the bulk viscosity. Specifically, we investigate its implications for tidal quantities, including the lag time and dissipative deformability, highlighting their dependence on temperature and stellar compactness. We find that the dissipative tidal effects become maximal at a temperature approximately coinciding with the one of maximum bulk viscosity on the onset of direct Urca. Additionally, these effects are more pronounced in intermediate neutron star masses compared to maximum ones. Finally, for both canonical $1.4\;M_\odot$ and maximum-mass neutron star configurations, we derive causality-based upper bounds on these quantities, providing theoretical benchmarks for assessing the potential observability of bulk-viscous effects in gravitational-wave signals from binary neutron star inspirals.

</details>

### [Fast Radio Bursts Co-detected by CHIME/FRB and DSA-110 from 400 to 1530 MHz](https://arxiv.org/abs/2611.28250)
*S. K. Ocker, K. Nimmo, J. Faber et al.* · `astro-ph.HE` · arXiv:2611.28250v1 · relevance 0.18

- **In one sentence**: A sample of 15 fast radio bursts detected by both the CHIME/FRB and DSA-110 telescopes (12 with channelized voltage data, 9 with secure redshifts) is used to study spectral shape, scattering, and selection effects across 400 to 1530 MHz.
- **In plain words**: Fast radio bursts are brief, very bright flashes of radio waves from distant galaxies. This paper looks at 15 of them that were caught by two different radio telescope systems, which together cover a wide range of radio frequencies. The authors compare how the bursts' energy and brightness change across that range, and how their signals are smeared out as they travel.
- **Why it matters**: Few bursts have been seen across more than one gigahertz of radio spectrum, so this sample helps test how bursts emit and how their signals are scattered on the way to us. The paper reports that the two telescopes appear to pick out different subsets of bursts, which matters for interpreting survey results and designing future wide-band surveys; the broader physical implications are not established by the text.
- **Background needed**: - Fast radio bursts (FRBs): millisecond-long radio flashes of unknown origin, mostly from other galaxies.
- Redshift: a measure of distance, inferred from how much a source's light is stretched on the way to Earth; "secure" means the host galaxy was identified reliably.
- Repeating vs. non-repeating: some FRBs flash again; most reported here have not been seen to repeat.
- MHz/GHz: units of radio frequency; CHIME observes 400 to 800 MHz and DSA-110 observes 1280 to 1530 MHz.
- Spectral index and spectral turnover: describe how a burst's brightness changes with frequency, and whether it peaks at some frequency.
- Pulse broadening and scintillation: scattering by intervening plasma stretches a pulse in time and causes twinkling in frequency, like starlight shimmering.
- Selection effect: a bias in which objects a survey is able to detect.
- Pulsars and magnetars: rotating neutron stars; some show spectra peaking near a gigahertz, which the paper compares to certain bursts. · level: research-level

<details><summary>Original abstract</summary>

We present a sample of $15$ fast radio bursts (FRBs) that were co-detected by the Deep Synoptic Array (DSA-110) and the Canadian Hydrogen Intensity Mapping Experiment (CHIME) between 2022 and 2024, of which $12$ have channelized voltage data from both instruments and 9 have secure redshifts. All but one are as-yet-non-repeating. Most bursts span the entire bandwidth of each instrument (400-800 MHz for CHIME, 1280-1530 MHz for DSA-110), significantly expanding the number of FRBs known to emit across $>1$ GHz of spectral bandwidth and constraining the spectral evolution of energy and propagation effects. On average, the FRBs exhibit higher spectral energies (up to a factor of $\sim10$) in the CHIME band but are lower in peak flux density due to substantial pulse broadening. The sample mean (median) spectral index $-0.4\pm0.4$ ($-0.3\pm0.4$) is shallower than previously reported spectral indices, likely a selection effect. A third of the sample shows evidence for a spectral turnover, comparable to that seen in GHz-peaked pulsar and magnetar spectra. Joint scintillation and pulse broadening constraints indicate that nearly all bursts encounter multiple scattering screens, with pulse broadening originating within their host galaxies. The co-detected bursts are among the most scattered in the CHIME/FRB sample, while being the narrowest in the DSA-110 sample, indicating that CHIME/FRB and DSA-110 select different subsets of the FRB population; the interplay between intrinsic burst width, scattering, and the FRB search time resolution creates a narrow window of sensitivity to co-detected FRBs, providing a blueprint for future ultra-wideband FRB surveys.

</details>

## Stars and the Sun

### [Asteroseismic investigation of intermediate age open star cluster NGC 2126](https://arxiv.org/abs/2611.29291)
*Athul Dileep, Santosh Joshi, Patricia Lampens et al.* · `astro-ph.SR` · arXiv:2611.29291v1 · relevance 0.11

- **In one sentence**: A preliminary asteroseismic study of delta Scuti pulsators and the binary V551 Aur in the intermediate-age open cluster NGC 2126, using TESS and ground-based photometry, with tentative mode identifications and a spectroscopic search for chemical peculiarities.
- **In plain words**: This paper studies a group of pulsating stars that belong to NGC 2126, a cluster of stars born together roughly a few hundred million to a billion years ago. The stars pulse, like a bell ringing, and the authors use the rhythm and brightness of those pulses to guess which vibration patterns they are showing. They report tentative matches for three stars and a firmer match for one, and they also find that one star's pulsations change as it orbits its partner in a binary system.
- **Why it matters**: Pulsations act like a stethoscope on a star's interior, so matching them to models can constrain stellar ages and structure. The authors call the work preliminary, and the identifications are described as tentative, so it is best read as a progress report rather than a settled result.
- **Background needed**: - Open star cluster: a loose group of stars formed from the same cloud at about the same time.
- Delta Scuti star: a type of pulsating star that swells and shrinks, changing brightness on timescales of hours.
- Asteroseismology: inferring a star's interior and properties from the frequencies of its oscillations, much like geologists use seismic waves.
- Radial mode / overtone: a pulsation in which the star expands and contracts uniformly; overtones are versions with more nodes in the pattern.
- TESS: a NASA space telescope that monitors large areas of sky for brightness changes.
- Eclipsing binary: two stars orbiting so that they periodically pass in front of each other, dimming the light.
- Am star: a star with unusual surface chemistry, with some metals appearing stronger than normal.
- The paper finds the fundamental radial mode fails to fit unless the star is much brighter than observed, so that mode is ruled out in this analysis. · level: research-level

<details><summary>Original abstract</summary>

We present a preliminary asteroseismic investigation of the pulsating stars in the intermediate-age open cluster NGC 2126. The TESS Full Frame Images and ground-based photometry from the previous study, Dileep et al. (2025), were used to identify the pulsation modes of {\delta} Scuti member stars using period-luminosity relations and pulsation modelling. Our analysis resulted in a tentative identification up to the first radial overtone in stars N1, N2 and ZV1. Additionally, the second radial overtone was secured in N1. The disentangled pulsation and eclipse light curves of the binary star V551 Aur (V6) from our previous research were employed to study pulsation amplitude and phase modulations across the orbital period. The primary component of V6 exhibits pulsations showing amplitude and phase modulations, indicating tidal influence on the oscillations. Modelling the pulsation as the fundamental radial mode reveals that in order for the mode to be radial, the star must be significantly brighter than observed. Hence, the mode is not the fundamental radial mode or the overtones. Low-resolution spectroscopy was used to search for chemical peculiarities in the pulsating members, and we found that star ID 143 has features similar to an Am star.

</details>

### [Empirical Mass and Radius Relations for Main-sequence Stars from Detached Eclipsing Binaries](https://arxiv.org/abs/2611.28229)
*D. M. Rowan, C. S. Kochanek* · `astro-ph.SR` · arXiv:2611.28229v1 · relevance 0.06

- **In one sentence**: Empirical polynomial relations linking spectroscopic parameters (temperature, surface gravity, metallicity) to masses and radii of main-sequence stars, calibrated on 605 stars in detached eclipsing binaries, with comparisons to MIST and PARSEC stellar models.
- **In plain words**: Astronomers want to know how big and how heavy a star is, but the most direct way needs a pair of stars orbiting and eclipsing each other. This paper uses about 605 such star pairs as reference points to build formulas that estimate a star's mass and radius from measurements of its light spectrum, such as its temperature and composition. The authors report that an eight-term formula matches the reference stars to within about 4% in radius and about 8% in mass, and they give a predicted mass and radius for the Sun.
- **Why it matters**: Mass and radius estimates feed into work on stellar evolution and on exoplanets, since a planet's size and mass depend on its host star's. The paper also reports that two widely used stellar model sets differ systematically from the observations, with hot stars' radii overestimated and cool stars' underestimated, which may matter for those models' users; the text does not say how much these offsets would change any particular result.
- **Background needed**: - Detached eclipsing binary: two stars orbiting each other, passing in front of one another without touching; their light dips reveal their sizes and masses precisely.
- Main-sequence star: a star in the stable, hydrogen-burning phase of its life, like the Sun.
- Effective temperature and surface gravity: the surface temperature of a star and how strongly gravity pulls on its surface; these are measured from spectra.
- Metallicity: the fraction of elements heavier than helium in a star, a measure of its chemical composition.
- Empirical relation: a formula fitted to observed data rather than derived from physical theory.
- RMS scatter and dex: the typical spread of the fit errors; a dex is a logarithmic unit, where 0.016 dex is about 3.8%.
- Stellar models (MIST, PARSEC): computer-calculated predictions of how stars evolve, used as theoretical comparisons. · level: research-level

<details><summary>Original abstract</summary>

Detached eclipsing binaries have long served as fundamental calibrators for stellar models because they provide precise measurements of stellar masses and radii. Given a sample of detached eclipsing binaries, we can derive empirical relations between spectroscopic parameters (effective temperatures, surface gravities and abundances) and stellar masses and radii. We use a sample of 605 stars (330 with metallicities) in detached eclipsing binaries to update and refine these empirical models for main-sequence stars. An eight-term polynomial model reproduces the radii and masses of the eclipsing binary calibrators with an RMS scatter of $\sigma_{\log R} = 0.0161$ dex (3.8%) and $\sigma_{\log M} = 0.0322$ dex (7.7%), respectively. Most of this scatter is explained by the parameter uncertainties - the estimated intrinsic scatters in the radius and mass are only $\sigma_{\rm int}=0.0085$ and $0.017$ dex (2.0% and 4.0%). The predicted mass and radius of the Sun are $(1.028\pm0.004)\ M_\odot$ and $(1.014\pm0.002)\ R_\odot$. A 14-term model, while formally preferred, explains little more of the intrinsic scatter. We additionally provide the equivalent relations in terms of the mean stellar density instead of the surface gravity for use with exoplanet host stars. If we compare the 8-term model to MIST and PARSEC model stars with closely matched spectroscopic parameters, we find systematic differences. For example, the radii of hot (cool) stars are systematically over- (under-)estimated in both models by several percent.

</details>

## Chemical physics

### [An equivariant classical density functional for ionic fluids at complex interfaces](https://arxiv.org/abs/2611.28501)
*Bingqing Cheng* · `physics.chem-ph` · arXiv:2611.28501v1 · relevance 0.13

- **In one sentence**: A machine-learned classical density functional for ionic fluids, with a symmetry-adapted neural term for short-range correlations plus explicit long-range Coulomb electrostatics, is shown to reproduce ionic structure, mean forces, electrode charging and charging dynamics near complex charged solutes and atomically structured metal electrodes.
- **In plain words**: The paper concerns how salt ions crowd and arrange themselves next to irregularly shaped charged surfaces, such as electrodes with steps and bumps, which matters for batteries and supercapacitors. The authors built a single learned model, trained on simulated ion densities and bulk correlations, that predicts these arrangements without running full atomistic simulations at each geometry. According to the text, it matches molecular dynamics results for ion structure and forces, and with separately measured ion mobilities it also captures the main features of how the electrode charges over time.
- **Why it matters**: Atomistic simulations of ions at electrodes are expensive, so a fast functional that transfers across geometries could make it practical to screen how composition and surface shape affect capacitance. The text presents this as a framework that could be extended to more complex ionic fluids, but the broader applicability has not been shown here.
- **Background needed**: - Classical density functional theory: a method that predicts the average density of particles near a surface by minimizing a free-energy functional, instead of tracking each particle.
- Restricted primitive model: a simplified model of salt where ions are charged hard spheres in a uniform background solvent.
- Long-range electrostatics (Coulomb interactions): forces that fall off slowly with distance, so they must be treated explicitly rather than cut off.
- Equivariance/symmetry-adapted models: neural networks built so their predictions rotate consistently with the geometry they describe.
- Molecular dynamics: computer simulation of atoms or ions moving under physical forces, used here as the reference.
- Electrode capacitance: how much charge an electrode stores per unit voltage; charging dynamics describe how fast this happens. · level: research-level

<details><summary>Original abstract</summary>

Predicting the combined effects of ionic packing and long-range electrostatics at complex interfaces is technologically important, but remains challenging without atomistic simulations. Here we present a machine-learned classical density functional for ionic fluids that combines a symmetry-adapted neural free energy for short-range correlations with explicit long-range electrostatics. Trained on three-dimensional equilibrium densities and bulk correlations of the full-Coulomb restricted primitive model, a single functional transfers to charge-patterned particles and atomically structured electrodes. Around anisotropic charged solutes, it reproduces the ionic structure and mean forces from molecular dynamics, including reversals of the bare electrostatic force. At metal electrodes, self-consistent coupling to metal atoms captures the redistribution of ionic and electrode charge and the loading-dependent capacitance enhancement produced by steps and bumps. Combined with mobilities determined independently from bulk molecular dynamics, the same functional describes the main features of charging dynamics and resolves geometry-dependent spatial relaxation. This framework can be extended to more complex ionic fluids, enabling efficient exploration of how composition and geometry control structure and response.

</details>

### [An informational interpretation of the reverse nonequilibrium molecular dynamics](https://arxiv.org/abs/2611.29174)
*Yuxing Jiao, Mingcheng Yang* · `cond-mat.stat-mech` · arXiv:2611.29174v1 · relevance 0.12

- **In one sentence**: The paper gives an information-thermodynamic reading of reverse nonequilibrium molecular dynamics (RNEMD), a simulation method for self-diffusivity, treating its Maxwell-demon-like exchange step as an information reservoir that drives a diffusive flux, and derives the linear transport coefficient, an entropy production fluctuation theorem and a thermodynamic uncertainty relation for it.
- **In plain words**: Computer simulations of molecules often need to measure how fast things spread or flow, such as how quickly particles diffuse through a liquid. One fast method, reverse nonequilibrium molecular dynamics, pushes particles between regions in an artificial way, which looks like it reverses the usual cause-and-effect between a driving gradient and the flow it produces. This paper explains that method using ideas from information thermodynamics, where the artificial exchange acts like a sorting demon that works from a reservoir of information. The authors report that the statistical bias in this information reservoir sustains a concentration gradient and a steady diffusive flow, and they check the theory with simulations.
- **Why it matters**: The work tries to give a physical foundation to a simulation shortcut that has so far been justified mainly by its practical success. Its links to fluctuation theorems and uncertainty relations suggest it may connect simulation methods with the wider thermodynamics of small systems, though the text does not show how far these ideas extend beyond the self-diffusion case studied.
- **Background needed**: - Transport coefficient: a number describing how readily a quantity (particles, heat, momentum) flows under a gradient; self-diffusivity is one such number.
- Molecular dynamics: computer simulation that tracks the motion of individual atoms or molecules over time.
- Nonequilibrium steady state: a system kept in a constant flow, so its properties stay the same over time but it is not at rest.
- Force-flux causality: the usual view that a gradient (the driving force) causes a flow; RNEMD appears to invert this.
- Maxwell demon and information thermodynamics: a thought experiment in which a sorting agent uses information to move particles against a gradient; the field studies how information is paid for in energy and entropy.
- Entropy production: a measure of irreversibility, the heat-like cost of keeping a system out of equilibrium.
- Fluctuation theorem and thermodynamic uncertainty relation: results saying how likely entropy-decreasing fluctuations are, and that more precise flows cost more entropy production.
- Large deviation functional: a mathematical tool describing the probabilities of rare fluctuations in averages. · level: research-level

<details><summary>Original abstract</summary>

Reverse nonequilibrium molecular dynamics (RNEMD) is an efficient simulation method for determining transport coefficients. In this method, a flux is imposed by a seemingly artificial nonlocal exchange operation and the corresponding thermodynamic gradient is induced as a result, apparently reversing the usual force-flux causality. Although this method is well studied as a simulation technique, developing an information-thermodynamic interpretation of its Maxwell-demon-type operation and the associated apparent reversal of force-flux causality would provide a solid physical foundation for algorithms of this type. Here, we develop an information-reservoir interpretation for a representative RNEMD scheme for determining self-diffusivity. We show that the statistical bias of the information reservoir defines an information affinity that sustains a concentration gradient and a diffusive flux in the steady state. We further derive the linear transport coefficient corresponding to the information affinity in the linear response regime. Using the large deviation functional for the steady-state densities and currents, we also establish a fluctuation theorem for entropy production and the thermodynamic uncertainty relation linking entropy production to the fluctuations of the particle current. Computer simulations are performed to corroborate our theoretical results.

</details>

## Materials science

### [DeepDOSReasoner: Physics-Grounded Reasoning for Density-of-States Prediction and Materials Discovery](https://arxiv.org/abs/2611.29132)
*Yingheng Wang, Francesco Ricci, Zhilong Wang et al.* · `cond-mat.mtrl-sci` · arXiv:2611.29132v1 · relevance 0.12

- **In one sentence**: DeepDOSReasoner is a machine-learning model that predicts electronic and phonon densities of states directly from crystal structure, using source attention and a continuity-equation transport step that enforces nonnegativity and total-state conservation, and it reports a prospective screen of 8,106 materials checked by new DFT calculations.
- **In plain words**: Materials scientists want to know how a material's electrons and vibrations are spread across energy levels, but computing this with a standard quantum simulation is slow, and many materials in a major database lack it. This paper describes a model that predicts these energy spectra from a material's atomic arrangement, and it is built to respect basic bookkeeping rules, such as the total number of states being conserved. The authors report that it was the most accurate of the methods they compared, and that its top candidates were often confirmed by new simulations.
- **Why it matters**: Spectra like these determine properties such as conductivity, optical response and heat capacity, so fast predictions could let researchers screen many more candidate materials before running expensive calculations. The text does not show how well the predictions transfer to real laboratory measurements or to materials far outside the training data, so the practical impact remains to be tested.
- **Background needed**: - Density of states (DOS): a curve showing how many energy levels a material has at each energy; it determines many electronic and thermal properties.
- eDOS and phDOS: the electronic DOS (for electrons) and phonon DOS (for lattice vibrations).
- Density functional theory (DFT): a standard, computationally costly quantum-mechanical method for estimating material properties from atomic structure.
- Materials Project: a public database of computed materials properties.
- Valence-band gap: an energy window in the electron spectrum relevant to whether a material conducts or insulates and to its optical behavior.
- Attention and continuity equations: machine-learning and physics tools; here, the model links atoms to energy levels, then adjusts the spectrum like conserved flow.
- Ablation and held-out testing: checking which model parts matter and how it performs on unseen data. · level: research-level

<details><summary>Original abstract</summary>

Predicting a material's behavior from its atomic structure is a longstanding goal of the physical sciences. The electronic and phonon densities of states (eDOS and phDOS) govern key electronic, optical, vibrational, and thermodynamic properties, yet their calculation using density functional theory (DFT) is costly: about 60% of Materials Project entries lack eDOS and over 80% lack phDOS. Existing crystal-to-spectrum models rely on pooled structural representations and pointwise regression, which blur spectral features and violate total-state conservation. Here we introduce DeepDOSReasoner, a physics-grounded framework that decodes spectra through atom-to-energy source attention and refines the normalized DOS through learned continuity-equation transport, enforcing nonnegativity and total-state conservation by construction. DeepDOSReasoner achieves the highest prediction accuracy across all evaluated metrics for both eDOS and phDOS, recovers element-resolved contributions without supervision, and most reliably identifies rare valence-band (VB) gaps. In a prospective screen of 8,106 uncharted materials validated by new DFT calculations, its predictions remain the most accurate among the methods evaluated, with 25 of its top 50 candidates confirmed as VB-gap materials. Three case studies spanning substituted compounds, photovoltaic chalcogenides, and a high-entropy alloy demonstrate transfer across materials classes. Ablations confirm that both stages are necessary, while the model retains comparable accuracy when trained on only 25% of the data. Predicting spectra in milliseconds enables exhaustive screening; we release predictions filling the missing eDOS for 91,405 and phDOS for 127,768 Materials Project entries. DeepDOSReasoner provides a blueprint for integrating machine learning with physical reasoning toward high-throughput spectral screening and autonomous materials discovery.

</details>

### [Diagnostic Accuracy Is Not Deployment Value: Decision-Aligned Reliability Evaluation for Foundation MLIPs in Materials Discovery](https://arxiv.org/abs/2611.30066)
*Harry Sevi, Joonatan E. M. Laulainen* · `cs.LG` · arXiv:2611.30066v1 · relevance 0.12

- **In one sentence**: The paper argues that standard reliability metrics for foundation machine-learned interatomic potentials (MACE-MP, CHGNet, Orb V3) do not predict whether they improve DFT-based screening decisions, and evaluates three reliability interventions against a decision-aligned deployment objective.
- **In plain words**: Researchers use AI models to guess which new materials are stable enough to be worth expensive quantum-mechanical calculations or lab tests. This paper asks whether making those AI models more "reliable" by usual measures actually leads to better choices about which candidates to check. The authors tested three fixes and found that each can succeed on its own narrow measure while leaving the final screening decision unchanged or worse.
- **Why it matters**: Materials discovery pipelines spend heavily on verification, so whether a reliability check saves that cost matters in practice. The paper's core point, that a model's accuracy or uncertainty is not the same as its value for a decision, may apply to other AI-guided screening settings, though the text itself only covers materials models.
- **Background needed**: - Interatomic potential: a machine-learned model that estimates the energy and forces of atoms, much faster than quantum calculations.
- DFT (density functional theory): the expensive quantum-mechanical calculation used to verify predicted energies.
- Foundation model: a large model pretrained on broad data and then applied to many tasks.
- Convex hull / near-hull candidates: a material is stable if its energy lies on or near the lowest-energy boundary among competing compositions; "near-hull" means close to that boundary.
- Recall: the fraction of truly promising candidates that the screening keeps.
- Calibration: whether a model's stated confidence matches how often it is actually right.
- Novelty detection: flagging inputs that differ from the training data.
- Two-oracle analysis: comparing decisions made using an ideal reference measure against decisions made using the target the paper proposes. · level: research-level

<details><summary>Original abstract</summary>

In AI-guided materials discovery, machine-learning models increasingly decide which candidate materials should receive expensive first-principles or experimental evaluation. Standard reliability metrics such as uncertainty, calibration, novelty, and ranking accuracy evaluate properties of the predictions, but success on these metrics does not necessarily imply a better downstream screening decision. We study this mismatch for foundation machine-learned interatomic potentials (MACE-MP, CHGNet, Orb V3) used to rank candidate crystal structures before DFT verification. We evaluate three representative reliability interventions (novelty detection, sparse DFT calibration, and chemistry-level ranking audits) using a deployment objective that measures how much DFT can be avoided while maintaining a required recall of near-hull candidates. Across all three, a reliability signal can succeed on its immediate target without improving the final screening decision: novelty detects distribution shift but weakly ranks failure severity; calibration can improve pooled ranking metrics while leaving screening unchanged or degrading it; and sparse audits identify MLIP-chemistry combinations with poor ranking reliability without yielding a robustly beneficial routing policy. A two-oracle analysis further shows that the source of failure depends on the screening decision itself: under formation-energy screening, even perfect knowledge of average ranking reliability can select the wrong model, whereas in the evaluated hull-aligned variant the oracle target becomes decision-aligned but finite-budget audits still fail to realize the value. Reliability should be evaluated relative to the decision it supports: the relevant question is not whether a model is uncertain or inaccurate, but whether acquiring and acting on additional information will improve the final discovery decision enough to justify its cost.

</details>

## Soft matter and polymers

### [Intrinsic volume fraction can decouple from hydrodynamic size in p(NIPAm-co-AA) microgels](https://arxiv.org/abs/2611.28284)
*Peter Edimeh, Howard Chen, Jacinta C. Conrad* · `cond-mat.soft` · arXiv:2611.28284v1 · relevance 0.08

- **In one sentence**: Experimental test of whether the intrinsic volume fraction and hydrodynamic size of p(NIPAm-co-AA) microgels stay proportional across pH and temperature, using capillary viscometry and static and dynamic light scattering for two crosslinker levels.
- **In plain words**: Microgels are tiny soft gel particles that swell and shrink with temperature and acidity, and scientists often estimate how tightly they pack together by assuming their size and the amount of polymer inside change in lockstep. This paper tests that assumption on two versions of a temperature- and pH-sensitive microgel. The authors found that at high temperature in acidic conditions, the size measured by light scattering and the volume measured by viscosity no longer change together.
- **Why it matters**: Packing fraction controls how thick or flowing a suspension is, so a wrong estimate could mislead predictions of rheology and transport in applications such as coatings, drug delivery, or fluids. The text suggests the mismatch comes from uneven polymer distribution inside the particle, but this is an interpretation from a single study and its broader reach is not established here.
- **Background needed**: - Microgels: micrometer-scale or smaller crosslinked polymer networks that swell in water like tiny sponges.
- Packing fraction / intrinsic volume fraction: how much space the swollen polymer occupies relative to the total volume; it governs flow behavior.
- Hydrodynamic radius (R_h): the effective size a particle has when it moves through liquid, measured by dynamic light scattering.
- Radius of gyration (R_g): a size measured from how light scatters at different angles, reflecting how mass is spread within the particle.
- Capillary viscometry: measuring a liquid's thickness by timing its flow through a thin tube.
- pKa and ionization: acrylic acid groups carry charge at high pH and are mostly uncharged at low pH, which changes swelling.
- Volume phase transition: an abrupt-ish shrinking of a gel as conditions cross a threshold; here near the lower critical solution temperature (LCST) of pNIPAm, roughly 32 °C.
- Crosslinker: the molecule (here methylenebisacrylamide) that ties polymer chains together; more crosslinker means a stiffer, less swollen network. · level: research-level

<details><summary>Original abstract</summary>

Quantifying the packing fraction of microgels is key to understanding their rheology and transport properties. Often, packing fractions are extrapolated from the hydrodynamic size and intrinsic volume fraction under the assumption that particle size and polymer volume change are proportional. Here, we test this assumption for p(N-isopropylacrylamide-co-acrylic acid) [p(NIPAm-co-AA)] microgels of two crosslinker concentrations (1 wt\% and 7 wt\% methylenebisacrylamide) using capillary viscometry and light scattering (static and dynamic) above and below the pKa of acrylic acid (AA). At pH 8, where AA is fully ionized, the microgels do not undergo a pronounced volume phase transition because electrostatic repulsion hinders thermal collapse, and both measures of hydrodynamic volume are equal. At pH 4, however, p(NIPAm-co-AA) microgels are weakly charged and exhibit a volume phase transition near the lower critical solution temperature of pNIPAm; the magnitude of the size change is greater for the less-crosslinked microgel. Above the volume phase transition temperature, the volume change from hydrodynamic radius decouples from that from viscosity. The ratio of the radius of gyration and hydrodynamic radius R_g/R_h of p(NIPAm-co-AA) microgels at high temperature exceeds the value theoretically predicted for homogeneous spheres and the deviation increases with the extent of crosslinking, suggesting that a non-uniform internal distribution of polymer gives rise to the anomalous decoupling at high temperatures. Our results indicate that care must be taken in extrapolating packing fractions for multi-responsive copolymer microgels, and suggest that copolymer composition and crosslink density may be used to tune bulk properties such as rheology through the internal microstructure.

</details>

### [Dynamical evolution and rheological behavior of a sheared compound vesicle with a highly viscous core: a mesoscale particle-based study](https://arxiv.org/abs/2611.30232)
*A. Lamura* · `cond-mat.soft` · arXiv:2611.30232v1 · relevance 0.05

- **In one sentence**: A two-dimensional mesoscale particle simulation of a compound vesicle (an outer membrane enclosing a fluid annulus and a more viscous inner core) in wall-bounded shear flow, examining how core viscosity and filling fraction change membrane dynamics and effective rheology.
- **In plain words**: This study uses computer simulations to look at a soft capsule-like object, a membrane bag with a second, thicker fluid inside it, being pushed along by a flowing liquid between walls. It is offered as a simple stand-in for a cell that has a nucleus-like inner body. The authors report that making the inner core more viscous eventually stops the outer membrane from settling into a steady rolling motion, and that the inner body's motion can cause the outer membrane's shape to jump around at high filling fractions.
- **Why it matters**: The work is a idealized model, so its value is mainly in showing how an internal viscous structure can change the flow behavior of a deformable cell-like object; the text does not show direct links to specific biological or industrial measurements. Its relevance to real cells would need experimental checks that the text does not describe.
- **Background needed**: - Vesicle: a thin elastic membrane enclosing fluid, a simple model of a cell.
- Compound vesicle: a vesicle with another vesicle or body inside, here a viscous core.
- Shear flow: liquid moving faster in one layer than the next, like wind shearing across a surface.
- Tank-treading: the membrane steadily rotates around its shape, like a tank track, rather than tumbling end over end.
- Viscosity: how thick or resistant to flow a fluid is.
- Filling fraction (φ): how much of the space between the walls is occupied by the object, with higher values meaning more crowded.
- Intrinsic viscosity: a measure of how much an suspended object raises the thickness of the surrounding fluid.
- Mesoscale particle-based simulation: a computer method that tracks groups of particles to represent fluid and membrane at a scale between atoms and whole continuum flows. · level: research-level

<details><summary>Original abstract</summary>

We study numerically the dynamics and the rheology of a two-dimensional compound vesicle in wall-bounded shear flow, as a minimal model of a nucleated cell. We consider the configuration in which the annular fluid is iso-viscous with the external one, while the inner core is more viscous. Increasing the core viscosity drives the external vesicle away from steady tank-treading at values $\phi \geq 0.6$. When an internal body is present, the annular fluid partially shields the outer membrane from the viscous core, so that at small filling fractions the external vesicle retains tank-treading with a higher inclination angle and the intrinsic viscosity stays comparatively low. The internal vesicle, by contrast, tumbles and migrates away from the center, and at high $\phi$ this motion couples back to the host, producing intermittent shape excursions of the external membrane. The inner viscous body thus acts as an internal governor of the dynamical state.

</details>

## AI for chemistry and materials

### [RumiFold: Teaching an LLM to Natively Fold Proteins and Reason About Their Function](https://arxiv.org/abs/2611.29444)
*Kevin Lu, David Bau, Wengong Jin* · `cs.LG` · arXiv:2611.29444v1 · relevance 0.19

- **In one sentence**: RumiFold is a pretrained chat language model that is taught to fold proteins (predict 3D structure) from its own hidden states, then uses those folded representations to answer natural-language questions about protein function, reporting accuracy comparable to SimpleFold and state-of-the-art results on Gene Ontology and free-text function tasks.
- **In plain words**: Proteins are chains of molecules that fold into specific 3D shapes, and the shape largely determines what they do in a cell. This paper asks whether a general-purpose chatbot-style language model can learn to predict those shapes inside its own internal processing, and then use that shape information to answer questions about what a protein does. The authors report that it predicts structures about as well as a dedicated folding model and does well on function-labeling tasks.
- **Why it matters**: It suggests that protein structure knowledge and ordinary language reasoning could live in one model rather than in separate tools, which may matter for scientists who want to query biology in plain language. The text does not show how it compares with the wider range of specialized tools beyond the named baseline, so the scope of the advance should be judged from the full paper.
- **Background needed**: - Protein folding: a protein's amino acid sequence determines its 3D shape, and shape largely determines function.
- Language model: a neural network trained on text; "hidden states" are its internal numerical representations of the input.
- Per-residue: one representation for each amino acid position along the protein chain.
- Gene Ontology (GO): a standard vocabulary of biological functions used to label proteins.
- Causal intervention: deliberately altering internal parts of the model to test whether they actually drive a given output.
- Dedicated single-representation models such as SimpleFold: specialized protein-structure predictors, used here as a comparison point. · level: research-level
- Matched keywords: protein

<details><summary>Original abstract</summary>

Can we teach a general-purpose language model to fold proteins? And if so, what does learning to fold enable beyond structure prediction itself? We introduce RumiFold, a pretrained chat model that learns to predict protein structures directly from its own hidden states. RumiFold processes proteins through repeated folding passes, then uses these folded representations to answer questions in natural language. It achieves folding accuracy comparable to dedicated single-representation models such as SimpleFold, alongside state-of-the-art performance on Gene Ontology protein function prediction and free-text function description. We find that folding pretraining organizes the model's hidden states around protein function, creating an internal per-residue workspace that is biologically grounded. Causal interventions show that this folded workspace links structure and language when RumiFold predicts function, providing rich representations for biomolecular reasoning. We see RumiFold as a step toward native biomolecular intelligence: where protein-based computations and language-based reasoning become integrated capabilities of general-purpose language models. Code, data, and models are available at: https://rumifold.baulab.info

</details>

### [Auditing two-stage MS/MS molecular retrieval on MassSpecGym v1.5: Reranking gains, candidate priors and spectrum dependence](https://arxiv.org/abs/2611.28096)
*Jiaqi Xue, Yutong Wu, Qiang Zhang* · `physics.chem-ph` · arXiv:2611.28096v1 · relevance 0.19

- **In one sentence**: An audit of a two-stage retrieval system that ranks candidate molecules for tandem mass spectra on the MassSpecGym v1.5 benchmark, separating genuine spectrum-based signal from candidate priors, replicate effects, and training-set overlap.
- **In plain words**: This paper looks at software that tries to identify an unknown chemical compound from its mass spectrum, a fingerprint made by breaking molecules into fragments and weighing them. The authors built a two-step system: first a shortlist of likely candidate structures, then a reranker that reorders them. They then tested how much of the reported accuracy really comes from the spectrum itself versus from shortcuts such as which candidates are common or well represented in training data.
- **Why it matters**: Reported gains in this kind of benchmark can look larger than they are if the tests reward shortcuts, so careful audits matter for anyone using such tools to identify compounds. The paper's own conclusion is limited: the gains come mainly from mass-feasibility evidence, not proven learned structural discrimination, and it argues that evaluation should check shortlist reachability, spectrum dependence and generalization to new molecules separately.
- **Background needed**: - Tandem mass spectrometry (MS/MS): an instrument method that fragments molecules and records the pieces' masses, giving a spectrum.
- Molecular retrieval: picking the correct chemical structure from a list of candidate structures for a given spectrum.
- Recall@k: the share of test spectra whose correct molecule appears in the top k ranked candidates.
- Two-stage retrieval: a fast first pass produces a shortlist, then a slower, more careful model reranks it.
- Fingerprints and embeddings: numerical encodings of molecules or spectra used for comparison.
- Adduct and precursor mass: the ion form and mass of the molecule being measured; used to filter chemically feasible candidates.
- Candidate priors: biases where some molecules are favoured simply because they are common or frequently seen in training.
- Data leakage and train/test overlap: when test molecules are too similar to training molecules, inflating scores. · level: research-level
- Matched keywords: molecule, molecular

<details><summary>Original abstract</summary>

Two-stage retrieval of molecular structures from tandem mass spectra (MS/MS) can benefit from candidate reranking, but benchmark gains may also reflect candidate priors, replicate spectra, precursor mass, and training-set coverage. We audit a two-stage retrieval system on the official MassSpecGym v1.5 split (17,556 test spectra). A data-safe DreaMS encoder and composite molecular fingerprints provide an initial shortlist; a support-gated reranker combines pair scores, candidate-relative peak coverage, and mass-feasibility features. The final system achieves 31.05% Recall@1, a 10.05-point gain over its Stage 1 ensemble, while preserving its 72.62% Recall@20. Replacing the query spectrum with one from a different molecule matched on adduct and precursor mass reduces Recall@1 by 9.0 points (15.3 points under molecule-balanced weighting); nevertheless, a training-mean spectrum retains 13.75% Recall@1, indicating substantial spectrum-independent signal. Mass-feasibility features improve Recall@1 beyond score and coverage controls, while learned peak-fragment similarities do not outperform constant coverage. Errors cluster by molecule, and removing close training neighbours causes a large decline in Stage 1 shortlist recall among initially well-covered molecules. We conclude that candidate-relative mass-feasibility evidence improves front-rank retrieval and spectrum dependence, but does not establish learned structural discrimination or eliminate candidate priors. Evaluation should separately assess shortlist reachability, spectrum dependence, and molecule-level generalization.

</details>

## Biochemistry

### [Albumin alleviates pressure overload-induced heart failure by improving mitochondrial homeostasis via PKA-LKB1-AMPK axis](https://www.biorxiv.org/content/10.64898/2026.11.21.768247v1)
*AN, Q.; Ma, B.; Fu, Y. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.21.768247 v1 · relevance 0.06

- **In one sentence**: In a mouse model of pressure-overload heart failure, recombinant mouse serum albumin improved cardiac function and mitochondrial energy metabolism, reportedly via a PKA-LKB1-AMPK signaling axis.
- **In plain words**: Heart failure is a condition where the heart cannot pump blood well enough, and it often carries a poor outlook. This study looked at albumin, the most abundant protein in blood, whose levels tend to be low in people with heart failure. In mice whose hearts were put under strain by constricting the aorta, giving extra albumin improved heart pumping and reduced enlargement, scarring and inflammation.
- **Why it matters**: It suggests that a protein already used clinically could be a therapeutic candidate for heart failure, and that its effect may run through the energy-producing machinery of heart cells (mitochondria). Whether this carries over to humans is not shown by the text, which reports only mouse and cell experiments.
- **Background needed**: - Heart failure: the heart weakens and cannot pump enough blood; pressure overload (e.g., from high blood pressure or a narrowed aortic valve) is a common cause.
- Serum albumin: the most abundant protein in blood plasma; low levels are linked to worse heart failure outcomes.
- Transverse aortic constriction (TAC): a surgical method in mice that narrows the aorta to mimic pressure overload.
- Knockout (AKO) mice: animals genetically engineered to lack the albumin gene, used to test whether a protein is needed.
- Mitochondria: the cell's energy-producing structures; "homeostasis" here means keeping their function and quality balanced.
- AMPK: an energy-sensing enzyme that switches cells toward fat burning and energy conservation when energy is low; PKA and LKB1 are signaling proteins that act upstream of it.
- Hypertrophy and fibrosis: enlargement of heart muscle cells and build-up of scar-like tissue. · level: research-level

<details><summary>Original abstract</summary>

Aims Heart failure (HF) is a global health challenge due to its high incidence, mortality, and socioeconomic burden. Despite medical advancements, HF prognosis remains poor, highlighting the need for enhanced understanding and treatment strategies. Serum albumin, a key circulatory protein, has gained attention as a biomarker in cardiovascular diseases. Low serum albumin levels are linked to HF incidence, progression, and prognosis, suggesting its regulatory role, though mechanisms remain unclear. This study aimed to elucidate the role of serum albumin in HF pathogenesis and investigate its potential therapeutic effects. Methods and results A mouse model of pressure overload-induced HF was established via transverse aortic constriction (TAC). Serum albumin levels were significantly decreased in HF mice. Administration of recombinant mouse serum albumin (rMSA) effectively restored serum albumin concentrations, improved cardiac systolic function, alleviated cardiac hypertrophy and fibrosis, and reduced inflammatory responses, collectively attenuating disease progression. In contrast, albumin-knockout (Alb-/-, AKO) HF mice displayed aggravated pathological manifestations compared with wild-type (WT) controls, whereas rMSA supplementation markedly ameliorated these impairments. In vitro experiments demonstrated that rMSA protected against phenylephrine (PE)-induced hypertrophy in cardiomyocytes. To elucidate the underlying mechanism, transcriptomic analyses of cardiac tissues revealed that albumin played a critical role in improving mitochondrial homeostasis. Experimental validation further demonstrated that albumin activated the PKA-LKB1-AMPK signaling axis, leading to improved mitochondrial respiratory function and oxidative phosphorylation, as well as enhanced mitochondrial quality control. These changes promoted fatty acid oxidation and optimized energy metabolism, thereby reversing the energy imbalance underlying cardiac dysfunction. Conclusion Our study suggests that serum albumin exerts a protective effect in HF by improving mitochondrial dysfunction and energy metabolism disorders, thus reversing energy imbalance and mitigating disease progression. These results support recombinant serum albumin as a promising therapeutic for HF, with its mechanism involving the critical improvement of mitochondrial homeostasis.

</details>

### [A Shifting Landscape: Deconvoluting the Effect of Mg2+ and pH on Base Triple Formation in 7SK SL-1](https://www.biorxiv.org/content/10.64898/2026.11.19.767663v1)
*Fallon, L.; Venkatesh, H.; Jones, A.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.19.767663 v1 · relevance 0.04

- **In one sentence**: A combined molecular dynamics, free-energy, NMR, and SAXS study that maps how Mg2+ and pH independently shift the conformational landscape and base-triple formation in the 7SK snRNA stem-loop 1 that binds HEXIM.
- **In plain words**: This paper looks at a small RNA molecule, 7SK, which helps control how a cell's gene-copying machinery (RNA polymerase II) switches genes on and off. The authors study one part of this RNA, stem-loop 1, and ask how the acidity of the surroundings (pH) and the amount of magnesium ions change the way its bases lock together into small three-way groupings. They report that both factors strongly reshape the molecule's possible shapes and that they act in different, independent ways to favor these groupings.
- **Why it matters**: The RNA's shape determines how it binds the protein HEXIM, which in turn affects transcription output, so understanding what tunes that shape is relevant to gene regulation. The text does not show any direct biological or therapeutic consequence; the link to transcription control is offered as a possibility the authors discuss.
- **Background needed**: - RNA is a chain of bases (building blocks) that can fold into shapes; this molecule is a noncoding RNA.
- Stem-loop: a hairpin-shaped fold of RNA.
- Base triple: three RNA bases held together by hydrogen bonds, which stabilizes a particular fold.
- HEXIM and P-TEFb: proteins that 7SK helps regulate, which in turn controls RNA polymerase II, the enzyme that copies protein-coding genes.
- Mg2+: magnesium ions, which help RNA fold by neutralizing its negative charge.
- pH: a measure of acidity; changes can alter which bases are charged and how they pair.
- Methods: molecular dynamics (computer simulation of atomic motion), free-energy calculations, NMR (spectroscopy that reports on atomic environments), and SAXS (X-ray scattering that reports overall shape in solution). · level: research-level

<details><summary>Original abstract</summary>

The small-nuclear RNA (snRNA) 7SK is essential for regulating the transcription of genes by RNA polymerase II through its interactions with Hexamethylene Bisacetamide Inducible Protein (HEXIM) and positive transcription elongation factor b (P-TEFb). High-resolution structures of 7SK stem-loop 1 (SL-1) reveal the presence of several base triples that coordinate the interaction with HEXIM. However, different high-resolution structures of 7SK SL-1 exhibit different conformations, each with unique base triple configurations. Previous NMR studies show that the conformation of 7SK SL-1 is sensitive to changes in pH and Mg2+ concentration. However, the exact mechanism by which Mg2+ and pH influence the formation and stability of base triples in 7SK SL-1 at an atomic level remains unclear. We combine molecular dynamics (MD) simulations, free energy calculations, nuclear magnetic resonance (NMR), and small angle X-ray scattering (SAXS) to conduct a detailed investigation into the mechanism and dynamics of base triple formation in 7SK SL-1, and deconvolute the effects of pH and Mg2+. We find that the conformational landscape of 7SK SL-1 dramatically changes depending on the pH and presence of Mg2+, and that pH and Mg2+ act orthogonally to favor the formation of base triples. We discuss how the dynamic behavior of the base triples may provide a means for 7SK to regulate its interactions with HEXIM, modulating the transcriptional output of RNA polymerase II.

</details>

## Pharmacology and drug discovery

Nothing notable this time.

## Computational and systems biology

### [Microbiome complexity shapes host transcriptional networks across the ileum-liver axis](https://www.biorxiv.org/content/10.64898/2026.11.16.767119v1)
*Halkhoree, A. C.; Grannell, A.; Pearson, C. et al.* · `systems biology` · bioRxiv doi:10.64898/2026.11.16.767119 v1 · relevance 0.08

- **In one sentence**: Transcriptomic survey of mouse terminal ileum across germ-free, defined 12-strain microbiota (MM12), and specific-pathogen-free conditions to test how microbiome complexity reshapes host gene co-expression networks in the ileum and liver axis.
- **In plain words**: This study asks how much the community of microbes living in the gut changes the way genes switch on and off in the lower small intestine (ileum), and whether that affects the nearby liver. The researchers compared mice with no microbes, mice with a simple set of 12 known bacterial strains, and mice with a normal, more varied microbiome. The text describes the setup and sample sizes but does not give the results in the excerpt provided.
- **Why it matters**: Gut bacteria are linked to digestion, immunity and liver health, so knowing which gene networks they tune could help explain those links. The excerpt does not report findings, so its significance beyond the design cannot yet be judged.
- **Background needed**: - Transcriptome: the full set of gene activity readings in a tissue sample, often used to see which genes are active.
- Co-expression network: a map of genes that rise and fall together, suggesting they are regulated as a group.
- Germ-free (GF) mice: raised with no microbes at all, used as a baseline.
- MM12 (Oligo-Mouse-Microbiota-12): mice colonised with a defined set of 12 bacterial strains, giving a controlled level of microbiome complexity.
- SPF (specific pathogen free): standard lab mice with a full, varied but screened microbiome.
- Ileum: the last part of the small intestine, where nutrients and bile acids are absorbed.
- Bile acids: digestive molecules made by the liver and modified by gut bacteria.
- Peyer's patches: immune tissue in the gut wall. · level: research-level

<details><summary>Original abstract</summary>

The microbiome plays an increasingly recognised role in development, metabolism and immunity across all segments of the small and large intestine, as well as more distant organs such as the liver. In the terminal ileum - a key site of nutrient absorption - the presence of microbes dictates the development of secondary lymphoid structures (Peyers patches), mediates bile acid metabolism, and impacts absorption. In part, coordinated regulatory networks in the gut impact liver function and immunity through gut-liver connectivity and the movement of immune cells and bioactive small molecules that includes bile acids and other bacterial metabolites. We aimed to examine the extent of microbiome involvement in ileal transcription, where subtle changes in co-expression networks can be tuned by microbiome diversity, composition and function. We surveyed ileal transcriptomes across mouse models which vary in microbiome complexity ranging from germ-free (GF, n = 15), the Oligo-Mouse-Microbiota-12 (MM12, n = 15), and specific pathogen free (SPF, n = 15).

</details>

### [A2Holo: Dual-Stream Flow Matching of 3D Structure and a Protein Language Model for Conformational Transition Prediction](https://www.biorxiv.org/content/10.64898/2026.11.20.768033v1)
*Kim, D.; Kim, H.; Sim, J. et al.* · `bioinformatics` · bioRxiv doi:10.64898/2026.11.20.768033 v1 · relevance 0.08

- **In one sentence**: A2Holo uses deterministic flow matching between apo and holo protein structures, with a dual-stream joint attention block that fuses a protein language model's residue embeddings with 3D structure, and analyses the resulting residue-level attention patterns.
- **In plain words**: Proteins change shape when a drug-like molecule (a ligand) binds to them, and drug designers would like to predict the bound shape from the unbound one. This paper presents A2Holo, a model that maps an unbound protein structure to its bound form in a single fixed sequence of steps, rather than starting from random noise. The authors report that it gives the lowest median structural error among existing methods on a shared benchmark, and they also inspect which residues (amino-acid building blocks) pay attention to which others inside the model.
- **Why it matters**: Predicting how a protein changes shape on binding matters for structure-based drug discovery, so a fast, deterministic predictor could be useful if the reported accuracy holds up. The attention analysis offers a possible window into how sequence and structure information are combined, though the text alone does not show how far that interpretation generalises.
- **Background needed**: - Apo vs holo: a protein's shape without (apo) and with (holo) a bound ligand.
- Flow matching: a way to train a model to transform one set of data into another along a smooth path; here, between two real structures.
- Protein language model: a neural network trained on protein sequences that produces a numerical vector for each residue.
- Joint attention: a mechanism letting two streams of information (here sequence and 3D structure) inform each other.
- C-alpha RMSD and TM-score: standard measures of how far a predicted 3D backbone is from the reference; lower RMSD and higher TM-score mean closer agreement.
- Stochastic sampling: generating several outputs with randomness; the paper compares against best-of-10 samples from such baselines. · level: research-level

<details><summary>Original abstract</summary>

Modelling a ligand-bound holo conformation from a ligand-free apo conformation is essential in structure-based drug discovery. We present A2Holo, which casts apo-to-holo prediction as flow matching between two experimental structures rather than generation from noise. It transplants the dual-stream joint attention of in-context image generation to residue-aligned protein language model embeddings and structure. Without ligand conditioning or stochastic sampling, A2Holo's single deterministic trajectory reaches a median C RMSD of 0.809 [A] on the D3PM benchmark, the lowest among existing methods. Its TM-score exceeds even the best of 10 samples from every stochastic baseline on at least 144 of 150 pairs. Beyond performance, we directly measure the transplanted multimodal mechanism itself. Because sequence and structure are residue-aligned, its joint attention can be measured at residue resolution and tested for reproducibility across independently trained model variants. Within the structure stream, the attention a residue receives recovers moving residues better than the attention it emits, and this asymmetry is learned. A2Holo demonstrates a successful multimodal transplant from in-context image generation to protein conformational change, with strong deterministic apo-to-holo prediction. It also provides a quantitative account of how that mechanism organises residue-aligned sequence and structure around the residues that move.

</details>

## Neuroscience

### [Investigating Motor Skill Acquisition in Mice and Humans: Towards A Cross-Species Paradigm](https://www.biorxiv.org/content/10.64898/2026.11.20.768070v1)
*Hille, M.; Justus, L. C.; Zocher, S. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.20.768070 v1 · relevance 0.06

- **In one sentence**: A cross-species study that uses a matched chopstick grasping task in humans and a single-pellet reaching task in mice, tracking structural and quantitative MRI changes during early motor learning.
- **In plain words**: Scientists want to connect brain scan changes seen in people with what is known about brain cells from animal studies. This paper builds a similar reaching-and-grasping task for mice and for people, trains some of each group while others serve as untrained controls, and scans their brains with MRI before, during, and after training. Mice showed shrinking volume in the motor area of the brain on the trained side, while in people the scans showed no reliable volume change but did show shifts in tissue-sensitive measures on the trained side.
- **Why it matters**: It is a careful attempt to bridge human brain imaging and animal cell-level research, which is a known gap in neuroscience. The authors themselves say the common biological mechanism is unclear, so the work is best read as a proposed starting point rather than a settled link between species.
- **Background needed**: - MRI measures brain structure non-invasively; "gray matter volume" is how much of the outer brain tissue there is.
- Quantitative MRI measures (MTsat, R1) are signals sensitive to tissue composition; an increase is consistent with more myelin, the fatty insulation around nerve fibers, but this is an interpretation, not a direct measurement.
- The motor cortex is the brain region that plans and controls movement; the contralateral side is the opposite hemisphere from the moving limb.
- The mouse single-pellet reaching task is a standard test where animals reach through a slot to grab a food pellet.
- Motor skill learning is the gradual improvement of a movement with practice; "early learning" refers to the first phase of training.
- Study sizes: 48 mice and 71 young men, all male, which limits how far results generalize. · level: research-level

<details><summary>Original abstract</summary>

Relating non-invasive observations of human brain plasticity to cellular processes identified in animal models remains a major challenge in neuroscience. We address this challenge by introducing a paradigm for studying motor skill acquisition across species. We designed a human chopstick grasping task modeled after the rodent single-pellet reaching task, resulting in a comparable sequence of reach-to-grasp movements across species. We studied 48 young adult male C57BL/6N mice and 71 young men, comparing trained groups with untrained controls. In both mice and humans, structural magnetic resonance imaging (MRI) was performed before, during, and after motor training. The functional form of behavioral performance gains on the trained task was highly similar across species. In trained compared to control mice, analysis of the early learning interval revealed decreases in regional volume in contralateral primary motor and forelimb somatosensory cortices, with greater volume reductions in primary motor cortex associated with better reaching performance. In humans, performance gains transferred to other chopstick tasks but not to general dexterity, and no reliable changes in gray matter volume were observed. Quantitative MRI, however, revealed early training-related changes in tissue-sensitive measures, including increases in magnetization transfer saturation (MTsat) and longitudinal relaxation rate (R1) in contralateral motor and frontal regions, potentially reflecting an increase in intracortical myelin. Thus, early structural changes in the contralateral motor cortex were detected in both species, but the degree to which these changes reflect a common biological mechanism is unclear. We conclude that the present cross-species paradigm provides a viable starting point for studying brain plasticity across species. Future work needs to relate macroscopic structural changes more directly to cellular processes by applying longitudinal microscopic imaging and MRI in the same animals.

</details>

### [Sex differences in the effects of enhanced adult hippocampal neurogenesis on pattern discrimination and Intellicage spatial learning in Bax-knockout mice](https://www.biorxiv.org/content/10.64898/2026.11.23.768231v1)
*Tunc-Ozcan, E.; Rodriguez, A. M.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.23.768231 v1 · relevance 0.05

- **In one sentence**: In Bax-knockout mice, which keep more newborn dentate granule cells alive, male and female mice showed different and task-dependent changes in Intellicage place learning, reversal learning, and A/B context discrimination.
- **In plain words**: The brain keeps making new nerve cells in a small memory region called the hippocampus, but many of them die off. In this study, researchers genetically blocked a cell-death gene (Bax) in mice so more of these new cells survived, then tested males and females on several learning tasks. The extra cells helped in some tests and not others, and the effects differed between the sexes.
- **Why it matters**: It tests whether a single way of boosting brain cell survival helps learning equally in both sexes, which matters because many studies use only one sex. The text reports partial, task-specific effects rather than a clear general improvement, so it should be read as a set of mixed findings rather than evidence of a therapy.
- **Background needed**: - Hippocampus: a brain region important for forming memories and navigating space.
- Neurogenesis: the birth of new nerve cells, which continues in adult hippocampus in mice.
- Dentate granule cells: the main type of neuron in the hippocampus's input region that the new cells become.
- Bax: a gene that drives programmed cell death; knocking it out lets more new cells survive.
- tdTomato: a fluorescent label used to mark and count the new cells.
- Intellicage: an automated home-cage system where mice choose between corners to learn places and reversals.
- Pattern/context discrimination: telling apart two similar environments or stimuli. · level: research-level

<details><summary>Original abstract</summary>

Adult hippocampal neurogenesis has been implicated in learning and memory. Although increasing neurogenesis has been associated with improved spatial learning and pattern discrimination, whether these benefits differ between male and female mice remains unclear. The goal of this study was to see if increasing adult hippocampal neurogenesis improves learning in male and female mice, and whether the benefit is the same in both sexes. We used conditional deletion of the pro-apoptotic gene Bax to increase the survival of newborn dentate granule cells. Male and female BAX knockout (KO) and wild-type (WT) mice were tested in Intellicage place learning and reversal learning tasks, and an A/B context discrimination task. BAX KO mice had more tdTomato-positive newborn dentate granule cells than BAX WT mice, with no significant effect of sex. During Intellicage adaptation, there were no differences between genotypes or sexes in total visits and licks. During place learning, male mice had a higher percent correct response than female mice, while female mice showed increases in licks and correct visits from day 1 to day 4. BAX KO mice made more visits overall but had a lower percent correct response than BAX WT mice on day 4. During reversal learning, male BAX KO mice showed a decrease in visits and had fewer visits with a lick than male BAX WT mice on day 4. In the A/B task, male BAX KO mice had higher discrimination scores than male BAX WT mice on day 5, while female BAX KO mice showed an initial advantage over female BAX WT mice. These results partially support our hypothesis that increasing neurogenesis would benefit male mice more. Overall, increasing the survival of newborn dentate granule cells does not improve learning in the same way across sexes and tasks.

</details>

## Genetics and genomics

### [The 'near T2T' Canton-S assembly is inconsistent with other Canton-S genomes](https://www.biorxiv.org/content/10.64898/2026.11.19.767897v1)
*Emerson, J. J.* · `genomics` · bioRxiv doi:10.64898/2026.11.19.767897 v1 · relevance 0.08

- **In one sentence**: A commentary arguing that the recently published "near T2T" genome assembly of the Drosophila Canton-S strain differs from three other independently sequenced Canton-S assemblies by an amount comparable to differences between distinct strains, raising doubts about its genetic identity.
- **In plain words**: Canton-S is a fruit fly lineage that scientists have used as a standard reference for decades. A newly published, very high-quality genome sequence of this fly is presented as a community resource, but this short comment says that its genetic makeup does not match three other separately sequenced versions of the same strain. The author suggests that this mismatch should make the community think carefully before adopting the new sequence.
- **Why it matters**: A reference genome is only useful if it truly represents the strain labelled on it, since many experiments and mapping studies rely on that identity. The comment matters for anyone choosing which fly genome to use as a baseline, though the text itself gives only the author's comparison and no independent check.
- **Background needed**: - Drosophila melanogaster is the common fruit fly, a major model organism in genetics.
- A "strain" is a line of flies kept inbred so that individuals are genetically very similar.
- Canton-S is a widely used wild-type (standard-type) strain for behaviour, genetics and trait mapping.
- A genome assembly is a reconstructed DNA sequence built from sequencing reads; "T2T" (telomere-to-telomere) means it aims to cover whole chromosomes end to end with no gaps.
- Comparing assemblies from the same named strain is a way to check whether they are genetically the same; large differences suggest different lineages or errors.
- The text gives no details of the methods, the exact size of differences, or any response from the original authors. · level: intermediate

<details><summary>Original abstract</summary>

Canton-S is among the most widely used Drosophila melanogaster strains, underlying substantial community infrastructure, including serving as a wild-type strain for: genetics studies; studying phenotypes, especially in behavioral studies; and complex trait mapping studies among many others. The recent 'near T2T' assembly of Canton-S (LIU et al.) is presented as delivering modern sequencing and assembly quality to the Drosophila community via this important strain. I find that this assembly is inconsistent with three other independently sequenced Canton-S genome assemblies on a magnitude comparable to differences between distinct strains, raising concerns about its genetic identity that the community should consider when choosing whether to adopt it as a resource.

</details>

### [Genomics of the diversification of Heliconius cydno (Lepidoptera: Nymphalidae) in northern South America: geographic and phenotypic patterns](https://www.biorxiv.org/content/10.64898/2026.11.20.768178v1)
*Arias Cardenas, A.; Rueda-M, N.; Arias, C. F. et al.* · `genomics` · bioRxiv doi:10.64898/2026.11.20.768178 v1 · relevance 0.08

- **In one sentence**: Whole-genome analysis of 133 Heliconius cydno butterflies that tests how Andean uplift, geography and introgression shaped its radiation, and maps the locus (ivory:mir-193) behind its hindwing white band.
- **In plain words**: This paper looks at a group of colorful butterflies in Central and northern South America and asks how they split into separate populations and forms. The researchers read the complete genomes of 133 butterflies covering all recognized subspecies. They found that five of the fourteen subspecies form distinct genetic lineages, and they traced a wing-pattern trait to one genetic region, while also finding signs that the trait moved between related species.
- **Why it matters**: It shows how mountains, geography and hybridization between species can together drive rapid diversification and the sharing of warning-color patterns. The text does not establish how broadly these findings apply beyond this butterfly group.
- **Background needed**: - Heliconius butterflies are known for warning (aposematic) coloration that predators avoid, and for mimicry, where unrelated-looking species share patterns.
- A subspecies is a geographic variant within a species; a monophyletic lineage is a group descended from a single common ancestor.
- Introgression means genes passing from one species into another through interbreeding.
- Cis-regulatory elements are DNA segments that switch genes on or off; microRNA (mir-193) is a small RNA that regulates gene activity.
- The Andean orogeny is the uplift of the Andes mountains, which can split populations and shape where species live.
- Whole-genome sequencing reads an organism's complete DNA, allowing comparison of genetic relationships. · level: research-level

<details><summary>Original abstract</summary>

The interplay between natural selection, gene flow, and geography is a key driver of population differentiation. This study investigates their influence on the recent adaptive radiation of Heliconius cydno, a mimetic and aposematic butterfly with striking variation in wing color pattern across its distribution in Central and northern South America. The genetic basis of this phenotypic diversity has a modular architecture, whereby a few key genes and cis-regulatory elements control differences among morphotypes. Using whole-genome sequences from 133 individuals representing all subspecies of H. cydno, we investigated (1) the role of Andean orogeny in its diversification and (2) the genetic basis of the variation in the hindwing white submarginal band, which to date, had remained unknown. First, we found that five of the fourteen described subspecies correspond to distinct monophyletic lineages and well-defined genetic clusters that originated in northwestern South America and later expanded into Central America and the Colombian inter-Andean valleys. Second, we observed signatures of genetic structure that were consistent with geographic patterns, particularly those associated with the inter-Andean region and Gorgona Island. Third, we identified ivory:mir-193 as the locus underlying variation in the white submarginal band on the hindwing. We also detected evidence of introgression suggesting that this trait was likely transferred from H. cydno to H. melpomene, contributing to the establishment of a novel mimicry ring with H. erato. Altogether, these findings highlight the roles of geography, genomic architecture, and introgression in the diversification of H. cydno.

</details>

## Cell and molecular biology

### [Smyd1 regulates H3K4me3 to support adaptive fatty acid oxidation in the adult heart during lipid overload](https://www.biorxiv.org/content/10.64898/2026.11.18.763125v1)
*Mukai, R.; Oka, S.; Sung, E.-A. et al.* · `cell biology` · bioRxiv doi:10.64898/2026.11.18.763125 v1 · relevance 0.10

- **In one sentence**: In mice fed a high-fat diet, the muscle-specific histone methyltransferase Smyd1 transiently rises in cardiomyocytes and supports fatty acid oxidation genes via H3K4me3 marks and an interaction with PPARα; partial Smyd1 loss worsens cardiac dysfunction.
- **In plain words**: Eating a high-fat diet can overload the heart with fat and weaken its ability to burn that fat for energy, which over time may lead to heart failure. This study looked at a protein called Smyd1 in mice and found that it briefly increases in heart muscle cells early on, when the diet is stressing the heart, and appears to help switch on genes that burn fat. Mice with less Smyd1 did worse on the diet, developing heart enlargement, scarring, and higher death rates.
- **Why it matters**: Obesity is a major risk factor for heart failure, and the heart's ability to burn fat is one proposed link, so a protein that helps maintain this process could be a candidate for future therapies. The text reports mouse findings only, and the link to human heart disease and treatment is not shown here.
- **Background needed**: - Fatty acid oxidation (FAO): the cell's process of breaking down fats to make energy; the heart relies heavily on it.
- Obesity-related cardiomyopathy: weakening of heart muscle linked to excess body fat.
- Histone methyltransferase: an enzyme that adds chemical tags (methyl groups) to histones, the spool-like proteins around which DNA is wrapped, changing how genes are switched on.
- H3K4me3: a specific methyl tag on histone H3 that is generally associated with active genes.
- PPARα: a nuclear receptor (a protein that binds DNA to control gene activity) that turns on fat-burning genes.
- Heterozygous knockout: mice carrying one working copy of a gene instead of two, here limiting Smyd1 in the heart.
- Single-cell RNA sequencing: a method that measures gene activity cell by cell, used here to locate the Smyd1 increase in cardiomyocytes.
- Co-immunoprecipitation: a lab method to test whether two proteins physically bind each other. · level: research-level

<details><summary>Original abstract</summary>

Obesity and metabolic syndrome are major risk factors for heart failure, and impaired fatty acid oxidation (FAO) is a key contributor to metabolic dysfunction in obesity-related cardiomyopathy. However, how the heart maintains FAO and adapts to chronic lipid overload remains poorly understood. Here, we identify SET and MYND domain-containing protein 1 (Smyd1), a muscle-specific histone methyltransferase, as an early compensatory regulator of cardiac metabolism in response to lipid overload. In wild-type mouse hearts, high-fat diet (HFD) feeding induced transient increases in Smyd1 expression and H3K4me3 levels during the early-to-mid phase of metabolic stress, both of which returned to baseline levels during prolonged HFD exposure. Single-cell RNA sequencing further revealed that this adaptive increase in Smyd1 expression occurred predominantly in cardiomyocytes. In contrast, cardiac-specific Smyd1 heterozygous knockout mice exhibited accelerated cardiac dysfunction, left ventricular dilation, increased myocardial fibrosis, and reduced survival following HFD feeding. Mechanistically, Smyd1 deficiency impaired the adaptive upregulation of key FAO-related genes and reduced cardiac FAO activity. Furthermore, co-immunoprecipitation analysis revealed an interaction between Smyd1 and peroxisome proliferator-activated receptor alpha (PPAR), suggesting a potential mechanism by which Smyd1 supports FAO gene expression. Taken together, these findings identify Smyd1 as an early compensatory regulator that supports FAO-dependent metabolic adaptation and protects the heart against lipid overload-induced cardiac dysfunction. This adaptive mechanism, involving H3K4me3 regulation and the Smyd1-PPAR interaction, may provide potential therapeutic targets for therapeutic strategies aimed at preserving cardiac metabolic flexibility in obesity-related cardiomyopathy.

</details>

### [Targeted protein depletion in quiescent fission yeast cells using an auxin-degron system](https://www.biorxiv.org/content/10.64898/2026.11.20.767346v1)
*Le Collen, D.; Vazquez-Bolado, A.; Wu, P.-Y. J.* · `cell biology` · bioRxiv doi:10.64898/2026.11.20.767346 v1 · relevance 0.09

- **In one sentence**: In nitrogen-starved fission yeast, a quiescence model, analog-sensitive kinases fail because the ATP analog acts as a nitrogen source and triggers cell cycle re-entry, whereas an auxin-inducible degron system enables rapid, lasting and reversible protein depletion.
- **In plain words**: Quiescence is a resting state that cells can enter and later leave, and it is hard to study genes that are needed for life in that state. This paper tests two common ways of switching off proteins in resting yeast cells. One method, which uses a modified enzyme blocked by a chemical copy of ATP, does not work here because the chemical is itself used as food and pushes the cells to start dividing again. The other method, which tags a protein so that it is removed when a plant hormone-like molecule (auxin) is added, does work for depleting proteins in these resting cells.
- **Why it matters**: Many essential proteins cannot be studied by simply deleting their genes, so a reliable way to switch them off in resting cells matters for understanding how cells stay dormant and wake up. The text reports the method working in fission yeast only; whether it transfers to other organisms or to the wider biology of quiescence is not shown here.
- **Background needed**: - Quiescence: a reversible, non-dividing resting state that cells can hold for long periods and then exit when conditions improve.
- Fission yeast (Schizosaccharomyces pombe): a single-celled organism widely used to study the cell cycle; here it is starved of nitrogen to induce quiescence.
- Kinase: an enzyme that switches other proteins on or off by adding phosphate groups, using ATP as the energy source.
- Analog-sensitive kinase: an engineered kinase that can be blocked by a modified ATP-like molecule that other kinases ignore.
- Non-hydrolyzable ATP analog: a chemical similar to ATP that cannot be broken down for energy in the usual way.
- Auxin-inducible degron: a tag added to a protein so that, when a plant hormone analog is present, the cell rapidly destroys that protein.
- Cell cycle re-entry: a resting cell restarting division. · level: intermediate

<details><summary>Original abstract</summary>

Quiescence is a reversible, non-proliferative cellular state in which cells can remain for extended periods of time while retaining the ability to re-enter the cell cycle upon exposure to favorable conditions. This physiological state is critical for a broad range of biological processes, from stress response in unicellular systems to differentiation and development in multicellular organisms. Surprisingly, despite its recognized roles in cell biology in diverse species, key aspects of the regulation of quiescence remain poorly understood. To investigate protein function specifically in quiescence, a conditional activation approach is critical, in particular for factors that are essential for cell viability. However, the efficacy of a number of such inactivation strategies in quiescent cells remained unknown. Using nitrogen-depleted fission yeast cells as a well-established model for quiescence, we probed two types of commonly-used approaches: a targeted method for the reversible inhibition of engineered kinases using non-hydrolyzable ATP analogs, and a more general system targeting protein depletion using an auxin-inducible degron. Here we show that the use of analog-sensitive kinases is unsuitable for quiescent fission yeast cells, as the ATP analog serves as a nitrogen source and induces cell cycle re-entry. We then demonstrate how coupling a degron tag with a specific auxin ligand allows for rapid, lasting and reversible protein depletion in quiescent cells, providing a powerful tool for investigating the regulation of this crucial and widespread cellular state.

</details>

## Immunology and microbiology

### [Oral microbiome and DNA virome profiling in pigs reveals age-associated dynamics and extracellular recovery of Streptococcus suis-associated phage lineages](https://www.biorxiv.org/content/10.64898/2026.11.21.768310v1)
*Osei, E. K.; Ornelas, M. A. S.; Garcia Manzanilla, E. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.21.768310 v1 · relevance 0.10

- **In one sentence**: Shotgun metagenomic profiling of oral fluids from pigs on 15 Irish farms, using paired bulk and virus-like-particle enrichment, describes age-associated succession of oral bacteria and DNA phages, and identifies 26 predicted Streptococcus suis-targeting phages among 25,223 viral operational taxonomic units (vOTUs).
- **In plain words**: Pigs' mouths host large communities of bacteria and viruses, and this study sampled oral fluid from pigs on 15 commercial farms in Ireland to map who is there as the animals age. The bacterial mix shifted from environmental genera such as Pseudomonas and Staphylococcus soon after weaning to lactic acid bacteria and anaerobes later on. Most of the viral sequences could not be matched to a known genus, and the authors report 26 viral lineages predicted to infect Streptococcus suis, a pig pathogen.
- **Why it matters**: Phages that infect a pathogen like S. suis could in principle inform phage-based therapies or microbiome-targeted approaches, though the text only describes a catalogue and predicted targets, not tested activity. The study is a descriptive survey, so its links to herd health or treatment remain possibilities the authors suggest rather than show.
- **Background needed**: - Metagenomics: sequencing all DNA in a sample at once, then identifying which organisms it came from.
- Virome: the set of viruses in a sample; here, DNA viruses (phages infect bacteria).
- Virus-like particles (VLP) enrichment: a lab step that concentrates viral particles so viral DNA is easier to capture.
- vOTU (viral operational taxonomic unit): a cluster of similar viral sequences treated as one viral 'species' when a formal name is unavailable.
- Phage: a virus that infects bacteria.
- Streptococcus suis: a bacterial pathogen of pigs.
- Resistome: the collection of antibiotic-resistance genes.
- Weaning: when piglets are separated from their mothers and move to a new diet. · level: research-level

<details><summary>Original abstract</summary>

The pig oral cavity is a critical interface for microbial transmission and herd health monitoring, yet its microbiome and virome remains poorly characterised. We performed shotgun metagenomic sequencing of oral fluids from pigs across 15 commercial farms in Ireland, using paired bulk and virus-like particles (VLP) enrichment to capture comprehensive microbial and DNA virome diversity. Microbial communities shifted progressively with age, with early post-weaning animals enriched in environmental genera such as Pseudomonas and Staphylococcus and later stages dominated by lactic acid bacteria and anaerobes. Only 20.6% of vOTUs could be assigned to a known genus, with the most abundant being Astrithrvirus, which increased with age. Both microbiome and DNA virome exhibited predictable, coordinated age-associated succession with strong cross-domain coupling supported by virus-host networks. Functional profiling of the microbiome revealed that predicted carbohydrate substrates tracked the dietary transitions, while accessory viral functions partitioned by lifestyle and host. The early post-weaning stage was characterised by high abundance of viral integration and excision functions, as well as elevated resistome diversity that was almost exclusively of prokaryotic origin rather than viral. Importantly, 26 of the 25,223 vOTUs identified were predicted to target Streptococcus suis, providing the first metagenomic catalogue of such phages from pig oral environments. These findings expand our understanding of oral microbiome-virome dynamics and establish a framework for integrated microbiome and viromics approaches that could enable therapeutic phage discovery and inform microbiome-targeted interventions in pig production systems.

</details>

### [Infant formula composition is linked to distinct patterns of early gut colonization](https://www.biorxiv.org/content/10.64898/2026.11.20.768025v1)
*Fountouli, I.; Jayaprakash, Y.; Keizer, T. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.20.768025 v1 · relevance 0.08

- **In one sentence**: In 240 exclusively formula-fed infants in the Lifelines-NEXT cohort, variation in 62 reconstructed formula components was associated with gut species richness and with species-level colonization, notably higher iron linked to lower Bifidobacterium breve and B. bifidum and higher Clostridium paraputrificum, with in vitro iron-limitation assays partly consistent with these associations.
- **In plain words**: Babies fed infant formula, rather than breast milk, get formulas that differ in their mix of vitamins, minerals and other nutrients. This study reconstructed the contents of 17 formulas used by 240 infants during their first three months and checked how those contents lined up with which bacteria settled in the babies' guts. Some micronutrients, such as vitamin E and iodine, tracked with the number of bacterial species, and higher iron tracked with fewer Bifidobacterium and more Clostridium paraputrificum.
- **Why it matters**: Formula is the main feeding option for many infants, and early gut bacteria are linked to later health, so knowing that formula composition may steer which microbes establish themselves is useful. The lab tests on stool isolates offer some support for the iron findings, but the study is observational, so it shows association rather than cause, and the text does not establish health outcomes.
- **Background needed**: - Infant gut microbiota: the community of bacteria that colonizes the gut in the first months of life; it changes with diet.
- Infant formula: manufactured milk substitute whose vitamins, minerals and other components vary between brands.
- Species richness: how many different bacterial species are present in a sample.
- Bifidobacterium: a genus of bacteria common in breastfed and formula-fed infant guts.
- Clostridium paraputrificum: a gut bacterium species; the text does not describe its health role.
- Observational association: a link found in data that does not by itself prove the nutrient caused the change.
- In vitro growth assay: testing how bacteria grow in a lab dish under set conditions, here with limited iron.
- Iron limitation: growing bacteria in a medium with little iron to see which species cope. · level: intermediate

<details><summary>Original abstract</summary>

Early-life nutrition shapes the gut microbiota and can have long-term health implications. While infant formula feeding is widespread, it remains unclear how variations in its nutritional components shape microbiome colonization. Here, we reconstructed 62 components across the 17 infant formulas consumed during the first three months of life in 240 exclusively formula-fed infants in the Lifelines-NEXT birth cohort. Formula composition varied widely and several micronutrients, including vitamin E and iodine, were associated with species richness. Components were also associated with species-level colonization patterns. Higher iron content was associated with reduced Bifidobacterium breve and Bifidobacterium bifidum and increased Clostridium paraputrificum. Follow-up in vitro growth assays on infant-derived stool isolates showed that Bifidobacterium breve and Bifidobacterium bifidum tolerated iron limitation, while C. paraputrificum did not, consistent with the association signals. These findings show that infant formulas are not all alike and differences in component concentration affect microbiome colonization in early-life.

</details>

## Cancer biology

### [A hidden mitotic vulnerability emerges from BCAT1 redox-motif disruption in Ewing sarcoma](https://www.biorxiv.org/content/10.64898/2026.11.20.768122v1)
*Li, J.; Geyer, F. H.; Yershova, A. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.20.768122 v1 · relevance 0.05

- **In one sentence**: In Ewing sarcoma, disrupting the redox-active CXXC motif of BCAT1 (a metabolic enzyme driven by the EWSR1::FLI1 fusion) causes mitotic and DNA damage defects and sensitizes cells to combined CK2 and AURKB inhibition, which differs from simply removing the protein.
- **In plain words**: Ewing sarcoma is a bone and soft-tissue cancer in young people whose cells already run under high oxidative stress, meaning chemically reactive molecules that can damage cell machinery. The authors studied BCAT1, an enzyme that high-risk tumors express more, and altered just its chemically active site, the redox-active CXXC motif, while leaving its metabolic activity intact. Disrupting that motif made cells more sensitive to oxidative stress, caused errors when chromosomes divide, and reduced tumor growth and spread in animal experiments, whereas deleting the protein entirely had weaker effects.
- **Why it matters**: The paper suggests that a specific chemical site on a metabolic enzyme, rather than the enzyme itself, can be a target for cell division errors, and it proposes a drug combination (silmitasertib plus barasertib) that uses clinically evaluated inhibitors. Whether this translates to patients is not established by the text, which reports preclinical cell and animal work only.
- **Background needed**: - Oxidative stress: an excess of reactive oxygen molecules that can damage DNA and proteins.
- Redox motif (CXXC): a pair of cysteine amino acids in a protein that can gain and lose electrons, letting it act as a chemical switch.
- Chromosomal instability (CIN): a state where chromosomes are gained or lost during cell division, often harmful to cells.
- Mitosis: the stage of cell division where chromosomes are separated into two daughter cells.
- EWSR1::FLI1: an abnormal fusion protein that drives Ewing sarcoma.
- Prime editing: a gene-editing technique used here to change specific DNA letters in the cell's own gene.
- CK2 and Aurora kinase B (AURKB): enzymes that regulate cell division; silmitasertib and barasertib are inhibitors of them.
- Preclinical: tested in cells and animals, not yet in patient trials. · level: research-level

<details><summary>Original abstract</summary>

Cancer cells must keep oxidative stress and chromosome-segregation errors within tolerable limits to sustain rapid proliferation. Because redox homeostasis supports faithful chromosome segregation, disrupting redox-dependent mitotic safeguards could drive chromosomal instability (CIN) beyond cell tolerance and suppress tumor growth. Here, we investigated whether selectively disrupting redox-dependent safeguards could uncouple oxidative-stress adaptation from faithful chromosome segregation, exposing a therapeutic vulnerability at the interface of metabolic regulation and genome maintenance. We used Ewing sarcoma (EwS) as a model because it combines low genomic complexity with elevated oxidative stress and limited redox-buffering capacity. A survival analysis of cell-cycle-associated genes prioritized branched-chain amino acid transaminase 1 (BCAT1), whose high expression was associated with adverse outcomes in both primary and relapsed EwS. Functional genomics analyses revealed that BCAT1 is transcriptionally regulated by the EwS-specific EWSR1::FLI1 fusion oncoprotein through a distal enhancer-like GGAA microsatellite. Using prime-edited endogenous alleles and isogenic cell models, we found that disrupting BCAT1 redox-active CXXC motif increased sensitivity to oxidative stress and impaired recovery from it. Motif disruption also caused chromosome-segregation defects and DNA damage, reduced three-dimensional growth, and suppressed tumor formation and metastasis in vivo. By contrast, catalytic inactivation had limited effects. Although acute BCAT1 protein depletion reduced proliferation and tumor formation, constitutive BCAT1 knockout cells remained viable in culture and reduced tumor formation less than motif disruption. Mechanistically, CXXC motif disruption reduced casein kinase 2 (CK2) activity and increased Aurora kinase B (AURKB) activity, whereas BCAT1 degradation left CK2 activity unchanged and reduced AURKB activity. The enhanced sensitivity of CXXC-mutant cells to AURKB inhibition suggests a therapeutic vulnerability that could be exploited in BCAT1-wild-type EwS cells through combined CK2 and AURKB inhibition with silmitasertib and barasertib, increasing maximal growth inhibition and lowering the barasertib concentration required to suppress proliferation. Collectively, these findings reveal a mitotic vulnerability associated with BCAT1 redox-motif disruption that is not fully reproduced by protein loss and can be therapeutically exploited using clinically evaluated CK2 and AURKB inhibitors.

</details>

### [CIP2A is a biomarker for progression and poor prognosis in cutaneous squamous cell carcinoma](https://www.biorxiv.org/content/10.64898/2026.11.19.767767v1)
*Nissinen, L.; Tran, P.; Heiskanen, L. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.19.767767 v1 · relevance 0.04

- **In one sentence**: CIP2A, an inhibitor of the tumor-suppressing phosphatase PP2A, is elevated in cutaneous squamous cell carcinoma, promotes cancer cell growth via the MEK1/ERK1/2 pathway in vitro, and correlates with worse survival in patient samples.
- **In plain words**: This study looks at a common type of skin cancer, cutaneous squamous cell carcinoma, which is becoming more frequent. The researchers examined a protein called CIP2A, which tends to be present at higher levels in these tumors than in normal skin cells. Turning CIP2A down in cancer cells slowed their growth, and patients whose tumors showed strong CIP2A staining had worse disease-specific survival.
- **Why it matters**: It suggests CIP2A could help flag which skin tumors are likely to spread and may be a possible drug target for advanced cases. These are early-stage findings, though: the text reports laboratory cell experiments and patient tissue data, and does not show that targeting CIP2A helps patients.
- **Background needed**: - Cutaneous squamous cell carcinoma (cSCC): a skin cancer arising from the outer layer of skin cells (keratinocytes); it can spread to other parts of the body.
- Actinic keratoses and in situ cSCC: early or precancerous skin changes, compared here with invasive tumors and metastases.
- Protein phosphatase 2A (PP2A): an enzyme that switches off signaling proteins and normally acts as a tumor suppressor.
- CIP2A: a protein that inhibits PP2A, so its high levels can allow cancer-promoting signals to stay on.
- MEK1 and ERK1/2: part of a cell signaling chain that drives cell growth and division; the study reports that silencing CIP2A reduced their activation.
- siRNA: short RNA molecules used in the lab to switch off a specific gene.
- Kaplan-Meier analysis: a standard way of comparing survival over time between patient groups.
- Biomarker: a measurable marker that indicates disease status or likely outcome. · level: intermediate

<details><summary>Original abstract</summary>

The incidence of cutaneous squamous cell carcinoma (cSCC) is rising worldwide, highlighting the need for novel therapeutic options for recurrent and metastatic disease. Protein phosphatase 2A (PP2A) is a keyt tumor suppressor, and its inhibition promotes malignant progression. Here, we investigated the role of the cancerous inhibitor of PP2A (CIP2A) in cSCC progression. RNA-sequencing, oligonucleotide array-based expression, and qRT-PCR analysis demonstrated elevated CIP2A mRNA levels in cSCC cells compared with normal human epidermal keratinocytes (NHEKs). Western blotting confirmed higher CIP2A protein production in cSCC cells than in NHEKs. Analysis of single-cell RNA-sequencing data from cSCC showed CIP2A expression in epithelial cells and fibroblasts. Silencing CIP2A with specific siRNAs reduced cSCC cell growth and viability by inhibiting MEK1 and ERK1/2 phosphorylation. In vivo, strong CIP2A immunostaining was observed in tumor cells of primary cSCCs and cSCC metastases, whereas staining was absent or weak in all actinic keratoses and most cSCC in situ samples. Kaplan-Meier analysis revealed that patients with high CIP2A expression had significantly worse disease-specific survival than those with low expression. These findings identify CIP2A as a clinically relevant oncogene in cSCC progression, with elevated expression in invasive primary tumors and metastases. CIP2A may serve as a biomarker of cSCC progression and metastasis, as well as a potential therapeutic target in advanced and metastatic cSCC.

</details>

## Ecology and evolution

### [Social information use promotes breeding synchrony but constrains adaptation to rapid environmental changes](https://www.biorxiv.org/content/10.64898/2026.11.20.767538v1)
*Zheng, J.; Kuijper, B.; Aplin, L. M. et al.* · `animal behavior and cognition` · bioRxiv doi:10.64898/2026.11.20.767538 v1 · relevance 0.09

- **In one sentence**: An evolutionary individual-based model shows that breeders copying their neighbours' timing synchronises populations and speeds adaptation in stable conditions, but slows tracking of directional climate change.
- **In plain words**: Many animals decide when to breed by watching what their neighbours do, not only by sensing conditions themselves. This paper uses a computer simulation of populations living in territories with seasonal food peaks and a warming climate to ask whether copying neighbours helps or hurts timing of breeding. The authors report that copying makes individuals' timing converge, which helps populations adapt in stable or dramatically changing settings but leaves them lagging behind steady, directional climate shifts.
- **Why it matters**: Shifts in breeding timing are a well-known response to climate change, so the finding that group-following can make populations less responsive is relevant to conservation and to how animal populations may cope with warming. The text is a modelling study, so its conclusions depend on the model's assumptions and are not yet tested against field data in the given text.
- **Background needed**: - Phenology: the timing of seasonal events such as breeding or egg-laying.
- Social information: cues gained by observing others, such as neighbours' breeding dates, as opposed to private information from one's own sensing of conditions.
- Individual-based model: a simulation in which each virtual animal is tracked separately and can evolve over generations.
- Synchrony: many individuals acting at the same time, which can arise from positive feedback when copying amplifies early or late choices.
- Adaptive lag: when a population's average response trails a moving target, here the shifting best breeding time under climate change.
- Trade-off: a gain in one property (synchrony, faster adaptation) that comes at a cost to another (flexibility under directional change). · level: research-level

<details><summary>Original abstract</summary>

Animals use social information to make decisions, yet how such processes influence predictions in reproductive timing and population adaptation under environmental change remains unclear. While social information can improve decision accuracy through information pooling, spatiotemporal heterogeneity in conditions and patterns of environmental changes creates noise that potentially limits the value of social information use among breeding individuals. Here, we established an evolutionary individual-based model to examine how social and private sensing interact to shape breeding phenology in species distributed across territories with peaked resources and facing annual fluctuations and rapid climate change. We show that when individuals incorporate social information from neighbours, behavioural responses become increasingly synchronised through positive feedback in decision-making. This emergent synchrony helps populations to adapt faster and can increase reproductive output under stable environmental conditions relative to relying only on private information. However, under directional climate change, the same mechanism reduces population responsiveness by constraining variation in individual responses, leading to systematic lag in tracking shifting environmental optima and reduced population reproductive output. Our results demonstrate that social information use can produce a general trade-off at the population level between synchronisation and adaptive flexibility across environmental contexts. Social interaction enhances population performance when environments are either consistent or changing drastically across both spatial and temporal scales. Rather than uniformly improving performance, social interaction may create conditions under which collective behaviour becomes maladaptive when environments change rapidly.

</details>

### [No evidence of evolution of male fitness components in response to yeast deprivation: Putative female specific nutrient dependent reproductive adaptation](https://www.biorxiv.org/content/10.64898/2026.11.23.768529v1)
*Adhikary, S.; Pal, R. S.; Halder, S. et al.* · `evolutionary biology` · bioRxiv doi:10.64898/2026.11.23.768529 v1 · relevance 0.08

- **In one sentence**: Experimental evolution of Drosophila melanogaster under adult live-yeast deprivation for over 140 generations found no measurable change in male pre- and post-copulatory competitive fitness traits, suggesting the nutrient-driven female adaptation is sex-specific and not carried over via genetic correlation.
- **In plain words**: Fruit flies were raised for more than 140 generations on a diet without live yeast, a protein source that females need to make eggs. Earlier work had shown that the females adapted to this, becoming more fertile early in life, and this study asked whether males changed too. The authors measured a range of male traits linked to winning mating and fathering offspring, and found none had shifted.
- **Why it matters**: It tests whether a trait that evolves in one sex drags the other sex along through shared genes, a question that matters for how sexes can separately adapt. The text does not show how far the result generalises beyond these four laboratory populations and this one stress.
- **Background needed**: - Experimental evolution: populations are kept under a set condition for many generations to see how they change genetically.
- Intersexual genetic correlation: when genes that affect a trait in one sex also affect it in the other, so selection on one sex can change the other.
- Sexual antagonism: a gene that helps one sex but harms the other.
- Pre-copulatory traits (before mating, such as mating success) and post-copulatory traits (after mating, such as sperm competition) are both components of male fitness.
- Drosophila melanogaster is the common fruit fly, widely used in genetics.
- Absence of change is reported as "no evidence"; it does not prove that males could never change. · level: intermediate

<details><summary>Original abstract</summary>

Intersexual genetic correlation (IGC) is pervasive in sexually reproducing organisms and can constrain sex-specific adaptive evolution. Nevertheless, sexes frequently undergo adaptive divergence in response to novel ecological challenges. Here, we investigated whether adaptation to nutritional stress is sex-limited or constrained by shared genetic architecture. We utilized four laboratory-adapted populations of Drosophila melanogaster subjected to experimental evolution under adult-stage live-yeast deprivation for over 140 generations - a regime that previously drove adaptive female reproductive evolution, particularly enhancing early-life fecundity and ovarian function. Because female D. melanogaster rely heavily on dietary yeast for protein-dependent egg production, this evolutionary response may be female-limited. Alternatively, male fitness traits could respond either through direct selection or via correlated response driven by IGC. To distinguish between these hypotheses, we evaluated a comprehensive suite of pre- and post-copulatory male competitive fitness components. We found that all measured male fitness traits remained unchanged following experimental evolution, demonstrating that nutrient-dependent adaptation in these populations is strictly female-specific, with no evidence of correlated responses or sexually antagonistic trade-offs. Our results indicate that the genetic architecture underlying nutrient-dependent reproductive adaptation is largely decoupled between the sexes, allowing each sex to independently approach its sex-specific fitness optimum.

</details>

## Plant biology

### [Arabidopsis histone demethylase RSI1/FLD self-regulates its pathogen-induced expression](https://www.biorxiv.org/content/10.64898/2026.11.19.767995v1)
*Singh, U.; Patil, V.; Kumar, R. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.19.767995 v1 · relevance 0.05

- **In one sentence**: In Arabidopsis, the histone demethylase RSI1/FLD appears to repress its own pathogen-induced expression by removing H3K4me2/me3 marks near its transcription start site, with GSTT2 needed for that induction.
- **In plain words**: Plants fight infections in one leaf and then prime the rest of the plant for defense, a process called systemic acquired resistance. This paper studies a plant gene, RSI1/FLD, that is needed for that whole-plant defense and that is itself switched on when a pathogen arrives. The authors found that the gene's own activity is limited by its own product: the protein removes chemical marks from the gene's packaging, which dials its expression back down.
- **Why it matters**: The work suggests a self-limiting feedback loop that could keep a defense response from running too strong, which matters for how plants balance immunity and cost. The text does not show how broadly this applies beyond the experiments described, so its wider significance is uncertain.
- **Background needed**: - Systemic acquired resistance (SAR): a whole-plant immune state triggered after an initial local infection.
- Histone: a protein spool around which DNA is wrapped; chemical tags on histones affect how readily genes are read.
- H3K4me2 and H3K4me3: methyl tags on histone H3 that are generally linked to active genes; removing them usually turns genes down.
- Histone demethylase: an enzyme that strips methyl tags off histones.
- Transcription start site (TSS): the point where a gene's copying into RNA begins.
- ChIP (chromatin immunoprecipitation): a lab method to find which DNA regions a protein or tag sits on.
- GUS reporter: a marker gene whose activity shows when a promoter is switched on.
- Arabidopsis: a small flowering plant widely used as a model organism. · level: research-level

<details><summary>Original abstract</summary>

REDUCED SYSTEMIC IMMUNITY 1(RSI1)/FLOWERING LOCUS D (FLD) is essential for the activation of systemic acquired resistance (SAR). RSI1 functions as a repressor of gene expression by demethylating H3K4me2 and H3K4me3. RSI1 expression is induced both in local and systemic tissues upon pathogen inoculation. However, the mechanism of its induction or its expression regulation upon pathogenesis is not known. Here we show that RSI1 expression in SAR-induced rsi1 mutant plants is higher than WT plants, suggesting self-regulation. Pathogen-induced expression of RSI1 requires the function of GSTT2, a SANT domain-containing protein essential for SAR activation. Co-expression of RSI1 suppresses pRSI1:GUS activity in a transient assay system. Chromatin-immunoprecipitation (ChIP) experiments reveal that RSI1 physically associates near the transcription start site (TSS) of the RSI1 locus and facilitates demethylation of H3K4me2 and H3K4me3 at RSI1 locus. Our data altogether demonstrate that RSI1 negatively regulates its own expression as a possible mechanism of keep the SAR expression at an optimal level.

</details>

### [Zeaxanthin-dependent rapid energy quenching uncovers complexity of PsbS protonation](https://www.biorxiv.org/content/10.64898/2026.11.21.768332v1)
*Ponce, R.; Liu, E.; Niyogi, K. K. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.21.768332 v1 · relevance 0.04

- **In one sentence**: In Arabidopsis plants expressing PsbS variants with mutated lumen-facing protonatable residues (E122 and E226), the authors show a residual rapid energy-dependent quenching (qE) that tracks zeaxanthin and lumen acidification and is partly dependent on CP29.
- **In plain words**: Plants protect themselves from too much sunlight by releasing extra light energy as harmless heat, a process called energy-dependent quenching. This study looks at a protein called PsbS, which senses acidity inside the cell's energy-capturing membranes and helps trigger that heat release. The researchers altered the two sites on PsbS that take up acid and found the protein still switched on a small amount of heat release, which depended on a pigment called zeaxanthin and on a light-harvesting complex called CP29.
- **Why it matters**: The work challenges a simple picture in which PsbS acts alone when it is acidified, suggesting that its physical presence and its interactions with pigments and antenna complexes matter. The text does not say how these findings will translate to crop performance or other applications, so their wider significance remains uncertain.
- **Background needed**: - Photosynthesis captures light in membranes called thylakoids; excess light can damage the machinery, so plants have ways to shed extra energy as heat.
- Energy-dependent quenching (qE) is the fast heat-release response that switches on when the inside of the thylakoid becomes acidic (low pH) from strong light.
- PsbS is a protein in photosystem II that senses this acidity; its key sites are the acid-accepting residues E122 and E226 (amino acids glutamate).
- Zeaxanthin is a yellow plant pigment whose build-up during strong light supports heat release.
- CP29 is a small light-harvesting antenna protein that sits near photosystem II.
- A "null mutant" is a plant lacking a gene entirely; the authors used altered versions of the protein instead. · level: research-level

<details><summary>Original abstract</summary>

Rapid responses to changes in light intensity are crucial for photosynthetic organisms to regulate their light-harvesting capacity and optimize growth. PsbS, the S subunit of photosystem II (PSII) located in the thylakoid membrane, senses lumenal pH changes that reflect the balance between the light and carbon reactions of photosynthesis. Upon lumenal acidification caused by absorption of excess light energy, PsbS undergoes protonation of its lumen-exposed domain, triggering energy-dependent quenching (qE), which dissipates excess energy as heat. Despite extensive research, the precise molecular mechanism by which PsbS induces qE remains poorly understood. In this study, rather than relying solely on a PsbS null mutant, we used Arabidopsis lines expressing PsbS variants with mutations at the two essential protonatable residues (E122 and E226) in the lumenal domains to investigate the molecular interplay among PsbS, lumenal acidification, and zeaxanthin during qE induction. Our results indicate that this mutant PsbS protein can induce a small qE, the magnitude of which is strongly linked to both zeaxanthin accumulation and lumenal acidification. Furthermore, we found that the loss of the monomeric light-harvesting antenna complex CP29 in this mutant PsbS line reduced the small qE induction by nearly half. Together, our observations suggest that the physical presence of PsbS is essential for qE induction, which is driven by direct or indirect interactions between PsbS and zeaxanthin, potentially mediated by light-harvesting antenna complexes.

</details>

## Bioengineering and synthetic biology

### [Correlative mapping links extracellular matrix architecture to local mechanics in cardiac aging](https://www.biorxiv.org/content/10.64898/2026.11.21.768346v1)
*Ramli, M. F. H.; Ghosh, A.; Hengst, R. M. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.21.768346 v1 · relevance 0.06

- **In one sentence**: Correlative imaging and nanoindentation study that links extracellular matrix architecture descriptors (combined into an index, ArchI) to local Young's modulus in young versus aged murine myocardium, supported by synthetic geometries and a stochastic network model.
- **In plain words**: As the heart ages, the scaffolding around its cells (the extracellular matrix, made of proteins such as collagen) changes shape and arrangement, and the tissue can become stiffer. This paper measured several structural features of that scaffolding in young and old mouse hearts and combined them into a single score. It then pressed a tiny probe into thin heart slices to measure local stiffness and compared those stiffness readings with the collagen structure in the same spots.
- **Why it matters**: Stiffening of heart tissue is linked to age-related heart problems, so understanding how specific structural changes map onto local stiffness may help interpret that process. The text reports a positive association between the architecture score and stiffness, steeper in aged hearts, but it is a mouse study and does not show that these changes cause heart dysfunction.
- **Background needed**: - Extracellular matrix (ECM): the non-cellular network of proteins that gives tissue its structure; collagen, fibronectin and laminin are main components.
- Fibrillar collagen: collagen assembled into thick, rope-like fibers that resist stretching.
- Architectural descriptors: measurable features of an image, such as how much area is filled, fiber thickness and how connected the network is.
- Synthetic geometries and stochastic network model: computer-made or randomly generated fiber patterns used to test how each feature changes the index.
- Nanoindentation: pressing a very fine tip into a material to measure its stiffness, reported as Young's modulus (higher means stiffer).
- Immunofluorescence: staining specific proteins with fluorescent markers so they show up under a microscope.
- Age-adjusted regression: a statistical method that tests the link between two measures while accounting for the mice's age. · level: research-level

<details><summary>Original abstract</summary>

Cardiac aging is accompanied by extracellular matrix (ECM) remodeling, but how changes in matrix architecture relate to local tissue mechanics remains poorly understood. Here, we quantified six image-derived architectural descriptors across selected ECM components in young and aged murine myocardium and integrated them into an architectural index that we term 'ArchI'. Age-associated architectural changes differed among ECM components, with higher ArchI values observed for fibrillar collagen, fibronectin, and laminin-associated networks. To examine how defined structural changes affect the component descriptors, we developed controlled synthetic geometries and a stochastic network model. These analyses revealed index sensitivity to matrix occupancy, fiber width, and network continuity. We then combined nanoindentation of fresh cardiac tissue slices with subsequent immunofluorescence staining and imaging of collagen to correlate local tissue stiffness with ECM architecture in corresponding regions. Aged myocardium exhibited higher ArchI and Young's modulus, with local heterogeneity in their spatial correspondence. Age-adjusted regression revealed a positive association between ArchI and Young's modulus, with a steeper association in aged myocardium. Together, these findings reveal component-specific ECM remodeling during aging and provide a means to examine spatial structure-mechanics relationships in the aging heart.

</details>

### [Enhancing the Efficacy of Oncolytic Viruses by Engineering Virus Host Interactions Using CRISPR Cas13d](https://www.biorxiv.org/content/10.64898/2026.11.20.768134v1)
*Ameil, Z.; Kooshki Zamani, N.; Khalid, Z. et al.* · `synthetic biology` · bioRxiv doi:10.64898/2026.11.20.768134 v1 · relevance 0.05

- **In one sentence**: The paper builds a doxycycline-inducible CRISPR Cas13d system carried inside an oncolytic herpes simplex virus type 1 (oHSV1) to switch off tumor-cell antiviral genes during infection, and tests guide RNAs across several mouse and human tumor cell lines.
- **In plain words**: Oncolytic viruses are viruses engineered to infect and kill cancer cells, but tumor cells can fight back with their own antiviral defenses. This paper describes a genetic tool that lets researchers turn off chosen defense genes on a schedule, using a drug (doxycycline) as the switch, and places that tool inside the herpes virus itself. The authors report that the system works in principle and that the effect depends on which guide sequence is used, tested in three tumor cell types.
- **Why it matters**: Oncolytic viruses are an active cancer treatment approach, and limits from host antiviral responses are one reason they may underperform. A tool that can time the silencing of specific host genes could help test which defenses matter, though the text reports only cell-level readouts and does not show that tumors shrink or that treatment improves.
- **Background needed**: - Oncolytic virus: a virus modified to replicate in and destroy cancer cells.
- Herpes simplex virus type 1 (HSV1): a common human virus, here engineered as a cancer therapy.
- Antiviral response: a cell's built-in defenses that slow or stop viral replication.
- CRISPR: a gene-editing toolkit; Cas13d is a variant that targets and cuts RNA rather than DNA, lowering the amount of a given protein.
- Guide RNA (gRNA): a short RNA sequence that directs Cas13d to a specific target.
- Promoter (RNA polymerase III, p7SK): a DNA switch that controls how much guide RNA is made.
- Tet On / Tet Off: drug-controlled genetic switches that turn gene expression on or off when doxycycline is present or absent.
- Cell lines EMT6, CT26 (mouse) and 786-O (human kidney cancer) are standard lab tumor models.
- Fluorescence readouts are used as a proxy for how much virus or gene activity is present. · level: research-level

<details><summary>Original abstract</summary>

Oncolytic herpes simplex virus type 1 (oHSV1) is a promising cancer therapy, but tumor cell antiviral responses can restrict viral replication. Strategies for temporally controlled targeting of antiviral factors remain limited. Here, we developed an inducible CRISPR Cas13d platform to modulate host responses during HSV1 infection. We screened 13 pharmacological inhibitors across tumor models to identify pathways associated with restricted infection. Reporter assays identified Cas13d as the preferred effector over Cas13b, while endogenous-target experiments demonstrated Cas13d mediated reductions in target protein abundance. We optimized guide RNA expression using RNA polymerase III promoters, selected p7SK, and established doxycycline-responsive Tet On and Tet Off systems. The platform was incorporated into HSV1 to generate a gRNA library targeting 15 host antiviral genes, together with two non-targeting controls. Doxycycline-dependent reporter readouts demonstrated inducible activity. Evaluation in EMT6, CT26, and 786 O cells revealed guide-dependent differences in fluorescence. These findings establish a programmable framework for investigating virus host interactions during oncolytic HSV infection.

</details>

## Mathematical biology (arXiv)

### [Beyond the Blueprint: The Continuing Evolution of Turing's Theory of Morphogenesis](https://arxiv.org/abs/2611.30543)
*Andrew L. Krause, Kevin J. Painter, Denis J. Headon* · `q-bio.CB` · arXiv:2611.30543v1 · relevance 0.06

- **In one sentence**: A historical and critical review of how Alan Turing's reaction-diffusion theory of pattern formation has been developed, applied, and sometimes oversimplified in contemporary biology, with a call for new conceptual frameworks.
- **In plain words**: This paper looks back at Alan Turing's 1952 idea that chemicals reacting and spreading through tissue could produce spots and stripes in living things. It traces how that idea has been taken up and reworked by biologists over the decades. The authors argue that some uses of the theory are useful, while simple claims that "Turing patterns explain this" deserve caution, and they outline open problems that will need several fields working together.
- **Why it matters**: Turing's model is one of the most cited ideas about how animal markings, limb spacing, and tissue layouts might arise without a blueprint, so a careful check on what it can and cannot explain matters for experimental work. The text itself does not give specific new results, so its value lies mainly in its critical synthesis rather than in any single finding.
- **Background needed**: - Morphogenesis: the process by which an organism's shape and pattern form during development.
- Reaction-diffusion: a model where two or more chemicals react with each other and spread out at different rates, which can spontaneously create regular patterns.
- Turing's 1952 paper "The Chemical Basis of Morphogenesis" proposed this mechanism as a way patterns could emerge from uniform starting conditions.
- Darwin's phrase "endless forms most beautiful" refers to the enormous variety of living forms.
- The paper is a review and perspective; it contains no experiments or numerical results in the provided text. · level: intermediate

<details><summary>Original abstract</summary>

Turing's article ``The Chemical Basis of Morphogenesis'' has profoundly influenced conceptual views on the emergence of biological form across scales and species. It has also served as a foundational framework to guide experimental investigations into the mechanisms that underlie pattern formation. In this article, we trace the historical development of Turing's ideas and examine their integration into contemporary research programs. We critically assess the broad and often overlapping concepts that have derived from Turing's work, both highlighting value in productive applications of the theory and suggesting that skepticism should remain in overly simplistic validations. By clarifying these concepts and their intrinsic limitations, we rethink contemporary approaches aimed at understanding the essential principles that govern biological pattern formation. We pose some important challenges that will require interdisciplinary expertise to overcome, and which will necessitate fundamentally new paradigms to understand the physical origin of Darwin's ``endless forms most beautiful''.

</details>

### [General-purpose language models are neurosymbolic reasoners able to annotate proteins from sequence](https://arxiv.org/abs/2611.28529)
*Christopher J. Mungall, Marcin P. Joachimiak* · `q-bio.GN` · arXiv:2611.28529v1 · relevance 0.04

- **In one sentence**: Preliminary evaluation finding that general-purpose frontier language models, prompted with raw protein sequences alone, perform above chance on several protein annotation tasks (Pfam domain location, loss of catalytic residues, structure and activity prediction), without being benchmarked against specialised tools.
- **In plain words**: Scientists want to work out what jobs genes and the proteins they encode do, across all living things. This paper asks whether general chatbot-style AI models, which are trained mostly on text rather than biology, can read a protein's amino-acid sequence and label it correctly. The authors report that the models did clearly better than guessing on every task they tried, but they also made confident-sounding mistakes, and they did not compare the models against dedicated biology tools.
- **Why it matters**: It challenges the common assumption that text-trained models and sequence-trained biology models are good at different things and cannot cross over. If it holds up, combining sequence data, experimental results and literature knowledge in one model could help annotate the large number of proteins that currently have no known function. The text is a short preliminary report, so its practical value is still unclear.
- **Background needed**: - Protein: a chain of amino acids, encoded by a gene; its sequence is a string of letters.
- Functional annotation: labelling what a gene or protein does (its job, domains, or active sites).
- Pfam domain: a named, recognised building block of a protein, with known positions along the sequence.
- Catalytic residue: an amino acid essential to a protein's chemical activity; losing it usually means the protein no longer works.
- Language model: an AI system trained to predict text (or sequences treated like text); "frontier" means the most capable current general models.
- Protein language model: a model trained specifically on protein sequences.
- Neurosymbolic: combining learned pattern-recognition (neural) with explicit rule-like knowledge (symbols).
- Hallucination: a confident but incorrect output from an AI model.
- Specialised tools: established, purpose-built bioinformatics software, which the authors did not compare against. · level: intermediate

<details><summary>Original abstract</summary>

Determining the function of genes across the tree of life is one of the major challenges in biology. Generative AI approaches to this problem generally fall into two categories: language models trained on biological sequences that are able to predict structure and function from signals in those sequences; and generalist language models trained on text, that are able to reason about biological function symbolically. A default operating assumption is that protein language models do not perform well on symbolic tasks, and that generalist language models do not perform well on sequence tasks. However, a recent report showed that frontier generalist models perform surprisingly well on next-residue prediction tasks. We set out to explore whether these capabilities extended to protein annotation. We assigned different frontier generalist models a variety of protein annotation tasks, including predicting the presence and coordinates of Pfam domains, loss of functional catalytic residues, and predicting structure and activity. On all annotation tasks, the frontier models performed well above chance; we did not benchmark them against specialised tools. The models also make characteristic hallucination errors, and they state them as confidently as their correct calls. Though untested against specialised methods, the nascent ability of frontier models to perform protein annotation from sequence alone is intriguing. The ability to reason over sequence, structure, and symbols in a single model allows for a neurosymbolic approach where a combination of sequence, experimental data and knowledge from the literature can be holistically combined to improve on de novo functional annotation of the protein universe. Prompts, test sets, model outputs and code: https://github.com/ai4curation/fable-sequence-to-function. Summary of results: https://ai4curation.io/fable-sequence-to-function/

</details>

## Epidemiology

### [Sources of protein in UK adults following contemporary plant-based diets: findings from the Feeding the Future (FEED) Study](https://www.medrxiv.org/content/10.64898/2026.11.23.26368579v1)
*Lawson, I.; Bell, W.; Key, T. J. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.23.26368579 v1 · relevance 0.05

- **In one sentence**: Cross-sectional analysis of the UK Feeding the Future (FEED) cohort (n=6,113) quantifying food-group sources of protein intake across omnivore, flexitarian, pescatarian, vegetarian and vegan diets, and the share of each group below the estimated average requirement (EAR) for protein, with and without excluding under-reporters.
- **In plain words**: This study looks at where protein comes from in the diets of about 6,000 UK adults who eat different ways, from meat-eaters to vegans. The researchers used an online food questionnaire to work out which foods supplied the protein and how many people got less than the estimated minimum they need. Grains and dairy were major sources across most groups, while vegans relied more on plant foods such as meat alternatives, legumes, nuts and seeds. Few people fell short, and most of the gap seen in vegetarians and vegans disappeared once people who likely under-reported their eating were removed.
- **Why it matters**: Plant-based diets are increasingly common, and a common worry is whether they supply enough protein. This paper gives a detailed picture of protein sources in a recent UK sample, and it shows that the apparent shortfall depends heavily on how under-reporting is handled. Its findings come from self-reported questionnaire data, so they describe associations in one cohort rather than establishing how adequate any diet is for health.
- **Background needed**: - Protein is needed for building and repairing body tissue; the EAR (estimated average requirement) is the amount that meets the needs of half of people in a group, so "below EAR" means a group-level shortfall, not necessarily a deficiency in an individual.
- Food frequency questionnaire: a survey asking how often people eat listed foods, used to estimate typical intake.
- Under-reporters: people whose reported energy intake is implausibly low compared with their needs, suggesting they under-recorded what they ate; excluding them changes results.
- Cross-sectional: data collected at one point in time, so it shows patterns, not cause and effect.
- Diet groups: omnivores eat everything; flexitarians mostly plant-based with occasional meat; pescatarians eat fish but no meat; vegetarians eat no meat or fish; vegans eat no animal products.
- Plant-based meat alternatives are processed products (for example, soy or pea-based) designed to resemble meat. · level: intermediate

<details><summary>Original abstract</summary>

Objective To identify and quantify sources of protein intake in United Kingdom (UK) adults following different diets, and assess how these sources contribute to meeting protein requirements. Design Cross-sectional analysis of the Feeding the Future Study (FEED), a UK cohort recruited in 2022-2023. Dietary intake was assessed using an online food frequency questionnaire. We calculated the percentage contribution of food groups to daily protein intake, and the proportion of participants meeting the estimated average requirement (EAR) for protein, with and without exclusion of under-reporters. Setting A contemporary cohort of UK adults. Participants 6,113 adults: 1,540 omnivores, 1,322 flexitarians, 547 pescatarians, 1,212 vegetarians, and 1,492 vegans. Results Grains contributed 10-30% of total protein intake across all groups. Dairy contributed 12.9-14.2% in non-vegan groups, while plant-based dairy alternatives contributed less in vegans (7%), mainly from soy milk (4.3%). Other major contributors (>10%) were meat for omnivores (33.0%) and flexitarians (13.5%); fish for pescatarians (14.9%); plant-based meat alternatives for vegetarians (12.0%); and plant-based meat alternatives (15.0%), legumes and pulses (10.5%), and nuts and seeds (10.5%) for vegans. The proportion below the protein EAR ranged from 1.9% in omnivores to 14.0% in vegans, falling to 0.01% and 3.6% respectively, after excluding under-reporters. Conclusions Grains were a major contributor to protein intake across all diet groups, as was dairy in all non-vegan groups. Protein sources were more varied in non-omnivorous groups, particularly vegans. Few participants fell below the protein EAR and the higher proportions among vegetarians and vegans were largely attenuated after excluding under-reporters.

</details>

### [Disease-anchored organ aging clocks enable multi-organ risk profiling from routine labs](https://www.medrxiv.org/content/10.64898/2026.11.22.26368688v1)
*Shi, C.; Sun, Y.; Ruan, X. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.22.26368688 v1 · relevance 0.05

- **In one sentence**: The paper trains organ-specific aging clocks on first disease onset using routine blood lab tests (rather than proteomics and chronological age), freezes them, and tests whether they track own-organ disease across UK Biobank, NHANES and JMDC cohorts.
- **In plain words**: Doctors can estimate how old a person's organs are by looking at markers in their blood, but the existing methods rely on expensive protein measurements and are tuned to a person's calendar age, so they do not say much about which organ disease is coming. This study built a set of organ "clocks" trained on which people went on to develop disease in each organ, using ordinary lab tests. The authors report that these clocks mainly pick out their own organ's proteins and flag people at higher risk of their own organ's disease, and that they still work in other cohorts.
- **Why it matters**: If organ-age readings from routine blood tests can flag which organ is at risk, they could be a cheap way to screen for multi-organ disease risk. The text reports the clocks add information to existing clinical risk scores, but it gives no effect sizes here, so the practical value is still unclear.
- **Background needed**: - Biological age: an estimate of how worn-out a body is, which can differ from calendar age.
- Organ clock: a model that estimates the age of one organ from blood measurements.
- Proteomics: measuring thousands of proteins in blood; costly and not routine.
- UK Biobank, NHANES, JMDC: large health cohort datasets (UK, US, Japan) used to train and test such models.
- First onset: the first time a person is diagnosed with a given disease, used as the training outcome.
- Frozen coefficients: the model's weights are fixed after training and applied unchanged to new data.
- Random protein panels: size-matched sets of random proteins used as a control to check whether a clock's signal is specific.
- Clinical risk score: a standard formula that estimates disease risk from routine patient information. · level: research-level

<details><summary>Original abstract</summary>

Organ clocks estimate the biological age of organs from blood, but current clocks assign tissue-enriched proteins to organs and train on chronological age, which requires proteomics and does not yield organ-specific disease risk. In the UK Biobank, we trained organ clocks on first onset of disease of each organ using routine laboratory tests and froze the coefficients. Under an age label, organ-clock readouts arose equally in size-matched random protein panels; with a disease label, clocks selected their own organ's proteins and predicted their own organ's diseases. Defining extreme aging by multiples of disease risk concentrated flags on own-organ disease. Frozen clocks kept organ correspondence in the US NHANES cohort, predicted first onset of own-organ disease in the Japanese JMDC cohort and added more information to clinical risk scores than current organ clocks. Trained once where disease follow-up exists, organ clocks can be used wherever routine laboratory tests are measured.

</details>

## Infectious diseases

### [Safety and microbiological activity of a combined phage cocktail in persons with cystic fibrosis colonized with Achromobacter: Study protocol for a phase 1, investigator-initiated, randomized clinical trial.](https://www.medrxiv.org/content/10.64898/2026.11.22.26368705v1)
*Massey, J.; Hughes Kramer, K.; Snook Barrett, S. et al.* · `infectious diseases` · medRxiv doi:10.64898/2026.11.22.26368705 v1 · relevance 0.05

- **In one sentence**: A registered phase 1 protocol for a randomized, open-label pilot testing the safety, tolerability, and early pharmacokinetics of a four-phage cocktail (AchromoPhage) given intravenously, by inhalation, or both, in 12 adults with cystic fibrosis and Achromobacter lung infection.
- **In plain words**: This is a plan for a small first-in-people safety trial of a mixture of four viruses that kill a bacterium called Achromobacter, which can cause serious lung infections in people with cystic fibrosis. Twelve adults will be split into three groups receiving three weekly doses by vein, by breathing it in, or both, and researchers will track side effects, lung function, quality of life, and how the viruses move through the blood and airways. The text describes the design only; no results are reported.
- **Why it matters**: Phage therapy is an understudied option for drug-resistant bacteria, and the authors note that clinical trial data in people with cystic fibrosis are scarce and that Achromobacter has not been studied in trials before. Results would help judge whether phages are safe and how they behave in the body, but this protocol alone shows no evidence of effectiveness.
- **Background needed**: - Cystic fibrosis (CF) is an inherited condition that causes thick mucus and chronic lung infections.
- Achromobacter is a group of Gram-negative bacteria (a bacterial category with a protective outer membrane) that are often resistant to many antibiotics.
- Bacteriophages ("phages") are viruses that infect and kill specific bacteria; they are not active against human cells.
- "Obligately lytic" means the phages only reproduce by bursting the bacterial cell rather than living alongside it.
- Phase 1 trials mainly test safety and dosing, not whether a treatment works.
- Pharmacokinetics means how a drug is absorbed, spread, and cleared from the body.
- Neutralizing antibodies are immune proteins that can block a virus; their appearance may limit repeated phage dosing.
- FEV1 is a standard spirometry measure of how much air a person can forcefully exhale in one second. · level: intermediate

<details><summary>Original abstract</summary>

Background: Achromobacter are a genus of difficult-to-treat, frequently multi-drug-resistant Gram-negative bacteria that can cause severe infections in people with cystic fibrosis (pwCF). Bacteriophages are an understudied yet promising therapy for these and other antibiotic-resistant bacteria. However, data are largely limited to case reports or series, and clinical trials among pwCF to date have not evaluated Achromobacter. Methods: This is an investigator-initiated, open-label, randomized phase 1 pilot trial to evaluate the safety, tolerability, and biological effects of AchromoPhage, a cocktail of four genetically distinct, obligately lytic Achromobacter-targeting phages (phiACH01, phiACH04, phiACH06, phiACH07) with broad activity against Achromobacter species, in 12 adult participants with CF and pulmonary Achromobacter infection. Twelve participants will be randomized into three groups to receive a total of three, increasing, weekly doses of the AchromoPhage cocktail via one of three routes: 1) intravenous, 2) via inhalation, or 3) or intravenously and inhaled. Participation in the trial will span approximately 7 weeks, which will consist of outpatient phage dose administrations, safety and symptom monitoring, and longitudinal collection of biospecimens for protocol-specified and exploratory analyses through Day 42. The primary safety endpoint is the occurrence of treatment-related Grade 4 or greater adverse events. Secondary endpoints include longitudinal changes in FEV1 by spirometry, longitudinal changes in health-related quality of life, pharmacokinetics of each of the four phages in blood and the respiratory tract, and emergence of a phage neutralizing antibody response in serum. Discussion: While existing case anecdotes and observational studies suggest that phages are safe and may have a role in treating human infections, there is a paucity of clinical trials studying the adverse effect profile and basic pharmacological parameters of phages. This trial will study the safety and explore the pharmacokinetic and other properties of a four-phage cocktail in patients with CF and chronic Achromobacter lung infection. Trial registration: ClinicalTrials.gov NCT0727590. Registered on 12/10/2025

</details>

## Public and global health

### [Procedure composition, age and race/color in gender-affirming surgical authorizations of the Brazilian public health system, 2014-2025](https://www.medrxiv.org/content/10.64898/2026.11.23.26368723v1)
*dos Santos, J.; Amorim Costa, C. M.* · `public and global health` · medRxiv doi:10.64898/2026.11.23.26368723 v1 · relevance 0.09

- **In one sentence**: A nationwide descriptive study of 1,375 Brazilian public-system (SUS) hospital authorizations for gender-affirming surgery from 2014 to 2025, classifying procedures by feminizing or masculinizing direction using versioned procedure codes, with a reproducibility check against the original public files.
- **In plain words**: This paper looks at records of surgeries that Brazil's public health system paid for, to see how gender-affirming operations changed between 2014 and 2025. The records show billed procedures and their codes, but not who the patients are, how they identify, or whether surgery was medically needed. The authors found that the share of feminizing procedures fell over time, and that the equal counts seen in 2024–2025 came from very different mixes of operations.
- **Why it matters**: Publicly funded gender-affirming care is a contested policy area, and administrative billing data are one of the few nationwide sources available. The paper's main message is methodological: it argues that monitoring should use procedure-specific indicators and versioned code definitions, and that questions of access and equity need person-level or patient-reported data that these records lack.
- **Background needed**: - SUS (Sistema Único de Saúde): Brazil's publicly funded national health system.
- Hospital Information System (SIH): the administrative database that records hospital admission billing across Brazil.
- Authorization (AIH): a record of a billed hospital admission; it describes procedures, not diagnoses or patient identity.
- Procedure codes: standard billing codes whose meaning can change across versions, so the classification must be dated.
- Feminizing vs. masculinizing surgery: the direction of the procedure inferred from its code, e.g., breast reconstruction vs. mastectomy.
- Descriptive study: it reports counts and shares; it does not test causes or estimate population rates.
- Race/color category "parda" (brown): a self-classification category used in Brazilian official statistics.
- Habilitated hospitals: hospitals formally approved by the health ministry to perform these surgeries. · level: intermediate

<details><summary>Original abstract</summary>

Hospital admission authorizations from publicly financed health systems are increasingly used to describe gender-affirming surgery, although they record billed procedures whose feminizing or masculinizing direction can be inferred from the code, without identifying people, self-reported gender identity or clinical need. This nationwide descriptive study examined the authorizations for gender-affirming surgery processed by the Brazilian Unified Health System from 2014 to 2025, which were selected from 3,888 public monthly state files of the Hospital Information System with a historically versioned classification of procedure codes. Of the 1,375 selected authorizations, 711 corresponded to directly feminizing procedures, 428 to directly masculinizing procedures and 236 to a complementary procedure that was analyzed separately. The feminizing share of the directly classified authorizations decreased from 81.7% (196/240) in 2014-2018 to 72.2% (213/295) in 2019-2023 and to 50.0% (302/604) in 2024-2025, proportions that describe composition within periods of unequal length and cannot be read as population rates. In 2024-2025, bilateral mastectomy accounted for 264 of the 302 masculinizing authorizations (87.4%), whereas bilateral breast reconstruction with silicone implants accounted for 118 of the 302 feminizing authorizations (39.1%). The median recorded age was 35 years in feminizing and 30 years in masculinizing authorizations over the whole period, and 34 and 29 years when the comparison was restricted to 2024-2025. The brown (parda) race/color category was recorded in 42.6% (303/711) of feminizing and 61.0% (261/428) of masculinizing authorizations, in a comparison pooled over the whole period and not adjusted for period or procedure. The number of hospitals habilitated for these surgeries remained at five from 2014 to 2022 and doubled in 2023. All aggregate results were reproduced by an independent pipeline that re-read every original public file. It was observed that the equal numbers of feminizing and masculinizing authorizations in the most recent period resulted from markedly different procedure portfolios, which suggests that the monitoring of publicly funded gender-affirming surgery may benefit from procedure-specific indicators and versioned code definitions, while questions of access and equity would require person-level and patient-reported data.

</details>

### [Association between Social Media Exposure and Self-Medication Practices: Public Health Implications in Punjab, Pakistan](https://www.medrxiv.org/content/10.64898/2026.11.22.26368645v1)
*Ashraf, A.; Saddique, M. A. B.; Sajid, M. S. et al.* · `public and global health` · medRxiv doi:10.64898/2026.11.22.26368645 v1 · relevance 0.06

- **In one sentence**: A cross-sectional survey of 280 adults in Punjab, Pakistan (March–May 2026) describes self-medication and social-media exposure and examines associations with usage frequency, demographics, and attitudes toward advertised medicines, with the overall regression model not statistically significant.
- **In plain words**: This study looks at whether seeing medicine information on social media is linked to people taking medicines on their own without seeing a doctor or pharmacist. Researchers surveyed 280 adults in Punjab, Pakistan, and found that most reported taking medicines without consultation at least occasionally. Some links appeared, such as with daily time spent on social media, age, and believing that advertised medicines are safe, but the overall model was not statistically significant.
- **Why it matters**: Self-medication is a common public health concern, and social media is an increasingly common source of health information, so the question matters for health communication. The study is small, uses a single snapshot in time, and cannot show cause and effect, so it is best read as a preliminary signal rather than evidence that social media drives medicine misuse.
- **Background needed**: - Self-medication: taking medicines on one's own, without a doctor's or pharmacist's advice.
- Cross-sectional survey: a one-time questionnaire that captures associations at a single point, not changes over time.
- Chi-square test: a statistical check of whether two categories (e.g., exposure and behaviour) are related more than chance would suggest.
- Multinomial logistic regression: a model that estimates how several factors together relate to one outcome with several categories (here, rarely, frequently, more often).
- p-value: the probability of seeing results at least this strong if there were no real link; below 0.05 is conventionally called significant.
- Nagelkerke R²: a rough 0–1 measure of how much variation the model explains; 0.205 is modest.
- Likelihood-ratio test: a way to check whether dropping a factor from a model worsens its fit.
- Sample caveats: 280 participants, aged 18–60, from one province; the authors note limitations in sample composition. · level: intermediate

<details><summary>Original abstract</summary>

Background: Social media has become an important source of health information, including information about medicines. Exposure to medicine-related content may affect decisions to use medicines without professional consultation. Objective: To describe self-medication practices and social-media exposure among adults in Punjab, Pakistan, and explore associations between self-medication frequency and demographic, social-media-use, and attitudinal factors. Methods: A cross-sectional analytical survey was conducted among adults aged 18-60 years in Punjab between March and May 2026. The final analytic sample comprised 280 participants. A bilingual (Urdu/English) questionnaire assessed demographics, social-media use and health-content exposure, self-medication in the preceding six months, medicine categories, and attitudes. The questionnaire was reviewed by two clinical experts and piloted among 30 participants. Descriptive analyses, chi-square tests, and multinomial logistic regression were reported using IBM SPSS Statistics; significance was set at alpha = 0.05. Results: Self-medication frequency was reported as Rarely by 117 participants (41.8%), Frequently by 130 (46.4%), and More Often by 33 (11.8%). Fever medicines were reported by 179 participants (63.9%) and gastrointestinal medicines by 96 (34.3%); multiple-response medicine categories were not mutually exclusive. Instagram was the most frequently selected social-media platform. Advertisement recall differed across self-medication frequency groups (chi-square (22) = 35.28, p = .036). Belief that medicines shown in advertisements/posts were safe was associated with self-medication frequency (chi-square (4) = 14.26, p = .007), while perceived risk was not (chi-square (4) = 1.587, p = .811). The multinomial model's overall test was not statistically significant (chi-square (40) = 54.07, p = .068; Nagelkerke R2 = .205). Likelihood-ratio tests identified associations for daily social-media-use duration (chi-square (2) = 13.085, p = .001), age group (chi-square (6) = 14.930, p = .021), and perceived advertisement safety (chi-square (4) = 10.899, p = .028). Conclusion: Self-medication was commonly reported in this sample. Some social-media-use and advertising-attitude variables were associated with self-medication frequency, but the overall regression model was not statistically significant and the cross-sectional design cannot establish causality. Findings should be interpreted cautiously given the sample composition and reported data limitations.

</details>

## Psychiatry and neurology

### [Plasma proteomic markers of cognitive and brain aging in a multi-ethnic cohort](https://www.medrxiv.org/content/10.64898/2026.11.22.26368682v1)
*Wood, B.; Wood Alexander, M.; Clappison, A. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.22.26368682 v1 · relevance 0.10

- **In one sentence**: A plasma proteomics study measuring 220 blood proteins in a multi-ethnic older cohort, relating them to cognition, brain MRI markers, and cognitive decline, with replication in ADNI participants.
- **In plain words**: Researchers measured about 220 proteins in blood samples from 250 older adults of Chinese, South Asian, and non-Hispanic White background. They looked for proteins linked to thinking ability and brain scan measures, such as markers of brain-cell damage (including a tau protein form), inflammation, and small blood-vessel disease. Several of these links were checked again in a separate group of about 1,381 people from the Alzheimer's Disease Neuroimaging Initiative.
- **Why it matters**: Most Alzheimer's and brain-aging research has been done in people of European descent, so testing blood markers in more diverse groups matters for whether they generalize. The text reports associations, not proof that these proteins cause brain decline, so they are candidate markers that would need further study before any clinical use.
- **Background needed**: - Plasma proteomics: measuring many proteins at once in a blood sample; here an ultrasensitive assay (NULISAseq) covering 220 brain-related proteins.
- Tau: a protein that forms tangles inside brain cells in Alzheimer's disease; BDpTau is a form of tau thought to come from the brain and detectable in blood.
- Entorhinal thickness: thickness of a brain region involved in memory, seen on MRI, often thinner early in Alzheimer's.
- Cerebral small vessel disease: damage to the tiny blood vessels deep in the brain, visible on MRI.
- Association vs. causation: a link between a protein level and a outcome does not show the protein drives the outcome.
- ADNI: a large, long-running North American study of people with and without memory problems, used here as a replication group. · level: research-level

<details><summary>Original abstract</summary>

Advances in ultrasensitive proteomics offer opportunities to characterize molecular pathways underlying brain aging. We measured 220 plasma proteins using NULISAseq Neuro220 in 250 Chinese, South Asian, and non-Hispanic White older adults (mean age=68.2 years, 70.4% female). Proteins implicated in neurodegenerative diseases (including brain-derived phosphorylated Tau, BDpTau), synaptic function, oxidative stress, and inflammation were associated with poorer cognition. Phosphorylated Tau205 was associated with reduced entorhinal thickness, whereas inflammatory proteins were associated with imaging markers of cerebral small vessel disease. Several findings were replicated in 1,381 participants in the Alzheimer's Disease Neuroimaging Initiative, including associations of BDpTau species, NPTX2, BACE1, TREM1, CCL17, PRDX6, and IGF1R with cognitive decline and clinical progression. Cardiometabolic risk factors were associated with widespread proteomic alterations, many of which were also linked to poorer brain health. These results identify promising molecular markers of brain aging and extend proteomic research to ethnically diverse populations historically underrepresented in Alzheimer's disease research.

</details>

### [Remote auditory task performance, cognition, and APOE4 across two dementia-risk cohorts](https://www.medrxiv.org/content/10.64898/2026.11.19.26368469v1)
*Happs, C.; Toma, A.; Koychev, I. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.19.26368469 v1 · relevance 0.07

- **In one sentence**: Two independent cohorts (164 older Great Minds adults, 90 mid-life PREVENT participants) completed the same remote auditory battery, and the study finds no link between APOE ε4 carrier status and auditory performance, with some links to memory only in the older group.
- **In plain words**: Hearing speech in noise is known to go along with thinking decline and dementia risk. This study asked whether online hearing and listening tests reflect the gene APOE ε4, the strongest common genetic risk factor for Alzheimer's disease, or just general ageing and thinking skills. In two groups of people, the tests did not track the gene, but in the older group better scores on some tests went with better memory learning.
- **Why it matters**: Remote tests are cheap and easy to scale, so knowing what they measure matters if they are ever used to screen for dementia risk. The paper is cautious: the samples are modest, so it cannot rule out small gene effects, and it only looks at one point in time, so it cannot say whether these tests predict later decline.
- **Background needed**: - APOE ε4 is a gene variant that raises the risk of Alzheimer's disease; "carrier" means a person has at least one copy.
- Digits-in-noise and speech-in-babble tests ask people to repeat numbers or words over background sound; they measure how well speech is understood in noise.
- Working-memory precision means how accurately someone holds and reproduces a sound (here a tone frequency or a rate of loudness fluctuation) in mind.
- Robust regression is a statistical method that is less thrown off by outliers; false-discovery-rate correction guards against false positives when many tests are run.
- Cohorts: Great Minds is a register of older adults; PREVENT Dementia follows people in mid-life.
- The Goldsmiths Musical Sophistication Index measures musical skill and engagement. · level: intermediate

<details><summary>Original abstract</summary>

Background. Difficulty hearing speech in noise is associated with cognitive ageing and dementia risk. It is unclear whether performance on remote auditory tasks reflects the apolipoprotein E (APOE) {epsilon}4 allele, the strongest common genetic risk factor for Alzheimers disease, or broader cognitive and ageing processes. Methods. We analysed two independent cohorts: the Great Minds research register of older adults and the mid-life PREVENT Dementia programme. Both completed the same remote auditory battery: digits-in-noise, speech-in-babble, auditory working-memory precision for tone frequency and for amplitude-modulation rate, and the Goldsmiths Musical Sophistication Index. Cognitive outcomes were paired-associate learning in Great Minds, and the Four Mountains Task, Supermarket Task and selected COGNITO scores in PREVENT. Associations were tested with covariate-adjusted robust regression and false-discovery-rate (FDR) correction. Results. The analytic samples comprised 164 Great Minds and 90 PREVENT participants (mean age 70.6 vs 56.8 years). APOE {epsilon}4 carrier status was not associated with any auditory measure in either cohort (all FDR-corrected p>0.70). In Great Minds, better speech-in-babble performance and better amplitude-modulation-rate working-memory precision were each associated with better paired-associate learning (both FDR-corrected p=0.019). In PREVENT, no auditory measure was associated with spatial-memory or COGNITO scores after age and sex adjustment and FDR correction. Conclusions. Remote auditory task performance was associated with memory in the older cohort but not with APOE {epsilon}4 carrier status in either cohort, although the samples could not exclude small genotype effects. Longitudinal studies are needed to determine whether remote auditory testing predicts cognitive change.

</details>

## Oncology

### [Direct tumour-adipocyte contact / Stroma AReactive Invasion Front Areas (TAC/SARIFA) in advanced oropharyngeal cancer](https://www.medrxiv.org/content/10.64898/2026.11.22.26368676v1)
*Haas, S.; Maerkl, B.; Peiper, A. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.22.26368676 v1 · relevance 0.03

- **In one sentence**: A monocentric retrospective study of 78 advanced (pT3–pT4) oropharyngeal squamous cell carcinomas assessing whether tumour-adipocyte contact (TAC/SARIFA) on routine H&E slides relates to overall survival, recurrence-free survival, p16 status, and nodal findings.
- **In plain words**: This paper looks at a feature seen under the microscope in throat cancers (oropharyngeal cancer): where the tumour meets fat cells at its outer edge. The researchers examined tissue from 78 patients treated between 2005 and 2023, including their lymph nodes, and checked whether this feature was linked to survival, recurrence and other tumour traits. The feature was linked to shorter overall survival and to spread into lymph nodes and extranodal extension, but the link to recurrence-free survival was not statistically significant.
- **Why it matters**: If confirmed, a feature that can be read on standard stained slides without extra tests could help flag higher-risk patients. The text is a small single-centre retrospective study, so it shows an association rather than proof that the feature drives worse outcomes, and the authors describe it only as a possible prognostic risk factor.
- **Background needed**: - Oropharyngeal cancer: cancer of the throat behind the mouth, including the tonsils and base of the tongue.
- pT3/pT4: tumour stage categories meaning a larger tumour or one that has grown into nearby structures.
- H&E staining: routine dye (haematoxylin and eosin) that colours tissue slides so pathologists can read them.
- SARIFA / TAC: stroma areactive invasion front area; the tumour's edge touches fat cells directly, with no reaction from surrounding tissue. Previously reported as a negative prognostic marker in other cancers.
- p16: a protein often used as a marker for HPV-linked oropharyngeal cancer.
- Extranodal extension (ENE): cancer spreading beyond the capsule of a lymph node into surrounding tissue.
- Overall and recurrence-free survival: time until death from any cause, and time until the cancer returns, respectively.
- Retrospective: analysis of records and stored tissue from past patients. · level: intermediate

<details><summary>Original abstract</summary>

Introduction: Stroma areactive invasion front areas (SARIFA) are a histopathological phenomenon at the tumour invasion front characterised by direct tumour-adipocyte contact (TAC). It can be detected on histological Haematoxylin-Eosin (H&E) stained tumour slides. TAC/SARIFA has emerged as a strong negative prognostic factor in several tumour entities. In this monocentric retrospective study, we aim to elucidate the impact of TAC/SARIFA in oropharyngeal cancer. Materials and methods: 78 cases of pT3 to pT4 oropharyngeal squamous cell cancer from 2005 to 2023 and their corresponding lymph nodes were analysed for the occurrence of TAC/SARIFA. Besides, we compared overall survival rates, recurrence-free survival (RFS) and association with biological and pathological tumour characteristics. Results: In total, overall survival was significantly reduced in TAC/SARIFA-positive tumours (p=0.014). Moreover, TAC/SARIFA positive primary tumours are associated with TAC/SARIFA positive lymph nodes (p<0.001) and extranodal extension (ENE) (p=0.032). Finally, RFS in TAC/SARIFA-positive tumours was reduced, but not significantly (p=0.072). No significant difference was found between p16 positive and p16 negative tumours and prevalence of TAC/SARIFA. Conclusion: TAC/SARIFA is a possible prognostically relevant risk factor in oropharyngeal cancer. When detected in the primary tumour or lymph nodes, it is associated with reduced overall survival rates and tendency towards shorter RFS. TAC/SARIFA-positive lymph nodes almost always show ENE.

</details>

## Health informatics and medical AI

### [STREAM: Sequential Transformer for Risk Estimation from Asynchronous Medical Events for Dynamic Postoperative AKI Prediction](https://www.medrxiv.org/content/10.64898/2026.11.21.26368665v1)
*Lu, S.; Ruan, X.; Wang, L. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.21.26368665 v1 · relevance 0.10

- **In one sentence**: STREAM is a Transformer model that treats each patient's irregular EHR data as a time-ordered stream of clinical events to predict postoperative acute kidney injury (PO-AKI) both at surgery completion and event by event afterward, in a retrospective cohort of 167,078 noncardiac surgical episodes.
- **In plain words**: After surgery, doctors need to know whether a patient's kidneys are at risk of sudden injury, and that risk changes as new test results and notes arrive. This study builds a model that reads a patient's record as a timeline of individual events, updating its risk estimate each time something new is added. In a retrospective analysis of about 167,000 non-heart surgeries, it scored somewhat better than two comparison models at predicting kidney injury.
- **Why it matters**: Risk estimates that update as information arrives, rather than from a fixed snapshot, could matter for postoperative monitoring. The authors also suggest it could feed future "digital twin" models of a patient, though the text does not test that link, and the gains over the comparators are modest.
- **Background needed**: - Acute kidney injury (AKI): a sudden drop in kidney function after surgery or illness.
- EHR (electronic health record): the digital chart holding labs, medications, and notes; its data arrive at irregular times.
- Transformer: a neural network architecture that weighs relationships among items in a sequence; widely used in language models.
- GRU-D: a recurrent network designed for irregular, gappy time series; used here as a comparator.
- AUROC / AUPRC: measures of how well a model ranks patients who will and will not develop the outcome (AUPRC is more sensitive when the outcome is rare).
- Calibration: whether predicted probabilities match observed event rates.
- Retrospective cohort: a study using existing records rather than a new trial.
- Digital twin: a computer model that mirrors an individual patient over time. · level: research-level

<details><summary>Original abstract</summary>

Postoperative acute kidney injury (PO-AKI) risk estimates evolve as clinical information accumulates, yet many electronic health record (EHR) models use static or fixed-window representations. We developed STREAM, a perioperative event-stream Transformer that represents irregular EHR data as chronological clinical events and supports surgery-index prediction at surgery completion and event-by-event postoperative AKI prediction. In a retrospective cohort of 167,078 noncardiac surgical episodes, STREAM achieved surgery-index AUROC/AUPRC of 0.942/0.771, the Time-series Transformer 0.933/0.729, and GRU-D 0.926/0.695. Postoperative macro-AUPRC across 6-hour evaluation intervals was 0.589, 0.525, and 0.547, respectively. STREAM showed more consistent calibration across postoperative time points than the comparators. Event-arrival attribution and within-window permutation analysis enabled event-level interpretation of how newly arrived information and fine-grained event ordering shaped evolving risk estimates. These findings support event-stream modeling as an interpretable framework for dynamic, temporally resolved prediction from longitudinal EHR data as well as a potential risk-estimation component for future perioperative digital twins.

</details>

### [Task-specific fine-tuning versus frontier large language models for RoB 2 risk of bias assessment: development and external benchmark evaluation of RoB-BERT](https://www.medrxiv.org/content/10.64898/2026.11.19.26368519v1)
*Pitre, T.; Mah, J.; Azlan, A. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.19.26368519 v1 · relevance 0.08

- **In one sentence**: A fine-tuned model (RoB-BERT) for RoB 2 risk-of-bias judgements on randomized trials is compared with three frontier large language models and with human assessors, using single published human judgements as the reference.
- **In plain words**: Medical reviews grade how trustworthy each clinical trial is, using a checklist called RoB 2, and that grading is slow and often inconsistent between people. This paper builds a specialised AI tool for that job and tests it against three general-purpose AI models and against published human ratings. The authors report that the specialised tool agreed with single human raters about as well as two humans agreed with each other, and was about as good as or better than the general models at far lower cost.
- **Why it matters**: Automating risk-of-bias checks could speed up evidence reviews, but agreement levels here are modest, and the human reference is a single published judgement rather than an expert gold standard, so the results should be read cautiously. The paper also suggests that human raters themselves are unreliable on this task, which matters for how review consensus is built.
- **Background needed**: - Randomized controlled trials are the main way new treatments are tested, and systematic reviews combine them.
- Risk of bias (RoB) is a judgement of whether a trial's design or reporting could distort its results.
- RoB 2 is a standard tool: it asks 22 signalling questions across five bias domains, then gives each domain and the overall trial a rating of low risk, some concerns, or high risk.
- A large language model (LLM) is a general AI system trained on large text collections; "frontier" models are the most capable current ones.
- Fine-tuning means further training a model on a specific task's examples, here 5,304 reviewer-checked assessments.
- Agreement is reported as percent agreement and kappa, a chance-corrected score where 0 means chance-level agreement and 1 means perfect.
- Sensitivity and specificity measure how often a tool catches high-risk domains and how often it correctly clears the others. · level: research-level

<details><summary>Original abstract</summary>

Background: Researchers increasingly use large language models (LLMs) to assess risk of bias in randomized trials, but how task-specific fine-tuned models compare with frontier models remains uncertain. Objective: To develop RoB-BERT, a fine-tuned RoB 2 assessment system, and to compare its agreement with human assessments against that of three frontier LLMs. Methods: RoB 2 rates five bias domains and the trial overall as low risk, some concerns or high risk, based on answers to 22 signalling questions. RoB-BERT answers each question, quotes the supporting sentences from the trial report, and applies the official RoB 2 algorithm. We trained RoB-BERT on 5,304 reviewer-checked assessments, none from a test trial, and compared it with Claude Fable 5.1, GPT-6 Astra and Gemini 4 Argon, each given identical prompts and text, against 419 published human assessments (ROBoto2, LogiMed-RoB and Cochrane reviews) made without AI assistance. Each reference was the single published judgement for that trial, made by one assessor or agreed by two, rather than an expert reference standard, so we also report agreement between two human assessors of the same trial. Results: In ROBoto2, pairs of human assessors who rated the same trial agreed on 61.2% to 64.7% of domain judgements ({kappa} 0.15 to 0.35) and 46.2% to 50.0% of overall judgements ({kappa} 0.15 to 0.17); across the 185 ROBoto2 trials, RoB-BERT agreed with the human judgement on 67.4% ({kappa} 0.35) and 53.5% ({kappa} 0.20). Across all 419 assessments, domain agreement was 67.9% ({kappa} 0.29) for RoB-BERT, 65.0% ({kappa} 0.24) for Claude Fable 5.1, 52.7% ({kappa} 0.21) for GPT-6 Astra and 66.7% ({kappa} 0.26) for Gemini 4 Argon; overall agreement was 46.1% ({kappa} 0.16), 47.3% ({kappa} 0.17), 31.0% ({kappa} 0.03) and 46.5% ({kappa} 0.14), respectively. For domains the reference rated high risk, sensitivity was 22.2% for RoB-BERT, 23.1% for Claude Fable 5.1, 41.9% for GPT-6 Astra and 24.8% for Gemini 4 Argon, with specificity of 92.5%, 92.8%, 80.0% and 95.0%. On the 52 ROBoto2 trials rated by two assessors, the second assessor's sensitivity for the reference assessor's high-risk domains was 23.1% (specificity 90.3%) and RoB-BERT's was 30.8% (specificity 92.7%). RoB-BERT located 95.7% of its quotations verbatim in the report and cost US$0.005 per trial, 2% to 6% of the frontier models' cost. Conclusions: RoB-BERT agreed with single human assessors at least as closely as two human assessors agreed with each other, and matched or exceeded frontier LLMs at a fraction of their cost. The results show the poor reliability of human assessors using RoB 2 and the need for consensus ratings, with RoB-BERT potentially serving as one rater.

</details>

## Econometrics and applied economics

### [Adaptive experiments with observational data: Efficient experimental design and asymptotic time-uniform inference for long-term treatment effects](https://arxiv.org/abs/2611.30595)
*Kentaro Kawato* · `econ.EM` · arXiv:2611.30595v1 · relevance 0.08

- **In one sentence**: The paper proposes using pre-experiment observational data both to identify long-term average treatment effects and to design adaptive experiments, deriving an efficiency-optimal fixed design, a sequential learning procedure that attains the oracle variance, and an anytime-valid confidence sequence.
- **In plain words**: Studies of policies often need years before the outcome that matters, such as income later in life, can be measured. This paper asks whether data gathered before a trial starts, which already contain the long-term outcome for other people, can be used to decide in advance who to enroll and how to assign treatment, so the trial estimates the long-term effect more precisely. The authors show how to learn this design while the experiment runs and provide confidence intervals that stay valid if the experimenter checks them after every participant.
- **Why it matters**: Shortening the wait for long-term results could speed up decisions in policy evaluation and online testing. The text reports simulation gains in precision and detection time, and an illustration with the Pakistan Graduation experiment, but the abstract does not show how large these gains are in practice.
- **Background needed**: - Average treatment effect: the average difference in outcomes between treated and untreated groups.
- Long-term outcome: a result measured only after a long delay, so it is often missing for the experiment's own participants.
- Observational data: records collected without random assignment, here used to predict long-term outcomes.
- Semiparametric efficiency bound: the lowest possible variance an estimator can reach without strong distributional assumptions.
- Adaptive experiment: a trial where later sampling and assignment decisions use data gathered earlier.
- Confidence sequence: an interval that stays valid across many interim looks, so the experimenter can stop early without invalidating results.
- Conditional variance: how much outcome noise varies across types of participants, which drives the optimal design. · level: research-level

<details><summary>Original abstract</summary>

Estimating long-term treatment effects in experiments requires waiting for outcomes to become observable, which can delay both the evaluation of an intervention and subsequent decisions. Recent econometric work has developed identification methods that combine experimental data with observational data containing long-term outcomes. This paper proposes using observational data available before the experiment begins not only for identification but also for designing adaptive experiments, in which experimental data are collected sequentially. To estimate the long-term average treatment effect as precisely as possible, we express its semiparametric efficiency bound as a function of the covariate sampling and treatment assignment rules and minimize the bound over these rules to characterize an optimal fixed experimental design. This experimental design depends on the treatment-specific conditional variances of the observational prediction of the long-term outcome, which can be learned only from experimental participants. We therefore construct a sequential procedure that learns the experimental design as experimental data accumulate and show that its estimator attains the same limiting variance as an oracle estimator implemented under the optimal fixed experimental design. We further construct an asymptotic confidence sequence whose coverage holds simultaneously over all rounds after a prespecified start, so that the experimenter can inspect the interval after each participant and stop once it excludes zero. Monte Carlo simulations show that the learned experimental design can improve precision and shorten the time to detection relative to baseline sampling and equal-probability assignment. An illustration using the Pakistan Graduation experiment shows how estimated conditional variance heterogeneity informs sampling and treatment assignment.

</details>

### [Place-Based Policy from Space: Evidence from Italy's Inner Areas](https://arxiv.org/abs/2611.31100)
*Nicola Caravaggio, Giuseppe Di Renzo, Giuliano Resce et al.* · `econ.GN` · arXiv:2611.31100v1 · relevance 0.06

- **In one sentence**: A staggered difference-in-differences study using satellite nighttime lights finds that Italy's SNAI place-based program is associated with a larger lit area, but no detectable change in brightness per lit cell, across 941 funded and 3,112 eligible control municipalities from 2011 to 2022.
- **In plain words**: Italy's National Strategy for Inner Areas is a government program that sends money to remote, struggling towns to fund services and local business. This paper asks whether the program shows up from space, using satellite images of nighttime lights as a rough proxy for economic activity. The authors report that funded towns saw their lit area grow, while the brightness of already-lit spots did not clearly change, which they read as activity spreading out rather than intensifying in existing centres.
- **Why it matters**: It offers a way to measure place-based policy with annual satellite data, which the authors suggest can complement slower and coarser official statistics. The text does not show how far the findings generalise beyond Italy, so the value as a method is worth weighing against that limit.
- **Background needed**: - Place-based policy: government programs that target specific geographic areas, here remote municipalities, rather than individuals or the whole country.
- Difference-in-differences: a comparison method that tracks treated and untreated areas before and after a program starts, to estimate its effect. "Staggered" means areas start receiving funds at different times.
- Nighttime lights: satellite measurements of artificial light at night, used as a rough stand-in for economic activity and settlement.
- Lit area vs. radiance: lit area is how much of a region shows any light; radiance is how bright each lit cell is.
- Control group: comparable areas that did not receive funds, used as a baseline for what would have happened anyway.
- The text only gives the abstract; details on methods, robustness checks and magnitudes are not available here. · level: research-level

<details><summary>Original abstract</summary>

This paper evaluates a place-based policy, Italy's National Strategy for Inner Areas (SNAI), using satellite nighttime lights. Targeting structurally fragile and peripheral municipalities, SNAI invests in essential services and economic activities. Staggered difference-in-differences compares 941 funded municipalities with 3,112 eligible controls over 2011--2022. Funding is associated with an expansion of lit area and no detectable change in radiance per lit cell, suggesting that activity extends its footprint rather than intensifying in existing centres. The expansion holds across comparison groups and, descriptively, concentrates at intermediate funding per resident. Annual satellite data can complement slower and coarser statistics.

</details>

## Economic theory

### [Shadow economy as a null set. Measure-theoretic approach to shadow economy](https://arxiv.org/abs/2611.29797)
*Rados\l{}aw A. Kycia, Andrzej Buszko* · `econ.EM` · arXiv:2611.29797v1 · relevance 0.08

- **In one sentence**: The paper proposes modeling the shadow economy as a null set relative to institutional measurement instruments, and combines Banach lattices, Lebesgue decomposition, copula theory, Kullback-Leibler divergence, and compressed sensing into a three-regime framework for estimating underreported transactions.
- **In plain words**: The paper asks whether the informal, unreported part of the economy can be defined in terms of what government institutions fail to measure. It proposes treating unobserved activity as a "null set," meaning something that registries and sensors effectively miss. The text describes three mathematical approaches for handling underreporting, hidden financial flows, and auditing at scale, but the abstract does not report any empirical results.
- **Why it matters**: Measuring the shadow economy is a long-standing problem for tax authorities and economists, and the paper's aim of separating the true informal economy from the limits of official observation is a conceptually interesting reframing. Its real-world usefulness is unclear from the abstract, since it gives no data, validation, or test results.
- **Background needed**: - Shadow economy: economic activity that is unreported to tax or statistical authorities, such as cash work or unregistered sales.
- Null set: in measure theory, a set that is so small it has zero measure, so it does not affect totals.
- Measure and institutional measure: a way of assigning sizes to sets of transactions; here, what registries and sensors can register.
- Lebesgue decomposition: splitting a measure into parts that are absolutely continuous and parts that are not, roughly separating observable from unobservable mass.
- Banach lattice and supremum fusion: an ordered space of functions; taking the supremum combines several partial records into one best-available picture.
- Copula and Kullback-Leibler divergence: tools for describing how variables are linked and for measuring how far one probability model is from another.
- Compressed sensing: recovering a sparse signal (one with few nonzero entries) from a small number of random measurements. · level: research-level

<details><summary>Original abstract</summary>

In this paper we asked if the shadow economy can be defined as a system of null sets for institutional measures or sensors that measure economic transactions. As an answer a measure-theoretic testable framework to redefine and quantify the shadow economy was designed. Traditional economic definitions frequently conflate the actual shadow economy with the observational limitations of state institutions. To resolve this, we model the shadow economy as a null set relative to institutional measures and analyze three complementary economic regimes. We explore in this context how standard mathematical tools can be given economic meaning. First, in the low-resolution regime, we apply Banach Lattices and Lebesgue decomposition of a measure to address transaction underreporting by aggregating incomplete institutional registries using a supremum fusion operator. Second, for hidden economic dimensions, we utilize Copula theory and Kullback-Leibler divergence optimization to reconstruct unobserved financial flows from technological and physical indicators. Third, we address audit scalability by modeling the shadow economy as a sparse vector, applying Compressed Sensing to detect high-volume sparse evasion networks through random, incoherent, and privacy-preserving sampling.

</details>

### [Principal Revelations of the Revelation Principle](https://arxiv.org/abs/2611.30612)
*Mark Whitmeyer* · `econ.TH` · arXiv:2611.30612v1 · relevance 0.07

- **In one sentence**: A converse to the revelation principle in mechanism design: under private values and independent types, direct truthful mechanisms must be assumed to select the principal's favorite equilibrium, and with quasilinear payoffs and unrestricted transfers any mechanism's equilibrium payoff can be approximated by a direct mechanism with a unique truthful equilibrium.
- **In plain words**: This paper looks at how a decision-maker (the "principal") who designs a set of rules for other people can predict how those people will behave. The revelation principle says that any outcome achievable by complicated rules can also be achieved by a simple setup where people just report their private information honestly. The author shows that the principal can only rely on this simplification if she assumes the people play the equilibrium that suits her best, and that unrestricted payments let her get close to any outcome with a setup where honest reporting is the only stable behavior.
- **Why it matters**: The result clarifies what assumptions the standard simplification in mechanism design quietly relies on, which matters for auction, contract, and policy design. The text itself does not discuss applications, so the wider connections are my inference and should be checked against the full paper.
- **Background needed**: - Mechanism design: building the rules of a game so that participants' choices lead to a desired outcome.
- Principal and agents: the principal designs the rules; the agents hold private information and choose how to act.
- Revelation principle: a standard result saying that one can restrict attention to mechanisms where agents report their private information truthfully.
- Equilibrium: a state where no participant wants to change their behavior given what others do.
- Private values: each agent's payoff depends only on their own private type, not on others' information.
- Independent types: agents' private information is statistically unrelated to each other.
- Quasilinear payoffs: utility is value minus money paid, so payments can be traded off directly against outcomes.
- Prior: the principal's initial beliefs about the agents' types; "prior in a set" means she knows only that beliefs lie in some range. · level: research-level

<details><summary>Original abstract</summary>

I prove a converse to the revelation principle, arguing that it is a principle of optimism: if it must hold for all environments (in fact, even just those with private values and independent types) the principal must assume her favorite equilibrium is played by the agents. When the principal knows only that the prior lies in some set, she must additionally assume it is her favorite one. With private values, independent types, and quasilinear payoffs, however, unrestricted transfers allow the principal to approximate any mechanism's equilibrium payoff via a direct mechanism whose unique equilibrium is truthful.

</details>

## Game theory and algorithmic economics

### [Optimal Regret Lower Bounds in Matrix Games](https://arxiv.org/abs/2611.31149)
*Taira Tsuchiya* · `cs.GT` · arXiv:2611.31149v1 · relevance 0.11

- **In one sentence**: The paper proves that deterministic learning dynamics in two-player zero-sum matrix games must incur regret of order sqrt(log m log n) on some payoff matrix (matching known upper bounds), plus a log-type lower bound valid for all m, n, and T, via an adaptive matrix construction.
- **In plain words**: The paper studies two players who repeatedly pick mixed strategies in a fixed zero-sum game, learning from the results as they go. It shows that no deterministic learning procedure can avoid a certain amount of regret (how much worse it does than the best fixed choice in hindsight) on some game, and that this amount matches the best known upper bound in a broad range of settings. The lower bound is built adaptively: as the players' algorithms run, the authors add a rank-one matrix each round that leaves past feedback unchanged while raising a lower bound on the players' combined regret.
- **Why it matters**: It closes a gap: matching lower bounds were previously known only for specific learning dynamics, and this shows the tight bound holds for all deterministic ones, which clarifies how fast self-play can approach equilibrium. It also yields limits on how quickly average strategies converge to a Nash equilibrium and on how many matrix-vector queries are needed to compute one; I have not checked how these connect to wider applications beyond the text.
- **Background needed**: - Two-player zero-sum game: one player's gain is the other's loss, described by a payoff matrix with m and n actions.
- Mixed strategy: choosing actions at random according to probabilities.
- Regret: how much a player loses compared with the best single fixed action in hindsight, accumulated over T rounds.
- Hedge / multiplicative weights: a standard online learning rule that shifts probability toward actions that have done well.
- Optimistic Hedge: a variant that uses a prediction of the next round's feedback.
- Nash equilibrium: a pair of strategies where neither player gains by changing alone; in zero-sum games it is the minimax solution.
- Minimax regret: the best worst-case regret any algorithm can guarantee; Omega, O, Theta denote lower, upper, and matching bounds.
- Deterministic dynamic: an algorithm with no internal randomness, so its behavior is fully fixed by the feedback it receives. · level: research-level

<details><summary>Original abstract</summary>

We study learning in two-player zero-sum games, also known as matrix games, in which two players with $m$ and $n$ actions repeatedly select mixed strategies for $T$ rounds. The learning dynamics based on optimistic Hedge guarantee regrets of $O(\log(mn))$, which improve to $O(\sqrt{\log m\log n})$ if each player knows the number of actions of the opponent, whereas matching regret lower bounds have been known only for specific learning dynamics. We prove that, for every deterministic learning dynamic, there exists a payoff matrix for which the maximum individual regret is $\Omega(\sqrt{\log m\log n})$ for a wide range of $m$ and $n$. Together with the upper bound $O(\sqrt{\log m\log n})$, this lower bound shows that the minimax regret of deterministic learning dynamics in matrix games is $\Theta(\sqrt{\log m\log n})$ in this regime. For all $m$, $n$, and $T$, we also prove the lower bound $\Omega(\min\{T,\log\min\{m,n\}\})$. These lower bounds hold even if each player also observes the strategies and the feedback of the opponent. Our main technical contribution is an adaptive construction of the payoff matrix. While running the algorithms of the two players, we add in each round a rank-one matrix that keeps the feedback of the previous rounds unchanged and increases a lower bound on the sum of the regrets of the two players. As by-products, we obtain lower bounds on the rate at which the average strategies converge to a Nash equilibrium and on the query complexity of matrix-vector products that deterministic algorithms need to compute an approximate Nash equilibrium.

</details>

### [A Characterized Softmax for Distributing Standing Across Multiple Affiliations](https://arxiv.org/abs/2611.28391)
*Md Mahedi Hasan Riday, Md Shajalal, Gunnar Stevens* · `cs.GT` · arXiv:2611.28391v1 · relevance 0.10

- **In one sentence**: The paper defines "membership attribution," the problem of splitting a player's standing across the overlapping groups it belongs to, and characterizes a restricted-domain softmax solution that is unique up to a temperature parameter under five stated requirements, with further requirements fixing the temperature's sign and forcing a shared temperature across players.
- **In plain words**: The paper asks a question that classic fair-sharing rules in game theory do not address: when a person (or player) belongs to several overlapping groups, how should their standing be divided among those groups? The direct proportional approach breaks down when the signals for a player's groups have mixed positive and negative signs, so the authors use a softmax-style weighting instead. They show that, under stated conditions on the group structure, this weighting is the only rule meeting their five requirements, up to one adjustable scale parameter.
- **Why it matters**: The text positions membership attribution as a fourth question alongside payoff allocation, interaction attribution, and coalition stability, which suggests a new axis for cooperative game theory. Its practical reach beyond this formal setting is not established in the text, so any wider application should be treated as speculative.
- **Background needed**: - Cooperative game theory: studies how a joint payoff is shared among players who can form coalitions (e.g., Shapley value).
- Overlapping group membership: a player can belong to several groups at once, with the group tags fixed in advance.
- Softmax: a standard way to turn a list of scores into positive weights that sum to one, using exponentials; a temperature parameter controls how sharply the weights favor the top scores.
- Axiomatic characterization: showing that a rule is the only one satisfying a list of stated requirements, so the requirements are the substance of the result.
- Mixed sign: some group-level signals are positive and others negative, which makes simple ratio-based splitting invalid.
- Richness condition: a structural requirement on the group layout that the paper states precisely; the summary does not reproduce it. · level: research-level

<details><summary>Original abstract</summary>

Cooperative game theory answers canonical questions on payoff allocation (Shapley, Owen), interaction attribution (Grabisch-Roubens, Faith-Shap), and coalition formation and stability. None answers a fourth question that arises whenever players carry known, overlapping group tags fixed independently of the game: how should a player's standing be distributed across the groups it already belongs to? We call this membership attribution, formalize it, and give a complete characterization of its solution. The direct, ratio-based answer is provably invalid whenever a player's group-level signals have mixed sign --- a common, structurally unavoidable case. We propose a restricted-domain softmax construction instead, and prove that, for any player satisfying a precisely defined richness condition on the group structure, it is the unique such map, up to a temperature parameter, satisfying five requirements. A sixth requirement fixes the sign of this temperature; a seventh, shown independent of the rest via an explicit counterexample, forces one shared temperature across all eligible players. A worked example on an exact cooperative game confirms the applicable requirements numerically and shows the construction degrades gracefully, valid but uninformative, when a player's evidence fails to distinguish between its groups.

</details>

## Mathematical finance

### [Model Doubt, Risk Aversion, and the Threshold for Trading: A Geometry of Pricing Measures](https://arxiv.org/abs/2611.28288)
*Amine Mohamed Aboussalah* · `q-fin.MF` · arXiv:2611.28288v1 · relevance 0.06

- **In one sentence**: In a one-period market, the paper characterizes when a Kullback-Leibler-robust investor stops trading, shows that below that threshold model doubt acts like higher risk aversion, and links the real-world, pricing and share measures through a Pythagorean-type identity whose defect is a log risk premium, with US data illustrations.
- **In plain words**: The paper asks how uncertain an investor can be about the true market model before they stop holding any risky asset. The author treats every model within a set distance of the investor's reference model as plausible, and measures that distance with an information-theoretic gap called Kullback-Leibler divergence. The main finding is a threshold: below it, the investor still trades, and doubt behaves like a higher level of caution; at or above it, the investor holds no risky asset.
- **Why it matters**: The text suggests a way to translate a market quote, such as the VIX, into a measure of how much model doubt an investor is implicitly carrying, and reports US illustrations (a risk-aversion equivalent of about 1.8 for a log investor who doubts the Black-Scholes mean return, and a defect of about 10% per year since 1990). How far these findings generalize beyond the chosen reference models is not something the summary can judge.
- **Background needed**: - Kullback-Leibler divergence: a non-symmetric measure of how different one probability model is from another.
- Utility and risk aversion: a concave utility function describes diminishing satisfaction from wealth; "log utility" is a specific case with relative risk aversion equal to 1.
- Pricing (risk-neutral) measure: a probability model under which asset prices equal discounted expected payoffs.
- Stock numeraire ("share measure"): a way of re-expressing prices in units of the stock itself.
- VIX: a market index of expected stock-market volatility, derived from option prices.
- Entropy premium: a risk premium measured using the entropy (log-moment) of returns.
- Robust decision-making: choosing a strategy that performs acceptably across a whole set of plausible models rather than one model. · level: research-level

<details><summary>Original abstract</summary>

How much model doubt can an investor bear before they stop trading? Our investor treats every model within a given Kullback-Leibler divergence of their reference model as plausible. In a finite one-period market, they hold no risky asset exactly when this doubt reaches the smallest divergence of a pricing measure from their model, for every smooth, strictly increasing, strictly concave utility; non-traded claims then have intervals of no-trade prices. Below this threshold, for log utility and in a given market, doubt acts exactly like higher constant relative risk aversion; their robust pricing measure moves from the log-utility measure toward the pricing measure at that smallest divergence. With a century of U.S. data, a log investor who doubts the Black-Scholes mean return over its 95% confidence interval acts like a fully trusting investor with relative risk aversion of about 1.8 instead of 1. Implied doubt turns a quote into a radius; the mean VIX implies doubt beyond the threshold, but whether significantly so depends on the reference model. By a known identity, real-world, pricing, and share (stock-numeraire) measures form a triangle whose Pythagorean defect is a log risk premium; one side is half the squared (ideal) VIX times the horizon. Since 1990, the U.S. defect averages about 10% per year, about 1 point of it entropy premium.

</details>

### [Gated Payoff-Weighted Net Profit Maximization For Online Portfolio Selection With Transaction Costs](https://arxiv.org/abs/2611.29552)
*Grace Chengrong Xie, Alvey Qianli Lin, Wai Ki Ching* · `q-fin.PM` · arXiv:2611.29552v1 · relevance 0.06

- **In one sentence**: The paper proposes a gated, payoff-weighted combination of net-profit-maximization portfolio experts built on Adaptive Online Moving Average forecasts, designed to correct for overstated forecasts and to account for transaction costs in online portfolio selection.
- **In plain words**: The paper looks at how to split money across several assets over time when each trade costs something, using only past prices. The base method trades only when its forecast gain is larger than the trading cost, but its forecasts tend to be too optimistic. The authors add a "gate" that learns, for each asset, how much of the forecast to trust, and combine several such strategies weighted by their accumulated wealth.
- **Why it matters**: Online portfolio selection is a practical problem for anyone trading under transaction costs, so better calibration of forecasts matters for real results. The text reports that on nine datasets at a 0.1% cost rate the method yields about 5.9 times the geometric-mean wealth of the base strategy and beats it on every dataset; the text does not say how these results would hold in live markets or under other conditions.
- **Background needed**: - Online portfolio selection: repeatedly deciding how to divide wealth among assets, one period at a time, using only data up to that point.
- Relative return: the ratio of an asset's price today to its price yesterday.
- Transaction cost: the fee or spread paid each time holdings are changed; here modeled as a rate (0.1%).
- Moving average forecast: a prediction formed by averaging recent values; "adaptive" means its weighting adjusts over time.
- Calibration: whether a forecast's stated strength matches how often it turns out right; the paper says these forecasts are overstated.
- Predictive likelihood: a score for how well a forecast explains observed outcomes, used here to set the gate.
- Geometric mean wealth: the typical per-period compounded growth of wealth across periods, a common performance measure in this area.
- Expert combination: running several strategies in parallel and weighting them by past performance. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we study online portfolio selection (OLPS) problems. The net profit maximization (NPM) acting upon Adaptive Online Moving Average (AOLMA), namely the AOLNPM strategy in portfolio selection, trades when forecast gain exceeds the transaction cost. In essence, this method relies heavily on calibrated forecasts. Indeed, we show that AOLMA forecasts overstate the realized relative returns. We therefore design a gate that adjusts how strongly an AOLMA forecast is used; for each asset, it learns the recent mixture proportion assigned to AOLMA from predictive likelihoods against a neutral forecast (no change). The proportion therefore estimates the extent to which the forecast is realized. We then feed the resulting forecast into the NPM portfolio rule, where the gate acts as an asset-specific cost threshold. A payoff-weighted fund combines gated NPM experts with fixed decay factors in proportion to their wealth and needs no learning rate. On nine datasets with a transaction cost rate of 0.1%, our method produces 5.9 times the wealth of AOLNPM in geometric mean and sits above AOLNPM on every dataset, with its preponderance growing with the cost rate.

</details>

## Financial markets

### [Political Orientation and Participation in Prediction Markets: Large Stakes Converge, Small Stakes Diverge](https://arxiv.org/abs/2611.29576)
*Ali Hosseinzadeh, Ali Hosseiny, Reza Jafari* · `physics.soc-ph` · arXiv:2611.29576v1 · relevance 0.06

- **In one sentence**: A complex-network analysis of about 1.14 billion Polymarket transactions that finds investment concentration is highly skewed and that, around the 2024 U.S. presidential election, large-scale Trump-only and Harris-only investors allocate capital more similarly across topics than small-scale ones do.
- **In plain words**: Prediction markets are online platforms where people bet real money on whether future events will happen. This paper looks at a very large set of trades on one such platform, Polymarket, to see who bets on what and how much. It finds that a small share of events and a small share of users account for most of the money, and that around the 2024 U.S. election, people who bet only on Trump or only on Harris spent their money in more similar ways when they placed large bets than when they placed small ones.
- **Why it matters**: The finding that political divides seem to narrow among large bettors and widen among small bettors is a specific, testable pattern about how beliefs show up in money. The paper reports that it holds across six network comparisons and that four of the differences are statistically supported, but the text does not say what causes the pattern, so its broader meaning remains uncertain.
- **Background needed**: - Prediction market: a platform where people buy and sell shares tied to whether an event happens; prices are often read as crowd estimates of likelihood.
- Wallet address: an identifier for a crypto account; one person may control several wallets, so wallets are not exactly people.
- Bipartite network: a graph with two kinds of nodes (here, users and events) where links only join one kind to the other.
- Community structure: groups of nodes that are more densely connected to each other than to the rest of the network.
- Concentration / skewed distribution: a pattern where a few items carry most of the total, such as 1% of wallets making up 79.2% of participation.
- Statistical support: a test indicating a difference is unlikely to be due to chance alone; the text does not give the test details. · level: intermediate

<details><summary>Original abstract</summary>

Prediction markets offer a way to study collective expectations and beliefs: people express their views on various events and, by putting money behind their predictions, take on the risks of their judgments. As a result, the scale of investment can reveal additional dimensions of individual behavior and beliefs. In this study, we use a complex network approach to examine the structure of user participation, drawing on roughly 1.14 billion transaction records from the Polymarket platform, covering more than 3.1 million wallet addresses and 764,000 prediction events. To do this, we build a bipartite network of users and events and analyze patterns of investment concentration, connections between topics, and the network's community structure. Our findings show a highly skewed distribution of financial participation: 1\% of events account for 64\% of total transaction volume, while 1\% of wallets account for 79.2\% of total financial participation. We also examine how investment scale and political orientation shape user participation patterns. Focusing on the 2024 U.S. presidential election, we compare users who invested exclusively in a Trump victory or exclusively in a Harris victory, grouping wallets by purchase size rather than by retail or institutional status. The results show that among large-scale investors, capital allocation patterns across topics are more similar between the two political groups; in contrast, these patterns diverge more and vary more among small-scale investors. This result holds across six different ways of representing and comparing the networks, and four of these differences are also statistically supported.

</details>

### [Cleaning correlation matrices with external information: the Maximum Variance estimat](https://arxiv.org/abs/2611.30843)
*S\'ebastien Valeyre* · `q-fin.PM` · arXiv:2611.30843v1 · relevance 0.06

- **In one sentence**: The paper proposes a Maximum Variance (MaxVar) estimator that cleans an empirical correlation matrix by fixing its leading eigenvectors to combinations of group-level maximum-variance portfolios, using asset-class groupings as external information, and tests it on 47 futures contracts.
- **In plain words**: Investors estimate how assets move together using a correlation table built from past prices, but with many assets and limited history that table is noisy and can mislead portfolio decisions. This paper proposes a way to tidy the table by using a simple outside fact: which group each asset belongs to, such as stock indices, bonds or currencies. On 47 futures contracts, the authors report that this approach gave a better-performing risk parity portfolio over 1993–2018 than both the raw table and a generic cleaning method.
- **Why it matters**: Cleaning noisy correlation estimates matters for portfolio construction, where errors in the inverse matrix can hurt returns. The reported Sharpe ratio gains are modest (1.28 versus 1.24 and 1.17), and the text covers only one dataset and one portfolio type, so the practical significance is not yet established.
- **Background needed**: - Correlation matrix: a table of how pairs of assets move together; with many assets and few observations, its estimates are noisy.
- Eigenvalues and eigenvectors: the main directions of variation in the table and how strong each one is; cleaning methods adjust these.
- Rotationally invariant estimators: a known family of methods that reshape the strengths of these directions while keeping their noisy orientations.
- Factor model: describing many assets by a small number of shared drivers, here with about n parameters rather than n²/2.
- Maximum-variance portfolio: the portfolio within a group that has the largest volatility.
- Risk parity: a portfolio approach that spreads risk evenly across holdings, which requires inverting the correlation matrix.
- Sharpe ratio: return earned per unit of risk taken; higher is better.
- Out-of-sample test: judging a method on later data than it was fitted on. · level: research-level

<details><summary>Original abstract</summary>

Rotationally invariant estimators clean the eigenvalues of an empirical correlation matrix but keep its noisy eigenvectors. We study an estimator that corrects the eigenvectors by using external information, namely a partition of the assets into groups such as asset classes or regions. The Maximum Variance (MaxVar) estimator restricts the leading eigenvectors to linear combinations of the maximum-variance portfolios of the groups and replaces the rest of the spectrum by a single eigenvalue. It is a factor model with about n parameters instead of n2/2, and it is positive de nite even when the number of observations is smaller than the number of assets n. We apply it to the correlation matrix of 47 futures on stock indices, bonds and currencies, with the three asset classes as groups. In an illustrative Monte Carlo test, in which the reference matrix has the structure assumed by the estimator, the distance to the reference is reduced by one third with respect to the empirical matrix, against less than 10% for the rotationally invariant estimator. The decisive test is the performance of a portfolio on real data: over 1993-2018, the Sharpe ratio of the risk parity portfolio, which involves the inverse of the matrix, is 1.28 with the MaxVar estimator, 1.24 with the rotationally invariant estimator and 1.17 with the empirical matrix, and the advantage increases when the estimation window is shortened.

</details>

## Signal processing

### [Deep-Learning-Based Classiffcation of Relay-Surface Scattering Regimes for NLOS Millimeter-Wave Sensing](https://arxiv.org/abs/2611.30279)
*Haoran Yuan, Guanghua Liu, You Xu et al.* · `eess.SP` · arXiv:2611.30279v1 · relevance 0.08

- **In one sentence**: DEKL, a deep-learning framework with a lightweight KLNet classifier, selects among specular, structured-multipath, diffuse, and no-target hypotheses for relay-surface scattering in NLOS millimeter-wave radar echoes, using a Kullback-Leibler information-criterion decision rule.
- **In plain words**: Radar signals that bounce off a relay surface before reaching a hidden target can be distorted in ways that mislead localization. This paper proposes a method that looks at radar echoes and decides which kind of surface scattering is dominant, without needing to measure the surface's roughness directly. The authors report that their approach discriminates better than the information-criterion rules they compared against, in analytical, electromagnetic and radar-measurement tests.
- **Why it matters**: Choosing the wrong propagation model for a relay surface can cause localization errors and ghost targets, so a reliable way to identify the scattering regime matters for NLOS sensing. The text links the predicted regime to model selection in wireless-network digital twins, but how far this extends beyond the evaluated setups is not shown here.
- **Background needed**: - Millimeter-wave radar: short-wavelength radio used for sensing object positions.
- Non-line-of-sight (NLOS): the target is hidden from direct view, so signals reach it via reflections.
- Specular vs. diffuse scattering: smooth surfaces reflect in one direction; rough surfaces scatter energy widely.
- Surface roughness: small-scale bumpiness of a surface, which determines the scattering type.
- Covariance matrix: a table of how signal channels co-vary, used here as the input features.
- Kullback-Leibler information criterion: a statistical score for choosing among candidate models by how well each fits the data while penalizing complexity.
- Attention and gated iterative decoding: neural-network mechanisms that focus on informative parts of the input and stop refining once the prediction is confident.
- Ghost target: a false detection caused by reflections. · level: research-level

<details><summary>Original abstract</summary>

In non-line-of-sight (NLOS) millimeter-wave sensing, relay-surface scattering alters target echoes and can cause propagation-model mismatch, angle-estimation errors, and ghost targets. DEKL, a deep-learning framework, identifies the dominant scattering regime from radar echoes without measuring surface roughness. Multipath echo models describe specular reflection, structured multipath reflection, and diffuse scattering. These models and a no-target hypothesis define a model-selection problem with unknown parameters. The Kullback-Leibler information criterion yields an adaptive decision rule for selecting among these hypotheses. A lightweight network, KLNet, learns covariance-domain features and combines attention with confidence-gated iterative decoding to avoid repeated likelihood evaluation. Analytical simulations, independent electromagnetic simulations, and radar measurements show that DEKL improves discrimination over the evaluated information-criterion-based rules. Ablations show how attention, confidence supervision, and gated decoding contribute to selective prediction and robustness under controlled covariance perturbations. The predicted regime guides propagation-model selection for radio-environment repre-sentations in wireless-network digital twins and informs NLOS localization and imaging.

</details>

### [From Surface Lakes to Subsurface Signatures in Antarctica with BIOMASS P-Band TomoSAR](https://arxiv.org/abs/2611.28189)
*Francesco Banda* · `astro-ph.IM` · arXiv:2611.28189v1 · relevance 0.08

- **In one sentence**: Uses P-band tomographic SAR from ESA's BIOMASS satellite to probe subsurface scattering beneath a region of past supraglacial lake activity on the Riiser-Larsen Ice Shelf, East Antarctica.
- **In plain words**: Meltwater sometimes pools on the surface of Antarctic ice shelves, and this paper asks whether those past pools leave traces in the snow and firn (compacted snow) below. Using radar from the newly launched BIOMASS satellite, the authors examine the subsurface beneath an area where lakes formed in the past. They report that the radar signal below the surface appears linked to where lakes recurred, with changes in structure and depth over time.
- **Why it matters**: Melt and refreeze in the firn affect how much ice an ice sheet holds, so better subsurface observations could help mass balance estimates. The text suggests recurring surface lakes may leave lasting hydrological marks, though the abstract alone does not show how far this generalises beyond this one site.
- **Background needed**: - Supraglacial lake: a pool of meltwater sitting on top of a glacier or ice shelf.
- Firn: old, partly compacted snow lying between fresh snow and solid glacier ice; it holds air and water.
- Ice shelf: a floating extension of an ice sheet.
- Mass balance: whether an ice body gains or loses mass over time.
- Radar wavelength: P-band uses a 70 cm wavelength, long enough to penetrate ice and snow rather than just reflect off the surface.
- SAR tomography (TomoSAR): combining many radar passes to build a vertical, 3D-like picture of what lies beneath the surface.
- Polarimetry and interferometry: other radar techniques that use signal polarisation and phase differences to extract more information. · level: research-level

<details><summary>Original abstract</summary>

Spaceborne remote sensing of the cryosphere is fundamental to map ice structure and dynamics. Accurate mass balance estimation requires a better understanding of melt/refreeze processes and firn hydrology, whereas spaceborne optical and Radar sensors are mostly limited to near-surface observations. The BIOMASS P-band Synthetic Aperture Radar, launched by European Space Agency in 2025, provides an unprecedented opportunity to gain a more direct access to englacial processes, thanks to the 70 cm wavelength paired with polarimetry, interferometry and tomography. This paper investigates subsurface beneath a region of historical supraglacial lake activity with BIOMASS tomography, at the Riiser-Larsen Ice Shelf in East Antarctica. The main result is that subsurface scattering appears to be related to historical supraglacial lake recurrence, with structural and depth variations over time. This suggests that recurrent supraglacial lake activity may leave persistent hydrological signatures within the firn. Overall, this study highlights the potential of gaining valuable insights into ice sheet hydrology with P-band.

</details>

## Audio and speech

### [Tenlai-TTS 2.0: Continuous-Representation LLM-Based TTS System with End-to-End Training](https://arxiv.org/abs/2611.29226)
*Changfeng Gao, Yong Ren, Jun Yuan et al.* · `cs.SD` · arXiv:2611.29226v1 · relevance 0.08

- **In one sentence**: Tenlai-TTS 2.0 jointly trains a speech encoder with a Gaussian bottleneck, an LLM with an autoregressive diffusion head, a flow-matching mel decoder, and a recognition model, so that continuous speech latents are learned to suit autoregressive generation rather than frozen beforehand.
- **In plain words**: This paper is about making computers speak from text using a large language model that predicts continuous sound features instead of discrete tokens. Earlier systems learned the sound representation first and then froze it, which can leave it poorly suited for the language model to predict. The authors train the whole system end to end, and report lower error rates on the Seed-TTS-eval benchmark, such as word error rate of 1.08% on English after reinforcement learning.
- **Why it matters**: It targets a specific trade-off in speech synthesis: keeping enough acoustic detail for high-fidelity audio while keeping the representation predictable for a language model. The reported gains are measured on one benchmark against the authors' own joint-training baseline, so how well they generalize beyond it is not established by this text.
- **Background needed**: - Text-to-speech (TTS): software that turns written text into spoken audio.
- Autoregressive model: a model that generates output one piece at a time, each piece depending on earlier ones.
- Latent space: a compressed internal representation of the audio.
- Continuous vs. discrete tokens: continuous values keep fine detail, while discrete tokens round values to a fixed set of symbols, losing some information.
- Gaussian bottleneck: a narrow channel that adds noise and limits how much information passes through, keeping the representation regularized.
- Flow matching: a training method for generating data, here used to produce mel-spectrograms (visual-like maps of sound frequency over time).
- Character/word error rate (CER/WER): share of words or characters a speech recognizer gets wrong on the synthesized audio; lower is better.
- Speaker similarity: how closely the synthesized voice matches the target speaker.
- Reinforcement learning: training that adjusts a model based on rewards for good outputs. · level: research-level

<details><summary>Original abstract</summary>

Autoregressive text-to-speech (TTS) with continuous speech latents avoids quantization-induced information loss, but typically relies on a latent space that is learned separately and then frozen before language-model training. Such a space must satisfy two competing requirements: it must retain enough acoustic detail for high-fidelity reconstruction, yet be sufficiently structured and regularized to support autoregressive prediction by a language model. We present Tenlai-TTS 2.0, which learns continuous speech representations through end-to-end training to balance acoustic detail with autoregressive predictability. The model comprises a speech encoder with a capacity-controlled Gaussian bottleneck, a large language model (LLM) with an autoregressive diffusion transformer (AR-DiT) head, a flow-matching (FM) mel-spectrogram decoder, and a multi-task recognition model (RM). With energy normalization and fixed-variance Gaussian noise, the bottleneck has a closed-form upper bound on its information rate. Through joint optimization with reconstruction, recognition, and next-patch prediction objectives, we learn continuous speech representations that suit all three tasks and train the LLM and AR-DiT for autoregressive generation. The LLM and AR-DiT are further optimized using differentiable reconstruction and recognition feedback on their predicted latents through the FM decoder and RM. On Seed-TTS-eval, this feedback-based optimization reduces character error rate (CER) from 0.82% to 0.74% on test-zh and from 8.32% to 7.08% on test-hard-zh, and word error rate (WER) from 1.32% to 1.27% on test-en, compared with joint training alone. Subsequent reinforcement learning further reduces CER to 6.29% on test-hard-zh and WER to 1.08% on test-en, with speaker similarity scores of 0.811, 0.766, and 0.784 on test-zh, test-en, and test-hard-zh, respectively.

</details>

### [CAST: A Deployed Speech-to-Text Cascade for Closed Captioning of Entertainment Television](https://arxiv.org/abs/2611.31055)
*Aditya Mishra, Thanish Bolla, Bidisha Sharma et al.* · `cs.SD` · arXiv:2611.31055v1 · relevance 0.07

- **In one sentence**: CAST is a deployed speech-to-text pipeline for closed captioning of long-form entertainment TV that wraps a frozen Whisper large-v3 model with hierarchical voice activity detection, language identification, lyrics routing, and hallucination detection and repair, evaluated against a WhisperX baseline on in-house assets and public datasets.
- **In plain words**: Automatic captioning of TV shows is hard because scenes often mix music, sound effects, accents, people talking over each other, and background noise. This paper describes a captioning system, called CAST, built around an existing speech recognition model, with extra steps that decide which parts of the audio to transcribe and fix errors the model invents. On 100 internal TV assets totaling about 60 hours, the authors report lower word error and fewer subtitle edits per hour than the WhisperX baseline, and say the system went into production use in late August 2026.
- **Why it matters**: Captioning long entertainment video is a practical problem for broadcasters and streaming services, and the paper focuses on the pipeline around the recognition model (segmentation, filtering, error repair) rather than on the model itself. The evidence is limited to the authors' in-house assets plus a deletion-rate gain on public data, so the results should be read as a single deployment report rather than a general benchmark.
- **Background needed**: - Automatic speech recognition (ASR): software that turns spoken audio into text.
- Whisper: a large open speech recognition model; "frozen" means its internal weights were not retrained here.
- Voice activity detection (VAD): a step that finds which parts of audio contain speech and which are silence or noise.
- Hallucination in autoregressive decoders: the model writes plausible but false text, or repeats phrases, when fed near-silent or unclear audio.
- Word error rate (WER): the share of words wrongly transcribed; lower is better.
- Subtitle edit rate: how much human editing a caption file needs, measured per hour of video here.
- Deletion rate: the share of spoken words the system leaves out entirely.
- Closed captioning (CC): on-screen text for viewers who are deaf or hard of hearing, or for muted viewing. · level: intermediate

<details><summary>Original abstract</summary>

Despite rapid progress in automatic speech recognition (ASR), caption generation for long-form entertainment video remains challenging for content dense in music and effects, rich in accents, crosstalk, and noise. The transcript quality depends on segmentation and surrounding modules as much as the acoustic model. A single pass voice activity detection (VAD) can miss faint, low-energy voice while forwarding near-silent segments that induce hallucination and repetition in an autoregressive decoder. These competing errors motivate a hierarchical VAD that revisits rejected segments under semantic and acoustic retention checks. We present Captioning ASR Stack for Television (CAST), an integrated speech-to-text pipeline for closed captioning (CC) combining frozen Whisper large-v3 with segmentation, language identification, lyrics routing, and targeted hallucination detection and repair on a single NVIDIA L4 GPU. On 100 in-house assets spanning 60.46 hours, CAST reduces normalized WER from 6.99% to 5.36% and subtitle edit rate from 254.2 to 221.9 min/hour against the WhisperX pipeline, and improves deletion rate by 11% on public datasets. We also present the behavior of each stage in the pipeline. CAST entered the production speech-to-text (STT) stage of our CC pipeline in late August 2026; we report the evaluation evidence and path to full-scale operation.

</details>

## Control systems

### [Autonomous UAV Navigation in an Unknown Environment via Multi-Trajectory Model Predictive Control](https://arxiv.org/abs/2611.30463)
*Danilo Saccani, Lorenzo Fagiano* · `eess.SY` · arXiv:2611.30463v1 · relevance 0.17

- **In one sentence**: The paper proposes multi-trajectory MPC (mt-MPC), which plans several candidate future state trajectories within one finite-horizon optimal control problem to partly separate obstacle-avoidance constraints from goal-reaching cost, and applies it to a LiDAR-equipped UAV flying in an unknown, time-invariant environment with recursive feasibility guarantees.
- **In plain words**: This paper is about getting a drone to fly to a target while avoiding obstacles it can only partly see, using its laser scanner. The authors built a planning method that considers several possible future flight paths at once, so that staying safe and making progress toward the goal are handled more separately. In simulation, it performed better than a standard version of the same kind of controller.
- **Why it matters**: Flying safely in places that are not fully mapped is a practical problem for drones and other autonomous vehicles. The text reports a simulation comparison with a standard controller and a formal guarantee under a stated assumption (that the environment does not change over time), but it does not show real-world flight tests, so its practical reach is uncertain.
- **Background needed**: - Model predictive control (MPC): at each moment, the controller plans a short future sequence of actions by solving an optimization problem, applies the first step, then re-plans.
- Finite Horizon Optimal Control Problem: the optimization over a limited look-ahead window that MPC solves repeatedly.
- Constraints and cost: constraints are rules the path must obey (such as not hitting obstacles); the cost is what is minimized (such as distance to target).
- Recursive feasibility: the guarantee that if a valid plan exists now, a valid plan will still exist at the next step, so the controller never gets stuck without a safe option.
- LiDAR: a laser sensor that measures distances to nearby surfaces, giving only a partial view of obstacles.
- Hierarchical control: low-level loops keep the vehicle stable and follow setpoints, while the high-level MPC chooses where to go. · level: research-level

<details><summary>Original abstract</summary>

A novel model predictive control (MPC) formulation, named multi-trajectory MPC (mt-MPC), is presented and applied to the problem of autonomous navigation of an unmanned aerial vehicle (UAV) in an unknown environment. The UAV is equipped with a LiDAR sensor, providing only a partial description of the surroundings and resulting in time-varying constraints as the vehicle navigates among the obstacles. The control system layout is hierarchical: the low-level loops stabilize the vehicle's trajectories and track the set-points commanded by the high-level, mt-MPC controller. The latter is required to plan the UAV trajectory trading off safety, i.e. to avoid collisions with the uncertain obstacles, and exploitation, i.e. to reach an assigned target location. To achieve this goal, mt-MPC considers different future state trajectories in the same Finite Horizon Optimal Control Problem (FHOCP), enabling a partial decoupling between constraint satisfaction (safety) and cost function minimization (exploitation). Recursive feasibility and, consequently, persistent obstacle avoidance guarantees are derived under the assumption of a time invariant environment. The performance of the approach is studied in simulation and compared with that of a standard MPC, showing good improvement.

</details>

### [Performance Evaluation of Nonlinear Model Predictive and Sliding Mode Controllers on a 4-Cable Spatial CSPR in Simscape](https://arxiv.org/abs/2611.29748)
*Erfun Bayat Sarmadi, Ali Asadi, Moosa Ayati* · `cs.RO` · arXiv:2611.29748v1 · relevance 0.15

- **In one sentence**: A comparative simulation study of nonlinear model predictive control (NMPC) and sliding mode control (SMC) on a four-cable spatial cable-suspended parallel robot, using both an analytical dynamic model with cable elasticity and friction and a MATLAB Simscape Multibody model.
- **In plain words**: This paper compares two ways of steering a robot that is held up and moved by four cables strung in three-dimensional space. The authors built the robot's behavior two ways, one with equations and one in a physics simulator, and tested two control methods on both. They report that the predictive method (NMPC) tracked the target path more accurately and resisted disturbances better than the sliding mode method, but needed more computing power.
- **Why it matters**: Cable-driven robots are of interest for large or high-precision motion tasks, and the paper's point that a physics simulator can check a controller before hardware exists is useful. The text does not give the numerical results, so the size of the advantage is unclear from the summary alone.
- **Background needed**: - Cable-suspended parallel robot: an end-effector held in place by several cables whose lengths are changed by motors.
- Control system: the logic that computes motor commands to make the robot follow a planned path.
- Nonlinear model predictive control (NMPC): at each step, the controller predicts future behavior with a model and optimizes its commands, respecting limits.
- Sliding mode control (SMC): a robust method that forces the system onto a chosen target behavior using switching commands.
- Simscape Multibody: a MATLAB tool for simulating mechanical systems with realistic physics.
- Cable elasticity and friction: real cables stretch and lose energy, which idealized models may omit. · level: intermediate

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
| AI industry news | 36 | 26 | 5 |
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
| Pharmacology and drug discovery | 7 | 6 | 0 |
| Computational and systems biology | 86 | 81 | 2 |
| Neuroscience | 45 | 40 | 2 |
| Genetics and genomics | 32 | 29 | 2 |
| Cell and molecular biology | 42 | 40 | 2 |
| Immunology and microbiology | 41 | 35 | 2 |
| Cancer biology | 19 | 15 | 2 |
| Ecology and evolution | 36 | 33 | 2 |
| Plant biology | 18 | 14 | 2 |
| Bioengineering and synthetic biology | 13 | 10 | 2 |
| Mathematical biology (arXiv) | 22 | 20 | 2 |
| Epidemiology | 14 | 13 | 2 |
| Infectious diseases | 4 | 3 | 1 |
| Public and global health | 18 | 14 | 2 |
| Psychiatry and neurology | 17 | 14 | 2 |
| Oncology | 6 | 3 | 1 |
| Health informatics and medical AI | 11 | 7 | 2 |
| Econometrics and applied economics | 22 | 18 | 2 |
| Economic theory | 11 | 8 | 2 |
| Game theory and algorithmic economics | 17 | 15 | 2 |
| Mathematical finance | 13 | 11 | 2 |
| Financial markets | 21 | 16 | 2 |
| Signal processing | 57 | 55 | 2 |
| Audio and speech | 30 | 28 | 2 |
| Control systems | 68 | 66 | 2 |

<!-- {% endraw %} -->
