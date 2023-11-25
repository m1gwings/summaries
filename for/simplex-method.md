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

- We say that a LP is in **canonical form** if it has the following structure:

<div class="centered-definition-expression">

$\min z = \underline{c}^T \underline{x}$
s. t. $A \underline{x} \geq \underline{b}$;
$\underline{x} \geq 0$.

</div>

### Geometry of LP

- A **level curve** of value $z$ of a function $f$ is the set of points in $\mathbb{R}^n$ where $f$ is constant and takes value $z$.

#### Planes and hyperplanes

- We say that $H = \{ \underline{x} \in \mathbb{R}^n \mid \underline{a}^T \underline{x} = b \}$ is a **hyperplane**, while $H^- = \{ \underline{x} \in \mathbb{R}^n \mid \underline{a}^T \underline{x} \leq b \}$ is an **affine half-space**.

#### Convex sets and polyhedrons

- Let $\underline{y}_1, \underline{y}_2 \in \mathbb{R}^n$ and $\alpha \in [0, 1]$; we call **convex combination** of $\underline{y}_1$ and $\underline{y}_2$ the vector $\alpha \underline{y}_1 + (1 - \alpha) \underline{y}_2$.

- Let $\underline{y}_1, \underline{y}_2 \in \mathbb{R}^n$ , we define the **segment** between $\underline{y}_1$ and $\underline{y}_2$ as the set of all their convex combinations: $[\underline{y}_1, \underline{y_2}] = \{ \alpha \underline{y}_1 + (1 - \alpha) \underline{y}_2 \mid \alpha \in [0, 1] \}$.

- A subset $S \in \mathbb{R}^n$ is **convex** if for each pair $\underline{y}_1, \underline{y}_2 \in S$, $S$ contains the segment between $\underline{y}_1$ and $\underline{y}_2$.

- We call **polyhedron** the intersection of a finite number of half-spaces.

- A **vertex** of a polyhedron $P$ is a point of $P$ which cannot be expressed as a convex combination of two other distinct points of $P$. Algebraically, $\underline{x}$ is a vertex of $P$ _iff_ $\underline{x} = \alpha \underline{y}_1 + (1 - \alpha) \underline{y}_2 \wedge \alpha \in [0, 1] \implies \underline{x} = \underline{y}_1 \lor \underline{x} = \underline{y}_2$. 

- Given a polyhedron $P$, a vector $\underline{d} \in \mathbb{R}^n$ with $\underline{d} \neq \underline{0}$ is an **unbounded feasible direction of $P$** if, for every point $x_0 \in P$, the _"ray"_ $\{ \underline{x}_0 + \lambda \underline{d} \mid \lambda \geq 0 \}$ is contained in $P$.

- A **polytope** is a bounded polyhedron, that is, a polyhedron which has no unbounded feasible direction.

### Algebraic characterization of LP

- Consider an $m \times n$ matrix $A$, a **basis** of $A$ is a subset of $m$ columns of $A$ that are linearly independent and form an $m \times m$ matrix $B$. (Sometimes we will refer to $B$ as the basis).

---

- Given a basis $B$, we call **basic variables** the vector of variables $\underline{x}_B$ which multiplies the linearly independent column of $A$ that are in $B$; we call the others **non-basic variables** and denote them with $\underline{x}_N$.

- Given a basis $B$, we call **basic solution** a solution where $\underline{x}_N = \underline{0}$.

- Given a basis $B$, we call **basic feasible solution** a basic solution where $\underline{x}_B \geq \underline{0}$ (_that is $B \underline{x}_B + N \underline{x}_N = \underline{b}$ [see property 17], $\underline{x}_N = \underline{0}$ , $\underline{x}_B \geq \underline{0}$ , which implies $\underline{x} \in P$_).

- Given a basis $B$, let $\underline{c}_B$ be the subvector of $\underline{c}$ which multiplies the basic variables $\underline{x}_B$ and $\underline{c}_N$ be the one which multiplies the non basic variables. We call **vector of reduced costs** the vector $\underline{\overline{c}}^T = \underline{c} - \underline{c}_B^T B^{-1}A$. We can split $\underline{\overline{c}}$ into (_block matrices formalism_) $\underline{\overline{c}}_B^T = \underline{c}_B^T - \underline{c}_B^T B^{-1} B = \underline{0}$ and $\underline{\overline{c}}_N^T = \underline{c}_N^T - \underline{c}_B^T B^{-1} N$.

- Given a basis $B$, we denote with **$z_0$** the quantity $\underline{c}_B^T B^{-1} \underline{b}$.

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
x_j = x_j^+ - x_j^-\\
x_j^+, x_j^- \geq 0
\end{cases}$ .


### Geometry of LP

5. The **gradient** $\nabla f$ of a function $f$ indicates the **direction of fastest increse** of $f$.

#### Planes and hyperplanes

6. We can write every plane as $H = \{ \underline{x}_P + \underline{y} \mid \underline{a}^T \underline{y} = 0 \}$ and every hyperplane as $H^- = \{ \underline{x}_P + \underline{y} \mid \underline{a}^T \underline{y} \leq 0 \}$ (_the proofs are straightforward, just apply the usual technique for showing that two sets are equal_) where $\underline{a}^T \underline{x}_P = b$.

> **Remark**: Since $\cos(\underline{a}, \underline{y}) = \frac{\underline{a}^T \underline{y}}{\lVert a \rVert \lVert y \rVert} \leq 0$ if $\underline{a}^T \underline{y} \leq 0$, then the points of $H^-$ lie in the _"opposite half"_ w. r. t. $\underline{a}$ after we have _"split"_ $\mathbb{R}^n$ in two through $H$.

7. Let $\underline{y}_1, \underline{y}_2 \in \mathbb{R}^n$ s. t. $\underline{a}^T \underline{y}_1 \leq 0$ and $\underline{a}^T \underline{y}_2 \leq 0$ ; let $\alpha, \beta \geq 0$ ; then $\underline{x}_P + (\alpha \underline{y}_1 + \beta \underline{y}_2) \in H^-$ (_straightforward proof by using the equivalent writing for an hyperplane provided above_).

#### Convex sets and polyhedrons

8. The **feasible region** of any LP is a **polyhedron** (_remember that we can express an equality constraint as $\underline{a}^T \underline{x} \leq b \wedge \underline{a}^T \underline{x} \geq b$_).

9. Every **polyhedron** is a **convex** set of $\mathbb{R}^n$ (_it follows immediately by property 7 that every half-space is convex and it is trivial that the intersection of a finite number of convex sets is convex_).

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
> - Case 2: $P$ has no unbounded feasible direction $\underline{d}$ s. t. $\underline{c}^T \underline{d} \leq 0$
>>> Then for every unbounded feasible direction $\underline{d}$, $\underline{c}^T \underline{d} \geq 0$. Since we can write every point $\underline{x} \in P$ as $\underline{x} = \alpha_1 \underline{x}_1 + ... + \alpha_k \underline{x}_k + \underline{d}$ where $\alpha_i \geq 0$, $\alpha_1 + ... + \alpha_k = 1$ and $\underline{d}$ can be $\underline{0}$ (_by theorem 12_), $\underline{c}^T \underline{x} = \alpha_1 \underline{c}^T + ... + \alpha_k \underline{c}^T \underline{x_k} + \underline{c}^T \underline{d}$
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
> - the **facets** are obtained by setting one variable to $0$;
> - the **vertices** are obtained by setting $n - m$ variables to $0$ where $A$ is an $m \times n$ matrix.

17. Given a basis $B$, we can write the system $A \underline{x} = \underline{b}$ as $B \underline{x}_B + N \underline{x}_N = \underline{b}$. Then $\underline{x}_B = B^{-1} \underline{b} - B^{-1} N \underline{x}_N$ .

18. $\underline{x} \in \mathbb{R}^n$ is a **basic feasible solution** $\iff$ $\underline{x}$ is a **vertex** of $P = \{ \underline{x} \in \mathbb{R}^n \mid A \underline{x} = \underline{b}, \underline{x} \geq \underline{0} \}$.

19. The **number of basic feasible solutions** is less than or equal to $\binom{n}{m}$ (_number of ways in which we can pick $m$ columns from a set of $n$ columns_).

20. Fixed a basis $B$, $\underline{c}^T \underline{x} = z_0 + \underline{\overline{c}}_N^T \underline{x}_N$ (_the proof follows from the second part of property 17 plus applying the block matrix formalism on $\underline{c}^T = [ \underline{c}_B^T \: \underline{c}_N^T ]$ and $\underline{x} = \left[ \begin{matrix} \underline{x}_B \\ \underline{x}_N \end{matrix} \right]$_).

21. **Optimality test**: Given a basis $B$, if $\underline{\overline{c}}_N \geq \underline{0}$ then the basic feasible solution $\underline{x}_B$ , $\underline{x}_N$(_where $\underline{x}_N = \underline{0}$ by definition of basic feasible solution and $\underline{x}_B = B^{-1} \underline{b} \geq \underline{0}$ by the second part of property 17 plus the definition of basic feasible solution_) is a **global optimum**.

> **Proof**: $\underline{c}^T \underline{x}$
>> $= z_0 + \underline{\overline{c}}_N^T \underline{x}_N$ (_property 20_)
>> $\geq z_0$ (_$\underline{\overline{c}}_N \geq \underline{0}$ by hypothesis, $\underline{x}_N \geq \underline{0}$ by the constraints_)
>> = $\underline{c}_B^T B^{-1} \underline{b} = \underline{c}^T [ B^{-1} \underline{b} \: O_{n-m \times n-m} ]$ (_assuming without loss of generality that the independent columns are at the beginning; it is equivalent to renaming the variables_)
>> $= \underline{c}^T [ \underline{x}_B \: \underline{x}_N ]$ .

---

> **Remarks**:
> - For a **maximization problem** we check whether $\underline{\overline{c}}_N \leq \underline{0}$;
> - The optimality condition is **sufficient but in general not necessary**.

## The Simplex method

### Tableaus

We can represent the set of constraints and the objective function of a LP in _standard form_ in a matrix known as **tableau**.
In particular (as we have done before), given a basis $B$ (_for now we will assume to always have one, we will see how to find it later_), without loss of generality we can write the matrix $A$ (_we're assuming the notation introduced before for an LP in standard form_) as $A = [ B \: N ]$ (_it is just a matter of renaming the variables_). Then the LP enforces the following equalities:
- $z = \underline{c}^T \underline{x} \iff 0 = \underline{c}_B^T \underline{x}_B + \underline{c}_N^T \underline{x}_N + (-1) z$ ;
- $\underline{b} = B \underline{x}_B + N \underline{x}_N = B \underline{x}_B + N \underline{x}_N + \underline{0} z$ .

As in linear algebra, where we associate to the system $A \underline{x} = \underline{b}$ the matrix $[ A \: \underline{b} \: ]$, here we can represent the LP with the matrix:

<div class="centered-definition-expression">

$$\left[ \begin{matrix}
0 & \underline{c}_B^T & \underline{c}_N^T & -1 \\
\underline{b} & B & N & \underline{0}_m
\end{matrix} \right]$$

</div>

where the vector of unknowns is $\left[ \begin{matrix} \underline{x}_B \\ \underline{x}_N \\ z \end{matrix} \right]$ and we swapped $A$ and $\underline{b}$ (_like in$[ \: \underline{b} \: A]$_).

As we will see the Simplex method boils down to applying pivoting operations to the tableau. Remember that pivoting operations consist in multiplying a row by a _non-zero_ scalar and adding to a row another row.
We can:

- Multiply the $i$_-th_ row by the scalar $\alpha \neq 0$ by premultiplying by $[ \underline{e}_1 \: ... \: \alpha \underline{e}_i \: ... \: \underline{e}_m ]$;

- Add the $i$-th row to the $j$-th row by premultiplying by $[ \underline{e}_1 \: ... \: \underline{e}_{i-1} \: \: \underline{e}_i + \underline{e}_j \: \: \underline{e}_{i+1} \: ... \: \underline{e}_m ]$.

These matrices are both invertible, hence (as we know from basic linear algebra) they preserve the underlying system of equations when we premultiply.

---

Applying the pivoting to the _"last"_ $m$ columns of the tableau in order to bring $B$ into $I$ is equivalent to the following premultiplication:

<div class="centered-definition-expression">

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

</div>

(_The equality follows from the block matrix formalism_).

Then extending the pivoting to the first row is obtained by:

<div class="centered-definition-expression">

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

</div>

(_The premultiplication matrix has been obtained by generalizing the matrix which represents the pivoting operation of adding a row to another to a linear combination of rows in which we add to the first row $-c_{B1}$ multiplied by the second row plus ... plus $-c_{Bm}$ multiplied by the last row_).

The last tableau has the structure on which the Simplex method operates. We usually omit the last column relative to $z$ :

<div class="centered-definition-expression">

$$\left[ \begin{matrix}
-z_0 & \underline{0}_m^T & \underline{\overline{c}}_N^T \\
B^{-1} \underline{b} & I_{m \times m} & B^{-1} N
\end{matrix} \right]
$$

</div>

Here are the reasons why the tableau in this form is so useful:

- In the first column we can find the value of the basic solution $\underline{x}_B = B^{-1} \underline{b}$ , $\underline{x}_N = \underline{0}$ (_see property 17_) associated to the basis $B$, then we can also determine if it is feasible (_iff_ $B^{-1} \underline{b} \geq \underline{0}$ );

- If the tableau represents a basic feasible solution, we can examine the **vector of reduced costs** in the first row: if $\underline{\overline{c}}_N^T \geq 0$ (_and we're minimizing_), then (_by theorem 21_) the basic feasible solution is optimal and we have solved the LP; otherwise we can either detect that the LP is unbounded or change the basis in such a way to improve the objective function and (paying attention to some details) we can iterate this process with the guarantee that we will reach an optimal vertex (_if the LP is bounded then there exists at least one optimal vertex by theorem 14_) or find the LP unbounded (_we will see how to do both_).

**Remark**: In general the tableaus with which we will work will have a structure where the columns are permutated with respect to the one above. This is due to the fact that when we apply the pivoting we "transform" one column $\underline{e}_i$ of the identity matrix into a column with no precise structure while a column in $B^-1 N$ becomes $\underline{e}_i$. As we have said many times, we could bring the tableau back to the the nice structure by renaming the variables, but it is not worth it. 

---

> (_cont'd_) What matters is that above a column of the identiry matrix $e_i$ we will have a $0$, above the other columns we will have the reduced cost associated to the corresponding variable (the one in the vector of unknowns that multiplies that column; _this is clear considering the system of equalities represented by the tableau_).

### From one feasible solution to another

