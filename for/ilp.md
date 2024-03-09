---
marp: true
theme: summary
math: mathjax
---
# Integer Linear Programming

<div class="author">

Cristiano Migali

</div>

## Basic definitions

- An **Integer Linear Programming** (**ILP**) **problem** is an optimizaztion problem of the form:

$$
\begin{matrix}
\min \underline{c}^T \underline{x} \\
\text{s. t. } A \underline{x} \geq \underline{b} \\
\underline{x} \geq \underline{0} \text{ with } \underline{x} \in \mathbb{Z}^n \text{ .}
\end{matrix}
$$

> Furthermore:
> - if we have the additional constraint that $x_j \in \{ 0, 1 \}$ for all $j$, then we say that the **LP** is **binary**;
> - if not all $x_j$s are constrained to be integer, we say that the LP is a **mixed integer LP**.

- The feasible region of an ILP is a **lattice**.

- Consider the general ILP (_in canonical form and we maximize_)

$$
\text{(ILP)} \begin{matrix}
z_{ILP} = \max \underline{c}^T \underline{x} \\
\text{s. t. } A \underline{x} \leq \underline{0} \\
\underline{x} \geq \underline{0}, \underline{x} \in \mathbb{Z}^n \text{.}
\end{matrix}
$$

> The problem

$$
\text{(LP)} \begin{matrix}
z_{LP} = \max \underline{c}^T \underline{x} \\
\text{s. t. } A \underline{x} \leq \underline{0} \\
\underline{x} \geq \underline{0}
\end{matrix}
$$

> is the **linear (continuous) relaxation** of the original ILP.

---

## Basic properties

1. The integrality condition $\underline{x} \in \mathbb{Z}^n$ can't be expressed as $g(\underline{x}) \: r \: 0$ with $r \in \{ =, \leq, \geq \}$ and $g$ linear. That is an **ILP** is not an **LP**. (_This follows easily by applying the linearity of $g$ for every kind of $r$_).

2. For any ILP with $\max$, we have **$z_{ILP}^* \leq z_{LP}^*$** , that is, $z_{LP}^*$ is an **upper bound** on the optimal value of (ILP). (_This follows trivially from the fact that the feasible region of the linear relaxation contains the feasible region of the original ILP_). 
An analogous result holds of course for ILPs with $\min$.

3. If an **optimal solution** of the **linear relaxation** is **integer**, then it is **also an optimal solution of (ILP)**. (_This follows by property 2_).

## Well-known problems formulable as ILPs

- The **binary knapsack problem** is defined as follows: we have $n$ objects, each object has a value $v_j$ and a weight $w_j$, we have a knapsack with capacity $b$ ; we want to determine a **subset of objects** that maximizes the total value, while respecting the knapsack capacity. (_The formulation as ILP is trivial_).

> **Remark**: the binary knapsack problem is NP-hard.

- The **assignment problem** is defined as follows: given $m$ machines and $n$ jobs with a cost $c_{ij}$ of assigning job $j$ to machine $i$ we want to determine an **assignment** of jobs to the machines so as to minimize the total cost, while assigning at least one job per machine and at most one machine for each job.

> The **decision variables** are: $x_{ij} = 1$ if we assign job $j$ to machine $i$, $0$ otherwise $\forall i \in \{ 1, ..., m \}, j \in \{ 1, ..., n \}$.

> The **ILP formulation** is:

$$
\begin{matrix}
\min \sum_{i=1}^m \sum_{j=1}^n c_{ij} x_{ij} \\
\text{s. t. } \sum_{j=1}^n x_{ij} \geq 1 \forall i \in \{ 1, ..., m \} \text{ (at least one job per machine)} \\
\sum_{i=1}^m x_{ij} \leq 1 \forall j \in \{ 1, ..., m \} \text{ (at most one machine per job)} \\
x_{ij} \in \{ 0, 1 \} \forall i \in \{1,...,m\}, j \in \{1,...,n\} \text{ .}
\end{matrix}
$$

- The **transportation problem** is defined as follows: given $m$ production plants and $n$ clients; $c_{ij}$ is the transportation cost of one unit of product from plant $i$ to client $j$, $p_i$ is the production capacity of plant $i$, $d_j$ is the demand of client $j$ and $q_{ij}$ is the maximum amount that can be transported from plant $i$ to client $j$. We want to determine a **transportation plan** that minimizes total costs while satisfying plant capacity and client demands. (_The formulation as ILP is straight forward_).

---

> **Remark**: by comparing the ILP formulations of both, it is easy to see that the **assignment problem is a special kind of transportation problem**.

- The **scheduling problem** is defined as follows: given $m$ machines, $n$ jobs each with a deadline $d_j$; $p_{jk} \geq 0$ is the processing time of job $j$ on machine $k$. We assume that each job must be processed once on each machine following the order of the machine indices: $1, 2, ..., m$. We want to determine an **optimal sequence** in which to process the jobs so as to minimize the total completion time while satisfying the deadlines.

> **Remark**: the total completion time is the _maximum_ among the completion times of each of the jobs.

> The **decision variables** are:
> - $t_{jk}$ : the time at which machine $k$ starts processing job $j$ for every $j \in \{ 1, ..., n \}$, $k \in \{ 1, ..., m \}$;
> - $t$ : is an upperbound to the total completion time of the project;
> - $y_{ijk} = 1$ if we process job $i$ before job $j$ on machine $k$, $0$ otherwise for every $k \in \{ 1, ..., m \}$, $i, j \in \{ 1, ..., n \}$, $i < j$.

> The **ILP formulation** is:

$$
\begin{matrix}
\min t \\
\text{s. t. } t_{jm} + p_{jm} \leq t \forall j \in \{ 1, ..., n \} \text{ (} t \text{ is an upperbound to the total completion time)} \\
t_{jm} + p_{jm} \leq d_j \forall j \in \{ 1, ..., n \} \text{ (the deadlines are satisfied)} \\
t_{jk} + p_{jk} \leq t_{j(k+1)} \forall j \in \{ 1, ..., n \}, \forall k \in \{ 1, ..., m - 1 \} \text{ (order of processing)} \\
t_{ik} + p_{ik} \leq t_{jk} + (1 - y_{ijk}) M \text{ where } M = \max_j d_j \text{ and} \\
t_{jk} + p_{jk} \leq t_{ik} + y_{ijk} M \:  \forall k \in \{ 1, ..., m \}, i, j \in \{1, ..., n\}, i < j \text{ (no overlapping executions)} \\
t_{jk} \geq 0 \forall j \in \{ 1, ..., n \}, k \in \{ 1, ..., m \}, t \geq 0, y_{ijk} \in \{0, 1\} \forall k \in \{ 1, ..., m \}, i, j \in \{ 1, ..., n \}, i < j \text{.}
\end{matrix}
$$

---

## More sophisticated properties

- If in a **transportation problem** $p_i$, $d_{ij}$ and $q_{ij}$ are integer, all **the basic feasible solutions (vertices) of its linear relaxation are integer**.

> **Idea of the proof**: This depends on the fact that the $(mn + n + m) \times mn$ constraint matrix (_in canonical form_) $A$ has a special structure: its elements are $a_{ij} \in \{ -1, 0, 1 \}$ with exactly $3$ non-zero coefficients per column. Then, it can be proved that $A$ is **totally unimodular**, that is $|Q| \in \{ -1, 0, 1 \}$, for any square sub-matrix $Q$ of $A$.

> By the laplace expansion of the determinant it is clear that this property holds even when we put the problem in standard form, adding the slack variables and transforming $A$ into $A'$ (we are just adding columns of the identity matrix).

> Then the optimal basic feasible solution to the linear relaxation is:

$$
\underline{x}^* = \left[ \begin{matrix}
B^{-1} \underline{b} \\
\underline{0}
\end{matrix} \right] \text{ where }
B^{-1} = \frac{1}{|B|} \left[\begin{matrix}
\alpha_{11} & ... & \alpha_{1n} \\
... & ... & ... \\
\alpha_{n1} & ... & \alpha_{nn}
\end{matrix}\right]
$$

> and $\alpha_{ij} = (-1)^{i+j} |M_{ij}|$ with $M_{ij}$ being the square sub-matrix obtained from $B$ by removing row $i$ and column $j$. Now observe that, since $B$ is integer, all $\alpha_{ij}$ are integers (_by the laplace expansion of the determinant_). Furthermore, for what we discussed above $|B| \in \{ -1, 1 \}$ (_it can't be $|B| = 0$ since $B$ is non-singular_) and so it must be that $\underline{x}^*$ is integer since $\underline{b}$ is also integer.

- The **optimal solution** of the **linear relaxation** of the **knapsack problem** can be computed by a **linear time** (in the number of objects) **algorithm** where we sort the objects based on their _value over weight_ ratio and fill the knapsack starting with the best object and taking for each as much as we can (remember that, since it is the continuos relaxation, we can also take fractions of objects).

> **Idea of the proof**: we will provide an idea of the proof for a (_equivalent_) variant of the so-called **continuos knapsack** problem:

$$
\begin{matrix}
\min c_1 y_1 + ... + c_n y_n \\
\text{s. t. } U_1 y_1 + ... + U_n y_n \geq U \\
0 \leq y_i \leq 1 \forall i \in \{ 1, ..., n \} \text{ .}
\end{matrix}
$$

> First of all, by performing the change of variable $x_i = U_i y_i$ we get the equivalent formulation:

$$
\begin{matrix}
\min r_1 x_1 + ... + r_n x_n \\
\text{s. t. } x_1 + ... + x_n \geq U \\
0 \leq x_i \leq U_i \forall i \in \{ 1, ..., n \} \text{ where } r_i = \frac{c_i}{U_i} \text{.}
\end{matrix}
$$

---

> Now assume WLOG that **(\*)** $r_1 \leq ... \leq r_n$. It is not too hard to show that the **greedy solution** described has this structure: $x_1^* = U_1,$ $...,$ $x_{k-1}^* = U_{k-1},$ $x_k^* \in [ 0, U_k ],$ $x_{k+1}^* = 0,$ $...,$ $x_{n}^* = 0$ for some $k \in \{ 1, ..., n \}$. Then, for every fesible solution $t_i$ we have that $t_1 \leq x_1^*,$ $...,$ $t_{k-1} \leq x_{k_1}^*,$ $t_{k+1} \geq x_{k+1}^*,$ $...,$ $t_n \geq x_n^*$. Then, by assumption **(\*)**: $c(\underline{t}) - c(\underline{x}) = \sum_{i=1}^n r_i (t_i - x_i^*) \geq r_k (\sum_{i=1}^n t_i - \sum_{i=1}^n x_i^*) \geq 0$. The last inequality follows from the fact that $\sum_{i=1}^n t_i \geq U$ since $\underline{t}$ is feasible and it can be proved that $\sum_{i=1}^n x_i^* = U$.

## Algorithms

### Branch-and-bound method

The **branch-and-bound method** is an optimization technique which we can apply to a generic optimization problem:

$$
\min\{ c(\underline{x}) \mid \underline{x} \in X \} \text{.}
$$

The idea behind it is to reduce the solution of a difficult problem to that of a sequence of simpler **subproblems** by (recursively) **partitioning** the feasible region $X$.

It is composed of two main operations: **branching** and **bounding**.

#### Branching

**Branching** consists in partitioning the feasible region $X$ into $X = X_1 \cup ... \cup X_k$ (with $X_i \cap X_j = \emptyset$ for each pair $i \neq j$) according to a **branching criterion**.

Let $z_i = min\{ c(\underline{x}) \mid \underline{x} \in X_i \}$ for $i \in \{ 1, ..., k\}$. Then it is clear that $z = \min\{ c(\underline{x}) \mid \underline{x} \in X \}$ $= \min\{ z_1, ..., z_k \}$.

So if we can compute the optimal solution for all the subproblems then finding the global optimum is trivial. Observe that we can apply branching recursively (_as remarked before_). In general we keep branching until we can easily solve the subproblem.


#### Bounding

In particular, for each subproblem $z_i = min\{ c(\underline{x}) \mid \underline{x} \in X_i \}$ we should do the following:

- first of all we detect if $X_i = \emptyset$ (in such a case the optimal solution can't be in $X_i$ _of course_ and we move to the next subproblem);
- if it is not the case we try to compute the optimal solution $z_i$, if we're capable of doing so we can move to the next subproblem keeping track of the best solution found so far (remember that $z = \min\{ z_1, ..., z_k \}$);
- otherwise we compute a lower (_we're minimizing_) bound $z_i' \leq z_i$ to $z_i$ according to a **bounding criterion**: if $z_i'$ is greater than or equal to the best solution found so far, then $z_i$ won't affect the value of $z = \min\{ z_1, ..., z_k \}$ and so we can move to the next subproblem;

---

- if the bound doesn't allow us to discard the problem, we keep branching.

**Remark**: the execution of the branch-and-bound method is subject to a tree representation where each node corresponds to a feasible region $X_i$ with its associated bound (_provided by the bounding criterion_) and possibly the value of $z_i$ (if we've already computed it). The children of a given node are the regions obtained by branching. In this setting, a node of the tree with no children is said **fathomed** (or **pruned**).

#### Branch-and-bound for ILP

Consider the general ILP (_in canonical form_) $\min \{ \underline{c}^T \underline{x} \mid A \underline{x} = \underline{b}, \underline{x} \geq \underline{0}, \underline{x} \in \mathbb{Z}^n \}$.

- Let $\underline{\overline{x}}$ denote an optimal solution for the **linear relaxation** of the ILP: $\min \{ \underline{c}^T \underline{x} \mid A \underline{x} = \underline{b}, \underline{x} \geq \underline{0} \}$ and $z_{LP}^* = \underline{c}^T \underline{\overline{x}}$ denote the corresponding optimal value.

- If $\underline{\overline{x}}$ is integer, $\underline{\overline{x}}$ is also optimal for the original ILP (_as we already remarked_).

- Otherwise there must exist $\overline{x}_h$ fractional for some $h \in \{1, ..., n\}$. Then we can apply the following **branching criterion**: we split the original problem into
    - $ILP_1$: $\min \{ \underline{c}^T \underline{x} \mid A \underline{x} = \underline{b}, x_h \leq \lfloor \overline{x}_h \rfloor, \underline{x} \geq \underline{0}, \underline{x} \in \mathbb{Z}^n \}$ and
    - $ILP_2$: $\min \{ \underline{c}^T \underline{x} \mid A \underline{x} = \underline{b}, x_h \geq \lfloor \overline{x}_h \rfloor + 1, \underline{x} \geq \underline{0}, \underline{x} \in \mathbb{Z}^n \}$ .

- The bounds for the **bounding criterion** are provided by the linear relaxation (_remember that $z_{LP}^* \leq z_{ILP}^*$ if we are minimizing_).

**Remark**: the optimal solution to the linear relaxation of each subproblem can be found efficiently starting from the one of the parent problem by applying one step of the so-called **dual Simplex method**.

When we apply the branch-and-bound method to an ILP we can exploit different heuristics for:
- the **choice of the subproblem to examine** and
- the **choice of the fractional variable for branching**.

Regarding the **choice of the subproblem** (which corresponds to a node in the tree representation) we can:
- examine **deeper nodes first**;
- examine **more promising nodes first** (the ones with better linear relaxation optimal value; this strategy is also known as **best bound first**).

For the **choice of the "branching variable"**:
- it may not be the best choice to select the variable whose fractional part (in the optimal solution to the linear relaxation) is closer to $\frac{1}{2}$;

---

- we can apply **strong branching**: we compute the optimal objective function value for the linear relaxation of each possible subproblem that we could obtain by branching "through" a certain varibale (_which, as we remarked before, we can compute efficiently_) and choose the one that leads to the **best imporvement in the objective function**.

**Remark**: branch-and-bound is also applicable to mixed ILPs: when branching just consider the fractional variables that must be integer.

### Cutting plane methods

Consider the feasible region of a generic ILP problem (_in canonical form_): $X = \{ \underline{x} \in \mathbb{Z}^n \mid A \underline{x} \geq \underline{b}, \underline{x} \geq \underline{0} \}$. It can be described by different (infinitely many) sets of constrains (that is, we can change $A$ and $\underline{b}$ without modifying $X$) that may be weaker/tighter. We will see in a moment that some formulations are more convenient than others.

- The **ideal formulation** is that describing the **convex hull of $X$, $conv(X)$**, where $conv(X)$ is the smallest convex subset containing $X$.

It is easy to see that $conv(X)$ is the set of the "convex combinations" of the points in $X$. The vertices of $conv(X)$ (_by the definition of vertex_) can't be expressed as a convex combination of other points in $conv(X)$, then, since $X \subset conv(X)$ they can't be expressed neither as a convex combination of other points of $X$; so it must be that the vertices of $conv(X)$ belong to $X$ (otherwise they would not be in $conv(X)$ neither since there would not be points in $X$ such that their convex combination is equal to one of them).

It follows that the **ideal formulation is very convenient**: if we apply the Simplex method to the linear relaxation of an ILP expressed with the ideal formulation, we would get as a result an optimal vertex which must be integer (_by what we observed above_) and so (_as we remarked previously_) it would also be an optimal solution for the original ILP.

It is possible to prove that **for any feasible region $X$** of an ILP (bounded or unbounded), there exists an **ideal formulation** (a description of $conv(X)$ involving a finite number of linear constraints). Unfourtanately the number of constraints can be very large (exponential) with respect to the size of the original formulation. Furthermore, the ideal formulation is often very difficult to determine.

The idea behind **cutting plane methods** is that a full description of $conv(X)$ is not required, we just need a good description in the neighborhood of the optimal solution (making sure that the optimal solution of the ILP is a vertex of the feasible region of its linear relaxation). So we have to improve the description "locally" by means of the so-called **cutting planes**.

- A **cutting plane** is an inequality $\underline{a}^T \underline{x} \leq b$ that is not satisfied by $\underline{x}_{LP}^*$ but is satisfied by all the feasible solutions of the ILP.

---

Given an initial formulation we will iteratively add cutting planes until the linear relaxation does not provide an optimal integer solution.

One kind of **cutting planes** are **Gomory fractional cuts** defined as follows.
Let $\underline{x}_{LP}^*$ be an optimal solution of the linear relaxation of the current formulation $\min \{ \underline{c}^T \underline{x} \mid A \underline{x} = \underline{b}, \underline{x} \geq \underline{0} \}$ and $x_{b_r}$ be a basic variable associated with the $(r+1)$-th row of the tableau, **with fractional value $x_{b_r}^* = \overline{b}_r$** (_it is clear by looking at the tableau equation below and putting the non-basic variables to 0_).
The $(r+1)$-th row of the optimal tableau can be translated into the equation:
$$
\text{(**) } x_{b_r} + \sum_{j \in N} \overline{a}_{rj} x_j = \overline{b}_r
$$
where $N$ is the set of indices of the non-basic variables.

- The **Gomory cut** w. r. t. the fractional basic variable $x_{b_r}$ is:
$$
\sum_{j \in N} (\overline{a}_{rj} - \lfloor \overline{a}_{rj} \rfloor) x_j \geq \overline{b}_r - \lfloor \overline{b}_r \rfloor
$$

Let's verify that a **Gomory cut is a cutting plane**.

1. **It is violated by the optimal fractional solution $\underline{x}_{LP}^*$ of the linear relaxation**: indeed $\overline{b}_r - \lfloor \overline{b}_r \rfloor > 0$ since $\overline{b}_r$ is fractional, while $x_j^* = 0 \forall j \in N$.

2. **It is satisfied by all integer feasible solutions**: since the tableau is an equivalent representation of the original constraints, all the points in $X$ must satisfy $\text{(**)}$. Furthermore, since for every point in $X$, $x_j \geq 0$ and it is clear that $\overline{a}_{rj} \geq \lfloor \overline{a}_{rj} \rfloor$, then
$$
x_{b_r} + \sum_{j \in N} \lfloor \overline{a}_{rj} \rfloor x_j \leq x_{b_r} + \sum_{j \in N} \overline{a}_{rj} x_j = \overline{b}_r \text{ .}
$$
> Finally, for every point of $X$, $x_{b_r} + \sum_{j \in N} \lfloor \overline{a}_{rj} \rfloor x_j$ is an integer, hence it must be:
$$
\text{(***) } x_{b_r} + \sum_{j \in N} \lfloor \overline{a}_{rj} \rfloor x_j \leq \lfloor \overline{b}_r \rfloor \text{.}
$$

> $\text{(***)}$ is known as the **integer form** of the gomory cut, by subtracting $\text{(***)}$ from $\text{(**)}$ we get the form in the definition, which is known as **fractional form**. The two are equivalent (assuming that $\text{(**)}$ holds).

**Remark**: before adding the **Gomory cut** to the tableau, we must put it in standard form, that is, we need to add a new slack variable.

**Important remark**: after having added the **Gomory cut** to the tableau, we can compute the optimal solution of the new linear relaxation by just one iteration of the **dual Simplex method**.

---

- It is possible to prove that **if we keep adding Gomory cuts iteratively**, eventually **we will find an integer optimal solution**.

### Branch-and-cut method

The "combined" **branch-and-cut** approach aims at overcoming the disadvantages of pure branch-and-bound (B&B) and pure cutting plane methods.

For each subproblem (node) of B&B, **several cutting planes** are generated to **improve the bound** and try to find an **optimal integer solution**.

Whenever the cutting planes become less effective, cut generation is stopped and branching operation is performed.

**Remark**: the cuts tend to strengthen the formulation (linear relaxation) of the various subproblems. Long series of cuts without sensible improvement are interrupted by branching operations.
