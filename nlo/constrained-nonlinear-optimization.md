---
marp: true
theme: summary
math: mathjax
---
# Constrained Nonlinear Optimization

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Edoardo Amaldi_)

</div>

## Necessary optimality conditions

Consider the generic nonlinear constrained optimization problem:
$$
\begin{matrix}
\min f(\underline{x}) \\
\text{s.t. } g_i(\underline{x}) \leq 0 \ \forall i \in I = \{ 1, \ldots, m \} \\
\underline{x} \in \mathbb{R}^n
\end{matrix}
$$
where $f, g_i \in \mathcal{C}^1$.

Furthermore, we **assume** that the feasible region $S = \{ \underline{x} \in \mathbb{R}^n \ | \ g_i(\underline{x}) \leq 0 \ \forall i \in I \} \neq \emptyset$ but its interior can be empty.

- For each $\underline{\overline{x}} \in S$, we define:
> - $\mathcal{D}(\underline{\overline{x}}) = \{ \underline{d} \in \mathbb{R}^n \ | \ \exists \overline{\alpha} > 0 \text{ s.t. } \underline{\overline{x}} + \alpha \underline{d} \in S \ \forall \alpha \in [0, \overline{\alpha}] \}$ **cone of the feasible directions**;
> - $I(\underline{\overline{x}}) = \{ i \in I \ | \ g_i(\underline{\overline{x}}) = 0 \} \subseteq I$ set of **indices** of the **active constraints**;
> - $D(\underline{\overline{x}}) = \{ \underline{d} \in \mathbb{R}^n \ | \ \nabla g_i^T(\underline{\overline{x}}) \underline{d} \leq 0 \ \forall i \in I(\underline{\overline{x}}) \}$ **cone of the directions constrained by the gradients of the active constraints**.

- **Theorem**: $\overline{\mathcal{D}}(\underline{\overline{x}}) \subseteq D(\underline{\overline{x}})$ for all $\underline{\overline{x}} \in S$.

> **Proof**: given any $\underline{d} \in \mathcal{D}(\underline{\overline{x}})$, for sufficiently small $\alpha$ we have, by 1st order Taylor's expansion of $\phi_i(\alpha) = g_i(\underline{\overline{x}} + \alpha \underline{d})$ for $i \in I(\underline{\overline{x}})$ (_$\phi_i$ is well defined since $\underline{d} \in \mathcal{D}(\underline{\overline{x}})$_):
$$
\phi_i(\alpha) = g_i(\underline{\overline{x}}) + \alpha \nabla g_i^T(\underline{\overline{x}}) \underline{d} + o(\alpha) = \alpha \nabla g_i^T(\underline{\overline{x}}) \underline{d} + o(\alpha)
$$
> (since $i \in I(\underline{\overline{x}})$, $\phi_i(0) = 0$).
Furthermore, since $\underline{\overline{x}} + \alpha \underline{d} \in S$, $\phi(\alpha) = g_i(\underline{\overline{x}} + \alpha \underline{d}) \leq 0$. Then:
$$
\alpha \nabla g_i^T(\underline{\overline{x}}) \underline{d} + o(\alpha) \leq 0.
$$
> We can find $\delta > 0$ s.t. for $\alpha \in (0, \delta)$:
$$
\left| \frac{o(\alpha)}{\alpha} \right| < \left| \frac{\nabla g_i^T(\underline{\overline{x}}) \underline{d}}{2} \right|.
$$
> Then, picking $\alpha \in (0, \delta)$ we can show that:
$$
\nabla g_i^T(\underline{\overline{x}}) \underline{d} \leq 0.
$$

---

> This holds for all $i \in I(\underline{\overline{x}})$. Then $\underline{d} \in D(\underline{\overline{x}})$ and hence $\mathcal{D}(\underline{\overline{x}}) \subseteq D(\underline{\overline{x}})$.
Finally $\overline{\mathcal{D}}(\underline{\overline{x}}) \subseteq D(\underline{\overline{x}})$ since $D(\underline{\overline{x}})$ is closed (_it is the intersection of a finite number of closed half spaces_) (_remember the definition/properties of the closure_).

> **Important remark**: not all $\underline{d} \in D(\underline{\overline{x}})$ are feasible directions.

- **Theorem** (**Extension of first order necessary optimality conditions**): if $f \in \mathcal{C}^1$ on $S$ and $\underline{\overline{x}} \in S$ is a local minimum of $f$ on $S$, then
$$
\nabla f^T(\underline{\overline{x}}) \underline{d} \geq 0 \ \forall \underline{d} \in \overline{\mathcal{D}}(\underline{\overline{x}}),
$$
> that is, all feasible directions are ascent directions.

> **Proof**: the result holds $\forall \underline{d} \in \mathcal{D}(\underline{\overline{x}})$ (_we already proved it_). For every $\underline{d} \in \overline{\mathcal{D}}(\underline{\overline{x}})$ $\exists$ a sequence $\{ \underline{d}^k \}_{k \in \mathbb{N}} \subseteq \mathcal{D}(\underline{\overline{x}})$ such that $\lim_{k \rightarrow +\infty} \underline{d}^k = \underline{d}$ (_the closure is a closed set_). Since $\nabla f^T(\underline{\overline{x}}) \underline{d}^k \geq 0 \ \forall k$ (_since the result holds in $\mathcal{D}(\underline{\overline{x}})$_), then $\lim_{k \rightarrow + \infty} \nabla f^T(\underline{\overline{x}}) \underline{d}^k = \nabla f^T(\underline{\overline{d}}) \underline{d} \geq 0$ (_limits preserve inequalities_).

Unfortunately $\overline{\mathcal{D}}(\underline{\overline{x}})$ is difficult to characterize. Conversely, $D(\underline{\overline{x}})$ is well characterized.

- The **Constraint Qualification** (**CQ**) assumption holds at $\underline{\overline{x}}$ if $\overline{\mathcal{D}}(\underline{\overline{x}}) = D(\underline{\overline{x}})$.

- **Theorem** (**Karush-Kuhn-Tucker necessary local optimality conditions**): suppose $f, g_i \in \mathcal{C}^1$ and CQ assumption holds at $\underline{\overline{x}} \in \{ \underline{x} \in \mathbb{R}^n \ | \ g_i(\underline{x}) \leq 0 \ \forall i \in I \}$.
If $\underline{\overline{x}}$ is a local minimum of $f$ over $S$, then $\exists u_1, \ldots, u_m \geq 0$ (_remember that $m = |I|$_) known as **KKT multipliers** such that:
$$
\nabla f(\underline{\overline{x}}) + \sum_{i \in I(\underline{\overline{x}})} u_i \nabla g_i(\underline{\overline{x}}) = \underline{0} \equiv \begin{cases}
\nabla f(\underline{\overline{x}}) + \sum_{i=1}^m u_i \nabla g_i(\underline{\overline{x}}) = \underline{0} \\
u_i g_i(\underline{\overline{x}}) = 0 \ \forall i \in I = \{ 1, \ldots, m \}
\end{cases}.
$$
> (_If the constraint is not active, $u_i g_i(\underline{\overline{x}}) = 0$ implies $u_i = 0$_). $\underline{\overline{x}}$ must also satisfy the constraints $g_i(\underline{x}) \leq 0 \ \forall i \in I$.

> **Interpretation**: for $\underline{\overline{x}}$ to be a local minimum, then $-\nabla f(\underline{x})$ must be expressible as a linear combination with $\mu_i \geq 0$ of $\nabla g_i(\underline{\overline{x}}) \ \forall i \in I(\underline{\overline{x}})$, i.e. it must form an obtuse angle with all the feasible directions.

> **Proof**: assuming CQ holds at $\underline{\overline{x}}$, we have $\overline{\mathcal{D}}(\underline{\overline{x}}) = D(\underline{\overline{x}})$.
NC for $\underline{\overline{x}}$ to be a local minimum of $f$ over $S$ is
$$
\nabla f^T(\underline{\overline{x}}) \underline{d} \geq 0 \ \forall \underline{d} \text{ s.t. } \nabla g_i^T(\underline{\overline{x}}) \underline{d} \leq 0 \ \forall i \in I(\underline{\overline{x}}).
$$
> We're going to apply a variant of Farkas lemma, in particular we will change how the "second alternative" is expressed:
$$
\not \exists \underline{y} (\underline{y}^T A \leq \underline{0}^T \land \underline{y}^T \underline{b} > 0) \equiv \forall \underline{y}(\lnot(\underline{y}^T A \leq \underline{0}^T) \lor \underline{y}^T \underline{b} \leq 0) \equiv
$$

---

$$
\equiv \forall \underline{y} (\underline{y}^T A \leq \underline{0}^T \implies \underline{y}^T \underline{b} \leq 0) \equiv \forall \underline{d} (\underline{d}^T A \geq \underline{0}^T \implies \underline{d}^T \underline{b} \geq 0).
$$
> Hence the Farkas lemma can be written as:
$$
\begin{cases}
A \underline{u} = \underline{b} \\
\underline{u} \geq \underline{0}
\end{cases} \text{ has a solution } \iff \forall \underline{d} (\underline{d}^T A \geq \underline{0}^T \implies \underline{d}^T \underline{b} \geq 0).
$$
> Taking $\underline{b} = \nabla f(\underline{\overline{x}})$ and $A = \begin{bmatrix}-\nabla g_{i_1}(\underline{\overline{x}}) & \cdots & -\nabla g_{i_{|I(\underline{\overline{x}})|}}(\underline{\overline{x}}) \end{bmatrix}$ where $\{ i_1, \ldots, i_{|I(\underline{\overline{x}})|} \} = I(\underline{\overline{x}})$.
Because of the NC for $\underline{\overline{x}}$ to be local minimum, the second alternative of Farkas lemma is satisfied. Hence, by the first alternative:
$$
\exists \underline{u} \in \mathbb{R}^{|I(\underline{\overline{x}})|}, \underline{u} \geq \underline{0} \text{ s.t. } A \underline{u} = \underline{b}.
$$
> That is:
$$
\nabla f(\underline{\overline{x}}) = \sum_{i \in I(\underline{\overline{x}})} (- u_i \nabla g_i(\underline{\overline{x}})).
$$
> Finally, we need to take $u_i = 0$ for all $i \in I \setminus I(\underline{\overline{x}})$.

> **Important remark**: if CQ assumption does not hold at $\underline{\overline{x}}$, KKT conditions need not be necessary for local optimality. (_Indeed there are some examples where CQ does not hold and an optimum does not satisfy KKT_).

- **Theorem** (**Sufficient conditions for Constraint Qualification**):
> 1. if
>> - all $g_i$ are linear functions (_Karlin_);

>> or

>> - all $g_i$ are convex and $\exists \underline{a}$ s.t. $g_i(\underline{a}) < 0 \ \forall i \in I$ (_Slater_)

>> CQ assumption holds at <u>every</u> $\underline{x} \in S$.

> 2. If $\nabla g_i(\underline{\overline{x}})$, $i \in I(\underline{\overline{x}})$ are linearly independent, CQ assumption holds at $\underline{\overline{x}} \in S$.

> **Important remark**: when the gradients of the active constraints are linearly independent, KKT multiplier vector is unique (_otherwise the active constraints gradients would not be linear independent_).

> **Theorem** (**Necessary and sufficient global optimality conditions for convex problems**): if $f \in \mathcal{C}^1 \ \forall i \in I$ are convex, and $\exists \underline{a}$ such that $g_i(\underline{a}) < 0 \ \forall i \in I$, then $\underline{x}^* \in S$ is a <u>global minimum</u> iff $\exists u_1, \ldots, u_m \geq 0$ s.t.
$$
\begin{cases}
\nabla f(\underline{x}^*) + \sum_{i=1}^m u_i \nabla g_i(\underline{x}^*) = \underline{0} \\
u_i g_i(\underline{x}^*) = 0 \ \forall i \in I
\end{cases}.
$$

---

> **Proof**: ($\implies$) Suppose that $\underline{x}^*$ is a (global) minimum. Then, by Slater, CQ holds at $\underline{x}^*$, hence $\underline{x}^*$ satisfies the KKT.

> ($\impliedby$) Suppose that the KKT conditions holds. Because of the Farkas lemma it must be $\forall \underline{d} (\underline{d}^T A \geq \underline{0}^T \implies \underline{d}^T \underline{b} \geq 0)$ where $\underline{b} = \nabla f(\underline{x}^*)$ and $A = \begin{bmatrix} -\nabla g_1(\underline{\overline{x}}) & \cdots & \nabla g_{|I(\underline{\overline{x}})|}(\underline{\overline{x}}) \end{bmatrix}$. Observe that, since CQ holds at $\underline{x}^*$, the set of $\{ \underline{d} \in \mathbb{R}^n \ | \underline{d}^T A \geq \underline{0}^T \} = D(\underline{x}^*) = \mathcal{\overline{D}}(\underline{\overline{x}})$. Then we're exactly in the NS 1st order condition for convex problems ($\{ \underline{y} - \underline{x}^* \ | \ \underline{y} \in C \} \subseteq \mathcal{D}(\underline{x}) \subseteq \overline{\mathcal{D}}(\underline{x})$).

> **Remark**: for linear programs, it amounts to the complementary slackness theorem.

> **Remark**: the result holds under milder convexity conditions ($f$ pseudo-convex and the $g_i$s quasi-convex).

Let's extend the treatment to the case in which we also have equality constraints.
Consider
$$
\begin{matrix}
\min f(\underline{x}) \\
\text{s.t. } g_i(\underline{x}) \leq 0 \ \forall i \in I = \{ 1, \ldots, m \} \\
h_l(\underline{x}) = 0 \ \forall i \in L = \{ 1, \ldots, p \} \\
\underline{x} \in X \subseteq \mathbb{R}^n
\end{matrix}
$$
where $f, g_i, h_i \in \mathcal{C}^1$.

The issue with the previous approach is that, when we have nonlinear equality constraints, usually $\mathcal{D}(\underline{x}) = \{ \underline{0} \}$. Hence the CQ assumption is almost never satisfied.

- We define the **closed cone of the tangents at $\underline{\overline{x}}$**
$$
\mathcal{T}(\underline{\overline{x}}) = \left\{ \underline{d} \in \mathbb{R}^n \ | \ \underline{d} = \lambda \lim_{k \rightarrow +\infty} \frac{\underline{x}^k - \underline{\overline{x}}}{||\underline{x}^k - \underline{\overline{x}}||}, \lambda \geq 0, \underline{x}^k \in S \rightarrow \underline{\overline{x}} \text{ with } \underline{x}^k \neq \underline{\overline{x}} \text{ s.t. the previous lim is defined} \right\}.
$$

> **Important remark**: we can generalize first order necessary optimality conditions to $\mathcal{T}(\underline{\overline{x}})$ as we did for $\overline{\mathcal{D}}(\underline{\overline{x}})$ [_see Noecedal-Wright, p. 325, Theorem 12.3_].

- The CQ assumption holds at $\underline{\overline{x}} \in S$ if $\mathcal{T}(\underline{\overline{x}}) = D(\underline{\overline{x}}) \cap H(\underline{\overline{x}})$ where
$$
D(\underline{\overline{x}}) = \{ \underline{d} \in \mathbb{R}^n \ | \ \nabla g_i^T(\underline{\overline{x}}) \underline{d} \leq 0 \ \forall i \in I(\underline{\overline{x}}) \},
$$
$$
H(\underline{\overline{x}}) = \{ \underline{d} \in \mathbb{R}^n \ | \ \nabla h_i^T(\underline{\overline{x}}) \underline{d} = 0 \ \forall l \in L \} \text{ (equality const. are always active)}.
$$

> **Remark**: the definition of $H(\underline{\overline{x}})$ makes sense: we can represent an equality constraint with two inequality constraints in opposite direction.

---

- **Theorem** (**General KKT necessary optimality conditions**): suppose $f \in \mathcal{C}^1, g_i \in \mathcal{C}^1 \ \forall i, h_l \in \mathcal{C}^1 \ \forall l$ and CQ assumption holds at $\underline{\overline{x}} \in S$. If $\underline{\overline{x}}$ is a local minimum of $f$ over $S$ then $\exists u_i \geq 0 \ \forall i \in I(\underline{\overline{x}})$ and $v_l \in \mathbb{R} \ \forall l \in L$ such that
$$
\nabla f(\underline{\overline{x}}) + \sum_{i \in I(\underline{\overline{x}})} u_i \nabla g_i(\underline{\overline{x}}) + \sum_{l \in L} v_l \nabla h_l(\underline{\overline{x}}) = 0.
$$

> [_The proof of the result requires a slightly generalized version of Farkas lemma, see Noecedal-Wright, p. 327, Lemma 12.4_].

> **Remark**: if we have only equality constraints, KKT conditions coincide with classical Lagrange optimality conditions.

- **Theorem** (**Sufficient conditions for CQ**)
> - If $g_i$ convex, $h_l$ linear and $\exits \underline{a} \in X$ s.t. $g_i(\underline{a}) < 0 \ \forall i \in I$ and $h_l(\underline{a}) = 0 \ \forall l \in L$, then CQ assumption holds at every $\underline{x} \in S$.

> - If $\nabla g_i(\underline{\overline{x}}) \ \forall i \in I(\underline{\overline{x}})$ and $\nabla h_l(\underline{\overline{x}}) \ \forall l \in L$ are linearly independent then CQ assumption holds at $\underline{\overline{x}} \in S$.
