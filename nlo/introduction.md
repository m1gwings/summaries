---
marp: true
theme: summary
math: mathjax
---
# Introduction

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Edoardo Amaldi_)

</div>

**Optimization** is a branch of applied mathematics which deals with problems of this kind: given $X \subseteq \mathbb{R}^n$ and $f : X \rightarrow \mathbb{R}$ to be minimized, find an optimal solution $\underline{x}^* \in X$, i.e., such that:
$$
f(\underline{x}^*) \leq f(\underline{x}) \ \forall \underline{x} \in X.
$$

In particular, we can express the **general optimization problem** as follows:

$$
\begin{matrix}
\min f(\underline{x}) \\
\text{s.t. } g_i(\underline{x}) \leq 0 \ \forall i \in \{ 1, \ldots, m \} \\
\underline{x} \in S \subseteq \mathbb{R}^n
\end{matrix}.
$$

The algebraic and set constraints define the **feasible region**:

$$
X = S \cap \{ \ \underline{x} \in \mathbb{R}^n \ | \ g_i(\underline{x}) \leq 0 \ \forall i \in \{ 1, \ldots, m \} \ \}.
$$

We call $f : S \rightarrow \mathbb{R}$ **objective function**.

Observe that the expression above is without loss of generality:
- we can translate _maximization_ problems into _minimization_ problems:
$$
\max\{ f(\underline{x}) \ | \ \underline{x} \in X \} = - \min\{ -f(\underline{x}) \ | \ \underline{x} \in X \}.
$$
- we can translate _equality_ constraints into _inequality_ constraints:
$$
\{ \underline{x} \in S \ | \ g(\underline{x}) = 0 \} = \{ \underline{x} \in S \ | \ g(\underline{x}) \leq 0 \land -g(\underline{x}) \leq 0 \}.
$$

- A feasible solution $\underline{x}^* \in X$ is a **global minimum** if:
$$
f(\underline{x}^*) \leq f(\underline{x}) \ \forall \underline{x} \in X.
$$

- A feasible solution $\overline{\underline{x}} \in X$ is a **local minimum** if $\exits \epsilon > 0$ such that:
$$
f(\underline{\overline{x}}) \leq f(\underline{x}) \ \forall \underline{x} \in X \cap \mathcal{N}_\epsilon(\underline{\overline{x}})
$$
> where $\mathcal{N}_\epsilon(\underline{\overline{x}}) = \{ \underline{x} \in X \ | \ ||\underline{x} - \underline{\overline{x}}|| \leq \epsilon \}$.

---

<style>

table {
    margin: auto;
}

td {
    padding: 0.5cm;
    padding-right: 0.7cm;
    padding-left: 0.7cm;
    text-align: center;
}

</style>

We can classify optimization problems according to the properties of $f$, $g_i$ and $S$.

| $f$                     | $g_i$  | $S$                                                                            | problem type                |
|-------------------------|--------|--------------------------------------------------------------------------------|-----------------------------|
| linear                  | linear | $S = \mathbb{R}^n$                                                             | Linear Programming (LP)     |
| linear                  | linear | $S \subseteq \mathbb{Z}^n$                                                     | Integer LP (ILP)            |
| linear                  | linear | $S \subseteq \mathbb{Z}^{n_1} \times \mathbb{R}^{n_2}$<br>with $n = n_1 + n_2$ | Mixed Integer LP (MILP)     |
| at least one non-linear |        | $S \subseteq \mathbb{R}^n$                                                     | Nonlinear Programming (NLP) |
| at least one non-linear |        | $S \subseteq \mathbb{Z}^{n_1} \times \mathbb{R}^{n_2}$<br>with $n = n_1 + n_2$ | Mixed Integer NLP (MINLP)   |
