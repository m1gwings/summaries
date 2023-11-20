# The Simplex method

<div class="author">

Cristiano Migali

</div>

## Basic definitions

### Linear Programming (LP)

- A **Linear Programming** (**LP**) **problem** is an optimization problem with the following structure:

<div class="centered-definition-expression">

$\min$ _(or_ $\max$_)_ $f(\underline{x})$<br>
s. t. $\underline{x} \in X \subseteq \mathbb{R}^n$

</div>

> where:
>
> - the **objective function** $f : X \rightarrow \mathbb{R}$ is linear;
> - the **feasible region** is $X = \{ \underline{x} \in \mathbb{R}^n \mid g_i(\underline{x}) \: r_i \: 0, i \in \{ 1, ..., m \}$, $r_i \in \{ =, \geq, \leq \} \}$ with $g_i : \mathbb{R}^n \rightarrow \mathbb{R}$ linear, for $i \in \{ 1, ..., m \}$.

- $\underline{x}^* \in X$ is an **optimal solution** for a LP problem if $f(\underline{x}^*) \leq f(\underline{x})$, $\forall \underline{x} \in X$ if we're **minimizing** $f(\underline{x})$ or $f(\underline{x}^*) \geq f(\underline{x})$, $\forall \underline{x} \in X$ if we're **maximizing** it instead.

- Thanks to the **linearity** of the involved functions and the structure of the feasible region, we can write a LP problem in the so-called **general form**:

<div class="centered-definition-expression">

$\min$ _(or_ $\max$_)_ $z = \underline{c}^T \underline{x}$
s. t.
$A_1 \underline{x} \geq \underline{b}_1$;
$A_2 \underline{x} \leq \underline{b}_2$;
$A_3 \underline{x} = \underline{b}_3$;
$x_j \geq 0$ $\forall j \in J \subseteq \{ 1, ..., n \}$.

</div>

> **Remark**: The $x_j$_s_ with $j \not \in J$ are intended to be **free** (uncostrained).

- We say that a LP is in **standard form** if it has the following structure:

<div class="centered-definition-expression">

$\min z = \underline{c}^T \underline{x}$
s. t. $A \underline{x} = \underline{b}$;
$\underline{x} \geq 0$.

</div>

---

## Basic properties

### Equivalence between general and standard form of LP

First of all observe that a LP in standard form is in general form.
Now, through the following 4 **transformation rules**, we'll see how it is possible to bring a LP in general form into an equivalent LP in standard form:

1. From _max_ to _min_: $\max \underline{c}^T \underline{x} = - \min(- \underline{c}^T \underline{x})$;

2. from $\leq$ to $=$ : $\: \: \underline{a}^T \underline{x} \leq b \iff \begin{cases}
\underline{a}^T \underline{x} + s = b \\
s \geq 0 
\end{cases}$ where s is a **slack** variable;

3. from $\geq$ to $=$ : $\: \: \underline{a}^T \underline{x} \geq b \iff \begin{cases}
\underline{a}^T \underline{x} - s = b \\
s \geq 0 
\end{cases}$ where s is a **surplus** variable;

4. from $x_j$ free to $x_j \geq 0$: $\begin{cases}
x_j = x_j^+ + x_j^-\\
x_j^+, x_j^- \geq 0
\end{cases}$ .
