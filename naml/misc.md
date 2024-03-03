---
marp: true
theme: summary
---
# Miscellaneous

<div class="author">

Cristiano Migali

</div>

---

## Methods & algorithms

### Power method

- Let $A \in \mathbb{R}^{n \times n}$. Let $\lambda_1, ..., \lambda_k$ be the (distinct) eigenvalues of $A$. We say the $\lambda_1$ is the **dominant eigenvalue of $A$** iff $|\lambda_1| > |\lambda_i|$ for every $i \in \{ 2, ..., k \}$.
The eigenvectors related to $\lambda_1$ are called **dominant eigenvectors of $A$**.

> **Remark**: not every matrix has a dominant eigenvector. For example:
$$
A = \begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix} \text{.}
$$

The **power method** allows to approximate numerically a dominant eigenvector of $A$ (given that some hypotheses are satisfied). The iteration rule is:
$$
\underline{x}^{(k)} = \frac{A \underline{x}^{(k-1)}}{||A \underline{x}^{(k-1)}||} \text{.}
$$

1. $\underline{x}^{(k)} = \frac{A^k \underline{x}^{(0)}}{||A^k \underline{x}^{(0)}||}$.

> **Proof**: the base case follows directly from the iteration rule.

> Inductive step: let $k > 1$.
$$
\underline{x}^{(k)} = \frac{A \underline{x}^{(k-1)}}{||A \underline{x}^{(k-1)}||} = \frac{A \frac{A^{k-1} \underline{x}^{(0)}}{||A^{k-1} \underline{x}^{(0)}||}}{||A \frac{A^{k-1} \underline{x}^{(0)}}{||A^{k-1} \underline{x}^{(0)}||}||} = \frac{||A^{k-1} \underline{x}^{(0)}||}{||A^{k-1} \underline{x}^{(0)}||} \frac{A^k \underline{x}^{(0)}}{||A^k \underline{x}^{(0)}||} = \frac{A^k \underline{x}^{(0)}}{||A^k \underline{x}^{(0)}||} \text{.}
$$

2. Let $A \in \mathbb{R}^{n \times n}$ be a diagonalizable matrix. Let $\underline{v}_1, ..., \underline{v}_n$ be a basis of eigenvectors of $A$ with **norm 1**. Let $\underline{x}^{(0)} = \alpha_1 \underline{v}_1 + ... + \alpha_n \underline{v}_n$ with $\alpha_1 \neq 0$. Assume that $\underline{v}_1$ is a dominant eigenvector and no other $\underline{v}_i$ with $i \in \{ 2, ..., n \}$ is. (_Observe that, if the dimension of the eigenspace to which $\underline{v}_1$ belongs is greater than 1, then there will be at least another dominant eigenvector in the basis. For the purpose of the proof we can sum all these eigenvectors together with the relative coefficients $\alpha$ and consider them as one: $\underline{v}_1' = \alpha_1 \underline{v}_1 + ... + \alpha_h \underline{v}_h, \alpha_1' = 1$_).
Then $\underline{x}^{(k)}$ "approaches" (it can oscillate without converging to any vector) $\underline{v}_1$.

> **Proof**: From 1:
$$
\underline{x}^{(k)} = \frac{A^k \underline{x}^{(0)}}{||A^k \underline{x}^{(0)}||} = \frac{\alpha_1 \lambda_1^k \underline{v}_1 + ... + \alpha_n \lambda_n^k \underline{v}_k}{|| \alpha_1 \lambda_1^k \underline{v}_1 + ... + \alpha_n \lambda_n^k \underline{v}_k ||} =
$$

---

$$
= \frac{\alpha_1 \lambda_1^k}{|\alpha_1 \lambda_1^k|} \frac{\underline{v}_1 + ... + \frac{\alpha_n}{\alpha_1} (\frac{\lambda_n}{\lambda_1})^k \underline{v}_n}{||\underline{v}_1 + ... + \frac{\alpha_n}{\alpha_1} (\frac{\lambda_n}{\lambda_1})^k \underline{v}_n||} \text{.}
$$

> Since $\lambda_1$ is a dominant eigenvector: $(\frac{\lambda_i}{\lambda_1})^k \underline{v}_i \rightarrow \underline{0}_n$ for every $i \in \{ 2, ..., k \}$.
Then $\underline{v}_1 + ... + \frac{\alpha_n}{\alpha_1} (\frac{\lambda_n}{\lambda_1})^k \underline{v}_n \rightarrow \underline{v}_1$, and $||\underline{v}_1 + ... + \frac{\alpha_n}{\alpha_1} (\frac{\lambda_n}{\lambda_1})^k \underline{v}_n|| \rightarrow ||\underline{v}_1|| = 1$.
Finally $\frac{\alpha_1 \lambda_1^k}{|\alpha_1 \lambda_1^k|} \in \{ -1, 1 \}$. Note that both $\underline{v}_1$ and $-\underline{v}_1$ are dominant eigenvectors.

> **Remark**: from the dominant eigenvector we can derive the corresponding eigenvalue through the rayleigh quotient.

> **Remark**: by applying the power method to $A^{-1}$ we can find an eigenvector of $A$ associated with the smallest eigenvalue in absolute value. (_Remember that the eigenvalues of $A^{-1}$ are $\frac{1}{\lambda}$_).

> **Remark**: by applying the power method to $(A - \alpha I)^{-1}$ we can find an eigenvector of $A$ associated with the eigenvalue closest to $\alpha$. (_Remember that the eigenvalues of $A - \alpha I$ are $\lambda - \alpha$_). This variant is known as the **power method with shift**.

### QR iteration

The **QR iteration** is an algorithm used to find the eigenvalues of a matrix $A \in \mathbb{R}^{n \times n}$ by repeadetly applying the QR factorization. It works as follows:
let $A_0 = A = Q_0 R_0$, then we apply the following iteration rule:
$$
A_i = Q_{i-1}^T A_{i-1} Q_{i-1} \text{ where } A_{i-1} = Q_{i-1}R_{i-1} \text{.}
$$

Note that $A_i = Q_{i-1}^T Q_{i-1} R_{i-1} Q_{i-1} = R_{i-1} Q_{i-1}$.

By how the iteration rule is defined (_remembering what it means for a matrix to be orthogonal_), all the $A_i$ are similar, and so they have the same eigenvalues.
Under certain conditions the matrices $\{ A_i \}$ converge to a triangular matrix. Then it is trivial to calculate the eigenvalues of $A$ (_they correspond to the diagonal of the limit matrix_).

### Singular Value Thresholding (SVT)

We will see an algorithm to solve the **matrix completion** problem, which is stated as follows: let $X \in \mathbb{R}^{n \times p}$ with $r(X) \ll \min(n,p)$. Suppose that we know only the elements $x_{ij}$ of $X$ for $(i,j) \in \Omega$. We want to reconstruct $X$ starting from the known data. Since $r(X)$ is small by hypothesis, we can try to predict the missing pieces through linear combinations of those which are known.
An ideal estimatore of $X$ is:
$$
\hat{X}_{\text{id}} = {\arg\min}_{Z \in \mathbb{R}^{n \times p}, z_{ij} = x_{ij} \forall (i,j) \in \Omega} r(Z) \text{.}
$$

---

Unfortunately $\hat{X}_{\text{id}}$ is very hard to compute: the **rank is not a convex function**.
For example, let $t \in (0, 1)$:
$$
r(t \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} + (1-t) \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}) = r(\begin{bmatrix} t & 0 \\ 0 & 1-t \end{bmatrix}) = 2 > 1 = t + (1-t) =
$$

$$
= t \cdot r(\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}) + (1-t) \cdot r(\begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}) \text{.}
$$

We need to introduce a "practical" estimator. For this purpose, let's define the nuclear norm of a matrix.

- Let $A \in \mathbb{R}^{m \times n}$. The **nuclear norm of $A$** is:
$$
||A||_* = \sum_{i=1}^{r(A)} \sigma_i(A) \text{.}
$$

> **Remark**: being a norm, the **nuclear norm is convex**. (_We're omitting the proof that the nuclear norm is a norm, of course the name is not a valid argument_).

The practical estimator is the following:
$$
\hat{X} = {\arg\min}_{Z \in \mathbb{R}^{n \times p}, z_{ij} = x_{ij} \forall (i,j) \in \Omega} ||Z||_* \text{.}
$$

The **Singular Value Thresholding** (**SVT**) algorithm converges to $\hat{X}$:

<div class="algorithm">

1. $\hat{X} \gets O_{n \times p}$
1. for every $(i,j) \in \Omega$:
1. &emsp; $\hat{x}_{ij} \gets x_{ij}$
1. do:
1. &emsp; $\hat{X}_{\text{old}} \gets \text{copy}(\hat{X})$
1. &emsp; $U, \Sigma, V^T \gets \text{svd}(\hat{X})$
1. &emsp; for $i$ from $1$ to $r(\hat{X})$:
1. &emsp; &emsp; if $\sigma_i(\hat{X}) \leq \tau$:
1. &emsp; &emsp; &emsp; $\sigma_i(\hat{X}) \gets 0$
1. &emsp; $\hat{X} \gets U \Sigma V^T$
1. &emsp; for every $(i,j) \in \Omega$:
1. &emsp; &emsp; $\hat{x}_{ij} \gets x_{ij}$
1. while $||\hat{X} - \hat{X}_{\text{old}}||_F < \epsilon$

</div>

$\tau$ is a **threshold parameter**, $\epsilon$ is a **tolerance parameter**.
Observe that the algorithm is **non monotone** if we consider $r(\hat{X}^{(k)})$ at every iteration $k$.

---

### Page rank

Consider $n$ websites which link one to the other. We can model them through a graph where each node represents a website and a directed edge from node $i$ to node $j$ means that the website $i$ links to the website $j$.
We want to find the **"most important" websites** among the $n$. In particular we say that a website is important if many important websites link to it. Our problem formulation is recursive: we defined important websites in terms of important websites. We will solve this issue through the following redefinition: imagine to be at website $i$, then you select uniformly one of the websites linked by $i$ and navigate to it. By iterating this process we produce a so-called random-walk over the network. The idea is the following: we start with a certain probability of being in each of the websites, then we compute how the probabilities change after the first step and interate until convergence.
The websites with the greatest associated probability at the end are the ones that we assume to be most important.
In order to compute the final probability distribution we need to introduce a data structure: the adjacency matrix $\hat{A}$ of a graph, defined as:
$$
\hat{a}_{ij} = \begin{cases}
1 \text{ if there is an arc from node } i \text{ to node } j \\
0 \text{ otherwise}
\end{cases} \text{.}
$$
From $\hat{A}$ we compute the matrix $A$ with columns normalized to 1 in 1-norm:
$$
A = \begin{bmatrix}
\frac{\underline{\hat{a}}_1}{||\underline{\hat{a}}_1||_1} & ... &
\frac{\underline{\hat{a}}_n}{||\underline{\hat{a}}_n||_1}
\end{bmatrix} \text{.}
$$

Let $P(\pi_j^{(k)})$ be the probability of being at the website $j$ at the step $k$.
Then
$$
a_{ij} = P(\pi_i^{(k+1)}|\pi_j^{(k)})
$$
since we assumed to select the next website uniformly.
Let
$$
\underline{\pi}^{(k)} = \begin{bmatrix}
P(\pi_i^{(k)}) \\
... \\
P(\pi_n^{(k)})
\end{bmatrix} \text{,}
$$
then
$$
A \underline{\pi}^{(k)} = \begin{bmatrix}
\sum_{j=1}^n P(\pi_1^{(k+1)}|\pi_j^{(k)})P(\pi_j^{(k)}) \\
... \\
\sum_{j=1}^n P(\pi_n^{(k+1)}|\pi_j^{(k)})P(\pi_j^{(k)})
\end{bmatrix} = \underline{\pi}^{(k+1)} \text{.}
$$
Reaching convergence means finding $\underline{\pi}$ s.t. $||\underline{\pi}||_1 = 1$, and $A \underline{\pi} = \underline{\pi}$.

---

That is, $\underline{\pi}$ is an eigenvector of $A$ with eigenvalue 1.

Observe that $A$ is a special matrix: it is a **stochastic matrix** which is a particular kind of **non-negative matrix** (that is, a matrix with non-negative entries).
Assuming that the initial graph is strongly connected, the theory of non-negative and stochastic matrices guarantees that 1 is an eigenvalue of $A$ and any other eigenvalue of $A$ is smaller than 1 in absolute value.

**Remark**: If $||\underline{x}||_1 = 1$, then $||A \underline{x}||_1 = 1$.
For:
$$
||A \underline{x}||_1 = ||x_1 \underline{a}_1 + ... + x_n \underline{a}_n||_1 = x_1 ||\underline{a}_1||_1 + ... + x_n || \underline{a}_n ||_1 = x_1 \cdot 1 + ... + x_n \cdot 1 = ||\underline{x}||_1 = 1 \text{.}
$$

Then we can determine $\underline{\pi}$ through the power method. Furthermore, because of what we've just remarked, we don't need to renormalize while applying the method.

### Numerical derivatives

#### The Decentered method

Assume that we want to differentiate numerically a function $f$ at $x \in \mathbb{R}$; the **decentered method** consists in the following computation:
$$
D_1(h) = \frac{f(x+h)-f(x)}{h} = \frac{1}{h}[f(x) + f'(x)h + \frac{1}{2}f''(x)h^2 + \frac{1}{3!}f'''(x)h^3 + ...
$$

$$
- f(x)] = f'(x) + \frac{1}{2}f''(x)h + \frac{1}{3!}f'''(x)h^2 + ... = f'(x) + O(h) \text{.}
$$

#### The Centered 

Assume that we want to differentiate numerically a function $f$ at $x \in \mathbb{R}$; the **centered method** consists in the following computation:
$$
D_2(h) = \frac{f(x+h)-f(x-h)}{2h} = \frac{1}{2h}[f(x) + f'(x)h + \frac{1}{2!}f''(x)h^2 + \frac{1}{3!}f'''(x)h^3 + ... 
$$

$$
-f(x)+f'(x)h-\frac{1}{2}f''(x)h^2 + \frac{1}{3!}f'''(x)h^3 - ...] =
$$

$$
= \frac{1}{2h}[2f'(x)h + \frac{2}{3!}f'''(x)h^3 + ...] = f'(x)+ \frac{f'''(x)}{3!}h^2 + ... = f'(x) + O(h^2) \text{.}
$$

These methods introduce the following types of error:
- **truncation error**: the term $O(h)$ in $D_1$ and $O(h^2)$ in $D_2$ due to the fact that both the functions are not equal to $f'$;
- **roundoff error**: due to the fact that numbers are represented using FP arithmetic that can lead to problems when subtracting two numbers which are close to each other or when summing numbers with very dfferent order of magnitude.

---

Both thse errors contribute to the **approximation error**, which is the difference between the computed value and the exact one of $f'(x)$ (which can oscillate in function of $h$).
