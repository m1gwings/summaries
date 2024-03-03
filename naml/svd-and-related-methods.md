---
marp: true
theme: summary
---
# SVD & related methods

<div class="author">

Cristiano Migali

</div>

## Singular value decomposition (SVD) introduction

We want to extend the factorization provided for real symmetric matrices by the spectral theorem, that is
$$
A = Q \Lambda Q^T
$$
to any matrix $A \in \mathbb{R}^{m \times n}$.
The **SVD** allows us to factorize $A$ as
$$
A = U \Sigma V^T
$$
where:
- $U \in \mathbb{R}^{m \times m}$ is an orthogonal matrix;

- $\Sigma = \begin{bmatrix} \text{diag}\{ \sigma_1, ..., \sigma_r \} & O_{r \times (n-r)} \\ O_{(m-r) \times r} & O_{(m-r) \times (n-r)} \end{bmatrix}$ with $\sigma_1 \geq ... \geq \sigma_r > 0$ and $r = r(A)$;

- $V \in \mathbb{R}^{n \times n}$ is an orthogonal matrix.

### The reduced form of the SVD

The one that we already presented ($A = U \Sigma V^T$) is known as the **full form** of the SVD. We will introduce an equivalent expression where we keep only the first $r$ columns of $U$ and $V$ that is known as the **reduced** (or **economy**) **form**:
let $U_r = \begin{bmatrix} \underline{u}_1 & ... & \underline{u}_r \end{bmatrix}$, $V_r = \begin{bmatrix} \underline{v}_1 & ... & \underline{v}_r \end{bmatrix}$, $\Sigma_r = \text{diag} \{ \sigma_1, ..., \sigma_r \}$.
Then:
$$
U_r \Sigma_r V_r^T = \begin{bmatrix} \underline{u}_1 & ... & \underline{u}_r \end{bmatrix}
\begin{bmatrix}
\sigma_1 & 0 & ... & 0 \\
0 & ...  & ... & ... \\
... & ... & ... & 0 \\
0 & ... & 0 & \sigma_r
\end{bmatrix}
\begin{bmatrix}
\underline{v}_1^T \\
... \\
\underline{v}_r^T
\end{bmatrix} = 
\begin{bmatrix} \underline{u}_1 & ... & \underline{u}_r \end{bmatrix} \begin{bmatrix}
\sigma_1 \underline{v}_1^T \\
... \\
\sigma_r \underline{v}_r^T
\end{bmatrix} =
$$

$$
= \sum_{i=1}^r \sigma_i \underline{u}_i \underline{v}_i^T \text{.}
$$

Now it is just a matter of proving that $A = U \Sigma V^T = \sum_{i=1}^r \sigma_i \underline{u}_i \underline{v}_i^T$. **This expression will be used quite often**.

---

$$
A = U \Sigma V^T =
\begin{bmatrix}
\underline{u}_1 & ... & \underline{u}_r & \begin{bmatrix} \underline{u}_{r+1} & ... & \underline{u}_m \end{bmatrix}
\end{bmatrix}

\begin{bmatrix}
\begin{bmatrix}
\sigma_1 & 0 & ... & 0 \\
0 & ...  & ... & ... \\
... & ... & ... & 0 \\
0 & ... & 0 & \sigma_r
\end{bmatrix} & O_{r \times (n - r)} \\

O_{(m - r) \times n} & O_{(m-r) \times (n-r)}
\end{bmatrix}
\begin{bmatrix}
\underline{v}_1^T \\
... \\
\underline{v}_r^T \\
\begin{bmatrix}
\underline{v}_{r+1}^T \\
... \\
\underline{v}_{n}^T
\end{bmatrix}
\end{bmatrix} =
$$

$$
= \begin{bmatrix}
\underline{u}_1 & ... & \underline{u}_r & \begin{bmatrix} \underline{u}_{r+1} & ... & \underline{u}_m \end{bmatrix}
\end{bmatrix}
\begin{bmatrix}
\sigma_1 \underline{v}_1^T \\
... \\
\sigma_r \underline{v}_r^T \\
O_{(m-r) \times n}
\end{bmatrix} = \sigma_1 \underline{u}_1 \underline{v}_1^T + ... + \sigma_r \underline{u}_r \underline{v}_r^T + O_{m \times n} =
$$

$$
= \sum_{i=1}^r \sigma_i \underline{u}_i \underline{v}_i^T \text{.}
$$
As we wanted to porve.

### Proof of existence of the SVD (*)

First of all let's rewrite the SVD expression: $A = U \Sigma V^T$ iff $A V = U \Sigma$ iff
- $A \underline{v}_i = \sigma_i \underline{u}_i$ for every $i \in \{ 1, ..., r \}$;
- $A \underline{v}_i = \underline{0}_m$ for every $i \in \{ r+1, ..., n \}$

where $r = r(A)$.

So, given $A \in \mathbb{R}^{m \times n}$ with $r = r(A)$, we need to prove that there exist:
- $\underline{v}_1, ..., \underline{v}_n$ which form an orthonormal basis of $\mathbb{R}^n$;
- $\underline{u}_1, ..., \underline{u}_m$ which form an orthonormal basis of $\mathbb{R}^m$;
- $\sigma_1 \geq ... \geq \sigma_r > 0$

s. t. $A \underline{v}_i = \sigma_i \underline{u}_i$ for every $i \in \{ 1, ..., r \}$ and $A \underline{v}_i = \underline{0}_m$ for every $i \in \{ r+1, ..., n \}$.

Consider the matrix $A^T A \in \mathbb{R}^{n \times n}$.

1. **$A^T A$ is symmetric**: $(A^T A)^T = A^T (A^T)^T = A^T A$.

2. **All the eigenvalues of $A^T A$ are non-negative**: by the Rayleigh quotient
$$
\lambda = \frac{\underline{x}^T A^T A \underline{x}}{\underline{x}^T \underline{x}} = \frac{||A \underline{x}||^2}{||\underline{x}||^2} \geq 0 \text{.}
$$

3. **$r(A^T A) = r$**: we will prove that $N(A^T A) = N(A)$. If $\underline{x} \in N(A)$, clearly $\underline{x} \in N(A^T A)$. Let $\underline{x} \in N(A^T A)$, that is $A^T A \underline{x} = \underline{0}_n$, then $\underline{x}^T A^T A \underline{x} = 0$ iff $||A \underline{x}||^2 = 0$ iff $A \underline{x} = \underline{0}_m$.

---

By 1 and by the spectral theorem, $A^T A$ is diagonalizable. Hence the geometric and algebraic multiplicity of 0 are the same. The geometric multiplicity of 0 is $\dim N(A^T A) = n - r$ by 3. Hence, by 2, the remaining $r$ (taken with their multiplicities) eigenvalues of $A^T A$ are strictly positive. We can always name them such that $\lambda_1 \geq ... \geq \lambda_r > \lambda_{r+1} = ... = \lambda_n = 0$. Let $\underline{v}_1$, ..., $\underline{v}_n$ be the corresponding eigenvectors, chosen such that they're orthonormal (we can do so in virtue of the spectral theorem).

Let $\sigma_i = \sqrt{\lambda_i}$, $\underline{u}_i = \frac{A \underline{v}_i}{\sigma_i}$ for $i \in \{ 1, ..., r \}$.
We just need to prove that $\underline{u}_1, ..., \underline{u}_r$ are orthonormal, then the result will follow by extending $\underline{u}_1, ..., \underline{u}_r$ to an orthonormal basis of $\mathbb{R}^m$.

Let $i, j \in \{ 1, ..., r \}, i \neq j$:
$$
\underline{u}_i^T \underline{u}_i = \frac{\underline{v}_i^T A^T A \underline{v}_i}{\sigma_i^2} = \frac{\lambda_i \underline{v}_i^T \underline{v}_i}{\lambda_i} = 1 \text{;}
$$

$$
\underline{u}_i^T \underline{u}_j = \frac{\underline{v}_i^T A^T A \underline{v}_j}{\sigma_i \sigma_j} = \frac{\lambda_j}{\sigma_i \sigma_j} \underline{v}_i^T \underline{v}_j = 0 \text{.}
$$

**Remark**: we can extend $\underline{u}_1, ..., \underline{u}_r$ to an orthonormal basis of $\mathbb{R}^m$ iff we add $\underline{u}_{r+1}, ..., \underline{u}_{m}$ which form an orthonormal basis of $N(A A^T)$.
First of all
$$
A A^T \underline{u}_i = \frac{1}{\sigma_i} A A^T A \underline{v}_i = \frac{1}{\sigma_i} A \lambda_i \underline{v}_i = \lambda_i \frac{A \underline{v}_i}{\sigma_i} = \lambda_i \underline{u}_i \text{,}
$$
that is, $\underline{u}_i$ is an eigenvector of $A A^T$ with eigenvalue $\lambda_i$.
Note that all the properties 1-3 hold also for $A A^T$ since $A A^T = B^T B$ with $B = A^T$. Hence $\dim N(A A^T) = m - r(A^T) = m - r$; furthermore an orthonormal basis of $N(A A^T)$ must be orthogonal to $\underline{u}_1, ..., \underline{u}_r$ since they are eigenvectors which belong to different eigenspaces of a symmetric matrix. The converse is also true, if $\underline{u}_{r+1}, ..., \underline{u}_m$ are orthonormal and orthogonal to $\underline{u}_1, ..., \underline{u}_r$ then they must be an orthonormal basis of $N(A A^T)$, otherwise, by adding an actual orthonormal basis of $N(A A^T)$ to $\underline{u}_1, ..., \underline{u}_m$ we would have more than $m$ linear independet vectors in $\mathbb{R}^m$ (_remember that $A A^T \underline{u}_i = \lambda_i \underline{u}_i \neq \underline{0}_m$, that is $\underline{u}_i \not \in N(A A^T)$, for $i \in \{ 1, ..., r \}$_).

### Proof of uniqueness of SVD

We want to prove that if
$$
A = \sum_{i=1}^r \sigma_i \underline{u}_i \underline{v}_i^T
$$
then $\underline{v}_i$ is an eigenvector of $A^T A$ with eigenvalue $\sigma_i^2$.

---

Indeed
$$
A^T A = \sum_{i=1}^r \sum_{j=1}^r \sigma_i \sigma_j \underline{v}_i \underline{u}_i^T \underline{u}_j \underline{v}_j^T = \sum_{i=1}^r \sigma_i^2 \underline{v}_i \underline{v}_i^T \text{.}
$$
Then
$$
A^T A \underline{v}_i = \sum_{j=1}^r \sigma_j^2 \underline{v}_j \underline{v}_j^T \underline{v}_i = \sigma_i^2 \underline{v}_i
$$
as we wanted to prove.

### Geometric interpretation of the SVD

The SVD allows to decompose the transformation described by the matrix $A$ into two rotations/reflections realized through the orthogonal matrices $U$ and $V$ and a stretch realized by $\Sigma$.

In particular:
- in the 2D case, $A \in \mathbb{R}^{2 \times 2}$ has 4 entries which are equivalent to 4 geometric parameters: 1 for the first rotation, 2 for the stretch, and 1 for the second rotation;
- in the 3D case, $A \in \mathbb{R}^{3 \times 3}$ has 9 entries which are equivalent to 9 geometric parameters: 3 for the first rotation (for example, we can use Euler angles), 3 for the stretch, and 3 for the second rotation.

### Properties of the SVD

1. If $A$ is orthogonal, then $\sigma_1 = ... \sigma_n = 1$.

> **Proof (*)**: $A^T A = I_n$, the proof follows from the uniqueness of the SVD.

2. $||A \underline{x}|| \leq \sigma_1 ||\underline{x}||$.

> **Proof (*)**:
$$
||A \underline{x}||^2 = ||\sum_{i=1}^r \sigma_i \underline{u}_i \underline{v}_i^T \underline{x}||^2 = \sum_{i=1}^r \sigma_i^2 ||(\underline{v}_i^T \underline{x}) \underline{u}_i||^2 \leq \sigma_1^2 \sum_{i=1}^r (\underline{v}_i^T \underline{x})^2 \leq
$$

$$
\leq \sigma_1^2 \sum_{i=1}^n (\underline{v}_i^T \underline{x})^2 = \sigma_1^2 \sum_{i=1}^n \underline{v}_i^T \underline{x} \underline{v}_i^T \underline{x} = \sigma_1^2 \underline{x}^T (\sum_{i=1}^n \underline{v}_i \underline{v}_i^T) \underline{x} =
$$

$$
= \sigma_1^2 \underline{x}^T I_n \underline{x} = \sigma_1^2 ||\underline{x}||^2 \text{.}
$$

> The second last inequality follows from the fact that $\underline{e}_i = \alpha_1 \underline{v}_1 + ... + \alpha_n \underline{v}_n$, then $\sum_{i=1}^n \underline{v}_i \underline{v}_i^T \underline{e}_i = \sum_{i=1}^n \sum_{j=1}^n \alpha_j \underline{v}_i \underline{v}_i^T \underline{v}_j = \sum_{j=1}^n \alpha_i \underline{v}_i = \underline{e}_i$.

---

3. For every eigenvalue $\lambda$ of $A$, $|\lambda| \leq \sigma_1$.

> **Proof (*)**: it follows from property 2.

## Polar (QS) decomposition

The SVD leads to another important decomposition for **square** matrices: $A = QS$ where $Q = U V^T$, and $S = V \Sigma V^T$. Note that $U, V \in \mathbb{R}^{n \times n}$ are orthogonal matrices, hence the same is true for $Q$.
Furthermore $S$ is a symmetric matrix with non-negative eigenvalues (the entries on the diagonal of $\Sigma$), hence it is semi-positive. This is known as **polar** (or **QS**) **decomposition**.

## Matrix norms

### Frobenius norm

- Let $A \in \mathbb{R}^{m \times n}$, we define the **frobenius norm of A** as $||A||_F = \sqrt{\sum_{i=1}^m\sum_{j=1}^n a_{ij}^2}$.

1. $||A||_F = \text{tr}(A^T A)^{\frac{1}{2}}$.

> **Proof (*)**:
$$
A^T A =
\begin{bmatrix}
\underline{a}_1^T \\
... \\
\underline{a}_n^T
\end{bmatrix}
\begin{bmatrix}
\underline{a}_1 & ... & \underline{a}_n
\end{bmatrix} =
\begin{bmatrix}
\underline{a}_1^T \underline{a}_1 & ... & \underline{a}_1^T \underline{a}_n \\
... & ... & ... \\
\underline{a}_n^T \underline{a}_1 & ... & \underline{a}_n^T \underline{a}_n
\end{bmatrix} \text{.}
$$

> Then $\text{tr}(A^T A) = \sum_{j=1}^n \underline{a}_j^T \underline{a}_j = \sum_{i=1}^m \sum_{j=1}^n a_{ij}^2 = ||A||_F^2$.

2. $||A||_F = \text{tr}(A A^T)^{\frac{1}{2}}$.

> **Proof (*)**: it follows from the cyclic property of the trace.

3. $||A||_F = ||UA||_F = ||AV||_F$ for every orthogonal matrices $U \in \mathbb{R}^{m \times n}$, $V \in \mathbb{R}^{n \times n}$.

> **Proof (*)**:
$$
||UA||_F = \text{tr}(A^T U^T U A)^{\frac{1}{2}} = \text{tr}(A^T A)^{\frac{1}{2}} = ||A||_F\text{;}
$$

$$
||AV||_F = \text{tr}(A V V^T A^T)^{\frac{1}{2}} = \text{tr}(A A^T)^{\frac{1}{2}} = ||A||_F \text{.}
$$

4. $||A||_F = \sqrt{\sum_{i=1}^r \sigma_i^2}$.

> **Proof (*)**:

$$
||A||_F = ||U \Sigma V^T||_F = ||\Sigma||_F = \sqrt{\sum_{i=1}^r \sigma_i^2} \text{.}
$$

---

### $p$-norm

- Let $A \in \mathbb{R}^{m \times n}, p \in \mathbb{R}, p \geq 1$, we define the **$p$-norm of A** as
$$
||A||_p = \max_{\underline{x} \in \mathbb{R}^n, \underline{x} \neq \underline{0}_n} \frac{||A \underline{x}||_p}{||\underline{x}||_p}
$$
> where the $p$-norm of $\underline{x} \in \mathbb{R}^n$ is
$$
||\underline{x}||_p = (\sum_{i=1}^n x_i^p)^{\frac{1}{p}} \text{.}
$$

We will prove in a moment that, for $p = 2$,
$$
\{ \frac{||A \underline{x}||_p}{||\underline{x}||_p} | \underline{x} \in \mathbb{R}^n, \underline{x} \neq \underline{0}_n \}
$$
admits maximum, hence $||A||_p$ is well defined.

1. $\{ \frac{||A \underline{x}||_p}{||\underline{x}||_p} | \underline{x} \in \mathbb{R}^n, \underline{x} \neq \underline{0}_n \} = \{ ||A \underline{u}||_p | \underline{u} \in \mathbb{R}^n, ||\underline{u}|| = 1 \}$.

> **Proof**: Let $\underline{x} \in \mathbb{R}^n$, $\frac{||A \underline{x}||_p}{||\underline{x}||_p} = ||A \frac{\underline{x}_p}{||\underline{x}||_p}||$ where $||\frac{\underline{x}_p}{||\underline{x}||_p}|| = 1$.
The converse inclusion is straightforward.

2. $||A||_2 = \sigma_1$.

> **Proof (*)**: By property 2 of the SVD $||A \underline{x}||_2 \leq \sigma_1 ||\underline{x}||_2$. Furthermore $||A \underline{v}_1||_2 = ||\sum_{i=1}^r \sigma_i \underline{u}_i \underline{v}_i^T \underline{v}_1||_2 = \sigma_1 || \underline{u}_1 ||_2 = \sigma_1 1 = \sigma_1 || \underline{v}_1 ||_2$.

## Eckart-Young theorem

- Let $A \in \mathbb{R}^{m \times n}$ with $r(A) = r$. We define the **rank $k$ approximation of $A$** for $k \leq r$ as
$$
A_k = \sum_{i=1}^k \sigma_i \underline{u}_i \underline{v}_i^T \text{.}
$$

- **Eckart-Young theorem**: Let $||\text{.}|| = ||\text{.}||_F$ or $||\text{.}|| = ||\text{.}||_2$, $A \in \mathbb{R}^{m \times n}$, $r = r(A)$, $k \in \{ 0, ..., r \}$. Then we have
$$
||A - A_k|| \leq ||A - B||
$$
> for every $B \in \mathbb{R}^{m \times n}$ with $r(B) = k$.

---

> Furthermore
$$
||A - A_k|| = \begin{cases}
\sigma_{k+1} \text{ if } ||\text{.}|| = ||\text{.}||_2 \\
\sqrt{\sum_{i=k+1}^r \sigma_i^2} \text{ if } ||\text{.}|| = ||\text{.}||_F
\end{cases}
$$

> **1st proof in $||\text{.}||_F$**: we will prove a stronger statement: let $B \in \mathbb{R}^{m \times n}$ be a matrix s.t. $r(B) \leq k$ and $||A - B||_F \leq ||A - B'||_F$ for every matrix $B'$ with **$r(B') \leq k$**. Then $B = A_k$.
By the SVD and from the fact that $r(B) \leq k$:
$$
B = U_B \begin{bmatrix}
D & O_{k \times (n-k)} \\
O_{(m-k) \times k} & O_{(m-k) \times (n-k)}
\end{bmatrix} V_B^T
$$
> where $D \in \mathbb{R}^{k \times k}$ is a diagonal matrix. (_Since a priori we don't know $r(B)$, we don't know that all the values on the diagonal of $D$ are stricly positive_).

> Let $M = U_B^T A V_B$. As every other matrix, we can write
$$
M = \begin{bmatrix}
L + E + R & F \\
G & H
\end{bmatrix}
$$
> where $L, E, R \in \mathbb{R}^{k \times k}$, $L$ is strictly lower triangular, $E$ is diagonal, $R$ is strictly upper triangular, $F \in \mathbb{R}^{k \times n-k}$, $G \in \mathbb{R}^{m-k \times k}$, $H \in \mathbb{R}^{m-k \times n-k}$.
Then
$$
A = U_B M V_B^T \text{.}
$$
> Let
$$
C_1 = U_B \begin{bmatrix}
L+D+R & F \\
O_{(m-k) \times k} & O_{(m-k)\times(n-k)}
\end{bmatrix} V_B^T \text{.}
$$
> Observe that $r(C_1) \leq k$ since:
> - $U_B$ and $V_B^T$ are invertible matrices which preserve the rank (_in particular it is clear that $N(P A) = N(A)$ and we proved in the linear algebra refresher that $\dim N(A P) = \dim N(A)$ for every invertible matrix $P$_);
> - $r(C_1) = r(C_1^T)$ (_this holds for every matrix_);
> - $C_1$ has $m-k$ rows equal to $\underline{0}_n^T$, hence $m - r(C_1) = \dim N(C_1^T) \geq m - k$.

> Furthermore
$$
||A - B||_F^2 = ||U_B \begin{bmatrix} L+E+R-D & F \\
G & H\end{bmatrix} V_B^T||_F^2 = ||\begin{bmatrix} L+E+R-D & F \\
G & H\end{bmatrix}||_F^2 =
$$

---

$$
= ||\begin{bmatrix}
E - D & O_{k \times (n -k )} \\
G & H
\end{bmatrix}||_F^2 + ||L||_F^2 + ||R||_F^2 + ||F||_F^2 =
$$

$$
= ||U_B \begin{bmatrix}
(L+E+R)-(L+D+R) & F - F \\
G - O_{(m-k) \times k} & H - O_{(m-k) \times (n-k)}
\end{bmatrix} V_B^T||_F^2 +
$$

$$
||L||_F^2 + ||R||_F^2 + ||F||_F^2 = ||A - C_1||_F^2 + ||L||_F^2 + ||R||_F^2 + ||F||_F^2 \text{.}
$$

> But, by hypothesis, $||A - B||_F^2 \leq ||A - C_1||_F^2$, hence it must be $L = R = O_{k \times k}$, and $F = O_{k \times (n-k)}$.

> Analogously through
$$
C_2 = U_B \begin{bmatrix}
L+D+R & O_{k \times (n-k)} \\
G & O_{(m-k) \times (n-k)}
\end{bmatrix} V_B^T
$$
> we can prove that $G = O_{(m-k) \times k}$.
Hence:
$$
M = \begin{bmatrix}
E & O_{k \times (n-k)} \\
O_{(m-k) \times k} & H
\end{bmatrix} \text{.}
$$

> By the SVD:
$$
H = U_H \Sigma_H V_H^T \text{.}
$$

> Let
$$
U = U_B \begin{bmatrix}
I_k & O_{k \times (m-k)} \\
O_{(m-k) \times k} & U_H
\end{bmatrix}, V = V_B \begin{bmatrix}
I_k & O_{n \times (n-k)} \\
O_{(n-k) \times k} & V_H
\end{bmatrix},
$$

$$
\Sigma = \begin{bmatrix}
E & O_{k \times (n-k)} \\
O_{(m-k) \times k} & \Sigma_H
\end{bmatrix}
\text{.}
$$
> Then, by straightforward block matrix multiplication:
> - $U^T U = I_m$, $V^T V = I_n$;
> - $U \Sigma V^T = A$;
> - $B = U \begin{bmatrix} D & O_{k \times (n-k)} \\ O_{(m-k) \times k} & O_{(m-k) \times (n-k)} \end{bmatrix} V^T$.

> Remark: we still have to prove that $U \Sigma V^T$ is the SVD decomposition of $A$, at this time we've only given names to matrices.

> By the uniqueness of the SVD, on the diagonal of $E$, and on the pseudodiagonal of $\Sigma_H$ there are the singular values of $A$, **with no guarantee on the order**.

---

> Since $B$ is the matrix with rank smaller or equal to $k$, closer to $A$:
> 1. $D = E$, otherwise
$$
U \begin{bmatrix}
E & O_{k \times (n-k)} \\
O_{(m-k) \times k} & O_{(m-k) \times (n-k)}
\end{bmatrix} V^T
$$
>> would be closer to $A$ than $B$;
> 2. $E = \text{diag}\{ \sigma_1, ..., \sigma_k \}$.
To understand why this is true, first of all observe that
$$
\Sigma = \begin{bmatrix}
E & O_{k \times (n-k)} \\
O_{(m-k) \times k} & \Sigma_H
\end{bmatrix} =
$$

$$
= \sum_{i=1}^k d_i \underline{e}_i^{(m)} (\underline{e}_i^{(n)})^T + \sum_{i=k+1}^{\min(m,n)} h_{i-k} \underline{e}_i^{(m)} (\underline{e}_i^{(n)})^T =
$$

$$
= \sum_{i=1}^{\min(m,n)} a_i \underline{e}_i^{(m)} (\underline{e}_i^{(n)})^T
$$
>> where $d_1, ..., d_k$ are the values on the diagonal of $D = E$; $h_1, ..., h_{\min(m,n)-k}$ are the values on the pseudodiagonal of $\Sigma_H$;
$$
a_i = \begin{cases}
d_i \text{ if } i \in \{ 1, ..., k \} \\
h_{i-k} \text{ if } i \in \{ k+1, ..., \min(m,n) \}
\end{cases} \text{;}
$$
>> $\underline{e}_i^{(j)}$ is the $i$-th "canonical vector" of $\mathbb{R}^j$.
By what we remarked before about the values on the pseudodiagonal of $\Sigma$:
$$
a_i = \sigma_{f(i)}
$$
>> with $f(i) \in \{ 1, ..., \min(m,n) \}$, $f(i) \neq f(j)$ for every $i,j \in \{ 1, ..., \min(m,n) \}$, $i \neq j$, if we define $\sigma_{r+1} = ... = \sigma_{\min(m,n)} = 0$.
Furthermore, since $E = D$, and both $D$ and $\Sigma_H$ have been obtained from the SVD, then $d_1 \geq ... \geq d_k$, and $h_1 \geq ... \geq h_{\min(m,n)}$, then, wlog, we can assume that $f(1) < ... < f(k)$, and $f(k+1) < ... < f(\min(m,n))$ (for, if it were $f(i) \geq f(i+1)$ for some $i \in \{1, ..., k-1\}$, then $d_i = \sigma_{f(i)} \leq \sigma_{f(i+1)} = d_{i+1}$, but $d_{i+1} \leq d_i$, hence $\sigma_{f(i)} = \sigma_{f(i+1)}$, and so we could redefine $f$ swapping the values of $f(i)$ and $f(i+1)$).

>> Now assume that $d_{\hat{i}} \neq \sigma_{\hat{i}}$ for some $\hat{i} \in \{ 1, ..., k \}$.

---

>> First of all, since $f(1) \geq 1$, and $f(i) > f(i-1)$ for $i \in \{2, ..., k\}$, then $f(i) \geq i$ for $i \in \{ 1, ..., k \}$, hence $d_i = \sigma_{f(i)} \leq \sigma_i$. Then, $d_{\hat{i}} \neq \sigma_{\hat{i}}$ implies $d_{\hat{i}} < \sigma_{\hat{i}}$.
Since $|\{ 1, ..., \hat{i} \}| = \hat{i}$, $|\{ f(1), ..., f(\hat{i}-1) \}| = \hat{i} - 1$, there must exist $\hat{j} \in \{ 1, ..., \hat{i} \}$ s.t. $\hat{j} \not \in \{ f(1), ..., f(\hat{i}-1) \}$.
Furthermore, it must be $f(\hat{i}) \neq \hat{i}$ (otherwise $d_{\hat{i}} = \sigma_{\hat{i}}$), which implies $f(\hat{i}) > \hat{i}$, hence $f(i) > \hat{i} \geq \hat{j}$ for every $i \in \{ \hat{i}, ..., k \}$.
Then $\hat{j} = f(\hat{l})$ for $\hat{l} \in \{ k+1, ..., \min(m,n) \}$ ($f$ is a bijection on $\{ 1, ..., \min(m,n) \}$).
Finally $a_{\hat{l}} = \sigma_{f(\hat{l})} = \sigma_{\hat{j}} \geq \sigma_{\hat{i}} > d_{\hat{i}}$.
Now consider the matrix
$$
J = U(\sum_{i=1}^{\hat{i}-1} d_i \underline{e}_i^{(m)} (\underline{e}_i^{(n)})^T + a_{\hat{l}} \underline{e}_{\hat{l}}^{(m)} (\underline{e}_{\hat{l}}^{(n)})^T + \sum_{i = \hat{i} + 1}^k d_i \underline{e}_i^{(m)} (\underline{e}_i^{(n)})^T ) V^T \text{.}
$$
>> Then
$$
||A - J||_F^2 = a_{k+1}^2 + ... + a_{\hat{l}-1}^2 + d_{\hat{i}}^2 + a_{\hat{l}+1}^2 + ... + a_{\min(m,n)}^2 <
$$

$$
< a_{k+1}^2 + ... + a_{\hat{l}-1}^2 + a_{\hat{l}}^2 + a_{\hat{l}+1}^2 + ... + a_{\min(m,n)}^2 = ||A - B||_F^2 \text{,}
$$
>> but $J$ has rank $k$, hence this violates our hypothesis.
So it must be $d_i = \sigma_i$ for every $i \in \{ 1, ..., k \}$ (_as we wanted to prove_).

> 3. The pseudodiagonal of $\Sigma_H$ corresponds to $\sigma_{k+1}, ..., \sigma_{\min(m,n)}$ in this order.
>> This follows from the fact that, in virtue of 2, in $\Sigma_H$ there are the values $\sigma_{k+1}, ..., \sigma_{\min(m,n)}$, and they must be in the right order since $\Sigma_H$ has been obtained from the SVD.

> 1 and 2 imply that $\Sigma = \Sigma_A$, which in turn implies $U = U_A$, and $V = V_A$ (that is $U \Sigma V^T$ is the SVD decomposition of $A$).
Finally (_remembering that $D = E = \text{diag}\{ \sigma_1, ..., \sigma_k \}$_)
$$
B = U \begin{bmatrix}
D & O_{k \times (n-k)} \\
O_{(m-k) \times k} & O_{(m-k) \times (n-k)}
\end{bmatrix} V^T = U_A
\begin{bmatrix}
\begin{bmatrix}
\sigma_1 & 0 & ... & 0 \\
0 & ... & ... & ... \\
... & ... & ... & 0 \\
0 & ... & 0 & \sigma_k
\end{bmatrix} & O_{k \times (n-k)} \\
O_{(m-k) \times k} & O_{(m-k) \times (n-k)}
\end{bmatrix} V_A^T = A_k
$$
> as we wanted to prove.

---

> The fact that $||A - A_k||_F = \sqrt{i=k+1}^r \sigma_i^2$ follows from the fact htat $A-A_K = \sum_{i=k+1}^r \sigma_i \underline{u}_i \underline{v}_i^T$, by the uniqueness of the SVD, and by the properties of the Frobenius norm.

- **Weyl's inequality**: let $X, Y \in \mathbb{R}^{m \times n}$, $\sigma_i(A)$ be the $i$-th singular value of $A$. Then:
$$
\sigma_{i+j-1}(X+Y) \leq \sigma_i(X) + \sigma_j(Y) \text{.}
$$

> **2nd proof in $||\text{.}||_F$ (*)**: let $X = A - B$, $Y = B$. Then, by the Weyl's inequality:
$$
\sigma_{i+k}(A) = \sigma_{i+k}(X+Y) \leq \sigma_i(X) + \sigma_{k+1}(Y) = \sigma_i(A-B) + \sigma_{k+1}(B) \text{.}
$$
> Since, $r(B) = k$, $\sigma_{k+1}(B) = 0$, hence:
$$
\sigma_{i+k}(A) = \sigma_i(A-B) \text{.}
$$

> Then:

$$
||A-A_k||_F^2 = \sum_{i=k+1}^r \sigma_i^2(A) = \sum_{i=1}^{r-k} \sigma_{i+k}^2(A) = \sum_{i=1}^{r-k} \sigma_i^2(A-B) \leq
$$

$$
\leq \sum_{i=1}^{r(A-B)} \sigma_i^2(A-B) = ||A-B||_F^2 \text{.}
$$

> **Proof in $||\text{.}||_2$ (*)**: assume $k < r$ since the proof for $k = r$ is straightforward.
It must be $\dim(\text{span}\{ \underline{v}_1, ..., \underline{v}_{k+1} \} \cap N(B)) \geq 1$ (_otherwise there would be more than $n$ linearly independent vectors in $\mathbb{R}^n$_). There there exists $\underline{w} \in \text{span}\{ \underline{v}_1, ..., \underline{v}_{k+1} \} \cap N(B)$, $\underline{w} \neq \underline{0}_n$.
Furthermore:
$$
A \underline{w} = \sum_{i=1}^r \sum_{j=1}^{k+1} \sigma_i \alpha_j \underline{u}_i \underline{v}_i^T \underline{v}_j = \sum_{j=1}^{k+1} \sigma_j \alpha_j \underline{u}_j \cdot 1 \text{ since } k+1 \leq r \text{,}
$$

$$
B \underline{w} = \underline{0}_m \text{.}
$$
> Hence:
$$
||(A-B) \underline{w}||_2^2 = ||\sum_{j=1}^{k+1} \sigma_j \alpha_j \underline{u}_j||_2^2 = \sum_{j=1}^{k+1} \sigma_j^2 \alpha_j^2 ||\underline{u}_j||_2^2 \geq \sigma_{k+1} \sum_{j=1}^{k+1} \alpha_j^2 ||\underline{v}_j||_2^2 =
$$

$$
= \sigma_k^2 || \sum_{j=1}^{k+1} \alpha_j \underline{v}_j ||_2^2 = \sigma_k^2 ||\underline{w}||_2^2 \text{.}
$$
> Since $\underline{w} \neq \underline{0}_n$, this implies $||A-B||_2 \geq \sigma_k = ||A - A_k||_2$ (_as we wanted to prove_).

---

## Principal Component Analysis (PCA)

Let $A \in \mathbb{R}^{p \times n}$ be a matrix which represents a dataset with $n$ samples, each of which has $p$ features. That is, the columns of $A$ are samples (it is possible to make an equivalent treatment where rows are samples).

Let's derive the expression for the sample covariance matrix of the data in $A$.
First of all we need to remove the sample mean of each feature from every sample:
$$
\overline{A} = \begin{bmatrix} \underline{a}_1 - \underline{\overline{a}} & ... & \underline{a}_n - \underline{\overline{a}} \end{bmatrix} = A - \underline{\overline{a}} \underline{1}_n^T = A - (\frac{1}{n}A \underline{1}_n) \underline{1}_n^T =
$$

$$
= A (I_n - \frac{1}{n} \underline{1}_n \underline{1}_n^T) = A H
$$

where $H = I_n - \frac{1}{n} \underline{1}_n \underline{1}_n^T$.

Let $\overline{F} = \overline{A}^T$, then $\underline{\overline{f}}_i$ is a vector with all the $n$ sampled values of the $i$-th feature, to which the sample mean has been subtracted, for $i \in \{ 1, ..., p \}$. Hence, the covariance matrix is:
$$
K = \frac{1}{n-1} \begin{bmatrix}
\underline{\overline{f}}_1^T \underline{\overline{f}}_1 & ... & \underline{\overline{f}}_1^T \underline{\overline{f}}_p \\
... & ... & ... \\
\underline{\overline{f}}_p^T \underline{\overline{f}}_1 & ... & \underline{\overline{f}}_p^T \underline{\overline{f}}_p
\end{bmatrix} = \frac{1}{n-1} \begin{bmatrix} \underline{\overline{f}}_1^T \\ ... \\ \underline{\overline{f}}_p^T \end{bmatrix} \begin{bmatrix} \underline{\overline{f}}_1 & ... & \underline{\overline{f}}_p \end{bmatrix} = \frac{1}{n-1} \overline{F}^T \overline{F} = \frac{1}{n-1} \overline{A} \overline{A}^T \text{.}
$$

On the diagonal of $K$ we find the sampled variances, the other entries of $K$ are the sampled covariances of pairs of distinct features.

**PCA** consists in finding a transformation, described by the matrix $Q \in \mathbb{R}^{k \times p}$ (with $k \leq p$) such that the sampled variances of the new $k$ features are maximal while the sampled covariances of pairs of distinct new feautures are minimal. In particular we want the features to be ordered by sampled variance, from the greatest to the lowest.
Furthermore, we impose $||Q||_2 = 1$, since, otherwise we can increase arbitrarily the variance of the dataset by multiplying $Q$ with a constant $\gamma > 1$ larger and larger.

The "transformed" dataset is:
$$
\begin{bmatrix} Q \underline{\overline{a}}_1 & ... & Q \underline{\overline{a}}_n \end{bmatrix} = Q \overline{A} \text{,}
$$
hence, the corresponding covariance matrix is:
$$
K_Q = \frac{1}{n-1} Q \overline{A} \overline{A}^T Q^T \text{.}
$$

Observe that, the sum of the variances of the features produced by $Q$ is:
$$
\text{tr}(K_Q) = \frac{1}{n-1} \text{tr}(Q \overline{A} \overline{A}^T Q^T) = \frac{1}{n-1} ||Q \overline{A}||_F^2 \text{.}
$$

---

Let
$$
Q = \begin{bmatrix}
\underline{q}_1^T \\
... \\
\underline{q}_k^T
\end{bmatrix} \text{,}
$$
then
$$
||Q \overline{A}||_F^2  = ||\begin{bmatrix}
\underline{q}_1^T \\
... \\
\underline{q}_k^T
\end{bmatrix} \sum_{i=1}^{r(\overline{A})} \sigma_i(\overline{A}) \underline{u}_i \underline{v}_i^T||_F^2 =
||\begin{bmatrix}
\sum_{i=1}^{r(\overline{A})} \sigma_i(\overline{A}) (\underline{q}_1^T \underline{u}_i) \underline{v}_i^T \\
... \\
\sum_{i=1}^{r(\overline{A})} \sigma_i(\overline{A}) (\underline{q}_k^T \underline{u}_i) \underline{v}_i^T
\end{bmatrix}||_F^2 =
$$

$$
= ||\sum_{i=1}^{r(\overline{A})} \sigma_i(\overline{A}) (\underline{q}_1^T \underline{u}_i) \underline{v}_i||^2 + ... +
|| \sum_{i=1}^{r(\overline{A})} \sigma_i(\overline{A}) (\underline{q}_k^T \underline{u}_i) \underline{v}_i ||^2 = 
$$

$$
= \sum_{i=1}^{r(\overline{A})} \sigma_i^2(\overline{A}) (\underline{q}_1^T \underline{u}_i)^2 ||\underline{v}_i||^2 + ... +
 \sum_{i=1}^{r(\overline{A})} \sigma_i^2(\overline{A}) (\underline{q}_k^T \underline{u}_i)^2 ||\underline{v}_i ||^2 =
$$

$$
= \sum_{j=1}^k \sum_{i=1}^{r(\overline{A})} \sigma_i^2(\overline{A}) (\underline{q}_j^T \underline{u}_i)^2 = \sum_{i=1}^{r(\overline{A})} \sigma_i^2(\overline{A}) \sum_{j=1}^k (\underline{q}_j^T \underline{u}_i)^2 = \sum_{i=1}^{r(\overline{A})} \sigma_i^2(\overline{A}) ||Q \underline{u}_i||^2 \text{.}
$$

Since $||Q||_2 = 1$, then $||Q \underline{u}_i||^2 \leq 1$.
Furthermore, it is straightforward to check from the SVD (exploiting the uniqueness) that $Q^T$ has the same singular values of $Q$, hence $||Q^T||_2 = ||Q||_2 = 1$ by property 2 of the 2-norm.
Then
$$
\sum_{i=1}^{r(\overline{A})} ||Q \underline{u}_i||^2 \leq \sum_{i=1}^p ||Q \underline{u}_i||^2 = ||\begin{bmatrix} Q \underline{u}_1 & ... & Q \underline{u}_p \end{bmatrix}||_F^2 = ||QU||_F^2 = ||Q||_F^2 =
$$

$$
= ||Q^T||_F^2 = ||Q^T \underline{e}_1||^2 + ... + ||Q^T \underline{e}_k|| \leq 1 + ... + 1 = k \text{.}
$$

The last inequality follows from the fact that $||Q^T||_2 = 1$.

Let $r = r(\overline{A}), \alpha_i = \sigma_i^2(\overline{A}), \beta_i = ||Q \underline{u}_i||^2$ for $i \in \{ 1, ..., r \}$.
Then, we have that $\beta_i \leq 1$ for $i \in \{ 1, ..., r \}$, and $\beta_1 + ... + \beta_r \leq k$.

Furthermore $\alpha_1 \geq ... \geq \alpha_r$.
Then:
$$
\alpha_1 + ... + \alpha_k - \beta_1 \alpha_1 - ... - \beta_r \alpha_r = (1-\beta_1) \alpha_1 + ... + (1-\beta_k) \alpha_k - \beta_{k+1} \alpha_{k+1} + ... + \beta_r \alpha_r \geq
$$

---

$$
\geq \alpha_k \sum_{i=1}^k (1-\beta_i) - \alpha_k \sum_{i=k+1}^r \beta_i \alpha_i = \alpha_k (k - \sum_{i=1}^r \beta_i) \geq 0 \text{.}
$$

Hence:
$$
||Q \overline{A}||_F^2 = \sum_{i=1}^{r} \alpha_i \beta_i \leq \sum_{i=1}^k \alpha_i = \sum_{i=1}^k \sigma_i^2(\overline{A}) \text{.}
$$

Now, let
$$
U_k = \begin{bmatrix} \underline{u}_1 & ... & \underline{u}_k \end{bmatrix} \text{.}
$$

Then
$$
||U_k^T \overline{A}||_F^2 = ||\begin{bmatrix} \underline{u}_1^T \\ ... \\ \underline{u}_k^T \end{bmatrix} \sum_{i=1}^r \sigma_i(\overline{A}) \underline{u}_i \underline{v}_i^T||_F^2 = ||\begin{bmatrix} \sigma_1(\overline{A}) \underline{v}_1^T \\ ... \\ \sigma_k(\overline{A}) \underline{v}_k^T \end{bmatrix}||_F^2 = \sum_{i=1}^k \sigma_i^2(\overline{A}) \geq ||Q \overline{A}||_F^2
$$
for every matrix $Q \in \mathbb{R}^{k \times p}$ s.t. $||Q||_2 = 1$ (observe that $||U_k^T||_2 = ||U_k||_2 = 1$ since the columns of $U_k$ are orthonormal, furthermore $U_k^T \in \mathbb{R}^{k \times p}$).

From the relation between $\text{tr}(K_Q)$ and $||Q \overline{A}||_F^2$, we conclude that $U_k^T$ leads to maximal variance.

Finally observe that:
$$
K_{U_k^T} = \frac{1}{n-1} U_k^T \overline{A} \overline{A}^T U_k =
\frac{1}{n-1} (\begin{bmatrix}
\underline{u}_1^T \\
... \\
\underline{u}_k^T
\end{bmatrix}
\sum_{i=1}^r \sigma_i(\overline{A}) \underline{u}_i \underline{v}_i^T)
(\begin{bmatrix}
\underline{u}_1^T \\
... \\
\underline{u}_k^T
\end{bmatrix}
\sum_{i=1}^r \sigma_i(\overline{A}) \underline{u}_i \underline{v}_i^T)^T =
$$

$$
= \frac{1}{n-1} \begin{bmatrix}
\sigma_1(\overline{A}) \underline{v}_1^T \\
... \\
\sigma_k(\overline{A}) \underline{v}_k^T
\end{bmatrix}
\begin{bmatrix}
\sigma_1(\overline{A}) \underline{v}_1 & ... & \sigma_k(\overline{A}) \underline{v}_k
\end{bmatrix} = \frac{1}{n-1} \begin{bmatrix}
\sigma_1^2(\overline{A}) & 0 & ... & 0 \\
0 & ... & ... & ... \\
... & ... & ... & 0 \\
0 & ... & 0 & \sigma_k^2(\overline{A})
\end{bmatrix} \text{.}
$$

That is, $U^T$ minimizes the sampled covariances of pairs of distinct features (they are 0). Hence, it is the matrix we were looking for.

In particular, we call:
- **principal components**: the transformed dataset $U_k^T \overline{A}$;
- **principal directions**: $\underline{u}_1$, ... $\underline{u}_k$.

**Remark**: the principal components are the coordinates (w.r.t. the principal directions) of the projections of the samples onto the space which is defined by the principal directions.

---

### Reconstructing the dataset

The transformation derived through the PCA has also another important property: it leads to the minimum reconstruction error of the dataset from the principal components.
In particular, we can "invert" the transformation by multiplying the principal components by $U_k$. The result is:
$$
U_k U_k^T \overline{A} = U_k \begin{bmatrix}
\underline{u}_1^T \\
... \\
\underline{u}_k^T
\end{bmatrix} \sum_{i=1}^r \sigma_i(\overline{A}) \underline{u}_i \underline{v}_i^T = \begin{bmatrix} \underline{u}_1 & ... & \underline{u}_k \end{bmatrix} \begin{bmatrix}
\sigma_1(\overline{A}) \underline{v}_1^T \\
... \\
\sigma_k(\overline{A}) \underline{v}_k^T
\end{bmatrix} =
$$

$$
= \sum_{i=1}^k \sigma_i(\overline{A}) \underline{u}_i \underline{v}_i^T = \overline{A}_k \text{.}
$$

Then $||\overline{A} - U_k U_k^T \overline{A}||_F = ||\overline{A} - \overline{A}_k||_F$ is minimum (if we restrict to rank $k$ matrices).

**Remark**: the reconstructed dataset is the orthogonal projection of the samples onto the space which is defined by the principal directions.

## How to choose the value of $k$ in the truncated SVD?

1. The first approach when choosing a suitable value $k$ in order to approximate $A \in \mathbb{R}^{m \times n}$ with $A_k$ is to preserve a certain fraction of the variance of $A$. In particular, the **variance of $A$** is given by
$$
||A||_F^2 = \sum_{i=1}^{r(A)} \sigma_i^2(A) \text{.}
$$
> Hence, fixed $\alpha \in (0, 1)$, we want to find the smaller $k \leq r(A)$ s.t.
$$
\frac{||A_k||_F^2}{||A||_F^2} = \frac{\sum_{i=1}^k\sigma_i^2(A)}{\sum_{i=1}^{r(A)} \sigma_i^2(A)} \geq \alpha \text{.}
$$

2. We can plot the singular values of $A$ and pick $k$ in the correspondance of a "jump" in the graph: that is $\sigma_k \gg \sigma_{k+1}$.

3. Suppose that
$$
A = A_{\text{true}} + \gamma A_{\text{noise}} \text{ with } \gamma > 0 \text{,}
$$
> where $A_{\text{true}}$ is the underlying low rank data, to which a gaussian noise of magnitude $\gamma$ ($\gamma A_{\text{noise}}$) has been added. In particular $A_{\text{noise}}$ has mean equal to 0 and variance equal to 1. We want to find a threshold $\tau$ such that if we select $k$ which guarantees $\sigma_k > \tau$, and $\sigma_{k+1} \leq \tau$, then $A_k \approx A_{\text{true}}$.

---

> 3.1 If $\gamma$ is known
>> 3.1.1 and $A \in \mathbb{R}^{n \times n}$
>>> then
$$
\tau = \frac{4}{\sqrt{3}} \sqrt{n} \gamma \text{;}
$$
>> 3.1.2 and $A \in \mathbb{R}^{m \times n}$
>>> 3.1.2.1 with $m \ll n$
>>>> then
$$
\tau = \lambda(\beta) \sqrt{n} \gamma \text{ with } \beta = \frac{n}{m} \text{ (aspect ratio) with}
$$

$$
\lambda(\beta) = (2(\beta + 1) + \frac{8 \beta}{(\beta+1) + (\beta^2 + 14 \beta + 1)^\frac{1}{2}})^{\frac{1}{2}} \text{;}
$$

>>> 3.1.2.2 with $n \ll m$
$$
\text{same as before with } \beta = \frac{m}{n} \text{;}
$$

> 3.2 If $\gamma$ is unknown
>> then
$$
\tau = w(\beta) \frac{1}{r(A)}\sum_{i=1}^{r(A)} \sigma_i(A) \text{ (average singular value), and }
$$

$$
w(\beta) = \frac{\lambda(\beta)}{\mu_\beta} \text{,} \beta = \frac{n}{m} \text{,}
$$

$$
\lambda \text{ defined as before}, \mu_\beta \text{ such that }
$$

$$
\int_{(1-\beta)^2}^{\mu_\beta} \frac{\{ [(1+\sqrt{\beta})^2 - t][t - (1-\sqrt{\beta})^2] \}^{\frac{1}{2}}}{2 \pi t} dt = \frac{1}{2} \text{.}
$$

---

## Randomized Singular Value Decomposition (rSVD)

**rSVD** is a technique for computing a good approximation of the truncated SVD of a matrix in a really fast way.

Let $A \in \mathbb{R}^{m \times n}$ and suppose that we want to approximate $A_k$ for $k \leq r(A)$.
First of all we have to sample $k$ gaussian vectors $\underline{w}_1, ..., \underline{w}_k \in \mathbb{R}^n$ (with mean 0 and variance 1) and put them into a matrix:
$$
\Omega = \begin{bmatrix} \underline{w}_1 & ... & \underline{w}_k \end{bmatrix} \in \mathbb{R}^{n \times k} \text{.}
$$

Now, consider the matrix:
$$
Y = A \Omega = A \begin{bmatrix} \underline{w}_1 & ... & \underline{w}_k \end{bmatrix} = \begin{bmatrix} A \underline{w}_1 & ... & A \underline{w}_k \end{bmatrix} \text{;}
$$
we can regard every column of $Y$ as a sample from $C(A)$.
Observe the following, if $\sigma_1(A) \gg \sigma_2(A) \gg ...$, then
$$
A \underline{w}_1 = \sum_{i=1}^{r(A)} \sigma_i(A) \underline{u}_i \underline{v}_i^T \underline{w}_1 = \sum_{i=1}^{r(A)} \sigma_i(A) (\underline{v}_i^T \underline{w}_1) \underline{u}_i \approx \sigma_1(A) (\underline{v}_1^T \underline{w}_1) \underline{u}_1
$$
since we expect $\underline{v}_i^T \underline{w}_1$ to have similar magnitudes for every $i \in \{ 1, ..., r(A) \}$.
Analogously, if we remove from $A \underline{w}_2$ the orthogonal projection onto $A \underline{w}_1$ we get:
$$
A \underline{w}_2 - \frac{A \underline{w}_1 A \underline{w}_1^T}{A \underline{w}_1^T A \underline{w}_1^T} A \underline{w}_2 = \sum_{i=1}^{r(A)} \sigma_i(A) (\underline{v}_i^T \underline{w}_2) \underline{u}_i - \frac{A \underline{w}_1 A \underline{w}_1^T}{A \underline{w}_1^T A \underline{w}_1^T} \sum_{i=1}^{r(A)} \sigma_i(A) (\underline{v}_i^T \underline{w}_2) \underline{u}_i \approx
$$

$$
\approx \sum_{i=1}^{r(A)} \sigma_i(A) (\underline{v}_i^T \underline{w}_2) \underline{u}_i - \frac{\sigma_1^2(A) (\underline{v}_1^T \underline{w}_1)^2 \underline{u}_1 \underline{u}_1^T}{\sigma_1^2(A) (\underline{v}_1^T \underline{w}_1)^2 \underline{u}_1^T \underline{u}_1} \sum_{i=1}^{r(A)} \sigma_i(A) (\underline{v}_i^T \underline{w}_2) \underline{u}_i = 
$$

$$
= \sum_{i=1}^{r(A)} \sigma_i(A) (\underline{v}_i^T \underline{w}_2) \underline{u}_i - \sigma_1(A) (\underline{v}_1^T \underline{w}_2) \underline{u}_1 = \sum_{i=2}^{r(A)} \sigma_i(A) (\underline{v}_i^T \underline{w}_2) \underline{u}_i \approx \sigma_2(A) (\underline{v}_i^T \underline{w}_2) \underline{u}_2 \text{.}
$$

By iterating this process through QR factorization:
$$
Y = QR \text{ and } Q \approx U_k \text{ (because of what we observed).}
$$

Then:
$$
Q Q^T \approx U_k U_k^T = \underline{u}_1 \underline{u}_1^T  + ... + \underline{u}_k \underline{u}_k^T
$$
approximates the orthogonal projection matrix onto $\text{span}\{ \underline{u}_1, ..., \underline{u}_k \}$. Hence:
$$
Q Q^T A \approx (\underline{u}_1 \underline{u}_1^T + ... + \underline{u}_k \underline{u}_k^T ) \sum_{i=1}^{r(A)} \sigma_i(A) \underline{u}_i \underline{v}_i^T = \sum_{i=1}^k \sigma_i(A) \underline{u}_i \underline{v}_i^T = A_k \text{.}
$$

---

Now let $B = Q^T A$. Note that $B \in \mathbb{R}^{k \times n}$ and usually $k$ and $n$ are both significantly smaller than $m$, hence we can compute its svd quite fast:
$$
B = \tilde{U} \Sigma V^T \text{.}
$$
Finally:
$$
A_k \approx Q Q^T A = Q B = (Q \tilde{U}) \Sigma V^T \text{.}
$$
That is: $U_k \approx Q \tilde{U}$, $V_K \approx V$, $\Sigma_k \approx \Sigma$.

### Improvements to rSVD

- **Power iteration** is a technique which makes the decay of the singular of $A$ faster while preserving the singular vectors. It improves the result of the rSVD, since, as we've seen, we want $\sigma_1(A) \gg \sigma_2(A) \gg ...$.
It works as follows:
$$
(AA^T)^qA = (\sum_{i=1}^{r(A)} \sigma_i(A) \underline{u}_i \underline{v}_i^T \sum_{j=1}^{r(A)} \sigma_j(A) \underline{v}_j \underline{u}_j^T)^q A = (\sum_{i=1}^{r(A)} \sigma_i^2(A) \underline{u}_i \underline{u}_i^T)^q A = 
$$

$$
= \sum_{i=1}^{r(A)} \sigma_i^{2q}(A) \underline{u}_i \underline{u}_i^T A =
\sum_{i=1}^{r(A)} \sigma_i^{2q}(A) \underline{u}_i \underline{u}_i^T \sum_{j=1}^{r(A)} \sigma_j(A) \underline{u}_j \underline{v}_j^T = \sum_{i=1}^{r(A)} \sigma_i^{2q+1}(A) \underline{u}_i \underline{v}_i^T \text{.}
$$

> Hence, the decay of the singular values is exponential in the factor $q$.

- **Oversampling** consists in sampling $k+p$ with $p \geq 0$ gaussian vectors instead of $k$. Then, after the QR factorization, we take only the first $k$ columns of $Q$.

A theoretical result gurantees the goodness of the rSVD:
$$
E(||A_k - QQ^TA||_2) \leq (1 + \sqrt{\frac{k}{p-1}} + \frac{e \sqrt{k + p}}{p} \sqrt{n-k})^{\frac{1}{2q+1}} \sigma_{k+1}(A) \text{.}
$$
