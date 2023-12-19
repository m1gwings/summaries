---
theme: summary
---
# Sensitivity analysis in Linear Programming

<div class="author">

Cristiano Migali

</div>

The **goal** of **sensitivity analysis** in linear programming is to evaluate the _"sensitivity"_ of an optimal solution with respect to variations of the model parameters.

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

Let $\underline{b}' = \underline{b} + \delta_k \underline{e}_k$. Observe that $\underline{\overline{c}}_N$ does not depend on the value of $\underline{b}$ , then $\underline{\overline{c}}_N' = \underline{\overline{c}}_N \geq \underline{0}$ and so the **optimality** is satisfied for every (_feasible_) value of $\delta_k$.

The new solution is:
$$
(\underline{x}^*)' = \left[ \begin{matrix}
B^{-1}(\underline{b} + \delta_k \underline{e}_k) \\
\underline{0}
\end{matrix} \right] \text{ .}
$$

It remains **feasible** if $B^{-1}(\underline{b} + \delta_k \underline{e}_k) \geq \underline{0} \iff B^{-1}\underline{b} \geq - \delta_k B^{-1} \underline{e}_k$. These $m$ inequalities (_remember that $B$ is $m \times m$_) define an interval of variation for $\delta_k$ .

The **objective function value** goes from $z_0 = \underline{c}_B^T B^{-1} \underline{b}$ to $z_0' = \underline{c}_B^T B^{-1}(\underline{b} + \delta_k \underline{e}_k)$, then $\Delta z^* = \underline{c}_B^T B^{-1} (\delta_k \underline{e}_k) = \delta_k y_k^*$ where $y_k^* = \underline{c}_B^T B^{-1} \underline{e}_k$.

---

> **Remark**: $z^* = z_0 = \underline{c}_B^T B^{-1} \underline{b} = \underline{c}_B^T B^{-1} (b_1 \underline{e}_1 + ... +  b_k \underline{e}_k + ... + b_m \underline{e}_m)$.

> Then it is clear that $y_k^* = \underline{c}_B^T B^{-1} \underline{e}_k = \frac{\partial z^*}{\partial b_k}$ . We call $y_k^*$ **shadow price** of the **$k$-th resource**, which is the maximum price the company is willing to pay to buy an additional unit of the $k$-th resource. In fact, if $\delta_k = 1$, $\Delta z^* = y_k^*$ and so the company can pay up to $y_k^*$ to get the additional unit wihout decreasing the objective function value (_w. r. t. the original one_).

> **Remark**: remember that by by the proof of the **strong duality theorem** $\underline{\overline{y}} = (\underline{c}_B^T B^{-1})^T$ is an optimal solution to the dual LP; $y_k^*$ is its $k$-th component.

### Variation of $\underline{c}$

Let $\underline{c}' = \underline{c} + \delta_k \underline{e}_k$. Since $\underline{b}' = \underline{b}$, varying $\underline{c}$ doesn't affect the feasibility of the solution.

For what regards optimality, the solution stays optimal as long as:

$$
\underline{\overline{c}}_N'^T = \underline{c}_N'^T - \underline{c}_B'^T B^{-1} N \geq \underline{0}^T \text{ .}
$$

> **Remark**: assuming that the condition above is satisfied, the optimal solution is the same, that is $(\underline{x}^*)' = \underline{x}^*$.

- If $x_k$ is a **non-basic variable**, then:

$$
\begin{matrix}
\underline{\overline{c}}_N'^T = (\underline{c}_N^T + \delta_k \underline{e}_k^T) - \underline{c}_B^T B^{-1} N =\\
= (\underline{c}_N^T - \underline{c}_B^T B^{-1} N) + \delta_k \underline{e}_k^T = \\
= \underline{\overline{c}}_N^T + \delta_k \underline{e}_k^T \geq \underline{0}^T \iff \\
\iff \overline{c}_{k} + \delta_k \geq 0 \iff \delta_k \geq - \overline{c}_k \text{ .}
\end{matrix}
$$

> This provides a new interpretation for the elements of the **vector of reduced costs**: $\overline{c}_k$ is the **maximum decrease** ($- \delta_k \leq \overline{c}_k$) of $c_k$ for which the basis $B$ **remains optimal**.

> In this case $\Delta z^* = 0$ since $(z^*)' = z_0'$ depends only on $\underline{c}_B' = \underline{c}_B$.

- If $x_k$ is a **basic variable**, then:

$$
\begin{matrix}
\underline{\overline{c}}_N'^T = \underline{c}_N^T - (\underline{c}_B^T + \delta_k \underline{e}_k^T) B^{-1} N = \\
= (\underline{c}_N^T - \underline{c}_B^T B^{-1} N) - \delta_k \underline{e}_k^T B^{-1} N = \\
= \underline{\overline{c}}_N^T - \delta_k \underline{\rho}_k^T  \geq \underline{0}^T \text{ where } \underline{\rho}_k^T \text{ is the } k \text{-th row of } B^{-1}N \iff \\
\iff \underline{\overline{c}}_N^T \geq \delta_k \underline{\rho}_k^T \text{ .}
\end{matrix}
$$

> That is, we have $n - m$ inequalities (_remember that $B^{-1} N$ is $m \times (n - m)$_) which define a variation interval for $\delta_k$. Furthermore $\Delta z^* = (\underline{c}_B^T + \delta_k \underline{e}_k^T - \underline{c}_B^T) B^{-1} \underline{b} = \delta_k \underline{e}_k^T B^{-1} \underline{b} = \delta_k x_k^*$ . (It is easy to see (_similar to what we did previously with $y_k^*$_) that $x_k^* = \partial z^* / \partial c_k$) .