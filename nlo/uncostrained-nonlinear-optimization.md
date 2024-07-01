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

## Iterative methods and convergence

Most N.O. (Nonlinear Optimization) methods are **iterative**:
- we start from an initial solution $\underline{x}_0 \in X$;
- we generate a sequence $\{ \underline{x}_k \}_{k \geq 0}$ that "converges" to a point of $\Omega = \{ \text{"desired solutions"} \}$.

We can have different meanings of "**converge**" and "**desired solutions**":
- $\{ \underline{x}_k \}_{k \geq 0}$ converges to a point of $\Omega$ or $\exists$ a limit point of $\{ \underline{x}_k \}_{k \geq 0}$ (_it is equivalent to the limit of a subsequence_) which belong to $\Omega$.
- $\Omega = \{ \text{"global optima"} \}$ or $\Omega = \{ \text{"set of candidate points satisfying 1st/2nd order NC"} \}$.

Often, but not always, the methods are **descent methods**: $f(\underline{x}_{k+1}) < f(\underline{x}_k)$ for each $k$.

We're interested in robust and efficient methods.
1. **RObustness** is associated to global convergence.

- An algorithm is **globally** (**locally**) **convergent** if $\{ \underline{x}_k \}_{k \geq 0}$ satisfies one of the previous properties for any $\underline{x}_0 \in X$ (only for $\underline{x}_0$ in a neighborhood of an $\underline{x}^* \in \Omega$).

---

2. **Efficiency** is characterized by convergence speed.

- Suppose that $\lim_{k \rightarrow +\infty} \underline{x}_k = \underline{x}^*$ where $\underline{x}^* \in \Omega$. We say that $\{ \underline{x}_k \}_{k \geq 0}$ converges to $\underline{x}^*$ with order $p \geq 1$ if $\exists r > 0$ and $k_0 \in \mathbb{N}$ s.t.
$$
||\underline{x}_{k+1} - \underline{x}^*|| \leq r ||\underline{x}_k - \underline{x}^*||^p \ \forall k \geq k_0.
$$
> The _largest_ $p$ is the **order of convergence**, the _smallest_ $r > 0$ is the **rate**.
If $p = 1$ and $r < 1$ the convergence is **linear**, if $p = 1$ and $r \geq 1$, the convergence is **sub-linear**.

> **Remark**: if $p = 1$ the distance w.r.t. $\underline{x}^*$ decreases at each iteration by a factor $r$.

> We can <u>compute</u> the order of convergence and the rate of a sequence as follows: we calculate the value of the limit $\lim_{k \rightarrow +\infty} \frac{|| \underline{x}_{k+1} - \underline{x}^* ||}{||\underline{x}_k - \underline{x}^*||^q}$ for different values of $q \geq 1$. We find the biggest value of $q$, namely $\hat{q}$, for which $\lim_{k \rightarrow +\infty} \frac{|| \underline{x}_{k+1} - \underline{x}^* ||}{||\underline{x}_k - \underline{x}^*||^\hat{q}} = \hat{s}^-$ for some $s > 0$. Then $p = \hat{q}$, $r = \hat{s}$. Indeed, we know that the order can't be greater than $p$ since the sequence diverges. Furthermore the rate can't be greater than $s$ (_usual proof, just take $\epsilon$ small enough_). Finally, since the limit is from below, the inequality is satisfied by every $k \geq k_0$ for some $k_0 \in \mathbb{N}$.

- The **convergence** is **superlinear** if there exists $\{ r_k \}_{k \geq 0}$ s.t. $\lim_{k \rightarrow + \infty} r_k = 0$ and
$$
||\underline{x}_{k+1} - \underline{x}^*|| \leq r_k ||\underline{x}_k - \underline{x}^*|| \ \forall k \geq k_0.
$$

- If $p = 2$ (and $r$ not necessarily smaller than $1$), the **convergence** is **quadratic**.

## Line search methods

**Line search methods** are a family of methods for solving unconstrained non-linear optimization problems iteratively.
The **general scheme** is the following.

1. At the beginning we choose an initial solution $\underline{x}_0$ and a tolerance $\epsilon > 0$. We set $k \gets 0$.

2. At every step $k$:
> 2.1 Choose a search direction $\underline{d}_k \in \mathbb{R}^n$.
> 2.2 Determine a step length $\alpha_k > 0$ along $\underline{d}_k$ satisfying certain criteria.
> 2.3 Set $\underline{x}_{k+1} = \underline{x}_k + \alpha_k \underline{x}_k$ and $k \gets k + 1$.
> 2.4 If the termination criterion is NOT satisfied: go to 2.

Usual **termination criteria** are: $||\nabla f(\underline{x}_k)|| < \epsilon$ or $|f(\underline{x}_k) - f(\underline{x}_{k+1})| < \epsilon$ or $||\underline{x}_{k+1} - \underline{x}_k|| < \epsilon$.

---

Different line search methods differ in the choice of $\underline{d}_k$ and $\alpha_k$ which determines the robustness and the efficiency of the method.

### Search direction

In many line search methods, the search direction has the following shape:
$$
\underline{d}_k = - D_k \nabla f(\underline{x}_k)
$$
with positive definite $n \times n$ matrix $D_k$.

- **Theorem**: $\underline{d}_k = - D_k \nabla f(\underline{x}_k)$ is a descent direction.

> **Proof**: $\nabla f^T(\underline{x}_k) \underline{d}_k = - \nabla f^T(\underline{x}_k) D_k \nabla f(\underline{x}_k) < 0$ since $D_k$ is p.d. and $||\nabla f(\underline{x}_k)|| > 0$ (_otherwise we would have stopped_).

---

#### Gradient method

Given $f \in \mathcal{C}^1$, consider the linear approximation of $f(\underline{x}_k + \underline{d})$ at $\underline{x}_k$:
$$
l_k(\underline{d}) = f(\underline{x}_k) + \nabla f^T(\underline{x}_K) \underline{d}
$$
and choose $\underline{d}_k \in \mathbb{R}^n$ minimizing $l_k(\underline{d})$ over sphere of radius $||\nabla f(\underline{x}_k)||$:
$$
\begin{matrix}
\min \nabla f^T(\underline{x}_k) \underline{d} \\
\text{s.t. } ||\underline{d}|| \leq ||\nabla f(\underline{x}_k)||. 
\end{matrix}
$$
Observe that, by Cauchy-Schwarz inequality $|\nabla f^T(\underline{x}_k) \underline{d}| \leq ||\nabla f(\underline{x}_k)|| ||\underline{d}|| \leq ||\nabla f(\underline{x}_k)||^2$, then $\nabla f^T(\underline{x}_k) \underline{d} \geq - ||\nabla f(\underline{x}_k)||^2$. Finally, this value is attained by $\underline{d}_k = - \nabla f(\underline{x}_k)$, which is thus the minimizer.

In particular, we call $\underline{d}_k = - \nabla f(\underline{x}_k)$ the **steepest descent direction**. Observe that the gradient method is a line search method of the form $\underline{d}_k = - D_k \nabla f(\underline{x}_k)$ where $D_k = I_n \ \forall k$. Since $I_n$ is clearly p.d., $\underline{d}_k$ is a descent direction.

- **Theorem**: if gradient method is applied with exact 1-D search, the successive directions are orthogonal.

> **Proof**: since $\alpha_k$ minimizes $\phi$:
$$
\underline{d}_{k+1}^T \underline{d}_k = \nabla f^T(\underline{x}_{k+1}) \underline{d}_k = \nabla f^T(\underline{x}_{k} + \alpha_k \underline{d}_k) \underline{d}_k = \phi'(\alpha_k) = 0.
$$
The result above shows that, if we were to apply exact 1-D search, gradient method would present a zig-zag trajectory and hence a very slow convergence.

##### Convergence analysis

Let's carry out the convergence analysis for quadratic strictly convex functions first.
Remember that any $\mathcal{C}^2$ function can be well approximated around any local/global minimum by such a function.
In particular, let
$$
f(\underline{x}) = \frac{1}{2} \underline{x}^T Q \underline{x} - \underline{b}^T \underline{x} \text{ with } Q \text{ p.d. }.
$$
The global minimum is the unique solution of $Q \underline{x} = \underline{b}$ ($\nabla f(\underline{x}) = \underline{0}$, _observe that this is a convex problem_) abd $\alpha_k$ can be determined explicitly:
$$
\phi(\alpha) = f(\underline{x}_k - \alpha \nabla f(\underline{x}_k)) = \frac{1}{2} (\underline{x}_k - \alpha \nabla f(\underline{x}_k))^T Q (\underline{x}_k - \alpha \nabla f(\underline{x}_k)) - \underline{b}^T (\underline{x}_k - \alpha \nabla f(\underline{x}_k)).
$$
Then:
$$
\phi'(\alpha) = - (\underline{x}_k - \alpha \nabla f(\underline{x}_k))^T Q \nabla f(\underline{x}_k) + \underline{b}^T \nabla f(\underline{x}_k).
$$

---

Since $\nabla f(\underline{x}_k) = Q \underline{x}_k - \underline{b}$, then $\underline{b} = - \nabla f(\underline{x}_k) + Q \underline{x}_k$.
Hence:
$$
\phi'(\alpha) = - (\underline{x}_k - \alpha \nabla f(\underline{x}_k))^T Q \nabla f(\underline{x}_k) + (-\nabla f(\underline{x}_k) + Q \underline{x}_k)^T \nabla f(\underline{x}_k) =
$$
$$
= - \underline{x}_k Q \nabla f(\underline{x}_k) + \alpha \nabla f^T(\underline{x}_k) Q \nabla f(\underline{x}_k) - \nabla f^T(\underline{x}_k) \nabla f(\underline{x}_k) + \underline{x}_k^T Q \nabla f(\underline{x}_k) =
$$
$$
= \alpha \nabla f^T(\underline{x}_k) Q \nabla f(\underline{x}_k) - \nabla f^T(\underline{x}_k) \nabla f(\underline{x}_k).
$$
Hence:
$$
\phi'(\alpha_k) = 0 \text{ iff } \alpha_k = \frac{\nabla f^T(\underline{x}_k) \nabla f(\underline{x}_k)}{\nabla f^T(\underline{x}_k) Q \nabla f(\underline{x}_k)} = \frac{\underline{d}_k^T \underline{d}_k}{\underline{d}_k^T Q \underline{d}_k}.
$$

Often we consider the convergence rate of $f(\underline{x}_k) \rightarrow f(\underline{x}^*)$ instead of that of $\underline{x}_k \rightarrow \underline{x}^*$ when $k \rightarrow + \infty$.

- **Theorem**: if $H(\underline{x}^*)$ is p.d., $\underline{x}_k$ converges (super)linearly at $\underline{x}^*$ w.r.t $|f(\underline{x}_k) - f(\underline{x}^*)|$ iff it converges in the same way w.r.t. $||\underline{x}_k - \underline{x}^*||$.

> **Proof**: first of all observe that, if $S \in \mathbb{R}^{n \times n}$ is a p.d. matrix, then, for every $\underline{y} \in \mathbb{R}^n$:
$$
\lambda_n(S) ||\underline{y}||^2 \leq \underline{y}^T S \underline{y} \leq \lambda_1(S) ||\underline{y}||^2
$$
> (_usual proof through spectral theorem_).
Now, by second order Taylor expansion:
$$
f(\underline{x}) = f(\underline{x}^*) + \nabla f^T(\underline{x}^*) (\underline{x} - \underline{x}^*) + \frac{1}{2} (\underline{x} - \underline{x}^*)^T H(\underline{x}^*) (\underline{x} - \underline{x}^*) + o(||\underline{x} - \underline{x}^*||^2).
$$
> Remember that $\nabla f(\underline{x}^*) = \underline{0}$.
> Then:
$$
\frac{\lambda_n(H(\underline{x}^*))}{2} ||\underline{x} - \underline{x}^*||^2 + o(||\underline{x} - \underline{x}^*||^2) \leq f(\underline{x}) - f(\underline{x}^*) \leq \frac{\lambda_1(H(\underline{x}^*))}{2} || \underline{x} - \underline{x}^* ||^2 + o(||\underline{x} - \underline{x}^*||^2).
$$
> Fix $\epsilon > 0$. By definition of $o(\cdot)$ we can find a neighborhood $\mathcal{N}(\underline{x}^*)$ s.t. for all $\underline{x} \in \mathcal{N}(\underline{x}^*)$:
$$
\frac{o(||\underline{x} - \underline{x}^*||^2)}{||\underline{x} - \underline{x}^*||^2} \in (-\epsilon, \epsilon),
$$
> which implies:
$$
o(||\underline{x} - \underline{x}^*||^2) \geq - \epsilon ||\underline{x} - \underline{x}^*||^2 \text{, and}
$$
$$
o(||\underline{x} - \underline{x}^*||^2) \leq \epsilon ||\underline{x} - \underline{x}^*||^2.
$$

---

> Then:
$$
\left( \frac{\lambda_n(H(\underline{x}^*))}{2} - \epsilon \right)||\underline{x} - \underline{x}^*||^2 \leq f(\underline{x}) - f(\underline{x}^*) \leq \left(\frac{\lambda_1(H(\underline{x}^*))}{2} + \epsilon \right)||\underline{x} - \underline{x}^*||^2.
$$
> Now, suppose that: $\underline{x}_k \rightarrow \underline{x}^*$ and
$$
||\underline{x}_{k+1} - \underline{x}^*|| \leq r_k ||\underline{x}_k - \underline{x}^*|| \ \forall k \geq k_0.
$$
> Then (_since $\underline{x}_k \rightarrow \underline{x}^*$_), there exists a $k_1$ s.t., for $k \geq k_1$, $\underline{x}_k \in \mathcal{N}(\underline{x}^*)$, and then, for $k \geq \max(k_0, k_1)$:
$$
|f(\underline{x}_{k+1}) - f(\underline{x}^*)| \stackrel{\underline{x}^* \text{ is a minimizer}}{=} f(\underline{x}_{k+1}) - f(\underline{x}^*) \leq \left( \frac{\lambda_1(H(\underline{x}^*))}{2} + \epsilon \right) || \underline{x}_{k+1} - \underline{x}^* ||^2 \leq
$$
$$
\leq \left( \frac{\lambda_1(H(\underline{x}^*))}{2} + \epsilon \right) r_k^2  ||\underline{x}_k - \underline{x}^*||^2 \leq \frac{\frac{\lambda_1(H(\underline{x}^*))}{2} + \epsilon}{\frac{\lambda_n(H(\underline{x}^*))}{2}-\epsilon} r_k^2 (f(\underline{x}_k) - f(\underline{x}^*)) =
$$
$$
= \frac{\lambda_1(H(\underline{x}^*)) + 2 \epsilon}{\lambda_n(H(\underline{x}^*)) - 2 \epsilon} r_k^2 |f(\underline{x}_k) - f(\underline{x}^*)|.
$$
> Observe that we can get as close to $\frac{\lambda_1(H(\underline{x}^*))}{\lambda_n(H(\underline{x}^*))}$ as we want by shrinking $\epsilon$. Anyway $\frac{\lambda_1(H(\underline{x}^*))}{\lambda_n(H(\underline{x}^*))} \geq 1$. If the convergence is superlinear this is not a problem, since the new rate still goes to 0. If the convergence is linear, then it could become sub-linear if $H(\underline{x}^*)$ is badly conditioned.

> If we were to assume that e have (super)linear convergence in $f(\underline{x}_k) \rightarrow f(\underline{x}^*)$, the proof would be analogous.

> **Remark**: this equivalence does not holds in general (e.g. functions non everywhere $\mathcal{C}^1$).

For quadratic strictly convex functions $f(\underline{x}) = \frac{1}{2} \underline{x}^T Q \underline{x} - \underline{b}^T \underline{x}$ we can define the weighted norm $||\underline{x}||_Q^2 = \underline{x}^T Q \underline{x}$.

> **Theorem**: if $f(\underline{x}) = \frac{1}{2} \underline{x}^T Q \underline{x} - \underline{b}^T \underline{x}$ with $Q$ p.d., $\frac{1}{2}||\underline{x} - \underline{x}^*||_Q^2 = f(\underline{x}) - f(\underline{x}^*)$ where $\underline{x}^*$ is the minimizer of $f$.

> **Proof**: observe that $\nabla f(\underline{x}) = Q \underline{x} - \underline{b}$, and $\nabla f(\underline{x}^*) = \underline{0}$, then $Q \underline{x}^* = \underline{b}$, and so:
$$
\frac{1}{2}||\underline{x} - \underline{x}^*||_Q^2 = \frac{1}{2} (\underline{x} - \underline{x}^*)^T Q (\underline{x} - \underline{x}^*) = \frac{1}{2} \underline{x}^T Q \underline{x} - {\underline{x}^*}^T Q \underline{x} + \frac{1}{2} {\underline{x}^*}^T Q \underline{x}^* =
$$
$$
= \frac{1}{2} \underline{x}^T Q \underline{x} - \underline{b}^T \underline{x} + \frac{1}{2} {\underline{x}^*}^T Q \underline{x}^* = f(\underline{x}) + \frac{1}{2} {\underline{x}^*}^T Q \underline{x}^*.
$$

---

> Observe that:
$$
-f(\underline{x}^*) = - \frac{1}{2} {\underline{x}^*}^T Q \underline{x}^* - \underline{b}^T \underline{x}^* = - \frac{1}{2} {\underline{x}^*}^T \underline{b} - \underline{b}^T \underline{x}^* = \frac{1}{2} {\underline{x}^*}^T \underline{b} = \frac{1}{2} {\underline{x}^*}^T Q \underline{x}^*.
$$
> Then:
$$
\frac{1}{2}||\underline{x} - \underline{x}^*||_Q^2 = f(\underline{x}) - f(\underline{x}^*)
$$
> as we wanted to prove.

Before proving an important theorem on the speed of the convergence of the gradient method for quadratic strictly convex, we need to present an intermediate result used in the proof.

- **Kantorovich inequality**: if $Q$ is p.d., for each $\underline{x} \neq \underline{0}$, we have:
$$
\frac{(\underline{x}^T \underline{x})^2}{(\underline{x}^T Q \underline{x}) (\underline{x}^T Q^{-1} \underline{x}) (\underline{x}^T Q^{-1} \underline{x})} \geq \frac{4 \lambda_1(Q) \lambda_n(Q)}{(\lambda_1(Q) + \lambda_n(Q))^2}.
$$

> **Proof**: by spectral decomposition:
$$
\frac{(\underline{x}^T \underline{x})^2}{(\underline{x}^T Q \underline{x}) (\underline{x}^T Q^{-1} \underline{x})} = \frac{(\sum_{i=1}^n \alpha_i^2)^2}{\sum_{j=1}^n \lambda_j^2(Q) \alpha_j^2 \sum_{k=1}^n \frac{1}{\lambda_k^2(Q)} \alpha_k^2} =
$$
$$
= \frac{1}{\sum_{j=1}^n \frac{\alpha_j^2}{\sum_{i=1}^n \alpha_i^2} \lambda_j(Q) \sum_{k=1}^n \frac{\alpha_k^2}{\sum_{i=1}^n \alpha_i^2}\frac{1}{\lambda_k(Q)}}.
$$
> Let $\xi_i = \frac{\alpha_i^2}{\sum_{j=1}^n \alpha_j^2}$ for $i \in \{ 1, \ldots, n \}$. Observe that $\xi_i \in [0, 1] \ \forall i \in \{ 1, \ldots, n \}$ and
$$
\xi_1 + \ldots + \xi_n = 1.
$$
> Then:
$$
\frac{(\underline{x}^T \underline{x})}{(\underline{x}^T Q \underline{x})(\underline{x}^T Q^{-1} \underline{x})} = \frac{1}{(\sum_{i=1}^n \xi_i \lambda_i(Q))(\sum_{i=1}^n \xi_i \frac{1}{\lambda_i(Q)})} = \frac{f(\sum_{i=1}^n \xi_i \lambda_i(Q))}{\sum_{i=1}^n \xi_i f(\lambda_i(Q))}
$$
> where $f(x) = \frac{1}{x}$ is a convex function if we restrict the domain to $\mathbb{R}^+$ (_just check the hessian_).
> Let $l(x)$ be the line from $(\lambda_n(Q), f(\lambda_n(Q))), (\lambda_1(Q), f(\lambda_1(Q)))$:
$$
l(x) = f(\lambda_n(Q)) + \frac{f(\lambda_1(Q)) - f(\lambda_n(Q))}{\lambda_1(Q) - \lambda_n(Q)} (x - \lambda_n(Q)) \text{ for } x \in [\lambda_n(Q), \lambda_1(Q)].
$$
> Remember that, by following the convention of singular values: $\lambda_1(Q) \geq \ldots \geq \lambda_n(Q) > 0$.

---

> Then $\lambda_i(Q) \in [\lambda_n(Q), \lambda_1(Q)]$.
We can always write $\lambda_i(Q)$ as:
$$
\lambda_i(Q) = \lambda_n(Q) + \frac{\lambda_i(Q) - \lambda_n(Q)}{\lambda_1(Q) - \lambda_n(Q)} (\lambda_1(Q) - \lambda_n(Q)) = \alpha_n \lambda_n(Q) + \alpha_1 \lambda_1(Q)
$$
> where $\alpha_n = 1 - \frac{\lambda_i(Q) - \lambda_n(Q)}{\lambda_1(Q) - \lambda_n(Q)} \geq 0$, $\alpha_1 = \frac{\lambda_i(Q) - \lambda_n(Q)}{\lambda_1(Q) - \lambda_n(Q)} \geq 0$ and $\alpha_n + \alpha_1 = 1$.
> Then:
$$
f(\lambda_i(Q)) = f(\alpha_n \lambda_n(Q) + \alpha_1 \lambda_1(Q)) \leq \alpha_n f(\lambda_n(Q)) + \alpha_1 f(\lambda_1(Q)) =
$$
$$
= \left( 1 - \frac{\lambda_i(Q) - \lambda_n(Q)}{\lambda_1(Q) - \lambda_n(Q)} \right) f(\lambda_n(Q)) + \frac{\lambda_i(Q) - \lambda_n(Q)}{\lambda_1(Q) - \lambda_n(Q)} f(\lambda_1(Q)) =
$$
$$
= f(\lambda_n(Q)) + \frac{\lambda_i(Q) - \lambda_n(Q)}{\lambda_1(Q) - \lambda_n(Q)} (f(\lambda_1(Q)) - f(\lambda_n(Q))) = l(\lambda_i(Q)).
$$
> Hence:
$$
\sum_{i=1}^n \xi_i f(\lambda_i(Q)) \leq \sum_{i=1}^n \xi_i l(\lambda_i(Q)) = \sum_{i=1}^n \xi_i \left[ f(\lambda_n(Q)) + \frac{\lambda_i(Q) - \lambda_n(Q)}{\lambda_1(Q) - \lambda_n(Q)}(f(\lambda_1(Q)) - f(\lambda_n(Q))) \right] =
$$
$$
\stackrel{\sum_{i=1}^n \xi_i = 1}{=} f(\lambda_n(Q)) + \frac{\sum_{i=1}^n \xi_i \lambda_i(Q) - \lambda_n(Q)}{\lambda_1(Q) - \lambda_n(Q)} (f(\lambda_1(Q)) - f(\lambda_n(Q))) = l (\sum_{i=1}^n \xi_i \lambda_i(Q)).
$$

> And so:
$$
\frac{(\underline{x}^T \underline{x})^2}{(\underline{x}^T Q \underline{x})(\underline{x}^T Q^{-1} \underline{x})} \geq \frac{f(\sum_{i=1^n \xi_i \lambda_i(Q)})}{l(\sum_{i=1}^n \xi_i \lambda_i(Q))} \stackrel{\lambda = \sum_{i=1}^n \xi_i \lambda_i(Q) \in [\lambda_n(Q), \lambda_1(Q)]}{=} \frac{f(\lambda)}{l(\lambda)} =
$$
$$
= \frac{f(\lambda)}{f(\lambda_1(Q)) + \frac{\lambda - \lambda_n(Q)}{\lambda_1(Q) - \lambda_n(Q)} (f(\lambda_1(Q)) - f(\lambda_n(Q)))} = \frac{\frac{1}{\lambda}}{\frac{1}{\lambda_1(Q)} + \frac{\lambda - \lambda_n(Q)}{\lambda_1(Q) - \lambda_n(Q)} \left(\frac{1}{\lambda_1(Q)} - \frac{1}{\lambda_n(Q)}\right)} =
$$
$$
= \frac{\lambda_n(Q) \lambda_1(Q)}{\lambda (\lambda_n(Q) + \lambda_1(Q)) - \lambda^2} \geq \frac{4 \lambda_n(Q) \lambda_1(Q)}{\frac{\lambda_n(Q) + \lambda_1(Q)}{2} (\lambda_n(Q) + \lambda_1(Q)) - \frac{(\lambda_n(Q) + \lambda_1(Q))^2}{4}} = \frac{4 \lambda_n(Q) \lambda_1(Q)}{(\lambda_n(Q) + \lambda_1(Q))^2}
$$
> where the last inequality comes from the fact that $\lambda (\lambda_n(Q) + \lambda_1(Q)) - \lambda^2 = \lambda [\lambda_n(Q) + \lambda_1(Q) - \lambda]$ attains its maximum at $\frac{\lambda_n(Q) + \lambda_1(Q)}{2}$ (_the average of the roots_).

We're ready to introduce the theorem.
- **Theorem**: if gradient method with <u>exact</u> 1_D search is applied to any quadratic strictly convex $f \in \mathcal{C}^2$, for any $\underline{x}_0$ we have $\lim_{k \rightarrow + \infty} \underline{x}_k = \underline{x}^*$ and
$$
||\underline{x}_{k+1} - \underline{x}^*||_Q^2 \leq \left( \frac{\lambda_1(Q) - \lambda_n(Q)}{\lambda_1(Q) + \lambda_n(Q)} \right)^2 || \underline{x}_k - \underline{x}^* ||_Q^2.
$$

---

> **Proof**: we proved before that the $\alpha_k$ provided by exact line search is:
$$
\alpha_k = \frac{\underline{g}_k^T \underline{g}_k}{\underline{g}_k^T Q \underline{g}_k}
$$
> where $\underline{g}_k = Q \underline{x}_k - \underline{b} = \nabla f(\underline{x}_k)$.
Then:
$$
||\underline{x}_{k+1} - \underline{x}^*||_Q^2 = ||\underline{x}_k - \frac{\underline{g}_k^T \underline{g}_k}{\underline{g}_k^T Q \underline{g}_k}\underline{g}_k - \underline{x}^*||_Q^2  =
$$
$$
= (\underline{x}_k - \underline{x}^*)^T Q (\underline{x}_k - \underline{x}^*) - 2 \frac{\underline{g}_k^T \underline{g}_k}{\underline{g}_k^T Q \underline{g}_k} (\underline{x}_k - \underline{x}^*)^T Q \underline{g}_k + \left( \frac{\underline{g}_k^T \underline{g}_k}{\underline{g}_k^T Q \underline{g}_k} \right)^2 \underline{g}_k^T Q \underline{g}_k =
$$
$$
= ||\underline{x}_k - \underline{x}^*||_Q^2 - 2 \frac{\underline{g}_k^T \underline{g}_k}{\underline{g}_k^T Q \underline{g}_k} (\underline{x}_k - \underline{x}^*)^T Q \underline{g}_k + \frac{(\underline{g}_k^T \underline{g}_k)^2}{\underline{g}_k^T Q \underline{g}_k}.
$$
> Observe that $Q \underline{x}^* = \underline{b}$ since $\nabla f(\underline{x}^*) = \underline{0}$, then $\underline{g}_k = Q \underline{x}_k - \underline{b} = Q (\underline{x}_k - \underline{x}^*)$ iff $\underline{x}_k - \underline{x}^* = Q^{-1} \underline{g}_k$.
hence:
$$
||\underline{x}_{k+1} - \underline{x}^*||_Q^2 = ||\underline{x}_k - \underline{x}^*||_Q^2 - 2 \frac{\underline{g}_k^T \underline{g}_k}{\underline{g}_k^T Q \underline{g}_k} \underline{g}_k^T Q^{-1}Q \underline{g}_k + \frac{(\underline{g}_k^T \underline{g}_k)^2}{\underline{g}_k^T Q \underline{g}_k} =
$$
$$
= ||\underline{x}_k - \underline{x}^*||_Q^2 - \frac{(\underline{g}_k^T \underline{g}_k)^2}{\underline{g}_k^T Q \underline{g}_k} = ||\underline{x}_k - \underline{x}^*||_Q^2 - \frac{(\underline{g}_k^T \underline{g}_k)^2}{(\underline{g}_k^T Q \underline{g}_k)(\underline{g}_k^T Q^{-1} \underline{g}_k)} (\underline{g}_k^T Q^{-1} \underline{g}_k) =
$$
$$
= ||\underline{x}_k - \underline{x}^*||_Q^2 - \frac{(\underline{g}_k^T \underline{g}_k)^2}{(\underline{g}_k^T Q \underline{g}_k)(\underline{g}_k^T Q^{-1} \underline{g}_k)} (\underline{x}_k - \underline{x}^*)^T Q Q^{-1} Q (\underline{x}_k - \underline{x}^*) = 
$$
$$
= ||\underline{x}_k - \underline{x}^*||_Q^2 - \frac{(\underline{g}_k^T \underline{g}_k)^2}{(\underline{g}_k^T Q \underline{g}_k)(\underline{g}_k^T Q^{-1} \underline{g}_k)} ||\underline{x}_k - \underline{x}^*||_Q^2 =
$$
$$
= \left[1 - \frac{(\underline{g}_k^T \underline{g}_k)^2}{(\underline{g}_k^T Q \underline{g}_k)(\underline{g}_k^T Q^{-1} \underline{g}_k)} \right] ||\underline{x}_k - \underline{x}^*||_Q^2.
$$
> Finally, by kantorovich inequality:
$$
||\underline{x}_{k+1} - \underline{x}^*||^2_Q \leq \left[ 1 - \frac{4 \lambda_1(Q) \lambda_n(Q)}{(\lambda_1(Q) + \lambda_n(Q))^2} \right] ||\underline{x}_k - \underline{x}^*||_Q^2 = \left( \frac{\lambda_1(Q) - \lambda_n(Q)}{\lambda_1(Q) + \lambda_n(Q)} \right)^2 ||\underline{x}_k - \underline{x}^*||_Q^2.
$$

---

> **Remark**: if $\lambda_1(Q) = \lambda_n(Q)$ (i.e., $Q = \gamma I$ with $\gamma > 0$), the method "converges" in one iteration: $||\underline{x}_1 - \underline{x}^*||_Q^2 \leq 0$.

> **Remark**: the upper bound is reached for some choices of $\underline{x}_0$.

> **Remark**: the convergence is linear and the rate depends on the condition number $\kappa(Q) = \frac{\lambda_1(Q)}{\lambda_n(Q)}$:
$$
r = \frac{\lambda_1(Q) - \lambda_n(Q)}{\lambda_1(Q) + \lambda_n(Q)} = \frac{\kappa(Q) - 1}{\kappa(Q) + 1}.
$$
> The closer is $\kappa(Q)$ to $1$, the smaller $r$; if the spectrum of $Q$ is very wide, then $\kappa(Q) \gg 1$ and $r \approx 1$.

> **Remark**: remember that: $||\underline{x}_{k+1} - \underline{x}^*||_Q^2 = 2 (f(\underline{x}_k) - f(\underline{x}^*))$.
By the theorem we proved before:
$$
||\underline{x}_{k+1} - \underline{x}^*||_2^2 \leq \frac{\lambda_1(Q) + 2 \epsilon}{\lambda_n(Q) - 2 \epsilon} \left( \frac{\lambda_1(Q) - \lambda_n(Q)}{\lambda_1(Q) + \lambda_n(Q)} \right)^2 ||\underline{x}_k - \underline{x}^*||_2^2 =
$$
$$
= \frac{\lambda_1(Q) + 2 \epsilon}{\lambda_1(Q) + \lambda_n(Q)} \frac{\lambda_1(Q) - \lambda_n(Q)}{\lambda_1(Q) + \lambda_n(Q)} \frac{\lambda_1(Q) - \lambda_n(Q)}{\lambda_n(Q) - 2 \epsilon} ||\underline{x}_k - \underline{x}^*||_2^2.
$$
> For appropriate values of $\epsilon$, the coefficient above is the product of 3 positive terms, each smaller than 1. Hence the convergence is linear also in $\underline{x}_k \rightarrow \underline{x}^*s$.

There are some result also for arbitrary nonlinear functions.
- **Theorem**: if $f \in \mathcal{C}^2$ and gradient method with <u>exact</u> 1-D search converges to $\underline{x}^*$ with $H(\underline{x}^*)$ p.d., then:
$$
f(\underline{x}_{k+1}) - f(\underline{x}^*) \leq \left( \frac{\lambda_1(H(\underline{x}^*)) - \lambda_n(H(\underline{x}^*))}{\lambda_1(H(\underline{x}^*)) + \lambda_n(H(\underline{x}^*))} \right)^2 \left[ f(\underline{x}_k) - f(\underline{x}^*) \right].
$$

> **Remark**: we cannot expect better convergence with inexact (approximate) 1-D search. $\alpha_k$ minimizing $\phi(\alpha)$ might not be the best choice, we could try to "extract" 2nd order information about $f(\underline{x})$.

---

#### Newton method

Given $f \in \mathcal{C}^2$ and $H(\underline{x}_k) = \nabla^2 f(\underline{x}_k)$.
Consider the quadratic approximation of $f(\underline{x}_k + \underline{d})$ at $\underline{x}_k$:
$$
q_k(\underline{d}) = f(\underline{x}_k) + \nabla f^T(\underline{x}_k) \underline{d} + \frac{1}{2} \underline{d}^T H(\underline{x}_k) \underline{d}
$$
and choose $\underline{d}_k \in \mathbb{R}^n$ and $\alpha_k$ leading to a stationary point of $q_k(\underline{d})$.
Observe that:
$$
\nabla_{\underline{d}} q_k(\underline{d}) = \nabla f(\underline{x}_k) + H(\underline{x}_k) \underline{d}.
$$
If $H^{-1}(\underline{x}_k)$ exists (this is not guaranteed), the stationary point of $q_k(\underline{d})$ is attained at:
$$
\underline{d}_k = - H^{-1}(\underline{x}_k) \nabla f(\underline{x}_k).
$$

In particular, we call $\underline{d}_k = -H^{-1}(\underline{x}_k) \nabla f(\underline{x}_k)$ the **newton direction**. Observe that Newton method is a line search method of the form $\underline{d}_k = - D_k \nabla f(\underline{x}_k)$ where $D_k = H^{-1}(\underline{x}_k)$.

If $H(\underline{x}_k)$ is p.d. and $\nabla f(\underline{x}_k) \neq \underline{0}$, $\underline{d}_k$ is a descent direction.
If $H(\underline{x}_k)$ is NOT p.d., $\underline{d}_k$ may not be defined ($\not \exists H^{-1}(\underline{x}_k)$) or may be an ascent direction.

In the "**pure**" Newton method. $\alpha_k = 1 \ \forall k$.

If $f$ is quadratic and strictly convex, we reach the global minimum in a single iteration.

- **Property**: Newton method is invariant w.r.t. affine and non singular coordinate changes.

**Remark**: Newton method is NOT globally convergent, but we have very fast local convergence if $\underline{x}_0$ is sufficiently close to a desired solution.
We will formalize this in a moment.

##### Alternative interpretation

There is an alternative interpretation of Newton's method in 1-D.
Suppose that $f(x) \in \mathcal{C}^2$ and we look for $x^*$ s.t. $f'(x^*) = 0$.
The _method of tangents_ (aka Newton-Raphson method) is a technique to determine the zeros of a 1-D function. We can apply it to $f'$, obtaining Newton's method.
At iteration $k$, $f'(x)$ is approximated with the tangent at $x_k$:
$$
z = f'(x_k) + f''(x_k) (x - x_k).
$$
$x_{k+1}$ corresponds to the intersection with the $x$-axis: $x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$.

In the $n$-D case we want to determine a stationary point of $f(\underline{x})$ by solving the non linear system $\nabla f(\underline{x}) = \underline{0}$ with "Newton-Raphson" method.

---

##### Convergence analysis

Before proving an important convergence theorem for Newton's method, we need some intermediate results.

- **Second order multivariate Taylor's theorem with integral remainder**: suppose that $f \in \mathcal{C}^2(\mathbb{R}^n)$ and that $\underline{p} \in \mathbb{R}^n$.
Then:
$$
\nabla f(\underline{x} + \underline{p}) = \nabla f(\underline{x}) + \int_0^1 \nabla f^2(\underline{x} + t \underline{p}) \underline{p} dt.
$$

> **Proof**: fix $i \in \{ 1, \ldots, n \}$. Let:
$$
\phi_i(t) = \frac{\partial f}{\partial x_i}(\underline{x} + t \underline{p}) \text{ for } t \in \mathbb{R}.
$$
> By the chain rule:
$$
\phi'(t) = \frac{\partial}{\partial \underline{x}} \left[ \frac{\partial f}{\partial x_i} \right](\underline{x} + t \underline{p}) \underline{o} = \begin{bmatrix} \frac{\partial^2 f}{\partial x_1 \partial x_i}(\underline{x} + t \underline{p}) & \cdots & \frac{\partial^2 f}{\partial x_n \partial x_i}(\underline{x} + t \underline{p})  \end{bmatrix} \underline{p},
$$
> which is continuous since $f \in \mathcal{C}^2(\mathbb{R}^n)$.
Hence $\phi_i'$ is integrable and we can apply the FTC:
$$
\phi_i(1) = \phi_i(0) + \int_0^1 \phi_i'(t)dt \text{ iff}
$$
$$
\frac{\partial f}{\partial x_i}(\underline{x} + \underline{p}) = \frac{\partial f}{\partial x_i}(\underline{x}) + \int_0^1 \begin{bmatrix} \frac{\partial^2 f}{\partial x_1 \partial x_i} (\underline{x} + t \underline{p}) & \cdots & \frac{\partial^2 f}{\partial x_n \partial x_i} (\underline{x} + t \underline{p}) \end{bmatrix} \underline{p} dt.
$$
Now, let's join all the partial derivatives in the gradient:
$$
\nabla f(\underline{x} + \underline{p}) = \nabla f(\underline{x}) + \int_0^1 {\nabla^2 f}^T(\underline{x} + t \underline{p}) \underline{p} dt = \nabla f(\underline{x}) + \int_0^1 \nabla^2 f(\underline{x} + t \underline{p}) \underline{p} dt.
$$

- **Theorem**: let $\underline{f} : [a, b] \rightarrow \mathbb{R}^n$ be an integrable function, Then:
$$
||\int_a^b \underline{f}(x)dx||_2 \leq \int_a^b ||\underline{f}(x)||_2 dx.
$$

> **Proof**: let
$$
\underline{v} = \int_a^b \underline{f}(x)dx.
$$
> Let's assume $\underline{v} \neq \underline{0}$, otherwise the statement is trivial by the integral comparison theorem.

---

> Then:
$$
||\underline{v}||_2^2 = \underline{v}^T \underline{v} = \underline{v}^T \int_a^b \underline{f}(x) dx = \int_a^b \underline{v}^T \underline{f}(x) dx \leq \int_a^b ||\underline{v}||_2 ||\underline{f}(x)||_2 dx = 
$$
$$
= ||\underline{v}||_2 \int_a^b ||\underline{f}(x)||_2 dx \text{ iff}
$$
$$
||\underline{v}|| \leq \int_a^b ||\underline{f}(x)||_2 dx
$$
> as we wanted to prove.

- **Theorem**: suppose $f \in \mathcal{C}^2$ and $\underline{x}^*$ s.t. $\nabla f(\underline{x}^*) = \underline{0}$ and $H(\underline{x}^*)$ p.d. and $\exists L > 0$ s.t.
$$
||H(\underline{x}) - H(\underline{y})|| \leq L ||\underline{x} - \underline{y}|| \ \forall \underline{x}, \underline{y} \in \mathcal{N}(\underline{x}^*).
$$
> Then, for $\underline{x}_0$ sufficiently close to a local minimum:
>> i. $\underline{x}_k \rightarrow \underline{x}^*$ with a <u>quadratic</u> convergence order;
>> ii. $\nabla f(\underline{x}_k) \rightarrow 0$ <u>quadratically</u> when $k \rightarrow +\infty$.

> **Proof**: from the definition of Newton step:
$$
\underline{d}_k = - \left[ \nabla^2 f(\underline{x}_k) \right]^{-1} \nabla f(\underline{x}_k).
$$
> Furthermore, by NS optimality condition, $\nabla f(\underline{x}^*) = \underline{0}$.
Then:
$$
\underline{x}_k + \underline{d}_k - \underline{x}^* = \underline{x}_k - \underline{x}^* - [\nabla^2 f(\underline{x}_k)]^{-1} \nabla f(\underline{x}_k) =
$$
$$
= [\nabla^2 f(\underline{x}_k)]^{-1} [\nabla^2 f(\underline{x}_k) (\underline{x}_k - \underline{x}^*) - (\nabla f(\underline{x}_k) - \nabla f(\underline{x}^*))].
$$
> Assume that $\underline{x}_k \in \mathcal{N}(\underline{x}^*)$. By Taylor's theorem:
$$
||\nabla^2 f(\underline{x}_k) (\underline{x}_k - \underline{x}^*) - (\nabla f(\underline{x}_k) - \nabla f(\underline{x}^*))|| = 
$$
$$
= ||\nabla^2 f(\underline{x}_k) (\underline{x}_k - \underline{x}^*) - \int_0^1 \nabla^2 f(\underline{x}^* + t(\underline{x}_k - \underline{x}^*))(\underline{x}_k - \underline{x}^*) dt|| =
$$
$$
= ||\int_0^1 \left\{ \nabla f^2(\underline{x}_k) - \nabla^2 f(\underline{x}^* + t(\underline{x}_k - \underline{x}^*)) \right\} (\underline{x}_k - \underline{x}^*) dt|| \leq
$$
$$
\leq \int_0^1 || \nabla^2 f(\underline{x}_k) - \nabla^2 f(\underline{x}^* + t(\underline{x}_k - \underline{x}^*)) (\underline{x}_k - \underline{x}^*) || dt \leq
$$
$$
\leq \int_0^1 || \nabla^2 f(\underline{x}_k) - \nabla^2 f(\underline{x}^* + t(\underline{x}_k - \underline{x}^*))|| || \underline{x}_k - \underline{x}^* || dt \leq
$$

---

$$
\leq \int_0^1 L ||t (\underline{x}_k - \underline{x}^*)|| || \underline{x}_k - \underline{x}^* || dt = L ||\underline{x}_k - \underline{x}^*||^2 \int_0^1 t dt = \frac{L}{2} ||\underline{x}_k - \underline{x}^*||^2.
$$

> We will take for true the following result: "Since $\nabla^2 f(\underline{x}^*)$ is non-singular, there is a radius $\rho > 0$ s.t. $||[\nabla^2f(\underline{x})]^{-1}|| \leq 2 ||[\nabla^2 f(\underline{x}^*)]^{-1}||$ for all $\underline{x} \in \mathcal{B}_\rho(\underline{x}^*) \subseteq \mathcal{N}(\underline{x}^*)$. This should follow from the fact that (if $\mathcal{B}_r(\underline{x}^*) \subseteq \mathcal{N}(\underline{x}^*)$) the Lipschitz continuity of $\nabla^2 f(\underline{x})$ implies the continuity of its entries, which imply the continuity of the determinant. Then $\nabla^2 f(\underline{x})$ is invertible in a neighborhood since $\nabla^2 f(\underline{x}^*)$ is, furthermore the entries of $\nabla^2 f^{-1}(\underline{x})$ are continuous in $\mathcal{N}(\underline{x}^*)$ (remember the formula for the inversion of a matrix with the determinant which requires only the sum, product, and reciprocal of continuous quantities). Hence the maximum of the eigenvalues of $\nabla^2 f^{-1}(\underline{x})$ is continuous since the roots of a polynomial are continuous in its coefficients [_this is the hardest part to formalize_] and the maximum of continuous functions is continuous, and so $||\nabla^2 f^{-1}(\underline{x})||$ is continuous. _Edit: I think that we can exploit the fact that every norm is continuous, hence we can skip the part about the roots of the polynomial_".
Then, by combining the results:
$$
||\underline{x}_{k+1} - \underline{x}^*|| = ||\underline{x}_k + \underline{d}_k - \underline{x}^*|| =
$$
$$
= ||[\nabla^2 f(\underline{x}_k)]^{-1} [\nabla^2 f(\underline{x}_k) (\underline{x}_k - \underline{x}^*) - (\nabla f(\underline{x}_k) - \nabla f(\underline{x}^*))]|| \leq 
$$
$$
\leq ||[\nabla^2 f(\underline{x}_k)]^{-1}|| ||[\nabla^2 f(\underline{x}_k) (\underline{x}_k - \underline{x}^*) - (\nabla f(\underline{x}_k) - \nabla f(\underline{x}^*))]|| \leq
$$
$$
\leq 2 ||[\nabla^2 f(\underline{x}^*)]^{-1}|| \frac{L}{2} ||\underline{x}_k - \underline{x}^*|| = \tilde{L} || \underline{x}_k - \underline{x}^* ||^2
$$
> with $\tilde{L} = ||[\nabla^2 f(\underline{x}^*)]^{-1}||L$.
Now suppose that $\underline{x}_0 \in \mathcal{B}_{\min\left(\rho, \frac{1}{2\tilde{L}}\right)}(\underline{x}^*) \subseteq \mathcal{B}_\rho(\underline{x}^*) \subseteq \mathcal{N}(\underline{x}^*)$. Then, the hypothesis to apply the inequality above are satisfied:
$$
||\underline{x}_1 - \underline{x}^*|| \leq \tilde{L} || \underline{x}_0 - \underline{x}^* ||^2 \leq \tilde{L} \frac{1}{4 \tilde{L}^2} = \frac{1}{4 \tilde{L}}.
$$
> Furthermore:
$$
||\underline{x}_1 - \underline{x}^*|| \leq \tilde{L} || \underline{x}_0 - \underline{x}^* || ||\underline{x}_0 - \underline{x}^*|| \leq \frac{\tilde{L}}{2 \tilde{L}} || \underline{x}_0 - \underline{x}^* ||,
$$
> hence also $\underline{x}_1$ satisfies the hypotheses to apply the inequality.
> It is easy to see by induction that:
$$
||\underline{x}_k - \underline{x}^*|| \leq \frac{1}{2^{2^k} \tilde{L}}
$$
> which implies $\underline{x}_k \rightarrow \underline{x}^*$.
Hence we have quadratic convergence.

---

> By using the relation $\underline{x}_{k+1} - \underline{x}_k = \underline{d}_k$ and $\nabla f(\underline{x}_k) + \nabla^2 f(\underline{x}_k) \underline{d}_k = \underline{0}$, we obtain that:
$$
||\nabla f(\underline{x}_{k+1})|| = || \nabla f(\underline{x}_{k+1}) - \nabla f(\underline{x}_k) - \nabla^2 f(\underline{x}_k) \underline{d}_k || =
$$
$$
= ||\int_0^1 \nabla^2 f(\underline{x}_k + t (\underline{x}_{k+1} - \underline{x}_k)) (\underline{x}_{k+1} - \underline{x}^*)dt - \nabla^2 f(\underline{x}_k) \underline{d}_k|| =
$$
$$
= ||\int_0^1 [\nabla^2 f(\underline{x}_k + t \underline{d}_k) - \nabla^2 f(\underline{x}_k)] \underline{d}_k dt|| \leq  \int_0^1 ||\nabla^2 f(\underline{x}_k + t \underline{d}_k) - \nabla^2 f(\underline{x}_k)|| ||\underline{d}_k|| dt \leq
$$
$$
\leq \int_0^1 L t ||\underline{d}_k||^2 dt = \frac{L}{2} ||\underline{d}_k||^2 = \frac{L}{2} ||[\nabla^2 f(\underline{x}_k)]^{-1} \nabla f(\underline{x}_k)||^2 \leq
$$
$$
\leq \frac{L}{2} ||[\nabla^2 f(\underline{x}_k)]^{-1}||^2 ||\nabla f(\underline{x}_k)||^2 \leq \frac{L}{2}4 ||[\nabla^2 f(\underline{x}^*)]^{-1}||^2 ||\nabla f(\underline{x}_k)||^2 = 2 \tilde{L} ||\nabla f(\underline{x}_k)||^2
$$
> as we wanted to prove.
(Observe that, by what we proved before, we're guaranteed that $\underline{x}_{k+1}$, $\underline{x}_k$ and all the points in the segment which connects them, satisfy all the hypothesis required to apply the inequalities).

##### Modification and extensions

1. If $\alpha_k = 1$ does not satisfy Wolfe (or other) conditions, then we can apply inexact 1-D search.

2. To guarantee global convergence
$$
\underline{d}_k = - D_k \nabla f(\underline{x}_k)
$$
> with $D_k \neq [\nabla^2 f(\underline{x}_k)]^{-1}$. If $D_k$ is symmetric and p.d, $\underline{d}_k$ is a descent direction. We can make a trade-off between steepest descent and Newton directions:
$$
D_k = (\epsilon_k I + \nabla^2 f(\underline{x}_k))^{-1}
$$
> where $\epsilon_k > 0$ is the smallest value such that the eigenvalues of $\epsilon_k I + \nabla^2 f(\underline{x}_k)$ are positive. It coincides with "pure" Newton method when getting closer to a local minimum.

3. **Trust region methods**: the idea is the following, we simultaneously determine $\underline{d}_k$ and $\alpha_k$ by minimizing a local quadratic approximation $q_k(\underline{x})$ at $\underline{x}_k$ over a trust region on which $q_k(\underline{x})$ provides a good approximation of $f(\underline{x})$.
For example $\mathcal{B}_k = \{ \underline{x} \in \mathbb{R}^n \ | \ ||\underline{x} - \underline{x}_k|| \leq \Delta_k \}$. In general, the trust region subproblem: $\min_{\underline{x} \in \mathcal{B}_k} q_k(\underline{x})$ can be solved in closed form or it has low computational requirements.

---

> The trust region size (e.g. $\Delta_k$) is updated adaptively during the iterations based on an estimate of the quality (e.g. $\max |f(\underline{x} - q_k(\underline{x}))|$) of the quadratic approximation over it.

---

#### Conjugate direction methods

The aim of this method it to aim at a faster convergence than gradient method and lower computational load than Newton method.
As usual, let's consider the quadratic strictly convex case first:
$$
\min_{\underline{x} \in \mathbb{R}^n} q(\underline{x}) = \frac{1}{2} \underline{x}^T Q \underline{x} - \underline{b}^T \underline{x}$$
with $Q$ $n \times n$ symmetric and p.d. .

- Given $n \times n$ and symmetric $Q$, two nonzero $\underline{d}_1, \underline{d}_2 \in \mathbb{R}^n$ are **$Q$-conjugate** if $\underline{d}_1^T Q \underline{d}_2 = 0$.

- **Theorem**: if $Q$ p.d. and nonzero $\underline{d}_0, \ldots, \underline{d}_k$ are mutually $Q$-conjugate, then $\underline{d}_0, \ldots, \underline{d}_k$ are linearly independent.

> **Proof**: suppose that $\lambda_0 \underline{d}_0 + \ldots + \lambda_k \underline{d}_k = \underline{0}$. Fix $i \in \{ 0, \ldots, k \}$. By left multiplying by $\underline{d}_i^T Q$ and exploiting $Q$-conjugacy:
$$
\lambda_i \underline{d}_i^T Q \underline{d}_i = 0.
$$
> Then, since $Q$ is p.d. and $\underline{d}_i \neq \underline{0}$ (by definition), $\underline{d}_i^T Q \underline{d}_i > 0$, hence $\lambda_i = 0$.
Hence it must be $\lambda_0 = \ldots = \lambda_k = 0$ as we wanted to prove.

$Q$-conjugacy is a really useful property w.r.t. the optimization of $q(\underline{x})$ because of the following observation: let $\underline{d}_0, \ldots, \underline{d}_{n-1}$ be $n$ mutually $Q$-conjugate vectors. We just proved that they must be linear independent, thus constituting a base of $\mathbb{R}^n$.
Hence we can write:
$$
\underline{x} = \sum_{i=0}^{n-1} \alpha \underline{d}_i
$$
for the generic $\underline{x} \in \mathbb{R}^n$. If we plug this change of coordinates in the expression of $q$, we get:
$$
\tilde{q}(\underline{\alpha}) = \frac{1}{2}(\sum_{i=0}^{n-1} \alpha_i \underline{d}_i)^T Q (\sum_{i=0}^{n-1} \alpha_i \underline{d}_i) - \underline{b}^T (\sum_{i=0}^{n-1} \alpha_i \underline{d}_i) = \sum_{i=0}^{n-1} \left[ \frac{1}{2} \alpha_i^2 \underline{d}_i^T Q \underline{d}_i - \alpha_i \underline{b}^T \underline{d}_i \right] =
$$
$$
= \sum_{i=0}^{n-1} \tilde{q}(\alpha_i) \text{ where } \tilde{q}(\alpha_i) = \left[ \frac{1}{2} \alpha_i^2 \underline{d}_i^T Q \underline{d}_i - \alpha_i \underline{b}^T \underline{d}_i \right].
$$
We have written $\tilde{q}(\underline{\alpha})$ as the sum of $n$ independent 1-D quadratic strictly convex functions, which can be optimized independently.

---

- **Conjugate directions theorem**: let $\{ \underline{d}_i \}_{i=0}^{n-1}$ be $n$ nonzero mutually $Q$-conjugate directions.
For any $\underline{x}_0 \in \mathbb{R}^n$, $\{ \underline{x}_k \}_{k \geq 0}$ generated according to
$$
\underline{x}_{k+1} = \underline{x}_k + \alpha_k \underline{d}_k
$$
> with
$$
\alpha_k = - \frac{\underline{g}_k^T \underline{d}_k}{\underline{d}_k^T Q \underline{d}_k} \text{ and } \underline{g}_k = \nabla q(\underline{x}_k) = Q \underline{x}_k - \underline{b}
$$
> terminates to the (unique) global optimal solution $\underline{x}^*$ of $q(\underline{x})$ in at most $n$ iterations, that is:
$$
\underline{x}_n = \underline{x}_0 + \sum_{k=0}^{n-1} \alpha_k \underline{d}_k = \underline{x}^*.
$$

> **Proof**: since $\underline{d}_k$s are linearly independent, $\exists$ $\alpha_k$s such that
$$
\underline{x}^* - \underline{x}_0 = \alpha_0 \underline{d}_0 + \ldots + \alpha_{n-1} \underline{d}_{n-1}.
$$
> By multiplying both sides by $\underline{d}_k^T Q$ and exploiting $Q$-conjugacy, we get:
$$
\underline{d}_k^T Q (\underline{x}^* - \underline{x}_0) = \alpha_k \underline{d}_k^T Q \underline{d}_k \text{ iff } \alpha_k = \frac{\underline{d}_k^T Q (\underline{x}^* - \underline{x}_0)}{\underline{d}_k^T Q \underline{d}_k}.
$$
> Observe that $\underline{x}_k - \underline{x}_0 = \alpha_0 \underline{d}_0 + \ldots + \alpha_{k-1} \underline{d}_{k-1}$.
Then:
$$
\underline{d}_k^T Q (\underline{x}_k - \underline{x}_0) = 0.
$$
> Finally:
$$
\alpha_k = \frac{\underline{d}_k^T Q (\underline{x}^* - \underline{x}_k + \underline{x}_k - \underline{x}_0)}{\underline{d}_k^T Q \underline{d}_k} = \frac{\underline{d}_k^T Q (\underline{x}^* - \underline{x}_k)}{\underline{d}_k^T Q \underline{d}_k} =
$$
$$
= - \frac{\underline{d}_k^T (Q \underline{x}_k - \underline{b})}{\underline{d}_k^T Q \underline{d}_k} = - \frac{\underline{g}_k^T \underline{d}_k}{\underline{d}_k^T Q \underline{d}_k}.
$$

- **Expanding subspace theorem**: let $\underline{d}_0, \ldots, \underline{d}_{n-1}$ be nonzero mutually $Q$-conjugate vectors. Then, for any $\underline{x}_0 \in \mathbb{R}^n$, $\{ \underline{x}_k \}_{k \geq 0}$ generated according to:
$$
\underline{x}_{k+1} = \underline{x}_k + \alpha_k \underline{d}_k \text{ with } \alpha_k = -\frac{\underline{g}_k^T \underline{d}_k}{\underline{d}_k^T Q \underline{d}_k}
$$

---

> is such that
$$
\underline{x}_k = \underline{x}_0 + \sum_{j=0}^{k-1} \alpha_j \underline{d}_j
$$
> <u>minimizes</u> $q(\underline{x}) = \frac{1}{2} \underline{x}^T Q \underline{x} - \underline{b}^T \underline{x}$, not only on the <u>line</u>
$$
\{ \underline{x} \in \mathbb{R}^n \ | \ \underline{x} = \underline{x}_{k-1} + \alpha \underline{d}_{k-1}, \alpha \in \mathbb{R} \}
$$
> but also on the <u>affine subspace</u> $V_k = \{ \underline{x} \in \mathbb{R}^n \ | \ \underline{x} = \underline{x}_0 + \text{span}\{ \underline{d}_0, \ldots, \underline{d}_{k-1} \} \}$.
> In particular, $\underline{x}_n$ is the global optimum of $q(\underline{x})$ on $\mathbb{R}^n$.

> **Proof**: recall the NS optimality condition for convex problems: since $q(\underline{x})$ is convex, $\underline{x}^*$ is a global minimum of $q(\underline{x})$ over the convex set $C \subseteq \mathbb{R}^n$ iff $\nabla q^T(\underline{x}^*) (\underline{x} - \underline{x}^*) \geq 0$ for all $\underline{x} \in C$.
Furthermore $V_k$ is a convex set. We will prove that $\nabla q^T(\underline{x}_k)(\underline{x} - \underline{x}_k) \geq 0$ for all $\underline{x} \in V_k$, for every $k$.
Then the result will follow by the remark above.
Fix $k \in \{ 0, \ldots, n \}$.
$$
\nabla q(\underline{x}_k) = Q \underline{x}_k - \underline{b} = Q \left( \underline{x}_0 + \sum_{j=0}^{k-1} \alpha_j \underline{d}_j \right) - \underline{b} =
$$
$$
= Q \underline{x}_0 + \sum_{j=0}^{k-1} \alpha_j Q \underline{d}_j - \underline{b} = \underline{g}_0 + \sum_{j=0}^{k-1} \alpha_j Q \underline{d}_j.
$$
> Let $\underline{x} \in V_k$, then $\underline{x} = \underline{x}_0 + \sum_{j=0}^{k-1} \lambda_j \underline{d}_j$ where $\lambda_j \in \mathbb{R}$ for all $j \in \{ 0, \ldots, k-1 \}$. Hence:
$$
\underline{x} - \underline{x}_k = \underline{x}_0 + \sum_{j=0}^{k-1} \lambda_j \underline{d}_j - \underline{x}_0 - \sum_{j=0}^{k-1} \alpha_j \underline{d}_j = \sum_{j=0}^{k-1} (\lambda_j - \alpha_j) \underline{d}_j.
$$
> Then:
$$
\nabla q^T(\underline{x}_k) (\underline{x} - \underline{x}_k) = \sum_{j=0}^{k-1} (\lambda_j - \alpha_j) \underline{g}_0^T \underline{d}_j + \sum_{i=0}^{k-1} \sum_{j=0}^{k-1} \alpha_i (\lambda_j - \alpha_j) \underline{d}_i^T Q \underline{d}_j =
$$
$$
= \sum_{j=0}^{k-1} (\lambda_j - \alpha_j) \underline{g}_0^T \underline{d}_j + \sum_{j=0}^{k-1} \alpha_j (\lambda_j - \alpha_j) \underline{d}_j^T Q \underline{d}_j =
$$
$$
= \sum_{j=0}^{k-1} (\lambda_j - \alpha_j) (\underline{g}_0^T \underline{d}_j - \frac{\underline{g}_j^T \underline{d}_j}{\underline{d}_j^T Q \underline{d}_j} \underline{d}_j^T Q \underline{d}_j) = \sum_{j=0}^{k-1} (\lambda_j - \alpha_j) (\underline{g}_0 - \underline{g}_j)^T \underline{d}_j.
$$

---

> Finally, observe that:
$$
\underline{g}_0 - \underline{g}_j = Q \underline{x}_0 - \underline{b} - Q \underline{x}_j + \underline{b} = Q \underline{x}_0 - Q \underline{x}_0 - \sum_{i=0}^{j-1} \alpha_i Q \underline{d}_i = - \sum_{i=0}^{j-1} \alpha_i Q \underline{d}_i,
$$
> then:
$$
(\underline{g}_0 - \underline{g}_j)^T \underline{d}_j = - \sum_{i=0}^{j-1} \alpha_i \underline{d}_i^T Q \underline{d}_j = 0
$$
> by $Q$-conjugacy.
If follows that
$$
\nabla q^T (\underline{x}_k) (\underline{x} - \underline{x}_k) = 0 \geq 0
$$
> as we wanted to prove.

> **Corollary**: in conjugate direction method, the gradients $\underline{g}_k$ satisfy $\underline{g}_k^T \underline{d}_i = 0$ for all $i \in \{ 1, \ldots, k \}$.

##### Conjugate gradient method for quadratic convex functions

We still need a method to find $Q$-conjugate directions. The conjugate gradient method answer this problem.
It works as follows.

Initialization: choose $\underline{x}_0$ arbitrarily, $\underline{g}_0 = \nabla q(\underline{x}_0) = Q \underline{x}_0 - \underline{b}$, $\underline{d}_0 = - \underline{g}_0$ and $k \gets 0$.

Iteration: $\underline{x}_{k+1} = \underline{x}_k + \alpha_k \underline{d}_k$ with $\alpha_k = -\frac{\underline{g}_k^T \underline{d}_k}{\underline{d}_k^T Q \underline{d}_k}$ (_exact 1-D search_). Then:
$$
\underline{d}_{k+1} = - \underline{g}_{k+1} + \beta_k \underline{d}_k \text{ with } \beta_k = \frac{\underline{g}_{k+1}^T Q \underline{d}_k}{\underline{d}_k^T Q \underline{d}_k}.
$$

**Remarks**:
- $\alpha_k = - \frac{\underline{g}_k^T \underline{d}_k}{\underline{d}_k^T Q \underline{d}_k}$ minimizes $q(\underline{x})$ along the line through $\underline{x}_k$ generated by $\underline{d}_k$ (_this is implied by the expanding subspace theorem_).

- The computational requirements are limited: NO matrix inversion.

- The method is NOT invariant w.r.t. affine transformations of the coordinates.

- **Theorem**: at each iteration $k$ in which the optimum solution of $q(\underline{x})$ has not yet been found ($\underline{g}_i \neq \underline{0}$ for $i \in \{ 0, \ldots, k \}$)
>> i. $\underline{d}_0, \ldots, \underline{d}_{k+1}$ generated are mutually $Q$-conjugate.

---

>> ii. $\alpha_k = \frac{\underline{g}_k^T \underline{g}_k}{\underline{d}_k^T Q \underline{d}_k} (\neq 0 \text{ until we reach the optimum})$.

>> iii. $\beta_k = \frac{\underline{g}_{k+1}^T (\underline{g}_{k+1} - \underline{g}_k)}{\underline{g}_k^T \underline{g}_k} = \frac{\underline{g}_{k+1}^T \underline{g}_{k+1}}{\underline{g}_k^T \underline{g}_k}$.

> **Proof**:

>> i. By induction on $k$, assuming that $\underline{d}_0, \ldots, \underline{d}_k$ are mutually $Q$-conjugate.
Clearly true for the base case (we have only one vector $\underline{d}_0$).
Inductive step: suppose that $\underline{d}_0, \ldots, \underline{d}_k$ are $Q$-conjugate.
$$
\underline{d}_{k+1}^T Q \underline{d}_k = [- \underline{g}_{k+1}^T + \beta_k \underline{d}_k^T] Q \underline{d}_k = - \underline{g}_{k+1}^T Q \underline{d}_k + \beta_k \underline{d}_k^T Q \underline{d}_k =
$$
$$
= -\underline{g}_{k+1}^T Q \underline{d}_k + \left( \frac{\underline{g}_{k+1}^T Q \underline{d}_k}{\underline{d}_k^T Q \underline{d}_k} \right) \underline{d}_k^T Q \underline{d}_k = - \underline{g}_{k+1}^T Q \underline{d}_k + \underline{g}_{k+1}^T Q \underline{d}_k = 0.
$$
>>  We need to verify that $\underline{d}_{k+1}^T Q \underline{d}_i = 0 \ \forall i \in \{ 0, \ldots, k-1 \}$.
$\underline{d}_k^T Q \underline{d}_i = - \underline{g}_{k+1}^T Q \underline{d}_i + \beta_k \underline{d}_k^T Q \underline{d}_i$ with the induction assumption $\underline{d}_k^T Q \underline{d}_i = 0 \ \forall i \in \{ 0, \ldots, k-1 \}$.
> Since $\underline{x}_{i+1} = \underline{x}_i + \alpha_i \underline{d}_i$ with $\alpha_i \neq 0$ (because of ii assuming we haven't reached the optimum yet [_we can apply it by ind. hp._])
$$
Q \underline{d}_i = \frac{1}{\alpha_i} (Q \underline{x}_{i+1} - Q \underline{x}_i) = \frac{1}{\alpha_i} (Q \underline{x}_{i+1} - \underline{b} - Q \underline{x}_i + \underline{b}) =
$$
$$
= \frac{1}{\alpha_i} (\underline{g}_{i+1} - \underline{g}_i) \stackrel{\text{def of } \underline{d}_i}{=} \frac{1}{\alpha_i} (- \underline{d}_{i+1} + \beta_i \underline{d}_i + \underline{d}_i - \beta_{i-1} \underline{d}_{i-1})
$$
>> is a linear combination of $\underline{d}_{i+1}, \underline{d}_i$ and $\underline{d}_{i-1}$ ($Q \underline{d}_0$ only of $\underline{d}_1$ and $\underline{d}_0$ with $\underline{g}_0 = - \underline{d}_0$).
Now $\underline{d}_0, \ldots, \underline{d}_k$ are mutually $Q$-conjugate, hence (by the expanding subspace property) $\underline{x}_{k+1}$ minimizes $q(\underline{x})$ on the subspace $V_{k+1}$ generated by $\underline{d}_0, \ldots, \underline{d}_k$ with $\underline{x}_0 \in V_{k+1}$.
Therefore $\underline{g}_{k+1} = \nabla q(\underline{x}_{k+1})$ is orthogonal to $V_{k+1}$ (_this is what we proved in the proof of the expanding subspace theorem_) and $Q \underline{d}_i \in V_{k+1}$ for $i \in \{ 0, \ldots, k-1 \}$ (_this is what we just proved_). Hence $\underline{g}_{k+1}^T Q \underline{d}_i = 0$ as we wanted to prove.

>> ii. Since $\underline{d}_k = - \underline{g}_k + \beta_{k+1} \underline{d}_{k-1}$, $\alpha_k = - \frac{\underline{g}_k^T \underline{d}_k}{\underline{d}_k^T Q \underline{d}_k}$ we can rewrite
$$
\alpha_k = \frac{\underline{g}_k^T \underline{g}_k}{\underline{d}_k^T Q \underline{d}_k} - \beta_{k-1} \frac{\underline{g}_k^T \underline{d}_{k-1}}{\underline{d}_k^T Q \underline{d}_k}.
$$

---

>> (_just plug the expression of $\underline{d}_k$ into that of $\alpha_k$_).

>> But $\underline{g}_k^T \underline{d}_{k-1} = 0$ since $\underline{d}_0, \ldots, \underline{d}_{k-1}$ because of the expanding subspace property. Moreover, $\alpha_k \neq 0$, since $\underline{g}_k \neq \underline{0}$.

>> iii. $\underline{g}_{k+1} - \underline{g}_k = Q (\underline{x}_{k+1} - \underline{x}_k) = \alpha_k Q \underline{d}_k$ implies that:
$$
\underline{g}_{k+1}^T Q \underline{d}_k = \frac{1}{\alpha_k} \underline{g}_{k+1}^T (\underline{g}_{k+1} - \underline{g}_k).
$$
>> According to ii
$$
\beta_k = \frac{\underline{g}_{k+1}^T Q \underline{d}_k}{\underline{d}_k^T Q \underline{d}_k} = \frac{1}{\alpha_k} \frac{\underline{g}_{k+1}^T (\underline{g}_{k+1} - \underline{g}_k)}{\underline{d}_k^T Q \underline{d}_k} =
$$
$$
\stackrel{\text{ii}}{=} \frac{\underline{d}_k^T Q \underline{d}_k}{\underline{g}_k^T \underline{g}_k} \frac{\underline{g}_{k+1}^T (\underline{g}_{k+1} - \underline{g}_k)}{\underline{d}_k^T Q \underline{d}_k} = \frac{\underline{g}_{k+1}^T (\underline{g}_{k+1} - \underline{g}_k)}{\underline{g}_k^T \underline{g}_k}.
$$
>> Since $\underline{g}_k \stackrel{\text{def. of } \underline{d}_k}{=} - \underline{d}_k + \beta_{k-1} \underline{d}_{k-1}$ belongs to the subspace generated by $\underline{d}_0, \ldots, \underline{d}_k$ and $\underline{g}_{k+1}$ is orthogonal to this subspace, we have $\underline{g}_{k+1}^T \underline{g}_k = 0$ and hence
$$
\beta_k = \frac{\underline{g}_{k+1}^T \underline{g}_{k+1}}{\underline{g}_k^T \underline{g}_k}.
$$

##### Conjugate direction methods for arbitrary nonlinear functions

Conjugate direction methods generalize the conjugate gradient method to arbitrary functions with large $n$. We must use formulae for $\alpha_k$ and $\beta_k$ that do not depend on the Hessian.

$\alpha_k$ is computed through inexact 1-D search and $\underline{d}_{k+1} = - \nabla f(\underline{x}_{k+1}) + \beta_k \underline{d}_k$.

The most popular formulae for $\beta_k$ are:
- **Fletcher-Reeves**
$$
\beta_k^{\text{FR}} = \frac{||\nabla f(\underline{x}_{k+1})||^2}{||\nabla f(\underline{x}_k)||^2}.
$$
- **Polak-Ribière**
$$
\beta_k^{\text{PR}} = \frac{\nabla f^T(\underline{x}_{k+1}) (\nabla f(\underline{x}_{k+1}) - \nabla f(\underline{x}_k))}{||\nabla f(\underline{x}_k)||^2}.
$$

---

**Remark**: $\underline{d}_k$ is a descent direction if we do exact 1-D search:
$$
\nabla f^T(\underline{x}_k) \underline{d}_k \stackrel{\text{def. of } \underline{d}_k}{=} - || \nabla f(\underline{x}_k) ||^2 + \beta_k \nabla f^T(\underline{x}_k) \underline{d}_{k-1} = - ||\nabla f(\underline{x}_k)||^2 < 0
$$
where the last inequality comes from the fact that the 1-D search is exact
($0 = \phi'(\alpha_{k-1}) = \nabla f^T(\underline{x}_{k-1} + \alpha_{k-1} \underline{d}_{k-1}) \underline{d}_{k-1} = \nabla f^T(\underline{x}_{k})\underline{d}_{k-1}$).

**Remark**: for quadratic functions the method coincides with the CG method.

**Remark**: for non-quadratic functions, Polak-Ribière version turns out to be more efficient than Fletcher-Reeves one.

At each iteration it suffices to store $\underline{x}_k$, $\nabla f(\underline{x}_k)$, $\nabla f(\underline{x}_{k+1})$ and $\underline{d}_k$.

There is a variant of the CD method "**with restart**": every $m$ iterations ($m \ll n$) $\beta_k \gets 0$, hence we perform a gradient step. This version is globally convergent (since GD is). Observe that, every time we set $\beta_k$ to $0$ we forget all previous information.
For large $n$, we hope to find a solution way before than $n$ iterations!

Let's state some results regarding the convergence of CD.

- **Convergence for quadratic functions**: let $q(\underline{x}) = \frac{1}{2} \underline{x}^T Q \underline{x} - \underline{b}^T \underline{x}$ be quadratic strictly convex, then:
$$
||\underline{x}_{k+1} - \underline{x}^*||_Q^2 \leq \left( \frac{\lambda_{1+k}(Q)-\lambda_n(Q)}{\lambda_{1+k}(Q)+\lambda_n(Q)} \right)^2 || \underline{x}_0 - \underline{x}^* ||_Q^2.
$$

> **Remark**: if there are $m$ large eigenvalues and other $n-m$ "concentrated" around $\tilde{\lambda}$, after $m+1$ iterations $||\underline{x}_{m+1} - \underline{x}^*||_Q \approx \epsilon || \underline{x}_0 - \underline{x}^* ||_Q$ with $\epsilon = \frac{\lambda_{1+m}(Q) - \lambda_n(Q)}{2 \tilde{\lambda}}$, that is, we have an accurate estimate of the solution after $m+1$ iterations.

- **Convergence for arbitrary functions**:
> 1. If $f \in \mathcal{C}^2$ and $\{ \underline{x}_k \}_{k \geq 0}$ generated by the FR method with exact 1-D search converges to $\underline{x}^*$ with p.d. $H(\underline{x}^*)$, then
$$
\lim_{k \rightarrow + \infty} \frac{||\underline{x}_{k+n} - \underline{x}^*||}{||\underline{x}_k - \underline{x}^*||} = 0,
$$
>> namely, the convergence is <u>superlinear within $n$ iterations</u>.

>> There are similar results also for inexact 1-D search.

> 2. FR method <u>converges globally</u> even without "restart".

---

>> Zoutendijk theorem implies that for FR method with inexact 1-D search satisfying strong Wolfe conditions with $0 < c_1 < c_2 < \frac{1}{2}$, we have
$$
\lim_{k \rightarrow +\infty} \int ||\nabla f(\underline{x}_k)|| = 0.
$$
>> THat is, a subsequence has $||\nabla f(\underline{x}_k)||$ that converges to $0$.

##### Preconditioned conjugate gradient method

The conjugate gradient method (CG) can be accelerated by a variable change $\underline{x} = S \underline{y}$, where $S$ is an $n \times n$ symmetric and non-singular matrix.
By applying CG to:
$$
h(\underline{y}) = q(S \underline{y}) = \frac{1}{2} \underline{y}^T S Q S \underline{y} - \underline{b}^T S \underline{y},
$$
we obtain:
$$
\underline{y}_{k+1} = \underline{y}_k + \alpha \tilde{\underline{d}}_k
$$
with $\alpha_k$ determined by 1-D search, $\tilde{\underline{d}}_0 = - \nabla h(\underline{y}_0)$ and $\tilde{\underline{d}_k} = - \nabla h(\underline{y}_k) + \beta_{k-1} \tilde{\underline{d}}_{k-1}$ for
$$
\beta_{k-1} = \frac{\nabla h^T(\underline{y}_k) \nabla h(\underline{y}_k)}{\nabla h^T(\underline{y}_k) \nabla h(\underline{y}_k)}.
$$
Setting $\underline{x}_k = S \underline{y}_k$, $\nabla h(\underline{y}_k) = S \underline{g}_k$, $\underline{d}_k = S \tilde{\underline{d}}_k$, we obtain the equivalent **preconditioned conjugate gradient method**:
$$
\underline{x}_{k+1} = \underline{x}_k + \alpha_k \underline{d}_k
$$
with $\alpha_k$ determined by 1-D search, $\underline{d}_0 = -S\underline{g}_0$ and
$$
\underline{d}_k = - S \underline{g}_k + \beta_{k-1} \underline{d}_{k-1} \ \forall k \in \{ 1, \ldots, n-1 \}
$$
where
$$
\beta_{k-1} = \frac{\underline{g}_k^T S^2 \underline{g}_k}{\underline{g}^T_{k-1} S^2 \underline{g}_{k-1}}.
$$
Clearly, when $S = I$, it coincides with the standard CG method.
Since $\nabla^2 h(\underline{y}) = SQS$, $\tilde{\underline{d}}_0, \ldots, \tilde{\underline{d}}_{n-1}$ are $(SQS)$-conjugate. Moreover $\underline{d}_k = S \tilde{\underline{d}_k}$ implies that $\underline{d}_0, \ldots, \underline{d}_{n-1}$ are $Q$-conjugate.

To achieve faster convergence, we look for $S$ such that $SQS$ has a smaller condition number than $Q$ or eigenvalues that are distributed into "groups".

---

**Recall**: a good approximate solution can be found in a number of iterations not much larger than the number of groups.

#### Quasi-Newton methods

Quasi-Newton methods aim at reducing the computational load of Newton method while trying to preserve the speed of converge due to the exploitation of second order information. Furthermore, we also want a guarantee of global convergence which is absent for Newton method.
The main idea behind this family of methods is the following: instead of using/inverting $\nabla^2 f(\underline{x}_k)$, second order derivative information is extracted from variations in $\nabla f(\underline{x})$.

The **general scheme** for quasi-Newton methods is the following.
We generate a sequence $\{ H_k \}$ of symmetric p.d. approximation of $[\nabla^2 f(\underline{x}_k)]^{-1}$ and take
$$
\underline{x}_{k+1} = \underline{x}_k + \alpha_k \underline{d}_k \text{ with } \underline{d}_k = - H_k \nabla f(\underline{x}_k)
$$
where $\alpha_k > 0$ minimizes $f(\underline{x})$ along $\underline{d}_k$ or satisfies some inexact 1-D search conditions.

**Advantages** w.r.t. Newton method:
- since $H_k$s are symmetric and p.d. we always have a well defined descent direction;
- only involves firsts order derivatives;
- $H_k$ is constructed iteratively, each iteration is $O(n^2)$.

**Disadvantages** w.r.t. Conjugate Direction Method: requires storing/handling matrices.

Let's see how we can approximate the hessian from the variation in the gradient.
As usual let's start from the quadratic approximation of $f(\underline{x})$ around $\underline{x}_k$:
$$
f(\underline{x}_k + \underline{\delta}) \approx f(\underline{x}_k) + \underline{\delta}^T \nabla f(\underline{x}_k) + \frac{1}{2} \underline{\delta}^T \nabla^2 f(\underline{x}_k) \underline{\delta}.
$$
Differentiating (taking the gradient w.r.t. $\underline{\delta}$) we obtain:
$$
\nabla f(\underline{x}_k + \underline{\delta}) \approx \nabla f(\underline{x}_k) + \nabla^2 f(\underline{x}_k) \underline{\delta}.
$$
Substituting $\underline{\delta}$ with $\underline{\delta}_k$, setting $\underline{\delta}_k = \underline{x}_{k+1} - \underline{x}_k$ and $\underline{\gamma}_k = \nabla f(\underline{x}_{k+1}) - \nabla f(\underline{x}_k)$, then:
$$
\underline{\gamma}_k \approx \nabla^2 f(\underline{x}_k) \underline{\delta}_k,
$$
namely
$$
[\nabla^2 f(\underline{x}_k)]^{-1} \underline{\gamma}_k \approx \underline{\delta}_k.
$$
In quasi-Newton methods we want to approximate $[\nabla^2 f(\underline{x}_k)]^{-1}$ with the p.d. matrix $H_{k+1}$. **Important remark**: the difference in the indices is a necessary tradeoff.

---

Since $\underline{\delta}_k$ and $\underline{\gamma}_k$ can only be determined after 1-D search, we select $H_{k+1}$ p.d. such that:
$$
H_{k+1} \underline{\gamma}_k = \underline{\delta}_k
$$
This is known as **secant condition**.
Observe that $H_{k+1}$ is NOT univocally defined: we have $n$ equations in $\frac{n(n+1)}{2}$ unknowns (the matrix is symmetric).

##### Rank one update

Furthermore, remember that we want to build $H_{k+1}$ iteratively, exploiting the information in $H_k$. At every step we don't want to modify $H_k$ too much. A simple way is doing a rank-1 update:
$$
H_{k+1} = H_k + a_k \underline{u} \underline{u}^T.
$$
Observe that $\underline{u} \underline{u}^T$ is a symmetric rank 1 matrix, while $a_k$ is a proportionality coefficient.

To satisfy the secant condition, we must have:
$$
H_k \underline{\gamma}_k + a_k \underline{u} \underline{u}^T \underline{\gamma}_k = \underline{\delta}_k
$$
and hence $\underline{u}$ and $\underline{\delta} - H_k \underline{\gamma_k}$ must be collinear. Indeed $a_k \underline{u}^T \underline{\gamma}_k \cdot \underline{u} = \underline{\delta}_k - H_k \underline{\gamma}_k$.
Since $a_k$ accounts for proportionality, we can set $\underline{u} = \underline{\delta}_k - H_k \underline{\gamma}_k$ and hence $a_k \underline{u}^T \underline{\gamma}_k = 1$. Then:
$$
a_k = \frac{1}{\underline{u}^T \underline{\gamma}_k} = \frac{1}{(\underline{\delta}_k - H_k \underline{\gamma}_k)^T \underline{\gamma}_k}.
$$
Finally:
$$
H_{k+1} = H_k + a_k \underline{u} \underline{u}^T = H_k + \frac{(\underline{\delta}_k - H_k \underline{\gamma}_k)(\underline{\delta}_k - H_k \underline{\gamma}_k)^T}{(\underline{\delta}_k - H_k \underline{\gamma}_k)^T \underline{\gamma}_k}.
$$
This is the so-called **rank one update formula**.

The following **properties** hold:
1. for quadratic strictly convex function, $H_n = Q^{-1}$ in at most $n$ iterations, even with inexact 1-D search;
2. There is NO guarantee that $H_k$ is p.d. . 

##### Rank two updates

Rank two updates of the shape:
$$
H_{k+1} = H_k + a_k \underline{u} \underline{u}^T + b_k \underline{v} \underline{v}^T
$$

---

are more interesting.
To satisfy the second condition, we have:
$$
H_k \underline{\gamma}_k + a_k \underline{u} \underline{u}^T \underline{\gamma}_k + b_k \underline{v} \underline{v}^T \underline{\gamma}_k = \underline{\delta}_k
$$
where $\underline{u}, \underline{v}$ are not determined univocally.
Setting $\underline{u} = \underline{\delta}_k$ and $\underline{v} = H_k \underline{\gamma}_k$, we obtain $a_k \underline{u}^T \underline{\gamma}_k = 1$ and $b_k \underline{v}^T \underline{\gamma}_k = -1$ and hence the rank two update formula:
$$
H_{k+1} = H_k + \frac{\underline{\delta}_k \underline{\delta}_k^T}{\underline{\delta}_k^T \underline{\gamma}_k} - \frac{H_k \underline{\gamma}_k \underline{\gamma}_k^T H_k}{\underline{\gamma}_k^T H_k \underline{\gamma}_k}.
$$
This is the celebrated **Davidon-Fletcher-Powell** (**DFP**) formula.

- **Theorem**: if the **curvature condition** holds:
$$
\underline{\delta}_k^T \underline{\gamma}_k > 0 \ \forall k,
$$
> the DFP method preserves the positive definiteness of $H_k$, i.e., if $H_0$ is p.d. then $H_k$ is p.d. for all $k \geq 1$.

> **Proof**: by induction. Suppose that $H_0$ is p.d. and verify that if $H_k$ is p.d. then $\underline{z}^T H_{k+1} \underline{z} > 0 \ \forall \underline{z} \neq \underline{0}$.
If $H_k$ is p.d. then it admits a Cholesky factorization [_there is a simple algorithm which induces a proof on Wikipedia_] $H_k = L_k L_k^T$.
Let $\underline{a} = L_k^T \underline{z}$ and $\underline{b} = L_k^T \underline{\gamma}_k$, then:
$$
\underline{z}^T \left( H_k - \frac{H_k \underline{\gamma}_k \underline{\gamma}_k^T H_k}{\underline{\gamma}_k^T H_k \underline{\gamma}_k} \right) \underline{z} = \underline{z}^T L_k L_k^T \underline{z} - \frac{\underline{z}^T L_k L_k^T \underline{\gamma}_k \underline{\gamma}_k^T L_k L_k^T \underline{z}}{\underline{\gamma}_k^T L_k L_k^T \underline{\gamma}_k} =
$$
$$
= \underline{a}^T \underline{a} - \frac{(\underline{a}^T \underline{b})^2}{\underline{b}^T \underline{b}} \geq 0
$$
> because of the Cauchy-Schwarz inequality.
Since $\underline{z} \neq \underline{0}$, equality holds if $\underline{a}$ and $\underline{b}$ are collinear, namely if $\underline{z}$ and $\underline{\gamma}_k$ are collinear (since $L_k^T$ is invertible, remember that $r(H_k) = r(L_k L_k^T) = r(L_k)$ [_see NAML summaries_]). Since $\underline{\delta}_k^T \underline{\gamma}_k > 0$ by hypothesis, we have that
$$
\underline{z}^T \frac{\underline{\delta}_k \underline{\delta}_k^T}{\underline{\delta}_k^T \underline{\gamma}_k} \underline{z} = \frac{1}{\underline{\delta}_k^T \underline{\gamma}_k} (\underline{z}^T \underline{\delta}_k)^2 \geq 0.
$$

---

> Observe that, if $\underline{z} = c \underline{\gamma}_k$ for some $c \in \mathbb{R} \setminus \{ 0 \}$ (_it can't be $c=0$ since $\underline{z} \neq \underline{0}$_), then:
$$
\underline{z}^T \frac{\underline{\delta}_k^T \underline{\delta}_k}{\underline{\delta}_k^T \underline{\gamma}_k} \underline{z} = \frac{1}{\underline{\delta}_k^T \underline{\gamma}_k} c^2 (\underline{\gamma}_k^T \underline{\delta}_k)^2 = \frac{c^2}{\underline{\delta}_k^T \underline{\gamma}_k} > 0
$$
> Remember that $H_{k+1} = H_k + \frac{\underline{\delta}_k \underline{\delta}_k^T}{\underline{\delta}_k^T \underline{\gamma}_k} - \frac{H_k \underline{\gamma}_k \underline{\gamma}_k^T H_k}{\underline{\gamma}_k^T H_k \underline{\gamma}_k}$.  Then $\underline{z}^T H_{k+1} \underline{z}$ is the sum of two non-negative quantities and in every case (both when $\underline{z}$ and $\underline{\gamma}_k$ are collinear and when they are not) at least one is strictly positive, thus
$$
\underline{z}^T H_{k+1} \underline{z} > 0
$$
> as we wanted to prove.

- **Theorem**: the curvature condition $\underline{\delta}_k^T \underline{\gamma}_k > 0$ holds for every $k \geq 0$ provided that the 1-D search satisfies (weak or strong) Wolfe conditions.

> **Proof**: for quadratic strictly convex function, $\underline{\gamma}_k = Q \underline{\delta}_k$ (_we already proved this with a different notation_) implies that $\underline{\delta}_k^T Q \underline{\delta}_k = \underline{\delta}_k^T \underline{\gamma}_k > 0$ because $Q$ is p.d..
For arbitrary function, the second Wolfe condition is:
$$
\nabla f^T(\underline{x}_k + \alpha_k \underline{d}_k) \underline{d}_k \geq c_2 \nabla f^T(\underline{x}_k) \underline{d}_k
$$
> with $c_2 < 1$. Observe that $\underline{\delta}_k = \alpha_k \underline{d}_k$, then:
$$
\nabla f^T(\underline{x}_{k+1}) \frac{\underline{\delta}_k}{\alpha_k} \geq c_2 \nabla f^T(\underline{x}_k) \frac{\underline{\delta}_k}{\alpha_k} \text{ iff}
$$
$$
\underline{\gamma}_k^T \underline{\delta}_k = (\nabla f(\underline{x}_{k+1}) - \nabla f(\underline{x}_k))^T \underline{\delta}_k \geq (c_2 - 1) \nabla f^T(\underline{x}_k) \underline{\delta}_k = (c_2 - 1) \alpha_k \nabla f^T(\underline{x}_k) \underline{d}_k > 0
$$
> since $\underline{d}_k$ is a descent direction (_$H_k$ is p.d. because we start with a p.d. matrix and the positive definiteness is preserved by what we just proved_).

The following **properties** hold:
> For quadratic strictly convex functions, DFP method with exact 1-D search:
> 1. terminates in at most $n$ iterations with $H_n = Q^{-1}$;
> 2. generates $Q$-conjugate directions (from $H_0 = I$ generates CG directions);
> 3. secant condition is hereditary, i.e., $H_i \underline{\gamma}_j = \underline{\delta}_j$ for $j \in \{ 0, \ldots, i-1 \}$.

> For arbitrary functions:
> 4. if $\underline{\delta}_k^T \underline{\gamma}_k > 0$ (curvature condition), all $H_k$ are p.d. if $H_0$ is p.d. (hence it is a descent method);
> 5. each iteration is $O(n^2)$;

---

> 6. we have superlinear convergence rate (in general only local);
> 7. if $f(\underline{x})$ is convex, DFP method with exact 1-D search is globally convergent.

##### BFGS

We can construct an approximation of $\nabla f^2(\underline{x}_k)$ rather than of $[\nabla f^2(\underline{x}_k)]^{-1}$. Since we aim at $B_k \approx \nabla^2f(\underline{x}_k)$, $B_k$ must satisfy $B_{k+1} \underline{\delta}_k = \underline{\gamma}_k$ [_it is equivalent to the secant condition_].
Taking $B_{k+1} = B_k + a_k \underline{u} \underline{u}^T + b_k \underline{v} \underline{v}^T$, with similar manipulations, we have
$$
B_{k+1} = B_k + \frac{\underline{\gamma}_k \underline{\gamma}_k^T}{\underline{\gamma}_k^T \underline{\delta}_k} - \frac{B_k \underline{\delta}_k \underline{\delta}_k^T B_k}{\underline{\delta}_k^T B_k \underline{\delta}_k}
$$
[_it is exactly the same expression of DFP where we exchange $\underline{\gamma}_k$ with $\underline{\delta}_k$_] which should be inverted to obtain $H_{k+1}$.
We can do so through the _Sherman-Morrison identity_.

- **Sherman-Morrison identity**:
$$
(A + \underline{a} \underline{b}^T)^{-1} = A^{-1} - \frac{A^{-1} \underline{a} \underline{b}^T A^{-1}}{1 + \underline{b}^T A^{-1} \underline{a}}
$$
> if $A \in \mathbb{R}^{n \times n}$ not singular, $\underline{a}, \underline{b} \in \mathbb{R}^n$ and the denominator is different from 0.

If we apply it twice on the above update, we obtain the **Broyden Fletcher Goldfrab  and Shanno** (**BFGS**) update formula:
$$
H_{k+1} = H_k + \left( 1 + \frac{\underline{\gamma}_k^T H_k \underline{\gamma}_k}{\underline{\delta}_k^T \underline{\gamma}_k} \right) \frac{\underline{\delta}_k \underline{\delta}_k^T}{\underline{\delta}_k^T \underline{\gamma}_k} - \frac{H_k \underline{\gamma}_k \underline{\delta}_k^T + \underline{\delta}_k \underline{\gamma}_k^T H_k}{\underline{\delta}_k^T \underline{\gamma}_k}.
$$
Indeed $B_{k+1} H_{k+1} = I$ if $B_k H_k = I$.

The BFGS method has the same properties from 1 to 5 of DFP method.
In practice, it is more robust w.r.t to rounding errors and inexact 1-D search.
BFGS and DFP are two extreme cases of unique Broyden family of update formulae:
$$
H_{k+1} = (1 - \phi) H_{k+1}^{\text{DFP}} + \phi H_{k+1}^{\text{BFGS}}
$$
with $0 \leq \phi \leq 1$.

The Broyden family updates enjoy the following properties:
- $H_{k+1}$ satisfies secant condition and is p.d. if $\underline{\delta}_k^T \underline{\gamma}_k > 0$.
- The methods are invariant w.r.t. affine transformations.

---

- If $f(\underline{x})$ is quadratic strictly convex, methods with exact 1-D search find $\underline{x}^*$ in at most $n$ iterations ($H_n = Q^{-1}$) and the generated directions are $Q$-conjugate.
- Quasi-Newton methods are much less "sensitive" to inexact 1-D search than CD ones.

Convergence analysis for quasi-Newton methods is complex because the approximation of the inverse Hessian is updated at each iteration.
The convergence speed result for $\{ B_k \}$ or $\{ H_k \}$ assumes inexact 1-D search (Wolfe conditions) where $\alpha_k = 1$ is tried first.

- **Theorem** (**Dennis and Moré**): consider $f \in \mathcal{C}^3$ and quasi-Newton method with $B_k$ p.d. and $\alpha_k = 1$ for each $k$.
If $\lim_{k \rightarrow + \infty} \underline{x}_k = \underline{x}^*$ with $\nabla f(\underline{x}^*) = \underline{0}$ and $\nabla^2 f(\underline{x}^*)$ is p.d., $\{ \underline{x}_k \}$ converges super-linearly iff
$$
\lim_{k \rightarrow + \infty} \frac{||(B_k - \nabla^2 f(\underline{x}^*)) \underline{d}_k||}{||\underline{d}_k||} = 0.
$$

> **Remark**: if quasi-Newton direction $\underline{d}_k$ approximates Newton direction well enough, $\alpha_k = 1$ satisfies Wolfe conditions when $\underline{x}_k \rightarrow \underline{x}^*$. Hence the assumption above is satisfied.

> **Remark**: we do not need that $B_k \rightarrow \nabla^2 f(\underline{x}^*)$, it suffices that $B_k$s become increasingly accurate approximations of $\nabla^2 f(\underline{x}^*)$ along $\underline{d}_k$.

> **Remark**: the condition of Dennis and Moré theorem is satisfied by BFGS and DFP.

Under some assumptions, we can guarantee the global convergence for arbitrary functions with inexact 1-D search.
In general "classical" globalization techniques (restart or trust region) are not adopted because no examples of non convergence are known.

---

### Step length

To guarantee global convergence, an <u>approximate solution</u> $\alpha_k$ of line search:
$$
\min_{\alpha \geq 0} \phi(\alpha) = f(\underline{x}_k + \alpha \underline{d}_k)
$$
is sufficient.

There are different methods to generate $\alpha_k$ and stop when appropriate conditions are satisfied.
Observe that guaranteeing $f(\underline{x}_k + \alpha_k \underline{d}_k) < f(\underline{x}_k)$ is not sufficient. There are counterexamples where $\underline{x}_k$ satisfies such condition, but it oscillates and it is such that $f(\underline{x}_k)$ converges to a suboptimal value.

The basic principles are the following:
- $\alpha$ must not be too small _to avoid premature convergence_;
- $\alpha$ must not be too large _to avoid oscillations_.

#### Wolfe conditions

**Wolfe conditions** are a set of two conditions that the step length must satisfy. As we will see later, they are enough to guarantee global convergence.
The _first condition_ enforces a sufficient reduction:
$$
\phi(\alpha) \leq \phi(0) + c_1 \alpha \phi'(0) \text{ with } c_1 \in (0, 1),
$$
which is equivalent to:
$$
f(\underline{x}_k + \alpha \underline{d}_k) \leq f(\underline{x}_k) + c_1 \alpha \nabla f^T(\underline{x}_k) \underline{d}_k,
$$
which is known as _Armijo criterion_.

> **Remark (A)**: if $\underline{d}_k$ is a decreasing direction, then there exists $\overline{\alpha} > 0$ s.t. the Armijo criterion holds for all $\alpha \in [0, \overline{\alpha}]$.

> **Proof**: since $\underline{d}_k$ is a decreasing direction (that is, $\nabla f^T(\underline{x}_k) \underline{d}_k < 0$), then:
$$
\phi'(0) = \nabla f^T(\underline{x}_k) \underline{d}_k < 0.
$$
> By Taylor's theorem (remember that $f \in \mathcal{C}^1$):
$$
\phi(\alpha) = \phi(0) + \alpha \phi'(0) + o(\alpha).
$$
> Then:
$$\phi(0) + c_1 \alpha \phi'(0) - \phi(\alpha) = \phi(0) + c_1 \alpha \phi'(0) - \phi(0) - \alpha \phi'(0) - o(\alpha) =
$$
$$
= (c_1 - 1) \alpha \phi'(0) - o(\alpha).
$$

---

> By definition of $o(\cdot)$ there exists $\delta > 0$ s.t.
$$
\left|\frac{o(\alpha)}{\alpha}\right| < (c_1 - 1) \phi'(0)
$$
> for all $\alpha \in (0, \delta)$.
Let $\overline{\alpha} = \frac{\delta}{2}$. Then, if $\alpha \in (0, \overline{\alpha}]$:
$$
\phi(0) + c_1 \alpha \phi'(0) - \phi(\alpha) > (c_1 - 1) \alpha \phi'(0) - (c_1 - 1)\alpha \phi'(0) = 0
$$
> Finally, the statement clearly holds for $\alpha = 0$.

The _second condition_ avoids too small steps:
$$
\phi'(\alpha) \geq c_2 \phi'(0) \text{ with } c_2 \in (c_1, 1),
$$
which is equivalent to:
$$
\nabla f^T(\underline{x}_k + \alpha \underline{d}_k) \underline{d}_k \geq c_2 \nabla f^T(\underline{x}_k) \underline{d}_k.
$$

> **Remark (B)**: if $\underline{d}_k$ is a decreasing direction, then there exists $\tilde{\alpha} > 0$ s.t. the second Wolfe condition does NOT hold for all $\alpha \in [0, \tilde{\alpha}]$.

> **Proof**: $\phi'$ is continuous since $f \in \mathcal{C}^1$. Observe that $\phi'(0) < 0$, then (c_2 < 1): $c_2 \phi'(0) > \phi'(0)$.
THe result follows by the continuity of $\phi'$ (take $\epsilon = \frac{(c_2 - 1) \phi'(0)}{2}$).

Let's put everything together. The (**weak**) **Wolfe conditions** are:
$$
\begin{matrix}
\phi(\alpha) \leq \phi(0) + c_1 \alpha \phi'(0) & \text{(2)} \\
\phi'(\alpha) \geq c_2 \phi'(0) & \text{(3)}
\end{matrix}
$$
with $0 < c_1 < c_2 < 1$.

There is a slight variant of Wolfe conditions, known as **strong Wolfe conditions**:
$$
\begin{matrix}
\phi(\alpha) \leq \phi(0) + c_1 \alpha \phi'(0) & \text{(4)} \\
|\phi'(\alpha)| \leq c_2 |\phi'(0)| & \text{(5)}
\end{matrix}
$$
with $0 < c_1 < c_2 < 1$.
This allows to exclude values of $\alpha$ for which $\phi'(\alpha)$ is too positive and thus far from stationary points of $\phi$.

> **Remark**: Wolfe conditions are invariant w.r.t. affine transformation of the variables.

> **Proof**: let $g(\underline{y}) = f(A \underline{y} + \underline{b})$ with $A \in \mathbb{R}^{n \times n}$ invertible.
Then: $\nabla g(\underline{y}) = A^T \nabla f(A \underline{y} + \underline{b})$.
Suppose that $\alpha$ satisfies the Wolfe conditions for $f$ in direction $\underline{d}_k$, at point $\underline{x}_k$.

---

> Let's translate the quantities to the coordinate space of $g$:
$$
\begin{matrix}
\underline{d}_k & \rightarrow & \underline{p}_k = A^{-1} \underline{d}_k \\
\underline{x}_k & \rightarrow & \underline{y}_k = A^{-1} (\underline{x}_k - \underline{b})
\end{matrix}.
$$
> Then $g(\underline{y}_k + \alpha \underline{p}_k) = f(A \underline{y}_k + \alpha A \underline{p}_k + \underline{b}) = f(\underline{x}_k - \underline{b} + \alpha \underline{d}_k + \underline{b}) = \phi(\alpha)$.
> Hence (_Wolfe conditions depend only on $\phi(\cdot)$_) $\alpha$ satisfies the Wolfe conditions for $g$ in direction $\underline{p}_k$ at point $\underline{y}_k$.
Furthermore, let $\underline{p} = A^{-1} \underline{d}$ with $\underline{d} \neq \underline{0}$:
$$
\nabla g^T(\underline{y}) \underline{p} = \nabla f^T(A \underline{y} + \underline{b}) A A^{-1} \underline{d} = \nabla f^T(\underline{x}) \underline{d},
$$
> hence $\underline{p}$ is a decreasing direction for $g$ at $\underline{y}$ iff $\underline{d}$ is a decreasing direction for $f$ at $\underline{x}$.

- **Theorem**: if $f : \mathbb{R}^n \rightarrow \mathbb{R}$ is $\mathcal{C}^1$ and $\underline{d}_k$ descent direction at $\underline{x}_k$ such that $f$ is bounded below along $\{ \underline{x}_k + \alpha \underline{d}_k \ | \ \alpha > 0 \}$. Then if $0 < c_1 < c_2 < 1$ there exists intervals of step lengths satisfying the Wolfe conditions (weak and strong).

> **Proof**: in the proof of remark (A) we showed that there exists $\overline{\alpha} > 0$ s.t.
$$
\phi(\alpha) < \phi(0) + c_1 \alpha \phi'(0)
$$
> for all $\alpha \in (0, \overline{\alpha}]$.
Consider the function:
$$
\begin{matrix}
\psi : [\overline{\alpha}, +\infty) & \rightarrow & \mathbb{R} \\
\alpha & \mapsto & \phi(\alpha) - \phi(0) - c_1 \alpha \phi'(0)
\end{matrix}.
$$
> By what we just remarked, $\psi(\overline{\alpha}) < 0$.
Since $\phi(\alpha)$ is bounded below while $\phi(0) + c_1 \alpha \phi'(0)$ is not, there must exists $\hat{\alpha} > \overline{\alpha}$ s.t.
$$
\psi(\hat{\alpha}) > 0
$$
> (_otherwise $\phi$ would be unbounded_).
Observe that $\psi$ is continuous, then, by the intermediate values theorem [_see Theorem 4.23 of Baby Rudin_], the set $\psi^{-1}(\{ 0 \})$ is not empty.
Furthermore [_by corollary of Theorem 4.8 of Baby Rudin_], since $\{ 0 \}$ is closed w.r.t. $\mathbb{R}$, $\psi^{-1}(\{ 0 \})$ is closed w.r.t. $[\overline{\alpha}, +\infty)$, and, since $[\overline{\alpha}, +\infty)$ is closed, it is also closed w.r.t. $\mathbb{R}$.
Finally, $\psi^{-1}(\{ 0 \}) \subseteq [\overline{\alpha}, +\infty)$, hence it is clearly bounded below. Then there exists
$$
\alpha' = \inf \psi^{-1}(\{ 0 \}),
$$
> furthermore $\alpha' \in \psi^{-1}(\{ 0 \})$ since $\psi^{-1}(\{ 0 \})$ is closed.

---

> We will show that it must be:
$$
\phi(\alpha) < \phi(0) + c_1 \alpha \phi'(0)
$$
> for all $\alpha \in (0, \alpha')$. Indeed, we know already that this is true for $\alpha \in (0, \overline{\alpha}]$. If $\alpha \in (\overline{\alpha}, \alpha')$, it can't be $\phi(\alpha) = \phi(0) + c_1 \alpha \phi'(0)$ (since $\alpha'$ is the infimum), and it can't be:
$$
\phi(\alpha) > \phi(0) + c_1 \alpha \phi'(0)
$$
> otherwise there would be a point $\beta \in (\overline{\alpha}, \alpha)$ s.t.
$$
\phi(\beta) = \phi(0) + c_1 \beta \phi'(0)
$$
> (_and it can't be since $\alpha'$ is the infimum_).

> By the mean value theorem, there must exists a point $\alpha'' \in (0, \alpha')$ s.t.
$$
\alpha' \phi'(\alpha'') = \phi(\alpha') - \phi(0).
$$
> Since $\alpha' \in \psi^{-1}(\{ 0 \})$, $\phi(\alpha') - \phi(0) = c_1 \alpha' \phi'(0)$.
Then:
$$
\alpha' \phi'(\alpha'') = c_1 \alpha' \phi'(0) \text{ iff } \phi'(\alpha'') = c_1 \phi'(0) > c_2 \phi'(0)
$$
> since $c_1 < c_2$ and $\phi'(0) < 0$.
By the continuity of $\phi'$ there must be a neighborhood of $\alpha''$ s.t. the curvature condition holds strictly.
If this neighborhood is inside $(0, \alpha')$, by the remark made before, we also have that the Armijo condition holds strictly.
Finally, $\phi'(\alpha'') = c_1 \phi'(0) < 0$, then:
$$
|\phi'(\alpha'')| = - \phi'(\alpha'') \stackrel{\text{curvature condition}}{<} -c_2 \phi'(0) = c_2 |\phi'(0)|.
$$
> Then, again, also the Strong Wolfe conditions hold in a neighborhood because of the continuity of $|\phi'|$.

#### Method for 1-D search

There are many methods (with/without derivatives) to determine an approximate solution $\alpha_k$ of
$$
\min_{\alpha \geq 0} \phi(\alpha) = f(\underline{x}_k + \alpha \underline{d}_k)
$$
satisfying appropriate conditions (e.g. Wolfe) which guarantee global convergence.

In general, they consist in two phases:
- **bracketing phase**: determine $[\alpha_\min, \alpha_\max]$ containing "acceptable" step lengths;
- select a good value $\alpha$ withing $[\alpha_\min, \alpha_\max]$ via bisection or interpolation.

---

##### Bisection method to find a minimizer of $\phi$

Consider the following setting: $\phi \in \mathcal{C}^1$, $\phi'(0) < 0$ since $\underline{d}_k$ is a descent direction and $\exists \overline{\alpha}$ s.t. $\phi'(\alpha) > 0$ for $\alpha \geq \overline{\alpha}$. <u>The last one is a very strong assumption</u>.

We want to apply the bisection method to find a step length which minimizes (at least locally) $\phi$.

In particular: we start from $[\alpha_\min, \alpha_\max]$ with $\phi'(\alpha_\min) < 0$ and $\phi'(\alpha_\max) > 0$ and iteratively reduce it.

Iteration:
> set $\tilde{\alpha} = \frac{1}{2} (\alpha_\min + \alpha_\max)$.
>> **if** $\phi'(\tilde{\alpha}) > 0$ **then** $\alpha_\max \gets \tilde{\alpha}$;
>> **if** $\phi'(\tilde{\alpha}) < 0$ **then** $\alpha_\min \gets \tilde{\alpha}$.

The convergence is linear with rate $\frac{1}{2}$.

To find the initial values of $\alpha_\min$ and $\alpha_\max$ we can proceed as follows:
1. $\alpha_\min \gets 0$ and $s \gets s_0$;
2. compute $\phi'(s)$
>> **if** $\phi'(s) < 0$ **then** $\alpha_\min \gets s$, $s \gets 2s$, **goto** 2;
>> **if** $\phi'(s) > 0$ **then** $\alpha_\max \gets s$, **stop**.

##### Bisection method for Wolfe conditions

We can adapt the bisection method to find a step length $\alpha_k$ satisfying Wolfe conditions.

Procedure:
> i. select $\alpha > 0$ and set $\alpha_\min \gets 0$, $\alpha_\max \gets 0$.

> ii. **if** $\alpha$ satisfies Wolfe (2) **then** **goto** iii
> &nbsp; &nbsp; **else** $\alpha_\max \gets \alpha$, $\alpha \gets \frac{\alpha_\min + \alpha_\max}{2}$, **goto** ii.

> iii. **if** $\alpha$ satisfies Wolfe (3) **then** $\alpha_k \gets \alpha$, **stop**
> &nbsp; &nbsp; **else** $\alpha_\min \gets \alpha$
$$
\alpha \gets \begin{cases}
2 \alpha_\min \text{ if } \alpha_\max = 0 \\
\frac{1}{2}(\alpha_\min + \alpha_\max) \text{ if } \alpha_\max > 0
\end{cases}
$$
> &nbsp; &nbsp; **goto** ii.

- **Theorem**: if $f \in \mathcal{C}^1$ is bounded below along ray $\{ \underline{x}_k + \alpha \underline{d}_k \}$, the procedure stops after a finite number of iterations and yields $\alpha_k$ satisfying Wolfe conditions.

---

> **Proof**: by how the algorithm is defined either we terminate before or we reach an iteration $N$ s.t.
>> $\alpha_\min^{(N)}$ satisfies Wolfe (2) but not Wolfe (3);

>> $\alpha_\max^{(N)}$ doesn't satisfy Wolfe (2).

> Indeed:
> - if $\alpha^{(0)}$ satisfies the Wolfe conditions then we terminate at the first iteration;
> - if $\alpha^{(0)}$ doesn't satisfy Wolfe (2), then we set $\alpha_\max^{(1)} = \alpha^{(0)}$. Furthermore $\alpha_\min^{(1)} = 0$, which always satisfies Wolfe (2) but not Wolfe (3). Hence $N = 1$;
> - if $\alpha^{(0)}$ satisfies Wolfe (2) but doesn't satisfy Wolfe (3), then $\alpha_\min^{(n+1)} = \alpha^{(n)}$, $\alpha^{(n+1)} = 2 \alpha_\min^{(n+1)} = 2 \alpha^{(n)}$. We stop doubling when wither $\alpha^{(N-1)}$ does NOT satisfy Wolfe (2) for some finite $N-1$ or $\alpha^{(n)}$ satisfies Wolfe conditions (and we terminate). (Observe that, if $\alpha^{(n)}$ were to satisfy Wolfe (2) for all $n$, then $\phi$ would be unbounded). Now (if we haven't terminated) we have $\alpha_\min^{(N)} = \alpha^{(N-2)}$ which satisfies Wolfe (2) but not Wolfe (3) and $\alpha_\max^{(N)} = \alpha^{(N-1)}$ which doesn't satisfy Wolfe (2).

> Observe that $[\alpha_\min^{(N)}, \alpha_\max^{(N)}]$ is a compact subset of $\mathbb{R}$ and $\phi'$ is continuous. Then [_see theorem 4.19 of Baby Rudin aka Heine Cantor theorem_] $\phi'$ is uniformly continuous on $[\alpha_\min^{(N)}, \alpha_\max^{(N)}]$. Let $\epsilon = - (c_2 - c_1) \phi'(0)$, then there exists $\delta > 0$ s.t. for all $\alpha_1, \alpha_2 \in [\alpha_\min^{(N)}, \alpha_\max^{(N)}]$ with $|\alpha_1 - \alpha_2|  < \delta$, then:
$$
|\phi'(\alpha_1) - \phi'(\alpha_2)| < - (c_2 - c_1) \phi'(0).
$$
> Now, observe that for all $n \geq N$ (until we terminate):
>> $\alpha_\min^{(n)}$ satisfies Wolfe (2) but not Wolfe (3);
>> $\alpha_\max^{(n)}$ doesn't satisfy Wolfe (2); $\alpha_\min^{(n)}$, $\alpha_\max^{(n)} \in [\alpha_\min^{(N)}, \alpha_\max^{(N)}]$;
>> $\alpha_\max^{(n)} \geq \alpha_\min^{(n)}$.

> Suppose that $\alpha_\max^{(n)} - \alpha_\min^{(n)} < \delta$. Then, for all $\alpha \in [\alpha_\min^{(n)}, \alpha_\max^{(n)}]$, $|\alpha-\alpha_\min^{(n)}| = \alpha - \alpha_\min^{(n)} < \delta$.
Hence:
$$
(c_2-c_1) \phi'(0) < \phi'(\alpha) - \phi'(\alpha_\min^{(n)}) < - (c_2 - c_1) \phi'(0),
$$
> which implies:
$$
\phi'(\alpha) < -(c_2 - c_1) \phi'(0) + \phi'(\alpha_\min^{(n)}) <
$$
$$
\stackrel{\text{Wolfe (3) not satisfied by } \alpha_min^{(n)}}{<} - (c_2 - c_1) \phi'(0) + c_2 \phi'(0) = c_1 \phi'(0).
$$

---

> Then:
$$
\phi(\alpha_\max^{(n)}) = \phi(\alpha_\min^{(n)}) + \int_{\alpha_\min^{(n)}}^{\alpha_\max^{(n)}} \phi'(\alpha) d\alpha \leq \phi(\alpha_\min^{(n)}) + c_1 \phi'(0)(\alpha_\max^{(n)} - \alpha_\min^{(n)}) \leq
$$
$$
\stackrel{\text{Wolfe (2) satisfied by } \alpha_min^{(n)}}{\leq} \phi(0) + c_1 \alpha_\min^{(n)} \phi'(0) + c_1 \phi'(0) (\alpha_\max^{(n)} - \alpha_\min^{(n)}) = \phi(0) + c_1 \phi'(0) \alpha_\max^{(n)}.
$$
> But this is absurd since $\alpha_\max^{(n)}$ doesn't satisfy Wolfe (2).
Then it must be $\alpha_\max^{(n)} - \alpha_\min^{(n)} \geq \delta > 0$. But at every iteration we bisect the interval:
$$
\alpha_\max^{(n)} - \alpha_\min^{(n)} = \frac{1}{2^{n-N}} [\alpha_\max^{(N)} - \alpha_\min^{(N)}] \geq \delta > 0.
$$
> Hence it must be:
$$
2^n \leq \frac{2^N}{\delta} [\alpha_\max^{(N)} - \alpha_\min^{(N)}].
$$
> Finally:
$$
n \leq N + \log_2\left( \frac{\alpha_\max^{(N)} - \alpha_\min^{(N)}}{\delta} \right).
$$

### Global convergence of line search methods

Suitable assumptions on $\alpha_k$ and $\underline{d}_k$ can guarantee global convergence.
A **key aspect** is the angle $\theta_k$ between $\underline{d}_k$ and $- \nabla f(\underline{x}_k)$, or, more in detail:
$$
\cos(\theta_k) = - \frac{\nabla f^T(\underline{x}_k) \underline{d}_k}{||\nabla f(\underline{x}_k)|| ||\underline{d}_k||}.
$$
There is a general result which shows how far $\underline{d}_k$ can deviate from $-\nabla f(\underline{x}_k)$ and still give rise to globally convergent iterations.

- **Zoutendijk theorem**: consider any line search method iteration with descent $\underline{d}_k$ and $\alpha_k$ satisfying Wolfe conditions. Suppose $f$ is bounded below on $\mathbb{R}^n$, $f \in \mathcal{C}^1$ on an open set $N$ containing $L_0 = \{ \underline{x} \in \mathbb{R}^n \ | \ f(\underline{x}) \leq f(\underline{x}_0)) \}$ and $\nabla f(\underline{x})$ is Lipschitz continuous on $N$, i.e., $\exists L > 0$ s.t.
$$
|| \nabla f(\underline{x}) - \nabla f(\underline{\overline{x}}) || \leq L || \underline{x} - \underline{\overline{x}} || \ \forall \underline{x}, \underline{\overline{x}} \in N.
$$
> Then
$$
\sum_{k \geq 0} \cos^2(\theta_k) || \nabla f(\underline{x}_k) ||^2 < +\infty.
$$

---

> **Proof**: observe that $(\nabla f(\underline{x}_{k+1}) - \nabla f(\underline{x_k}))^T \underline{d}_k \geq c_2 \nabla f^T(\underline{x}_k) \underline{d}_k - \nabla f^T(\underline{x}_k) \underline{d}_k = (c_2 -1) \nabla f^T(\underline{x}_k) \underline{d}_k$ because of Wolfe (3) on $\underline{x}_{k+1}$.
> At the same time, because of the Lipschitz continuity:
$$
(\nabla f(\underline{x}_{k+1}) - \nabla f(\underline{x}_k))^T \underline{d}_k \stackrel{\text{Cauchy-Schwarz}}{\leq} || \nabla f(\underline{x}_{k+1}) - \nabla f(\underline{x}_k) || || \underline{d}_k || \leq
$$
$$
\stackrel{\text{Lipschitz continuity}}{\leq} L || \underline{x}_{k+1} - \underline{x}_k || || \underline{d}_k || = L || \alpha_k \underline{d}_k || || \underline{d}_k || = \alpha_k L || \underline{d}_k ||^2.
$$
> By combining the two inequalities, we obtain:
$$
\alpha_k L || \underline{d}_k ||^2 \geq (c_2 - 1) \nabla f^T(\underline{x}_k) \underline{d}_k \text{ iff}
$$
$$
\alpha_k \geq \frac{c_2 - 1}{L} \frac{\nabla f^T(\underline{x}_k) \underline{d}_k}{|| \underline{d}_k ||^2}.
$$
> By substituting this inequality into Wolfe (2), we obtain:
$$
f(\underline{x}_{k+1}) \leq f(\underline{x}_k) + c_1 \alpha_k \nabla f^T(\underline{x}_k) \underline{d}_k \stackrel{\nabla f^T(\underline{x}_k) \underline{d}_k \leq 0}{\leq} f(\underline{x}_k) - c_1 \frac{1-c_2}{L} \frac{(\nabla f^T(\underline{x}_k) \underline{d}_k)^2}{||\underline{d}_k||^2} =
$$
$$
\stackrel{\text{assuming } \nabla f(\underline{x}_k) \neq \underline{0}}{=} f(\underline{x}_k) - c_1 \frac{1-c_2}{L}\left( \frac{\nabla f^T(\underline{x}_k) \underline{d}_k}{||\nabla f(\underline{x}_k)|| ||\underline{d}_k||} \right)^2 ||\nabla f(\underline{x}_k)||^2 =
$$
$$
= f(\underline{x}_k) - c_1 \frac{1-c_2}{L} \cos^2 (\theta_k) || \nabla f(\underline{x}_k) ||^2 = f(\underline{x}_k) - c \cos^2(\theta_k) || \nabla f(\underline{x}_k) ||^2,
$$
> where $c = c_1\frac{1-c_2}{L} > 0$.
By summing this expression over all indices less than or equal to $k$, we obtain:
$$
f(\underline{x}_{k+1}) - f(\underline{x}_0) = \sum_{j=0}^k (f(\underline{x}_{j+1}) - f(\underline{x}_j)) \leq -c\sum_{j=0}^k \cos^2(\theta_k) || \nabla f(\underline{x}_k) ||^2.
$$
> Since $f$ is bounded below, we have that:
$$
f(\underline{x}_0) - f(\underline{x}_{k+1}) \leq f(\underline{x}_0) + M
$$
> for all $k$. Then:
$$
c \sum_{j=0}^k \cos^2(\theta_k) || \nabla f(\underline{x}_k) ||^2 \leq f(\underline{x}_0) + M.
$$
> Finally, since $\cos^2(\theta_k) ||\nabla f(\underline{x}_k)||^2 \geq 0$, $c \sum_{j=0}^k \cos^2(\theta_k) || \nabla f(\underline{x}_k) ||^2$ is a non-decreasing and bounded sequence, hence it must converge. Being $c > 0$, the result follows.

---

**Important remark**: Zoutendijk theorem implies that $\cos^2(\theta_k) || \nabla f(\underline{x}_k) ||^2 \rightarrow 0$ as $k \rightarrow + \infty$. Hence, if $\cos(\theta_k) \geq \delta > 0 \ \forall k \geq 0$, then it must be $\lim_{k \rightarrow +\infty} || \nabla f(\underline{x}_k) || = 0$, that is: $\lim_{k \rightarrow + \infty} \nabla f(\underline{x}_k) = \underline{0}$.
As a consequence, the gradient method, with $\cos(\theta_k) = 1 \ \forall k$, satisfying Wolfe conditions, is globally convergent.

- **Theorem**: if $D_k$ is symmetric and p.d. $\forall k \geq 0$ and $\exists$ a constant $M$ s.t.
$$
||D_k|| ||D_k||^{-1} \leq M \ \forall k \geq 0
$$ 
> (_bounded condition number_), then
$$
\cos(\theta_k) \geq \frac{1}{M}.
$$
> In such cases Newton and quasi-Newton methods are globally convergent.

> **Proof**: since $D_k$ is symmetric, it is diagonalizable. Being p.d., its eigenvalues are strictly positive. Furthermore, if $\text{eig}(D_k) = \{ \lambda_1, \ldots, \lambda_n \}$ with $\lambda_1 \geq \ldots \geq \lambda_n \geq 0$, then:
$$
\text{eig}(D_k^{-1}) = \{ \frac{1}{\lambda_n}, \ldots, \frac{1}{\lambda_1} \}
$$
> with $\frac{1}{\lambda_n} \geq \ldots \geq \frac{1}{\lambda_1} > 0$.
> Remember that $||D_k|| (= ||D_k||_2) = \lambda_1$ [_see NAMl summaries_].
Analogously $||D_k||^{-1} = \frac{1}{\lambda_n}$.
$$
\cos(\theta_k) = \frac{- \nabla f^T(\underline{x}_k) \underline{d}_k}{||\nabla f(\underline{x}_k)|| || \underline{d}_k ||} = \frac{\nabla f^T(\underline{x}_k) D_k^{-1} \nabla f(\underline{x}_k)}{|| \nabla f(\underline{x}_k) || ||D_k^{-1} \nabla f(\underline{x}_k)||} \geq
$$
$$
\stackrel{\frac{1}{||A \underline{x}||} \geq \frac{1}{||A|| ||\underline{x}||}}{\geq} \frac{\nabla f^T(\underline{x}_k) D_k^{-1} \nabla f(\underline{x}_k)}{||\nabla f(\underline{x}_k)|| ||D_k^{-1}|| ||\nabla f(\underline{x}_k)||} = \frac{\nabla f^T(\underline{x}_k) D_k^{-1} \nabla f(\underline{x}_k)}{||D_k^{-1}|| ||\nabla f(\underline{x}_k)||^2} =
$$
$$
\stackrel{\text{spectral theorem}}{=} \frac{\sum_{i=1}^n \alpha_i \underline{v}_i^T \sum_{j=1}^n \frac{1}{\lambda_j} \underline{v}_j \underline{v}_j^T \sum_{k=1}^n \alpha_k \underline{v}_k}{||D_k^{-1}|| ||\nabla f(\underline{x}_k)||^2} = \frac{\sum_{i=1} \frac{\alpha_i^2}{\lambda_i}}{||D_k^{-1}|| ||\nabla f(\underline{x}_k)||^2} \geq
$$
$$
\geq \frac{\frac{1}{\lambda_1} \sum_{i=1}^n \alpha_i^2}{||D_k^{-1}|| ||\nabla f(\underline{x}_k)||^2} = \frac{||\nabla f(\underline{x}_k)||^2}{\lambda_1 ||D_k^{-1}|| ||\nabla f(\underline{x}_k)||^2} = \frac{1}{||D_k|||D_k^{-1}||} \geq \frac{1}{M}.
$$