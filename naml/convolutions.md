---
marp: true
theme: summary
---
# Convolutions

<div class="author">

Cristiano Migali

</div>

## Introduction

We will discuss a topic which has become more and more relevant in ML applications and in particular for NNs: **convolutions**.

- Given two functions $f, g : \mathbb{R} \rightarrow \mathbb{R}$, the **convolution** of $f$ and $g$ is the function
$$
(f * g)(x) = \int_{-\infty}^{+\infty} f(t) g(x-t) dt \text{.}
$$

For our purposes, we are more interested in the convolution between two vectors:
- Given two vectors
$$
\underline{c} = \begin{bmatrix}
c_0 \\ ... \\ c_{n-1}
\end{bmatrix} \text{, }
\underline{d} = \begin{bmatrix}
d_0 \\ ... \\ d_{n-1}
\end{bmatrix}
$$
> the **convolution** $\underline{c} * \underline{d}$ is a vector with $2n-1$ components, whose $k$-th component is
$$
(\underline{c} * \underline{d})_k = \sum_{\begin{matrix}
i+j = k \\
i,j \in \{ 0, ..., n-1 \}
\end{matrix}} c_i d_j
$$
> with $k \in \{ 0, ..., 2n-2 \}$.

We can rewrite the $k$-th element of the convolution in a more handy way:
$$
(\underline{c} * \underline{d})_k = \sum_{i = \max(0, k-n+1)}^{\min(k, n-1)} c_i d_{k-i} \text{.}
$$

To prove the equivalence, we need to show that
$$
\{ (i,j) | i,j \in \{ 0, ..., n-1 \} \land i+j = k \} = 
$$
$$
= \{ (i, k-i) | i \in \{ \max(0, k-m+1), ..., \min(k, n-1) \} \} \text{.}
$$
For:
> let $i, j \in \{ 0, ..., n-1 \}$ with $i+j = k$.
Then  $j = k-i$. Furthermore $i \geq 0$, and $i = k-j \geq k-n+1$ (since $j \leq n-1$).

---

> Then $i \geq \max(0, k-n+1)$. Also, $i = k-j \leq k$ (since $j \geq 0$), and $i \leq n-1$.
Then $i \in \{ \max(0, k-n+1), ..., \min(k, n-1) \}$.

> Conversely, let $i \in \{ \max(0, k-n+1) \}, ..., \min(k, n-1)$ and $j = k-i$.
Then $i \geq \max(0, k-n+1) \geq 0$, and $i \leq \min(k, n-1) \leq n-1$, and so $i \in \{ 0, ..., n-1 \}$.
$i+j = i + k -i = k$.
$j = k-i \geq k-k = 0$, and $j = k-i \leq k-k+n-1$. Then $j \in \{ 0, ..., n-1 \}$ as we wanted to prove.

There is a strong relationship between convolutions and the coefficients of the product between two polynomials: let $c(x), d(x)$ be the polynomials "induced" by $\underline{c}$, and $\underline{d}$:
$$
c(x) = c_0 + c_1 x + ... c_{n-1}x^{n-1} \text{,}
$$
$$
d(x) = d_0 + d_1 x + ... + d_{n-1}x^{n-1} \text{.}
$$
Then
$$
c(x)d(x) = c_0d_0 + (c_0 d_1 + c_1 d_0) x + ... + c_{n-1}d_{n-1}x^{2n-2}
$$
is the polynomial "induced" by $\underline{c} * \underline{d}$.

Most of the times we will be interested in a slight variation of the convolution: the **cyclic convolution** (_since, as we will see, it can be computed in a smart and fast way_).
- (_We will use a notation analogous to the one used in the definition of "standard" convolutions_). The **cyclic convolution** $\underline{c} \circledast \underline{d}$ is the vector with $n$ components whose $k$-th component is
$$
(\underline{c} \circledast \underline{d})_l = \sum_{\begin{matrix}
i+j = k \mod n \\
i,j \in \{ 0, ..., n-1 \}
\end{matrix}} c_i d_j
$$
> with $k \in \{ 0, ..., n-1 \}$.

Observe that, since $i \in \{ 0, ..., n-1 \}$, and $j \in \{ 0, ..., n-1 \}$, $i+j \in \{ 0, ..., 2n-2 \}$.
Then $i+j = k \mod n$ (with $k \in \{ 0, ..., n-1 \}$) iff
$$
i+j = k \text{ or } i+j = n+k \text{.}
$$
Hence
$$
(\underline{c} \circledast \underline{d})_k = \begin{cases}
\sum_{i = \max(0, k-n+1)}^{\min(k, n-1)} c_i d_{k-i} + \sum_{i = \max(0, k+1)}^{\min(k+n, n-1)} c_i d_{k+n-i} \text{ if } k \in \{ 0, ..., n-2 \} \\
\sum_{i = \max(0, 0)}^{\min(n-1,n-1)} c_i d_{n-1-i} \text{ if } k = n-1
\end{cases} =
$$

---

$$
= \begin{cases}
\sum_{i=0}^k c_i d_{k-i} + \sum_{i = k+1}^{n-1} c_i d_{k+n-i} \text{ if } k \in \{ 0, ..., n-2 \} \\
\sum_{i=0}^{n-1} c_i d_{k-i} \text{ if } k = n-1
\end{cases} =
$$

$$
= \sum_{i=0}^{n-1} c_i d_{k-i \mod n} \text{ since } k+n-i = k-i \mod n \text{.}
$$

## Convolutions through matrices

We will introduce two families of matrices that, as we will see, are strictly related to convolutions and cyclic convolutions respectively.

### Toeplitz matrices

- A **toeplitz matrix** $T \in \mathbb{R}^{n \times n}$ is a matrix whose elements are given by a $(2n-1)$-length sequence $\{ t_k \}, k \in \{ -(n-1), ..., 0, ..., n-1 \}$. The element at row $i$ and column $j$ of $T$ is (_we count rows and columns starting from 0: $i, j \in {0, ..., n-1}$_) $T(i,j) = t_{i-j}$. That is
$$
T = \begin{bmatrix}
t_0 & t_{-1} & t_{-2} & ... & ... & t_{-(n-1)} \\
t_1 & t_0 & t_{-1} & t_{-2} & ... & ... \\
t_2 & t_1 & t_0 & t_{-1} & ... & ... \\
... & t_2 & t_1 & t_0 & ... & ... \\
... & ... & ... & ... & ... & ... \\
t_{n-1} & ... & ... & ... & ... & t_0 \\
\end{bmatrix} \text{.}
$$

**Reamrks**:
1. Since the elements of the main diagnals are $(i, j)$ s.t. $i-j = d$, every main diagonal has elements all equal: $T(i, j) = t_{i-j} = t_d$.
2. Because of the 1st remark, if we know the first row and the first column of $T$, $T$ is univocally determined.

### Circulant matrices

- A **circulant matrix** $C \in \mathbb{R}^{n \times n}$ is a matrix whose elments are given by a $n$-length sequence $\{ c_k \}, k \in \{ 0, ..., n-1 \}$. The element at row $i$ and column $j$ of $C$ is $C(i, j) = c_{i-j \mod n}$. That is
$$
C = \begin{bmatrix}
c_0 & c_{n-1} & ... & c_1 \\
c_1 & c_0 & ... & c_2 \\
... & ... & ... & ... \\
c_{n-1} & c_{n-2} & ... & c_0 \\
\end{bmatrix} \text{.}
$$

---

**Remark**: A circulant matrix is a toeplix matrix where
$$
t_k = c_{k \mod n} \text{.}
$$

## Cyclic convolutions and Discrete Fourier Transform (DFT)

**Important**: in what follows, we will use often matrices of the form
$$
C' = \begin{bmatrix}
c_0'& c_1' & ... & c_{n-1}' \\
c_{n-1}' & c_0' & ... & c_{n-2}' \\
... & ... & ... & ... \\
c_1' & c_2' & ... & c_0'
\end{bmatrix} \text{.}
$$
These **are circulant matrices** where $c_k = c'_{-k \mod n}$.

For example, let $c'_k = (1, 3, 5, 8)$.
Then
$$
C' = \begin{bmatrix}
1 & 3 & 5 & 8 \\
8 & 1 & 3 & 5 \\
5 & 8 & 1 & 3 \\
3 & 5 & 8 & 1
\end{bmatrix}
$$

The followin remarks and theorems will allow us to write circulant matrices in polynomial form.

Consider $P \in \mathbb{R}^{n \times n}$:
$$
P_n = \begin{bmatrix}
O_{(n-1) \times 1} & I_{n-1} \\
1 & O_{1 \times (n-1)}
\end{bmatrix} \text{.}
$$

Observe that
$$
P_n \underline{c}' = \begin{bmatrix}
O_{(n-1) \times 1} & I_{n-1} \\
1 & O_{1 \times (n-1)}
\end{bmatrix} \begin{bmatrix}
c_0' \\
\begin{bmatrix}
c_1' \\
... \\
c_{n-1}'
\end{bmatrix}
\end{bmatrix} = \begin{bmatrix} c_1' \\ ... \\ c_{n-1}' \\ c_0' \end{bmatrix} \text{.}
$$

THat is, the matrix $P_n$ lifted the elements of $\underline{c}'$ up of one row (and put $c_0'$ in the last row).

Let's discover more properites of $P_n$.

- **Theorem (1)**:
$$
P_n^j = \begin{bmatrix}
O_{(n-j) \times j} & I_{n-j} \\
I_j & O_{j \times (n-j)}
\end{bmatrix} \text{.}
$$

---

> **Proof**:
> - Base case: $j = 0$
$$
P_n^0 = I_n = \begin{bmatrix}
O_{n \times 0} & I_n \\
I_0 & O_{0 \times n} \text{.}
\end{bmatrix}
$$
> - Inductive step: $j > 0$
> By the inductive hypothesis
$$
P_n^{j-1} = \begin{bmatrix}
O_{(n-j+1) \times (j-1)} & I_{n-j+1} \\
I_{j-1} & O_{(j-1) \times (n-j+1)}
\end{bmatrix} = \begin{bmatrix}
\begin{bmatrix} O_{1 \times (j-1)} & 1 \end{bmatrix} & O_{1 \times n-j} \\
\begin{bmatrix}
O_{(n-j) \times (j-1)}  & O_{(n-j) \times 1} \\
I_{j-1} & O_{(j-1) \times 1}
\end{bmatrix} & \begin{bmatrix}
I_{n-j} \\
O_{(j-1) \times (n-j)}
\end{bmatrix}
\end{bmatrix} \text{.}
$$
> The result follows by performing the block matrix multiplication $P_n^j = P_n P_n^{j-1}$.

- **Theorem (2)**: $P_n^n = I_n$.

> **Proof**: the reuslt follows by writing $P_n^n = P_n P_n^{n-1}$, applying theorem (1) to $P_n^{n-1}$, and then doing the block matrix multiplication.

- **Theorem (3)**: $P_n^{n-1} = P_n^T$.

> **Proof**: the result follows from theorem (1).

- **Corollary of theorems (2), and (3)**: $P_n^T P_n = P_n P_n^T = I_n$, that is, $P_n$ is an orthogonal matrix.

- **Theorem (4)**: let $C'$ be the matrix whose elements are $C'(i, j) = c'_{j-i \mod n}$ where ${c_k'}$ is an $n$-length sequence.
Then
$$
C' = c_0 I + c_1 P_n + ... + c_{n-1} P_n^{n-1} \text{.}
$$

> **Proof**: we will show that
$$
P_n^m(i, j) = \begin{cases}
1 \text{ if } j-i = m \mod n \\
0 \text{ otherwise}
\end{cases} \text{,}
$$
> the proof will follow.
By theorem (1):
$$
P_n^m = \begin{bmatrix}
O_{(n-m) \times m} & I_{n-m} \\
I_m & O_{m \times n-m}
\end{bmatrix} \text{.}
$$
> Then $P_n^m$ equals 1 **at and only at** $(n-m, 0), ..., (n-m+m-1, m-1)$ (_the lower left $I_m$_), and $(0, m), ..., (n-m-1, m+n-m-1)$ (_the upper right $I_{n-m}$_).

---

> Hence, what we want to prove is that:
$$
\{ (n-m + k, k) | k \in \{ 0, ..., m-1 \} \} \cup \{ (k, m+k) | k \in \{ 0, ..., n-m-1 \} \} = 
$$
$$
= \{ (i, j) | i, j \in \{ 0, ..., n-1 \}, j-i = m \mod n \} \text{.}
$$
> For: consider $(n-m + k, k)$ with $k \in \{ 0, ..., m-1 \}$. It is clear that $n-m+k, k \in \{ 0, ..., n-1 \}$, furthermore $k-n+m-k = m-n = m \mod n$. The same is true for $(k, m+k)$ with $k \in \{ 0, ..., n-m-1 \}$.

> Conversely, let: $(i, j)$ with $i, j \in \{ 0, ..., n-1 \}$, and $j-i = m \mod n$. Then, either $j-i = m$ or $j-i = m-n$.
In the first case, $j = m + i$, hence $i \leq n-1-m$ (otherwise $j > n$), and so $(i, j) \in \{ (k, m+k) | k \in \{ 0, ..., n-m-1 \} \}$, with $k = i$.
In the second case, $i = n-m+j$, hence $l \leq m-1$ (otherwise $i > n$), and so $(i, j) \in \{ (n-m + k, k) | k \in \{ 0, ..., m-1 \} \}$, wtih $k = j$.

**Remark**: the theorem above is a representation theorem, a matrix has the "structure" of $C'$ iff it can be written as that polynomial in $P$.

Now let $C', D'$ be two matrices "with the usual shape". What happens if we multiply them?

**Remark**: since $P_n^n = I_n$, then $P_n^k = P_n^{k \mod n}$ (it works also when $k$ is negative).

We know that:
$$
C' = c_0' I + ... + c_{n-1}'P_n^{n-1}
$$
and
$$
D' = d_0' I + ... + d_{n-1}'P_n^{n-1} \text{.}
$$

Let
$$
\underline{c} = \begin{bmatrix}
c_0' \\
... \\
c_k'
\end{bmatrix} \text{, and} \begin{bmatrix}
d_0' \\
... \\
d_k'
\end{bmatrix} \text{.}
$$
Then, by the remark above, and by the relationship between convolutions and polynomials multiplications that we discussed at the beginning:
$$
C'D' = (\underline{c}' \circledast \underline{d}')_0I + ... + (\underline{c}' \circledast \underline{d}')_{n-1} P_n^{n-1} \text{.}
$$
That is, by theorem (4), $C'D'$ is the matrix "with the usual shape" generated by $\underline{c} \circledast \underline{d}$.

**Remark**: when computing convolutions on paper we can use the elementary school technique for multiplying to numbers (which are polynomials in $10$). Then, to get a cyclic convolution we just need to sum together the components which have the same index $\mod n$.

---

There is another way of computing cyclic convolutions through circulant matrices. Let $C$ be a "standard" circulant matrix (observe that it is $C$, not $C'$) generated by $\underline{c}$. Then
$$
C \underline{d} = \begin{bmatrix}
c_0 & c_{n-1} & ... & c_1 \\
c_1 & c_0 & ... & c_2 \\
... & ... & ... & ... \\
c_{n-1} & c_{n-2} & ... & c_0 \\
\end{bmatrix} \begin{bmatrix}
d_0 \\
d_1 \\
... \\
d_{n-1}
\end{bmatrix} = \begin{bmatrix}
\sum_{j=1}^{n-1} d_i c_{0-i \mod n} \\
\sum_{j=1}^{n-1} d_i c_{1-i \mod n} \\
... \\
\sum_{j=1}^{n-1} d_i c_{n-1-i \mod n}
\end{bmatrix} = \underline{d} \circledast \underline{c} = \underline{c} \circledast \underline{d} \text{.}
$$

(_The commutativity of $*$, and $\circledast$ follows directly from the polynomial multiplication interpretation_).

### The eigenvalues and eigenvectors of $C'$

> **Theorem (5)**: $\lambda \in \mathbb{C}$ is an eigenvalue of $P_n$ iff $\lambda^n = 1$.

> **Proof**: assume that $P_n \underline{v} = \lambda \underline{v}$ for some $\underline{v} \neq 0$. Hence:
$$
\underline{v} = I_n \underline{v} = P_n^n  \underline{v} = \lambda^n \underline{v} \text{ iff }
$$
$$
(\lambda^n - 1) \underline{v} = \underline{0} \text{ iff }
$$
$$
\lambda^n = 1 \text{.}
$$

> Now, suppose that $\lambda^n = 1$, let
$$
\underline{v} = \begin{bmatrix}
1 \\
\lambda \\
... \\
\lambda^{n-1}
\end{bmatrix} \text{.}
$$
> Hence
$$
P \underline{v} = \begin{bmatrix} \lambda\\
... \\
\lambda^{n-1} \\
1
\end{bmatrix} = \lambda \begin{bmatrix}
1 \\
... \\
\lambda^{n-2} \\
\lambda^{n-1}
\end{bmatrix} = \lambda \underline{v} \text{.}
$$

- Let
$$
\omega_n = e^{\frac{2 \pi i}{n}}
$$

By the $n$-th root theorem, the $n$ $n$-th roots of 1 are: $\omega_n^0, ..., \omega_n^{n-1}$, which, by theorem (5), are the eigenvalues of $P$. $P$ has $n$ simple eigenvalues, hence it is diagonalizable.

---

Furthermore, we already discovered in the proof of theorem (5) that
$$
\underline{v}_k = \begin{bmatrix}
1 \\
\omega_n^k \\
... \\
\omega_n^{(n-1)k}
\end{bmatrix}
$$
is the eigenvector associated to $\omega_n^k$ with $k \in \{ 0, ..., n-1 \}$.

- We define **Fourier matrix**
$$
F = \begin{bmatrix}
\omega_n^{0 \cdot 0} & ... & \omega_n^{0 \cdot (n-1)} \\
... & ... & ... \\
\omega_n^{(n-1) \cdot 0} & ... & \omega_n^{(n-1)(n-1)}
\end{bmatrix} \text{.}
$$
> That is, $F_n(p, q) = \omega_n^{p \cdot q}$ with $p, q \in \{ 0, ..., n-1 \}$.

> **Theorem (6)**:
$$
\underline{\overline{v}}_p^T \underline{v}_q = \begin{cases}
0 \text{ if } p \neq q \\
n \text{ otherwise }
\end{cases} \text{.}
$$

> **Remark**: it is easy to check that $\overline{\omega}_n = \omega_n^{-1}$.

> **Proof**:
$$
\underline{\overline{v}}_p^T \underline{v}_q = \sum_{j=0}^{n-1} \omega_n^{-j \cdot p} \omega_n^{j \cdot q} = \sum_{j=0}^{n-1} \omega_n^{j (p-q)} = \omega_n^{-(p-q)} \sum_{j=0}^{n-1} \omega_n^{(j+1)(p - q)} =
$$
$$
\omega_n^{q-p} (\sum_{j=1}^{n-1} \omega_n^{j(p-q)} + \omega_n^{n(p-q)} ) =
\omega_n^{q-p} (\sum_{j=0}^{n-1} \omega_n^{j(p-q)}) = \omega_n^{q-p} \underline{\overline{v}}_p^T \underline{v}_q \text{ iff }
$$
$$
(1 - \omega_n^{q-p}) \underline{\overline{v}}_p^T \underline{v}_q = 0 \text{.}
$$

> Now observe that, if $q \neq p$, then $\omega_n^{q-p} \neq 1$, hence it must be $\underline{\overline{v}}_p^T \underline{v}_q = 0$.
Conversely, if $p = q$,
$$
\underline{\overline{v}}_p^T \underline{v}_q = \sum_{j=0}^{n-1} \omega_n^{j \cdot 0} = n \text{.}
$$

> **Corollary**: $\overline{F}_n^T F_n = n I_n$. Hence $\frac{1}{\sqrt{n}}\overline{F}_n^T \frac{1}{\sqrt{n}} F_n = I_n$.

**Remark**: the columns of $F_n$ are the eigenvectors of $P$.

---

It follows from the last remark that
$$
P_n = \frac{1}{\sqrt{n}} F_n \Lambda \frac{1}{\sqrt{n}} \overline{F}_n \text{ where } \Lambda = \text{diag}\{ \omega_n^0, ..., \omega_n^{n-1} \} \text{.}
$$

Now we're ready to tackle the initial problem: finding the eigenvalues of $C'$.
Observe that
$$
C' \underline{v}_k = (c_0' I_n + ... + c_{n-1}' P_n^{n-1}) \underline{v}_k =
$$
$$
= (c_0' + c_1' \omega_n^{1 \cdot k} + ... + c_{n-1}' \omega_n^{(n-1) \cdot k}) \underline{v}_k \text{.}
$$

Then every eigenvector of $P$ is an eigenvector of $C'$. Furthermore, since $P$ is diagonalizable, it has $n$ linearly independent eigenvectors, hence it is the same for $C'$: a basis of eigenvectors of $C'$ is $\underline{v}_0, ..., \underline{v}_{n-1}$, and the corresponding eigenvalues are $c_0' + c_1' \omega_n^{1 \cdot 0} + ... + c_{n-1}' \omega_n^{(n-1) \cdot 0}$, ..., $c_0' + c_1' \omega_n^{1 \cdot (n-1)} + ... + c_{n-1}' \omega_n^{(n-1) \cdot (n-1)}$.

Now, let $\underline{c}' = \begin{bmatrix} c_0' & ... & c_{n-1}' \end{bmatrix}^T$.
Then:
$$
F_n \underline{c}' = \begin{bmatrix}
c_0' + c_1' \omega_n^{1 \cdot 0} + ... + c_{n-1}' \omega_n^{(n-1) \cdot 0} \\
... \\
c_0' + c_1' \omega_n^{1 \cdot (n-1)} + ... + c_{n-1}' \omega_n^{(n-1) \cdot (n-1)}
\end{bmatrix}
$$
is the **vector of the eigenvalues of $C'$**, that we denote with $\underline{\lambda}(C')$.

Let's see what happends when we consider the product of two matrices "with the usual shape".

> **Theorem (7)**: let $\underline{s}_0$, ..., $\underline{s}_{n-1}$, be linearly independent eigenvectors of both $A$, and $B$ ($A$, and $B$ are both diagonalizable) s.t.
$$
A \underline{s}_i = \alpha_i \underline{s}_i \text{ and } B \underline{s}_i = \beta_i \underline{s}_i  \text{.}
$$
> Then $\underline{s}_0$, ..., $\underline{s}_{n-1}$ is a basis for all the eigenvectors of $AB$, and $AB \underline{s}_i = \alpha_i \beta_i \underline{s}_i$.

> **Proof**: $A B \underline{s}_i = \beta_i A \underline{s}_i = \alpha_i \beta_i \underline{s}_i$. The proof follows since $AB \in \mathbb{R}^{n \times n}$, and $\underline{s}_0$, ..., $\underline{s}_{n-1}$ are linearly independent.

Now consider $C'$, and $D'$.
By what we have seen before, $\underline{v}_0$, ..., $\underline{v}_{n-1}$, are eigenvectors of both $C'$, and $D'$.
Then, by theorem (7),
$$
\underline{\lambda} (C' D') = \underline{\lambda} (C') \cdot^* \underline{\lambda} (D') = F_n \underline{c}' \cdot^* F_n \underline{d}' \text{.} 
$$

But also, from what we have seen before, $C' D'$ is the matrix generated by $\underline{c} \circledast \underline{d}$, hence $\underline{\lambda}(C' D') = F_n (\underline{c} \circledast \underline{d})$.

---

It follows that:
$$
F_n(\underline{c} \circledast \underline{d}) = F_n \underline{c} \cdot^* F_n \underline{d}
$$
which is known as the **convolution rule**.

**Remark**: thanks to the so-called FFT (Fast Fourier Transform) algorithm, we can compute the result of the product $F \underline{a}$ in $O(n \log n)$, then:
- computing $\underline{\lambda}(C'D')$ as $F_n (\underline{c}' \circledast \underline{d}')$ requires $O(n^2)$ operations to compute $\underline{c}' \circledast \underline{d}'$ (_see the formula that we derived at the beginning for $(\underline{c} \circledast \underline{d})_k$_), and then $O(n \log n)$ operations for the product $F_n (\underline{c}' \circledast \underline{d}')$, for a total of $O(n^2 + n \log n) = O(n^2)$ operations;
- computing $F_n \underline{c}'$, and $F_n \underline{d}'$ requries $O(n \log n)$ for each product, then the componentwise product $F_n \underline{c}' \cdot^* \underline{d}'$ is $O(n)$, for a total of $O(n \log n)$ operations.

## Generalizing linear ("standard") convolutions

Let's generalize the definition of convultion to vectors of different dimensions.
- Given two vectors
$$
\underline{c} = \begin{bmatrix}
c_0 \\
... \\
c_{n-1}
\end{bmatrix} \text{ and }
\underline{d} = \begin{bmatrix}
d_0 \\
... \\
d_{m-1}
\end{bmatrix}
$$
> where $n, m \in \mathbb{N}^+$, the **convolution** $\underline{c} * \underline{d}$ is a vector with $n+m-1$ components whose $k$-th component is
$$
(\underline{c} * \underline{d})_k = \sum_{\begin{matrix}
i + j = k \\
i \in \{ 0, ..., n-1 \} \\
j \in \{ 0, ..., m-1 \}
\end{matrix}} c_i d_i 
$$
> with $k \in \{ 0, ..., n+m-2 \}$.

Through the following lemma we will rewrite the expression for the $k$-th component of the convolution between $\underline{c}$ and $\underline{d}$.

> **Lemma (1)**:
$$
\{ (i, j) | i \in \{ 0, ..., n-1 \}, j \in \{ 0, ..., m-1 \}, i+j=k \} =
$$
$$
= \{ (i, k-i) | i \in \{ \max(0, k-m+1), ..., \min(k, n-1) \} \}
$$
> for every $n, m \in \mathbb{N}^+$, $k \in \{ 0, ..., n+m-2 \}$.

---

> **Proof**: let $i \in \{ 0, ..., n-1 \}$, $j \in \{ 0, ..., m-1 \}$ s.t. $i+j = k$. 
Then $j = k - i$. Since $i \in \{ 0, ..., n-1 \}$, then $0 \leq i \leq n-1$. Furthermore, since $-m+1 \leq -j \leq 0$, hence $k-m+1 \leq i = k-i \leq k$.
By joining the two chains of inequalities $\max(0, k-m+1) \leq i \leq \min(n-1, k)$.

> Conversely, let $(i, k-i)$ with $i \in \{ \max(0, k-m+1), ..., \min(k, n-1) \}$. Let $j = k-i$. Clearly $i+j=k$. Since $\max(0, k-m+1) \leq i \leq \min(k, n-1)$, then $0 \leq i \leq n-1$, and $k-m+1 \leq i \leq k$, which implies $0 \leq j = k-i \leq m-1$.

Lemma (1) implies that:
$$
(\underline{c} * \underline{d})_k = \sum_{i = \max(0, k-m+1)}^{\min(k, n-1)} c_i d_{k-i} \text{.}
$$

Let's generalize the concept of a toeplitz matrix to a $m \times n$ matrix.

- Let $m, n \in \mathbb{N}^+$,
$$
\underline{c} = \begin{bmatrix}
c_0 \\
... \\
c_{m-1}
\end{bmatrix} \text{ and } \underline{r} = \begin{bmatrix}
r_0 \\
... \\
r_{n-1}
\end{bmatrix}
$$
> with $c_0 = r_0$. We say that $T \in \mathbb{R}^{m \times n}$ is a **toeplitz matrix** iff
$$
T(i, j) = \begin{cases}
c_0 = r_0 \text{ if } i = j = 0 \\
c_i \text{ if } j = 0, i \neq 0 \\
r_j \text{ if } i = 0, j \neq 0 \\
c_{i-j} \text{ if } i \geq j > 0 \\
r_{j-i} \text{ if } j > i > 0
\end{cases} \text{.}
$$

**Remark**: the definition above implies that a toeplitz matrix is defined by its first row and column since all the elements along the main and secondary diagonals are equal.
That is:
$$
T = \begin{bmatrix}
c_0 & r_1 & r_2 & ... & ... & r_{n-1} \\
c_1 & c_0 & r_1 & r_2 & ... & ... \\
c_2 & c_1 & c_0 & r_1 & ... & ... \\
... & c_2 & c_1 & c_0 & ... & ... \\
... & ... & ... & ... & ... & ... \\
c_{m-1} & ... & ... & ... & ... & ...
\end{bmatrix} \text{.}
$$

---

Let
$$
\underline{k} = \begin{bmatrix}
k_0 \\
... \\
k_{n-1}
\end{bmatrix} \text{, } \underline{v} = \begin{bmatrix}
v_0 \\
... \\
v_{m-1}
\end{bmatrix} \text{ where } n \leq m \text{.}
$$
We want to $\underline{k} * \underline{v}$ through a toeplitz matrix.
Let:
$$
\underline{c} = \begin{bmatrix}
k_0 \\
... \\
k_{n-1} \\
\underline{0}_{m-1}
\end{bmatrix} \in \mathbb{R}^{n+m-1} \text{, }
\underline{r} = \begin{bmatrix}
k_0 \\
\underline{0}_m
\end{bmatrix} \in \mathbb{R}^m \text{.}
$$

Let $T \in \mathbb{R}^{(n+m-1) \times m}$ be the toeplitz matrix induced by $\underline{c}$, and $\underline{r}$.
By definition of the matrix product, the $i$-th element of the vector $T \underline{v} \in \mathbb{R}^{n+m-1}$ is
$$
(T \underline{v})(k) = \sum_{j=0}^{m-1} T(k,j) v_j \text{.}
$$

If $k \geq m-1$, then
$$
\sum_{j=0}^{m-1} T(k, j) v_j= \sum_{j=0}^{m-1} c_{k-j} v_j = \sum_{i=k-m+1}^k c_i v_{k-i} = \sum_{i = \max(0, k-m+1)}^k c_i v_{k-i} =
$$

$$
= \sum_{i = \max(0, k-m+1)}^{n-1} c_i v_{k-i} + \sum_{i = n}^k c_i v_{k-i} \text{ (since } m \geq n \text{ then } k \geq m-1 \geq n-1 \text{)} =
$$

$$
= \sum_{\max(0, k-m+1)}^{\min(k, n-1)} c_i v_{k-i} + \sum_{i=n}^k c_i v_{k-i} = \sum_{\max(0, k-m+1)}^{\min(k, n-1)} k_i v_{k-i} + \sum_{i=n}^k 0 \cdot v_{k-i} = (\underline{k} * \underline{v})_k \text{.}
$$

If $k < m-1$, then
$$
\sum_{j=0}^{m-1} T(k,j) v_j = \sum_{j=0}^k T(k, j) v_j + \sum_{j=k+1}^{m-1} T(k, j) v_j = \sum_{j=0}^k c_{k-j} v_j + \sum_{j=k+1}^{m-1} r_{j-k} v_j =
$$

$$
= \sum_{j=0}^k c_{k-j} v_j + \sum_{j=k+1}^{m-1} 0 \cdot v_j = \sum_{i=0}^k c_i v_{k-i} = \sum_{i = \max(0, k-m+1)}^{\min(k, n-1)} k_i v_{k-i} = (\underline{k} * \underline{v})_k \text{.}
$$

We proved that:
$$
T \underline{v} = \underline{k} * \underline{v} \text{.}
$$

---

## Generalizing circular convolutions

The definition of circular convolution is extended to $\underline{k} \in \mathbb{R}^n$ and $\underline{v} \in \mathbb{R}^m$ of different sizes (with $n < m$) by making $\underline{k}$ of the same size of $\underline{v}$ through zero padding:
$$
\underline{\tilde{k}} = \begin{bmatrix}
\underline{k} \\
\underline{0}_{m-n}
\end{bmatrix} \text{.}
$$

That is:
$$
(\underline{k} \circledast \underline{v})_i = (\underline{\tilde{k}} \circledast \underline{v})_i \text{ for } i \in \{ 0, ..., m-1 \} \text{.}
$$

From what we've seen at the beginning:
$$
(\underline{\tilde{k}} \circledast \underline{v})_i = \begin{cases}
\sum_{j=0}^i \tilde{k}_j v_{i-j} + \sum_{j = i+1}^{m-1} \tilde{k}_j v_{i+m-j} \text{ if } i \in \{ 0, ..., m-2 \} \\
\sum_{j=0}^{m-1} \tilde{k}_j v_{i-j} \text{ if } i = m-1
\end{cases} \text{.}
$$

Now let $i \geq n-1$, $i < m-1$, then, if $j \geq i +1 \geq n$, it follows that $\tilde{k}_j = 0$.
Hence:
$$
(\underline{\tilde{k}} \circledast \underline{v})_i = \sum_{j=0}^{n-1} \tilde{k}_j v_{i-j} + \sum_{j=n}^i 0 \cdot v_{i-j} + \sum_{j=i+1}^{m-1} 0 \cdot v_{i+m-j} = \sum_{j=0}^{n-1} k_j v_{i-j} =
$$

$$
= \sum_{j = \max(0, i-m+1)}^{\min(i, n-1)} k_j v_{i-j} = (\underline{k} * \underline{v})_i \text{.}
$$

Analogously $(\underline{\tilde{k}} \circledast \underline{v})_{m-1} = (\underline{k} * \underline{v})_{m-1}$.

That is:
$$
(\underline{\tilde{k}} \circledast \underline{v})_i = (\underline{k} * \underline{v})_i \text{ for every } i \in \{ n-1, ..., m-1 \} \text{.}
$$

- We define **valid** this "_portion_" of the circular convolution which is equal to the linear one. The remaing portion of the circular convolution is known as **boundary layer**.
