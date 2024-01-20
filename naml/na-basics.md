---
theme: summary
---
# Numerical analysis basics

<div class="author">

Cristiano Migali

</div>

---

## Methods

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
