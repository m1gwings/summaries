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
> - $S \subseteq \mathbb{R}^n$ is closed iff every sequence $\{ \underline{x}_i \}_{i \in \mathbb{N}} \subseteq S$ that converges, converges to $\underline{\overline{x}} \in S$. [_Trivial, since you can build a sequence in $S$ converging to every $\underline{\overline{x}} \in \partial(S)$ and it must always be $\underline{\overline{x}} \in S \cup \partial(S)$_].
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
It has also a _geometric interpretation_: $\underline{b}$ belongs to the cone generated by the columns of $A$: $A_1, \ldots, A_n$, i.e. $\underline{b} \in \text{cone}(A) = \{ \underline{z} \in \mathbb{R}^n \ | \ \underline{z} = \sum_{j=1}^n x_j A_j, x_j \geq 0 \ \forall j \in \{ 1, \ldots, n \} \}$ if and only if no hyperplane separating $\underline{b}$ from $\text{cone}(A)$ exists.

> As anticipated in the geometric interpretation, we want to use the separation theorem to prove Farkas lemma, but the theorem applies only to non-empty, closed, and convex sets. Cones are clearly convex, and, in particular, $\text{cone}(A)$ is also non-empty. We need to show that it is also closed. This will require some intermediate result.

- **Theorem**: if $S = \{ \underline{x}_1, \ldots, \underline{x}_r \}$ is a set of _linearly independent_ vectors, then $\text{cone}(S)$ is closed.

> **Proof**: we will prove that $\text{cone}(S)$ is closed by showing that every convergent sequence in $\text{cone}(S)$ converges to a point in $\text{cone}(S)$. Let $\{ \underline{x}_i \}_{i \in \mathbb{N}} \subseteq \text{cone}(S)$ s.t. $\underline{x}_i \rightarrow \underline{\overline{x}}$. Let $X = \begin{bmatrix} \underline{x}_1 & \cdots & \underline{x}_r \end{bmatrix}$. Observe that, by hypothesis, $r(X) = r$.
Hence, the SVD decomposition of $X$ [_see NAML summaries_] is $X = \sum_{i=1}^r \sigma_i(X) \underline{u}_i \underline{v}_i^T$ with $\sigma_1(X) \geq \ldots \geq \sigma_r(X) > 0$. Furthermore, we can build a unique sequence $\{ \underline{\alpha}_i \}_{i \in \mathbb{N}}$ s.t. $\underline{x}_i = X \underline{\alpha}_i$, $\underline{\alpha}_i \geq \underline{0}$ $\forall i \in \mathbb{N}$.
Being convergent, $\{ \underline{x}_i \}_{i \in \mathbb{N}}$ is a Cauchy sequence [_see Baby Rudin_]. We will show that the same holds for $\{ \underline{\alpha}_i \}_{i \in \mathbb{N}}$. Fix $\epsilon > 0$. Then, there exists $N \in \mathbb{N}$ s.t. for all $n, m \geq N$, $n, m \in \mathbb{N}$:
$$
\sigma_r^2(X) \epsilon^2 > ||\underline{x}_n - \underline{x}_m||^2 = ||X(\underline{\alpha}_n - \underline{\alpha}_m)||^2 = || \sum_{i=1}^r \sigma_i(X) \underline{u}_i \underline{v}_i^T (\underline{\alpha}_n - \underline{\alpha}_m) ||^2 =
$$
$$
= \sum_{i=1}^r \sigma_i^2(X) [\underline{v}_i^T (\underline{\alpha}_n - \underline{\alpha}_m)]^2 \geq \sigma_r^2(X) \sum_{i=1}^r [\underline{v}_i^T(\underline{\alpha}_n - \underline{\alpha}_m)]^2 =
$$
$$
= \sigma_r^2(X) (\underline{\alpha}_n - \underline{\alpha}_m)^T \left(\sum_{i=1}^r \underline{v}_i \underline{v}_i^T\right) (\underline{\alpha}_n - \underline{\alpha}_m) = \sigma_r^2(X) (\underline{\alpha}_n - \underline{\alpha}_m)^T I_r (\underline{\alpha}_n - \underline{\alpha}_m) = 
$$
$$
= \sigma_r^2(X) || \underline{\alpha}_n - \underline{\alpha}_m ||^2 \text{ iff } ||\underline{\alpha}_n - \underline{\alpha}_m|| < \epsilon.
$$
> Since every Cauchy sequence in $\mathbb{R}^r$ is convergent [_see Baby Rudin_], $\underline{\alpha}_i \rightarrow \underline{\overline{\alpha}}$.

---

> Remember that [_see Baby Rudin_]:
$$
\lim_{i \rightarrow +\infty} \begin{bmatrix} \alpha_{i,1} \\ \vdots \\ \alpha_{i,r} \end{bmatrix} = \begin{bmatrix} \lim_{i \rightarrow +\infty} \alpha_{i,1} \\ \vdots \\ \lim_{i \rightarrow +\infty} \alpha_{i,r} \end{bmatrix},
$$
> hence, if $\underline{\alpha}_i \geq \underline{0} \ \forall i \in \mathbb{N}$ by applying the comparison theorem component-wise: $\underline{\overline{\alpha}} \geq \underline{0}$.
> Finally:
$$
\underline{\overline{x}} = \lim_{i \rightarrow +\infty} \underline{x}_i = \lim_{i \rightarrow + \infty} X \underline{\alpha}_i = X \lim_{i \rightarrow +\infty} \underline{\alpha}_i = X \underline{\overline{\alpha}}
$$
> with $\underline{\overline{\alpha}} \geq \underline{0}$. Hence $\underline{\overline{x}} \in \text{cone}(S)$.

- **Carathéodory theorem for cones**: let $\underline{x} \in \text{cone}(S)$ where $S = \{ \underline{x}_1, \ldots, \underline{x}_m \}$. Then $\underline{x} \in \text{cone}(S')$ where $S' = \{ \underline{x}_{k_1}, \ldots, \underline{x}_{k_r} \} \subseteq S$ is a set of linearly independent vectors. Hence $\text{cone}(S) = \bigcup_{\begin{matrix}S' \subseteq S \\ S' \text{ lin. ind.}\end{matrix}} \text{cone}(S')$. [_Observe that it is clear that $\bigcup_{\begin{matrix}S' \subseteq S \\ S' \text{ lin. ind.}\end{matrix}} \text{cone}(S') \subseteq \text{cone}(S)$, the converse inclusion follows by the statement of the theorem_].

> **Proof**: we will present a procedure that, if $\underline{x}$ is written as a conic combination of $p$ linearly dependent vectors, allows to express it as a combination of $p-1$ of the previous vectors. Hence we keep applying the procedure until we reach a linear independent set of vectors. Observe that the procedure must terminate since we start with a finite number of vectors.
We can always write $\underline{x} \in \text{cone}(S)$ as $\underline{x} = \alpha_1 \underline{x}_{j_1} + \ldots + \alpha_p \underline{x}_{j_p}$ with $\{ \underline{x}_{j_1}, \ldots, \underline{x}_{j_p} \} \subseteq S$, $\alpha_1, \ldots, \alpha_p \neq 0$. If $\{ \underline{x}_{j_1}, \ldots, \underline{x}_{j_p} \}$ are linearly independent, we are done. Otherwise there exits $\underline{\beta} \neq \underline{0}$ s.t. $\beta_1 \underline{x}_{j_1} + \ldots + \beta_p \underline{x}_{j_p} = \underline{0}$. Let $\gamma_i = \frac{\beta_i}{\alpha_i} \ \forall i \in \{ 1, \ldots, p \}$.
Then $\gamma_1 \alpha_1 \underline{x}_{j_1} + \ldots + \gamma_p \alpha_p \underline{x}_{j_p} = \underline{0}$.
If $\gamma_i \leq 0 \ \forall i \in \{ 1, \ldots, p \}$ let $\gamma'_i = - \gamma_i \ \forall i \in \{ 1, \ldots, p \}$, otherwise $\gamma'_i = \gamma_i \ \forall i \in \{ 1, \ldots, p \}$. Hence, in every case, $\max_{i=1}^n \gamma'_i > 0$.
Now let $\gamma''_i = \frac{\gamma'_i}{\max_{i=1}^p \gamma'_i} \ \forall i \in \{ 1, \ldots, p \}$. Then: $\gamma''_i \leq 1 \ \forall i \in \{ 1, \ldots, p \}$ and $\gamma''_{\hat{i}} = 1$ for some $\hat{i} \in \{ 1, \ldots, p \}$. Observe that, since we just rescaled the coefficients:
$$
\gamma''_1 \alpha_1 \underline{x}_{j_1} + \ldots + \gamma''_p \alpha_p \underline{x}_{j_p} = \underline{0}.
$$
> Then:
$$
\underline{x} = \alpha_1 \underline{x}_{j_1} + \ldots + \alpha_p \underline{x}_{j_p} - \gamma''_1 \alpha_1 \underline{x}_{j_1} - \ldots - \gamma''_p \alpha_p \underline{x}_{j_p} =
$$

---

$$
= (1-\gamma''_1) \alpha_1 \underline{x}_{j_1} + \ldots + (1-\gamma''_{j_p}) \alpha_p \underline{x}_{j_p}.
$$
> This concludes the proof since $(1-\gamma_i'')\alpha_i \geq 0 \ \forall i \in \{ 1, \ldots, p \}$ and $(1-\gamma_{\hat{i}}'') \alpha_{\hat{i}} = 0$, hence $\underline{x}$ is a conic combination of $\{ \underline{x}_{j_1}, \ldots, \underline{x}_{j_p} \} \setminus \{ \underline{x}_{j_{\hat{i}}} \}$.

- **Theorem**: if $S$ is finite, $\text{cone}(S)$ is closed.
> **Proof**: because of Carathéodory theorem:
$$
\text{cone}(S) = \bigcup_{\begin{matrix}S' \subseteq S \\ S' \text{ lin. ind.}\end{matrix}} \text{cone}(S').
$$
> We also showed that $\text{cone}(S')$ is closed. Then $\text{cone}(S)$ is the union of a <u>finite</u> (_the subsets of $S$ composed of linearly independent vectors are in finite number_) number of closed sets, hence it is closed [_see Baby Rudin_].

> Now we're ready to prove Farkas lemma.
**Proof**: suppose first that there exists $\underline{\tilde{x}} \in \mathbb{R}^n$, $\underline{\tilde{x}} \geq \underline{0}$ s.t. $A \underline{\tilde{x}} = \underline{b}$. Pick $\underline{y} \in \mathbb{R}^m$ s.t. $\underline{y}^T A \leq \underline{0}^T$. Then: $\underline{y}^T \underline{b} = \underline{y}^T A \underline{\tilde{x}} \leq 0$ since $\underline{y}^T A \leq \underline{0}^T$ and $\underline{\tilde{x}} \geq \underline{0}$ as we wanted to prove.

> We will prove the converse direction through the contrapositive. Suppose that there is no $\underline{x} \in \mathbb{R}^n$, $\underline{x} \geq \underline{0}$ s.t. $A \underline{x} = \underline{b}$. Then $\underline{b} \not \in \text{cone}(A)$. By the previous results, we can apply the separation theorem to $\text{cone}(A)$. Then, there exist $\underline{p} \neq \underline{0}$, $\beta$ s.t. $\underline{p}^T A \underline{x} < \beta < \underline{p}^T \underline{b}$ for all $\underline{x} \geq \underline{0}$ (_observe that every point in $\text{cone}(A)$ can be written as $A \underline{x}$ with $\underline{x} \geq \underline{0}$_).
By taking $\underline{x} = \underline{0}$ we obtain $\underline{p}^T \underline{b} > 0$. Furthermore it must $\underline{p}^T A \leq \underline{0}^T$, otherwise $\underline{p}^T A \underline{x}$ for $\underline{x} \geq \underline{0}$ would not be bounded above. Taking $\underline{y} = \underline{p}$ concludes the proof.

### Convex functions

- A **function** $f : C \rightarrow \mathbb{R}$ defined on a convex set $C \subseteq \mathbb{R}^n$ is **convex** if
$$
f(\alpha \underline{x}_1 + (1-\alpha) \underline{x}_2) \leq \alpha f(\underline{x}_1) + (1-\alpha) f(\underline{x}_2) \ \forall \underline{x}_1, \underline{x}_2 \in C, \alpha \in [0, 1].
$$
- $f$ is **strictly convex** if the inequality holds with $<$ for all $\underline{x}_1, \underline{x}_2 \in C$ with $\underline{x}_1 \neq \underline{x}_2$ and $\alpha \in (0, 1)$.
- $f$ is **concave** if $-f$ is convex.

- **Theorem**: $f$ is **linear** iff $f$ is both convex and concave.

- The **epigraph** of $f : S \subseteq \mathbb{R}^n \rightarrow \mathbb{R}$, denoted by $\text{epi}(f)$, is the subset of $\mathbb{R}^{n+1}$
$$
\text{epi}(f) = \{ (\underline{x}, y) \in S \times \mathbb{R} \ | \ f(\underline{x}) \leq y \}.
$$

---

- Let $f : C \rightarrow \overline{\mathbb{R}}$ be convex, the **domain** of $f$ is the subset of $\mathbb{R}^n$
$$
\text{dom}(f) = \{ \underline{x} \in C \ | \ f(\underline{x}) < + \infty \}.
$$

Let's list some properties of convex functions.

- **Theorems**: let $C \subseteq \mathbb{R}^n$ with $C \neq \emptyset$ and $f : C \rightarrow \mathbb{R}$ be convex.
> - For each $\beta \in \mathbb{R}$ (also $\beta = + \infty$), the level sets
$$
L_\beta = \{ \underline{x} \in C \ | \ f(\underline{x}) \leq \beta \} \text{ and } \{ \underline{x} \in C \ | \ f(\underline{x}) < \beta \}
$$
>> are convex subsets of $\mathbb{R}^n$.
> - $f$ is continuous in the relative interior (with respect to $\text{aff}(C)$) of its domain.
> - $f$ is convex if and only if $\text{epi}(f)$ is a convex subset of $\mathbb{R}^{n+1}$.
>> **Proof**: let $(\underline{x}_1, y_1), (\underline{x}_2, y_2) \in \text{epi}(f)$. Then $y_1 \geq f(\underline{x}_1)$ and $y_2 \geq f(\underline{x}_2)$. Let $\alpha \in [0, 1]$. Hence:
$$
\alpha \begin{bmatrix} \underline{x}_1 \\ y_1 \end{bmatrix} + (1-\alpha) \begin{bmatrix} \underline{x}_2 \\ y_2 \end{bmatrix} = \begin{bmatrix} \alpha \underline{x}_1 + (1-\alpha) \underline{x}_2  \\ \alpha y_1 + (1-\alpha) y_2 \end{bmatrix}.
$$
>> Observe that $\alpha \underline{x}_1 + (1-\alpha) \underline{x}_2 \in C$ since $C$ is convex. Furthermore:
$$
\alpha y_1 + (1-\alpha) y_2 \geq \alpha f(\underline{x}_1) + (1-\alpha) f(\underline{x}_2) \geq f(\alpha \underline{x}_1 + (1-\alpha) \underline{x}_2)
$$
>> since $f$ is convex. Hence $\text{epi}(f)$ is convex.

>> The converse direction is trivial observing that $(\underline{x}_1, f(\underline{x}_1)), (\underline{x}_2, f(\underline{x}_2)) \in \text{epi}(f)$.

### Optimal solution for convex problems

Consider the problem $\min_{\underline{x} \in C} f(\underline{x})$ where $C \subseteq \mathbb{R}^n$ and $f : C \rightarrow \mathbb{R}$ are convex.

- **Theorem**:
>> i. If $C$ and $f$ are convex, each local minimum of $f$ on $C$ is a global minimum.
>> ii. If $f$ is strictly convex on $C$, there exists at most one global minimum (there can be none if $f$ is unbounded, e.g. $-\log x$).

> **Proof**:
>> i. Let $\underline{x}^*$ be a local minimizer of $f$ on $C$. Suppose that there exists $\underline{x}' \in C$ s.t. $f(\underline{x}') < f(\underline{x}^*)$. Let $\alpha \in (0, 1)$. Then $f(\alpha \underline{x}' + (1-\alpha) \underline{x}^*) \leq \alpha f(\underline{x}') + (1-\alpha) f(\underline{x}') < f(\underline{x}^*)$.

---

>> But this contradicts the hypothesis that $\underline{x}^*$ is a local minimizer, since $\alpha \underline{x}' + (1-\alpha) \underline{x}^*$ can get arbitrarily close to $\underline{x}^*$. Hence $\underline{x}^*$ must be a global minimizer.

>> ii. Suppose that there are two global minimizers $\underline{x}_1^* \neq \underline{x}_2^*$. The it must be $f(\underline{x}_1^*) = f(\underline{x}_2^*)$. Furthermore $f(\frac{1}{2} \underline{x}_1^* + \frac{1}{2} \underline{x}_2^*) < \frac{1}{2} f(\underline{x}_1^*) + \frac{1}{2} f(\underline{x}_2^*) = f(\underline{x}_1^*)$. But this is absurd since $\underline{x}_1^*$ is a global minimizer.

An example of convex optimization problem is LP:
$$
\begin{matrix}
\min \underline{c}^T \underline{x} \\
\text{s.t. } A \underline{x} \geq \underline{b} \\
\underline{x} \geq \underline{0}
\end{matrix}.
$$

- **Theorem**: given any LP with $P = \{ \underline{x} \in \mathbb{R}^n \ | \ A \underline{x} \geq \underline{b}, \underline{x} \geq \underline{0} \}$, then either exists (at least) one optimal extreme point or the objective function value is unbounded over $P$.

### Characterizations for convex functions

- **Proposition 1**: $f : C \rightarrow \mathbb{R}$ of class $\mathcal{C}^1$ with non-empty convex and open $C \subseteq \mathbb{R}^n$ is convex if and only if
$$
f(\underline{x}) \geq f(\underline{\overline{x}}) + \nabla f^T(\underline{\overline{x}}) (\underline{x} - \underline{\overline{x}}) \ \forall \underline{x}, \underline{\overline{x}} \in C.
$$
> Furthermore $f$ is strictly convex if and only if the inequality holds with $>$ for all $\underline{x}, \underline{\overline{x}} \in C$, $\underline{x} \neq \underline{\overline{x}}$.

> **Proof**: [_see NAML summaries_].

> The _geometric interpretation_ of _proposition 1_ is that the linear approximation of $f$ at $\underline{\overline{x}}$ bounds below $f(\underline{x})$ and
$$
H = \left\{ \begin{bmatrix} \underline{x} \\ y \end{bmatrix} \in \mathbb{R}^{n+1} \ | \ \begin{bmatrix} \nabla f^T(\underline{\overline{x}}) & -1 \end{bmatrix} \begin{bmatrix} \underline{x} \\ y \end{bmatrix} = -f(\underline{\overline{x}}) + \nabla f^T(\underline{\overline{x}}) \underline{\overline{x}} \right\}
$$
> is a supporting hyperplane of $\text{epi}(f)$ at $(\underline{\overline{x}}, f(\underline{\overline{x}}))$, with $\text{epi}(f) \subseteq H^-$.

- **Proposition 2**: $f : C \rightarrow \mathbb{R}$ of class $\mathcal{C}^2$ with nonempty convex and open $C \subseteq \mathbb{R}^n$ is convex if and only if the Hessian matrix $\nabla^2 f(\underline{x})$ is positive semi-definite at every $\underline{x} \in C$. For $f \in \mathbb{C}^2$, if $\nabla^2f(\underline{x})$ is positive definite $\forall \underline{x} \in C$ then $f$ is strictly convex.

> **Important remark**: the last one is only a <u>sufficient</u> condition, but not necessary. For example $f(x) = x^4$ is strictly convex, but $f''(x) = 12 x^2$ is s.t. $f''(0) = 0$ which is clearly not positive definite.

---

### Convexity-preserving operations

Certain operations preserve convexity.

- **Theorem**: consider a convex set $C \subseteq \mathbb{R}^n$ and convex functions $f_i : C \rightarrow \mathbb{R}$ with $i \in \{ 1, \ldots, m \}$.
> - $g(\underline{x}) = \sum_{i=1}^m \lambda_i f_i(\underline{x})$ with $\lambda_i \geq 0 \ \forall i \in \{ 1, \ldots, m \}$ is convex.

>> **Proof**: let $\underline{x}_1, \underline{x}_2 \in C, \alpha \in [0, 1]$. Then:
$$
g(\alpha \underline{x}_1 + (1-\alpha) \underline{x}_2) = \sum_{i=1}^m \lambda_i f_i(\alpha \underline{x}_1 + (1-\alpha) \underline{x}_2) \leq
$$
$$
\leq \alpha \sum \lambda_i f(\underline{x}_1) + (1-\alpha) \sum_{i=1}^m \lambda_i f(\underline{x}_2) = \alpha g(\underline{x}_1) + (1-\alpha) g(\underline{x}_2).
$$

> - $g(\underline{x}) = \max_{i=1}^m f_i(\underline{x})$ is convex.

>> **Proof**: let $\underline{x}_1, \underline{x}_2 \in C, \alpha \in [0, 1]$. Then:
$$
g(\alpha \underline{x}_1 + (1-\alpha) \underline{x}_2) = \max_{i=1}^m f_i(\alpha \underline{x}_1 + (1-\alpha) \underline{x}_2) \leq \max_{i=1}^m \left[ \alpha f_i(\underline{x}_1) + (1-\alpha) f_i(\underline{x}_2) \right] \leq
$$
$$
\leq \alpha \max_{i=1}^m f_i(\underline{x}_1) + (1-\alpha) \max_{i=1}^m f_i(\underline{x}_2) = \alpha g(\underline{x}_1) + (1-\alpha) g(\underline{x}_2).
$$

### Subgradients of convex/concave functions

Consider a convex/concave not everywhere differentiable (but continuous) function, e.g. $f(x) = |x|$. We want to generalize the concept of gradient for $\mathcal{C}^1$ functions to this class of functions.

- Let $C \subseteq \mathbb{R}^n$ and $f : C \rightarrow \mathbb{R}$ be convex.
> - $\underline{\gamma} \in \mathbb{R}^n$ is a **subgradient** of $f$ at $\underline{\overline{x}}$ if
$$
f(\underline{x}) \geq f(\underline{\overline{x}}) + \underline{\gamma}^T (\underline{x} - \underline{\overline{x}}) \ \forall \underline{x} \in C.
$$
> - The **subdifferential**, denoted by $\partial f(\underline{x})$, is the set of all the subgradients of $f$ at $\underline{x}$.

Let $C \subseteq \mathbb{R}^n$ and $f : C \rightarrow \mathbb{R}$ be convex.
The following **properties** hold:

1. $f$ admits at least a subgradient at every interior point $\underline{\overline{x}}$ of $C$. In particular, if $\underline{\overline{x}} \in \text{int}(C)$ then $\exists \underline{\gamma} \in \mathbb{R}^n$ such that
$$
H = \left\{ (\underline{x}, y) \in \mathbb{R}^{n+1} \ | \ y = f(\underline{\overline{x}}) + \underline{\gamma}^T (\underline{x} - \underline{\overline{x}}) \right\}
$$

---

> is a supporting hyperplane of $\text{epi}(f)$ at $(\underline{\overline{x}}, f(\underline{\overline{x}}))$.

2. If $\underline{x} \in C$, $\partial f(\underline{x})$ is a non-empty, convex, closed and bounded set.

3. $\underline{x}^*$ is a (global) minimum of $f$ on $C$ if and only if $\underline{0} \in \partial f(\underline{x}^*)$.

> **Proof**: _trivial in both directions by definition of subgradient and global minimum_.
