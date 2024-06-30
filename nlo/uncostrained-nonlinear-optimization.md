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

> **Proof**: resume...

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

---

### Step length

TO guarantee global convergence, an <u>approximate solution</u> $\alpha_k$ of line search:
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