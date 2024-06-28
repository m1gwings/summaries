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
\phi(\alpha) = \phi(0) + \alpha \phi'(0) + o(\alpha.)
$$
> Suppose $\phi'(0) \neq 0$ first.
Since (_by definition of $o(\cdot)$_) $\frac{o(\alpha)}{\alpha} \rightarrow 0$ for $\alpha \rightarrow 0^+$, there exists $\delta \in (0, \overline{\alpha}]$ s.t., if $\alpha \in (0, \delta)$, then $\frac{o(\alpha)}{\alpha} < |\phi'(0)|$. Furthermore, for every $\alpha \in (0, \overline{\alpha}]$ _resume..._
