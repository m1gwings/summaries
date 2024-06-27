---
marp: true
theme: summary
math: mathjax
---
# Convex analysis

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Edoardo Amaldi_)

</div>

## Basic concepts

- In $\mathbb{R}^n$ with Euclidean norm:
> - $\underline{x} \in S \subseteq \mathbb{R}^n$ is an **interior point** of $S$ if $\exists \epsilon > 0$ such that $B_\epsilon(\underline{x}) = \{ \underline{y} \in \mathbb{R}^n \ | \ ||\underline{y} - \underline{x}|| < \epsilon \} \subseteq S$.
> - $\underline{x} \in \mathbb{R}^n$ is a **boundary point** of $S$ if, for every $\epsilon > 0$, $B_\epsilon(\underline{x})$ contains at least one point of $S$ and one point of $\mathbb{R}^n \setminus S$.
> - The set of all the interior points of $S$ is the **interior** of $S$,
denoted by $\text{int}(S)$.
> - The set of all boundary points of $S$ is the **boundary** of $S$,
denoted by $\partial(S)$.
> - $S \subseteq \mathbb{R}^n$ is **open** if $S = \text{int}(S)$; $S$ is **closed** if its complement is open. Equivalently, $S$ is closed iff $\partial(S) \subseteq S$.
> - $S \subseteq \mathbb{R}^n$ is **bounded** if $\exists M > 0$ such that $||\underline{x}|| < M$ for every $\underline{x} \in S$.
> - $S \subseteq \mathbb{R}^n$ closed and bounded is **compact**.

- **Theorems**:
> - $S \subseteq \mathbb{R}^n$ is closed iff every sequence $\{ \underline{x}_i \}_{i \in \mathbb{N}} \subseteq S$ that converges, converges to $\underline{\overline{x}} \in S$. [_Trivial, since it must be $\underline{\overline{x}} \in \partial(S)$_].
> - $S \subseteq \mathbb{R}^n$ is compact iff every sequence $\{ \underline{x}_i \}_{i \in \mathbb{N}} \subseteq S$ admits a subsequence that converges to a point $\underline{x} \in S$. [_See Baby Rudin_].


In general, when minimizing $f : S \subseteq \mathbb{R}^n \rightarrow \mathbb{R}$, we only know that a largest lower bound (infimum) exists, that is:
$$
\inf_{\underline{x} \in S} f(\underline{x}).
$$

- **Weierstrass theorem**: let $S \subseteq \mathbb{R}^n$ be nonempty and compact, and $f : S \rightarrow \mathbb{R}$ be continuous. Then $\exists \underline{x}^* \in S$ such that $f(\underline{x}^*) \leq f(\underline{x}) \ \forall \underline{x} \in S$.
When $\underline{x}^*$ exists, we can write $\min_{\underline{x} \in S} f(\underline{x})$.

## Cones and affine subspaces

Consider any $S \subset \mathbb{R}^n$.

- $\text{cone}(S)$ denotes the set of all **conic combinations** of points of $S$, i.e., all $\underline{x} = \sum_{i=1}^m \alpha_i \underline{x}_i$ with $\underline{x}_1, \ldots, \underline{x}_m \in S$ and $\alpha_i \geq 0 \ \forall i \in \{ 1, \ldots, m \}$.

---

- $\text{aff}(S)$ denotes the smallest **affine subspace** that contains $S$.

- **Theorem**: $\text{aff}(S)$ coincides with the set of all **affine combinations** of points in $S$, i.e., all $\underline{x} = \sum_{i=1}^m \alpha_i \underline{x}_i$ with $\underline{x}_1, \ldots, \underline{x}_m \in S$, $\sum_{i=1}^m \alpha_i = 1$, and $\alpha_i \in \mathbb{R} \ \forall i \in \{ 1, \ldots, m \}$.

> **Proof**: if $S = \emptyset$ there is nothing to prove: $\text{aff}(S) = \emptyset$.
Suppose that $S \neq \emptyset$. Then, there exists $\overline{\underline{x}} \in S$. Clearly $\overline{\underline{x}} \in \text{aff}(S)$.
First of all let's prove that $\text{aff}(S)$ is an affine subspace.
In particular we want to show that:
$$
\overline{\underline{x}} + \lambda_1 (\underline{y}_1 - \overline{\underline{x}}) + \lambda_2 (\underline{y}_2 - \overline{\underline{x}}) \in \text{aff}(S) \ \forall \underline{y}_1, \underline{y}_2 \in \text{aff}(S), \lambda_1, \lambda_2 \in \mathbb{R}.
$$
> Fix $\underline{y}_1, \underline{y}_2 \in \text{aff}(S), \lambda_1, \lambda_2 \in \mathbb{R}$. Then:
$$
\underline{y}_1 = \alpha_{1,1} \underline{x}_1' + \ldots + \alpha_{1,m_1} \underline{x}_{m_1}',
$$
$$
\underline{y}_2 = \alpha_{2,1} \underline{x}_1'' + \ldots + \alpha_{2,m_2} \underline{x}_{m_2}''
$$
> where $\underline{x}_1', \ldots, \underline{x}_{m_1}', \underline{x}_1'', \ldots, \underline{x}_{m_2}'' \in S$, and $\sum_{i=1}^{m_1} \alpha_{1,i} = \sum_{i=1}^{m_2} \alpha_{2,i} = 1$.
Then:
$$
\overline{\underline{x}} + \lambda_1 (\underline{y}_1 - \overline{\underline{x}}) + \lambda_2 (\underline{y}_2 - \overline{\underline{x}}) = (1-\lambda_1-\lambda_2) \underline{\overline{x}} +
$$
$$
+ \sum_{i=1}^{m_1} (\lambda_1 \alpha_{1,i}) \underline{x}_i' + \sum_{i=1}^{m_2} (\lambda_2 \alpha_{2,i}) \underline{x}_i'',
$$
> where $\underline{\overline{x}}, \underline{x}_1', \ldots, \underline{x}_{m_1}', \underline{x}_1'', \ldots, \underline{x}_{m_2}'' \in S$ and
$$
1-\lambda_1-\lambda_2 + \lambda_1 \sum_{i=1}^{m_1} \alpha_{1,i} + \lambda_2 \sum_{i=1}^{m_2} \alpha_{2,i} = 1 - \lambda_1 - \lambda_2 + \lambda_1 + \lambda_2 = 1,
$$
> as we wanted to prove.
> Now let $A$ be an affine subspace such that $S \subseteq A$.
Let $\alpha_1 \underline{x}_1 + \ldots + \alpha_m \underline{x}_m \in \text{aff}(S)$. Then:
$$
\alpha_1 \underline{x}_1 + \ldots + \alpha_m \underline{x}_m = \left(\sum_{i=1}^m \alpha_i \right) \underline{\overline{x}} + \alpha_1 (\underline{x}_1 - \underline{\overline{x}}) + \ldots + \alpha_m (\underline{x}_m - \underline{\overline{x}}) =
$$
$$
= \underline{\overline{x}} + \alpha_1 (\underline{x}_1 - \underline{\overline{x}}) + \ldots + \alpha_m (\underline{x}_m - \underline{\overline{x}}) \in A
$$
> since $\underline{\overline{x}}, \underline{x}_1, \ldots, \underline{x}_m \in S \subseteq A$ and $A$ is affine. This means that $\text{aff}(S) \subseteq A$ and thus concludes the proof.

---

## Elements of convex analysis

- $C \subset \mathbb{R}^n$ is **convex** if
$$
\alpha \underline{x}_1 + (1-\alpha) \underline{x}_2 \in C \ \forall \underline{x}_1, \underline{x}_2 \in C \text{ and } \forall \alpha \in [0, 1].
$$

- $\underline{x} \in \mathbb{R}^n$ is a **convex combination** of $\underline{x}_1, \ldots, \underline{x}_m \in \mathbb{R}^n$ if
$$
\underline{x} = \sum_{i=1}^m \alpha_i \underline{x}_i
$$
> with $\sum_{i=1}^m \alpha_i = 1$ and $\alpha_i \geq 0 \ \forall i \in \{ 1, \ldots, m \}$.

> **Theorem**: if $C_i$ is convex $\forall i \in \{ 1, \ldots, k \}$ are convex, then
$$
\bigcap_{i=1}^k C_i
$$
> is convex.

> **Proof**: _trivial_.

Let's list some _examples of convex sets_:
1. **Hyperplane** $H = \{ \underline{x} \in \mathbb{R}^n \ | \ \underline{p}^T \underline{x} = \beta \}$ with $\underline{p} \neq \underline{0}$. [_See the recap on hyperplanes in the FOR LP summary_].
**Remark**: $H$ is closed since $H = \partial(H)$.
2. Closed **half-spaces** $H^+ = \{ \underline{x} \in \mathbb{R}^n \ | \ \underline{p}^T \underline{x} \geq \beta \}$ and $H^- = \{ \underline{x} \in \mathbb{R}^n \ | \ \underline{p}^T \underline{x} \leq \beta \}$ with $\underline{p} \neq \underline{0}$.
3. **Feasible region of a LP** $X = \{ \underline{x} \in \mathbb{R}^n \ | \ A \underline{x} \geq \underline{b}, \underline{x} \geq \underline{0} \}$ (_it is the intersection of $m+n$ closed half-spaces if $A \in \mathbb{R}^{m \times n}$_).

- A **polyhedron** is the intersection of a finite number of closed half-spaces.
**Remark**: the set of optimal solutions of a LP is a polyhedron defined by the constraints of the original LP plus an additional "optimality constraint": $\underline{c}^T \underline{x} = z^*$ where $z^*$ is the optimal value for the objective function.

### Convex hulls and extreme points

- The **convex hull** of $S \subseteq \mathbb{R}^n$, denoted by $\text{conv}(S)$, is the intersection of all convex sets containing $S$.
An _equivalent characterization_ sees the convex hull as the set of all convex combinations of points in $S$ [_the equivalence is trivial remembering that $A \cap B \subseteq A$_].

- Given $C \subseteq \mathbb{R}^n$ convex, $\underline{x} \in C$ is an **extreme point** of $C$ if it cannot be expressed as convex combination of two different points of $C$, that is

---

$$
\underline{x} = \alpha \underline{x}_1 + (1-\alpha) \underline{x}_2 \text{ with } \underline{x}_1, \underline{x}_2 \in C \text{ and } \alpha \in (0, 1)
$$
> implies that $\underline{x}_1 = \underline{x}_2 = \underline{x}$.

### Projection on a convex set

- **Projection lemma**: let $C \subseteq \mathbb{R}^n$ be nonempty, closed, and convex, then for every $\underline{y} \not \in C$ there exits a unique $\underline{x}' \in C$ at minimum distance from $\underline{y}$. Moreover, $\underline{x}' \in C$ is the closed point to $\underline{y}$ if and only if
$$
(\underline{y} - \underline{x}')^T (\underline{x} - \underline{x}') \leq 0 \ \forall \underline{x} \in C.
$$

> **Proof**: let $d^* = \inf \{ || \underline{y} - \underline{x} || \ | \ \underline{x} \in C \}$. Observe that $d^*$ is well defined since $|| \underline{y} - \underline{x} ||$ is bounded below by $0$ and non-empty. By the properties of the infimum, there exists a sequence $\{ \underline{x}_i \}_{i \in \mathbb{N}} \subseteq C$ s.t.
$$
d^* \leq || \underline{y} - \underline{x}_i || < d^* + \frac{1}{i} \ \forall i \in \mathbb{N}^+.
$$
> Such sequence is bounded, hence it has a converging subsequence $\{ \underline{x}_{i_j} \}_{j \in \mathbb{N}}$ [_see Baby Rudin_] which converges to a point $\underline{x}'$. Since $C$ is closed, $\underline{x}' \in C$. Furthermore, since limits preserve inequalities, it must be:
$$
d^* \leq ||\underline{y} - \underline{x}'|| \leq d^*,
$$
> that is $\underline{x}' \in C$ is among the closest points to $\underline{y}$.
Now suppose there exists $\underline{x}'' \in C$, $\underline{x}'' \neq \underline{x}'$ s.t. $||\underline{y} - \underline{x}''|| = d^*$.
Then we have:
$$
2 || \underline{y} - \underline{x}' ||^2 = || \underline{y} - \underline{x}' ||^2 + || \underline{y} - \underline{x}'' ||^2 = \frac{||\underline{y} - \underline{x}'||^2}{2} + \frac{||\underline{y} - \underline{x}''||^2}{2} +
$$
$$
+ \frac{||\underline{y} - \underline{x}'||^2 + ||\underline{y} - \underline{x}''||^2}{2} = \frac{||\underline{y} - \underline{x}'||^2}{2} + \frac{||\underline{y} - \underline{x}''||^2}{2} +
$$
$$
+ \frac{||\underline{y} - \underline{x}'' - (\underline{y} - \underline{x}')||^2 + 2(\underline{y} - \underline{x}')^T(\underline{y} - \underline{x}'')}{2} = 2 \left[ \left|\left|\frac{\underline{y} - \underline{x}'}{2}\right|\right|^2 + \left|\left|\frac{\underline{y} - \underline{x}''}{2}\right|\right|^2 + \frac{(\underline{y} - \underline{x}')^T(\underline{y} - \underline{x}'')}{2} \right] +
$$

$$
+ \frac{||\underline{x}' - \underline{x}''||^2}{2} =  2 \left|\left| \frac{\underline{y} - \underline{x}'}{2} + \frac{\underline{y} - \underline{x}''}{2} \right|\right|^2 + \frac{||\underline{x}' - \underline{x}''||^2}{2} = 2 \left|\left|\underline{y} - \frac{\underline{x}' + \underline{x}''}{2}\right|\right|^2 + \frac{||\underline{x}' - \underline{x}''||^2}{2}.
$$
> Since $C$ is convex, $\frac{\underline{x}' + \underline{x}''}{2} \in C$. Furthermore, by the previous expression:
$$
\left|\left|\underline{y} - \frac{\underline{x}' + \underline{x}''}{2}\right|\right|^2 = ||\underline{y} - \underline{x}'||^2 - \frac{||\underline{x}' - \underline{x}''||^2}{2} < d^*,
$$

---

> but this is a contradiction.
We still need to prove the second part of the lemma. Fix $\underline{x} \in C$. Let $\underline{x} \in C$, $\lambda \in (0, 1)$. Since $C$ is convex, $\lambda \underline{x} + (1-\lambda) \underline{x}' \in C$. Then:
$$
||\underline{y} - \underline{x}'||^2 = {d^*}^2 \leq ||\underline{y} - \underline{x}' - \lambda (\underline{x} - \underline{x}')||^2 = ||\underline{y} - \underline{x}'||^2 - 2\lambda (\underline{y} - \underline{x}')^T(\underline{x} - \underline{x}') +
$$
$$
+ \lambda^2 ||\underline{x} - \underline{x}'||^2.
$$
That is:
$$
2 (\underline{y} - \underline{x}')^T (\underline{x} - \underline{x}') \leq \lambda || \underline{x} - \underline{x}' ||^2.
$$
> Letting $\lambda \rightarrow 0^+$, we have:
$$
(\underline{y} - \underline{x}')^T(\underline{x} - \underline{x}') \leq 0.
$$
> Conversely, suppose that:
$$
(\underline{y} - \underline{x}')^T(\underline{x} - \underline{x}') \leq 0 \ \forall \underline{x} \in C.
$$
> Then:
$$
||\underline{y} - \underline{x}||^2 = ||\underline{y} - \underline{x}'||^2 + ||\underline{x}' - \underline{x}||^2 + 2 (\underline{y} - \underline{x}')^T(\underline{x}' - \underline{x}) \geq
$$
$$
\geq ||\underline{y} - \underline{x}'||^2 + ||\underline{x}' - \underline{x}||^2 \geq ||\underline{y} - \underline{x}'||^2.
$$

- We call the point $\underline{x}'$, characterized in the previous lemma, the **projection** of $\underline{y}$ on $C$.

### Separation theorem

We are going to present a geometrically intuitive but fundamental result.

- **Separating hyperplane theorem**: let $C \subset \mathbb{R}^n$ be non-empty, closed, and convex. Let $\underline{y} \not \in C$, then $\exists \underline{p} \in \mathbb{R}^n$, $\underline{p} \neq \underline{0}$ such that $\underline{p}^T \underline{x} < \underline{p}^T \underline{y}$ for every $\underline{x} \in C$.
In particular, there exits $\beta \in \mathbb{R}$ s.t. the hyperplane $H = \{ \underline{x} \in \mathbb{R}^n \ | \ \underline{p}^T \underline{x} = \beta \}$ separates $\underline{y}$ from $C$, i.e., more formally: $\underline{p}^T \underline{x} < \beta \ \forall \underline{x} \in C$ and $\underline{p}^T \underline{y} > \beta$.

> **Proof**: because of the projection lemma, we know that there exists a point $\underline{x}' \in C$ s.t.
$$
(\underline{y} - \underline{x}')^T(\underline{x} - \underline{x}') \leq 0 \ \forall \underline{x} \in C.
$$
> Let $\underline{p} = \underline{y} - \underline{x}'$. Observe that $\underline{p} \neq \underline{0}$ since $\underline{y} \not \in C$, $\underline{x}' \in C$.
Let
$$
\beta = \frac{\underline{p}^T (\underline{x}' + \underline{y})}{2}.
$$

---

> Fix $\underline{x} \in C$. Then:
$$
\underline{p}^T \underline{x} = \underline{p}^T (\underline{x} - \underline{x}') + \frac{\underline{p}^T (\underline{x}' + \underline{y})}{2} - \frac{\underline{p}^T (\underline{y} - \underline{x}')}{2} =
$$
$$
= (\underline{y} - \underline{x}')^T (\underline{x} - \underline{x}') + \beta - \frac{||\underline{p}||^2}{2} \leq \beta - \frac{||\underline{p}||^2}{2} < \beta.
$$
> Finally:
$$
\underline{p}^T \underline{y} = \frac{\underline{p}^T (\underline{y} - \underline{x}')}{2} + \frac{\underline{p}^T(\underline{x}' + \underline{y})}{2} = \frac{||\underline{p}||^2}{2} + \beta > \beta.
$$

#### Consequences of the separation theorem

1. Any non-empty, closed and convex set $C \subset \mathbb{R}^n$ is the intersection of all closed half-spaces containing it.

> **Proof**: clearly $C$ is a subset of such set. Furthermore, for every $\underline{y} \not \in C$, there exists an half-space which contains $C$ but not $\underline{y}$ (_here we are using the separation theorem_), hence $\underline{y}$ doesn't belong to the intersection of all half-spaces containing $C$.

2. Let $S \subset \mathbb{R}^n$ with $S \neq \emptyset$ and $\underline{\overline{x}} \in \partial(S)$ (boundary w.r.t. $\text{aff}(S)$), $H = \{ \underline{x} \in \mathbb{R}^n \ | \ \underline{p}^T (\underline{x} - \underline{\overline{x}}) = 0 \}$ is a **supporting hyperplane** of $S$ at $\underline{\overline{x}}$ if $S \subseteq H^-$ or $S \subseteq H^+$.
> **Remark**: if $\text{aff}(S) \neq \mathbb{R}^n$, then $\partial(S)$ w.r.t. $\mathbb{R}^n$ is $S$.

> **Proof**: since $\underline{\overline{x}} \in \partial(S)$, there exists a sequence $\{ \underline{y}_i \}_{i \in \mathbb{N}}$ s.t. $\underline{y}_i \not \in C \ \forall i \in \mathbb{N}$ and $\underline{y}_i \rightarrow \underline{\overline{x}}$. Because of the separation theorem, for all $i \in \mathbb{N}$ there exists $\underline{p}_i$ with norm $1$ (_just divide both sides by $||\underline{p}|| \neq 0$_) s.t. $\underline{p}_i^T \underline{x} < \underline{p}_i^T \underline{y}_i \ \forall \underline{x} \in C$. The sequence $\{ \underline{p}_i \}_{i \in \mathbb{N}}$ is bounded, hence it admits a convergent subsequence [_see Baby Rudin_] $\{ \underline{p}_{i_j} \}_{j \in \mathbb{N}}$ which tends to $\underline{p}$. Then:
$$
\underline{p}_{i_j}^T (\underline{x} - \underline{y}_{i_j}) < 0 \ \forall \underline{x} \in C.
$$
> By taking the limit observing that the dot product is continuous:
$$
\underline{p}^T (\underline{x} - \underline{\overline{x}}) \leq 0 \ \forall \underline{x} \in C.
$$
> Hence, $S \subseteq H^- = \{ \underline{x} \in \mathbb{R}^n \ | \ \underline{p}^T \underline{x} \leq \underline{p}^T \underline{\overline{x}} \}$ as we wanted to prove.

---

3. **Farkas lemma**: let $A \in \mathbb{R}^{m \times n}$ and $\underline{b} \in \mathbb{R}^m$. Then
$$
\exists \underline{x} \in \mathbb{R}^n \text{ s.t. } A \underline{x} = \underline{b} \text{ and } \underline{x} \geq \underline{0} \iff \not \exists \underline{y} \in \mathbb{R}^m \text{ s.t. } \underline{y}^T A \leq \underline{0}^T \text{ and } \underline{y}^T \underline{b} > 0.
$$

> _Farkas lemma_ provides an infeasibility certificate, it is also known as the theorem of the alternative: exactly one of $A \underline{x} = \underline{b}, \underline{x} \geq \underline{0}$ and $\underline{y}^T A \leq \underline{0}^T, \underline{y}^T \underline{b} > 0$ is feasible.
It has also a _geometric interpretation_: resume...
