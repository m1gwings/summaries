---
marp: true
theme: summary
math: mathjax
---
# Linear algebra refresher

<div class="author">

Cristiano Migali

</div>

## Notation

- Every vector $\underline{v} \in \mathbb{R}^n$ has to be intended as a **column vector**.

- Given a matrix $A \in \mathbb{R}^{m \times n}$, $\underline{a}_i$ is its **$i$-th column**. That is $A = \begin{bmatrix} \underline{a}_1 & ... & \underline{a}_n \end{bmatrix}$.

---

## Some definitions

We will list some definitions to remember since they are particularly relevant for the usage of LA in NAML course. The list is NOT exhaustive (that is, we will take for well known some definitions, not stated here, that will be used further on).

- Given a matrix $A \in \mathbb{R}^{m \times n}$, we define the **column space of $A$** $C(A) = \text{span}\{ \underline{a}_1, ..., \underline{a}_n \}$.

- Given a matrix $A \in \mathbb{R}^{m \times n}$, we define the **rank of $A$** $r(A) = \dim C(A)$.

- We say that $Q \in \mathbb{R}^{n \times n}$ is **orthogonal** iff $Q^T Q = I_n$.

- Let $\underline{v}, \underline{x} \in \mathbb{R}^{n \times n}$, the **orthogonal projection** of $\underline{x}$ onto $H = \text{span}\{ \underline{v} \}$ is

$$
P_H(\underline{x}) = \underline{v} \frac{\underline{v}^T \underline{x}}{\underline{v}^T \underline{v}} \text{.}
$$

> Analogously, if $\underline{v}_1, ..., \underline{v}_r$ is an **orthogonal basis** of $H$, then

$$
P_H(\underline{v}) = \sum_{i=1}^r \underline{v}_i \frac{\underline{v}_i^T \underline{x}}{\underline{v}_i^T \underline{v}_i} \text{.}
$$

- Given a matrix $A \in \mathbb{R}^{m \times n}$, we say **null space of $A$** $N(A) = \{ \underline{x} \in \mathbb{R}^n | A\underline{x} = \underline{0}_m \}$.

- Let $i, j, n \in \mathbb{N}^+$ s. t. $1 \leq i < j \leq n$. We define the **permutation matrix $P_{i,j,n}$** as

$$
P_{i,j,n} = \begin{bmatrix}
I_{i-1} & \underline{0}_{i-1} & O_{i-1 \times j-i-1} & \underline{0}_{i-1} & O_{i-1 \times n-j} \\
\underline{0}_{i-1}^T & 0 & \underline{0}_{j-i-1}^T & 1 & \underline{0}_{n-j}^T \\
O_{j-i-1 \times i-1} & \underline{0}_{j-i-1} & I_{j-i-1} & \underline{0}_{j-i-1} & O_{j-i-1 \times n-j} \\
\underline{0}_{i-1}^T & 1 & \underline{0}_{j-i-1}^T & 0 & \underline{0}_{n-j}^T \\
O_{n-j \times i-1} & \underline{0}_{n-j} & O_{n-j \times j-i-1} & \underline{0}_{n-j} & I_{n-j}
\end{bmatrix} \text{.}
$$

- Let $A \in \mathbb{R}^{n \times n}$ and $\underline{x}$ be one of its eigenvectors. We define **Rayleigh quotient** the quantity:

$$
\frac{\underline{x}^T A \underline{x}}{\underline{x}^T \underline{x}} \text{.}
$$

- Let $S \in \mathbb{R}^{n \times n}$ be a symmetric matrix. We say that $S$ is **positivie definite** iff $\underline{v}^T S \underline{v} \geq 0$ for every $\underline{v} \in \mathbb{R}^n$ and $\underline{v}^T S \underline{v} = 0$ iff $\underline{v} = \underline{0}$. We call this characterization the **energy test**.

---

- Let $P \in \mathbb{R}^{n \times n}$. $P$ is said to be a **projection matrix** iff $P^2 = P$.

- Let $P \in \mathbb{R}^{n \times n}$. $P$ is said to be an **orthogonal projection matrix** if $P$ is a projection matrix and it is symmetric.

---

## Some properties

1. Let $A \in \mathbb{R}^{m \times n}, \underline{b} \in \mathbb{R}^m$. The linear system $A \underline{x} = \underline{b}$ admits solution iff $\underline{b} \in C(A)$.

2. **Echelon form of $A$**: we can factorize every matrix $A \in \mathbb{R}^{m \times n}$ into $A = CR$ where $C \in \mathbb{R}^{m \times r}$, $R \in \mathbb{R}^{r \times n}$, and $r = r(A)$.

> **Proof**: Let $\underline{a}_{b_1}, ..., \underline{a}_{b_r}$ be a maximal set of linear independent columns of $A$ (that is a basis of $C(A)$). By definition of basis, we can write every $\underline{a}_i$ as $\underline{a}_i = r_{1i} \underline{a}_{b_1} + ... r_{ri} \underline{a}_{b_r}$. Let $C = \begin{bmatrix} \underline{a}_{b_1} & ... & \underline{a}_{b_r} \end{bmatrix}$ and $R = \begin{bmatrix} r_{ij} \end{bmatrix}$. The proof follows.

> **Remark**: We can identify a maximal set of linear independent columns by applying gaussian elimination to $A$. The result of gaussian elimination is a "stair" matrix $U$. Since elementary operations preserve the underlying linear systems: $A \underline{x} = \underline{0}_m$ iff $U \underline{x} = \underline{0}_m$. Hence $\underline{u}_{b_1}, ..., \underline{u}_{b_k}$ are linearly independent iff $\underline{a}_{b_1}, ..., \underline{a}_{b_k}$ are. Furthermore the columns in $U$ with pivots form a maximal set of linear independent of columns.

3. $r(A) = \dim C(A) = \dim C(A^T) = r(A^T)$.

> **Proof**: Again it follows from applying gaussian elimination to $A$ (_see the previous remark_). Elementary operations preserve the $\text{span}$ of the **rows** of $A$. The rows of $U$ with pivots form a maximal set of linear independent rows. Finally, $C(A^T)$ is the $\text{span}$ of the rows of $A$.

4. Let $A \in \mathbb{R}^{m \times n}, B \in \mathbb{R}^{n \times p}$, then $AB = \sum_{i = 1}^n \underline{a}_i \underline{b}^T_i$ where $\underline{b}^T_i$ is the $i$-th row of $B$. That is, we can write $AB$ as a sum of rank-1 matrices.

> **Proof**: $r(\underline{a}_i \underline{b}_i^T) =  r(\begin{bmatrix} b_{i1} \underline{a}_i & ... & b_{ip} \underline{a}_i \end{bmatrix}) = 1$.

5. Let $A \in \mathbb{R}^{m \times n}, \Sigma \in \text{diag}(n), B \in \mathbb{R}^{n \times p}$, then $A \Sigma B = \sum_{i=1}^n \sigma_i \underline{a}_i \underline{b}_i^T$.

> **Proof**:
$$
A \Sigma B =

\begin{bmatrix}
\underline{a}_1 & \underline{a}_2 & ... & \underline{a}_n
\end{bmatrix}

\begin{bmatrix}
\sigma_1 & 0 & ... & ... & 0 \\
0 & \sigma_2 & 0 & ... & 0 \\
... & 0 & ... & ... & ... \\
... & ... & ... & ... & 0 \\
0 & 0 & ... & 0 & \sigma_n
\end{bmatrix}

\begin{bmatrix}
\underline{b}^T_1 \\
\underline{b}^T_2 \\
... \\
\underline{b}^T_n
\end{bmatrix} =
$$

$$
= \sigma_1 \underline{a}_1 \underline{b}^T_1 + ... + \sigma_n \underline{a}_n \underline{b}^T_n \text{.}
$$

---

6. Transformations by means of an orthogonal matrix preserve norms and relative angles of vectors.

> **Proof**:

$$
||Q \underline{x}|| = \underline{x}^T Q^T Q \underline{x} = \underline{x}^T \underline{x} = ||\underline{x}|| \text{,}
$$

$$
\angle(Q \underline{x}, Q \underline{y}) = \frac{\underline{x}^T Q^T Q \underline{y}}{||Q \underline{x}|| ||Q \underline{y}||} = \frac{\underline{x}^T \underline{y}}{||\underline{x}|| ||\underline{y}||} = \angle(\underline{x}, \underline{y}) \text{.}
$$

7. Let $\underline{n} \in \mathbb{R}^n$ be a versor. The matrix of the reflection of a vector w.r.t. the plane $\pi$ with vectors orthogonal to $\underline{n}$ is $I_n - 2 \underline{n} \underline{n}^T$.

> **Proof**: $I_n - 2 \underline{n} \underline{n}^T$ removes twice the ortogonal projection of $\underline{x}$ onto the line $\text{span}\{ \underline{n} \}$, which is orthogonal to the plane.

> **Remark**:

$$
(I - 2 \underline{n} \underline{n}^T)(I - 2 \underline{n} \underline{n}^T) = I - 4 \underline{n} \underline{n}^T + 4 \underline{n} \underline{n}^T \underline{n} \underline{n}^T =
$$

$$
= I - 4 \underline{n} \underline{n}^T + 4 \underline{n} 1 \underline{n}^T = I \text{.}
$$

8. Let $U$ be an orthogonal matrix, then $\det U \in \{ -1, 1 \}$.

> **Proof**: Remember that $\det A B = \det A \det B$, $\det A^T = \det A$, and $\det I = 1$, hence $(\det U)^2 = \det U^T U = 1$.

9. **Spectral theorem**: we can decompose every **symmetric** matrix $S \in \mathbb{R}^{n \times n}$ into $S = Q \Lambda Q^T$ where $Q$ is orthogonal and $\Lambda$ is diagonal.

> **Remark** By property 5: $S = \sum_{i=1}^n \lambda_i \underline{q}_i \underline{q}_i^T$.

10. Let $A \in \mathbb{R}^{m \times n}$, then $C(A) \perp N(A^T)$.

> **Proof**: Let $\underline{x} \in N(A^T)$, then

$$
\begin{bmatrix}
\underline{a}_1^T \underline{x} \\
... \\
\underline{a}_n^T \underline{x}
\end{bmatrix} = \underline{0}_n \text{.}
$$

> Let $\underline{y} \in C(A)$, then $\underline{y} = \alpha_1 \underline{a}_1 + ... + \alpha_n \underline{a}_n$.
It follows that $\underline{y}^T \underline{x} = \alpha_1 \underline{a}_1^T \underline{x} + ... + \alpha_n \underline{a}_n^T \underline{x} = 0$.

---

11. $P_{i,j,n}^2 = I_n$.

> **Proof**: By block matrix multiplication it follows that:
$$
P_{i,j,n}^2 = \begin{bmatrix}
I_{i-1} & \underline{0}_{i-1} & O_{i-1 \times j-i-1} & \underline{0}_{i-1} & O_{i-1 \times n-j} \\
\underline{0}_{i-1}^T & 1 & \underline{0}_{j-i-1}^T & 0 & \underline{0}_{n-j}^T \\
O_{j-i-1 \times i-1} & \underline{0}_{j-i-1} & I_{j-i-1} & \underline{0}_{j-i-1} & O_{j-i-1 \times n-j} \\
\underline{0}_{i-1}^T & 0 & \underline{0}_{j-i-1}^T & 1 & \underline{0}_{n-j}^T \\
O_{n-j \times i-1} & \underline{0}_{n-j} & O_{n-j \times j-i-1} & \underline{0}_{n-j} & I_{n-j}
\end{bmatrix} = I_n \text{.}
$$

12. Let $A \in \mathbb{R}^{m \times n}$, $A P_{i,j,n}$ has the same columns of $A$, but the $i$-th and $j$-th columns are swapped.

> **Proof**:

$$
A P_{i,j,n} = \begin{bmatrix} \begin{bmatrix} \underline{a}_1 & ... & \underline{a}_{i-1} \end{bmatrix} \underline{a}_i \begin{bmatrix} \underline{a}_{i+1} & ... & \underline{a}_{j-1} \end{bmatrix} \underline{a}_j \begin{bmatrix} \underline{a}_{j+1} & ... & \underline{a}_n \end{bmatrix} \end{bmatrix} P_{i,j,n} =
$$

$$
= \begin{bmatrix} L_{A,i,j} & \underline{a}_i & C_{A,i,j} & \underline{a}_j & R_{A,i,j} \end{bmatrix} P_{i,j,k} = \begin{bmatrix} L_{A,i,j} & \underline{a}_j & C_{A,i,j} & \underline{a}_i & R_{A,i,j} \end{bmatrix} =
$$

$$
= \begin{bmatrix} \begin{bmatrix} \underline{a}_1 & ... & \underline{a}_{i-1} \end{bmatrix} \underline{a}_j \begin{bmatrix} \underline{a}_{i+1} & ... & \underline{a}_{j-1} \end{bmatrix} \underline{a}_i \begin{bmatrix} \underline{a}_{j+1} & ... & \underline{a}_n \end{bmatrix} \end{bmatrix} \text{.}
$$

13. Let $A, B \in \mathbb{R}^{n \times n}$ be two invertible matrix. Then $(AB)^{-1} = B^{-1}A^{-1}$.

> **Proof**: $ABB^{-1}A^{-1} = A I_n A^{-1} = I_n$.

> **Remark**: this theorem implies that the product of two invertible matrices is invertible. Through induction it can be generalized to the product of $n$ matrices.

14. Let $P \in \mathbb{R}^n$ be an invertible matrix, let $A \in \mathbb{R}^{m \times n}$, then $\dim N(A P) = \dim N(A)$.

> **Proof**: Let $\underline{v}_1, ..., \underline{v}_k$ be a basis for $N(A)$.
We will prove that $P^{-1} \underline{v}_1, ..., P^{-1} \underline{v}_k$ is a basis for $N(A P)$.

> Let $\underline{x} \in N(A P)$, then $A P \underline{x} = \underline{0}_m$, hence $P \underline{x} \in N(A)$, so $P \underline{x} = \alpha_1 \underline{v}_1 + ... + \alpha_k \underline{v}_k$, finally $\underline{x} = \alpha_1 P^{-1} \underline{v}_1 + ... + \alpha_k P^{-1} \underline{v}_k$. That is $N(AP) \subseteq \text{span}\{P^{-1} \underline{v}_1, ..., P^{-1} \underline{v}_k \}$.

> Let $\underline{x} \in \text{span}\{P^{-1} \underline{v}_1, ..., P^{-1} \underline{v}_k \}$, then $\underline{x} = \alpha_1 P^{-1} \underline{v}_1 + ... + \alpha_k P^{-1} \underline{v}_k$, hence $A P \underline{x} = \alpha_1 A \underline{v}_1 + ... + \alpha_k A \underline{v}_k = \underline{0}_m$. That is $\text{span}\{P^{-1} \underline{v}_1, ..., P^{-1} \underline{v}_k \} \subseteq N(AP)$.

> Finally, we have to prove that $P^{-1} \underline{v}_1, ..., P^{-1} \underline{v}_k$ are linearly independent. This follows from the fact that $\alpha_1 P^{-1} \underline{v}_1 + ... + \alpha_k P^{-1} \underline{v}_k = \underline{0}_m$ iff $\alpha_1 \underline{v}_1 + ... + \alpha_k \underline{v}_k = \underline{0}$ (just primultiply by $P$).

---

15. Let $A \in \mathbb{R}^{m \times n}$ and $r = r(A)$. Then $\dim N(A) = n - r$.

> **Proof (*)**: by properties 11, 12, 13, and 14 we can assume without loss of generaly that the first $r$ columns of $A$ are linearly independent (_that is, if it is not the case, we can use $P_{i,j,n}$ to swap the columns, knowing, by property 14 that $\dim N(A)$ is preserved_). It follows that every other column of $A$ is a linear combination of the first $r$ (_$A$ has rank $r$_).

> Let $A_r = \begin{bmatrix} \underline{a}_1 & ... & \underline{a}_r \end{bmatrix}$. By the same reasoning we applied to derive the echelon form of $A$: $A = A_r \begin{bmatrix} I_r & B \end{bmatrix}$ with $B \in \mathbb{R}^{r \times n-r}$.

> Let $K = \begin{bmatrix} -B \\ I_{n-r} \end{bmatrix}$. We will prove that the columns of $K$, which are $n-r$, form a basis of $N(A)$.

> $A K = A_r \begin{bmatrix} I_r & B \end{bmatrix} \begin{bmatrix} -B \\ I_{n-r} \end{bmatrix} = A_r (-B + B) = O_{m \times n-r}$. Then $\underline{k}_1, ..., \underline{k}_{n-r} \in N(A)$.

> Let $A \underline{x} = \underline{0}_m$. We can write $\underline{x} = \begin{bmatrix} \underline{x}_1 \\ \underline{x}_2 \end{bmatrix}$ where $\underline{x}_1 \in \mathbb{R}^r$, $\underline{x}_2 \in \mathbb{R}^{n-r}$. The $\underline{0}_m = A \underline{x} = A_r ( \underline{x}_1 + B \underline{x}_2 )$ iff $\underline{x}_1 + B \underline{x}_2 = \underline{0}_r$ (since the columns of $A_r$ are linearly independent). Then $\underline{x}_1 = -B \underline{x}_2$. Hence
$$
\underline{x} = \begin{bmatrix}
-B \\
I_{n-r}
\end{bmatrix} \underline{x}_2 = K \underline{x}_2 \in C(K) \text{.}
$$

> $K \underline{x} = \underline{0}_n$ iff $\begin{bmatrix} -B \\ I_{n-r} \end{bmatrix} \underline{x} = \underline{0}_n$, which implies $\underline{x} = \underline{0}_{n-r}$.

16. Let $\lambda$ be an eigenvalue of $A$. Then $\lambda^n$ is an eigenvalue of $A^n$.
Furthermore said $V_\lambda$ the eigenspace of $A$ associated to $\lambda$ and $W_{\lambda^n}$ the eigenspace of $A^n$ associated to $\lambda^n$, we have that $V_\lambda \subseteq W_{\lambda^n}$.

> **Proof**: if $A \underline{v} = \lambda \underline{v}$, then $A^n \underline{v} = \lambda A^{n-1} \underline{v} = ... = \lambda^n \underline{v}$.

17. The Rayleigh quotient $\frac{\underline{x}^T A \underline{x}}{\underline{x}^T \underline{x}} = \lambda$ where $\lambda$ is the eigenvalue associated to $\underline{x}$.

> **Proof**:

$$
\frac{\underline{x}^T A \underline{x}}{\underline{x}^T \underline{x}} = \frac{\lambda \underline{x}^T \underline{x}}{\underline{x}^T \underline{x}} = \lambda \text{.}
$$

---

18. Let $A \in \mathbb{R}^{n \times n}$ be an invertible and diagonalizable matrix. If $\lambda_1, ..., \lambda_n$ are the eigenvalues of $A$, then $\frac{1}{\lambda_1}, ..., \frac{1}{\lambda_n}$ are the eigenvalues of $A^{-1}$.

> **Proof**: Let $\underline{v}$ be an eigenvector of $A$. Then $A \underline{v} = \lambda \underline{v}$, which implies $\underline{v} = A^{-1} \lambda \underline{v}$. Note that, being invertible, $\det A \neq 0$, hence $0$ is not an eigenvalue of $A$, an so $\lambda \neq 0$. Then $A^{-1} \underline{v} = \frac{1}{\lambda} \underline{v}$.

19. Let $A \in \mathbb{R}^{n \times n}$ be a diagonalizable matrix. If $\lambda_1, ..., \lambda_n$ are the eigenvalues of $A$, then $\lambda_1 - \alpha$, ..., $\lambda_n - \alpha$ are the eigenvalues of $A - \alpha I_n$.

> **Proof**: Let $\underline{v}$ be an eigenvector of $A$. Then $(A - \alpha I_n) \underline{v} = \lambda \underline{v} - \alpha \underline{v} = (\lambda - \alpha) \underline{v}$.

20. **QR factorization of $A$**: we can factorize a matrix $A \in \mathbb{R}^{m \times n}$ where $m \geq n$ and $r(A) = n$ into
$$
A = Q \begin{bmatrix} R \\ O_{(m-n) \times n} \end{bmatrix}
$$
> where $Q \in \mathbb{R}^{m \times m}$ is an orthogonal matrix and $R \in \mathbb{R}^{n \times n}$ is an upper-triangular matrix.

> **Proof**: we have to exploit the Gram-Schmidt othogonalization procedure (_we'll see how_).

> Let $\underline{w}_1 = \underline{a}_1, \underline{w}_i = \underline{a}_i - \sum_{k=1}^{i-1} b_{i,k} \underline{w}_k \text{ for } i \in \{ 2, ..., n \}$ where
$$
b_{i,k} = \frac{\underline{a}_i^T \underline{w}_k}{||\underline{w}_k||^2} \text{.}
$$

> First of all we will prove that $\underline{w}_i$ is a non-trivial linear combination of $\underline{a}_1$, ..., $\underline{a}_i$ by induction. The base case is straightforward ($\underline{w}_1 = \underline{a}_1$), for the inductive step let $i > 1$: $\underline{w}_i = \underline{a}_i - \sum_{k=1}^{i-1} b_{i,k} \underline{w}_k = \underline{a}_i - \sum_{k=1}^{i-1} b_{i,k} (\alpha_{k,1} \underline{a}_1 + ... + \alpha_{k,k} \underline{a}_k)$ by induction hypothesis. The result follows since $\underline{a}_i$ never appears inside the summation and its coefficient outside of the summation is 1. Since $\underline{a}_1, ..., \underline{a}_n$ are linearly independent, we also proved that $\underline{w}_i \neq \underline{0}_m$, and so $b_{i,k}$ is well-defined.

> Now let's prove that $\underline{w}_i^T \underline{w}_j = 0$ for $i \in \{ 2, ..., n \}$, for $j \in \{ 1, ..., i-1 \}$ (_by the commutativity of the scalar product, the result holds for every $i, j \in \{ 1, ..., n \}$ with $i \neq j$_). We will proceed by induction.
> - Base case: $i = 2$, then $j = 1$.
$$
\underline{w}_2^T \underline{w}_1^T = (\underline{a}_2 - b_{2,1} \underline{w}_1)^T \underline{w}_1 = \underline{a}_2^T\underline{w}_1 - b_{2,1} ||\underline{w}_1||^2 = 0 \text{.}
$$

---

> - Inductive step: $i > 2$. By induction hypothesis $\underline{w}_k^T \underline{w}_j = 0$ for every $k, j \in \{ 1, ..., i-1 \}$, $k > j$.
$$
\underline{w}_i^T\underline{w}_j = (\underline{a}_i - \sum_{k=1}^{j-1} b_{i,k} \underline{w}_k - b_{i,j} \underline{w}_j - \sum_{k=j+1}^{i-1} b_{i,k} \underline{w}_k)^T \underline{w}_j =
$$

$$
\underline{a}_i^T \underline{w}_j - b_{i,j} ||\underline{w}_j||^2 - \sum_{k=1}^{j-1} b_{i,k} \underline{w}_j^T \underline{w}_k - \sum_{k=j+1}^{i-1} b_{i,k} \underline{w}_k^T \underline{w}_i =
$$

$$
0 - \sum_{k=1}^{j-1} 0 - \sum_{k=j+1}^{i-1} 0 = 0 \text{.}
$$

> By the last result
$$
\underline{q}_i = \frac{\underline{w}_i}{||\underline{w}_i||} \text{ for } i \in \{ 1, ..., n \}
$$
> is a set of orthonormal vectors.
Let $i \in \{ 1, ..., n \}$, then it is straightforward that $\underline{a}_i^T \underline{q}_i = ||\underline{w}_i||$. Furthermore, for every $j \in \{1, ..., i-1\}$ $\underline{a}_i^T \underline{w}_j = b_{i,j} || \underline{w}_j ||$.
Then, since $||\underline{w}_k|| \underline{q}_k = \underline{w}_k$ for every $k \in \{ 1, ..., i-1 \}$, it follows that
$$
\underline{a}_i = ||\underline{w}_i|| \underline{q}_i + \sum_{k=1}^{i-1} b_{i,k} ||\underline{w}_k|| \underline{q}_k = \sum_{k=1}^i \underline{a}_i^T \underline{q}_k \underline{q}_k \text{.}
$$

> Not to get the remaining $m-n$ orthonormal vectors to put in $Q$ we can extend $\underline{a}_1, ..., \underline{a}_n$ to a basis of $\mathbb{R}^m$ and apply the same procedure.
Finally, by the last result
$$
R = \begin{bmatrix}
\underline{a}_1^T \underline{q}_1 & ... & ... & \underline{a}_n^T \underline{q}_1 \\
0 & ... & ... & ... \\
... & ... & ... & ... \\
0 & ... & 0 & \underline{a}_n^T \underline{q}_n
\end{bmatrix} \text{.}
$$

21. Let $S \in \mathbb{R}^{n \times n}$ be a symmetric matrix. Then the eigenvectors which belong to different eigenspaces of $S$ are orthogonal.

> **Proof (*)**: we will prove a special case first: let $\underline{x}, \underline{y} \in \mathbb{R}^{n}$ s.t. $S \underline{x} = \lambda \underline{x}$ with $\lambda \neq 0$, and $S \underline{y} = \underline{0}$. Then:
$$
\underline{y}^T \underline{x} = \frac{1}{\lambda} \underline{y}^T S \underline{x} = \frac{1}{\lambda} (S \underline{y})^T \underline{x} = 0 \text{.}
$$

---

> Now let $\underline{x}, \underline{y} \in \mathbb{R}^{n}$ s.t. $S \underline{x} = \lambda \underline{x}$ and $S \underline{y} = \alpha \underline{y}$ with $\lambda \neq \alpha$. Then (_see property 19_) $\underline{x}$ and $\underline{y}$ are eigenvectors of $S - \alpha I$ which satisfy the hypothesis of the "special case" proved before. Hence $\underline{y}^T \underline{x} = 0$.

22. Let $S \in \mathbb{R}^{n \times n}$ be a symmetric matrix. All the eigenvalues of $S$ are real numbers.

> **Proof (*)**: Let $\underline{x} \in \mathbb{C}^{n}$ s.t. $S \underline{x} = \lambda \underline{x}$ with $\lambda \in \mathbb{C}$. We want to prove that $\lambda \in \mathbb{R}$. Let $\overline{\underline{x}}$ be the vector of conjugates of $\underline{x}$.
Since $S \underline{x} = \lambda \underline{x}$, then $\overline{\underline{x}}^T S \underline{x} = \overline{\underline{x}}^T \lambda \underline{x}$. Now observe that:
$$
\overline{\underline{x}}^T \underline{x} = \sum_{i=1}^n |x_i|^2 \in \mathbb{R}^+ \text{ (eigenvectors are different from 0).}
$$
> Furthermore:
$$
\overline{\underline{x}}^T S \underline{x} = \frac{1}{2}(\overline{\underline{x}}^T S \underline{x} + \overline{\underline{x}}^T S^T \underline{x}) =
$$

$$
= \frac{1}{2}(\overline{\underline{x}}^T \begin{bmatrix} \underline{s}_1 & ... & \underline{s}_n \end{bmatrix} \begin{bmatrix} x_1 \\ ... \\ x_n \end{bmatrix} + \begin{bmatrix} \overline{x}_1 & ... & \overline{x}_n \end{bmatrix} \begin{bmatrix} \underline{s}_1^T \\ ... \\ \underline{s}_n^T \end{bmatrix} \underline{x}) =
$$

$$
= \frac{1}{2}(x_1 \overline{\underline{x}}^T \underline{s}_1 + ... + x_n \overline{\underline{x}}^T \underline{s}_n + \overline{x}_1 \underline{s}_1^T \underline{x} + ... + \overline{x}_1 \underline{s}_n^T \underline{x}) =
$$

$$
= \frac{1}{2}((x_1 \underline{\overline{x}}^T + \overline{x}_1 \underline{x}^T) \underline{s}_1 + ... + (x_n \underline{\overline{x}}^T + \overline{x}_n \underline{x}^T) \underline{s}_n) \text{.}
$$

> Now let $x_i = a_i + i b_i, x_j = a_j + i b_j$, it is easy to check that $x_i \overline{x}_j + \overline{x}_i x_j = 2(a_ia_j + b_ib_j) \in \mathbb{R}$, hence $x_i \underline{\overline{x}} + \overline{x}_i \underline{x} \in \mathbb{R}^n$, and so
$$
\overline{\underline{x}}^T S \underline{x} \in \mathbb{R} \text{.}
$$
> It follows that:
$$
\lambda = \frac{\overline{\underline{x}}^T S \underline{x}}{\overline{\underline{x}}^T \underline{x}} \in \mathbb{R} \text{.}
$$

23. A matrix is positive definite iff it has all positive eigenvalues.

> **Proof (*)**: _we will just prove that a matrix with positive eigenvalues is positive definite_. Being symmetric, $S$ is orthogonally diagonalizable. Let $\underline{x} \in \mathbb{R}^n$. Then $\underline{x} = \alpha_1 \underline{v}_1 + ... + \alpha_n \underline{v}_n$ where $S \underline{v}_i = \lambda_i \underline{v}_i$ with $\lambda_i > 0$ and $\underline{v}_i^T \underline{v}_j = 0$ if $i \neq j$. Then
$$
\underline{x}^T S \underline{x} = (\alpha_1 \underline{v}_1^T + ... + \alpha_n \underline{v}_n^T) (\alpha_1 \lambda_1 \underline{v}_1 + ... + \alpha_n \lambda_n \underline{v}_n) = \sum_{i=1}^n \alpha_i^2 \lambda_i ||\underline{v}_i||^2 \geq 0 \text{.}
$$

---

> Furthermore
$$
\sum_{i=1}^n \alpha_i^2 \lambda_i ||\underline{v}_i||^2 = 0 \text{ iff } \underline{x} = \underline{0} \text{.}
$$

24. A matrix is positive definite iff al its leading determinants are positive.

> **Remark**: a **leading determinant** $D_i$ for $i \in \{ 1, ..., n \}$ is the determinant of the submatrix of $S$ obtained by choosing the rows $\{ 1, ..., i \}$, and the columns $\{ 1, ..., i \}$.

25. A matrix $S \in \mathbb{R}^{n \times n}$ is positive definite iff $S = A^T A$ where $r(A) = n$.

> **Proof (*)**: _we will just prove that if $S = A^T A$, then $S$ is positive definite_.
Let $\underline{x} \in \mathbb{R}^n$, then $\underline{x}^T S \underline{x} = \underline{x}^T A^T A \underline{x} = ||A \underline{x}||^2 \geq 0$. Furthermore $||A \underline{x}||^2 = 0$ iff $A \underline{x} = \underline{0}$ iff $\underline{x} = \underline{0}$, since $r(A) = n$.

> **Remark**: if $A$ is an upper triangular matrix, this is known as **Cholesky factorization**.

26. A matrix $S$ is positive definite iff we don't need to swap rows during gaussian elimination and all the resulting (by strictly applying the algorithm) pivots are positive.

27. A matrix $P$ is a projection matrix iff $P \underline{x} = \underline{x}$ for every $\underline{x} \in C(P)$.

> **Proof**: let $P$ be a projection matrix, let $\underline{x} \in C(P)$, then $\underline{x} = P \underline{y}$, hence
$$
P \underline{x} = P^2 \underline{y} = P \underline{y} = \underline{x} \text{.}
$$

> Let $P$ s.t. $P \underline{x} = \underline{x}$ for every $\underline{x} \in C(P)$, hence $P \underline{p}_i = \underline{p}_i$, and so $P^2 = P$.

28. A matrix $P$ is an orthogonal projection matrix iff $P = U U^T$ where the columns of $U$ are an orthonormal basis of $C(P)$.

> **Proof**: let $P$ be an orthogonal projection matrix. Beign symmetric
$$
P = V \Lambda V^T \text{,}
$$
> furthermore $V \Lambda V^T = P = P^2 = V \Lambda^2 V^T$. Hence, for every eigenvalue of $\lambda$ of $P$, it must be $\lambda^2 = \lambda$ iff $\lambda = 1$ or $\lambda = 0$. Hence, we can write $P$ as:
$$
P = \tilde{V} \begin{bmatrix}
I_{r(P)} & O_{r(P) \times (n-r(P))} \\
O_{(n-r(P)) \times r(P)} & O_{(n-r(P)) \times (n-r(P))}
\end{bmatrix} \tilde{V}^T
$$
> Hence $P = \begin{bmatrix} \tilde{v}_1 & ... & \tilde{v}_{r(P)} \end{bmatrix} \begin{bmatrix} \tilde{v}_1^T \\ ... \\ \tilde{v}_{r(P)}^T \end{bmatrix} = U U^T$.

---

> And the columns of $U$ are orthonormal. Now let $\underline{x} \in C(U)$, that is 
$$
\underline{x} = U \underline{y} = U I_{r(P)} \underline{y} = U U^T U \underline{y} = P U \underline{y} \in C(P)\text{;}
$$
> if instead $\underline{x} \in C(P)$, that is
$$
\underline{x} = P \underline{y} = U U^T \underline{y} \in C(U) \text{.}
$$
> Hence $C(U) = C(P)$ as we wanted to prove.

> Now let's prove the converse: let $P = U U^T$ where the columns of $U$ are orthonormal. It is clear the $P$ is symmetric. Finally
$$
P^2 = U U^T U U^T = U I_{r(P)} U^T = U U^T = P \text{.}
$$