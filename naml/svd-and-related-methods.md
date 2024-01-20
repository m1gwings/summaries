---
theme: summary
---
# SVD & related methods

<div class="author">

Cristiano Migali

</div>

## Singular value decomposition (SVD)

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

