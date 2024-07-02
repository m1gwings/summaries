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
> - If $g_i$ convex, $h_l$ linear and $\exists \underline{a} \in X$ s.t. $g_i(\underline{a}) < 0 \ \forall i \in I$ and $h_l(\underline{a}) = 0 \ \forall l \in L$, then CQ assumption holds at every $\underline{x} \in S$.

> - If $\nabla g_i(\underline{\overline{x}}) \ \forall i \in I(\underline{\overline{x}})$ and $\nabla h_l(\underline{\overline{x}}) \ \forall l \in L$ are linearly independent then CQ assumption holds at $\underline{\overline{x}} \in S$.

## Sufficient optimality conditions

Let's consider the generic NLP
$$
\text{(P) } \begin{cases}
\min f(\underline{x}) \\
\text{s.t. } g_i(\underline{x}) \leq 0 \ \forall i \in I = \{ 1, \ldots, m \} \\
\underline{x} \in X \subseteq \mathbb{R}^n
\end{cases}
$$
where $X$ is an arbitrary subset (<u>even discrete</u>).

- The **Lagrange function** associated with (P) is
$$
L(\underline{x}, \underline{u}) = f(\underline{x}) + \sum_{i \in I} u_i g_i(\underline{x}) \ \forall \underline{x} \in X \text{ and } \underline{u} \geq \underline{0}.
$$

> **Remark**: $\underline{u} \geq \underline{0}$ since $g_i(\underline{x}) \leq 0$.

- $(\underline{\overline{x}}, \underline{\overline{u}})$ with $\underline{\overline{x}} \in X$ and $\underline{\overline{u}} \geq \underline{0}$ is a **saddle point** of $L(\underline{x}, \underline{u})$ if $L(\underline{\overline{x}}, \underline{\overline{u}}) \leq L(\underline{x}, \underline{\overline{u}}) \ \forall \underline{x} \in X$ and $L(\underline{\overline{x}}, \underline{u}) \leq L(\underline{\overline{x}}, \underline{\overline{u}}) \ \forall \underline{u} \geq \underline{0}$.
That is, $\underline{\overline{x}}$ minimizes $L(\underline{x}, \underline{\overline{u}})$ over $X$ and $\underline{\overline{u}}$ maximizes $L(\underline{\overline{x}}, \underline{u})$ over $\{ \underline{u} \in \mathbb{R}^m \ | \ \underline{u} \geq \underline{0} \}$.

- **Theorem** (**Characterization of saddle points**): $(\underline{\overline{x}}, \underline{\overline{u}})$ with $\underline{\overline{x}} \in X$ and $\underline{\overline{u}} \geq \underline{0}$ is a saddle point of $L(\underline{\overline{x}}, \underline{\overline{u}})$ iff
>> i. $L(\underline{\overline{x}}, \underline{\overline{u}}) = \min_{\underline{x} \in X} L(\underline{x}, \underline{\overline{u}})$;

---

>> ii. $g_i(\underline{\overline{x}}) \leq 0 \ \forall i \in I$;
>> iii. $\overline{u}_i g_i(\underline{\overline{x}}) = 0 \ \forall i \in I$.

> **Proof**: [_taken from Bazaraa's book, p. 265_]
($\implies$) Suppose that $(\underline{\overline{x}}, \underline{\overline{u}})$ is a saddle point of $L(\underline{x}, \underline{u})$. Then i is satisfied by definition of saddle point. Furthermore:
$$
f(\underline{\overline{x}}) + \underline{\overline{u}}^T \underline{g}(\underline{\overline{x}}) \geq f(\underline{\overline{x}}) + \underline{u}^T \underline{g}(\underline{\overline{u}}) \text{ for all } \underline{u} \geq \underline{0}.
$$
> It follows that $(\underline{u} - \underline{\overline{u}})^T \underline{g}(\underline{\overline{x}}) \leq 0$. Let $\underline{u} = \underline{\overline{u}} + \underline{e}_i \geq \underline{0}$. Then $g_i(\underline{\overline{x}}) = \underline{e}_i^T \underline{g}(\underline{\overline{x}}) \leq 0$, that is, ii holds.
If instead we put $\underline{u} = \underline{0}$ in the previous expression, we get:
$$
\underline{\overline{u}}^T \underline{g} (\underline{\overline{x}}) \geq 0.
$$
> Since $\underline{\overline{u}} \geq \underline{0}$ and $\underline{g}(\underline{\overline{x}}) \leq \underline{0}$, it must be $\overline{u}_i g_i(\underline{\overline{x}}) = 0$. And so, also iii holds.

> ($\impliedby$) Suppose now that i, ii, and iii hold.
Then, by i, $L(\underline{\overline{x}}, \underline{\overline{u}}) \leq L(\underline{x}, \underline{\overline{u}})$ for all $\underline{x} \in X$.
Furthermore:
$$
L(\underline{\overline{x}}, \underline{\overline{u}}) = f(\underline{\overline{x}}) + \underline{\overline{u}}^T \underline{g}(\underline{\overline{x}}) \stackrel{\text{iii}}{=} f(\underline{\overline{x}}) \stackrel{\text{ii}}{\geq} f(\underline{\overline{x}}) + \underline{u}^T \underline{g}(\underline{\overline{x}}) = L(\underline{\overline{x}}, \underline{u})
$$
> for all $\underline{u} \geq \underline{0}$. Then $(\underline{\overline{x}}, \underline{\overline{u}})$ is a saddle point.

- **Theorem** (**Sufficient global optimality condition**): if $(\underline{\overline{x}}, \underline{\overline{u}})$ is a saddle point of $L(\underline{x}, \underline{u})$, then $\underline{\overline{x}}$ is a <u>global minimum</u> of problem (P).

> **Proof**: let $\underline{x} \in X$ s.t. $\underline{g}(\underline{\overline{x}}) \leq \underline{0}$ ($\underline{x}$ is feasible). Then:
$$
f(\underline{\overline{x}}) \stackrel{\text{iii}}{=} f(\underline{\overline{x}}) + \underline{\overline{u}}^T \underline{g}(\underline{\overline{x}}) \stackrel{\text{i}}{\leq} f(\underline{x}) + \underline{\overline{u}}^T \underline{g}(\underline{x}) \leq f(\underline{x}).
$$
> That is, $\underline{\overline{x}}$ is a global minimum.

> **Remarks**:
> - The result applies to <u>any mathematical program</u> (convex or not, with $f$ and $g_i$ differentiable or not, $X$ continuous or discrete, $\ldots$).
> - For some problems a saddle point may not exist, in general for non-convex problems.

- **Theorem** (**Saddle point for convex problems**): suppose $f$ and $g_i$ $\forall i \in I$ are convex, $X \subseteq \mathbb{R}^n$ is convex and $\exists \underline{a} \in X$ s.t. $\underline{g}(\underline{a}) \leq \underline{0}$. If (P) has an optimal solution $\underline{\overline{x}}$, $\exists \underline{\overline{u}} \geq \underline{0}$ s.t. $(\underline{\overline{x}}, \underline{\overline{u}})$ is a saddle point of $L(\underline{x}, \underline{u})$.

---

- **Connection with KKT conditions for convex problems**: if $f$ and $g_i \in \mathcal{C}^1$ are convex, $X = \mathbb{R}^n$ and $\exists \underline{a} \in X$ s.t. $\underline{g}(\underline{a}) \leq \underline{0}$, then $\underline{\overline{x}}$ is an optimal solution iff $\underline{\overline{x}}$ satisfies the KKT conditions.

> **Proof**: $\underline{\overline{x}}$ is an optimal solution $\iff$ $\exists \underline{u} \geq \underline{0}$ s.t. $(\underline{\overline{x}}, \underline{\overline{u}})$ is a saddle point of $L(\underline{x}, \underline{u})$ (_because of SC for global optimality and the previous theorem_).
Observe that $L(\underline{x}, \underline{u}) = f(\underline{x}) + \underline{\overline{u}}^T \underline{g}(\underline{x})$ for fixed $\underline{\overline{u}} \geq \underline{0}$ is a conic combination of convex functions, hence it is convex.
Because of i and the NS optimality condition for convex problems:
$$
\nabla_{\underline{x}} L(\underline{\overline{x}}, \underline{\overline{u}}) = \underline{0} \text{ iff } \nabla f(\underline{\overline{x}}) + \left[\frac{\partial \underline{g}}{\partial \underline{x}}(\underline{\overline{x}})\right]^T \underline{u} = \underline{0}.
$$
> By adding ii and iii we have the KKT conditions.
Furthermore the CQ assumption holds for every feasible $\underline{x}$. The result follows by taking the chain of equivalences first in a direction and then in the other.

**Remarks**:
> - Without convexity assumption a stationary point $\underline{\overline{x}}$ may not minimize $L(\underline{x}, \underline{\overline{u}})$.
> - KKT multipliers are then identical to Lagrange multipliers at the saddle point.

## Lagrangian duality

Consider again the generic NLP of the previous chapter:
$$
\text{(P) } \begin{cases}
\min f(\underline{x}) \\
\text{s.t. } g_i(\underline{x}) \leq 0 \ \forall i \in I = \{ 1, \ldots, m \} \\
\underline{x} \in X \subseteq \mathbb{R}^n
\end{cases}.
$$
To any minimization NLP we can associate a maximization NLP such that, under some assumptions, the objective function values of respective optimal solutions coincide.

We can:
- tackle the <u>primal</u> problem (P) indirectly, by solving the <u>dual</u> problem;
- try to solve (P), we can look for a saddle point of the Lagrange function.

- We define **dual function**
$$
w(\underline{u}) = \min_{\underline{x} \in X} L(\underline{x}, \underline{u}) \ \forall \underline{u} \geq \underline{0}.
$$
> It is well-defined, if, for instance, $f$ and the $g_i$s are continuous and $X$ is compact (_in virtue of Weierstrass theorem_).

---

- We define the **dual problem** (_of searching a saddle point_)
$$
\text{(D) } \begin{cases}
\max w(\underline{u}) \\
\underline{u} \geq \underline{0}
\end{cases}.
$$

> **Remark**: $w(\underline{u})$ and (D) are defined even if no saddle point exists.

> **Remarks**:
> - There can be different Lagrangian duals of (P) depending on which $g_i(\underline{x}) \leq 0$ are dualized. The choice affects the optimal value of (D) and the complexity to evaluate $w(\underline{u})$.

> - Lagrangian dual is useful to solve large-scale LPs and (non)convex/discrete optimization problems.

- **Theorem** (**Weak duality**): for every feasible $\underline{x}$ of (P) and $\underline{u} \geq \underline{0}$ of (D), we have $w(\underline{u}) \leq f(\underline{x})$.

> **Proof**:
$$
w(\underline{u}) \leq \min_{\underline{\tilde{x}} \in X} L(\underline{\tilde{x}}, \underline{u}) \leq L(\underline{x}, \underline{u}) = f(\underline{x}) + \underline{u}^T \underline{g}(\underline{x}) \leq f(\underline{x}).
$$

- **Corollary**: in particular, fore every $\underline{u} \geq \underline{0}$ we have $w(\underline{u}) \leq f(\underline{x}^*)$ for an optimal $\underline{x}^*$ of (P).

- **Corollary**: if a feasible solution $\underline{\overline{x}}$ of (P) and $\underline{\overline{u}} \geq \underline{0}$ satisfy $w(\underline{\overline{u}}) = f(\underline{\overline{x}})$, $\underline{\overline{x}}$ is optimal for (P) and $\underline{\overline{u}}$ is optimal for (D).

- **Remark**: for LP the objective function values of optimal solutions of (P) and (D) coincide, for NLPs this is not always the case.

- **Theorem** (**Strong duality**):
>> i. If (P) has a saddle point $(\underline{\overline{x}}, \underline{\overline{u}})$, then
$$
\begin{cases}
\max w(\underline{u}) \\
\underline{u} \geq \underline{0}
\end{cases} = w(\underline{\overline{u}}) = f(\underline{\overline{x}}) = \min \{ f(\underline{x}) \ | \ \underline{g}(\underline{x}) \leq \underline{0}, \underline{x} \in X \}.
$$

>> ii. If $\exists$ a feasible $\underline{\overline{x}}$ of (P) and $\underline{\overline{u}} \geq \underline{0}$ such that $w(\underline{\overline{u}}) = f(\underline{\overline{x}})$, then $(\underline{\overline{x}}, \underline{\overline{u}})$ is a saddle point of $L(\underline{x}, \underline{u})$.

> **Proof**: 
>> i. Since $(\underline{\overline{x}}, \underline{\overline{u}})$ is a saddle point:
$$
w(\underline{\overline{u}}) = \min_{\underline{x} \in X} L(\underline{x}, \underline{\overline{u}}) \stackrel{\text{i of saddle points}}{=} L(\underline{\overline{x}}, \underline{\overline{u}}) = f(\underline{\overline{x}}) + \underline{\overline{u}}^T \underline{g}(\underline{\overline{x}}) \stackrel{\text{ii of saddle points}}{=} f(\underline{\overline{x}}).
$$

---

>> Then $\underline{\overline{x}}$ and $\underline{\overline{u}}$ are optimal for (P) and (D) respectively because of weak duality as we wanted to prove.

>> ii. Let $\underline{\overline{x}}$ be a feasible solution of (P) and $\underline{\overline{u}} \geq \underline{0}$ s.t. $w(\underline{\overline{u}}) = f(\underline{\overline{x}})$. Because of weak duality $\underline{\overline{x}}$ and $\underline{\overline{u}}$ are optimal for (P) and (D) respectively.
>> - $f(\underline{\overline{x}}) = w(\underline{\overline{u}}) = \min_{\underline{x} \in X} L(\underline{x}, \underline{\overline{u}}) \leq L(\underline{\overline{x}}, \underline{\overline{u}}) = f(\underline{\overline{x}}) + \underline{\overline{u}}^T \underline{g}(\underline{\overline{x}})$ iff $\underline{\overline{u}}^T \underline{g}(\underline{\overline{x}}) \geq 0$. Then, since $\underline{\overline{u}} \geq \underline{0}$ and $\underline{g}(\underline{\overline{x}}) \leq \underline{0}$, it must be $\overline{u}_i g_i(\underline{\overline{x}}) = 0 \ \forall i \in I$ (characterization iii of saddle points).

>> - $L(\underline{\overline{x}}, \underline{\overline{u}}) = f(\underline{\overline{x}}) + \underline{\overline{u}}^T \underline{g}(\underline{\overline{x}}) = f(\underline{\overline{x}}) = w(\underline{\overline{u}}) = \min_{\underline{x} \in X} L(\underline{x}, \underline{\overline{u}})$ (characterization i of saddle points).

>> - $\underline{g}(\underline{\overline{x}}) \leq \underline{0}$ since $\underline{\overline{x}}$ is feasible for (P) (characterization ii of saddle points).

>> Then $(\underline{\overline{x}}, \underline{\overline{u}})$ is a saddle point.

- **Consequence**: if $f$, $g_i$s and $X \subseteq \mathbb{R}^n$ are convex, $\exists \underline{a}$ s.t. $\underline{g}(\underline{a}) < \underline{0}$ and (P) has a finite optimal solution, $\exists$ a saddle point (_we stated the theorem_) $(\underline{\overline{x}}, \underline{\overline{u}})$ and i (_of the previous theorem_) holds:
$$
\begin{cases}
\max w(\underline{u}) \\
\underline{u} \geq \underline{0}
\end{cases} = \min \{ f(\underline{x}) \ | \ \underline{g}(\underline{x}) \leq \underline{0}, \underline{x} \in X \}.
$$

> **Remark**: in general, we can have a <u>duality gap</u>.

- **Theorem**: the dual function $w(\underline{u})$ is <u>concave</u>.

> **Proof**: let $\alpha \in [ 0, 1 ]$, $\underline{u}_1, \underline{u}_2 \geq \underline{0}$. Then:
$$
w(\alpha \underline{u}_1 + (1-\alpha) \underline{u}_2) = \min_{\underline{x} \in X} L(\underline{x}, \alpha \underline{u}_1 + (1-\alpha) \underline{u}_2) =
$$
$$
= \min_{\underline{x} \in X} \left( f(\underline{x}) + \alpha \underline{u}_1^T \underline{g}(\underline{x}) + (1-\alpha) \underline{u}_2^T \underline{g}(\underline{x}) \right) =
$$
$$
= \min_{\underline{x} \in X} \left[ \alpha (f(\underline{x}) + \underline{u}_1^T \underline{g}(\underline{x})) + (1-\alpha) (f(\underline{x}) + \underline{u}_2^T \underline{g}(\underline{x})) \right] \geq
$$
$$
\geq \alpha \min_{\underline{x} \in X} \left( f(\underline{x}) + \underline{u}_1^T \underline{g}(\underline{x}) \right) + (1-\alpha) \min_{\underline{x} \in X} \left( f(\underline{x}) + \underline{u}_2^T \underline{g}(\underline{x}) \right) =
$$
$$
= \alpha w(\underline{u}_1) + (1-\alpha) w(\underline{u}_2).
$$

> **Observations**:
> - If $X \subseteq \mathbb{Z}^n$, $w(\underline{u})$ is <u>not everywhere continuously differentiable</u>.

---

>>  It is a concave piecewise linear function, the lower envelope of a (in)finite family of hyperplanes in $\mathbb{R}^{n+1}$.

> - In general (D) is easier than (P).

> - Since $w(\underline{u})$ is concave, local optima are global optima but we need an ad hoc solution method: **subgradient method**.


> **Property 2**: for $\underline{\tilde{u}} \in \mathbb{R}^m_+$ let $X(\underline{\tilde{u}}) = \{ \underline{x} \in X \ | \ f(\underline{x}) + \underline{\tilde{u}}^T \underline{g}(\underline{x}) = w(\underline{\tilde{u}}) \}$ then $\underline{g}(\underline{x})$ is a subgradient of $w(\underline{u})$ at $\underline{\tilde{u}}$ for each $\underline{x} \in X(\underline{\tilde{u}})$.

> **Remark**: if we derived an expression of $w(\underline{u})$ analytically, usually we have an expression for at least a point in $X(\underline{\tilde{u}})$.

> **Proof**: let $\underline{\tilde{x}} \in X(\underline{\tilde{u}})$. Then:
$$
w(\underline{u}) = \min_{\underline{x} \in X} L(\underline{x}, \underline{u}) = \min_{\underline{x} \in X} (f(\underline{x}) + \underline{u}^T \underline{g}(\underline{x})) \leq
$$
$$
\leq f(\underline{\tilde{x}}) + \underline{u}^T \underline{g}(\underline{\tilde{x}}) = f(\underline{\tilde{x}}) + \underline{\tilde{u}}^T \underline{g}(\underline{\tilde{x}}) + (\underline{u} - \underline{\tilde{u}})^T \underline{g}(\underline{\tilde{x}}) =
$$
$$
= w(\underline{\tilde{u}}) + (\underline{u} - \underline{\tilde{u}})^T \underline{g} (\underline{\tilde{x}})
$$
> as we wanted to prove. (_Since $w$ is concave the inequality which defines the subgradient takes the opposite direction_).

> **Remark**:
> - Every subgradient at $w$ at $\underline{\tilde{u}}$ can be expressed as a convex combination of the subgradients $\underline{g}(\underline{x})$ with $\underline{x} \in X(\underline{\tilde{u}})$.

> - If $w$ is continuously differentiable at $\underline{\tilde{u}}$, $X(\underline{\tilde{u}})$ contains a single element $\underline{\tilde{x}}$ and $\underline{g}(\underline{\tilde{x}})$ is the gradient of $w(\underline{u})$ at $\underline{\tilde{u}}$.

> **Final remarks**:
> - if a saddle point exists: we can solve (D) and derive optimal $\underline{x}^*$ of (P) by minimizing $L(\underline{x}, \underline{u}^*)$ over $X$, ensuring $q_i(\underline{x}^*) \leq 0$ and $u_i^* g_i(\underline{x}^*) = 0 \ \forall i \in I$.
> - if no saddle point exists: optimal $\underline{u}^*$ of (D) gives a lower bound $w(\underline{u}^*)$ for $f(\underline{x}^*)$. Find $\underline{u}^* \geq \underline{0}$ maximizing $w(\underline{u})$ by using the <u>subgradient method</u> that generates $\underline{u}^k \rightarrow \underline{u}^*$ when $k \rightarrow +\infty$.
For each $\underline{u}^k$, we have a lower bound $w(\underline{u}^k)$ for $f(\underline{x}^*)$ and we determine $\underline{x}^k$ that minimizes $L(\underline{x}, \underline{u}^k)$ over $X$.

---

### Subgradient method

The **subgradient method** is a technique which allows to optimize not-everywhere differentiable convex/concave functions.
Because of the previous results, we can use it to solve the dual problem (D).

In particular, consider the problem $\min_{\underline{x} \in \mathbb{R}^n} f(\underline{x})$ with $f$ convex.
The method works as follows:

We start from an arbitrary $\underline{x}_0$.
At $k$-th iteration: consider $\underline{\gamma}_k \in \partial f(\underline{x}_k)$ and set
$$
\underline{x}_{k+1} = \underline{x}_k - \alpha_k \underline{\gamma}_k
$$
with $\alpha_k > 0$.

**Remark**: we should not do 1-D search because for non-differentiable functions a subgradient $\underline{\gamma} \in \partial f(\underline{x})$ is not necessarily a descent direction!

The following result holds.

- **Theorem**: if $f$ is convex, $\lim_{||\underline{x}|| \rightarrow +\infty} f(\underline{x}) = +\infty$, $\lim_{k \rightarrow +\infty} \alpha_k = 0$ and $\sum_{k=0}^{\infty} \alpha_k = \infty$, the subgradient method terminates after a finite number of iterations with an optimal solution $\underline{x}^*$ or the infinite sequence $\{ \underline{x}_k \}$ admits a sequence converging to $\underline{x}^*$.

> **Remark on step-size**: in practice $\{ \alpha_k \}$ as above (e.g. $\alpha_k = \frac{1}{k}$) are too slow. An option is $\alpha_k = \alpha_0 \rho^k$ for a given $\rho < 1$. A more popular one (for min problems) is:
$$
\alpha_k = \epsilon_k \frac{f(\underline{x}_k) - \tilde{f}}{||\underline{\gamma}_k||^2}
$$
> where $0 < \epsilon_k < 2$ and $\hat{f}$ is either the optimal value $f(\underline{x}^*)$ or an estimate.

> **Remark on stopping criterion**: the usual stopping criterion is having a prescribed maximum number of iterations (even if $\underline{0} \in \partial f(\underline{x}_k)$, it may not be considered at $\underline{x}_k$).

> **Remark**: we need to store the best solution $\underline{x}_k$ found.

---

## Second order optimality conditions

Consider the generic nonlinear program:
$$
\text{(P) }

\begin{matrix}
\min f(\underline{x}) \\
\text{s.t. } g_i(\underline{x}) \leq 0 \ \forall i \in I = \{ 1, \ldots, m \} \\
h_l(\underline{x}) = 0 \ \forall l \in L = \{ 1, \ldots, k \} \\
\underline{x} \in X \subseteq \mathbb{R}^n
\end{matrix}
$$
with $f$, $g_i$s and $h_i$s of class $\mathcal{C}^2$ and $X$ an open subset of $\mathbb{R}^n$.

The Lagrange function is:
$$
L(\underline{x}, \underline{u}, \underline{v}) = f(\underline{x}) + \sum_{i=1}^m u_i g_i(\underline{x}) + \sum_{l=1}^k v_l h_l(\underline{x}) = f(\underline{x}) + \underline{u}^T \underline{g}(\underline{x}) + \underline{v}^T \underline{h}(\underline{x})
$$
with $\underline{u} \geq \underline{0}$ and $\underline{v} \in \mathbb{R}^k$.

The Hessian sub-matrix w.r.t. the variables $\underline{x}$ is:
$$
\nabla^2_{\underline{x} \underline{x}} L(\underline{x}, \underline{u}, \underline{v}) = \nabla^2_{\underline{x} \underline{x}} f(\underline{x}) + \sum_{i=1}^m u_i \nabla^2_{\underline{x} \underline{x}} g_i(\underline{x}) + \sum_{l=1}^k v_l \nabla^2_{\underline{x} \underline{x}}
 h_l(\underline{x}).
$$

- **Second order KKT necessary conditions**: if $\underline{\overline{x}}$ is a local minimum of (P) and $\nabla g_i(\underline{\overline{x}})$, with $i \in I(\underline{\overline{x}})$ and $\nabla h_l(\underline{\overline{x}})$ with $l \in L$ are linearly independent, then $\underline{\overline{x}}$ and some $(\underline{\overline{u}}, \underline{\overline{v}})$ satisfy the KKT conditions:
$$
\begin{matrix}
\nabla_{\underline{x}} L(\underline{x}, \underline{u}, \underline{v}) = \underline{0} \\
\underline{g}(\underline{x}) \leq \underline{0} \\
\underline{h}(\underline{x}) = \underline{0} \\
\underline{u}^T \underline{g}(\underline{x}) \geq 0 \\
\underline{u} \geq \underline{0}, \underline{v} \in \mathbb{R}^k.
\end{matrix}
$$
> Moreover, every $\underline{d} \in \mathbb{R}^n$ s.t.
$$
\nabla g_i^T(\underline{\overline{x}}) \underline{d} \leq 0 \ \forall i \in I(\underline{\overline{x}}) \\
\nabla h_l^T(\underline{\overline{x}}) \underline{d} = 0 \ \forall l \in L
$$
> must satisfy:
$$
\underline{d}^T \nabla^2_{\underline{x} \underline{x}} L(\underline{\overline{x}}, \underline{\overline{u}}, \underline{\overline{v}}) \underline{d} \geq 0. 
$$

---

- **Second order KKT sufficient conditions**: let $\underline{\overline{x}}$ satisfies with $(\underline{\overline{u}}, \underline{\overline{v}})$ the previous KKT conditions.
If
$$
\underline{d}^T \nabla_{\underline{x} \underline{x}}^2 L(\underline{\overline{x}}, \underline{\overline{u}}, \underline{\overline{v}}) \underline{d} > 0
$$
> for each $\underline{d} \neq \underline{0}$ s.t.
$$
\begin{matrix}
\nabla g_i^T(\underline{\overline{x}}) \underline{d} = 0 \ \forall i \in I^+ \\
\nabla g_i^T(\underline{\overline{x}}) \underline{d} \leq 0 \ \forall i \in I^0 \\
\nabla h_l^T(\underline{\overline{x}}) \underline{d} = 0 \ \forall l \in L
\end{matrix}
$$
> where $I^+ = \{ i \in I \ | \ u_i > 0 \}$ and $I^0 = \{ i \in I \ | \ u_i = 0 \}$,
then $\underline{\overline{x}}$ is a strict local minimum of (P).

## Quadratic programming

In **quadratic programming**, we want to optimize a quadratic function subject to linear constraints:
$$
\text{(P) }
\begin{matrix}
\min \frac{1}{2} \underline{x}^T Q \underline{x} + \underline{c}^T \underline{x} \\
\text{s.t. } \underline{a}_i^T \underline{x} \leq b_i \ \forall i \in I \\
\underline{a}_i^T \underline{x} = b_i \ \forall i \in E \\
\underline{x} \in \mathbb{R}^n
\end{matrix},
$$
> where $Q \in \mathbb{R}^{n \times n}$.

Without loss of generality we can assume $Q$ symmetric (if $\overline{Q}$ is not symmetric we have the same function if we substitute it with $\frac{1}{2} (\overline{Q} + \overline{Q}^T)$).

The difficulty depends on $Q$: if $Q$ is positive (semi)definite, (P) is convex, otherwise can have a large number of local optima.

QPs are the simplest NLP problems besides Linear Programs. Efficient QP algorithms are available.

### QP with only equality constraints

Consider
$$
\min \left\{ \frac{1}{2} \underline{x}^T Q \underline{x} + \underline{c}^T \underline{x} \ | \ A \underline{x} = \underline{b} \right\}
$$
where $A \in \mathbb{R}^{m \times n}$.

---

Since we have only linear equations, CQ assumption is satisfied at every feasible point and simple KKT conditions hold:
$$
\begin{matrix}
Q \underline{x} + \underline{c} + \sum_{i=1}^m u_i \underline{a}_i = \underline{0} \\
A \underline{x} = \underline{b}
\end{matrix}.
$$

> **Remark**: complementary slackness constraints are automatically satisfied (_we only have equalities_).

Observe that the KKT conditions in this case consist in a linear system:
$$
\begin{bmatrix}
Q & A^T \\
A & O
\end{bmatrix} \begin{bmatrix}
\underline{x} \\
\underline{u} \\
\end{bmatrix} = \begin{bmatrix}
- \underline{c} \\
\underline{b}
\end{bmatrix}.
$$

**Remark**: if $A$ is full rank and $Q$ is p.d. on subspace $\{ \underline{x} \in \mathbb{R}^n \ | \ A \underline{x} = \underline{0} \}$, the matrix is non-singular.

#### Null-space method

In the null-space method we determine $Z \in \mathbb{R}^{n \times (n-m)}$ whose columns span the null space $\{ \underline{x} \in \mathbb{R}^n \ | \ A \underline{x} = \underline{0} \}$ of $A$.
$Z$ can be computed by (sub)matrix factorization of $A$ (if $A$ is sparse, by LU factorization)
For example, assume that the first $m$ columns of $A$ are linearly independent, through Gaussian elimination we bring $A$ into $\begin{bmatrix} I_m & B \end{bmatrix}$. Then $A \underline{x} = \underline{0}$ iff $\underline{x}_1 = - B \underline{x}_2$ with $\underline{x} = \begin{bmatrix} \underline{x}_1^T & \underline{x}_2^T \end{bmatrix}^T$. Then
$$
\text{ker}(A) = \left\{ \begin{bmatrix} - B \underline{x}_2 \\ \underline{x}_2 \end{bmatrix} \ | \ \underline{x}_2 \in \mathbb{R}^{n-m} \right\} = \left\{ \begin{bmatrix} -B \\ I_{n-m} \end{bmatrix} \underline{x}_2 \ | \ \underline{x}_2 \in \mathbb{R}^{n-m} \right\}.
$$

Given any feasible $\underline{x}_0$, other feasible solution
$$
\underline{x} = \underline{x}_0 + Z \underline{w}
$$
for an appropriate $\underline{w} \in \mathbb{R}^{n-m}$.

The the original QP with only equality constraints is equivalent to an unconstrained problem:
$$
\min_{\underline{w} \in \mathbb{R}^{n-m}} \frac{1}{2} (\underline{x}_0 + Z \underline{w})^T Q (\underline{x}_0 + Z \underline{w}) + \underline{c}^T (\underline{x}_0 + Z \underline{w}) \equiv
$$
$$
\equiv \frac{1}{2} \underline{w}^T (Z^T Q Z) \underline{w} + (Q \underline{x}_0 + \underline{c})^T Z \underline{w}.
$$
If $Z^T Q Z$ is p.d., then $\exists !$ optimal $\underline{w}^*$ obtained by solving:
$$
(Z^T Q Z) \underline{z} = - Z^T (Q\underline{x}_0 + \underline{c}).
$$

---

### QP with equality and inequality constraints

#### Active-set method

The **active-set method** is a technique for solving generic QP problems (with both equalities and inequalities).

The idea is the following: we want to determine $I(\underline{x^*}) = \{  i \in I \ | \ \underline{a}_i^T \underline{x}^* = b_i \}$ where $\underline{x}^*$ is an optimal solution, by solving a sequence of QPs with only equality constraints.

We will focus on the version of the method for <u>convex problems</u>, which works as follows.

Initialization: find an initial feasible $\underline{x}_0$ (_we can use phase 1 of the Simplex method since the feasible region is the same as LPs_) and choose $W_0 \subseteq \{ i \in I \ | \ \underline{a}_i^T \underline{x}_0 = b_i \} \cup E$ of the active constraints at $\underline{x}_0$ with $E \subseteq W_0$.

Iteration $k$: given the current feasible $\underline{x}_k$, determine $\underline{d}_k$ by solving the subproblem
$$
\min \{ q(\underline{x}_k + \underline{d}) \ | \ \underline{a}_i^T (\underline{x}_k + \underline{d}) = b_i \ \forall i \in W_k \},
$$
where $W_k$ is the current _working set_, with $W_k \subseteq \{ i \in I \ | \ \underline{a}_i^T \underline{x}_k = b_i \} \cup E$.
The subproblem is equivalent to $\min \{ q(\underline{x}_k + \underline{d}) \ | \ \underline{a}_i^T \underline{d} = 0 \ \forall i \in W_k \}$ since $\underline{a}_i^T \underline{x}_k = b_i \ \forall i \in W_k$.

**Remark**: if $Z^T Q Z$ is p.d. (always true if $Q$ is p.d.), the subproblem has a unique solution $\underline{d}_k$ which we can find with the null-space method.

- If $\underline{d}_k \neq \underline{0}$, we determine the largest $\alpha$ satisfying all constraints not in $W_k$. Let $i \not \in W_k$ with $\underline{a}_i^T \underline{d}_k > 0$, then:
$$
\underline{a}_i^T (\underline{x}_k + \alpha_k \underline{d}_k) \leq b_i \text{ iff } \alpha_k \leq \frac{b_i - \underline{a}_i^T \underline{x}_k}{\underline{a}_i^T \underline{d}_k}.
$$
> Hence it must be: $\alpha_k = \min \{ 1, \min_{i \not \in W_k, \underline{a}_i^T \underline{d}_k > 0} \frac{b_i - \underline{a}_i^T \underline{x}_k}{\underline{a}_i^T \underline{d}_k} \}$ (_the $1$ accounts for the case in which $\underline{x} + \underline{d}_k$ is feasible_).
Now we can set $\underline{x}_{k+1} = \underline{x}_k + \alpha_k \underline{d}_k$.
Furthermore $W_{k+1} = W_k \cup \{ i' \}$ where $i'$ is the index of <u>one</u> of the constraints becoming active at $\underline{x}_{k+1}$. (_It can be that two constraints become active at the same time_).

- If $\underline{d}_k = \underline{0}$, $\underline{x}_k$ is a minimum over the subspace defined by $W_k$ and we set $\underline{x}_{k+1} = \underline{x}_k$.
The KKT conditions applied to the subproblem imply that there are multipliers $\underline{u}^k$ such that:
$$
Q \underline{x}_k + \underline{c} + \sum_{i \in W_k} u_i^k \underline{a}_i = \underline{0}.
$$

---

> If $u_i^k \geq 0$ for every $i \in W_k \cap I$ then $\underline{x}_k$ is a local optimum of original QP (remember that we assumed the problem to be convex, hence KKT conditions are also sufficient).
Else $W_{k+1} = W_k \setminus \{ i' \}$ where $i'$ is the index with the <u>most negative</u> $u_i^k$.

- **Theorem**: if $Q$ is p.d. ($q$ strictly convex), the method (with anti-cycling rule) finds an optimal solution within a finite number of iterations.

> **Remark**: there is a finite number of working sets.

**Extension to non-convex problems**: if $Q$ has some negative eigenvalues, the active-set method for convex QP can be adapted by modifying $\underline{d}_k$ and $\alpha_k$ in certain situations.
