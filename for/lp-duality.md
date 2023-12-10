---
theme: summary
---
# Linear Programming duality

<div class="author">

Cristiano Migali

</div>

## Introduction

The central idea of **Linear Programming duality** (_and duality in general_) is the following: to any minimization (maximization) LP we can associate a closely related maximization (minimization) LP based on the same parameters. The two problems will have different feasible regions and objective functions, but we are guaranteed that the **optimal objective function values coincide**.

### Heuristic motivation

Consider the following (_general_, in _canonical form_) maximization LP:

<div class="centered-definition-expression">

$\max z = \sum_{j=1}^{n} c_j x_j$

s. t.

$\sum_{j=1}^n a_{1j} x_j \leq b_1$ ,
...,
$\sum_{j=1}^n a_{mj} x_j \leq b_m$ ,

$x_j \geq 0 \forall j \in \{ 1, ..., n \}$

</div>

Suppose that we want to **estimate** the **optimal objective function** value $z^*$ by providing better and better **upper bounds**. Let's see how we can do so:

- consider the linear combination (with non-negative coefficients) of the constraints of the LP, that is:

<div class="centered-definition-expression">

$(\sum_{i=1}^m a_{i1} y_i) x_1 + ... +  (\sum_{i=1}^m a_{in} y_i) x_n =$

$= y_1 \sum_{j=1}^n a_{1j} x_j + ... + y_m \sum_{j=1}^n a_{mj} x_j \leq$

$\leq y_1 b_1 + ... + y_m b_m = b_1 y_1 + ... + b_m y_m$

where $y_1, ..., y_m \geq 0$ ;

</div>

- since $x_1, ..., x_n \geq 0$ , if $c_1 \leq \sum_{i=1}^m a_{i1} y_i, ..., c_n \leq \sum_{i=1}^m a_{in} y_i$, then

<div class="centered-definition-expression">

$z = c_1 x_1 + ... + c_n x_n \leq$

$\leq (\sum_{i=1}^m a_{i1} y_i) x_1 + ... +  (\sum_{i=1}^m a_{in} y_i) x_n \leq$

$\leq b_1 y_1 + ... + b_m y_m$ ;

</div>

---

- and clearly, it holds even at optimality:

<div class="centered-definition-expression">

$z^* = c_1 x_1^* + ... + c_n x_n^* \leq$

$\leq (\sum_{i=1}^m a_{i1} \overline{y}_i) x_1^* + ... +  (\sum_{i=1}^m a_{in} \overline{y}_i) x_n^* \leq$

$\leq b_1 \overline{y}_1 + ... + b_m \overline{y}_m$

</div>

> if $\overline{y}_1 \geq 0, ..., \overline{y}_m \geq 0$ are chosen properly.

We've found an upper bound to $z^*$! Now we can reformulate the problem of finding the best upper bound to $z^*$ through the procedure described above as a LP:

- the **coefficients** $y_1 \geq 0, ..., y_m \geq 0$ are the **decision variables**;

- the **upper bound to $z^*$** $\sum_{i=1}^m b_i y_i$ is the **objective function** and we want to **minimize it**;

- the **constraints** are $\sum_{i=1}^m a_{i1} y_i \geq c_1, ..., \sum_{i=1}^m a_{in} y_i \geq c_n$ .

With the usual notation we get:

<div class="centered-definition-expression">

$\min \sum_{i=1}^m b_i y_i$

s. t.

$\sum_{i=1}^m a_{i1} y_i \geq c_1$ ,
...,
$\sum_{i=1}^m a_{in} y_i \geq c_n$ ,

$y_i \geq 0 \forall i \in \{ 1, ..., m \}$ .

</div>

Now let's define the **dual LP** formally.

### Definition

-  Given a **maximization LP in canonical form** (we call it the **primal LP (P)**):

<div class="centered-definition-expression">

$\max \underline{c}^T \underline{x}$
s. t.
$A \underline{x} \leq \underline{b}$ ,
$\underline{x} \geq \underline{0}$

</div>

> the corresponding **dual LP (D)** is:

<div class="centered-definition-expression">

$\min \underline{b}^T \underline{y}$
s. t.
$A^T \underline{y} \geq \underline{c}$ ,
$\underline{y} \geq \underline{0}$ .

</div>

---

> **Remark**: it is easy to check that the defintion for **(D)** matches exactly the one that we got in the _Heuristic motivation_ paragraph (_just write it in matricial form_).

- We say that $\leq$ is the **natural direction** for **inequality constraints** of a maximization LP, while $\geq$ is the natural direction for inequality constraints of a minimization LP.

## Properties

- The **dual of a LP in standard form** is:

$$
\begin{matrix}
\min \underline{c}^T \underline{x} \\
\text{s. t. } A \underline{x} = \underline{b} \\
\underline{x} \geq \underline{0}
\end{matrix}

\: \equiv \:\:

\begin{matrix}
- \max - \underline{c}^T \underline{x} \\
\text{s. t. } A \underline{x} \leq \underline{b} \\
-A \underline{x} \leq -\underline{b} \\
\underline{x} \geq \underline{0}
\end{matrix}

\: \rightarrow^{(D)} \:\:

\begin{matrix}
- \min \underline{b}^T \underline{y}_1 - \underline{b}^T \underline{y}_2 \\
\text{s. t. } A^T \underline{y}_1 \geq - \underline{c} \\
-A^T \underline{y}_2 \geq -\underline{c} \\
\underline{y}_1, \underline{y}_2 \geq \underline{0}
\end{matrix}

\: \equiv \:\:
$$

$$
\: \equiv \:\:

\begin{matrix}
- \min - \underline{b}^T (\underline{y}_2 - \underline{y}_1) \\
\text{s. t. } A^T (\underline{y}_2 - \underline{y}_1) \leq \underline{c} \\
\underline{y}_1, \underline{y}_2 \geq \underline{0}
\end{matrix}

\: \equiv_{\underline{y} \: = \: \underline{y}_2 - \underline{y}_1} \:\:

\begin{matrix}
- \min - \underline{b}^T \underline{y} \\
\text{s. t. } A^T \underline{y} \leq \underline{c} \\
\underline{y} \in \mathbb{R}^m
\end{matrix}

\: \equiv \:\:

\begin{matrix}
\max \underline{b}^T \underline{y} \\
\text{s. t. } A^T \underline{y} \leq \underline{c} \\
\underline{y} \in \mathbb{R}^m
\end{matrix} \text{ .}
$$ 

- The **dual of the dual problem** coincides with the **primal problem**:

$$
\begin{matrix}
\min \underline{b}^T \underline{y} \\
\text{s. t. } A^T \underline{y} \geq \underline{c} \\
\underline{y} \geq 0
\end{matrix}

\: \equiv \:\:

\begin{matrix}
- \max - \underline{b}^T \underline{y} \\
\text{s. t. } - A^T \underline{y} \leq - \underline{c} \\
\underline{y} \geq \underline{0}
\end{matrix}

\: \rightarrow^{(D)} \:\:

\begin{matrix}
- \min - \underline{c}^T \underline{x} \\
\text{s. t. } - (A^T)^T \underline{x} \geq - \underline{b} \\
\underline{x} \geq \underline{0}
\end{matrix}

\: \equiv \:\:

\begin{matrix}
\max \underline{c}^T \underline{x} \\
\text{s. t. } A \underline{x} \leq \underline{b} \\
\underline{x} \geq \underline{0}
\end{matrix} \text{ .}
$$

- The following **general transformation rules** hold:

<style>
.table-container {
    display: flex;
    justify-content: center;
}
</style>

<div class="centered-definition-expression">
<div class="table-container">

Rule                                                                    |Primal LP **(P)**                                          | Dual LP **(D)**
------------------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------
**type**                                                                | $\max$                                                    | $\min$
**number of variables**                                                 | $n$                                                       | $m$ 
**number of constraints**                                               | $m$                                                       | $n$
**coefficients of the objective function**                              | $\underline{c}$                                           | $\underline{b}$
**r.h.s of the constraints**                                            | $\underline{b}$                                           | $\underline{c}$
**constraints matrix**                                                  | $A$                                                       | $A^T$
**constraint  with equality $\implies$ variable $\in \mathbb{R}$**      | $\sum_{j=1}^n a_{ij} x_j = b_i$                           | $y_i \in \mathbb{R}$ (unrestricted in sign)
**constraint in natural direction $\implies$ variable $\geq 0$**        | $\sum_{j=1}^n a_{ij} x_j \leq b_i$ (if **(P)** is $\max$) | $y_i \geq 0$
**constraint not in natural direction $\implies$ variable $\leq 0$**    | $\sum_{j=1}^n a_{ij} x_j \geq b_i$ (if **(P)** is $\max$) | $y_i \leq 0$
</div>
</div>

---

<div class="centered-definition-expression">
<div class="table-container">

Rule                                                                    |Primal LP **(P)**                                          | Dual LP **(D)**
------------------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------
**variable $\in \mathbb{R} \implies$ constraint with equality**         | $x_j \in \mathbb{R}$ (unrestricted in sign)               | $\sum_{i=1}^m a_{ij} y_i = c_j$
**variable $\geq 0 \implies$ constraint in natural direction**          | $x_j \geq 0$                                              | $\sum_{i=1}^m a_{ij} y_i \geq c_j$ (if **(P)** is $\max$)
**variable $\leq 0 \implies$ constraint not in natual direction**        | $x_j \leq 0$                                              | $\sum_{i=1}^m a_{ij} y_i \leq c_j$ (if **(P)** is $\max$)
</div>
</div>

> **Proof**: it is just a matter of applying the equivalences that we've already seen to a general maximization LP (then we get the results also for a general minimization LP by reading the equivalences in the opposite direction, since the dual of the dual is the primal).

> Let

$$
\underline{x} = \left[ \begin{matrix} \underline{x}_l \\ \underline{x}_u \\ \underline{x}_g \end{matrix} \right],
\underline{c} = \left[ \begin{matrix} \underline{c}_l \\ \underline{c}_u \\ \underline{c}_g \end{matrix} \right],
\underline{b}  = \left[ \begin{matrix} \underline{b}_l \\ \underline{b}_e \\ \underline{b}_g \end{matrix} \right],
A = \left[ \begin{matrix}
A_{ll} & A_{lu} & A_{lg} \\
A_{el} & A_{eu} & A_{eq} \\
A_{gl} & A_{gu} & A_{gg}
\end{matrix} \right] \text{ .}
$$

> We can express a general maximization LP as:

$$
\begin{matrix}
\max \underline{c}_l^T \underline{x}_l + \underline{c}_u^T \underline{x}_u + \underline{c}_g^T \underline{x}_g \\
\text{s. t. } A_{ll} \underline{x}_l + A_{lu} \underline{x}_u + A_{lg} \underline{x}_g \leq \underline{b}_l \\
A_{el} \underline{x}_l + A_{eu} \underline{x}_u + A_{eg} \underline{x}_g = \underline{b}_e \\
A_{gl} \underline{x}_l + A_{gu} \underline{x}_u + A_{gg} \underline{x}_g \geq \underline{b}_g \\
\underline{x}_l \leq \underline{0}, \underline{x}_u \text{unrestricted}, \underline{x}_g \geq \underline{0}
\end{matrix}

\: \equiv_{\underline{x}_u \: = \: \underline{x}_u^+ - \underline{x}_u^-} \:\:

\begin{matrix}
\max - \underline{c}_l^T (- \underline{x}_l) + \underline{c}_u^T \underline{x}_u^+ - \underline{c}_u^T \underline{x}_u^- + \underline{c}_g^T \underline{x}_g \\
\text{s. t. } - A_{ll} (- \underline{x}_l) + A_{lu} \underline{x}_u^+ - A_{lu} \underline{x}_u^- + A_{lg} \underline{x}_g \leq \underline{b}_l \\
- A_{el} (- \underline{x}_l) + A_{eu} \underline{x}_u^+ - A_{eu} \underline{x}_u^- + A_{eg} \underline{x}_g \leq \underline{b}_e \\
A_{el} (- \underline{x}_l) -A_{eu} \underline{x}_u^+ + A_{eu} \underline{x}_u^- -A_{eg} \underline{x}_g \leq -\underline{b}_e \\
A_{gl} (- \underline{x}_l) -A_{gu} \underline{x}_u^+ + A_{gu} \underline{x}_u^- -A_{gg} \underline{x}_g \leq -\underline{b}_g \\
-\underline{x}_l \geq \underline{0}, \underline{x}_u^+ \geq \underline{0}, \underline{x}_u^- \geq \underline{0}, \underline{x}_g \geq \underline{0}
\end{matrix}

\: \rightarrow^{(D)} \:\:
$$

$$
\: \rightarrow^{(D)} \:\:

\begin{matrix}
\min \underline{b}_l^T \underline{y}_l + \underline{b}_e^T \underline{y}_u^+ - \underline{b}_e^T \underline{y}_u^- - \underline{b}_g^T (- \underline{y}_g) \\
\text{s. t. } -A_{ll}^T \underline{y}_l -A_{el}^T \underline{y}_u^+ + A_{el}^T \underline{y}_u^- + A_{gl}^T (- \underline{y}_g) \geq - \underline{c}_l \\
A_{lu}^T \underline{y}_l + A_{eu}^T \underline{y}_u^+ - A_{eu}^T \underline{y}_u^- - A_{gu}^T (- \underline{y}_g) \geq \underline{c}_u \\
-A_{lu}^T \underline{y}_l - A_{eu}^T \underline{y}_u^+ + A_{eu}^T \underline{y}_u^- + A_{gu}^T (- \underline{y}_g) \geq - \underline{c}_u \\
A_{lg}^T \underline{y}_l + A_{eg}^T \underline{y}_u^+ - A_{eg}^T \underline{y}_u^- - A_{gg}^T (- \underline{y}_g) \geq \underline{c}_g \\
\underline{y}_l \geq \underline{0}, \underline{y}_u^+ \geq \underline{0}, \underline{y}^- \geq \underline{0}, - \underline{y}_g \geq \underline{0}
\end{matrix}

\: \equiv_{\underline{y}_u \: = \: \underline{y}_u^+ - \underline{y}_u^-} \:\:

\begin{matrix}
\min \underline{b}_l^T \underline{y}_l + \underline{b}_e^T \underline{y}_u + \underline{b}_g^T \underline{y}_g \\
\text{s. t. } A_{ll}^T \underline{y}_l + A_{el}^T \underline{y}_u + A_{gl}^T \underline{y}_g \leq \underline{c}_l \\
A_{lu}^T \underline{y}_l + A_{eu}^T \underline{y}_u + A_{gu}^T \underline{y}_g = \underline{c}_u \\
A_{lg}^T \underline{y}_l + A_{eg}^T \underline{y}_u + A_{gg}^T \underline{y}_g \geq \underline{c}_g \\
\underline{y}_l \geq \underline{0}, \underline{y}_u \text{unrestricted}, \underline{y}_g \leq \underline{0}
\end{matrix}
$$

- **Weak duality theorem**: given
$$
\text{(P)}
\begin{matrix}
\min z = \underline{c}^T \underline{x} \\
\text{s. t. } A \underline{x} \geq \underline{b} \\
\underline{x} \geq \underline{0}
\end{matrix}

\: \rightarrow^{(D)} \:\:

\text{(D)}

\begin{matrix}
\max w = \underline{b}^T \underline{y} \\
\text{s. t. } A^T \underline{y} \leq \underline{c} \\
\underline{y} \geq \underline{0}
\end{matrix}
$$

> with $X = \{ \underline{x} \in \mathbb{R}^n \mid A \underline{x} \geq \underline{b}, \underline{x} \geq \underline{0}\} \neq \emptyset$ and $Y = \{ \underline{y} \in \mathbb{R}^m \mid A^T \underline{y} \leq \underline{c}, \underline{y} \geq \underline{0} \} \neq \emptyset$, (_cont'd_)

---

> (_cont'd_) then, for every feasible solution $\underline{x} \in X$  of (P) and every feasible solution $\underline{y} \in Y$ of (D) we have $\underline{b}^T \underline{y} \leq \underline{c}^T \underline{x}$.

> **Proof**: $\underline{b}^T \underline{y} \leq \underline{x}^T A^T \underline{y}$ since $A \underline{x} \geq \underline{b}$ and $\underline{y} \geq \underline{0}$ , $\underline{x}^T A^T \underline{y} \leq \underline{x}^T \underline{c}$ since $A^T \underline{y} \leq \underline{c}$ and $\underline{x} \geq \underline{0}$. The proof follows by the commutative property of scalar product.

- **Corollary**: if $\underline{x}$ is a feasible solution of (P), $\underline{y}$ is a feasible solution of (D), and $\underline{c}^T \underline{x} = \underline{b}^T \underline{y}$ , then $\underline{x}$ is optimal for (P) and $\underline{y}$ is optimal for (D).

- **Strong duality theorem**: (_we will adopt the notation used in the statement of the Weak duality theorem_) if $\{ \underline{c}^T \underline{x} \mid \underline{x} \in X \}$ admits minimum, then there exist $\underline{x}^* \in X$ and $\underline{y}^* \in Y$ s. t. **$\underline{c}^T \underline{x}^* = \underline{b}^T \underline{y}$** .

> **Proof**: First of all remember that we can always write (P) in standard form:

$$
\begin{matrix}
\min z = \underline{c}^T \underline{x} \\
\text{s. t. } A \underline{x} \geq \underline{b} \\
\underline{x} \geq \underline{0}_n
\end{matrix}

\: \equiv \:\:

\begin{matrix}
\min z = \underline{c}^T \underline{x} + \underline{0}_m^T \underline{s} \\
\text{s. t. } A \underline{x} - I_m \underline{s} = \underline{b} \\
\underline{x} \geq \underline{0}_n, \underline{s} \geq \underline{0}_m
\end{matrix} \text{ .}
$$

> By assumption (P) admits an optimal solution, hence, (as we know) the Simplex method with Bland's rule can provide one after a finite number of iterations. Furthermore, due to the termination condition of the Simplex method, the vector of reduced costs associated with such solution must be non-negative. Let's write everything in formulas: the Simplex method provides

$$
\underline{x}^* = \left[ \begin{matrix} \underline{x}_{B_A}^* & \underline{x}_{N_A}^* & \underline{x}_{B_{-I_m}}^* & \underline{x}_{N_{-I_m}}^* \end{matrix} \right]^T
\text{ where } \underline{x}_B^* = \left[ \begin{matrix} \underline{x}_{B_A}^* \\ \underline{x}_{B_{-I_m}}^* \end{matrix} \right], \underline{x}_N^* = \left[ \begin{matrix} \underline{x}_{N_A}^* \\ \underline{x}_{N_{-I_m}}^* \end{matrix} \right]
$$

$$
\underline{c}_B = \left[ \begin{matrix} \underline{c}_{B_A} \\ \underline{c}_{B_{-I_m}} \end{matrix} \right],
\underline{c}_N = \left[ \begin{matrix} \underline{c}_{N_A} \\ \underline{c}_{N_{-I_m}} \end{matrix} \right],
B = \left[ \begin{matrix} B_A & B_{-I_m} \end{matrix} \right], N = \left[ \begin{matrix} N_A & N_{-I_m} \end{matrix} \right],
$$

$$
\text{with } \underline{x}_B^* = B^{-1} \underline{b}, \underline{x}_N^* = \underline{0}_n,
\left[ \begin{matrix} B_A & N_A & B_{-I_m} & N_{-I_m} \end{matrix} \right] = \left[ \begin{matrix} A & -perm(I_m) \end{matrix} \right],
$$

> (_$perm(I_m)$ is a matrix with the columns of $I_m$, potentially in a different order_) such that

$$
\underline{\overline{c}}_N^T = \underline{c}_N^T - (\underline{c}_B^T B^{-1}) N \geq \underline{0} \text{ .}
$$

> **Remark**: as we know a basic feasible solution provided by the simplex method is determined by a basis, that is, a set of linearly independent columns of $\left[ \begin{matrix} A & -I_m \end{matrix} \right]$ (_in this case_). The linearly independent columns can be either columns of $A$ or $-I_m$, then, without loss of generality (_by renaming variables_) we can assume that the basis is composed by the first $k$ columns of $A$ and the first $l$ columns of $-perm(I)_m$, with $k + l = m$.

---

> Now let $\underline{\overline{y}} = (B^{-1})^T \underline{c}_B \in \mathbb{R}^m$ (_since $B \in \mathbb{R}^{m \times m}$_). First of all we will prove that $\underline{\overline{y}}$ is a feasible solution of (D):

$$
\underline{0} \leq \underline{\overline{c}}_N^T = \underline{c}_N^T - \underline{\overline{y}}^T N \iff N^T \underline{\overline{y}} \leq \underline{c}_N \text{ ;}
$$

> furthermore

$$
\underline{0} = \underline{\overline{c}}_B^T = \underline{c}_B^T - \underline{\overline{y}}^T B \iff B^T \underline{\overline{y}} = \underline{c}_B \text{ .}
$$

> Then

$$
\left[ \begin{matrix} A^T \\ -perm(I_m) \end{matrix} \right] \underline{\overline{y}} = \left[ \begin{matrix} B_A^T \\ N_A^T \\ B_{-I_m}^T \\ N_{-I_m}^T \end{matrix} \right] \underline{\overline{y}} = \left[ \begin{matrix} B_A^T \underline{\overline{y}} \\ N_A^T \underline{\overline{y}} \\ B_{-I_m}^T \underline{\overline{y}} \\ N_{-I_m}^T \underline{\overline{y}} \end{matrix} \right] \leq \left[ \begin{matrix} \underline{c}_{B_A} \\ \underline{c}_{N_A} \\ \underline{c}_{B_{-I_m}} \\ \underline{c}_{N_{-I_m}} \end{matrix} \right] \text{ .}
$$

> Now observe that, by how we have defined the variables $\underline{x}_{B_A}, \underline{x}_{N_A}, \underline{x}_{B_{-I_m}}, \underline{x}_{N_{-I_m}}$ it follows that $\left[ \begin{matrix} \underline{c}_{B_A} & \underline{c}_{N_A} \end{matrix}\right]^T = \underline{c}^T$ and $\left[ \begin{matrix} \underline{c}_{B_{-I_m}} & \underline{c}_{N_{-I_m}} \end{matrix}\right]^T = \underline{0}_n^T$, then, the inequality above is equivalent to:

$$
A^T \underline{\overline{y}} \leq \underline{c} \: \land \: \underline{\overline{y}} \geq \underline{0} 
$$

> (_the second inequality follows from $-perm(I_m) \underline{\overline{y}} \leq \underline{0}$_). That is, $\underline{\overline{y}}$ is a feasible solution of (D) (as we wanted to prove).
