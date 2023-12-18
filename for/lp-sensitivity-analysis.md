---
theme: summary
---
# Sensitivity analysis in Linear Programming

<div class="author">

Cristiano Migali

</div>

The **goal** of **sensitivity analysis** in linear programming is to evaluate the _"sensitivity"_ of an optimal solution with respect to variations of the model parameters.

- We call the **shadow price** of the **$i$-th resource** the maximum price the company is willing to pay to buy an additional unit of the $i$-th resource.

## Algebraic formulation

Consider the following LP (_in standard form_):

$$
\begin{matrix}
\min \underline{c}^T \underline{x} \\
\text{s. t. } A \underline{x} = \underline{b} \\
\underline{x} \geq \underline{0}
\end{matrix} \text{ .}
$$

As we know, an **optimal basic feasible solution** $\underline{x}^*$ is of the form:

- $\underline{x}_B^* = B^{-1} \underline{b} \geq \underline{0}$ ;
- $\underline{x}_N^* = \underline{0}$ .

Furthermore:

1. $B^{-1} \underline{b} \geq \underline{0}$ **gurantees** that the solution is **feasible**, while

2. $\underline{\overline{c}}_N^T = \underline{c}_N^T - \underline{c}_B^T B^{-1} N \geq \underline{0}^T$ **gurantees** that the solution is **optimal**.

We want to modify $\underline{b}$ and $\underline{c}$ , keeping (1) and (2) satisfied; then we will compute the corresponding variation in the **objective function value** $z^*$.

### Variation of $\underline{b}$

Let $\underline{b}' = \underline{b} + \delta_k \underline{e}_k$. Observe that $\underline{\overline{c}}_N$ does not depend on the value of $\underline{b}$ , then the **optimality** is satisfied for every (_feasible_) value of $\delta_k$.

The new solution is:
$$
\underline{x}^* = \left[ \begin{matrix}
B^{-1}(\underline{b} + \delta_k \underline{e}_k) \\
\underline{0}
\end{matrix} \right] \text{ .}
$$

It remains **feasible** if $B^{-1}(\underline{b} + \delta_k \underline{e}_k) \geq \underline{0} \iff B^{-1}\underline{b} \geq - \delta_k B^{-1} \underline{e}_k$. These $m$ inequalities (_remember that $B$ has $m$ rows_) define an interval of variation for $\delta_k$ .

---

The **objective function value** goes from $z_0 = \underline{c}_B^T B^{-1} \underline{b}$ to $z_0' = \underline{c}_B^T B^{-1}(\underline{b} + \delta_k \underline{e}_k)$, then $\Delta z^* = \underline{c}_B^T B^{-1} (\delta_k \underline{e}_k) = \delta_k y_k^*$ where $y_k^* = \underline{c}_B^T B^{-1} \underline{e}_k$.

> **Remark**: $z^* = z_0 = \underline{c}_B^T B^{-1} \underline{b} = \underline{c}_B^T B^{-1} (b_1 \underline{e}_1 + ... +  b_k \underline{e}_k + ... + b_m \underline{e}_m)$.

> Then it is clear that $\underline{y}_k^* = \underline{c}_B^T B^{-1} \underline{e}_k = \frac{\partial z^*}{\partial b_k}$ .
