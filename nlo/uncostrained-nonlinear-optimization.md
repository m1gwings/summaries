---
marp: true
theme: summary
math: mathjax
---
# Unconstrained Nonlinear Optimization

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Edoardo Amaldi_)

</div>

## Optimality conditions

We can express the _generic unconstrained optimization problem_ as:
$$
\min_{\underline{x} \in S} f(\underline{x})
$$
where $S \subseteq \mathbb{R}^n$, $f : S \rightarrow \mathbb{R}$ and $f \in \mathcal{C}^1$ or $f \in \mathcal{C}^2$.
Usually we have $S = \mathbb{R}^n$.

- $\underline{d} \in \mathbb{R}^n$ is a feasible direction at $\underline{\overline{x}} \in S$ if $\exists \overline{\alpha} > 0$ s.t. $\underline{\overline{x}} + \alpha \underline{d} \in S \ \forall \alpha \in [0, \overline{\alpha}]$.

> **Important remark**: if $\underline{\overline{x}} \in \text{int}(S)$ then every $\underline{d} \in \mathbb{R}^n$ is a feasible direction.

### First order necessary local optimality conditions

- **Theorem**: if $f \in \mathcal{C}^1$ on $S$ and $\underline{\overline{x}}$ is a _local minimum_ of $f$ over $S$, then for any feasible direction $\underline{d} \in \mathbb{R}^n$ at $\underline{\overline{x}}$
$$
\nabla f^T(\underline{\overline{x}}) \underline{d} \geq 0,
$$
> namely all feasible directions are ascent directions.
[_In particular, I think, that $f$ has to be interpreted as a $\mathcal{C}^1$ function defined on an open set $A$, whose domain has been restricted to $S$ which could be not open. Hence partial derivatives are well-defined everywhere_].

> **Proof**: consider $\phi : [0, \overline{\alpha}] \rightarrow \mathbb{R}$, $\phi(\alpha) = f(\underline{\overline{x}} + \alpha \underline{d})$.
Since $\underline{\overline{x}}$ is a local minimum of $f$ over $S$, $\alpha = 0$ is a local minimum of $\phi(\alpha)$. By taylor expansion at $\alpha = 0$:
$$
\phi(\alpha) = \phi(0) + \alpha \phi'(0) + o(\alpha).
$$
> Suppose $\phi'(0) \neq 0$ first.
Since (_by definition of $o(\cdot)$_) $\frac{o(\alpha)}{\alpha} \rightarrow 0$ for $\alpha \rightarrow 0^+$, there exists $\delta \in (0, \overline{\alpha}]$ s.t., if $\alpha \in (0, \delta)$, then $\left|\frac{o(\alpha)}{\alpha}\right| < |\phi'(0)|$. Furthermore, for every $\alpha \in (0, \overline{\alpha}]$:
$$
\frac{\phi(\alpha) - \phi(0)}{\alpha} \geq 0
$$
> since $\alpha = 0$ is a local minimum of $\phi$ (_we can assume that $\overline{\alpha}$ is small enough_).

---

> Hence, for $\alpha \in (0, \delta)$, we have:
$$
\phi'(0) + \frac{o(\alpha)}{\alpha} = \frac{\phi(\alpha) - \phi(0)}{\alpha} \geq 0,
$$
> and so it must be $\phi'(0) \geq 0$ (_remember that $\frac{o(\alpha)}{\alpha} < |\phi'(0)|$, hence, the sign of the lhs depends on the sign of $\phi'(0)$_).
Otherwise, if we suppose $\phi'(0) = 0$, then clearly $\phi'(0) \geq 0$.
The proof follows by applying the chain rule to $\phi$ (_observe that $f$ of class ${C}^1$ is differentiable because of the total differential theorem, hence we can apply the chain rule_):
$$
\phi'(0) = \nabla f^T(\underline{\overline{x}}) \underline{d} \geq 0.
$$

### Second order necessary local optimality conditions

- **Theorem**: if $f \in \mathcal{C}^2$ and $\underline{\overline{x}}$ is a local minimum of $f$ over $S$ then:
>> i. $\nabla f^T(\underline{\overline{x}}) \underline{d} \geq 0 \ \forall \underline{d} \in \mathbb{R}^n$ feasible direction at $\underline{\overline{x}}$.
ii. if $\nabla f^T(\underline{\overline{x}}) \underline{d} = 0$ then $\underline{d}^T \nabla^2 f(\underline{\overline{x}}) \underline{d} \geq 0$.

> **Proof**:
>> i. It follows from the first order necessary local optimality condition.
ii. Suppose that $\nabla f^T(\underline{x}) \underline{d} = 0$, then, by second order Taylor expansion:
$$
\phi(\alpha) = \phi(0) + \alpha \phi'(0) + \frac{1}{2} \alpha^2 \phi''(0) + o(\alpha^2) = \phi(0) + \frac{1}{2} \alpha^2 \phi''(0) + o(\alpha^2)
$$
>> since $\phi'(0) = \nabla f^T(\underline{x}) \underline{d} = 0$.
We can apply the same reasoning of the previous proof to:
$$
\frac{\phi(\alpha) - \phi(0)}{\alpha^2} = \frac{1}{2} \phi''(0) + \frac{o(\alpha^2)}{\alpha^2},
$$
>> concluding that $\phi''(0) \geq 0$. Finally, by the chain rule:
$$
\phi''(0) = \frac{\partial}{\partial \alpha} \left[ \nabla f^T(\underline{\overline{x}} + \alpha \underline{d}) \underline{d} \right]_{\lvert \alpha = 0} = \underline{d}^T \frac{\partial}{\partial \alpha}\left[ \nabla f(\underline{\overline{x}} + \alpha \underline{d}) \right]_{\lvert \alpha = 0} = \underline{d}^T \nabla^2 f(\underline{\overline{x}}) \underline{d} \geq 0.
$$

- **Corollary**: if $f \in \mathcal{C}^2$ on $S$ and $\underline{\overline{x}} \in \text{int}(S)$ is a _local minimum_ of $f$ over $S$, then:
>> i. $\nabla f(\underline{\overline{x}}) = \underline{0}$ (_stationarity condition_);
>> ii. $\nabla^2 f(\underline{\overline{x}})$ is positive semi-definite.

> **Proof**: if $\underline{\overline{x}} \in \text{int}(S)$ every direction is a feasible direction. Hence $\nabla f^T(\underline{\overline{x}}) \underline{d} \geq 0$ and $\nabla f^T(\underline{\overline{x}})(- \underline{d}) \geq 0$, so it must be $\nabla f^T(\underline{\overline{x}}) \underline{d} = \underline{0}$ for every $\underline{d}$, hence it must be $\nabla f(\underline{\overline{x}}) = 0$ (_take $\underline{d} = \underline{e}_i$ to show that the $i$-th component of the gradient is $0$_).

---

> For what concerns the second result, we already showed that $\nabla f^T(\underline{\overline{x}}) \underline{d} = 0$ for every direction $\underline{d}$. Hence it must be $\underline{d}^T \nabla^2 f(\underline{\overline{x}}) \underline{d} \geq 0$ for every direction $\underline{d}$, which is the definition of positive semi-definite matrix.

### Sufficient local optimality conditions

Before introducing sufficient local optimality conditions, we need to present a result about positive definite matrices.

- **Theorem**: if $A \in \mathbb{R}^{n \times n}$ is positive definite, there exists a constant $a > 0$ s.t. $\underline{x}^T A \underline{x} \geq a || \underline{d} ||^2$ for all $\underline{x} \in \mathbb{R}^n$.

> **Proof**: by the spectral theorem, we can write:
$$
A = \sum_{i=1}^n \lambda_i(A) \underline{v}_i \underline{v}_i^T.
$$
> We can write the generic $\underline{x} \in \mathbb{R}^n$ as $\underline{x} = \sum_{i=1}^n \alpha \underline{v}_i$.
Then (_assuming $\lambda_1(A) \geq \ldots \geq \lambda_n(A)$_):
$$
\underline{x}^T A \underline{x} = \sum_{i=1}^n \alpha_i \underline{v}_i \sum_{j=1}^n \lambda_j(A) \underline{v}_j \underline{v}_j^T \sum_{k=1}^n \alpha_k \underline{v}_k =
$$
$$
= \sum_{i=1}^n \lambda_i(A) \alpha_i^2 \geq \lambda_n(A) \sum_{i=1}^n \alpha_i^2 = \lambda_n(A) ||\underline{v}||^2.
$$
> This concludes the proof since $\lambda_n(A) > 0$, being $A$ positive definite.

- **Theorem**: if $f \in \mathcal{C}^2$ and $\underline{\overline{x}} \in \text{int}(S)$ such that $\nabla f(\underline{\overline{x}}) = \underline{0}$ and $\nabla^2 f(\underline{\overline{x}})$ is positive <u>definite</u>, then $\underline{\overline{x}}$ is a strict local minimum of $f$ over $S$, namely:
$$
f(\underline{x}) > f(\underline{\overline{x}}) \ \forall\underline{x} \in \mathcal{N}_\epsilon(\underline{\overline{x}}) \cap S.
$$

> **Proof**: let $\underline{d} \in \mathcal{B}_\epsilon(\underline{0})$ be any feasible direction such that $\underline{\overline{x}} + \underline{d} \in S \cap \mathcal{B}_\epsilon(\underline{\overline{x}})$. Then, because of the second order <u>multinomial</u> Taylor's expansion [_see NAML notes_]:
$$
f(\underline{\overline{x}} + \underline{d}) = f(\underline{\overline{x}}) + \nabla f^T(\underline{\overline{x}}) \underline{d} + \frac{1}{2} \underline{d}^T \nabla^2 f(\underline{\overline{x}}) \underline{d} + o(||\underline{d}||^2) =
$$
$$
= f(\underline{\overline{x}}) + \frac{1}{2} \underline{d}^T \nabla^2 f(\underline{\overline{x}}) \underline{d} + o(||\underline{d}||^2).
$$
> By the result above, there exists $a > 0$ s.t. $\underline{d}^T \nabla^2f(\underline{\overline{x}}) \underline{d} \geq a ||\underline{d}||^2$.
Then:
$$
f(\underline{\overline{x}} + \underline{d}) \geq f(\underline{\overline{x}}) + \frac{1}{2} a ||\underline{d}||^2 + o(||\underline{d}||^2).
$$

---

> Let $\epsilon$ be such that $\left| \frac{o(||\underline{d}||^2)}{||\underline{d}||^2} \right| < \frac{a}{4} > 0$ for all $\underline{d}$ s.t. $\underline{\overline{x}} + \underline{d} \in S \cap \mathcal{B}_\epsilon(\underline{x}) \setminus \{ \underline{\overline{x}} \}$. Then:
$$
\frac{f(\underline{\overline{x}} + \underline{d}) - f(\underline{\overline{x}})}{||\underline{d}||^2} = \frac{1}{2}a + \frac{o(||\underline{d}||^2)}{||\underline{d}||^2} > \frac{1}{2} a - \frac{1}{4} a = \frac{1}{4} a > 0.
$$
> Finally, $f(\underline{\overline{x}}) < f(\underline{\overline{x}} + \underline{d})$ as we wanted to prove.

### Optimality conditions for convex problems

Consider the generic unconstrained convex optimization problem:
$$
\min_{\underline{x} \in C} f(\underline{x})
$$
where $C \subseteq \mathbb{R}^n$ and $f : C \rightarrow \mathbb{R}$ are convex.
Remember that, in this setting, every local minimum is a global minimum.

- **Theorem**: let $f$ be convex and $\mathcal{C}^1$ on $C \subseteq \mathbb{R}^n$ convex. $\underline{x}^*$ is a <u>global minimum</u> of $f$ on $C$ iff
$$
\nabla f^T(\underline{x}^*) (\underline{y} - \underline{x}^*) \geq 0 \ \forall \underline{y} \in C.
$$

> **Proof**: (N.C.) (_Necessary Condition_) If $f \in \mathcal{C}^1$ and $\underline{x}^*$ is a global minimum, then, by the N.C. for $\mathcal{C}^1$ functions, $\nabla f^T(\underline{x}^*) \underline{d}$ for every feasible direction $\underline{d}$. Since $C$ is convex, $\underline{y} - \underline{x}^*$ is a feasible direction for every $\underline{y} \in C$. This concludes this direction of the proof.

> (S.C.) (_Sufficient Condition_) We can use the characterization for $\mathcal{C}^1$ convex functions:
$$
f(\underline{y}) \geq f(\underline{x}^*) + \nabla f^T(\underline{x}^*) (\underline{y} - \underline{x}^*) \geq f(\underline{x}^*) \ \forall \underline{y} \in C,
$$
> hence $\underline{x}^*$ is a global minimum.

- **Maximization of convex functions theorem**: let $f$ be convex defined on $C$ convex, bounded and closed. If $f$ has a (finite) maximum over $C$, then there exists an optimal _extreme_ point of $C$.

> **Proof**: suppose that $\underline{x}^*$ is a global maximum of $f$ over $C$, but not an extreme point.

> 1. We will first prove that there exists a point in $\partial C$ which attains the maximum.

>> If $\underline{x}^* \in \partial (C)$ there is nothing to prove. Suppose now that $\underline{x}^* \in \text{int}(C)$.

---

>> We want to show that we can write $\underline{x}^* = \alpha \underline{y}_1 + (1-\alpha) \underline{y}_2$ for some $\underline{y}_1, \underline{y}_2 \in \partial (C)$.
Let $\underline{d} \in \mathbb{R}^n$, $\underline{d} \neq \underline{0}$. Let
$$
A = \left\{ a \in \mathbb{R} \ | \ \underline{x}^* + a \underline{d} \in C \right\}.
$$
>> Since $\underline{x}^* \in \text{int}(C)$, there exists $\epsilon > 0$ s.t. $(-\epsilon, \epsilon) \subseteq A$. Hence $A$ is not empty.
Since $C$ is bounded, the same holds for $A$. Then $a^- = \inf A$ and $a^+ = \sup A$ exist in virtue of the least upper-bound property of $\mathbb{R}$.
Now, suppose there was $\delta > 0$ s.t.
$$
\mathcal{B}_\delta(\underline{x}^* + a^- \underline{d}) \subseteq C,
$$
>> then $\underline{x}^* + (a^- - \frac{\delta}{2 ||\underline{d}||}) \underline{d} \in C$ and so $a^- - \frac{\delta}{2 ||\underline{d}||} \in A$, which is absurd since $a^- = \inf A$. Then, it must be $\underline{x}^* + a^- \underline{d} \in \partial (C)$. Analogously, $\underline{x}^* + a^+ \underline{d} \in \partial (C)$.
Finally, observe that $a^- \leq -\epsilon < 0$ and $a^+ \geq \epsilon > 0$. Then $a^+ - a^- > 0$. Let:
$$
\alpha = \frac{a^+}{a^+-a^-} \in (0, 1).
$$
>> Then:
$$
\alpha (\underline{x}^* + a^-\underline{d}) + (1-\alpha) (\underline{x}^* + a^+ \underline{d}) = \underline{x}^*.
$$
>> This is what we wanted to show, taking $\underline{y}_1 = \underline{x}^* + a^- \underline{d}$ and $\underline{y}_2 = \underline{x}^* + a^+ \underline{d}$.
Finally, because of the convexity:
$$
f(\underline{x}^*) = f(\alpha \underline{y}_1 + (1-\alpha) \underline{y}_2) \leq \alpha f(\underline{y}_1) + (1-\alpha)f(\underline{y}_2) \leq \max\{ f(\underline{y}_1), f(\underline{y}_2) \}.
$$
>> Hence, one among $\underline{y}_1, \underline{y}_2 \in \partial(C)$ must attain the maximum.

> 2. Now, suppose that $\underline{x}^* \in \partial(C)$, but that it is not an extreme point.

>> Consider $T_1 = C \cap H$, where $H$ is a supporting hyperplane at $\underline{x}^* \in \partial(C)$. Clearly $\dim (T_1) \leq n-1$ (_since $\dim(H) = n-1$_). Furthermore $T_1$ is compact being the intersection between a closed and bounded set ($C$), and a closed set ($H$). Then there exists a global optimum $\underline{x}_1$ of $f$ over $T_1$ [_I think that we should assume also that $f$ is continuous: [here](https://math.stackexchange.com/questions/3390339/convex-function-with-convex-and-compact-domain-attains-maximum) is a counterexample for $f$ not continuous_] such that
$$
\max_{\underline{x} \in T_1} f(\underline{x}) = f(\underline{x}_1) = f(\underline{x}^*)
$$

---

>> since $\underline{x}^* \in T_1$. Furthermore, because of (1), we can assume wlog that $\underline{x}_1 \in \partial(T_1)$.

>> Now observe that, if $\underline{x}_1$ is an extreme point of $T_1$, $\underline{x}_1$ is also an extreme point of $C$.
In particular we will prove the contra-positive: suppose that $\underline{x}_1$ is not an extreme point of $C$. Then $\underline{x}_1 = \alpha \underline{z}_1 + (1-\alpha) \underline{z}_2$. By the properties of the supporting hyperplane: $\underline{z}_1, \underline{z}_2 \in C \subseteq H^-$. Now, suppose that either among $\underline{z}_1$ and $\underline{z}_2$ belongs to $H^- \setminus H$. Then (_easy to show by pre-multiplying by $\underline{p}^T$_) $\underline{x}_1 = \alpha \underline{z}_1 + (1-\alpha) \underline{z}_2 \in H^- \setminus H$, but this is absurd since $\underline{x}_1 \in T_1 \subseteq H$. Then it must be $\underline{z}_1, \underline{z}_2 \in H$. Hence $\underline{z}_1, \underline{z}_2 \in T_1$ and so $\underline{x}_1$ is NOT an extreme point of $T_1$.

>> Hence, if $\underline{x}_1$ is an extreme point of $T_1$ we're done. Otherwise we define $T_2$ analogously (_taking $T_1$ as $C$_). At every step, the dimension of $T_i$ decreases (_at least_) by one (_we take the supporting hyperplane w.r.t. $\text{aff}(T_{i-1})$_). The procedure must terminate with an extreme point since, in the worst case, we get to $T_n$,
 which is s.t. $\dim(T_n) = 0$. Such an isolated point must be an extreme point. Finally we exploit the fact that an extreme point of $T_i$ is an extreme point of $T_{i-1}$ and so on, up to $C$.
