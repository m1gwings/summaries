---
marp: true
theme: summary
---
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

- We say that a LP is **infeasible** if $X = \emptyset$. 

- $\underline{x}^* \in X$ is an **optimal solution** for a LP problem if $f(\underline{x}^*) \leq f(\underline{x})$, $\forall \underline{x} \in X$ if we're **minimizing** $f(\underline{x})$ or $f(\underline{x}^*) \geq f(\underline{x})$, $\forall \underline{x} \in X$ if we're **maximizing** it instead.

- Thanks to the **linearity** of the involved functions and the structure of the feasible region, we can write a LP problem in the so-called **general form**:

<div class="centered-definition-expression">

$\min$ _(or_ $\max$_)_ $z = \underline{c}^T \underline{x}$
s. t.
$A_1 \underline{x} \geq \underline{b}_1$ ;
$A_2 \underline{x} \leq \underline{b}_2$ ;
$A_3 \underline{x} = \underline{b}_3$ ;
$x_j \geq 0$ $\forall j \in J \subseteq \{ 1, ..., n \}$ .

</div>

> **Remark**: The $x_j$_s_ with $j \not \in J$ are intended to be **free** (uncostrained).

- We say that a LP is in **standard form** if it has the following structure:

<div class="centered-definition-expression">

$\min z = \underline{c}^T \underline{x}$
s. t. $A \underline{x} = \underline{b}$;
$\underline{x} \geq 0$.

</div>

---

- We say that a LP is in **canonical form** if it has the following structure:

<div class="centered-definition-expression">

$\min z = \underline{c}^T \underline{x}$
s. t. $A \underline{x} \geq \underline{b}$;
$\underline{x} \geq 0$.

</div>

### Geometry of LP

- A **level curve** of value $z$ of a function $f$ is the set of points in $\mathbb{R}^n$ where $f$ is constant and takes value $z$.

#### Hyperplanes and affine half-spaces

- We say that $H = \{ \underline{x} \in \mathbb{R}^n \mid \underline{a}^T \underline{x} = b \}$ is a **hyperplane**, while $H^- = \{ \underline{x} \in \mathbb{R}^n \mid \underline{a}^T \underline{x} \leq b \}$ is an **affine half-space**.

#### Convex sets and polyhedrons

- Let $\underline{y}_1, \underline{y}_2 \in \mathbb{R}^n$ and $\alpha \in [0, 1]$; we call **convex combination** of $\underline{y}_1$ and $\underline{y}_2$ the vector $\alpha \underline{y}_1 + (1 - \alpha) \underline{y}_2$.

- Let $\underline{y}_1, \underline{y}_2 \in \mathbb{R}^n$ , we define the **segment** between $\underline{y}_1$ and $\underline{y}_2$ as the set of all their convex combinations: $[\underline{y}_1, \underline{y_2}] = \{ \alpha \underline{y}_1 + (1 - \alpha) \underline{y}_2 \mid \alpha \in [0, 1] \}$.

- A subset $S \in \mathbb{R}^n$ is **convex** if for each pair $\underline{y}_1, \underline{y}_2 \in S$, $S$ contains the segment between $\underline{y}_1$ and $\underline{y}_2$.

- We call **polyhedron** the intersection of a finite number of half-spaces.

- A **vertex** of a polyhedron $P$ is a point of $P$ which cannot be expressed as a convex combination of two other distinct points of $P$. That is: $\underline{x}$ is a vertex of $P$ _iff_ $\underline{x} = \alpha \underline{y}_1 + (1 - \alpha) \underline{y}_2 \wedge \alpha \in [0, 1] \implies \underline{x} = \underline{y}_1 \lor \underline{x} = \underline{y}_2$. 

- Given a polyhedron $P$, a vector $\underline{d} \in \mathbb{R}^n$ with $\underline{d} \neq \underline{0}$ is an **unbounded feasible direction of $P$** if, for every point $x_0 \in P$, the _"ray"_ $\{ \underline{x}_0 + \lambda \underline{d} \mid \lambda \geq 0 \}$ is contained in $P$.

- A **polytope** is a bounded polyhedron, that is, a polyhedron which has no unbounded feasible direction.

### Algebraic characterization of LP

- Consider an $m \times n$ matrix $A$ (_with $m \leq n$_), a **basis** of $A$ is a subset of $m$ columns of $A$ that are linearly independent and form an $m \times m$ matrix $B$. (Sometimes we will refer to $B$ as the basis).

---

- Given a basis $B$, we call **basic variables** the vector of variables $\underline{x}_B$ which multiplies the linearly independent column of $A$ that are in $B$ ; we call the others **non-basic variables** and denote them with $\underline{x}_N$.

- Given a basis $B$, we call **basic solution** a solution (_to the system $A \underline{x} = \underline{b}$_) where $\underline{x}_N' = \underline{0}$ .

- Given a basis $B$, we call **basic feasible solution** a basic solution where $\underline{x}_B' \geq \underline{0}$ (_that is $B \underline{x}_B' + N \underline{x}_N' = \underline{b}$ [see property 17], $\underline{x}_N' = \underline{0}$ , $\underline{x}_B' \geq \underline{0}$ , which implies $\underline{x}' \in P$_).

- Given a basis $B$, let $\underline{c}_B$ be the subvector of $\underline{c}$ which multiplies the basic variables $\underline{x}_B$ and $\underline{c}_N$ be the one which multiplies the non basic variables. We call **vector of reduced costs** the vector $\underline{\overline{c}}^T = \underline{c} - \underline{c}_B^T B^{-1}A$. We can split $\underline{\overline{c}}$ into (_block matrices formalism_) $\underline{\overline{c}}_B^T = \underline{c}_B^T - \underline{c}_B^T B^{-1} B = \underline{0}$ and $\underline{\overline{c}}_N^T = \underline{c}_N^T - \underline{c}_B^T B^{-1} N$.

- Given a basis $B$, we denote with **$z_0$** the quantity $\underline{c}_B^T B^{-1} \underline{b}$.

- A **basic feasible solution** $\underline{x}'$ is **degenerate** if it contains at least one basic variable with value $x_{B,i}' = 0$ .

---

## Basic properties

### Equivalence between general and standard form of LP

First of all observe that a LP in standard form is in general form.
Now, through the following 4 **transformation rules**, we'll see how it is possible to bring a LP in general form into an equivalent LP in standard form:

1. From _max_ to _min_: $\max \underline{c}^T \underline{x} = - \min(- \underline{c}^T \underline{x})$;

2. from $\leq$ to $=$ : $\: \: \underline{a}^T \underline{x} \leq b \iff \begin{cases}
\underline{a}^T \underline{x} + s = b \\
s \geq 0 
\end{cases}$ where $s$ is a **slack** variable;

3. from $\geq$ to $=$ : $\: \: \underline{a}^T \underline{x} \geq b \iff \begin{cases}
\underline{a}^T \underline{x} - s = b \\
s \geq 0 
\end{cases}$ where $s$ is a **surplus** variable;

4. from $x_j$ free to $x_j \geq 0$: $\begin{cases}
x_j = x_j^+ - x_j^-\\
x_j^+, x_j^- \geq 0
\end{cases}$ .


### Geometry of LP

5. The **gradient** $\nabla f$ of a function $f$ indicates the **direction of fastest increse** of $f$.

#### Hyperplanes and affine half-spaces

6. We can write every hyperplane as $H = \{ \underline{x}_P + \underline{y} \mid \underline{a}^T \underline{y} = 0 \}$ and every affine half-space as $H^- = \{ \underline{x}_P + \underline{y} \mid \underline{a}^T \underline{y} \leq 0 \}$ where $\underline{a}^T \underline{x}_P = b$ (_the proofs are straightforward, just apply the usual technique for showing that two sets are equal_).

> **Remark**: Since $\cos(\underline{a}, \underline{y}) = \frac{\underline{a}^T \underline{y}}{\lVert a \rVert \lVert y \rVert} \leq 0$ if $\underline{a}^T \underline{y} \leq 0$, then the points of $H^-$ lie in the _"opposite half"_ w. r. t. $\underline{a}$ after we have _"split"_ $\mathbb{R}^n$ in two through $H$.

7. Let $\underline{y}_1, \underline{y}_2 \in \mathbb{R}^n$ s. t. $\underline{a}^T \underline{y}_1 \leq 0$ and $\underline{a}^T \underline{y}_2 \leq 0$ ; let $\alpha, \beta \geq 0$ ; then $\underline{x}_P + (\alpha \underline{y}_1 + \beta \underline{y}_2) \in H^-$ (_straightforward proof by applying property 6_).

#### Convex sets and polyhedrons

8. The **feasible region** of any LP is a **polyhedron** (_remember that we can express an equality constraint as $\underline{a}^T \underline{x} \leq b \wedge \underline{a}^T \underline{x} \geq b$_).

9. Every **polyhedron** is a **convex** subset of $\mathbb{R}^n$ (_it follows immediately by property 7 that every half-space is convex and it is trivial that the intersection of a finite number of convex sets is convex_).

---

10. A non-empty polyhedron $P = \{ \underline{x} \in \mathbb{R}^n \mid A \underline{x} = \underline{b}, \underline{x} \geq 0 \}$ (_in standard form_) or $P = \{ \underline{x} \in \mathbb{R}^n \mid A \underline{x} \geq \underline{b}, \underline{x} \geq 0 \}$ (_in canonical form_) has a **finite number ($\geq 1$) of vertices**.

11. Let $\underline{d}_1$ and $\underline{d}_2$ be two unbounded feasible directions of $P$, then **$\underline{d}_1 + \underline{d}_2$ is an unbounded feasible direction of $P$** (_for the proof we just need to apply the associative property plus the definition of unbounded feasible direction both on $\underline{d}_1$ and $\underline{d}_2$_); clearly **$\lambda \underline{d}_1$ is an unbounded feasible direction of $P$** for every $\lambda > 0$.

12. **_Weyl-Minkowski_ Representation of polyhedra theorem**: Every point $\underline{x}$ of a _polyhedron_ $P$ can be expressed as a **convex combination** of its **vertices** (_which are in finite number by 10_) $\underline{x}_1, ..., \underline{x}_k$ plus (if needed) an **unbounded feasible direction $\underline{d}$** of $P$ : $\underline{x} = \alpha_1 \underline{x}_1 + ... + \alpha_k \underline{x}_k (+ \underline{d})$ where $\alpha_i \geq 0$ and $\alpha_1 + ... + \alpha_k = 1$.

13. Every point $\underline{x}$ of a polytope can be expressed as a linear combination of its vertices (_follows immediately by 12 and by the definition of polytope_).

### Optimal vertices in LP

14. **Fundamental theorem of Linear Programming**: Consider a LP $\min\{ \underline{c}^T \underline{x} \mid \underline{x} \in P \}$ where $P \subset \mathbb{R}^n$ is a non-empty polyhedron (_in standard or canonical form_). Then either there exists (at least) one **optimal vertex** or the value of the objective function is **unbounded below** on $P$.

> **Proof**:
> - Case 1: $P$ has an unbounded feasible direction $\underline{d}$ s. t. $\underline{c}^T \underline{d} < 0$
>>> Let $\underline{x}_P \in P$, then $\underline{x}_0 + \lambda \underline{d} \in P$ for every $\lambda \geq 0$. Hence the set of values of the objective function on $P$ is a super set of $\{ \underline{c}^T \underline{x}_P + \lambda \underline{c}^T \underline{d} \mid \lambda \geq 0 \}$ which is **unbounded below** by hypothesis.
> - Case 2: $P$ has no unbounded feasible direction $\underline{d}$ s. t. $\underline{c}^T \underline{d} < 0$
>>> Then for every unbounded feasible direction $\underline{d}$, $\underline{c}^T \underline{d} \geq 0$. Since we can write every point $\underline{x} \in P$ as $\underline{x} = \alpha_1 \underline{x}_1 + ... + \alpha_k \underline{x}_k + \underline{d}$ where $\alpha_i \geq 0$, $\alpha_1 + ... + \alpha_k = 1$ and $\underline{d}$ can be $\underline{0}$ (_by theorem 12_), $\underline{c}^T \underline{x} = \alpha_1 \underline{c}^T \underline{x}_1 + ... + \alpha_k \underline{c}^T \underline{x_k} + \underline{c}^T \underline{d}$
$\geq \alpha_1 \underline{c}^T + ... + \alpha_k \underline{c}^T \underline{x_k}$ (_by hypothesis_)
$\geq \min_{i \in \{1, ..., k\}} \underline{c}^T \underline{x}_i$ (_we are exploiting the fact that $\underline{c}^T \underline{x}_i \geq \min \underline{c}^T \underline{x}_j$ , $\alpha_i \geq 0$ preserves the inequality direction, $\alpha_1 + ... + \alpha_k = 1$_). Then, said $\overline{i} = arg\,min_{i \in {1, ..., k}} \underline{c}^T \underline{x}_i$, $x_{\overline{i}}$ is an **optimal vertex**.

---

15. There are **four** types of LP (_it follows from theorem 14_):
> - with a **unique optimal solution**;
> - with **multiple (infinitely many)** optimal solutions (_if there are two optimal solutions, then every convex combination of those is an optimal solution, hence they are infinitely many_);
> - with **unbounded objective function**;
> - **infeasible**.

### Algebraic characterization of LP

16. For any polyhedron $P = \{ \underline{x} \in \mathbb{R}^n \mid A \underline{x} = \underline{b}, \underline{x} \geq \underline{0} \}$:
> - the **facets** are obtained by setting one variable to $0$ (_and determining all the values for the other variables that satisfy the constraints_);
> - the **vertices** are obtained by setting $n - m$ variables to $0$ where $A$ is an $m \times n$ matrix.

17. Given a basis $B$, we can write the system $A \underline{x} = \underline{b}$ as $B \underline{x}_B + N \underline{x}_N = \underline{b}$. Then $\underline{x}_B = B^{-1} \underline{b} - B^{-1} N \underline{x}_N$ .

18. $\underline{x} \in \mathbb{R}^n$ is a **basic feasible solution** $\iff$ $\underline{x}$ is a **vertex** of $P = \{ \underline{x} \in \mathbb{R}^n \mid A \underline{x} = \underline{b}, \underline{x} \geq \underline{0} \}$.

19. The **number of basic feasible solutions** is less than or equal to $\binom{n}{m}$ (_number of ways in which we can pick $m$ columns from a set of $n$ columns_).

20. Fixed a basis $B$, $\underline{c}^T \underline{x} = z_0 + \underline{\overline{c}}_N^T \underline{x}_N$ (_the proof follows from the second part of property 17 plus applying the block matrix formalism on $\underline{c}^T = [ \underline{c}_B^T \: \underline{c}_N^T ]$ and $\underline{x} = \left[ \begin{matrix} \underline{x}_B \\ \underline{x}_N \end{matrix} \right]$_).

21. **Optimality test**: Given a basis $B$, if $\underline{\overline{c}}_N \geq \underline{0}$ then the basic feasible solution $(\underline{x}_B^* , \underline{x}_N^*)$ (_where $\underline{x}_N^* = \underline{0}$ by definition of basic feasible solution and $\underline{x}_B^* = B^{-1} \underline{b} \geq \underline{0}$ by the second part of property 17 plus the definition of basic feasible solution_) is a **global optimum**.

> **Proof**: $\underline{c}^T \underline{x}$
>> $= z_0 + \underline{\overline{c}}_N^T \underline{x}_N$ (_property 20_)
>> $\geq z_0$ (_$\underline{\overline{c}}_N \geq \underline{0}$ by hypothesis, $\underline{x}_N \geq \underline{0}$ by the constraints_)
>> = $\underline{c}_B^T B^{-1} \underline{b} = \underline{c}^T \left[ \begin{matrix} B^{-1} \underline{b} \\ \underline{0}_{n-m} \end{matrix} \right]$ (_assuming without loss of generality that the independent columns are at the beginning; it is equivalent to renaming the variables_)
>> $= \underline{c}^T \left[ \begin{matrix} \underline{x}_B^* \\ \underline{x}_N^* \end{matrix} \right]$ .

---

> **Remarks**:
> - For a **maximization problem** we check whether $\underline{\overline{c}}_N \leq \underline{0}$ ;
> - The optimality condition is **sufficient but in general not necessary**.

## The Simplex method

### Tableaus

We can represent the set of constraints and the objective function of a LP in _standard form_ in a matrix known as **tableau**.
In particular (as we have done before), given a basis $B$ (_for now we will assume to always have one, we will see how to find it later_), without loss of generality we can write the matrix $A$ (_we're using the notation introduced before for an LP in standard form_) as $A = [ B \: N ]$ (_it is just a matter of renaming the variables_). Then the LP enforces the following equalities:
- $z = \underline{c}^T \underline{x} \iff 0 = \underline{c}_B^T \underline{x}_B + \underline{c}_N^T \underline{x}_N + (-1) z$ ;
- $\underline{b} = B \underline{x}_B + N \underline{x}_N = B \underline{x}_B + N \underline{x}_N + \underline{0} z$ .

As in linear algebra, where we associate to the system $A \underline{x} = \underline{b}$ the matrix $[ A \: \underline{b} \: ]$, here we can represent the LP with the matrix:

$$\left[ \begin{matrix}
0 & \underline{c}_B^T & \underline{c}_N^T & -1 \\
\underline{b} & B & N & \underline{0}_m
\end{matrix} \right]$$

where the vector of unknowns is $\left[ \begin{matrix} \underline{x}_B \\ \underline{x}_N \\ z \end{matrix} \right]$ and we swapped $A$ and $\underline{b}$ (_like in$[ \: \underline{b} \: A]$_).

As we will see the Simplex method boils down to applying pivoting operations to the tableau. Remember that pivoting operations consist in multiplying a row by a _non-zero_ scalar and adding to a row another row.
We can:

- Multiply the $i$_-th_ row by the scalar $\alpha \neq 0$ by premultiplying by $[ \underline{e}_1 \: ... \: \alpha \underline{e}_i \: ... \: \underline{e}_m ]$;

- Add the $i$-th row to the $j$-th row by premultiplying by $[ \underline{e}_1 \: ... \: \underline{e}_{i-1} \: \: \underline{e}_i + \underline{e}_j \: \: \underline{e}_{i+1} \: ... \: \underline{e}_m ]$.

(_To see why, it is sufficient to postmultiply the matrices above by $A = \left[ \begin{matrix} \underline{a}_1^T \\ ... \\ \underline{a}_m^T \end{matrix} \right]$ using the block matrix formalism_).

These matrices are both invertible, hence (as we know from basic linear algebra) they preserve the underlying system of equations when we premultiply.

---

Applying the pivoting to the _"last"_ $m$ rows of the tableau in order to bring $B$ into $I$ is equivalent to the following premultiplication:

$$\left[ \begin{matrix}
1 & \underline{0}_m^T \\
\underline{0}_m & B^{-1}
\end{matrix} \right]

\left[ \begin{matrix}
0 & \underline{c}_B^T & \underline{c}_N^T & -1 \\
\underline{b} & B & N & \underline{0}_m
\end{matrix} \right]

=

\left[ \begin{matrix}
0 & \underline{c}_B^T & \underline{c}_N^T & -1 \\
B^{-1} \underline{b} & I_{m \times m} & B^{-1} N & \underline{0}_m
\end{matrix} \right]$$

(_The equality follows from the block matrix formalism_).

Then extending the pivoting to the first row is obtained by:

$$\left[ \begin{matrix}
1 & - \underline{c}_B^T \\
\underline{0}_m & I_{m \times m}
\end{matrix} \right]

\left[ \begin{matrix}
0 & \underline{c}_B^T & \underline{c}_N^T & -1 \\
B^{-1} \underline{b} & I_{m \times m} & B^{-1} N & \underline{0}_m
\end{matrix} \right]

=

\left[ \begin{matrix}
-z_0 & \underline{0}_m^T & \underline{\overline{c}}_N^T & -1 \\
B^{-1} \underline{b} & I_{m \times m} & B^{-1} N & \underline{0}_m
\end{matrix} \right]$$

(_The premultiplication matrix has been obtained by generalizing the matrix which represents the pivoting operation of adding a row to another to a linear combination of rows in which we add to the first row $-c_{B1}$ multiplied by the second row plus ... plus $-c_{Bm}$ multiplied by the last row_).

The last tableau has the structure on which the Simplex method operates. We usually omit the last column relative to $z$ :

$$\left[ \begin{matrix}
-z_0 & \underline{0}_m^T & \underline{\overline{c}}_N^T \\
B^{-1} \underline{b} & I_{m \times m} & B^{-1} N
\end{matrix} \right]
$$

In the following we will refer to tableaus with the structure above as tableaus in **(\*)** form.

Here are the reasons why the tableau in (\*) form is so useful:

- In the first column we can find the value of the basic solution $\underline{x}_B' = B^{-1} \underline{b}$ , $\underline{x}_N' = \underline{0}$ (_see property 17_) associated to the basis $B$, then we can also determine if it is feasible (_iff_ $B^{-1} \underline{b} \geq \underline{0}$ );

- If the tableau represents a basic feasible solution, we can examine the **vector of reduced costs** in the first row: if $\underline{\overline{c}}_N^T \geq 0$ (_and we're minimizing_), then (_by theorem 21_) the basic feasible solution is optimal and we have solved the LP; otherwise we can either detect that the LP is unbounded or change the basis in such a way to improve the objective function and (paying attention to some details with which we will deal later) we can iterate this process with the guarantee that we will reach an optimal vertex (_if the LP is bounded then there exists at least one optimal vertex by theorem 14_) or find that the LP unbounded (_we will see how to do both_).

**Remark**: In general the tableaus with which we will work will have a structure where the columns are permutated with respect to the (\*) form above. This is due to the fact that when we apply the pivoting we "transform" one column $\underline{e}_i$ of the identity matrix into a column with no precise structure while a column in $B^{-1} N$ becomes $\underline{e}_i$. As we have said many times, we could bring the tableau back to (\*) form by renaming the variables, but it is not worth it. 

---

> (_cont'd_) What matters is that above a column of the identiry matrix $e_i$ we will have a $0$, above the other columns we will have the reduced cost associated to the corresponding variable (the one in the vector of unknowns that multiplies that column; _this is clear considering the system of equations represented by the tableau_).

### From one basic feasible solution to another

Consider the tableau in (\*) form below where we highlight the elements in the $(i + 1)$-th row and $(m+j+1)$-th column:

$$
\left[ \begin{matrix}
-z_0 & \underline{0}_m^T & \underline{\overline{c}}_{N,l}^T & \overline{c}_{N,j} & \underline{\overline{c}}_{N,r}^T \\
x_{B,1}' & \underline{e}_1^T & \underline{a}_{1,l}^T & a_{1,m+j} & \underline{a}_{1,r}^T \\
... & ... & ... & ... & ... \\
x_{B,i}' & \underline{e}_i^T & \underline{a}_{i,l}^T & a_{i,m+j} & \underline{a}_{i,r}^T \\
... & ... & ... & ... & ... \\
x_{B,m}' & \underline{e}_m^T & \underline{a}_{m,l}^T & a_{m,m+j} & \underline{a}_{m,r}^T
\end{matrix} \right]
$$

Assume that:

1. we're minimizing;
2. $x_{B,k}' \geq 0 \forall k \in \{ 1, ..., m \}$ (_that is, the tableau represents a basic feasible solution_);
3. $\overline{c}_{N,j} < 0$ ;
4. $a_{i,m+j} > 0$ ;
5. said $\theta_k = \frac{x_{B,k}'}{a_{k,m+j}}$ for every $k$ s. t. $a_{k,m+j} > 0$, then $i = arg\,\min_{k \: s.t. \: a_{k,m+j} > 0} \theta_k$ .

Let's see what happens if we pivot around the element $a_{i,m+j}$ ; first of all we have to multiply the $(i+1)$-th row by $\frac{1}{a_{i,m+j}}$ :

$$
\left[ \begin{matrix}
-z_0 & \underline{0}_m^T & \underline{\overline{c}}_{N,l}^T & \overline{c}_{N,j} & \underline{\overline{c}}_{N,r}^T \\
x_{B,1}' & \underline{e}_1^T & \underline{a}_{1,l}^T & a_{1,m+j} & \underline{a}_{1,r}^T \\
... & ... & ... & ... & ... \\
\theta_i & \frac{1}{a_{i,m+j}}\underline{e}_i^T & \frac{1}{a_{i,m+j}}\underline{a}_{i,l}^T & 1 & \frac{1}{a_{i,m+j}}\underline{a}_{i,r}^T \\
... & ... & ... & ... & ... \\
x_{B,m}' & \underline{e}_m^T & \underline{a}_{m,l}^T & a_{m,m+j} & \underline{a}_{m,r}^T
\end{matrix} \right]
$$

---

Then we have to clear the $(m+j+1)$-th column, that is, we subtract from the $1$-st row $\overline{c}_{N,j}$ times the $(i + 1)$-th row, from the $2$-nd row $a_{1,m+j}$ times the $(i + 1)$-th row, ... :

$$
\left[ \begin{matrix}
-z_0 - \overline{c}_{N,j} \theta_i & -\frac{\overline{c}_{N,j}}{a_{i,m+j}} \underline{e}_i^T & \underline{\overline{c}}_{N,l}^T - \frac{\overline{c}_{N,j}}{a_{i,m+j}} \underline{a}_{i,l}^T & 0 & \underline{\overline{c}}_{N,r}^T - \frac{\overline{c}_{N,j}}{a_{i,m+j}} \underline{a}_{i,r}^T \\
x_{B,1}' - a_{1,m+j} \theta_i & \underline{e}_1^T - \frac{a_{1,m+j}}{a_{i,m+j}} \underline{e}_i^T & \underline{a}_{1,l}^T - \frac{a_{1,m+j}}{a_{i,m+j}} \underline{a}_{i,l}^T & 0 & \underline{a}_{1,r}^T - \frac{a_{1,m+j}}{a_{i,m+j}} \underline{a}_{i,r}^T \\
... & ... & ... & ... & ... \\
\theta_i & \frac{1}{a_{i,m+j}} \underline{e}_i^T & \frac{1}{a_{i,m+j}} \underline{a}_{i,l}^T & 1 & \frac{1}{a_{i,m+j}} \underline{a}_{i,r}^T \\
... & ... & ... & ... & ... \\
x_{B,m}' - a_{m,m+j} \theta_i & \underline{e}_m^T - \frac{a_{m,m+j}}{a_{i,m+j}} \underline{e}_i^T & \underline{a}_{m,l}^T - \frac{a_{m,m+j}}{a_{i,m+j}} \underline{a}_{i,l}^T & 0 & \underline{a}_{m,r}^T - \frac{a_{m,m+j}}{a_{i,m+j}} \underline{a}_{i,r}^T
\end{matrix} \right]
$$

**Remarks**:

- The new tableau **still** represents a **basic solution** (_remember that the pivoting preserves the underlying system of equations_) where the basic variables are $x_{B,1}, ..., x_{B,i-1}, x_{B,i+1}, ..., x_{B,m}, x_{N,j}$ and the non-basic variables are $x_{N,1}, ..., x_{N,j-1}, x_{N,j+1}, ..., x_{N,n-m}, x_{B,i}$ (_if we swap the $(m+j+1)$-th column with the $(i+1)$-th we get a tableau exactly in (*) form_);

- The solution is **also feasible**: $\theta_i \geq 0$ (_by assumptions 2 and 4_), for every $k$ s. t. $a_{k,m+j} \leq 0$ , $x_{B,k}' - a_{k,m+j} \theta_i \geq x_{B,k}' \geq 0$ (_by assumption 2 and since $\theta_i \geq 0$_), for every $k$ s. t. $a_{k,m+j} > 0$, $x_{B,k}' - a_{k,m+j} \theta_i = a_{k,m+j}(\theta_k - \theta_i) \geq 0$ (_by assumptions 4 and 5_);

- The **new value of the objective function** associated with the basic feasible solution is $z_0 + \overline{c}_{N,j} \theta_i \leq z_0$ (_by assumption 3 and since $\theta_i \geq 0$_), which is good since we're minimizing (_by assumption 1_).

### Detect that the LP is unbounded

Suppose that, after a certain number of _"change of basis"_ as described above, we find a **non-basic variable** $x_{N,j}$ s. t. $\overline{c}_{N,j} < 0$ and $a_{k,m+j} \leq 0$ for every $k \in \{ 1, ..., m \}$ (_hence we can't apply the change of basis with such non-basic variable since it violates assumption 4_). Then, if we assign the value $x_{N,j}' > 0$ to $x_{N,j}$ and $0$ to every other non-basic variable, we get a solution with:

- $z'' = z_0 + \overline{c}_{N,j} x_{N,j}'$ ;
- $x_{B,k}'' = x_{B,k}' - a_{k,m+j} x_{N,j}' \geq x_{B,k}' \geq 0$ .

(_The equalities follow from writing down the underlying equations of the tableau_).

The solution is feasible for every value of $x_{N,j}' > 0$ and the value $z''$ is unbounded below, hence **the LP is unbounded**.

---

### Prevent cycling

The procedure that we've described has still a problem: as we've described in detail before, when we want to perform a change of basis, we have to choose a non-basic variable $x_{N,j}$ s. t. $\overline{c}_{N,j} < 0$ (if there isn't such non-basic variable we've found an optimal basic feasible solution by theorem 21), then we have to pick a basic varibale $x_{N,i}$ s. t. $\theta_i \leq \theta_k$ for every other $k \in \{ 1, ..., m \}$ s. t. $a_{k,m+j} > 0$ (if $a_{k,m+j} \leq 0 \forall k \in \{ 1, ..., m \}$ the LP is unbounded as stated earlier); but we haven't said how to break ties (both in the choice of $x_{N,j}$ and $x_{B,i}$).

It can be proven (by providing a counterexample) that for certain criteria of breaking ties there can be cycles where we change the basis going back to a basic feasible solution that we've already examined but that doesn't allow us to stop the execution (neither $\underline{\overline{c}}_N \geq \underline{0}$ or we detect that the LP is unbounded), that is, the algorithm will loop forever.

To solve this problem we can apply a criterion of breaking ties which provides a (proved) guarantee of halting: the **Bland**'s rule, where we break ties by choosing the variable with the **lowest index** (both for $x_{N,j}$ and $x_{B,i}$).

That is, if we apply the Bland's rule it can be proven that:

- if the LP is bounded we will find a basic feasible solution with $\underline{\overline{c}}_N \geq \underline{0}$ (remember that this condition is only sufficient for optimality);

- if the LP is unbounded we will detect it as described before;

hence, in every scenario, the algorithm will halt.

### The algorithm

Let's sum up everything into an algorithm. Assume that we have an initial basis $B$ (we will see how to find one by applying the algorithm below to an auxiliary problem which has an "evident" initial basis by construction) for an LP **in standard form**.

First of all we have to bring the tableau in (\*) form.

Then we iterate the following procedure:

1. if $\underline{\overline{c}}_N \geq \underline{0}$ we have found an optimal basic feasible solution (and we can stop)

2. otherwise let $x_{N,j}$ be the non-basic variable s. t. $\overline{c}_{N,j} < 0$ with the lowest index (Bland's rule)

> 3. if $a_{k,m+j} \leq 0 \forall k \in \{ 1, ..., m \}$ then the LP is unbounded (and we can stop)

> 4. otherwise let $x_{N,i}$ be the basic variable s. t. $a_{i,m+j} > 0$, $\theta_i \leq \theta_k$ for every other $k \in \{ 1, ..., m \} \mid a_{k,m+j} > 0$ with the lowest index (Bland's rule)

---

> 5. We change the basis through pivoting (as described before) and go back to 1

### Two-phase Simplex method

From an LP in standard form we can derive the so-called **auxiliary LP**:

<div class="centered-definition-expression">

$\min z = \underline{1}_m^T \underline{y}$
s. t. $A \underline{x} + I_{m \times m} \underline{y} = \underline{b}$ ;
$\underline{x} \geq 0, \underline{y} \geq 0$ .

</div>

Without loss of generality we can assume that $\underline{b} \geq \underline{0}$ (_if it is not the case we can substitue all the $b_i < 0$ with $-b_i$ and the corresponding $\underline{a}_i^T$ with $-\underline{a}_i^T$ in the original LP_).

**Observe that**:

- the auxiliary LP has always a basic feasible solution with $\underline{x}_N = \underline{x}$ and $\underline{x}_B = \underline{y}$ where $\underline{y}' = \underline{b} \geq \underline{0}$ (_this implies that the auxiliary LP is always feasible_);

- if the original LP is feasible there exists a solution with $\underline{y}' = \underline{0}$ which must be optimal since $z' = \underline{1}_m^T \underline{0} = 0$ and $\underline{y} \geq \underline{0}$ implies $z \geq 0$, hence, if we find an optimal solution to the auxiliary problem with $\underline{y}' \neq \underline{0}$, then the original LP is infeasible;

- the converse is also true: if there exists a basic feasible solution with $\underline{y}' = \underline{0}$, then the original LP is feasible.

These considerations allow us to introduce the **two-phase Simplex method**:

1. given an LP in standard form we build the auxiliary LP;

2. we apply the Simplex method to the auxiliary LP (for which we always know an initial feasible basis);

3. if the optimal solution has $\underline{y}' \neq \underline{0}$ then the original LP is infeasible;

4. otherwise the original LP is feasible: if all the $y_i$ are non-basic variables then we have an initial feasible basis for the original LP; we can discard the first row (with the objective function of the auxiliary LP) and the last $m$ columns (related to the variables $\underline{y}$) from the tableau, add the row representing the original objective function on top and perform the pivoting to bring the tableau in (_a "permutation"_) of (\*) form (_we want to have $0$ for all the elements on the first row above a column $\underline{e}_i$_). It can happen that, even if $\underline{y}' = \underline{0}$, some variables $y_j$ are still in the basis, that is, we have a degenerate basic feasible solution. In this case we can bring all the $y_j$ outside of the basis by pivoting in such a way to bring a variable $x_k$ inside (_see how in the page that follows_).

---

Let's visualize the process. Consider the tableau below (**where in the top row we put also the vector of unknows for clarity**) representing a degenerate basic feasible solution with $y_{B,j}' = 0$ (the value below $x_{B,i-1}'$ and above $x_{B,i+1}'$ in the first column) in the basis; for simplicity we will assume that the "$x$"-basic variables ($x_{B,1}, x_{B,2}, ...$) are in the vector of unknowns with the same order with which their corresponding values ($x_{B,1}', x_{B,2}', ...$) appear in the first column (_as always this doesn't compromise generality_):

$$
\left[ \begin{matrix}
 & ... & x_{B,1} & ... & x_{B,i-1} & ... & x_k & ... & x_{B,i+1} & ... & x_{B,m} & ... & y_{B,j} & ... \: \\
-z_0 & ... & 0 & ... & 0 & ... & \alpha_0 & ... & 0 & ... & 0 & ... & 0 & ... \: \\
x_{B,1}' & ... & 1 & ... & 0 & ... & \alpha_1 & ... & 0 & ... & 0 & ... & 0 & ... \: \\
... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... \: \\
x_{B,i-1}' & ... & 0 & ... & 1 & ... & \alpha_{i-1} & ... & 0 & ... & 0 & ... & 0 & ... \: \\
0 & ... & 0 & ... & 0 & ... & \alpha_i & ... & 0 & ... & 0 & ... & 1 & ... \: \\
x_{B,i+1}' & ... & 0 & ... & 0 & ... & \alpha_{i+1} & ... & 1 & ... & 0 & ... & 0 & ... \: \\
... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... \: \\
x_{B,m}' & ... & 0 & ... & 0 & ... & \alpha_{m} & ... & 0 & ... & 1 & ... & 0 & ... \: \\
\end{matrix} \right]
$$

In order to perform the pivoting we need to choose a variable $x_k$ whose coefficient in the row which determines the value of $y_{B,j}$ (above it is the $(i+1)$-th row if we don't account for the top row with the vector of unknowns) is different from zero. That is we will assume that $\alpha_i \neq 0$ (**the column relative to $x_{k}$ doesn't need to be between the columns relative to $x_{B,i-1}$ and $x_{B,i+1}$ in general**). Then it easy to see that after the pivoting we get the following tableau:

$$
\left[ \begin{matrix}
 & ... & x_{B,1} & ... & x_{B,i-1} & ... & x_k & ... & x_{B,i+1} & ... & x_{B,m} & ... & y_{B,j} & ... \: \\
-z_0 & ... & 0 & ... & 0 & ... & 0 & ... & 0 & ... & 0 & ... & -\frac{\alpha_0}{\alpha_i} & ... \: \\
x_{B,1}' & ... & 1 & ... & 0 & ... & 0 & ... & 0 & ... & 0 & ... & -\frac{\alpha_1}{\alpha_i} & ... \: \\
... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... \: \\
x_{B,i-1}' & ... & 0 & ... & 1 & ... & 0 & ... & 0 & ... & 0 & ... & -\frac{\alpha_{i-1}}{\alpha_i} & ... \: \\
0 & ... & 0 & ... & 0 & ... & 1 & ... & 0 & ... & 0 & ... & \frac{1}{\alpha_i} & ... \: \\
x_{B,i+1}' & ... & 0 & ... & 0 & ... & 0 & ... & 1 & ... & 0 & ... & -\frac{\alpha_{i+1}}{\alpha_i} & ... \: \\
... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... & ... \: \\
x_{B,m}' & ... & 0 & ... & 0 & ... & 0 & ... & 0 & ... & 1 & ... & -\frac{\alpha_m}{\alpha_i} & ... \: \\
\end{matrix} \right]
$$

**That is** the value of every other basic variable (different from $y_{B,j}$) isn't affected and the new value for $x_{k}$ is $0$: we still have a degenerate basic feasible solution; but $y_{B,j}$ is now outside of the basis, while $x_{k}$ (which we can rename into $x_{B,i}$) is inside.
